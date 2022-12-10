class Pila():
    def __init__(self):
        self.items=[]

    def llenadoPila(self):
        return self.items==[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    def top(self):
        return self.items[len(self.item)-1]
    def size(self):
        return len(self.items)

Pila=Pila()
#print(pila.llenadoPila())
Pila.push(4)
Pila.push("jjff")
Pila.push(6)
Pila.push("fkfkfi")
