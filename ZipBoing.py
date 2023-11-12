"""
Here I am writing a program based on game "Zip Boing". The game is called Zip Boing because every time the next number is
divisible by 3 the player has to say "zip" and every time the number is divisible by 7 the player has to say "boing".
Also, if the umber is divisible by both the numbers, the player should say "zip boing".
"""
def main():
    count = 1
    num = int(input("How many numbers would you like to have? "))
    while count <= num:
        # Here checking the multiples of 3 & 7
        if count % 3 == 0 and count % 7 == 0:
            print("zip boing")
            count = count + 1
        elif count % 3 == 0:
            print("zip")
            count = count + 1
        elif count % 7 == 0:
            print("boing")
            count = count + 1
        elif count % 3 != 0 and count % 7 != 0:
            print(count)
            count = count + 1
        else:
            print("Invalid input")
if __name__ == "__main__":
    main()