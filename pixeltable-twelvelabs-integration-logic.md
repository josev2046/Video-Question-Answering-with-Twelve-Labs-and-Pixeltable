# Multimodal AI governance: Pixeltable x Twelve Labs

## 1. The big picture
The integration represents the transition from **static data** (files in a folder) to **semantic data** (files that maintain awareness of their content).

* **Twelve Labs** provides the multimodal intelligence (the eyes and ears).
* **Pixeltable** provides the data infrastructure (the brain and memory).

---

## 2. Twelve Labs: The reasoning engine
Twelve Labs is a specialised AI platform for video understanding. Unlike standard LLMs that process text in isolation, Twelve Labs utilises **multimodal embeddings**.

**Core concepts:**
* **Multimodal ingestion:** It does not simply view the video; it simultaneously analyses visual frames, audio/speech, and on-screen text (OCR).
* **Temporal grounding:** The ability to pinpoint exactly when an event occurs (e.g., 00:15 - 00:22).
* **Pegasus (reasoning):** A specialised model capable of answering complex, nuanced questions about video context (e.g., "Is this person following safety protocols?" rather than just "Is there a person in the video?").
* **Indexing:** The process of converting video pixels into a mathematical map that can be queried instantly.

---

## 3. Pixeltable: The AI orchestrator
Pixeltable is a declarative AI database designed to treat AI models as if they were simple table columns.

**Core concepts:**
* **Declarative logic:** Instead of writing complex loops to process files, a relationship is declared (e.g., "This column will always be a summary of that video column").
* **Computed columns:** These act as the "live wires" of the database. They store the result of a function rather than static data. When the input changes, the computed column updates automatically.
* **Incremental computing:** Pixeltable maintains efficiency by tracking processed data. If 100 videos are added but 95 are already indexed, inference is triggered only for the 5 new entries.
* **User-defined functions (UDFs):** These serve as bridges, allowing external tools (such as Twelve Labs) to be wrapped and plugged directly into the database schema.

---

## 4. The collaborative workflow
The relationship follows a trigger-action pattern:

<img width="1357" height="732" alt="image" src="https://github.com/user-attachments/assets/a6bd1f54-29ed-4e9c-a150-c9d4f03b3f61" />

1.  **The event:** A video URL is inserted into a Pixeltable input column.
2.  **The trigger:** Pixeltable detects the new entry and identifies a dependency in a computed column.
3.  **The request:** Pixeltable orchestrates the call to Twelve Labs, managing the upload and indexing latency.
4.  **The transformation:** Twelve Labs returns a complex, unstructured JSON object.
5.  **The refinement:** Pixeltable utilises secondary functions to parse that JSON into structured, readable table rows (decisions, findings, timestamps).

---

## 5. Importance for governance
In an evidence-based audit, this combination addresses two major challenges:

* **Auditability:** As a database, Pixeltable maintains a permanent record of why a video was flagged, linked to the exact timestamp provided by Twelve Labs.
* **Scalability:** Large-scale social media monitoring for brand safety is unmanageable for human teams alone. Twelve Labs analyses the video, while Pixeltable organises the rejections for human review.

