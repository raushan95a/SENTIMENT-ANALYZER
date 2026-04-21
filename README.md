# Sentiment Analyzer

[![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)
![Status](https://img.shields.io/badge/Status-Completed-success)
[![Live Demo](https://img.shields.io/badge/Live-Demo-blue)](https://raushan95a.github.io/SENTIMENT-ANALYZER/)

A hybrid NLP project for sentiment classification with:
- Browser interface using PyScript + TextBlob
- Local Python modules for CLI and neural experimentation

## Links
- Source Code: [Source Code](Source%20Code/)
- Technical Specification: [docs/SPECIFICATION.md](docs/SPECIFICATION.md)
- Live Demo: [GitHub Pages](https://raushan95a.github.io/SENTIMENT-ANALYZER/)

## Features
- Interactive web sentiment analyzer in [index.html](index.html)
- CLI workflow in [Source Code/app.py](Source%20Code/app.py)
- Neural model pipeline in [Source Code/neural_sentiment.py](Source%20Code/neural_sentiment.py)
- Notebook exploration in [Source Code/SENTIMENT_ANALYSIS.ipynb](Source%20Code/SENTIMENT_ANALYSIS.ipynb)

## Tech Stack
- Python 3.9+
- TextBlob
- Hugging Face Transformers
- PyScript / Pyodide
- HTML + CSS

## Project Structure

```python
SENTIMENT-ANALYZER/
├── .github/workflows/deploy.yml
├── docs/
│   └── SPECIFICATION.md
├── screenshots/
│   ├── 01-landing-page.png
│   └── 02-input-stage.png
├── Source Code/
│   ├── app.py
│   ├── neural_sentiment.py
│   ├── SENTIMENT_ANALYSIS.ipynb
│   └── requirements.txt
├── static/
│   └── style.css
├── index.html
├── 404.html
├── README.md
├── SECURITY.md
├── LICENSE
├── CITATION.cff
└── codemeta.json
```

## Screenshots
![Landing Page](screenshots/01-landing-page.png)
![Input and Output Stage](screenshots/02-input-stage.png)


## License
Licensed under the MIT License. See [LICENSE](LICENSE).

## Author
Maintained by [Raushan](https://github.com/raushan95a).
