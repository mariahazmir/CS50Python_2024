class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Jar cannot be negative")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if n < 0:
            raise ValueError("Cannot add a negative number of cookies")
        if self._size + n > self._capacity:
            raise ValueError("Not enough space in the jar")
        self._size += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Cannot withdraw a negative number of cookies")
        if self._size - n < 0:
            raise ValueError("Not enough cookies in the jar")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
