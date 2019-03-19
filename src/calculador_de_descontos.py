from src.orcamento import Orcamento, Item
from src.descontos import Desconto_por_cinco_itens, Desconto_por_mais_de_quinhentos_reais, Sem_desconto


class Calculador_de_descontos:
    def calcula(self, orcamento):
        desconto = Desconto_por_cinco_itens(Desconto_por_mais_de_quinhentos_reais(Sem_desconto()))

        return desconto.calcula(orcamento)


if __name__ == '__main__':
    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM - 1', 100))
    orcamento.adiciona_item(Item('ITEM - 2', 50))
    orcamento.adiciona_item(Item('ITEM - 3', 100))

    print(f'Orçamento de: {orcamento.valor:.2f}')

    calculador = Calculador_de_descontos()

    desconto = calculador.calcula(orcamento)
    print(f'Desconto de: {desconto:.2f}')