# An implementation of a hash set

class HashSet:
    def __init__(self, capacity):
        self.__data = []
        self.__size = 0  # Number of elements in the HashSet
        self.__hash_table_length = int(capacity / 0.75)  # Load factor: 0.75
        self.__initialize_data(self.__hash_table_length)

    # Add multiple values to the HashSet. Values can be as many values as needed.
    def add(self, *values):
        for value in values:
            if not self.contains(value):  # Does not allow any duplicates
                i = self.__index_of(value)
                self.__data[i] = self.__HashNode(value, self.__data[i])
                self.__size += 1

    # Remove value from the HashSet, assuming value is in the HashSet
    def remove(self, value):
        if self.contains(value):
            i = self.__index_of(value)
            if self.__data[i].value == value:
                self.__data[i] = self.__data[i].next
            else:
                current = self.__data[i]
                while current.next.value != value:
                    current = current.next
                current.next = current.next.next
            self.__size -= 1

    # Checks if the HashSet contains the value
    # Returns True if it does contain value, False if not
    def contains(self, value):
        i = self.__index_of(value)
        current = self.__data[i]
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    # Returns the number of elements in the HashSet
    def size(self):
        return self.__size

    def empty(self):
        return self.__size == 0

    # Returns the location (the index) of the value in the HashSet
    def __index_of(self, value):
        return int(abs(hash(value) % self.__hash_table_length))  # Hash code is the same for ints

    # Creates a list that is table_length long. Each list element is a HashNode, since this is a
    # list of linked lists
    def __initialize_data(self, table_length):
        for i in range(table_length):
            self.__data.append(self.__HashNode())

    # Returns a string version of the HashSet in an easily readable format
    def __str__(self):
        result = "{\n"
        for i in range(self.__hash_table_length):
            if self.__data[i].value is not None:
                current = self.__data[i]
                while current.value is not None:
                    result += str(i) + ': ' + str(current.value) + '\n'
                    current = current.next
        result += "}"
        return result

    # Returns an iterator composed of the values in this HashSet
    def __iter__(self):
        result = []
        for i in range(self.__hash_table_length):
            if self.__data[i].value is not None:
                current = self.__data[i]
                while current.value is not None:
                    result.append(current.value)
                    current = current.next
        
        return iter(result)

    # Returns true if self and other have the same elements
    def __eq__(self, other):
        return list(iter(self)) == list(iter(other))

    # 1 node of a linked list
    class __HashNode:
        def __init__(self, value=None, next=None):
            self.value = value
            self.next = next
