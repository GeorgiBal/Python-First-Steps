class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def traversal(self):
        first = self.head
        while first:
            for grocery in first.data:
                print(grocery)
            first = first.next

    def insert_new_head(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def search(self, x):
        temp = self.head
        while temp is not None:
            for grocery in temp.data:
                if grocery == x:
                    return True
            temp = temp.next
        else:
            return False

    def delete_node(self, data):
        temp = self.head
        while temp is not None:
            for grocery in temp.data:
                if grocery == data:
                    temp.data.remove(data)
                    break
            temp = temp.next

    def delete_tail(self):
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next.data.pop()

groceries = LinkedList()

groceries.head = Node(['Eggs', 'Meat', 'Bread'])
drinks = Node(['Water', 'Soda', 'Juice'])
sweets = Node(['Cereal', 'Candies', 'Cookies'])

groceries.head.next = drinks
drinks.next = sweets


groceries.traversal()
groceries.insert_new_head(['Veggies', 'Fruits', 'Nuts'])
groceries.traversal()
print(groceries.search('Soda'))
groceries.delete_node('Soda')
groceries.traversal()
groceries.delete_tail()
groceries.traversal()
