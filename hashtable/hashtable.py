from linkedlist import Node, LinkedList

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        
    def __str__(self):
        return f"<HashTableEntry('{self.key}', '{self.value}')>"


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # ensure we are not below capacity
        if capacity < MIN_CAPACITY:
            capacity = MIN_CAPACITY
            
        # set up storage using a Linked List
        self.data = [LinkedList()] * capacity
        self.capacity = capacity
        
        # when the hashtable's load factor is greater
        # than this, it should be resized
        self.resizeWhenLoadFactorGreaterThan = 0.7
        
        # the count of items in the HT
        self.count = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.data)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.count / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        # don't fully understand,
        hval = 0x811c9dc5
        fnv_32_prime = 0x01000193
        for s in key:
            hval = hval ^ ord(s)
            hval = (hval * fnv_32_prime) % self.capacity
        return hval


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    # this is not being used anywhere--I am taking care
    # of the % in the hash itself
    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Search through the list and find if this key exists.
        # If it does, overwrite the value stored there
        
        # First, loop thru hashtable data
        for index in self.data:
            node_with_key = self.__find_node_with_key_in_ll(index, key)
            if node_with_key is not None:
                # A node with this key exists--simply update
                # its value
                node_with_key.value.value = value
                # ^^^ value.value because the node's value is a
                # HashTableEntry which also has value (with a key)
                return # we are done
        
        # The key was not found anywhere. Now move on to ADDING
        # an entry--but beforehand, let's see if we need to resize
        # the hashtable
        
        if self.get_load_factor() > self.resizeWhenLoadFactorGreaterThan:
            # the load is too much--double the size of the HT
            self.resize(self.capacity * 2)
        
        # create the node
        node = Node(HashTableEntry(key, value))
        # insert the node at the head of the linked list
        # that is at the hashed key's index
        index = self.fnv1(key)
        self.data[index].insert_at_head(node)
        # increment the HT item count
        self.count += 1
        
    def __find_node_with_key_in_ll(self, linkedlist, key): 
        cur = linkedlist.head
        while cur is not None:
            if cur.value.key == key:
                return cur
            cur = cur.next
        return None


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        
        # get the index of this key
        index = self.fnv1(key)
        # find the ll at this index
        ll_at_index = self.data[index]
        # get the head
        cur = ll_at_index.head
        
        # Special case - deleting the head
        if cur is not None:
            if cur.value.key == key:
                ll_at_index.head = ll_at_index.head.next
                # decrement the HT item count
                self.count -= 1
                return cur
        
            # General case - deleting any node that is not the head
            prev = cur
            cur = cur.next
            while cur is not None:
                if cur.value.key == key: # the node to delete
                    prev.next = cur.next # removes all refs to this node for GC
                    # decrement the HT item count
                    self.count -= 1
                    return cur
                else:
                    prev = prev.next
                    cur = cur.next
                
        return None


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # get the index of this key
        index = self.fnv1(key)
        # find the ll at this index
        ll_at_index = self.data[index]
        # find the node with this key in this ll
        found_node = self.__find_node_with_key_in_ll(ll_at_index, key)
        
        if found_node:
            return found_node.value.value
        # ^^^^ value.value because find_node returns a node with
        # a HashTableEntry as its value, which in turn has
        # its own value
        
        # not found
        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # set the new capacity
        self.capacity = new_capacity
        # set the placeholder for the resized HT
        new_data = []
        # loop thru the current HT and add all its
        # values to new_data
        for ll_at_index in self.data:
            cur = ll_at_index.head
            while cur is not None:
                kv = {}
                kv["key"] = cur.value.key
                kv["value"] = cur.value.value
                new_data.append(kv)
                cur = cur.next
                                
        # resize data
        self.data = [LinkedList()] * self.capacity
        for kv in new_data:
            self.put(kv["key"], kv["value"])


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

