class Jar:
    def __init__(self, capacity=12):
        if capacity > 0:
            self._capacity = capacity
        else:
            raise ValueError("Invalid capacity")
        self._size = 0

    def __str__(self):
        return f"{'🍪' * self._size}"

    def deposit(self, n):
        if n + self._size <= self.capacity:
            self._size += n
        else:
            raise ValueError("Invalid deposit")

    def withdraw(self, n):
        if n <= self._size:
            self._size -= n
        else:
            raise ValueError("Invalid withdraw")

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
