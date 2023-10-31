class Queue():
    def __init__(self):
        self._data = list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        return self._data.append(value)

    def dequeue(self):
        if len(self._data) == 0:
            return None
        return self._data.pop(0)

    def search(self, index):
        if index < 0 or index >= len(self._data):
            raise IndexError("Índice Inválido ou Inexistente")
        return self._data[index]


# minha_fila = Queue()
# minha_fila.enqueue(10)
# minha_fila.enqueue(20)

# tamanho = len(minha_fila)
# print(tamanho)
