class BombaCombustivel:
    def __init__(self):
        self._tipoCombustivel = ""
        self._valorLitro = 0
        self._quantidadeCombustivel = 0

    def __str__(self):
        mensagem = f"""
                      Bomba Combustivel
              --------------------------------
            Tipo de combustivel         {self.tipoCombustivel}
            Valor por litro             R$ {self.valorLitro:.2f}
            Quantidade de combustivel   {self.quantidadeCombustivel:.2f} L

        """
        return mensagem

    #tipo Combustivel
    @property
    def tipoCombustivel(self):
        return self._tipoCombustivel.capitalize()
    
    @tipoCombustivel.setter
    def tipoCombustivel(self, val):
        self._tipoCombustivel = val

    #quantidade combustivel
    @property
    def quantidadeCombustivel(self):
        return self._quantidadeCombustivel

    @quantidadeCombustivel.setter
    def quantidadeCombustivel(self, val: float):
        if not isinstance(val, (int,float)):
            raise TypeError()
        if val >= 0:
            self._quantidadeCombustivel = val
        else:
            raise ValueError("Digite um valor valido")
    #valor do litro
    @property
    def valorLitro(self):
        return self._valorLitro

    @valorLitro.setter
    def valorLitro(self, val: float):
        if not isinstance(val, (int,float)):
            raise TypeError()
        if val > 0:
            self._valorLitro = val
        else:
            raise ValueError("Digite um valor valido")


    def abastecerPorValor(self, val: float):
        if not isinstance(val, (int,float)):
            raise TypeError()
        if val < 0:
            raise ValueError("Digite um valor valido e positivo")

        qtd_combustivel = val / self.valorLitro
        if qtd_combustivel > self.quantidadeCombustivel:
            print(f"Quantiade de combustivel na bomba indisponviel")
            print(f"Valor maximo possível no momento R${(self.quantidadeCombustivel / self.valorLitro):.2f}")
            return False
        else:
            self.quantidadeCombustivel = self.quantidadeCombustivel - qtd_combustivel
            print(f"Abastecido {qtd_combustivel:.2f}L de {self.tipoCombustivel}")
            return True

    def abastecerPorLitro(self, litros: float):
        if not isinstance(litros, (int,float)):
            raise TypeError()
        if litros < 0:
            raise ValueError("Digite um valor válido e positivo")
        if litros > self.quantidadeCombustivel:
            print("Quantidade de combustivel na bomba indisponivel")
            print(f"Quantidade maxima disponivel no momento: {self.quantidadeCombustivel}")
            return False
        else:
            valor = litros*self.valorLitro
            print(f"""  
                Valor a ser pago:          {valor:.2f}
                Quantidade de combustivel: {litros:.2f}
            """)

            self.quantidadeCombustivel = self.quantidadeCombustivel - litros
            return True


bomba = BombaCombustivel()
bomba.valorLitro = 5.42
bomba.tipoCombustivel = "gasolina"
bomba.quantidadeCombustivel = 500
bomba.abastecerPorLitro(500)
#print(bomba)



