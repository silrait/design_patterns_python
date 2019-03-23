from abc import ABC, abstractmethod


class Imposto(ABC):
    def __init__(self, outro_imposto = None):
        self.__outro_imposto = outro_imposto

    def _calculo_do_outro_imposto(self, orcamento):
        return self.__outro_imposto.calcula(orcamento) if self.__outro_imposto else 0

    @abstractmethod
    def calcula(self, orcamento):
        return self._calculo_do_outro_imposto(orcamento)


class Template_de_imposto_condicional(Imposto):
    def calcula(self, orcamento):
        if self._deve_usar_maxima_taxacao(orcamento):
            return self._maxima_taxacao(orcamento) + super().calcula(orcamento)
        else:
            return self._minima_taxacao(orcamento) + super().calcula(orcamento)

    @abstractmethod
    def _deve_usar_maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def _maxima_taxacao(self, orcamento):
        pass

    @abstractmethod
    def _minima_taxacao(self, orcamento):
        pass


# python decorator
def IPVX(metodo_ou_funcao):
    def wrapper(self, orcamento):
        return metodo_ou_funcao(self, orcamento) + 50
    return wrapper


class ICMS(Imposto):
    @IPVX
    def calcula(self, orcamento):
        return orcamento.valor * 0.1 + super().calcula(orcamento)


class ISS(Imposto):
    @IPVX
    def calcula(self, orcamento):
        return orcamento.valor * 0.06 + super().calcula(orcamento)


class ICPP(Template_de_imposto_condicional):

    def _maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.07

    def _minima_taxacao(self, orcamento):
        return orcamento.valor * 0.05

    def _deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500


class IKCV(Template_de_imposto_condicional):
    def _deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500 and self.__tem_item_maior_que_100_reais(orcamento)

    def _maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.1

    def _minima_taxacao(self, orcamento):
        return orcamento.valor * 0.06

    def __tem_item_maior_que_100_reais(self, orcamento):
        for item in orcamento.obter_itens():
            if item.valor > 100:
                return True
        return False