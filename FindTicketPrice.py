"""
Here I am writing a code that prints the price of a single ride bus ticket in Tampere and surrounding areas on Aug 23rd, 2020.
The prices of tickets with reference to age is as follows:
  -----  -------
   Age    Price
  -----  -------
   >24     2.04
  17-24    1.47
   7-16    1.02
   0-6     0.00
"""
def main():
    age = int(input("Please, enter your age as whole number: "))
    if age >= 17 and age <= 24:
        ticket_price = 1.47
    elif age >= 7 and age <= 16:
        ticket_price = 1.02
    elif age >= 0 and age <= 6:
        ticket_price = 0.00
    else:
        ticket_price = 2.04
    print("Your ride will cost:", ticket_price)
if __name__ == "__main__":
    main()