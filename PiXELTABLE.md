# Pixeltable: Infrastructure & Multimodal AI Cheatsheet

Pixeltable is a declarative data infrastructure specifically engineered for multimodal AI applications. It unifies data storage, orchestration, and model inference into a single table-based interface, eliminating the need for fragmented pipelines involving separate vector databases and manual glue code.

---

## 1. Core Infrastructure Architecture
Pixeltable operates as a high-performance orchestration layer atop standard database and storage technologies.

### Architectural Components
* **Declarative Table Interface:** Replaces traditional ETL pipelines with persistent tables where columns can be "computed" via AI models.
* **Incremental Update Engine:** Automatically tracks data changes. If new rows are added, Pixeltable only executes models on the new entries, ensuring computational efficiency.
* **Hybrid Storage:** Structured metadata and model outputs are stored in **PostgreSQL**, while heavy unstructured media (Video, Audio, Images) reside in object storage (S3, B2, or Local).
* **Built-in Versioning:** Provides automatic data lineage. Every transformation is tracked, allowing for reproducible experiments and audit trails.

---

## 2. Multimodal Data Handling
Pixeltable treats unstructured media as first-class citizens rather than binary blobs, enabling deep integration with AI workflows.

### Native Data Types
| Type | Capabilities |
| :--- | :--- |
| `pxt.Image` | Supports native transformations (resizing, filtering) and direct model input. |
| `pxt.Video` | Enables frame-level indexing, temporal analysis, and metadata extraction. |
| `pxt.Audio` | Supports automated transcription and segment-based analysis. |
| `pxt.Document` | Handles PDF parsing and semantic chunking for RAG pipelines. |

### Data Iterators (Views)
Pixeltable uses **Views** to transform high-level media into granular, queryable data:
* **Frame Extraction:** Automatically decomposes Video into a sequence of Image rows at a defined frequency.
* **Document Chunking:** Fragments long-form text or PDFs into individual chunks for embedding.
* **Audio Segmentation:** Breaks continuous streams into time-stamped snippets for speech-to-text.

---

## 3. Multimodal AI Integration
Model inference is integrated directly into the schema definition through **Computed Columns**.

### The Integrated Workflow
1.  **Schema Definition:** Define columns for raw data (e.g., `Video`).
2.  **Computed Columns:** Define columns that invoke models (e.g., `openai.gpt4_vision`).
3.  **Automatic Execution:** Upon data ingestion, Pixeltable triggers the necessary model calls and stores the results.
4.  **Vector Search:** Generate embeddings within the table. Similarity searches can be performed directly against these columns without external vector synchronisation.

### Efficiency Features
* **Automatic Caching:** Results of model inferences are cached to prevent redundant API costs or GPU cycles.
* **Provider Agnostic:** Supports native integrations with OpenAI, Anthropic, Gemini, Hugging Face, and custom local models (e.g., PyTorch, YOLOX).

---

## 4. Summary for Implementation

* **Installation:** `pip install pixeltable`
* **Core Philosophy:** Move the logic to the data. Instead of writing scripts to process data, define a table that "knows" how to process itself.
* **Use Cases:** Video search engines, automated media tagging, Document RAG (Retrieval-Augmented Generation), and multimodal model benchmarking.
