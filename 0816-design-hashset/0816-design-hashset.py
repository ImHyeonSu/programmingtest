class MyHashSet:

    def __init__(self):
        self.hash_set = set()

    def add(self, key: int) -> None:
        self.hash_set.add(key)

    def remove(self, key: int) -> None:
        self.hash_set.discard(key)

    def contains(self, key: int) -> bool:
        return key in self.hash_set
