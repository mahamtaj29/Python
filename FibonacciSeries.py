"""
Here I am wrting a program that prints the Fibonacci sequence for a number of times set by the user.
"""
def main():
    numbers = int(input("How many Fibonacci numbers do you want? "))
    first = 1
    second = 1
    x = 0
    print("1.", first)
    print("2.", second)
    for x in range(3, numbers + 1):
        third = first + second
        print(x, ". ", third, sep = "")
        first = second
        second = third
if __name__ == "__main__":
    main()
