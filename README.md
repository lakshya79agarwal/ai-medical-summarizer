# AI Medical Report Summarizer

The **AI Medical Report Summarizer** is an automated healthcare technology solution designed to bridge the medical literacy gap between doctors and patients. Medical lab reports are dense with technical terminology, making them difficult for non-professionals to interpret. This project provides a patient-friendly platform that instantly converts complex health metrics into simple, plain language.

---

## 👥 1. Team Setup & Task Assignment Matrix

**Project Leader:** Narmeta Archana  
*Responsibilities: Architect cross-module data pipelines, lead final version alignments, oversee testing validation passes, and synchronize code distribution checkpoints.*

| Module Track | Assigned Members | Core Micro-Tasks & Responsibilities |
| :--- | :--- | :--- |
| **1. Frontend UI Development** | Sachin, Archana, Aravind, Abhishek | Develop the primary Streamlit interface shell dashboard; build drag-and-drop file upload windows; implement simple rendering displays for medical metrics cards. |
| **2. PDF & Document Processing** | Rishvik | Implement text stream extractors using pdfplumber/PyPDF2; process raw digital PDF documents without using heavy OCR layers; feed extracted strings safely into the preprocessing text queues. |
| **3. OCR Extraction Engine** | Vaishnavi, Lakshya | Configure Tesseract OCR and EasyOCR runtime environments; write OpenCV pre-filters (binarization, threshold adjustments); recover written lines from smartphone camera report snaps. |
| **4. Core Text Processing** | Aprajita, Khusi, Aryan | Build regex scripts to trim spacing fragments and metadata line artifacts; format raw layout strings systematically into continuous code blocks; provide consistent text files to downstream extraction APIs. |
| **5. Medical Info Extraction** | Kavya, Aarti | Isolate high/low metric pointers (e.g. Blood Sugar, HbA1c levels); map patient metrics data structures (Name, Age, Lab units); isolate Doctor Impressions text fields precisely from inputs. |
| **6. AI Summarization & Prompts** | Divyanshi, Abhishek sanu, Archana | Construct system instructions for plain text summaries; connect API calls via official Generative AI / OpenAI SDK libraries; build strict system guards preventing health metric hallucinations. |
| **7. Backend Architecture** | Gobinath, Lakshya Agrawal | Architect RESTful application server ports using FastAPI; build structural data checking patterns using Pydantic fields; expose reliable backend API routes for the frontend Streamlit UI. |
| **8. Translation & PDF Generation** | Vaishnavi | Configure localization systems for fluent Hindi translations; build clean exportable PDF layout engines using FPDF tools; verify that metrics and value tables render correctly across languages. |
| **9. Testing, Deployment & Docs** | Sachin, Gobinath, Archana | Run performance checks across fuzzy, low-light test image files; containerize the backend and UI instances via Docker environments; host systems live on secure cloud targets (HuggingFace / AWS). |

---

## 🌿 2. Repository Branching Policy

To maintain repository stability and prevent code conflicts across our 15-member team, please adhere strictly to this branching strategy:

* **`main`**: Production-ready, stable code only. **Do not commit directly to this branch.** All additions must come via an approved Pull Request (PR).
* **`feature/frontend-*`**: For Streamlit interface development, shell layouts, and display card cards.
* **`feature/backend-*`**: For FastAPI core routing, Pydantic data schemas, and API design.
* **`feature/ocr-*`**: For Tesseract, EasyOCR adjustments, and OpenCV pre-filtering modules.
* **`feature/text-processing-*`**: For regular expressions (Regex) cleaning strings and data preparation pipelines.
* **`feature/llm-*`**: For prompt tuning, system guardrails, and API connector scripts.

---

## 📅 3. Execution Roadmap

### Phase 1: Environment Architecture & Server Setup (Week 1)
* **Goal:** Launch backend server routes, data schemas, and primary UI layouts.
* **Focus:** Setting up FastAPI connection wrappers, base route channels, Streamlit upload interfaces, and baseline text extractors for native digital PDFs.

### Phase 2: Core Processing, OCR Engines & Metrics Parsing (Week 2)
* **Goal:** Optimize text collection rules, image enhancement passes, and laboratory parameter matching structures.
* **Focus:** Configuring OpenCV filters, raw image OCR models, writing text string filters via regex definitions, and engineering specific medical item extraction rules.

### Phase 3: Prompt Tuning, Translation & Live Cloud Hosting (Week 3)
* **Goal:** Wire backend API endpoints to LLMs, implement translation rules, run extensive system testing, and deploy live.
* **Focus:** Linking AI prompt pipelines and API connectors, fine-tuning Hindi translation routes, generating downloadable PDF reports, packaging components via Docker files, and launching live production servers.
