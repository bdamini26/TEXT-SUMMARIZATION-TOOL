A Python-based Text Summarization Tool that generates concise summaries from lengthy text using Natural Language Processing (NLTK). 
OUTPUT:
<img width="2551" height="1364" alt="Image" src="https://github.com/user-attachments/assets/ce033e09-1730-4182-a9f8-412d2a5b7ae4" />
# 📝 Text Summarization Tool

## 🔍 Project Overview

This project implements an **extractive text summarization system** that:

- Takes long text as input  
- Processes it using NLP techniques  
- Scores sentences based on word importance  
- Generates a concise summary

---

## ⚙ Technologies Used

- Python  
- NLTK (Natural Language Toolkit)  
- Regular Expressions  
- Heapq Algorithm  
- Extractive Summarization

---

## 🚀 Features

- Accepts manual text input  
- Supports text file input  
- Generates user-defined length summary  
- Removes stopwords  
- Ranks sentences based on frequency

---

## ▶ How to Run

1. Install dependencies:

```bash
pip install nltk

2.Download NLTK resources:

import nltk
nltk.download('punkt')
nltk.download('stopwords')

3.Run the program:
python textsummarizetool.py
