# Bot Agência de Viagem

Este projeto é um bot de agência de viagem desenvolvido em Python. Ele auxilia os usuários a planejar suas viagens, escolhendo a região e o estado de destino, a duração da estadia, e opcionalmente, incluindo serviços adicionais como café da manhã, transporte e guia turístico. O bot calcula o custo total da viagem com base nas escolhas do usuário.

## Funcionalidades

- Escolha da região de destino.
- Escolha do estado dentro da região escolhida.
- Definição da quantidade de dias de estadia.
- Inclusão opcional de serviços adicionais:
  - Café da manhã.
  - Transporte.
  - Guia turístico.
- Cálculo do custo total da viagem.
- Resumo detalhado da viagem e do custo total.

## Estrutura do Projeto

- `regioes`: Dicionário contendo as regiões do Brasil e os estados pertencentes a cada região.
- `passagem_aerea`: Dicionário contendo os valores das passagens aéreas por região.
- `estados`: Dicionário contendo os valores das diárias por estado.
- `valores_adicionais`: Dicionário contendo os valores dos serviços adicionais.

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone este repositório:
   ```bash
   git clone https://github.com/ElismarSilva/Bot_viagem_LFA
                                                                        
