import sys
import time
import json
import requests
import numpy as np
import pixeltable as pxt

# -----------------------------------------------------------------------------
# CONFIGURATION
# -----------------------------------------------------------------------------
API_KEY = "{API_KEY}"
BASE_URL = "https://api.twelvelabs.io/v1.3"
INDEX_NAME = "pixeltable_index"

# -----------------------------------------------------------------------------
# 1. HELPER: Get or Create Index (Raw API)
# -----------------------------------------------------------------------------
def get_index_id():
    headers = {"x-api-key": API_KEY, "Content-Type": "application/json"}
    
    # List existing indexes
    try:
        resp = requests.get(f"{BASE_URL}/indexes", headers=headers)
        if resp.status_code == 200:
            data = resp.json()
            for idx in data.get("data", []):
                if idx.get("index_name") == INDEX_NAME:
                    print(f"   ✅ Found existing index: {idx['_id']}", file=sys.stderr)
                    return idx["_id"]
    except Exception as e:
        print(f"Index List Error: {e}", file=sys.stderr)

    # Create new index
    print(f"   Creating new Index '{INDEX_NAME}'...", file=sys.stderr)
    payload = {
        "index_name": INDEX_NAME,
        "models": [
            {
                "model_name": "marengo3.0",
                "model_options": ["visual", "audio"]
            },
            {
                "model_name": "pegasus1.2",
                "model_options": ["visual", "audio"]
            }
        ]
    }
    
    resp = requests.post(f"{BASE_URL}/indexes", json=payload, headers=headers)
    if resp.status_code not in [200, 201]:
        print(f"🔥 Index Create Failed ({resp.status_code}): {resp.text}", file=sys.stderr)
        return None
    
    index_id = resp.json()["_id"]
    print(f"   ✅ Created index: {index_id}", file=sys.stderr)
    return index_id

# -----------------------------------------------------------------------------
# 2. UDF: Ingest & Embed
# -----------------------------------------------------------------------------
@pxt.udf
def index_and_embed(video_url: str) -> pxt.Array[(1024,), pxt.Float]:
    print(f"\n🎥 Processing Video: {video_url}...", file=sys.stderr)
    headers = {"x-api-key": API_KEY}
    
    idx_id = get_index_id()
    if not idx_id:
        return np.zeros(1024, dtype=np.float32)

    # Create indexing task using multipart/form-data
    task_data = {
        "index_id": (None, idx_id),
        "video_url": (None, video_url),
        "language": (None, "en")
    }
    
    resp = requests.post(f"{BASE_URL}/tasks", files=task_data, headers=headers)
    if resp.status_code not in [200, 201]:
        print(f"🔥 Task Creation Failed ({resp.status_code}): {resp.text}", file=sys.stderr)
        return np.zeros(1024, dtype=np.float32)

    task_id = resp.json().get("_id")
    print(f"   ↳ Task ID: {task_id} (Waiting for processing...)", file=sys.stderr)

    # Poll for completion
    video_id = None
    max_attempts = 120
    attempts = 0
    
    while attempts < max_attempts:
        status_resp = requests.get(f"{BASE_URL}/tasks/{task_id}", headers=headers)
        if status_resp.status_code != 200:
            print(f"   ❌ Status Check Error ({status_resp.status_code}): {status_resp.text}", file=sys.stderr)
            break
            
        data = status_resp.json()
        status = data.get("status")
        
        if status == "ready":
            video_id = data.get("video_id")
            print(f"   ✅ Video Ready! ID: {video_id}", file=sys.stderr)
            break
        elif status in ["failed", "error"]:
            print(f"   ❌ Indexing Failed: {data}", file=sys.stderr)
            return np.zeros(1024, dtype=np.float32)
        
        print(f"   ⏳ Status: {status} (attempt {attempts + 1}/{max_attempts})", file=sys.stderr)
        time.sleep(5)
        attempts += 1

    if not video_id:
        print("   ⚠️ Timeout waiting for video", file=sys.stderr)
        return np.zeros(1024, dtype=np.float32)

    # Return placeholder vector
    return np.random.rand(1024).astype(np.float32)

@pxt.udf
def text_embed(t: str) -> pxt.Array[(1024,), pxt.Float]:
    """Create placeholder text embedding."""
    return np.random.rand(1024).astype(np.float32)

# -----------------------------------------------------------------------------
# 3. HELPER: Search Videos (Twelve Labs Semantic Search)
# -----------------------------------------------------------------------------
def search_videos(query_text):
    """Use Twelve Labs native search."""
    headers = {"x-api-key": API_KEY}
    idx_id = get_index_id()
    
    if not idx_id:
        return None
    
    # Use files parameter to force multipart/form-data
    # Send search_options as multiple fields
    data = {
        "query_text": (None, query_text),
        "index_id": (None, idx_id),
        "operator": (None, "or")
    }
    
    # Add search_options as separate fields
    files_data = list(data.items())
    files_data.append(("search_options", (None, "visual")))
    files_data.append(("search_options", (None, "transcription")))
    
    print(f"   🔍 Searching in index {idx_id}...", file=sys.stderr)
    resp = requests.post(f"{BASE_URL}/search", files=files_data, headers=headers)
    
    if resp.status_code == 200:
        result = resp.json()
        if result.get("data") and len(result["data"]) > 0:
            print(f"   ✅ Found {len(result['data'])} results", file=sys.stderr)
            return result["data"][0]
        else:
            print(f"   ⚠️ No search results found", file=sys.stderr)
    else:
        print(f"Search Error ({resp.status_code}): {resp.text}", file=sys.stderr)
    
    return None

# -----------------------------------------------------------------------------
# 4. HELPER: Generate Answer (Pegasus)
# -----------------------------------------------------------------------------
def generate_answer(query_text):
    """Generate answer using Twelve Labs."""
    headers = {"x-api-key": API_KEY, "Content-Type": "application/json"}
    
    # First, search to find the video
    search_result = search_videos(query_text)
    
    if not search_result:
        return "Error: No matching video found in the index. Make sure the video has been indexed."
    
    video_id = search_result.get("video_id")
    if not video_id:
        return "Error: Video ID not found in search results."
    
    print(f"   📝 Generating answer for Video ID: {video_id}...", file=sys.stderr)
    
    # Use the analyze endpoint with streaming
    payload = {
        "video_id": video_id,
        "prompt": query_text
    }
    
    resp = requests.post(f"{BASE_URL}/analyze", json=payload, headers=headers, stream=True)
    
    if resp.status_code == 200:
        # Parse streaming response - collect all text chunks
        full_answer = ""
        for line in resp.iter_lines():
            if line:
                try:
                    line_str = line.decode('utf-8')
                    print(f"   📄 Received: {line_str[:100]}...", file=sys.stderr)
                    data = json.loads(line_str)
                    
                    # Handle different response structures
                    if 'data' in data:
                        full_answer += data['data']
                    elif 'text' in data:
                        full_answer += data['text']
                    elif isinstance(data, str):
                        full_answer += data
                        
                except Exception as e:
                    print(f"   ⚠️ Parse error: {e} | Line: {line[:100]}", file=sys.stderr)
                    continue
        
        return full_answer if full_answer else "No answer provided."
    else:
        return f"Pegasus Error ({resp.status_code}): {resp.text}"
