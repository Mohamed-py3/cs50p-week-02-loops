def main():
    text = input("Input: ")
    print("Output: ", end="")
    for char in text:
        if char.lower() in ["a", "e", "i", "o", "u"]:
            continue
        print(char, end="")
    print()


main()