# 🤖 AI Assistant Comparison Project

## Overview

This project compares two AI personal assistants:

1. Open Source Assistant using Qwen2.5 from Hugging Face
2. Frontier Model Assistant using Llama 3.1 via Groq API

The project evaluates:
- factual accuracy
- hallucination rate
- jailbreak resistance
- bias and harmful outputs
- safety handling


# Features

✅ Multi-turn conversations  
✅ Short-term conversational memory  
✅ Open-source model integration  
✅ Frontier model integration  
✅ Streamlit chat interface  
✅ Safety and jailbreak testing  
✅ Bias evaluation  
✅ Comparative evaluation framework  


# Models Used

| Assistant Type | Model |
|---|---|
| Open Source Assistant | Qwen2.5-0.5B-Instruct |
| Frontier Model Assistant | Llama 3.1 via Groq API |


# Tech Stack

- Python
- Streamlit
- Hugging Face Transformers
- Groq API
- Qwen2.5
- Llama 3.1
- Git & GitHub


# Project Structure

```bash
ai-assistant-project/
│
├── app.py
├── README.md
├── evaluation_report.md
├── requirements.txt
│
├── prompts/
│   ├── factual.txt
│   ├── jailbreak.txt
│   └── bias.txt
│
├── results/
│   └── results.md
│
└── screenshots/
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/varunsai584/ai-assistant-comparison.git
cd ai-assistant-comparison
```


## 2. Create Virtual Environment

```bash
python -m venv .venv
```


## 3. Activate Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```


## 4. Install Dependencies

```bash
pip install -r requirements.txt
```


## 5. Add Groq API Key

Inside `app.py` replace:

```python
api_key="YOUR_GROQ_API_KEY"
```

with your actual Groq API key.


## 6. Run Application

```bash
python -m streamlit run app.py
```


# Evaluation Categories

The assistants were evaluated on:

## 1. Factual Accuracy
- correctness of responses
- hallucination rate

## 2. Jailbreak Resistance
- refusal handling
- robustness against harmful prompts

## 3. Bias & Harmful Outputs
- stereotype handling
- discriminatory prompt safety


# Results Summary

| Category | Open Source | Frontier Model |
|---|---|---|
| Accuracy | Medium | High |
| Hallucination Rate | Medium | Low |
| Safety | Good | Very Good |
| Response Quality | Good | Excellent |
| Refusal Handling | Good | Excellent |


# Key Findings

- The Frontier Model provided better factual accuracy and safer responses.
- The Open Source model was lightweight and suitable for local deployment.
- Frontier APIs showed stronger robustness against adversarial prompts.


# Future Improvements

- Public deployment on Hugging Face Spaces
- Long-term memory support
- Vector database integration
- Better UI/UX
- Observability and monitoring
- Guardrails and moderation layers



# Screenshots

Screenshots for:
- factual prompts
- jailbreak prompts
- bias evaluation

are included inside the `screenshots/` folder.


# Author

**Varun Sai**

GitHub:
https://github.com/varunsai584
