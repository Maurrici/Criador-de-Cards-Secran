# 🧠 Automatizador de Criação de Cards - Secran

Este script automatiza o processo de criação de cards no sistema [Secran Digital](https://secran.digital) com base em dados de uma planilha Excel.

## 📦 Requisitos

- Python 3.8+
- Google Chrome instalado
- ChromeDriver compatível com sua versão do Chrome (adicione ao PATH)

## 🛠️ Instalação das Dependências

1. Clone ou baixe este repositório.
2. Certifique-se de que o arquivo `planilha_cards.xlsx` esteja no mesmo diretório do script `learning.py`.
3. Instale as dependências com o comando: `pip install -r requirements.txt`

## 🚀 Executando o Script

Com tudo configurado, execute:

```bash
python learning.py
```

O script irá:

- Abrir o navegador com Selenium  
- Fazer login automaticamente  
- Criar cards com base nos dados da planilha Excel  

## 🧾 Sobre a Planilha

A planilha deve conter as seguintes colunas (com esses nomes exatamente):

| Modelo | Título | Data | Responsável | Tag | Baixa |
|--------|--------|------|-------------|-----|-------|

A data deve estar no formato `DD/MM/YYYY`.

A coluna baixa deve ser preenchida apenas para cards que devem ser concluídos logo após a criação.

## ⚠️ Observações

- Certifique-se de que os nomes de modelos, responsáveis e tags estão corretos.
- A execução depende da estrutura atual da página. Mudanças no layout podem exigir ajustes no script.
- Verifique se o navegador Chrome está atualizado e compatível com o ChromeDriver.