class HashTableEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

MIN_CAPACITY = 8

class HashTable:
    def __init__(self, capacity):
        self.storage = [None] * capacity
        if len(self.storage) < MIN_CAPACITY:
           self.storage = [None] * MIN_CAPACITY
    
    def __str__(self):
        out = ''
        if self.storage:
            for i in self.storage:
                if i:
                    while i != None:
                        out += f"[\'{i.key}\', \'{i.value}\'] -> "
                        i = i.next
                out += 'None\n'
            return out

        out = 'Empty HashTable'
        return out

    def get_num_slots(self):
        return len(self.storage)

    def get_load_factor(self):
        # load factor = n/m
        m = len(self.storage)
        n = m - self.storage.count(None)
        return n/m


    def fnv1(self, key):
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

    def put(self, key, value):
        # Grab first entry in ll @ index
        e = self.storage[self.hash_index(key)]
        if e == None:
            # If index is not occupied, add new entry
            self.storage[self.hash_index(key)] = HashTableEntry(key, value)

        # While index is occupied
        while e != None:

            # If entry already exists
            if e.key == key:
                # Update with new value
                e.value = value
                return

            # if next pointer is None, add new entry
            if e.next == None:
                e.next = HashTableEntry(key, value)
                return
            
            # Go to next
            e = e.next

    def delete(self, key):
        # Grab first entry in ll @ index
        e = self.storage[self.hash_index(key)]
        if e and e.key == key:
            self.storage[self.hash_index(key)] = e.next

        while e != None: 
            if e.next != None and e.next.key == key:
                e.next = e.next.next
            e = e.next

    def get(self, key):
        # Grab first entry in ll @ index
        e = self.storage[self.hash_index(key)]
        # If entry is not None
        if e:
            # Loop thru ll until entry is none
            while e != None:
                # OR if we find matching key, return value
                if e.key == key:
                    return e.value
                e = e.next
        # No match found or invalid key, return None
        return None

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
