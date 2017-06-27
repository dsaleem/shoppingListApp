shopping_list = []

def show_help():


    print("""


Enter done to start adding the items.
Enter help to get help
Enter show to see your current list.
    """)

print("what should we pick up at the store ?: ")

show_help()
def new_list():
    print("Here is you List :")
    for item in shopping_list:
        print(item)

def add_list(item):
    shopping_list.append(item)
    print("{} item has been added to the list , now the list has {} item".format(item,len(shopping_list)))


while True:
    new_item = input("> : ")
    if new_item.lower() == 'done':
        break
    elif new_item.lower() =='help':
        show_help()
        continue
    elif new_item.lower() == 'show':
        new_list()
        continue
    add_list(new_item)

new_list()
