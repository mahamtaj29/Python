"""
Here I am writing a program that asks the user how they feel on scale 1-10 and then proposes a suitable emoticon to describe the mood.
First I will implement a relatively expressionless version that prints :-) for feelings over 7 and otherwise prints the basic face :-|
Then verify the numeric values - if something other than a numeric value between 1 and 10 is entered, the program should print Bad input!
Then add the program a sad emoticon :-(, which is recommended for feelings that are less than 4.
Then add the extremes of the emotion scale, the values 1 and 10, use the stronger faces :'( and :-D
"""
def main():
    enter_value = input("How do you feel? (1-10) ")
    scale = int(enter_value)
    # Firstly, validating the input
    if scale >= 1 and scale <= 10:
        if scale == 1:
            print("A suitable smiley would be :'(")
        elif scale > 7 and scale <= 9:
                print("A suitable smiley would be :-)")
        elif scale <= 7 and scale >= 4:
            print("A suitable smiley would be :-|")
        elif scale <= 2:
            print("A suitable smiley would be :-(")
        elif scale == 10:
            print("A suitable smiley would be :-D")
        else:
            print("A suitable smiley would be :-(")
    else:
        # Print an error message.
        print("Bad input!")
if __name__ == "__main__":
    main()
