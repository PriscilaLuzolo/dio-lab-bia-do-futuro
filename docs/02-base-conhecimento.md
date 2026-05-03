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
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...
```
