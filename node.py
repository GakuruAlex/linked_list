class Node():
        def __init__(self,  data):
            self._next = None
            self.data = data
        @property
        def next(self):
            return self._next
        def __str__(self):
            return f"{self.data}"
        def __repr__(self):
            return self.__str__()
