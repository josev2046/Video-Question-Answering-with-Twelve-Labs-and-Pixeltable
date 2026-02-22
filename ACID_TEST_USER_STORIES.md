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
