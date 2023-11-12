"""
Here I am writing a program that prints a simple cheat sheet for learning the multiplication table.
The program's printout is also formatted so that each multiplication result is shown in a printout field,
which is four characters wide.
"""
def main():
    for i in range(1, 11):
        for j in range(1, 11):
            # Here using the named parameter (end) in order to continue the next print in same line
            print(f"{i*j:4.0f}", end="")
        print()
if __name__ == "__main__":
    main()
