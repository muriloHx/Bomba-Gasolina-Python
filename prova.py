class BombaCombustivel:
    def __init__(self):
        self._tipoCombustivel = ""
        self._valorLitro = 0
        self._quantidadeCombustivel = 0


    #tipo Combustivel
    @property
    def tipoCombustivel(self):
        return self._tipoCombustivel.capitalize()
    
    @tipoCombustivel.setter
    def tipoCombustivel(self, val):
        self._tipoCombustivel = val

    #qtdcombustivel
    @property
    def quantidadeCombustivel(self):
        return self._quantidadeCombustivel

    @quantidadeCombustivel.setter
    def quantidadeCombustivel(self, val):
        if val > 0:
            self._quantidadeCombustivel = val
        else:
            raise ValueError("Digite um valor valido")
    #valorLitro
    @property
    def valorLitro(self):
        return self._valorLitro

    @valorLitro.setter
    def valorLitro(self, val):
        if val > 0:
            self._valorLitro = val
        else:
            raise ValueError("Digite um valor valido")


    def abastecerPorValor(self, valor: float):
        if valor < 0:
            raise ValueError("Digite um valor valido")
        qtd_combustivel = valor / self.valorLitro
        if qtd_combustivel > self.quantidadeCombustivel:
            print(f"Quantiade de combustivel na bomba indisponviel")
            print(f"Valor maximo possível no momento R${(self.quantidadeCombustivel / self.valorLitro):.2f}")
            return 0
        else:
            self.quantidadeCombustivel = self.quantidadeCombustivel - qtd_combustivel
            print(f"Abastecido {qtd_combustivel:.2f}L de {self.tipoCombustivel}")
        
        
        
        

        

        
bomba = BombaCombustivel()
bomba.valorLitro = 5
bomba.tipoCombustivel = "gasolina"
bomba.quantidadeCombustivel = 500

bomba.abastecerPorValor(3000)



