import random

def main():
    min_bound = None
    max_bound = None
    while not min_bound:
        min_bound = input("Enter a min bound: ")
        try:
            min_val = int(min_bound)
        except ValueError:
            print("You should give me an integer")
            return
    while not max_bound:
        max_bound = input("Enter a max bound: ")
        try:
            max_val = int(max_bound)
        except ValueError:
            print("You should give me an integer")
            return
    if min_val >= max_val:
        print("min bound should be smaller than max bound")
        return
    
    random_list = []
    for i in range(30):
        random_list.append(random.randrange(min_val, max_val + 1))

    print(random_list)
    while 13 in random_list:
        random_list.remove(13)
    print("sum of random list except 13: ", sum(random_list))
    print("average of random list except 13: ", sum(random_list) / len(random_list))

if __name__ == "__main__":
    main()
