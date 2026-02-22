### CRAWL

**User Story:** As an AI Researcher, I want to manually upload videos and test natural language queries in the Twelve Labs web playground so that I can validate the model's capabilities before committing engineering resources to build a programmatic pipeline.

**Acceptance Criteria:**

| Criterion | Description |
| :--- | :--- |
| **Ingestion** | User can successfully upload a sample video asset via the browser. |
| **Querying** | User can input text-based questions (e.g., "What is the man searching for?") into the UI. |
| **Validation** | User receives an accurate, timestamped response directly in the interface. |
| **Zero-Code** | The entire process requires no API keys, local environment setup, or code execution. |

---

### WALK

**User Story:** As a Developer, I want to programmatically ingest a video and generate vector embeddings using Pixeltable and Twelve Labs so that I can automatically query the video content and return specific insights to the end-user.

**Acceptance Criteria:**

| Criterion | Description |
| :--- | :--- |
| **Data Structure** | A Pixeltable directory and table are successfully created to store video URLs and metadata. |
| **Automated Indexing** | Inserting a video URL automatically triggers the `index_and_embed` function to compute embeddings. |
| **Search & Generate** | The system can take a programmatic text prompt, run a native search, and generate a contextual answer. |
| **Console Output** | The console clearly logs the progress (Setup, Ingest, Compute, Search) and prints the final AI-generated answer. |

---

### RUN

**User Story:** As a “TRUST EXEC” I want to process a batch of creator video submissions through an automated multimodal intelligence pipeline so that I can instantly generate compliance summaries and approve, block, or flag content without manual review.

**Acceptance Criteria:**

| Criterion | Description |
| :--- | :--- |
| **Batch Processing** | The pipeline can ingest an array of multiple video URLs and their associated creator handles. |
| **Pipeline Triggers** | Pixeltable computed columns automatically trigger compliance analysis, summarization, and decision-making logic for every inserted row. |
| **Decision Engine** | The system accurately assigns a status (APPROVE, BLOCK, or FLAG) based on the findings from the Twelve Labs compliance report. |
| **Audit Logging** | The console outputs a clean, formatted audit table detailing the creator, the final decision with visual icons (✅, ❌, ⚠️), the AI engine used, a summary, and specific policy findings. |

---

### APIs under the hood:

I am making calls to several core Twelve Labs APIs to power these multimodal features. Here is the breakdown of the obvious APIs being invoked during my "Walk" and "Run" phases.

### (`main.py`)

In my foundational Q&A script, I am leveraging Twelve Labs' search and generation capabilities. The underlying API calls for this include:

* **Index API (`POST /indexes`)**: When I set up `PROJECT_NAME`, this creates the structural container (index) on the Twelve Labs platform to hold my video embeddings.
* **Task/Upload API (`POST /tasks` or the newer `POST /assets` + `POST /indexes/{id}/indexed-assets`)**: Triggered by `index_and_embed(videos.url)`. This is where the actual video URL is passed to Twelve Labs to extract and compute the multimodal embeddings (visual, audio, speech, text).
* **Embed API (`POST /embed`)**: Triggered by the `text_embed` function. This takes my text query and turns it into vector embeddings in the exact same latent space as the video (typically using their Marengo model) so that a similarity search can happen.
* **Search API (`POST /search`)**: Used to locate the specific, relevant moments within the video based on my prompt.
* **Generate API (`POST /generate`)**: Triggered by `generate_answer()`. This likely utilizes Twelve Labs' Pegasus model to perform an open-ended analysis, turning the retrieved video context into the final natural language answer to "What is the man searching for?".

---

### (`FINAL_main.py`)

In my automated compliance pipeline, the focus shifts heavily toward batch processing and complex video understanding/reasoning.

* **Task/Upload API (`POST /tasks` / `POST /assets`)**: Used iteratively or asynchronously to ingest my batch of 5 test submissions (`MECCA_Beauty.mp4`, etc.) into the compliance index.
* **Generate API (`POST /generate`)**: This is the star of the `analyze_compliance_live()` function. It uses the Pegasus model for high-level video reasoning. Instead of just searching, I am likely passing a strict system prompt (e.g., "Analyze this video for brand safety, NSFW content, and specific policy violations") and receiving structured text back.
* **(Optional/Likely) Summarize or Generate API**: If `get_summary()` and `get_decision()` aren't just parsing the initial report locally via Python, they might be making secondary calls to the Generate API to condense the complex policy findings into the short 📝 summary and the `APPROVE`/`BLOCK` statuses.
