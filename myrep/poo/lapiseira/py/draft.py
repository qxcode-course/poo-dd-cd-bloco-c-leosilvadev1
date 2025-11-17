class Grafite:
    def __init__(self, hardness: float, thickness: str, size: int):
        self.hardness : float = hardness
        self.thickness : str = thickness
        self.size : int = size

    def __str__(self):
        return f"[{self.hardness}:{self.thickness}:{self.size}]"

class Lapiseira:
    def __init__(self, hardness : float):
        self.bico: Grafite | None = None
        self.tambor: list[Grafite] = []
        self.hardness : float = hardness

    def inserir(self, grafite: Grafite):
        if grafite.hardness != self.hardness:
            print("fail: calibre incompatível")
            return
        self.tambor.append(grafite)

    def pull(self):
        if not self.tambor:
            print("fail: nao existe grafite no tambor")
            return
        if self.bico is not None:
            print("fail: ja existe grafite no bico")
            return
        self.bico = self.tambor.pop(0)

    def remove(self):
        if self.bico is None:
            print("fail: nao existe grafite no bico")
            return
        self.bico = None

    def write(self, folhas : int):
        if self.bico is None:
            print("fail: nao existe grafite no bico")
            return
        g = self.bico
        consumo_por_folha = {"HB": 1, "2B": 2, "4B": 4, "6B": 6}
        if g.thickness not in consumo_por_folha:
            print("fail:dureza desconhecida")
            return
        gasto = consumo_por_folha[g.thickness] * folhas
        if g.size <= 10:
            print("fail: tamanho insuficiente")
            return
        if g.size - gasto < 10:
            print("fail: folha incompleta")
            g.size = 10
        else:
            g.size -= gasto


    def __str__(self):
        bico_str = "[]" if self.bico is None else f"{self.bico}"
        tambor_str = "<>" if self.tambor is None else "<" + \
            "".join(str(g) for g in self.tambor) + ">"
        return f"calibre: {self.hardness}, bico: {bico_str}, tambor: {tambor_str}"


def main():
    lapiseira: Lapiseira | None = None
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break

        elif args[0] == "init":
            calibre = float(args[1])
            lapiseira = Lapiseira(calibre)

        elif args[0] == "insert":
            hardness = float(args[1])
            thickness = args[2]
            size = int(args[3])
            g = Grafite(hardness, thickness, size)
            if lapiseira is not None:
                lapiseira.inserir(g)

        elif args[0] == "pull":
            if Lapiseira is not None:
                lapiseira.pull()

        elif args[0] == "remove":
            if Lapiseira is not None:
                lapiseira.remove()

        elif args[0] == "show":
            print(lapiseira)

        elif args[0] == "write":
            if len(args) == 1:
                folhas = 1
            else:
                folhas = int(args[1])
            lapiseira.write(folhas)

main()