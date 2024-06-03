# Integrantes
 
# Nome: Lucas de Sousa Andrade
# RGM: 27963217

# Nome: Elismar Silva de Oliveira
# RGM: 25894323

# Nome: João Victor Azeredo de Morais
# RGM: 26429594

class ChatbotAgenciaViagem:

  def __init__(self):

    # Dicionário de Regiões e seus estados
    self.regioes = {
        "Norte": ["Acre", "Amapá", "Amazonas", "Pará", "Rondônia", "Tocantins"],
        "Nordeste": ["Alagoas", "Bahia", "Ceará", "Maranhão", "Paraíba", "Pernambuco","Piauí", "Rio Grande do Norte", "Sergipe"],
        "Centro-Oeste": ["Distrito Federal", "Goiás", "Mato Grosso", "Mato Grosso do Sul"],
        "Sudeste": ["Espírito Santo", "Minas Gerais", "Rio de Janeiro", "São Paulo"],
        "Sul": ["Paraná", "Rio Grande do Sul", "Santa Catarina"],
    }

    # Dicionário dos valores das passagens aéreas por região
    self.passagem_aerea = {
      "Norte": 300.00,
      "Nordeste" : 250.00,
      "Centro-Oeste" : 350.00,
      "Sudeste" : 400.00,
      "Sul" : 320.00,
    }

    # Dicionário dos valores de diária por estado
    self.estados = {
        "Acre": 150.00,
        "Amapá": 180.00,
        "Amazonas": 200.00,
        "Pará": 170.00,
        "Rondônia": 160.00,
        "Tocantins": 140.00,
        "Alagoas": 120.00,
        "Bahia": 130.00,
        "Ceará": 110.00,
        "Maranhão": 100.00,
        "Paraíba": 90.00,
        "Pernambuco": 115.00,
        "Piauí": 80.00,
        "Rio Grande do Norte": 105.00,
        "Sergipe": 125.00,
        "Distrito Federal": 165.00,
        "Goiás": 155.00,
        "Mato Grosso": 175.00,
        "Mato Grosso do Sul": 185.00,
        "Espírito Santo": 145.00,
        "Minas Gerais": 135.00,
        "Rio de Janeiro": 190.00,
        "São Paulo": 210.00,
        "Paraná": 150.00,
        "Rio Grande do Sul": 160.00,
        "Santa Catarina": 170.00,
    }

    # Dicionário dos valores dos opcionais da viagem
    self.valores_adicionais = {
        "cafe_manha": 30.00,
        "transporte": 50.00,
        "guia_turistico": 100.00,
    }

  # Função para exibir as opções de regiões e valores de cada uma
  def escolher_regiao(self):
    print("Regiões do Brasil:\n")
    for i, regiao in enumerate(self.regioes.keys()):
      print(f"{i + 1}. {regiao} ({self.value_formatted(self.passagem_aerea[regiao])} passagem aérea)")
    while True:
      try:
        escolha_regiao = int(input("\nEscolha sua região (número): "))
        if 1 <= escolha_regiao <= len(self.regioes):
          return list(self.regioes.keys())[escolha_regiao - 1]
        else:
          print("Opção inválida. Tente novamente.")
      except ValueError:
        print("Valor inválido. Digite um número inteiro.")

  # Função para exibir os estados de cada região escolhida
  def escolher_estado(self, regiao):
    print(f"\nEstados da {regiao}:\n")
    estados_regiao = self.regioes[regiao]
    for i, estado in enumerate(estados_regiao):
      print(f"{i + 1}. {estado}")
    while True:
      try:
        escolha_estado = int(input("\nEscolha uma opção: "))
        if 1 <= escolha_estado <= len(estados_regiao):
          return estados_regiao[escolha_estado - 1]
        else:
          print("Opção inválida. Tente novamente.")
      except ValueError:
        print("Valor inválido. Digite um número inteiro.")

  # Função para exibir a escolha da quantidade de dias que deseja viajar
  def escolher_dias_estadia(self):
    while True:
      try:
        dias_estadia = int(input("Quantos dias deseja ficar? "))
        if dias_estadia > 0:
          return dias_estadia
        else:
          print("Quantidade inválida. Digite um número inteiro positivo.")
      except ValueError:
        print("Valor inválido. Digite um número inteiro.")

  # Função para exibir a escolha de café da manhã todos os dias
  def escolher_cafe_manha(self):
    while True:
      try:
        resposta_cafe_manha = int(input("Deseja incluir café da manhã? \n 1 para (Sim) \n 2 para (Não) \n"))
        if resposta_cafe_manha in [1, 2]:
          return resposta_cafe_manha == 1
        else:
          print("Resposta inválida. Digite 1 para 'sim' ou 2 para 'não'.")
      except ValueError:
        print("Entrada inválida. Digite um número inteiro (1 ou 2).")

  # Função para exibir a escolha de transporte todos os dias
  def escolher_transporte(self):
    while True:
      try:
        resposta_transporte = int(input("Deseja incluir transporte? \n 1 para (Sim) \n 2 para (Não) \n"))
        if resposta_transporte in [1, 2]:
          return resposta_transporte == 1
        else:
          print("Resposta inválida. Digite 1 para 'sim' ou 2 para 'não'.")
      except ValueError:
        print("Entrada inválida. Digite um número inteiro (1 ou 2).")

  # Função para exibir a escolha de guia turístico para todos os dias
  def escolher_guia_turistico(self):
    while True:
      try:
        resposta_guia_turistico = int(input("Deseja incluir guia turístico? \n 1 para (Sim) \n 2 para (Não) \n"))
        if resposta_guia_turistico in [1, 2]:
          return resposta_guia_turistico == 1
        else:
          print("Resposta inválida. Digite 1 para 'sim' ou 2 para 'não'.")
      except ValueError:
        print("Entrada inválida. Digite um número inteiro (1 ou 2).")

  # Função para calcular o valor total da viagem
  def calcular_valor_total(self, regiao, estado, dias_estadia, cafe_manha, passagem_aerea, transporte, guia_turistico):
    valor_total = self.estados[estado] * dias_estadia
    if cafe_manha:
      valor_total += self.valores_adicionais["cafe_manha"] * dias_estadia
    if transporte:
      valor_total += self.valores_adicionais["transporte"]
    if guia_turistico:
      valor_total += self.valores_adicionais["guia_turistico"]
    if passagem_aerea:
      valor_total += self.passagem_aerea[regiao]

    return self.value_formatted(valor_total)

  # Função onde retorna o resumo da viagem, com todas as informações escolhidas
  def mostrar_resumo(self, regiao, estado, dias_estadia, cafe_manha, passagem_aerea, transporte, guia_turistico, valor_total):

    print("\nResumo da sua viagem:\n")
    print(f"- Região: {regiao}")
    print(f"- Estado: {estado}")
    print(f"- Dias de estadia: {dias_estadia}")
    # print(f"- Diária: R${diaria:.2f}")

    if passagem_aerea:
      print(f"- Passagem aérea (opcional): {self.value_formatted(self.passagem_aerea[regiao])}")
    if cafe_manha:
      print(f"- Café da manhã (opcional): {self.value_formatted(self.valores_adicionais['cafe_manha'])} por dia")
    if transporte:
      print(f"- Transporte (opcional): {self.value_formatted(self.valores_adicionais['transporte'])}")
    if guia_turistico:
      print(f"- Guia turístico (opcional): {self.value_formatted(self.valores_adicionais['guia_turistico'])}")

    print(f"\nValor total: {valor_total}")


  def value_formatted(self, valor):
    return "R${:,.2f}".format(valor).replace(",", "X").replace(".", ",").replace("X", ".")


if __name__ == "__main__":
  agencia_viagem = ChatbotAgenciaViagem()

  # Iniciar o chatbot
  regiao = agencia_viagem.escolher_regiao()
  estado = agencia_viagem.escolher_estado(regiao)
  dias_estadia = agencia_viagem.escolher_dias_estadia()
  cafe_manha = agencia_viagem.escolher_cafe_manha()
  transporte = agencia_viagem.escolher_transporte()
  guia_turistico = agencia_viagem.escolher_guia_turistico()
  passagem_aerea = agencia_viagem.passagem_aerea[regiao]

  valor_total = agencia_viagem.calcular_valor_total(regiao, estado, dias_estadia, cafe_manha, passagem_aerea, transporte, guia_turistico)

  # Mostrar o resumo da viagem e o valor total
  agencia_viagem.mostrar_resumo(regiao, estado, dias_estadia, cafe_manha, passagem_aerea,transporte, guia_turistico, valor_total)
