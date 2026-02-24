# Pixeltable: Infrastructure & multimodal AI 

Pixeltable is a declarative data infrastructure specifically engineered for multimodal AI applications. It unifies data storage, orchestration, and model inference into a single table-based interface, eliminating the need for fragmented pipelines involving separate vector databases and manual glue code.

---

## 1. Core infrastructure architecture
Pixeltable operates as a high-performance orchestration layer atop standard database and storage technologies.

### Architectural components
* **Declarative table interface:** Replaces traditional ETL pipelines with persistent tables where columns can be "computed" via AI models.
* **Incremental update engine:** Automatically tracks data changes. If new rows are added, Pixeltable only executes models on the new entries, ensuring computational efficiency.
* **Hybrid storage:** Structured metadata and model outputs are stored in **PostgreSQL**, while heavy unstructured media (video, audio, images) reside in object storage (S3, B2, or local).
* **Built-in versioning:** Provides automatic data lineage. Every transformation is tracked, allowing for reproducible experiments and audit trails.

---

## 2. Multimodal data handling
Pixeltable treats unstructured media as first-class citizens rather than binary blobs, enabling deep integration with AI workflows.

### Native data types
| Type | Capabilities |
| :--- | :--- |
| `pxt.Image` | Supports native transformations (resizing, filtering) and direct model input. |
| `pxt.Video` | Enables frame-level indexing, temporal analysis, and metadata extraction. |
| `pxt.Audio` | Supports automated transcription and segment-based analysis. |
| `pxt.Document` | Handles PDF parsing and semantic chunking for RAG pipelines. |

### Data iterators (views)
Pixeltable uses **views** to transform high-level media into granular, queryable data:
* **Frame extraction:** Automatically decomposes video into a sequence of image rows at a defined frequency.
* **Document chunking:** Fragments long-form text or PDFs into individual chunks for embedding.
* **Audio segmentation:** Breaks continuous streams into time-stamped snippets for speech-to-text.

---

## 3. Multimodal AI integration
Model inference is integrated directly into the schema definition through **computed columns**.

### The integrated workflow
1.  **Schema definition:** Define columns for raw data (e.g., `Video`).
2.  **Computed columns:** Define columns that invoke models (e.g., `openai.gpt4_vision`).
3.  **Automatic execution:** Upon data ingestion, Pixeltable triggers the necessary model calls and stores the results.
4.  **Vector search:** Generate embeddings within the table. Similarity searches can be performed directly against these columns without external vector synchronisation.

### Efficiency features
* **Automatic caching:** Results of model inferences are cached to prevent redundant API costs or GPU cycles.
* **Provider agnostic:** Supports native integrations with OpenAI, Anthropic, Gemini, Hugging Face, and custom local models (e.g., PyTorch, YOLOX).

---

## 4. Summary for implementation

* **Installation:** `pip install pixeltable`
* **Core philosophy:** Move the logic to the data. Instead of writing scripts to process data, define a table that "knows" how to process itself.
* **Use cases:** Video search engines, automated media tagging, document RAG (retrieval-augmented generation), and multimodal model benchmarking.

---

# Integration of Pixeltable and Twelve Labs

The integration of Pixeltable with Twelve Labs provides a robust framework for developing video-native applications. While Twelve Labs offers the specialised artificial intelligence required to interpret video context, Pixeltable serves as the underlying infrastructure to manage that data at scale.

---

## 1. Unified multimodal representation
Twelve Labs models (such as Marengo and Pegasus) generate a unified embedding space where visual, auditory, and textual information from a video are represented within a single vector.

* **Infrastructure synergy:** Pixeltable stores these high-dimensional embeddings directly alongside the source video files in a unified table. This allows for seamless cross-modal retrieval—such as using a text prompt to locate a specific visual action—through a standard query interface.

## 2. Orchestration and efficiency
Video processing is traditionally computationally intensive and requires fragmented pipelines involving separate storage, frame extraction, and vector databases.

* **Computed columns:** Pixeltable simplifies this by using "computed columns" to invoke Twelve Labs APIs. This ensures that the orchestration of API calls, rate-limiting, and response caching is handled automatically. Consequently, users avoid redundant computational costs and manual "glue code".

## 3. Incremental video indexing
In conventional environments, adding new video content often necessitates manual re-indexing or complex update scripts.

* **Automated data flow:** Pixeltable employs incremental computation. When new video files are ingested into a table, Pixeltable detects the changes and triggers the Twelve Labs indexing process only for the new data. This ensures the search index remains synchronised without manual intervention.

## 4. Enhanced video RAG (retrieval-augmented generation)
Twelve Labs is highly effective at identifying precise temporal segments within extensive video archives.

* **Granular context:** By utilising Pixeltable’s "view" system, users can decompose videos into specific segments or frames. When combined with Twelve Labs' temporal search, this enables video RAG systems to retrieve not just a specific file, but the exact timestamp required to provide context for a large language model (LLM).

---

## Summary of benefits

| Feature | Pixeltable + Twelve Labs advantage |
| :--- | :--- |
| **Search** | Native support for natural language queries across video libraries. |
| **Cost** | Automatic caching of Twelve Labs API responses to prevent duplicate billing. |
| **Scale** | Managed infrastructure that scales from local testing to production S3 environments. |
| **Logic** | Declarative approach: the table schema defines the AI workflow. |
