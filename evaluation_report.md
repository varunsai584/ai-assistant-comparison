# AI Assistant Evaluation Report

## Objective

The objective of this project was to compare an Open Source AI Assistant and a Frontier Model Assistant across factual accuracy, safety, hallucination rate, and harmful prompt handling.



# Models Used

| Assistant Type | Model |
|---|---|
| Open Source | Qwen2.5-0.5B-Instruct |
| Frontier Model | Llama 3.1 via Groq API |



# Evaluation Categories

## 1. Factual Accuracy

The Frontier Model produced more concise and accurate answers compared to the Open Source model.

The Open Source model occasionally generated overly verbose responses and minor hallucinations.



## 2. Jailbreak Resistance

Both assistants successfully refused harmful prompts such as:
- malware creation
- phishing generation
- hacking instructions

The Frontier Model provided cleaner and shorter refusal responses.


## 3. Bias & Harmful Outputs

Both assistants avoided generating discriminatory or hateful responses.

The Frontier Model handled sensitive prompts more professionally and consistently.



# Final Comparison

| Category | Open Source | Frontier Model |
|---|---|---|
| Accuracy | Medium | High |
| Safety | Good | Very Good |
| Hallucination Rate | Medium | Low |
| Speed | Medium | Fast |
| Refusal Quality | Good | Excellent |


# Recommendation

The Frontier Model performed better overall in:
- factual reliability
- safety handling
- concise responses
- robustness

The Open Source model remains valuable for:
- local deployment
- low-cost inference
- offline experimentation


# Conclusion

This project demonstrates how hosted frontier models currently outperform lightweight open-source models in reliability and safety, while open-source models provide flexibility and deployment freedom.