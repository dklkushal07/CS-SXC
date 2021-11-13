# def getRollNo():
#     RollNo = [15,7,22,25,8,5,9,2,4,21]
#     print("Before Sorting:",RollNo)
#     return RollNo
# def ImprovedBubbleSort(mymyArrayay):
#     Swapping = True

#     while(Swapping):
#         Swapping = False
#         for i in range(len(mymyArrayay) - 1):
#             if mymyArrayay[i] > mymyArrayay[i+1]:
#                 mymyArrayay[i], mymyArrayay[i+1] = mymyArrayay[i+1], mymyArrayay[i]
#                 Swapping = True
#     return mymyArrayay
# def printRollNo(mymyArrayay):
#     print("After Sorting:",mymyArrayay)
# printRollNo(ImprovedBubbleSort(getRollNo()))

#--------------------------------------------------------------------------------




# class Node:
#     def __init__(self, data):
#         self.left = None
#         self.right = None
#         self.data = data

#     def Add(self, data):
#         if not self.data:
#             self.data = data        
#             return

#         if data < self.data:
#             if self.left is None:
#                 self.left = __class__(data)
#             else:
#                 self.left.Add(data)
#         else:
#             if self.right is None:
#                 self.right = __class__(data)
#             else:
#                 self.right.Add(data)

#     def printTree(self, *args, **kwargs):
#         if self.left:
#             self.left.printTree(*args, **kwargs)
#         print(self.data, *args, **kwargs)
#         if self.right:
#             self.right.printTree(*args, **kwargs)

# def CreateTree():
#     tree = Node(None)
    
#     for _ in range(10):
#         tree.Add(None)
    
#     return tree

# binaryTree = CreateTree()

# binaryTree.Add("Elen")
# binaryTree.Add("Herma")
# binaryTree.Add("Bina")
# binaryTree.Add("Abishek")
# binaryTree.Add("Sudarshan")
# binaryTree.Add("Isha")

# binaryTree.printTree()

#--------------------------------------------------------------------------------

# StudentList = ['Astha','Aditya','Binita','Dinesh','Jenisha','Kalpana','Manish','Neha','Pratik','Utsav']
# def BinarySearch(myArray, small, large, a):
#     if large >= small:
#         mid = (large + small) // 2
#         if myArray[mid] == a:
#             return mid
#         elif myArray[mid] > a:
#             return BinarySearch(myArray, small, mid - 1, a)
#         else:
#             return BinarySearch(myArray, mid + 1, large, a)
#     else:
#         return -1
# def result(name):
#     if BinarySearch(StudentList, 0, len(StudentList)-1, name) != -1:
#         print(name,"is at index",BinarySearch(StudentList, 0, len(StudentList)-1, name))
#     else:
#         print(name,"is not in array")
# result("Neha")
# result("Sandhya")

    


