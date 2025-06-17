AI Text Completion App (Hugging Face Version)

This is a simple Python-based text completion application that uses a pre-trained GPT-2 language model from [Hugging Face Transformers](https://huggingface.co/docs/transformers/index). The app allows users to input a text prompt and receive AI-generated completions in the terminal.

---

## Features

- Text generation using Hugging Face's `pipeline`
- User control over generation temperature and token length
- Reproducible results with random seed
- Input validation and basic error handling
- Works offline after model is downloaded

---

## 🛠Requirements

Make sure you have Python 3.7+ installed, then install the required libraries:

```bash
pip install transformers torch
