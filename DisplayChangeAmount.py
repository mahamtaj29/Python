"""
Here I am writing a program that asks how much purchases cost and the amount of paid money is and then prints the amount of change.
After that I simplify the program by only allowing the use of sums of 1, 2, 5 and 10 euros.
The program will work when the total price is always in full euros.
"""
def main():
    cost = int(input("Please enter purchased cost: "))
    paid = int(input("Please enter paid amount of money: "))
    change = paid - cost
    # checking if change is not zero and not negative, then total notes of ten can be counted.
    if change != 0 and change > 0:
        ten_notes = change // 10
        print("Offer change to customer: ")
        if ten_notes != 0:
            print(ten_notes, "ten-euro notes")
        # this step will give the total count of cents
        cents = change % 10
        if cents > 0:
            # Here counting 5 euro notes
            five_notes = cents // 5
            if five_notes != 0:
                print(five_notes, "five-euro notes")
            two_notes = cents % 5
            if two_notes > 0:
                two_coins = two_notes // 2
                one_coins = two_notes % 2
                if two_coins != 0:
                    print(two_coins, "two-euro coins")
                if one_coins != 0:
                    print(one_coins, "one-euro coins")
    else:
        print("No change")
if __name__ == "__main__":
    main()