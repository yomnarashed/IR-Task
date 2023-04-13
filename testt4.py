values_list = [3, 2, 9, 11, 7]
m =7
hash_table = [[] for _ in range(m)]  # create an empty hash table (list of lists)

def hash_function(value):
    return value % m  # hash function to map the value to a key

def construct_hash_table():
    for value in values_list:
        key = hash_function(value)
        hash_table[key].append(value)

def add_element():
    value = int(input("Enter a new value: "))
    key = hash_function(value)
    hash_table[key].append(value)

def update_element():
    key = int(input("Enter a key to update: "))
    value = int(input("Enter a new value: "))
    if key in range(m):
        hash_table[key] = [value]
    else:
        print("Invalid key.")

def delete_element():
    value = int(input("Enter a value to delete: "))
    for values in hash_table:  
        if value in values:      
            values.remove(value)
            print ("Succesffully deleted")
            
def search_element():
    value = int(input("Enter a value to search: "))
    key = hash_function(value)
    for key, values in enumerate(hash_table):  
        if value in values:      
            print ("Value found at key", key)

def print_elements():
    for key, values in enumerate(hash_table):
        if values:  #if key has values and not empty list
            print("Key", key, ":", values)

while True:
    print("1. Construct the whole hash table")
    print("2. Add a new element to the hash table")
    print("3. Update a value of a certain key")
    print("4. Delete an element from the hash table")
    print("5. Search for an element in the hash table")
    print("6. Print all elements with their keys of the hash table")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        construct_hash_table()
    elif choice == 2:
        add_element()
    elif choice == 3:
        update_element()
    elif choice == 4:
        delete_element()
    elif choice == 5:
        search_element()
    elif choice == 6:
        print_elements()
    else:
        print("Invalid choice.")