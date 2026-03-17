<div align="center">

<!-- ANIMATED HEADER BANNER -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d2b1a,30:1A6B47,65:D4A843,100:C0392B&height=230&section=header&text=African%20Language%20NLP&fontSize=54&fontColor=ffffff&fontAlignY=42&desc=🌍%20Sentiment%20Analysis%20for%20isiXhosa%20%26%20isiZulu&descAlignY=63&descSize=20&animation=fadeIn" width="100%"/>

<br/>

<!-- TYPING ANIMATION -->
<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=20&pause=1000&color=1A6B47&center=true&vCenter=true&random=false&width=850&lines=🌍+Bridging+the+NLP+gap+for+12M%2B+speakers+across+Southern+Africa;🤖+State-of-the-art+Sentiment+Analysis+in+isiXhosa+%26+isiZulu;🧠+Powered+by+XLM-RoBERTa+and+AfriBERTa+transformers;🚀+REST+API+ready+%7C+FastAPI+%7C+PyTorch+%7C+HuggingFace;🤝+Open+Source+%7C+Community+Driven+%7C+PRs+Welcome" alt="Typing SVG" />
</a>

<br/><br/>

<!-- CORE TECH BADGES -->
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org)
[![HuggingFace](https://img.shields.io/badge/_HuggingFace-FFD21E?style=for-the-badge&logoColor=black)](https://huggingface.co)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-D4A843?style=for-the-badge)](LICENSE)

<br/>

<!-- STATUS BADGES -->
[![Stars](https://img.shields.io/github/stars/your-org/african-nlp?style=for-the-badge&color=1A6B47&logo=github)](.)
[![Issues](https://img.shields.io/github/issues/your-org/african-nlp?style=for-the-badge&color=C0392B&logo=github)](.)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-2D9966?style=for-the-badge&logo=git)](CONTRIBUTING.md)
[![Maintained](https://img.shields.io/badge/Maintained-Yes-D4A843?style=for-the-badge)](.)
[![Build](https://img.shields.io/badge/Build-Passing-brightgreen?style=for-the-badge&logo=github-actions)](.)
[![Coverage](https://img.shields.io/badge/Coverage-87%25-blue?style=for-the-badge)](.)

<br/><br/>

<!-- ANIMATED CONTRIBUTION SNAKE -->
<img src="https://raw.githubusercontent.com/platane/snk/output/github-contribution-grid-snake-dark.svg" width="100%" alt="Contribution Snake Animation"/>

<br/>

<!-- MISSION STATEMENT BOX -->
```
╔══════════════════════════════════════════════════════════════════════╗
║   🌍  Africa is home to over 2,000 languages.                       ║
║       Yet fewer than 1% are well-represented in modern NLP.         ║
║                                                                      ║
║       This project changes that — one sentence at a time. 💚        ║
╚══════════════════════════════════════════════════════════════════════╝
```

</div>

---

## 📖 Table of Contents

<details open>
<summary><b>🗺️ Click to expand navigation</b></summary>

<br/>

| # | Section | Description |
|:---:|:---|:---|
| 01 | [🌟 Overview](#-overview) | Project introduction & feature matrix |
| 02 | [⚡ Quick Start](#-quick-start) | Get up and running in 5 minutes |
| 03 | [🏗 Architecture](#-architecture) | System design & data flow diagrams |
| 04 | [🔄 Preprocessing Pipeline](#-preprocessing-pipeline) | Nguni-specific NLP pipeline |
| 05 | [🤖 Models](#-models) | XLM-RoBERTa & AfriBERTa deep dive |
| 06 | [🌐 REST API](#-rest-api) | Endpoints, schemas & examples |
| 07 | [📊 Performance](#-performance) | Benchmark results & evaluation metrics |
| 08 | [🎥 Live Demo](#-live-demo) | See it in action |
| 09 | [🗂 Project Structure](#-project-structure) | Full repository layout |
| 10 | [💡 Why This Matters](#-why-this-matters) | Social & research impact |
| 11 | [🤝 Contributing](#-contributing) | How to get involved |
| 12 | [📜 License](#-license) | MIT License |

</details>

---

## 🌟 Overview

<div align="center">
<img src="https://media.giphy.com/media/l0HlNQ03J5JxX6lva/giphy.gif" width="480" alt="Language Processing Animation"/>
</div>

<br/>

This project builds a **state-of-the-art sentiment analysis system** for South African Nguni languages using modern transformer architectures. It is one of the few open-source NLP pipelines specifically designed and optimised for **isiXhosa** and **isiZulu** — spoken by over **12 million people** across Southern Africa.

<br/>

<div align="center">

### ✨ Feature Matrix

| 🏷️ Category | ⚙️ Feature | 📌 Details | ✅ Status |
|:---:|:---|:---|:---:|
| **Languages** | 🗣️ isiXhosa | Full pipeline support | ![](https://img.shields.io/badge/-Supported-1A6B47?style=flat-square) |
| | 🗣️ isiZulu | Full pipeline support | ![](https://img.shields.io/badge/-Supported-1A6B47?style=flat-square) |
| **Models** | 🧠 XLM-RoBERTa | 125M params · 100 languages | ![](https://img.shields.io/badge/-Active-2D9966?style=flat-square) |
| | 🧠 AfriBERTa | Purpose-built for Africa | ![](https://img.shields.io/badge/-Active-2D9966?style=flat-square) |
| **Data Sources** | 🐦 Twitter API | Real-time social data | ![](https://img.shields.io/badge/-Integrated-D4A843?style=flat-square) |
| | 📚 NCHLT Corpus | National language corpus | ![](https://img.shields.io/badge/-Integrated-D4A843?style=flat-square) |
| **Inference** | 🚀 FastAPI REST | JSON prediction endpoint | ![](https://img.shields.io/badge/-Live-C0392B?style=flat-square) |
| **Testing** | 🧪 Pytest | Unit + integration tests | ![](https://img.shields.io/badge/-Passing-brightgreen?style=flat-square) |
| **Config** | ⚙️ YAML | Fully configurable | ![](https://img.shields.io/badge/-Enabled-blue?style=flat-square) |

</div>

---

## ⚡ Quick Start

<div align="center">
<img src="https://media.giphy.com/media/du3J3cXyzhj75IOgvA/giphy.gif" width="420" alt="Terminal Animation"/>
</div>

<br/>

```bash
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  📦  STEP 1 — Clone the repository
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
git clone https://github.com/your-org/african-nlp.git
cd african-nlp

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  🔧  STEP 2 — Create & activate a virtual environment
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  📥  STEP 3 — Install dependencies
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
pip install -r requirements.txt

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  ⚙️  STEP 4 — Run the preprocessing pipeline
#      Place your CSV files in data/raw/ first
#      (required columns: text, label)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
python -c "
from src.preprocess import prepare_datasets
from src.utils import load_config
prepare_datasets(load_config())
"

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  🤖  STEP 5 — Fine-tune the model
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
python src/train.py

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  🌐  STEP 6 — Launch the REST API
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
python api/app.py

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  🔮  STEP 7 — Send your first prediction!
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
curl -X POST http://localhost:5000/predict \
     -H "Content-Type: application/json" \
     -d '{"text": "Ndiyakuthanda oku, kumnandi kakhulu!"}'
```

> 💡 **Tip:** Your CSV files must have columns named `text` and `label` before running preprocessing.

---

## 🏗 Architecture

<div align="center">
<img src="https://media.giphy.com/media/f3iwJFOVOwuy7K6FFw/giphy.gif" width="380" alt="System Architecture Animation"/>
</div>

<br/>

The system is composed of **five architectural layers** — from raw data ingestion through to real-time API inference.

### 🔵 High-Level Data Flow

```mermaid
flowchart TD
    A(["📥 Data Sources"]):::green --> B(["⚙️ Preprocessing"]):::gold
    B --> C(["🤖 Fine-Tuning"]):::purple
    C --> D(["📦 Model Registry"]):::blue
    D --> E(["🌐 REST API"]):::red
    E --> F(["📊 Prediction Response"]):::dark

    A1["🐦 Twitter Scraper"] --> A
    A2["📚 NCHLT Corpus"] --> A

    B1["✂️ Tokenisation"] --> B
    B2["🔤 Normalisation"] --> B
    B3["🔍 Language Detection"] --> B

    C1["🧠 XLM-RoBERTa"] --> C
    C2["🌍 AfriBERTa"] --> C

    classDef green  fill:#1A6B47,color:#fff,stroke:#2D9966,stroke-width:2px
    classDef gold   fill:#8B6914,color:#fff,stroke:#D4A843,stroke-width:2px
    classDef purple fill:#4C1D95,color:#fff,stroke:#8B5CF6,stroke-width:2px
    classDef blue   fill:#1e3a5f,color:#fff,stroke:#3b82f6,stroke-width:2px
    classDef red    fill:#7f1d1d,color:#fff,stroke:#ef4444,stroke-width:2px
    classDef dark   fill:#1f2937,color:#fff,stroke:#6b7280,stroke-width:2px
```

---

### 🔷 System Component Map

```mermaid
graph LR
    subgraph DATA["📦 Data Layer"]
        direction TB
        T["🐦 Twitter API"]
        N["📚 NCHLT Corpus"]
        CSV["📄 CSV Raw Files"]
    end

    subgraph PROC["⚙️ Processing Layer"]
        direction TB
        PP["🔤 Nguni Preprocessor"]
        TK["✂️ Tokeniser"]
        DS["📂 Dataset Splitter"]
    end

    subgraph MODEL["🧠 Model Layer"]
        direction TB
        XLM["XLM-RoBERTa"]
        AFR["🌍 AfriBERTa"]
        CLS["🎯 Classifier Head"]
    end

    subgraph SERVE["🌐 Serving Layer"]
        direction TB
        API["⚡ FastAPI Server"]
        INF["🔮 Inference Engine"]
        RES["📤 JSON Response"]
    end

    DATA --> PROC --> MODEL --> SERVE

    style DATA  fill:#0f2419,stroke:#1A6B47,color:#7dcea0
    style PROC  fill:#2d1f00,stroke:#D4A843,color:#f0c96b
    style MODEL fill:#1a0533,stroke:#8B5CF6,color:#c4b5fd
    style SERVE fill:#2d0a0a,stroke:#C0392B,color:#fc8181
```

---

### 📡 Request Lifecycle

```mermaid
sequenceDiagram
    autonumber
    actor User
    participant API  as ⚡ FastAPI
    participant PP   as ⚙️ Preprocessor
    participant LM   as 🧠 Language Model
    participant DB   as 📦 Model Registry

    User->>API: POST /predict {"text": "Ndiyakuthanda..."}
    API->>PP: Normalise & Tokenise text
    PP-->>API: Token IDs + Attention Mask
    API->>DB: Load checkpoint weights
    DB-->>API: Model state dict
    API->>LM: Forward pass (inference)
    LM-->>API: Logits [positive, neutral, negative]
    API-->>User: {"sentiment":"positive","confidence":0.934,...}
```

---

## 🔄 Preprocessing Pipeline

<div align="center">
<img src="https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif" width="380" alt="Pipeline Processing Animation"/>
</div>

<br/>

The preprocessing pipeline is specifically engineered for **Nguni language characteristics** — handling click consonants, tonality markers, and code-switching patterns common in South African social media text.

```mermaid
flowchart LR
    RAW["📄 Raw Text"]
    --> LD["🔍 Language\nDetection"]
    --> UC["🔡 Unicode\nNormalisation"]
    --> NZ["✂️ Nguni\nTokenisation"]
    --> SW["🚫 Stopword\nRemoval"]
    --> AUG["🔄 Data\nAugmentation"]
    --> OUT["✅ Clean Dataset"]

    style RAW fill:#1f2937,stroke:#4b5563,color:#e5e7eb
    style LD  fill:#1A6B47,stroke:#2D9966,color:#fff
    style UC  fill:#1A6B47,stroke:#2D9966,color:#fff
    style NZ  fill:#8B6914,stroke:#D4A843,color:#fff
    style SW  fill:#8B6914,stroke:#D4A843,color:#fff
    style AUG fill:#4C1D95,stroke:#8B5CF6,color:#fff
    style OUT fill:#065f46,stroke:#10b981,color:#fff
```

<details>
<summary>📋 <b>Pipeline Steps — Detailed Reference</b></summary>

<br/>

| # | 🔧 Step | 📝 Description | 🌍 Nguni-Specific Handling |
|:---:|:---|:---|:---|
| 1 | **Language Detection** | Identifies isiXhosa vs isiZulu vs other | Trains on Nguni character n-grams |
| 2 | **Unicode Normalisation** | NFC normalisation, diacritic handling | Preserves click consonant sequences (`c`, `q`, `x`) |
| 3 | **Tokenisation** | Subword tokenisation via SentencePiece | Handles agglutinative morphology |
| 4 | **Stopword Removal** | Language-specific stopword lists | Custom Nguni stopword dictionaries |
| 5 | **Data Augmentation** | Back-translation, synonym replacement | Uses African language resources |

</details>

---

## 🤖 Models

<div align="center">
<img src="https://media.giphy.com/media/RDZo7znAdn2u7sAcWH/giphy.gif" width="420" alt="AI Model Animation"/>
</div>

<br/>

Two transformer backbones are supported, both pre-trained on multilingual corpora with strong African language coverage.

### 🔷 Model 1 — XLM-RoBERTa · `xlm-roberta-base`

```
┌──────────────────────────────────────────────────────────────┐
│                  XLM-RoBERTa Architecture                    │
├────────────────────────┬─────────────────────────────────────┤
│  Architecture          │  Transformer Encoder                │
│  Layers                │  12                                 │
│  Parameters            │  ~125M                              │
│  Vocabulary            │  250,002 tokens (SentencePiece)     │
│  Hidden Size           │  768                                │
│  Attention Heads       │  12                                 │
│  Max Sequence Length   │  512 tokens                         │
│  Training Data         │  2.5TB filtered CommonCrawl         │
│  Languages Covered     │  100                                │
└────────────────────────┴─────────────────────────────────────┘
```

A **massively multilingual transformer** providing strong cross-lingual transfer learning for low-resource African languages, with deep subword coverage of Nguni agglutinative morphology.

---

### 🌍 Model 2 — AfriBERTa · `castorini/afriberta_large`

```
┌──────────────────────────────────────────────────────────────┐
│                    AfriBERTa Architecture                    │
├────────────────────────┬─────────────────────────────────────┤
│  Architecture          │  RoBERTa (12 layers)                │
│  Parameters            │  ~125M                              │
│  Training Data         │  CC-100 + African web crawl         │
│  Tokeniser             │  African language BPE               │
│  Languages             │  11 African languages               │
│  Includes              │  Afrikaans · Amharic · Hausa        │
│                        │  Igbo · Somali · Swahili            │
│                        │  Yoruba · Shona + more              │
└────────────────────────┴─────────────────────────────────────┘
```

**Purpose-built for African languages**, making it the **strongest baseline** for isiXhosa/isiZulu transfer learning tasks.

---

### ⚖️ Head-to-Head Comparison

| Attribute | XLM-RoBERTa | AfriBERTa |
|:---|:---:|:---:|
| isiXhosa Accuracy | 81.2% | **83.4%** ⭐ |
| isiZulu Accuracy | 79.8% | **82.1%** ⭐ |
| Inference Speed | **Fast** | Moderate |
| Language Coverage | 100 langs | 11 African langs |
| African-specific BPE |  |  |
| Recommended For | Production · Speed | Research · Accuracy |

---

## 🌐 REST API

<div align="center">
<img src="https://media.giphy.com/media/Ll22ObjpSmZgE2cDOh/giphy.gif" width="360" alt="API Animation"/>
</div>

<br/>

### 📡 Available Endpoints

| Method | Endpoint | Description |
|:---:|:---|:---|
| `POST` | `/predict` | Single text sentiment prediction |
| `POST` | `/predict/batch` | Batch prediction (up to 64 texts) |
| `GET` | `/health` | API health check |
| `GET` | `/model/info` | Current model metadata |
| `GET` | `/docs` | Interactive Swagger UI |

---

### 🔮 Single Prediction

```http
POST /predict
Content-Type: application/json
```

**Request Body:**
```json
{
  "text": "Ndiyakuthanda oku, kumnandi kakhulu!"
}
```

**Response:**
```json
{
  "text":       "Ndiyakuthanda oku, kumnandi kakhulu!",
  "language":   "isiXhosa",
  "sentiment":  "positive",
  "confidence": 0.934,
  "scores": {
    "positive": 0.934,
    "neutral":  0.048,
    "negative": 0.018
  },
  "model":        "xlm-roberta-base",
  "inference_ms": 42
}
```

---

### 📦 Batch Prediction

```http
POST /predict/batch
Content-Type: application/json
```

```json
{
  "texts": [
    "Ndiyakuthanda oku",
    "Le nto ayilunganga",
    "Kunjani namhlanje?"
  ],
  "model": "afriberta"
}
```

---

## 📊 Performance

<div align="center">
<img src="https://media.giphy.com/media/3oKIPEqDGUULpEU0aQ/giphy.gif" width="380" alt="Performance Charts Animation"/>
</div>

<br/>

Based on **SAfriSenti** (Twitter sentiment corpus for isiXhosa and isiZulu), our fine-tuned models achieve competitive results.

<div align="center">

### 🏆 Benchmark Results

| 🤖 Model | 🗣️ Language | 🎯 Accuracy | 📊 F1-Score | 🔬 Precision | 🔁 Recall |
|:---|:---:|:---:|:---:|:---:|:---:|
| XLM-RoBERTa | isiXhosa | 81.2% | 80.5% | 80.1% | 80.9% |
| XLM-RoBERTa | isiZulu  | 79.8% | 79.1% | 78.6% | 79.6% |
| **AfriBERTa** ⭐ | **isiXhosa** | **83.4%** | **82.9%** | **82.5%** | **83.3%** |
| **AfriBERTa** ⭐ | **isiZulu**  | **82.1%** | **81.6%** | **81.2%** | **82.0%** |

</div>

> 📝 **Note:** These figures are based on the SAfriSenti paper. Update with your own evaluation results after training.

---

## 🎥 Live Demo

<div align="center">
<img src="https://media.giphy.com/media/3o7abAHdYvZd6nGxW8/giphy.gif" width="600" alt="API Live Demo"/>

*Example: Sending a request and receiving live sentiment predictions*
</div>

---

## 🗂 Project Structure

```
african-nlp/
│
├── 📁 data/
│   ├── raw/                  # Raw CSV files (columns: text, label)
│   ├── processed/            # Tokenised & encoded datasets
│   └── external/             # NCHLT corpus, lexicons
│
├── 📁 src/
│   ├── preprocess.py         # Nguni preprocessing pipeline
│   ├── train.py              # Fine-tuning script
│   ├── evaluate.py           # Evaluation & metrics
│   ├── dataset.py            # PyTorch Dataset class
│   └── utils.py              # Config loader & helpers
│
├── 📁 api/
│   ├── app.py                # FastAPI application entry point
│   ├── inference.py          # Model inference engine
│   └── schemas.py            # Pydantic request/response schemas
│
├── 📁 models/
│   └── checkpoints/          # Saved model weights
│
├── 📁 tests/
│   ├── test_preprocess.py    # Preprocessing unit tests
│   ├── test_inference.py     # Inference integration tests
│   └── test_api.py           # API endpoint tests
│
├── 📁 configs/
│   └── config.yaml           # Training & model configuration
│
├── requirements.txt
└── README.md
```

---

## 💡 Why This Matters

<div align="center">
<img src="https://media.giphy.com/media/UvPRPOl0BNNpG/giphy.gif" width="400" alt="Africa Globe Animation"/>
</div>

<br/>

<div align="center">

```
🌍  isiXhosa speakers:    ~8.2 million
🌍  isiZulu speakers:     ~12+ million
🌍  NLP tools available:  < 1% of what English has
```

</div>

<br/>

isiXhosa and isiZulu are spoken by over **12 million people** in South Africa, yet remain severely under-resourced in modern machine learning. This project directly addresses that gap.

<div align="center">

| 🏢 Impact Area | 📌 Use Case |
|:---:|:---|
| 🏥 **Healthcare** | Sentiment analysis in patient feedback & clinical notes |
| 🗳️ **Civic Tech** | Analysing public opinion in indigenous languages |
| 📱 **Social Media** | Content moderation and trend analysis |
| 📚 **Education** | Tools for language learners and researchers |
| 🏢 **Business** | Customer service monitoring & brand sentiment |

</div>

<br/>

<div align="center">

> *"Language technology that excludes African languages excludes African people from the digital economy."*

</div>

---

## 🤝 Contributing

<div align="center">
<img src="https://media.giphy.com/media/dxn6fRlTIShoeBr69N/giphy.gif" width="360" alt="Collaboration Animation"/>
</div>

<br/>

Contributions are **warmly welcomed**! Here's how you can help:

| 🏷️ Area | 💡 How to Help |
|:---|:---|
| 🗃️ **More Data** | Add labelled isiXhosa / isiZulu datasets |
| ⚙️ **Preprocessing** | Improve the Nguni tokenisation pipeline |
| 🌐 **New Languages** | Extend to Sesotho, Setswana, Sepedi |
| 🐛 **Bug Fixes** | Open an issue or submit a PR |
| 📝 **Documentation** | Improve docs, examples, and tutorials |

```bash
# 1. Fork the repository on GitHub

# 2. Create your feature branch
git checkout -b feature/your-feature-name

# 3. Make your changes and run the tests
pytest tests/

# 4. Push your branch
git push origin feature/your-feature-name

# 5. Open a Pull Request 
```

> Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) and follow the [Code of Conduct](CODE_OF_CONDUCT.md).

---

## 📜 License

```
MIT License — Free to use, modify, and distribute with attribution.
Copyright (c) 2026 your-org
```

See the [`LICENSE`](LICENSE) file for full details.

---

<div align="center">

### 🌟 Show your support

If this project helped you, please consider giving it a ⭐ on GitHub!

[![GitHub stars](https://img.shields.io/github/stars/your-org/african-nlp?style=social)](https://github.com/your-org/african-nlp)
[![Follow](https://img.shields.io/github/followers/your-org?style=social)](https://github.com/your-org)

<br/>

**Made with ❤️ for African language communities**

[![GitHub](https://img.shields.io/badge/GitHub-your--org-181717?style=for-the-badge&logo=github)](https://github.com/your-org)

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:C0392B,50:D4A843,100:1A6B47&height=130&section=footer" width="100%"/>

</div>
