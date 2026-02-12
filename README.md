# Lead qualification + deduplication pipeline

[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

> **Automated cleaning, standardization and intelligent deduplication for company databases.**
> 
> [🇧🇷 Leia em português](README_pt.md)

---

## ⭐ Overview

This project consists of an automated Python script for **cleaning, standardizing and qualifying** company databases (leads).
The goal is to transform raw, "dirty" lists into a reliable **ICP (Ideal Customer Profile)** base, applying advanced algorithms to remove complex duplicates without losing valuable contact information.


## 🏷️ Features

#### 1. Waterfall deduplication
Unlike standard Excel or Pandas deduplication methods, this algorithm uses a **hierarchical and safe approach**:
* **Hierarchy of trust:** checks for duplicates in a specific priority order:
    1.  `CNPJ` (unique tax ID - strongest match)
    2.  `Website`
    3.  `E-mail` and `Phone`
    4.  `Company Name` (fuzzy text match)
* **Safe-null logic:** the algorithm **does not delete** rows simply because a field is empty. If a company lacks a website, it is preserved to be checked against phone or email records later in the pipeline.

#### 2. Completeness score
Before removing a duplicate, the script calculates a *score* for each row. If multiple records exist for the same company, the system automatically preserves the one with the **most filled columns**, ensuring the highest data quality.

#### 3. Smart normalization
Data is standardized at runtime for accurate comparison (without altering the original saved data):
* **Websites:** `https://www.site.com`, `www.site.com/`, and `site.com` are treated as identical.
* **IDs/Phones:** removal of non-numeric characters and formatting.
* **Text:** handling of extra spaces, case sensitivity and special characters.

## 💡 Configuration 

The script is highly configurable via a mapping dictionary. You can adapt it to any spreadsheet layout by modifying the `MAPA_COLUNAS` variable in the script:

```python
MAPA_COLUNAS = {
    "CNPJ": "CNPJ",               # Key column: Excel header name
    "Razão Social": "Razão Social",
    "Website": "Websites",
    "E-mail": "E-mails"
}
```

### Optional ICP filtering (CNAE / industry codes)

In many real-world datasets, deduplication alone is not enough. This pipeline also supports optional industry filtering before the cleaning stage.

The script can filter companies by a list of allowed industry codes (e.g., CNAE or similar classification systems) to ensure the final dataset aligns with a target ICP segment.

This step is:
* **Optional:**  can be turned on or off
* **Configurable:** accepts any column name and list of codes
* **Non-destructive:** only removes rows outside the target segment
* **Generic:** works with any industry classification system

```python
CNAES_DESEJADOS = ["6201-5/01", "6204-0/00", "6209-1/00"]  # example tech-related segments

df = filtrar_cnae(
    df,
    coluna_cnae = "CNAE",
    cnaes_permitidos=CNAES_DESEJADOS
)
```

If no list is provided, the pipeline runs normally with no filtering.

This design allows the script to be used both as:
* a generic spreadsheet cleaning tool
* a targeted ICP-building pipeline for specific market segments


## 💫 Tech stack

* **Python 3.x**
* **Pandas** (data manipulation)
* **NumPy** (high-performance handling of null/NaN values)
* **OpenPyXL** (excel I/O)


## 📋 How to use

1.  Clone this repository.
2.  Install dependencies:
    ```bash
    pip install pandas openpyxl
    ```
3.  Place your raw spreadsheet in the project folder.
4.  Open the script and adjust the input filename and MAPA_COLUNAS if necessary.
5.  Run the script to generate the clean output file.


## ⚠️ Privacy note (GDPR/LGPD)

This repository contains only the **source code** for automation. No spreadsheets containing real company data or personal information have been or will be shared publicly, in full compliance with data protection laws (GDPR/LGPD).


♡‧₊˚✧

### Developed by **Débora Tavares**
*Working in Sales Operations & Data Intelligence*


[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/deborasiltavares/)
