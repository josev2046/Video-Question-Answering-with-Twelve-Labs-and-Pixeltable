import pixeltable as pxt
from my_functions import index_and_embed, text_embed, generate_answer
import time

PROJECT_NAME = "dokumenta_video"

def main():
    print(f"🚀 Starting {PROJECT_NAME}...")
    
    # 1. SETUP
    pxt.drop_dir(PROJECT_NAME, force=True)
    pxt.create_dir(PROJECT_NAME)
    
    videos = pxt.create_table(f'{PROJECT_NAME}.index', {
        'video': pxt.Video,
        'url': pxt.String
    })
    
    # 2. INGEST
    video_url = 'https://github.com/pixeltable/pixeltable/raw/main/docs/resources/The-Pursuit-of-Happiness.mp4'
    videos.insert([{'video': video_url, 'url': video_url}])
    
    # 3. Add a computed column that will trigger indexing
    print("🧠 Adding embedding column (this will trigger Twelve Labs indexing)...")
    videos.add_computed_column(embedding=index_and_embed(videos.url))
    
    # 4. Force computation by selecting the embedding column
    print("\n⏳ Computing embeddings (this may take several minutes)...")
    result = videos.select(videos.url, videos.embedding).collect()
    
    print("\n✅ Indexing complete!")
    
    # 5. Now add the embedding index for Pixeltable searches
    videos.add_embedding_index(
        'url', 
        embedding=index_and_embed,
        string_embed=text_embed
    )
    
    # 6. Wait a moment for everything to settle
    time.sleep(2)
    
    # 7. SEARCH & GENERATE
    query_text = "What is the man searching for?"
    print(f"\n🤖 Asking Twelve Labs about: '{query_text}'")
    
    # Use Twelve Labs native search + generate
    answer = generate_answer(query_text)
    
    print("\n" + "="*40)
    print(f"QUESTION: {query_text}")
    print(f"TWELVE LABS ANSWER: {answer}")
    print("="*40)

if __name__ == "__main__":
    main()
