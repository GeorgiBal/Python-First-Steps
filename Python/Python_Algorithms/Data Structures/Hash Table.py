class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        self.table[index].append({key: value})

    def get(self, key):
        index = self._hash(key)
        for items in self.table[index]:
            for inner_key in items:
                if inner_key == key:
                    return items[key]

    def delete(self, key):
        index = self._hash(key)
        for items in self.table[index]:
            for inner_key in items:
                if inner_key == key:
                    self.table[index].remove(items)
                    return True

    def __str__(self):
        return str(self.table)


ht = HashTable()
ht.insert("apple", 1)
ht.insert("banana", 2)
ht.insert("orange", 3)
print("Hash Table:", ht)

print(ht.get("apple"))

ht.delete("banana")
print("After deleting 'banana':", ht)
