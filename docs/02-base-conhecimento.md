# Base de Conhecimento
>[!TIP]
> Prompt usado para esta etapa:
>
> Utilize a base de dados da agente "Katherine Johnson", organize os 4 arquivos em anexo. Explique para que serve cada arquivo e monte um exemplo de contexto para cada arquivo.

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Ele armazena as conversas anteriores, dúvidas já tiradas e alertas enviados |
| `perfil_investidor.json` | JSON | Ele contém os dados demográficos, a renda, os objetivos de vida e, crucialmente, o nível de tolerância a riscos. |
| `produtos_financeiros.json` | JSON | Ele lista as opções de onde o dinheiro pode ser alocado, detalhando riscos, rentabilidade e aporte mínimo |
| `transacoes.csv` | CSV | Monitora o consumo de recursos atual |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os dados das transações.csv foram expandidos para atender melhor ao projeto. Foram adicionados 20 novos registros, melhorando a performance do agente na análise de comportamento e permitindo o envio de alertas de gastos excessivos. Campos adicionados: Delivery e Vestuário.

Os dados de histórico_atendimento foram modificados e expandidos. Dez novas linhas foram adicionadas para tornar as conversas mais adaptadas ao contexto do agente Katherine.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

[ex: Os JSON/CSV são carregados no início da sessão e incluídos no contexto do prompt]

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

[Sua descrição aqui]

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
DADOS DO PERFIL:
{
  "nome": "João Silva",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 5000.00,
  "perfil_investidor": "moderado",
  "objetivo_principal": "Construir reserva de emergência",
  "patrimonio_total": 15000.00,
  "reserva_emergencia_atual": 10000.00,
  "aceita_risco": false,
  "metas": [
    {
      "meta": "Completar reserva de emergência",
      "valor_necessario": 15000.00,
      "prazo": "2026-06"
    },
    {
      "meta": "Entrada do apartamento",
      "valor_necessario": 50000.00,
      "prazo": "2027-12"
    }
  ]
}
TRANSACOES DO CLIENTE:

data;descricao;categoria;valor;tipo
01/10/2025;Salário;receita;5000.00;entrada
02/10/2025;Aluguel;moradia;1200.00;saida
03/10/2025;Supermercado;alimentacao;450.00;saida
05/10/2025;Netflix;lazer;55.90;saida
07/10/2025;Farmácia;saude;89.00;saida
10/10/2025;Restaurante;alimentacao;120.00;saida
12/10/2025;Uber;transporte;45.00;saida
15/10/2025;Conta de Luz;moradia;180.00;saida
20/10/2025;Academia;saude;99.00;saida
25/10/2025;Combustível;transporte;250.00;saida
01/11/2025;Salario;receita;5000.00;entrada
02/11/2025;Aluguel;moradia;1200.00;saida
02/11/2025;iFood - Burguer King;delivery;45.90;saida
03/11/2025;Supermercado;alimentacao;450.00;saida
04/11/2025;iFood - Japones;delivery;89.90;saida
05/11/2025;Uber Eats - Padaria;delivery;25.00;saida
06/11/2025;Zattini - Tenis Novo;vestuario;189.90;saida
07/11/2025;iFood - Marmita Fit;delivery;32.00;saida
08/11/2025;Netflix;lazer;55.90;saida
10/11/2025;iFood - McDonald's;delivery;54.00;saida
11/11/2025;Renner - Calça Jeans;vestuario;119.90;saida
12/11/2025;iFood - Sorvete;delivery;18.00;saida
13/11/2025;99Food - Chines;delivery;47.00;saida
14/11/2025;iFood - Café da Manhã;delivery;28.90;saida
15/11/2025;Conta de Luz;moradia;180.00;saida
15/11/2025;H&M - Camisetas;vestuario;150.00;saida
16/11/2025;iFood - Hot Dog;delivery;21.00;saida
17/11/2025;Uber;transporte;35.00;saida
18/11/2025;iFood - Poke Bowl;delivery;58.00;saida
19/11/2025;iFood - Sobremesa;delivery;15.50;saida
20/11/2025;Combustível;transporte;250.00;saida
20/11/2025;Shein - Acessórios;vestuario;85.00;saida
20/11/2025;Academia;saude;99.00;saida
21/11/2025;99Food - Pastelaria;delivery;33.00;saida
22/11/2025;Freelance;receita;350.00;entrada
23/11/2025;iFood - Sanduíche natural;delivery;24.00;saida
24/11/2025;Nike - Meias e Short;vestuario;130.00;saida
25/11/2025;99Food - Yakisoba;delivery;42.00;saida
26/11/2025;iFood - Taco Bell;delivery;38.50;saida
27/11/2025;iFood - Combo Sushi;delivery;110.00;saida

