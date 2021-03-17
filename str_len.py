
def length_string():
    print("HI! Do you want to know the length of a string?\n")

    while True:
        string = input("""Print some string here!\nPS if you want to exit print 'exit'\n""")
        if string == "exit":
            break
        if len(string) < 3:
            print("ERROR! Your string is too weak. Length must be more than 3")
            continue
        print("String length", len(string))


if __name__ == "__main__":
    length_string()
else:
    print('hey! I''m imported')
