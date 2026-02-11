# Twelve Labs: Technology & Market Overview

## 1. What is Twelve Labs?
Twelve Labs is an AI infrastructure startup building **multimodal foundation models** specifically designed for video understanding. unlike traditional models that treat video as a sequence of static images, Twelve Labs builds models that understand video holistically—combining visuals, audio, speech, and on-screen text—to allow computers to "see" and "listen" the way humans do.

### Core Value Proposition
* **Searchable Video:** Making video data searchable via natural language (e.g., "find the moment the car turns left in the rain") without manual tagging.
* **Programmable Video:** Allowing developers to write software that can query, summarize, and extract data from video files automatically.

---

## 2. Core Technology & Models
Twelve Labs uses **vector embeddings** to convert video content into mathematical coordinates. This enables semantic understanding rather than keyword matching.

### The Two "Workhorse" Models

| Model | Type | Function |
| :--- | :--- | :--- |
| **Marengo** | **Embedding (Search)** | Converts video into vector data. Used for search, classification, and recommendation. It enables "Zero-Shot" search (finding things it wasn't explicitly trained to recognize). |
| **Pegasus** | **Generative (Text)** | Acts like a ChatGPT for video. It can summarize content, answer questions (QA), and generate titles or chapters based on visual and audio context. |

---

## 3. Comparison: Twelve Labs vs. Legacy Solutions (e.g., IBM Watson)

The industry has shifted from "Stitched Analysis" to "Multimodal Embeddings."

### Legacy Approach (IBM Watson Video Enrichment)
* **Method:** "Bag of Tags." It ran separate models for audio, OCR, and vision, then stitched them together.
* **Output:** A list of disconnected tags (e.g., `[Sky: 90%]`, `[Man: 80%]`, `[Loud Noise]`).
* **Weakness:** Lacked context. It struggled to differentiate between a "cooking show" and a "horror movie" because it didn't understand how the audio, visual, and time components related to each other.

### Modern Approach (Twelve Labs)
* **Method:** Joint Multimodal Embeddings. It ingests audio, video, and time simultaneously into a single model.
* **Output:** Vector representations that understand relationships (e.g., "Man chopping onions quickly").
* **Strength:** Context-aware and time-sensitive. It understands actions and events as they unfold.

---

## 4. Integration with Traditional Library Schemas
Despite using vector technology, Twelve Labs allows for integration with legacy SQL databases and Media Asset Management (MAM) systems.

* **Structured Output:** Developers can pass a specific **JSON Schema** to the Pegasus model.
* **Function:** The model watches the video and forces the output into the defined fields, creating clean metadata for traditional archives.

**Example Schema Capabilities:**
[ ]
## 5. Market & Use Cases
Twelve Labs primarily targets organizations dealing with massive amounts of "dark data" (unsearchable video archives).

### Key Buyer Personas
* **Media & Entertainment (The biggest spenders):**
    * **Sports Leagues (e.g., NFL):** Searching decades of footage for specific plays.
    * **Broadcasters:** Finding B-roll or archival clips instantly for news and editing.
* **Tech Platforms:**
    * **Cloud Data (Snowflake, Databricks):** Integrating video search into data lakes.
    * **MAM Systems:** Adding AI search capabilities to editing software.
* **Government & Security:**
    * **Surveillance:** Searching live CCTV feeds for specific anomalies or actions (e.g., "red truck turning left").
    * **Defense:** Analyzing drone or satellite footage (backed by In-Q-Tel).
* **AdTech:**
    * **Contextual Targeting:** Ensuring ads appear in relevant, brand-safe moments within a video stream.

---

## 6. Recent Developments, Funding & Ecosystem
Twelve Labs has rapidly evolved from a research-heavy startup into a key infrastructure player, backed by the biggest names in hardware and data.

### Funding & Valuation
* **Total Funding:** The company has raised significant capital (exceeding **$100M+** total), positioning it as a well-capitalized Series B stage company.
* **Strategic Round (Late 2024):** Secured **$30M** specifically from strategic partners including **Databricks**, **Snowflake Ventures**, and **SK Telecom**. This was a signal that the major data platforms want Twelve Labs integrated directly into their ecosystems.
* **Series A (Mid 2024):** Raised **$50M** co-led by **NEA** and **NVIDIA’s NVentures**, with participation from **Intel Capital**.

### Strategic Partnerships
The company strategy is to be "everywhere video lives."
* **NVIDIA:** A deep technical partnership. Twelve Labs trains its models on NVIDIA H100 clusters. In return, NVIDIA promotes them as the premiere video understanding solution for their hardware.
* **AWS (Amazon Web Services):**
    * **Bedrock Integration:** Twelve Labs' models (Marengo and Pegasus) are available directly on **Amazon Bedrock**, making them easy for any AWS developer to rent via API.
    * **Marketplace:** They are listed on the AWS Marketplace for simplified enterprise procurement.
* **Data Clouds (Snowflake & Databricks):** Both companies invested to ensure Twelve Labs integrates with their data lakes. This allows an analyst to run a SQL query in Snowflake that actually "searches" video files stored in the cloud.
* **Oracle:** Partnered to offer video understanding on Oracle Cloud Infrastructure (OCI).

### Latest Product Releases
* **Marengo 2.7 (Embedding Model):** The latest iteration of their search model, offering higher accuracy in distinguishing subtle actions and better OCR (reading text inside the video).
* **Pegasus 1.2 (Generative Model):** Enhanced capabilities for "Video-to-Text," reducing hallucinations when summarizing long-form video content.
* **Embeddings API:** A developer-focused shift allowing direct access to the vector embeddings, enabling teams to build their own custom search engines or recommendation systems on top of Twelve Labs' "brain."
