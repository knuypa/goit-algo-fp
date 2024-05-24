class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = ListNode(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(value)

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sorted_merge(self, other):
        dummy = ListNode(0)
        tail = dummy
        a = self.head
        b = other.head

        while a and b:
            if a.value <= b.value:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        tail.next = a if a else b

        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list

    def merge_sort(self):
        if not self.head or not self.head.next:
            return self

        def split(head):
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            mid = slow.next
            slow.next = None
            return head, mid

        def merge(l1, l2):
            dummy = ListNode(0)
            current = dummy
            while l1 and l2:
                if l1.value <= l2.value:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next
            current.next = l1 or l2
            return dummy.next

        def merge_sort_rec(head):
            if not head or not head.next:
                return head
            left, right = split(head)
            left = merge_sort_rec(left)
            right = merge_sort_rec(right)
            return merge(left, right)

        sorted_head = merge_sort_rec(self.head)
        sorted_list = LinkedList()
        sorted_list.head = sorted_head
        return sorted_list

# Створення та виведення початкового списку
ll = LinkedList()
for value in [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]:
    ll.append(value)

print("Початковий список:")
ll.print_list()

# Реверсування списку
ll.reverse()
print("Реверсований список:")
ll.print_list()

# Сортування списку
sorted_ll = ll.merge_sort()
print("Відсортований список:")
sorted_ll.print_list()

# Об'єднання двох відсортованих списків
ll1 = LinkedList()
for value in [1, 3, 5]:
    ll1.append(value)

ll2 = LinkedList()
for value in [2, 4, 6]:
    ll2.append(value)

merged_ll = ll1.sorted_merge(ll2)
print("Об'єднаний відсортований список:")
merged_ll.print_list()