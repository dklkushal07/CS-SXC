class binary_tree:
    def __init__(self,value) -> None:
        self.left = None
        self.data = value
        self.right = None
    def insert(self,value):
        if self.data:
                if value > self.data:
                    if self.right:
                        self.right.insert(value)
                    else:
                        self.right = binary_tree(value)
                if value < self.data:
                    if self.left:
                        self.left.insert(value)
                    else:
                        self.left = binary_tree(value)
        else:
            self.data = value
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()
root = binary_tree(5)
root.insert(3)
root.insert(7)
root.insert(2)
root.insert(4)
root.insert(6)
root.insert(8)
root.insert(1)
root.print_tree()