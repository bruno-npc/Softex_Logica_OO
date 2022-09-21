class Carro:
  def __init__(self, modelo: str, ano: int, potencia: float):
    self.modelo = modelo
    self.ano = ano
    self.potencia = potencia

  def mostrar_modelo(self):
    print(f'\n\nModelo do carro: {self.modelo}. \nAno de lançamento: {self.ano} '
          f'\nPotência: {self.potencia} cv.')

  def nome_dono(self, nome: str):
    print(f'Dono do veiculo: {nome}')

  def atualizacao_potencia(self, potencia: float):
    self.potencia = potencia
    print(f'Potência modificada, novo valor: {potencia} cv.\n\n')
