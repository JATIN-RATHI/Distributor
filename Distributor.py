if __name__ == '__main__':
    print("Welcome to the program\tcreated by Jatin Rathi")
    item = input("Enter the item you have to distribute among Students : ")
    n = int(input(f"Enter the no. of {item} Jatin got : "))
    mn = int(input(f"Enter the starting range of students to distribute these {item} : "))
    mx = int(input(f"Enter the last range of students to distribute these {item}: "))
    j = 1
    for i in range(mn, mx+1):
        a = n % i
        if a == 0:
            print(f"{j}: {item} can be equally distributed among {i} students.")
        else:
            print(f"{j}: {item} cannot be equally distributed among {i} students. It requires {a} more {item}.")
        j += 1
        