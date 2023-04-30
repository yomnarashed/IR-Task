from binarytree import build, Node

# Construct binary tree from list of integers
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
root = build(nums)
print (root)

# Define function to add new element to binary tree
def add_element():
    new_num = int(input("Enter the new element: "))
    nums.append(new_num)
    print("New element added to the binary tree")
    root = build(nums)
    return root

# Define function to delete element from binary tree
def delete_element():
    del_index = int(input("Enter the index you want to delete: "))
    del root[del_index]


# Prompt user to choose between adding or deleting an element
while True:
    choice = int(input("Choose an operation:\n1. Add a new element\n2. Delete an element\nEnter your choice: "))
    if choice == 1:
        root = add_element()
        print(root)
    elif choice == 2:
        delete_element()
        print(root)
    else:
        print("Invalid choice. Please enter 1 or 2.")
    
   