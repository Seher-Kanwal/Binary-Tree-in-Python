class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        element = []

        # first go to the left
        if self.left:
            # we first go in the depth that come back with a list we combine it with the list we received from the
            # lower left children

            element += self.left.in_order_traversal()

        # then root node
        element.append(self.data)

        # Then right side of the tree
        if self.right:
            element += self.right.in_order_traversal()

        return element

    def delete(self, value):
        if value < self.data:
            self.left = self.left.delete(value)
        elif value > self.data:
            self.right = self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            max_value = self.left.find_max()
            self.data = max_value
            # no remove the duplication
            self.left = self.left.delete(max_value)
        return self

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def sum(self):
        left_sum = 0
        right_sum = 0
        left_sum += self.left.sum() if self.left else 0
        right_sum += self.right.sum() if self.right else 0
        return  self.data + right_sum + left_sum


def building_a_tree(data):
    print("we need to assign a root node first:")
    root = BinarySearchTree(data[0])

    print("After the root we need to add elements from 1 till the end of the list so....")
    for i in range(1, len(data)):
        root.add_child(data[i])

    return root


if __name__ == "__main__":
    elements = [17, 4, 1, 20, 9, 23, 18, 34]
    print("We are going to build a tree.....")
    obj = building_a_tree(elements)
    print("Is this number present in the tree :", obj.search(5))
    print("The tree with in order traversal:", obj.in_order_traversal())
    obj.delete(20)
    print("The tree with in order traversal:", obj.in_order_traversal())
    obj.delete(9)
    print("The tree with in order traversal:", obj.in_order_traversal())