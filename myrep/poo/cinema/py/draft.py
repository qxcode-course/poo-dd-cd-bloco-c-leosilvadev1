class Cliente:
    def __init__(self, id: str, telefone: int):
        self.id :str = id 
        self.telefone : int = telefone

    def __str__(self):
        return f"{self.id}:{self.telefone}"

class Sala:
    def __init__(self,capacidade : int):
        self.capacidade: int = capacidade
        self.assentos: list [Cliente | None] = [None for _ in range(capacidade)]

    def verificar(self, index: int) -> bool:
        if index > len(self.assentos):
            return False
        if index >= 0:
            return True

    def procurar(self,name: str) -> int:
        for i, cliente in enumerate(self.assentos):
            if cliente is not None and cliente.id == name:
                return i
        return -1

    def reservar(self, id: str, telefone : int, index : int) -> bool:
        if not self.verificar(index):
            print("fail: cadeira nao existe")
            return False
        if self.procurar(id) != -1:
            print("fail: cliente ja esta no cinema")
            return False
        if self.assentos[index] is not None:
            print("fail: cadeira ja esta ocupada")
            return False
        self.assentos[index] = Cliente(id, telefone)
        return True

    
    def cancelar(self, id :str) -> bool:
        c = self.procurar(id)
        if c == -1:
            print("fail: cliente nao esta no cinema")
            return False
        self.assentos[c] = None
        return True
        

    def __str__(self):
        return "[" + " ".join(str(c) if c else "-" for c in self.assentos) + "]"

def main():
    sala: Sala() | None = None
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break

        if args[0] == "init":
            c = int(args[1])
            sala = Sala(c)

        if args[0] == "cancel":
            sala.cancelar(str(args[1]))

        if args [0] == "reserve":
            i = str(args[1])
            t = int(args[2])
            ind = int(args[3])
            sala.reservar(i, t, ind)

        if args[0] == "show":
            if sala:
                print(sala)
            else:
                print("[]")

main()

    