# Implementation of Binary Search Algorithm in Python
# Prerequisite: The given list must be sorted
def search(List,SearchItem):
    Found = False
    SearchFailed = False
    First = 0
    Last = MaxItems - 1
    while not Found and not SearchFailed:
        Middle = (First + Last)//2
        if List[Middle] == SearchItem:
            Found = True
        else:
            if First >= Last:
                SearchFailed = True
            else:
                if List[Middle] > SearchItem:
                    Last = Middle -1
                else:
                    First = Middle + 1 
    if Found == True:
        print(Middle)
    else:
        print("Item not present in array")
SearchItem = int(input("Enter the number"))
List = [7,12,19,23,27,33,37,41,45,56,59,60,62,71,75,80,84,88,92,99]
MaxItems = len(List)
search(List,SearchItem)

