### CRAWL

**User Story:** As an AI Researcher, I want to manually upload videos and test natural language queries in the Twelve Labs web playground so that I can validate the model's capabilities before committing engineering resources to build a programmatic pipeline.

**Acceptance Criteria:**

| Criterion | Description |
| :--- | :--- |
| **Ingestion** | User can successfully upload a sample video asset via the browser. |
| **Querying** | User can input text-based questions into the UI. |
| **Validation** | User receives an accurate, timestamped response directly in the interface. |
| **Zero-Code** | The entire process requires no API keys, local environment setup, or code execution. |

---

### WALK

**User Story:** As a Developer, I want to programmatically ingest a video and generate vector embeddings using Pixeltable and Twelve Labs so that I can automatically query the video content and return specific insights to the end-user.

**Acceptance Criteria:**

| Criterion | Description |
| :--- | :--- |
| **Data Structure** | A Pixeltable directory and table are successfully created to store video URLs and metadata. |
| **Automated Indexing** | Inserting a video URL automatically triggers the indexing function to compute embeddings. |
| **Search & Generate** | The system can take a programmatic text prompt, run a native search, and generate a contextual answer. |
| **Console Output** | The console clearly logs progress and prints the final AI-generated answer. |

---

### RUN

**User Story:** As a Global Brand Safety Manager for a Tier-1 Cosmetics Corporation, I want to automatically audit influencer video content against a set of "Zero-Tolerance" safety and relevance triggers, so that I can instantly block off-topic content, flag dangerous physical techniques for review, and reject misleading medical claims without manually watching thousands of hours of footage.

**Acceptance Criteria:**

| Criterion | Description |
| :--- | :--- |
| **Multimodal Context** | The system analyzes visual actions (sharp tools), audio/speech (medical claims), and thematic relevance (culinary) simultaneously. |
| **Binary Logic Triggers** | The AI follows strict "If/Then" triggers (e.g., If Food -> BLOCK) to override model helpfulness bias. |
| **Temporal Evidence** | Every decision is anchored to a specific timestamp (e.g., 00:15s) providing explainability for every BLOCK or REVIEW status. |
| **Automated Reporting** | Pixeltable computed columns "shred" raw AI JSON into a structured dashboard showing Creator, Decision, Findings, and Summary. |

---

### APIs Under the Hood

The system leverages several core Twelve Labs APIs to power these multimodal features across the "Walk" and "Run" phases.

### Phase: WALK (main.py)

In the foundational Q&A script, the focus is on search and generation:

* **Index API (POST /indexes):** Creates the structural container on Twelve Labs to hold video embeddings.
* **Task/Upload API (POST /tasks):** Ingests the video URL to extract multimodal embeddings (visual, audio, speech).
* **Search API (POST /search):** Locates specific, relevant moments within the indexed video based on a text prompt.
* **Generate API (POST /generate):** Uses the Pegasus model to turn retrieved video context into a natural language answer.

### Phase: RUN (app.py & AI_my_functions.py)

In the automated compliance pipeline, the focus shifts to deep reasoning and adversarial instructions:

* **Task/Upload API (POST /tasks):** Manages the batch ingestion of creator submissions into a specialized compliance index.
* **Analyze API (POST /analyze):** This is the core of the Pegasus 1.2 integration. It sends a "Zero-Tolerance" system prompt to the model. Unlike standard search, this performs deep reasoning to evaluate the video against specific brand safety rules.
* **Structured Output:** The Generate/Analyze response is returned as a JSON object, which is then parsed by Pixeltable UDFs to populate the final audit table.
