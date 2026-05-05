# Código da Aplicação

Esta pasta contém o código do seu agente financeiro.

## Estrutura Sugerida

```
src/
├── app.py              # Aplicação principal (Streamlit)
├── agente.py           # Lógica do agente
├── config.py           # Configurações (API keys do Groq)

```

## Exemplo de requirements.txt

```
streamlit
pandas
groq
python-dotenv
```

## Como Rodar

```bash
# Instalar dependências
pip install streamlit pandas groq

# Rodar a aplicação
python -m streamlit run src/app.py
```
