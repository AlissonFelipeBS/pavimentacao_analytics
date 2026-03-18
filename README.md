# Pavimentação Analytics

Projeto simples de análise e simulação de custos de obras de pavimentação utilizando Python, Machine Learning e Streamlit.

## 📊 Objetivo

Criar uma aplicação interativa capaz de estimar o custo de obras com base em parâmetros básicos como área, espessura e tipo de obra, além de permitir simulações rápidas com aplicação de BDI.

## ⚙️ Tecnologias utilizadas

* Python
* Pandas
* Scikit-learn
* Streamlit
* Plotly

## 🧠 Modelagem

Foi utilizado um modelo de regressão linear para prever o custo base da obra a partir das variáveis:

* Área (m²)
* Espessura (cm)
* Tipo de obra

O valor final é ajustado posteriormente com base no BDI informado pelo usuário.

## 📈 Funcionalidades

* Simulação de custo de obras em tempo real
* Aplicação de BDI com diferentes estratégias
* Visualização de indicadores (KPIs)
* Histórico de simulações
* Gráficos dinâmicos

## ⚠️ Observações

Este é um projeto com fins de estudo e experimentação.
O modelo foi treinado com dados sintéticos e simplificados, não representando a complexidade real do mercado.

## 🔧 Possíveis melhorias

* Utilizar dados reais de obras
* Incluir novas variáveis (materiais, equipamentos, produtividade, localização)
* Aplicar modelos mais robustos (Random Forest, XGBoost)
* Separar custo direto e indireto de forma mais detalhada
* Criar modelo de previsão de risco (estouro de custo)
* Persistir histórico de simulações em banco de dados

## 🚀 Como executar

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📌 Status do projeto

Finalizado como projeto de estudo.
