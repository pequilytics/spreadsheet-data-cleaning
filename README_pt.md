# Pipeline de qualificação e deduplicação de leads

[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

> **Higienização, padronização e deduplicação inteligente automatizada para bases de empresas (foco em construção civil).**


<p align="center">
  <a href="#README.md"> Read in english</a>
</p>

---

## ⭐ Visão geral
Este projeto consiste em um script Python automatizado para **higienização, padronização e qualificação** de bases de dados de empresas (leads), com foco no **setor da construção civil**.

O objetivo é transformar listas brutas e "sujas" em uma base **ICP (Ideal Customer Profile)** confiável, aplicando algoritmos avançados para remover duplicatas complexas sem perder contatos valiosos.

## 🏷️ Funcionalidades

#### 1. deduplicação em cascata (waterfall)
Diferente da remoção de duplicatas padrão do Excel ou Pandas, este algoritmo utiliza uma abordagem hierárquica e **segura**:
* **Hierarquia de confiança:** verifica duplicidade na seguinte ordem de prioridade:
    1.  `CNPJ` (identificador fiscal único)
    2.  `Website`
    3.  `E-mail` & `Telefone`
    4.  `Razão Social` (nomes similares)
* **Preservação de dados (safe-null):** o algoritmo **não exclui** linhas apenas porque um campo está vazio. Se uma empresa não tem site, ela é preservada para ser verificada pelo telefone ou e-mail.

#### 2. Score de completude
Antes de remover uma duplicata, o script calcula um *score* para cada linha. Se houver três registros da mesma empresa, o sistema manterá automaticamente aquele que tiver **mais colunas preenchidas**, garantindo a melhor qualidade de dado possível.

#### 3. Normalização inteligente
Os dados são padronizados em tempo de execução para comparação (sem alterar o dado original salvo):
* **Websites:** `https://www.site.com`, `www.site.com/` e `site.com` são tratados como iguais.
* **CNPJ/Tel:** remoção de pontuações e formatação.
* **Textos:** tratamento de espaços extras e *case sensitivity*.

###  Configuração

O script é altamente configurável através de um dicionário de mapeamento. Você pode adaptar para qualquer planilha alterando a variável `MAPA_COLUNAS` no código:

```python
MAPA_COLUNAS = {
    "CNPJ": "CNPJ",               # Coluna Chave: Nome no Excel
    "Razão Social": "Razão Social",
    "Website": "Websites",
    "E-mail": "E-mails",
    # ... adicione suas colunas
}
```

## 💫 Tecnologias utilizadas

* **Python 3.x**
* **Pandas** (manipulação de dados e dataframes)
* **NumPy** (tratamento de alta performance para valores nulos)
* **OpenPyXL** (Leitura e escrita de arquivos Excel)


## 📋 Como usar

1.  Clone este repositório.
2.  Instale as dependências:
    ```bash
    pip install pandas openpyxl
    ```
3.  Coloque sua planilha bruta na pasta do projeto.
4.  Abra o script e ajuste o nome do arquivo de entrada e o MAPA_COLUNAS se necessário.
5.  Execute o script para gerar o arquivo limpo.

## ⚠️ Nota sobre privacidade (LGPD)

Este repositório contém apenas o **código-fonte** da automação. Nenhuma planilha com dados reais de empresas ou dados pessoais foi ou será compartilhada publicamente, em conformidade com as leis de proteção de dados.


♡‧₊˚✧
### Desenvolvido por **Débora Tavares**
*Atuando em Sales Operations & Data Intelligence*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/deborasiltavares/)
