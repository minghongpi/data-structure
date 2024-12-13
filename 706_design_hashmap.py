# No underscore: Public, for regular use.
# Single underscore (_): Protected, for internal use but accessible if needed.
# Double underscore (__): Private, name-mangled for better isolation.
# hashTable: a list
# hash function: key -> index of hashTable
class node:
    def __init__(self, key=-1, value = -1, next=None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:

    def __init__(self):
        self.__size = 1000
        self.__hashTable = [node() for i in range(self.__size) ]


    def put(self, key: int, value: int) -> None:
        index = self.__hash(key)
        head = self.__hashTable[index]
        # find the previous pointer where its next
        # node's key is equal to the given key 
        while head.next and head.next.key != key: 
            head = head.next
        # two cases (1) existing in hashTable
        #           (2) nonexisting
        if head.next: 
            head.next.value = value;
        else:
            head.next = node(key, value)


    def get(self, key: int) -> int:
        index = self.__hash(key)
        head = self.__hashTable[index]
        while head.next and head.next.key != key:  
            head = head.next
            
        # two cases (1) existing in hashTable
        #           (2) nonexisting
        if head.next:
            return head.next.value;
        else:
            return -1

    def remove(self, key: int) -> None:
        index = self.__hash(key)
        head = self.__hashTable[index]
        while head.next and head.next.key != key: 
            head = head.next
        if head.next:
            tmp = head.next
            head.next = head.next.next

    def __hash(self, key: int) -> int:
        return key%self.__size;
