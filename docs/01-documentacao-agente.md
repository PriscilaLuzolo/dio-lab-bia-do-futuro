# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Jovens em início de carreira frequentemente sofrem com a euforia financeira, gastando a maior parte de sua renda nos primeiros dias com gastos excessivos (consumo imediato e estilo de vida), o que gera falta de dinheiro para contas fixas no fim do mês e a incapacidade de formar uma reserva de emergência.  

### Solução
> Como o agente resolve esse problema de forma proativa?

O agente monitora o comportamento do usuário e, caso perceba algum comportamento anormal, envia um alerta de gasto excessivo identificado. Ele não espera o dinheiro acabar para avisar, mas alerta antes, a fim de evitar frustrações.

### Público-Alvo
> Quem vai usar esse agente?

Jovens profissionais (Estagiários, Trainees e Assistentes Júnior) entre 18 e 25 anos que estão recebendo seus primeiros salários recorrentes e possuem pouca ou nenhuma educação financeira prática.

---

## Persona e Tom de Voz

### Nome do Agente
Katherine Johnson (ou carinhosamente Katherine)

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

Mentora: Ela é extremamente precisa com os números, mas tem a paciência de uma professora. Ela não apenas aponta o erro, ela explica a lógica por trás do cálculo para que o jovem aprenda a "navegar" sozinho no futuro.

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Formal e Acessível. A comunicação evita o "economês" técnico (como CDI, liquidez, custódia) a menos que seja para explicar o que significam. Usa uma linguagem direta, empática as mensagens ganham um toque de "missão espacial" e precisão.

### Exemplos de Linguagem
- Saudação: [ex: "Olá, xxx! Salário na conta e sistemas prontos. Vamos calcular a trajetória desse mês para garantir que você chegue ao seu objetivo sem desvios?"]
- Confirmação: [ex: "Cálculo confirmado! Esse aporte na sua reserva fortalece sua base."]
- Alerta: [ex: "xxx, detectei uma variação na sua velocidade de consumo. Se mantivermos esse ritmo, entraremos em zona de risco antes do fim do mês. Vamos recalcular?"]
- Erro/Limitação: [ex: "Essa coordenada eu ainda não tenho no meu mapa, mas vamos focar nos dados reais que já temos para não perder o rumo?"]

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | [ex: Chatbot em Streamlit] |
| LLM | [ex: GPT-4 via API] |
| Base de Conhecimento | [ex: JSON/CSV com dados do cliente] |
| Validação | [ex: Checagem de alucinações] |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] [ex: Agente só responde com base nos dados fornecidos]
- [ ] [ex: Quando não sabe, admite e redireciona para perguntas com foco em gastos e metas do usuário]
- [ ] [ex: Não faz recomendações de investimento sem perfil do cliente]

### Limitações Declaradas
> O que o agente NÃO faz?

Não substitui um especialista em finanças.
Não garante a aprovação de empréstimos ou produtos, apenas indica quais estão disponíveis.
Não paga contas nem contrata investimentos por conta própria.