HISTÓRICO DE ATENDIMENTO:

data;canal;tema;resumo;resolvido
22/09/2025;telefone;Problema no app;Erro ao visualizar extrato foi corrigido;sim
01/10/2025;chat;Tesouro Selic;Cliente pediu explicação sobre o funcionamento do Tesouro Direto;sim
12/10/2025;chat;Metas financeiras;Cliente acompanhou o progresso da reserva de emergência;sim
25/10/2025;email;Atualização cadastral;Cliente atualizou e-mail e telefone;sim
02/11/2025;chat;Alerta de Gastos;Katherine alertou sobre 3 pedidos de delivery seguidos na mesma semana;sim
05/11/2025;chat;Metas financeiras;Cliente perguntou se o gasto com delivery atrasaria a meta do notebook;sim
07/11/2025;chat;Alerta de Gastos;Aviso de excesso de carga no módulo 'Vestuário' após compra de tênis;sim
10/11/2025;chat;Educação Financeira;Explicação sobre a diferença entre Renda Fixa e Variável para o perfil moderado;sim
15/11/2025;chat;Alerta de Gastos;Alerta de vazamento de combustível: 10 pedidos de iFood atingidos no mês;sim
18/11/2025;chat;Metas financeiras;Recálculo de trajetória para reserva de emergência após gastos extras;sim
22/11/2025;chat;Alerta de Gastos;Aviso de turbulência: Gastos com lazer ultrapassaram 20% da renda mensal;sim
24/11/2025;chat;Planejamento;Cliente pediu para simular compra de notebook parcelado vs à vista;sim
26/11/2025;chat;Alerta de Gastos;Katherine detectou gasto crítico em delivery que compromete o aporte do mês;sim
28/11/2025;chat;Revisão Mensal;Relatório final de novembro: Identificado excesso de peso em delivery e roupas;sim

PRODUTOS FINANCEIROS PARA ESNINO DO CLIENTE:
[
  {
    "nome": "Tesouro Selic",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "100% da Selic",
    "aporte_minimo": 30.00,
    "indicado_para": "Reserva de emergência e iniciantes"
  },
  {
    "nome": "CDB Liquidez Diária",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "102% do CDI",
    "aporte_minimo": 100.00,
    "indicado_para": "Quem busca segurança com rendimento diário"
  },
  {
    "nome": "LCI/LCA",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "95% do CDI",
    "aporte_minimo": 1000.00,
    "indicado_para": "Quem pode esperar 90 dias (isento de IR)"
  },
  {
    "nome": "Fundos Imobiliários",
    "categoria": "fundo",
    "risco": "medio",
    "rentabilidade": "de  0,7% a mais de 1% ao mês",
    "aporte_minimo": 10,
    "indicado_para": "Perfil moderado que busca diversificação"
  },
  {
    "nome": "Fundo de Ações",
    "categoria": "fundo",
    "risco": "alto",
    "rentabilidade": "Variável",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil arrojado com foco no longo prazo"
  }
]


...
```
