class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class HashTable:
    def __init__(self, capacity):
        self.storage = [None] * capacity

    def get_num_slots(self):
        return len(self.storage)

    def get_load_factor(self):
        # load factor: a = n/m
        m = len(self.storage)
        n = m - self.storage.count(None)
        return n/m


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        FNV_offset_basis = 14695981039346656037
        FNV_prime = 1099511628211
		
        fnv1_hash = FNV_offset_basis

        for byte in key.encode():
            fnv1_hash *= FNV_prime
            fnv1_hash ^= byte
		
        return fnv1_hash

    def djb2(self, key):
        pass


    def hash_index(self, key):
        return self.fnv1(key) % len(self.storage)
        #return self.djb2(key) % self.capacity

    def put(self, key, value):
        self.storage[self.hash_index(key)] = value


    def delete(self, key):
        self.storage[self.hash_index(key)] = None


    def get(self, key):
        return self.storage[self.hash_index(key)]


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")
    print("self.storage:")
    print(ht.storage)

    """
    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
    """
