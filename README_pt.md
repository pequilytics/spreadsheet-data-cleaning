# Pipeline de limpeza e qualificação de leads (construção civil)

Este projeto consiste em um script Python automatizado para limpeza, padronização e qualificação de bases de dados de empresas (leads), focado especificamente no setor de **construção civil**.
O objetivo é transformar listas brutas e "sujas" em uma base qualificada de **ICP (Ideal Customer Profile)**, filtrando apenas construtoras e incorporadoras relevantes e removendo duplicidades complexas.


## Funcionalidades

### 1. Filtragem inteligente por CNAE
O script isola apenas empresas com atividades econômicas estratégicas, eliminando reformas pequenas e obras irrelevantes:
- **4120-4/00:** construção de edifícios.
- **4110-7/00:** incorporação de empreendimentos imobiliários.
- **4399-1/01:** administração de obras.

### 2. Deduplicação segura
Algoritmo personalizado que remove duplicatas sem perder dados. Ele verifica múltiplos critérios em ordem de prioridade:
1.  **CNPJ** (identificador único).
2.  **Website** (empresas do mesmo grupo).
3.  **E-mail e Telefone** (contatos repetidos).
*Obs: O algoritmo protege campos vazios, garantindo que empresas sem site/email não sejam excluídas incorretamente.*


## Tecnologias utilizadas

* **Python 3.x**
* **Pandas** (Manipulação de dados e Dataframes)
* **OpenPyXL** (Leitura e escrita de arquivos Excel)


## Como usar

1.  Clone este repositório.
2.  Instale as dependências:
    ```bash
    pip install pandas openpyxl
    ```
3.  Coloque sua planilha bruta na pasta do projeto.
4.  Abra o arquivo `.ipynb` (Jupyter notebook) e ajuste o nome do arquivo de entrada.
5.  Execute as células para gerar o arquivo `planilha-limpinha.xlsx`.

## Nota sobre privacidade (LGPD)

Este repositório contém apenas o **código-fonte** da automação. Nenhuma planilha com dados reais de empresas ou pessoas foi ou será compartilhada publicamente, em conformidade com as leis de proteção de dados.


♡‧₊˚✧
### Desenvolvido por **[Débora Tavares]**
*Atuando em Sales Operations & Data Intelligence*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/deborasiltavares/)
