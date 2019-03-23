from abc import ABC, abstractmethod


class EstadoDeUmOrcamento(ABC):
    @abstractmethod
    def aplica_desconto_extra(self, orcamento):
        pass

    @abstractmethod
    def aprova(self, orcamento):
        pass

    @abstractmethod
    def reprova(self, orcamento):
        pass

    @abstractmethod
    def finaliza(self, orcamento):
        pass


class EmAprovacao(EstadoDeUmOrcamento):
    def aprova(self, orcamento):
        orcamento.estado_atual = Aprovado()

    def reprova(self, orcamento):
        orcamento.estado_atual = Reprovado()

    def finaliza(self, orcamento):
        raise Exception('Orçamento em aprovação não pode ser finalizado')

    def aplica_desconto_extra(self, orcamento):
        orcamento.desconto_extra = orcamento.valor * 0.02


class Aprovado(EstadoDeUmOrcamento):
    def aprova(self, orcamento):
        raise Exception('Oçamento já foi aprovado')

    def reprova(self, orcamento):
        raise Exception('Oçamento já foi aprovado')

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()

    def aplica_desconto_extra(self, orcamento):
        orcamento.desconto_extra = orcamento.valor * 0.05


class Reprovado(EstadoDeUmOrcamento):
    def aprova(self, orcamento):
        raise Exception('Oçamento já foi reprovado')

    def reprova(self, orcamento):
        raise Exception('Oçamento já foi reprovado')

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()

    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orçamentos reprovados não recebem desconto extra')


class Finalizado(EstadoDeUmOrcamento):
    def aprova(self, orcamento):
        raise Exception('Oçamento já foi finalizado')

    def reprova(self, orcamento):
        raise Exception('Oçamento já foi finalizado')

    def finaliza(self, orcamento):
        raise Exception('Oçamento já foi finalizado')

    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orçamentos finalizados não recebem desconto extra')


class Orcamento:

    def __init__(self):
        self.__itens = []
        self.estado_atual = EmAprovacao()
        self.__desconto_extra = 0

    @property
    def valor(self):
        total = 0.0

        for item in self.__itens:
            total += item.valor

        return total - self.__desconto_extra

    def obter_itens(self):
        return tuple(self.__itens)

    @property
    def total_itens(self):
        return len(self.__itens)

    @property
    def desconto_extra(self):
        return self.__desconto_extra

    @desconto_extra.setter
    def desconto_extra(self, desconto):
        self.__desconto_extra = desconto

    def adiciona_item(self, item):
        self.__itens.append(item)

    def aplica_desconto_extra(self):
        self.estado_atual.aplica_desconto_extra(self)


    def aprova(self):
        self.estado_atual.aprova(self)

    def reprova(self):
        self.estado_atual.reprova(self)

    def finaliza(self):
        self.estado_atual.finaliza(self)


class Item:
    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @property
    def nome(self):
        return self.__nome


if __name__ == '__main__':
    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM - 1', 200))
    orcamento.adiciona_item(Item('ITEM - 2', 50))
    orcamento.adiciona_item(Item('ITEM - 3', 250))

    print(orcamento.valor)
    orcamento.estado_atual = EmAprovacao()
    orcamento.aplica_desconto_extra()
    print(orcamento.valor)