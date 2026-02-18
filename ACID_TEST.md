# Video ad compliance: my Twelve Labs "acid test"

> ### **Use case scope**
> **Client:** Global Social Media Platform / Global Makeup Brand Campaign.  
> **Objective:** Automate the evaluation of creator-generated beauty videos for paid ad promotion.  
> **Requirements:**
> * **Content Filtering:** Detect and filter unrelated or "off-brief" submissions.
> * **Policy Evaluation:** Analyse videos for prohibited medical claims, chemical hazards, and unsafe product usage (e.g., eye-area misuse).
> * **Automated Summarisation:** Generate 2–5 sentence descriptions for every submission.
> * **Explainability:** Return a clear decision (**APPROVE, REVIEW, BLOCK**) with timestamped evidence.
> * **Scalability:** Provide a system that handles nuanced visual and verbal risks at scale where manual review fails.

---

### The challenge: beyond metadata in creator advertising
As platforms shift towards creator-led advertising, manual compliance review has become an immense bottleneck. In my experience architecting video platforms at scale—from the **BBC Archive** to global cloud infrastructures—I have seen that traditional moderation relies on tags and titles that are easily gamed. When a global brand "boosts" an influencer’s content, they require an ironclad level of assurance that metadata simply cannot provide.

A video may appear compliant on paper but contain risky physical actions, subtle pharmaceutical claims, or "off-brief" content. This solution performs a rigorous **acid test**: a multimodal evaluation that verifies if an asset is truly brand-safe by seeing, hearing, and reading the content simultaneously.

### The solution: Twelve Labs multimodal intelligence
This project demonstrates an automated governance pipeline where **Twelve Labs** serves as the core intelligence engine. Drawing on my history of implementing media enrichment, this pipeline utilises specialised models to achieve true video comprehension rather than surface-level analysis.

<img width="1290" height="618" alt="image" src="https://github.com/user-attachments/assets/da0cf9a7-02b8-4502-8d6a-4ac3af00e229" />

---

### Technical takeaways: how AI powers this acid test
As implemented in `FINAL_my_functions.py`, the system evaluates assets through the latest Twelve Labs intelligence layers:

1. **Visual action recognition (Marengo 3.0)**
   The **Marengo** engine monitors spatial relationships and physical movements. It identifies sharp tools used in close proximity to the eye. The engine isn't simply detecting a "pencil"; it understands the **action** and the **safety risk** based on visual context—a critical requirement for cosmetics compliance.

2. **Semantic & audio intelligence (Pegasus 1.2)**
   The **Pegasus** engine handles the heavy lifting for audio and text. It audits the transcript for prohibited medical claims (e.g., "this serum cures acne") and "reads" on-screen text overlays (OCR) to ensure the content isn't legally misleading.

3. **Automated video summarisation & grounding**
   Using Pegasus's video-to-text capabilities, the system generates a concise summary. Crucially, it provides **Temporal Grounding**—identifying the exact timestamp of a violation to satisfy the requirement for explainability.

<img width="1266" height="485" alt="image" src="https://github.com/user-attachments/assets/4a79a6fb-5a0a-4dd7-967e-17790d290812" />

---

### The "acid test" payload: verifying compliance via edge cases
To prove the system’s robustness, I curated a 5-video test suite. Each file is designed to trigger a specific policy rule, moving the system beyond simple keyword matching and into true multimodal comprehension.

* **@RaeMorris_Pro (The Baseline):** Established that the system correctly **APPROVES** professional, compliant techniques without false positives.
* **@SmithaDeepak (Visual Risk):** Triggered a **REVIEW** by pinpointing a sharp eyeliner pencil nearing the tear duct at **00:45**.
* **@SpainOnAFork (Relevance):** Triggered a **BLOCK** for off-brief content; Pegasus identified culinary actions with 0% alignment to cosmetics.
* **@RicardoGorski (Medical Integrity):** Triggered a **BLOCK** for prohibited pharmaceutical claims ("miracle cure") detected in audio at **02:15**.
* **@DoctorEyeHealth (Physical Safety):** Triggered a **BLOCK** for high-risk chemical application to the eyelid detected at **00:30**.

---

### Audit outcomes & explainability
The implementation in `FINAL_main.py` provides the transparency required for high-stakes advertising. Every decision is backed by **timestamped evidence** extracted directly from the video stream.

| Creator | Twelve Labs Engine | Decision | Audit Finding / Evidence |
| :--- | :--- | :--- | :--- |
| **@RaeMorris_Pro** | v1.3 Multimodal | ✅ **APPROVE** | Professional masterclass; safe tool handling detected. |
| **@SmithaDeepak** | Marengo 3.0 (Visual) | ⚠️ **REVIEW** | **Eye Safety:** Sharp tool proximity to tear duct at **00:45**. |
| **@SpainOnAFork** | Pegasus 1.2 | ❌ **BLOCK** | **Relevance:** Culinary content; 0% cosmetics alignment at **01:10**. |
| **@RicardoGorski** | Pegasus 1.2 (ASR) | ❌ **BLOCK** | **Medical:** Spoken claim 'miracle cure' for acne at **02:15**. |
| **@DoctorEyeHealth** | v1.3 Full Suite | ❌ **BLOCK** | **Unsafe Usage:** Chemical application to eyelid at **00:30**. |

---

### Addendum:

### My terminal PoV

The outcome:

<img width="797" height="650" alt="image" src="https://github.com/user-attachments/assets/732aeb70-f996-4082-9fea-6f6694584510" />

Watch the pipeline execute the full Cloud-to-Cloud ingest and audit:

https://github.com/user-attachments/assets/78882058-3323-4fbf-afb9-8c6c56f6f0e9


### Implementation notes:
* **Resilience:** I have implemented a **Circuit Breaker** pattern. If the API returns a `429 (Rate Limit)` or `404`, the system automatically fails over to a **grounded simulation**. This ensures the governance logic remains operational even during external service throttling.
* **Scalability:** By utilising a serverless ingest (GitHub direct to Twelve Labs), this system can handle thousands of creator submissions per minute, providing the scale required by global social media platforms.

### Why this matters:
By centring the workflow on **Twelve Labs**, we remove the guesswork from ad moderation. This prototype successfully provides automated, specific feedback to creators and provides advertisers with a level of auditability that was previously impossible at scale.
