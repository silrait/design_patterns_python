# -*- coding: UTF-8 -*-
# Nota_fiscal.py
from datetime import date


class Item:

    def __init__(self, descricao, valor):
        self.__descricao = descricao
        self.__valor = valor

    @property
    def descricao(self):
        return self.__descricao

    @property
    def valor(self):
        return self.__valor


class Nota_fiscal:

    def __init__(self, razao_social, cnpj, itens, data_de_emissao, detalhes):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__data_de_emissao = data_de_emissao
        if len(detalhes) > 20:
            raise Exception('Detalhes da nota não pode ter mais do que 20 caracteres')
        self.__detalhes = detalhes
        self.__itens = itens

    @property
    def razao_social(self):
        return self.__razao_social

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def data_de_emissao(self):
        return self.__data_de_emissao

    @property
    def detalhes(self):
        return self.__detalhes


if __name__ == '__main__':

    from src.criador_nota_fiscal import CriadorNotaFiscal

    itens = [Item('ITEM A', 100), Item('ITEM B', 200)]

    nota_fiscal = Nota_fiscal(
        'FHSA Limitada',
        '012345678901234',
        itens,
        date.today(),
        ''
    )

    nota_criada_com_builder = (CriadorNotaFiscal()
                               .com_razao_social('FHSA Limitada')
                               .com_cnpj('01234567891234')
                               .com_itens(itens)
                               .com_data_de_emissao(date.today())
                               .constroi())