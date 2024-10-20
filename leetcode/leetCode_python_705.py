class MyHashSet:

    def __init__(self):
        self.hash_set = set()

    def add(self, key: int) -> None:
        self.hash_set.add(key)

    def remove(self, key: int) -> None:
        self.hash_set.discard(key)

    def contains(self, key: int) -> bool:
        return key in self.hash_set


commands = [
    "MyHashSet",
    "add",
    "add",
    "contains",
    "contains",
    "add",
    "contains",
    "remove",
    "contains",
]
values = [[], [1], [2], [1], [3], [2], [2], [2], [2]]

result = []


for idx, command in enumerate(commands):
    if idx == 0:
        my_hash_set = MyHashSet()
        result.append(None)
    if command == "add":
        my_hash_set.add(values[idx][0])
        result.append(None)
    elif command == "contains":
        result.append(my_hash_set.contains(values[idx][0]))
    elif command == "remove":
        my_hash_set.remove(values[idx][0])
        result.append(None)
    print(idx, command)
print(result)
