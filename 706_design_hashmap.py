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
        head = self.__find_prev_node(key)
        if head.next: 
            head.next.value = value;
        else:
            head.next = node(key, value)


    def get(self, key: int) -> int:
        head = self.__find_prev_node(key)
        if head.next:
            return head.next.value;
        else:
            return -1

    def remove(self, key: int) -> None:
        head = self.__find_prev_node(key)
        if head.next:
            tmp = head.next
            head.next = head.next.next

    def __hash(self, key: int) -> int:
        return key%self.__size;

    def __find_prev_node(self, key: int) -> node:
        # given key and find the index in hashTable
        index = self.__hash(key)
        # find the dummy head of linked list
        head = self.__hashTable[index]
        # find the previous node where its next node's value
        # is equal to given key
        while head.next and head.next.key != key: 
            head = head.next
        return head
