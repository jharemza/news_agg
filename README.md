# 🗞️ news_agg

A lightweight Python utility to aggregate and display news headlines from multiple sources using RSS feeds. Ideal for quick terminal-based news summaries.

![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Last Commit](https://img.shields.io/github/last-commit/jharemza/news_agg)
![Repo Size](https://img.shields.io/github/repo-size/jharemza/news_agg)

---

## 📌 Overview

`news_agg` is a command-line tool that collects and formats headlines from curated RSS feeds. It is designed to give users a fast snapshot of breaking news from trusted sources.

---

## 🧱 Features

- Aggregates headlines from top-tier news sources
- Simple and fast terminal output
- Easily configurable feed list
- Built-in filtering and formatting

---

## 🚀 Setup

Clone the repository and install dependencies:

```bash
git clone https://github.com/jharemza/news_agg.git
cd news_agg
pip install -r requirements.txt
```

This project requires Python 3.10+.

---

## 🛠️ Usage

Run the main script to fetch the latest headlines:

```bash
python news_agg.py
```

To customize the feeds, modify the feeds.yaml file located in the project directory.

---

## 🧪 Example Output

```text
--- BBC News ---
• World leaders gather for G7 summit
• New COVID variant detected in Europe

--- Reuters ---
• Stock markets rise on Fed comments
• Tech earnings beat Wall Street expectations
```

---

## 📂 Project Structure

```bash
news_agg/
│
├── news_agg.py        # Main script
├── feeds.yaml         # RSS feed definitions
├── requirements.txt   # Python dependencies
└── README.md
```

---

## 📝 License

This project is licensed under the MIT License.

---

## 🤝 Contributing

Pull requests and ideas are welcome. For major changes, please open an issue first to discuss your plans.

---

## 📖 Additional Notes

- Designed for personal use or quick prototyping.
- Extendable for keyword filtering, sentiment analysis, or storage to DB.
