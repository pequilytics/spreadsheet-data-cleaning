[🇧🇷 Leia em Português](README_pt.md)

[🇧🇷 Leia em Português](README_pt.md)

# ⭐ Lead qualification pipeline

This project consists of an automated Python script for cleaning, standardizing, and qualifying company databases (leads), specifically focused on the **construction sector**.
The goal is to transform raw, "dirty" lists into a qualified **ICP (Ideal Customer Profile)** base, filtering for relevant construction and real estate development companies while removing complex duplicates.

## 🏷️ Features

### 1. Smart CNAE (tax code) filtering
The script isolates only companies with strategic economic activities, eliminating small renovations and irrelevant works:
- **4120-4/00:** construction of buildings.
- **4110-7/00:** real estate development.
- **4399-1/01:** construction management.

### 2. Safe deduplication
Custom algorithm that removes duplicates without data loss. It checks multiple criteria in priority order:
1.  **CNPJ** (unique Tax ID).
2.  **Website** (same group companies).
3.  **E-mail and Phone** (repeated contacts).
*Note: The algorithm protects empty fields, ensuring companies without a site/email are not incorrectly deleted.*


## 🛠️ Tech Stack

* **Python 3.x**
* **Pandas** (Data Manipulation)
* **OpenPyXL** (Excel I/O)

## 📋 How to Use

1.  Clone this repository.
2.  Install dependencies:
    ```bash
    pip install pandas openpyxl
    ```
3.  Place your raw spreadsheet in the project folder.
4.  Open the `.ipynb` file (Jupyter Notebook) and adjust the input filename.
5.  Run the cells to generate the clean output file.

## ⚠️ Privacy Note (GDPR/LGPD)

This repository contains only the **source code** for automation. No spreadsheets with real company or personal data have been or will be shared publicly, in compliance with data protection laws.

---
Developed for Sales Ops and Commercial Intelligence optimization.

♡‧₊˚✧
### Developed by **Débora Tavares**
*Working in Sales Operations & Data Intelligence*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/seu-link-aqui)
