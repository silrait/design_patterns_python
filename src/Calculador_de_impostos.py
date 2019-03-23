from src.orcamento import Orcamento, Item
from src.impostos import ICMS, ISS, ICPP, IKCV


class Calculador_de_impostos:
    def realiza_calculo(self, orcamento, imposto):
        imposto_calculado = imposto.calcula(orcamento)
        print(imposto_calculado)


if __name__ == '__main__':
    calculador = Calculador_de_impostos()

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM - 1', 200))
    orcamento.adiciona_item(Item('ITEM - 2', 50))
    orcamento.adiciona_item(Item('ITEM - 3', 250))

    print(f'Orçamento de: {orcamento.valor:.2f}')

    print('ISS e ICMS')
    calculador.realiza_calculo(orcamento, ISS())
    calculador.realiza_calculo(orcamento, ICMS())

    print('ICMS com ISS')
    calculador.realiza_calculo(orcamento, ICMS(ISS()))

    print('ICPP e IKCV')
    calculador.realiza_calculo(orcamento, ICPP())
    calculador.realiza_calculo(orcamento, IKCV())

    print('ICPP com IKCV')
    calculador.realiza_calculo(orcamento, ICPP(IKCV()))


