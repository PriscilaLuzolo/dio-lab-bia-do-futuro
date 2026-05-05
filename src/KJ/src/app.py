import streamlit as st
import pandas as pd
import json
from groq import Groq
from datetime import datetime

# ======= CONFIGURAÇÃO DA PÁGINA =======
st.set_page_config(page_title="Katherine Johnson - Mentoria Financeira", page_icon="🚀")

# ======= CARREGAR DADOS =======
@st.cache_data
def carregar_base():
    perfil = json.load(open('./Data/perfil_investidor.json', encoding='utf-8'))
    produtos = json.load(open('./Data/produtos_financeiros.json', encoding='utf-8'))
    transacoes = pd.read_csv('./Data/transacoes.csv', encoding='latin-1', sep=';')
    historico = pd.read_csv('./Data/historico_atendimento.csv', encoding='latin-1', sep=';')
    return perfil, produtos, transacoes, historico

perfil, produtos, transacoes, historico = carregar_base()

# ======= LÓGICA DE CONTEXTO  =======
def gerar_prompt_sistema():
    mes_atual = datetime.now().month
    essenciais = ['moradia', 'saude', 'alimentacao']
    gastos_monitorados = transacoes[(transacoes['tipo'] == 'saida') & (~transacoes['categoria'].isin(essenciais))]
    totais_cat = gastos_monitorados.groupby('categoria')['valor'].sum()
    
    limite_porcentagem = 0.35 if mes_atual == 12 else 0.20
    valor_limite = perfil['renda_mensal'] * limite_porcentagem
    
    alertas = [f"Categoria {cat}: R$ {v:.2f} (Limite: R$ {valor_limite:.2f})" 
               for cat, v in totais_cat.items() if v > valor_limite]

    return f"""Você é a Katherine Johnson, uma mentora e educadora financeira especializada em guiar jovens.
    OBJETIVO: Ajudar a organizar a vida financeira e atingir metas.
    REGRAS: 
    1. Use os dados: Nome {perfil['nome']}, Salário R$ {perfil['renda_mensal']} e outras informações {perfil}.
    2. Nunca invente dados, use apenas os fornecidos{transacoes}. Se não tiver resposta, diga que não sabe.
    3. Alertas atuais: {alertas if alertas else "Nenhum desvio"}.
    4. Use analogias leves (como missões espaciais ou trajetórias) para explicar conceitos financeiros mantendo a linguagem formal com foco no público jovem
    5. Nunca sugira investimentos, apenas explique-os (Base: {produtos}).
    6. Máximo 2 parágrafos responda de forma sucinta e sempre pergunte se o cliente entendeu.
    7. Qualquer pergunta fora do escopo financeiro, responda de forma educada que só pode ajudar com finanças. Lembrando o cliente que você é uma mentora financeira.Deixe isso salvo no seu sistema para futuras interações.{historico}
    """

# ======= INTERFACE DO CHAT =======
st.title("🚀Katherine Johnson, Sua mentora e educadora financeira")


# Inicializar histórico no Streamlit
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Olá, sou a Katherine, sua mentora e educadora financeira. Estou aqui para ajudar você a organizar sua vida financeira e alcançar suas metas."}
    ]

# Exibir mensagens anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrada do Usuário
if prompt := st.chat_input("Como posso te ajudar hoje?"):
    # Adicionar mensagem do usuário
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Chamada para o Groq
    try:
        client = Groq(api_key="coloque_sua_chave_aqui")
        
        # Prepara o contexto dinâmico
        full_system_prompt = gerar_prompt_sistema()
        
        response = client.chat.completions.create(
            messages=[{"role": "system", "content": full_system_prompt}] + 
                     [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
            model="llama-3.1-8b-instant",
        )
        
        full_response = response.choices[0].message.content
        
        with st.chat_message("assistant"):
            st.markdown(full_response)
        
        st.session_state.messages.append({"role": "assistant", "content": full_response})
        
    except Exception as e:
        st.error(f"Erro na comunicação com a base: {e}")