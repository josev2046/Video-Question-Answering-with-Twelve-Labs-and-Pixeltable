# Multimodal AI Governance: Pixeltable x Twelve Labs

## 1. The Big Picture
The integration represents the transition from Static Data (files in a folder) to Semantic Data (files that know what they contain). 

* Twelve Labs provides the Multimodal Intelligence (The Eyes & Ears).
* Pixeltable provides the Data Infrastructure (The Brain & Memory).

---

## 2. Twelve Labs: The Reasoning Engine
Twelve Labs is a specialized AI platform for video understanding. Unlike standard LLMs that only process text, Twelve Labs uses Multimodal Embeddings.

**Core Concepts:**
* Multimodal Ingestion: It does not just watch the video; it simultaneously analyzes visual frames, audio/speech, and on-screen text (OCR).
* Temporal Grounding: The ability to pinpoint exactly when an event happens (e.g., 00:15 - 00:22).
* Pegasus (Reasoning): A specialized model that can answer complex, nuanced questions about video context, such as "Is this person following safety protocols?" rather than just "Is there a person in the video?"
* Indexing: The process of converting video pixels into a mathematical map that can be searched or questioned instantly.

---

## 3. Pixeltable: The AI Orchestrator
Pixeltable is a Declarative AI Database. It is designed to treat AI models as if they were simple table columns.

**Core Concepts:**
* Declarative Logic: Instead of writing complex loops to process files, you declare a relationship. (e.g., "This column will always be a summary of that video column").
* Computed Columns: These are the live wires of your database. They do not store static data; they store the result of a function. When the input changes, the computed column updates automatically.
* Incremental Computing: Pixeltable is efficient. It remembers what it has already processed. If you add 100 videos but 95 were already indexed, it only triggers the AI for the 5 new ones.
* UDF (User Defined Functions): These are the bridges. They allow you to wrap any external tool (like Twelve Labs) and plug it directly into the database schema.

---

## 4. The Collaborative Workflow
The relationship follows a Trigger-Action pattern:

<img width="1357" height="732" alt="image" src="https://github.com/user-attachments/assets/a6bd1f54-29ed-4e9c-a150-c9d4f03b3f61" />


1. The Event: A Video URL is inserted into a Pixeltable Input Column.
2. The Trigger: Pixeltable detects the new entry and realizes a Computed Column depends on it.
3. The Request: Pixeltable orchestrates the call to Twelve Labs, handling the upload and the waiting period while the video indexes.
4. The Transformation: Twelve Labs returns a complex, unstructured JSON blob. 
5. The Refinement: Pixeltable uses secondary functions to shred that JSON into clean, readable table rows (Decision, Findings, Timestamps).

---

## 5. Why This Matters for Governance
In an Evidence-Based Audit, this duo solves two major problems:

* Auditability: Because Pixeltable is a database, you have a permanent record of why a video was blocked, linked to the exact timestamp provided by Twelve Labs.
* Scalability: Large scale social media monitoring for brand safety is impossible for human teams alone. Twelve Labs watches the video, and Pixeltable organizes the Rejections for a human to review.

---

## 6. Summary of Terms
* Schema: The blueprint of your database (What data are we keeping?).
* Embedding: The AI-readable version of a video.
* Pegasus: The specific Twelve Labs model used for deep reasoning.
* Computed Column: A column that is calculated by an AI model.
* Temporal Evidence: The specific start/end times that prove an AI's claim.
