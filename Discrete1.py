set_input = input("Enter the sets with space")
converter = set_input.split()

def eliminate_duplicates(duplicate):
    new_set = []
    for item in duplicate:
        if item not in new_set:
            new_set.append(item)
    return new_set

def set_output():
    new_set = eliminate_duplicates(converter)
    if converter == new_set:
        print("True")
    else:
        print("False")
        print("This is the correct set", new_set)

set_output()