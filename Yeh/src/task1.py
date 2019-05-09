def main():
    tag = None
    input_str = None
    while not tag:
        tag = input("Enter a HTML tag: ")
    while not input_str:
        input_str = input("Enter a word: ")
    
    left_output_tag = "<" + tag + ">"
    right_output_tag = "</" + tag + ">"

    print("Your HTML text is ", left_output_tag + input_str + right_output_tag)

if __name__ == "__main__":
    main()
