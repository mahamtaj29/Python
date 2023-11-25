"""
Implementing a program that will print the products on screen sorted in the incresing order of the prices.
Dictionary named PRICES is given in the template:
"""
PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.70, "grasshopper": 13.25,
    "sushi": 19.90, "noodles": 0.97, "beans": 0.87, "bean": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}
def main():
    # sorting the Dict with keys
    sorted_dict = sorted(PRICES, key=PRICES.get)
    # printing the Dictionary
    for key in sorted_dict:
         print(f"{key} {PRICES[key]:0.2f}")
if __name__ == "__main__":
    main()
