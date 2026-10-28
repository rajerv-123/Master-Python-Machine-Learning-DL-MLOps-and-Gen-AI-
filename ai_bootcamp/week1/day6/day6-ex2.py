def write_item_to_file(item, filename):
    with open(filename, "a") as file:
       for item  in items:
           file.write(item + "\n")
 
def read_items_from_file(filename):
    try:
        with open(filename, "r") as file:
            items = [line.strip() for line in file.readlines()]
            print(items)
            for item in items:
                print(item.strip())
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
        return []
              
              
fruists = ["apple", "banana", "cherry"]
write_item_to_file(fruists, "fruits.txt")