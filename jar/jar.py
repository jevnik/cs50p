class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return ('🍪'*self.size)

    def deposit(self, n):
        if isinstance(n, int) and self.size + n <= self.capacity:
            self.size += n
        else:
            raise ValueError()

    def withdraw(self, n):
        if self.size < n:
            raise ValueError
        self.size -= n
    #getter gor capacity
    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if isinstance(capacity, int) and capacity > 0:
            self._capacity = capacity
        else:
            raise ValueError()

    #getter for size
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self,size):
        self._size = size

