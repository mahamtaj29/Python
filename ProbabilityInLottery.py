"""
In this program, I am finding the probability of the player winning the jackpot, ie. guessing all the balls correctly. In Finnish lottery,
for instance, this would mean the probability of the player guessing all 7 balls correctly with only one lottery ticket. This is a
combinatorics-related problem assuming that n is the number of balls in a lottery and p is the number of the predicted balls.
"""
def check_inputs(t_balls, d_balls):
    """ This function will check if both inputs (total balls and drawn balls) are
     positive. If inputs are negative then error message will be printed and
     code will be terminated. If drawn balls are greater than total balls then
     error message will be displayed and code will be terminated. This function
     returns True or False
    """
    if d_balls <= 0:
        print("The number of balls must be a positive number..")
        flag = False
        return flag
    elif t_balls <= 0:
        print("The number of balls must be a positive number.")
        flag = False
        return flag
    elif d_balls > t_balls:
        print("At most the total number of balls can be drawn.")
        flag = False
        return flag
    else:
        # here Both inputs are positive
        flag = True
        return flag
def factorial(counter):
    """This function will calculate the factorial of total balls and
    drawn balls in order to find out the possibility of getting all
    numbers right. result is an integer variable and returns the integer value"""
    result = 1
    for line in range(1, counter + 1):
        result = result * line
    return result

def probability(t_balls, d_balls):
    """This function will calculate the possibility of getting all numbers right
    using the formula (n!/(n-p)! * p!). This function first calculate the factor
    of each value and then apply the formula to calculate the possibility"""
    factor_of_totalballs = factorial(t_balls)
    # This step will give the Factorial of total balls
    factor_of_drawnballs = factorial(d_balls)
    # This step will give the Factorial of drawn balls
    subtraction = t_balls - d_balls
    # This step will give the Subtraction of both balls
    factor_of_subtraction = factorial(subtraction)
    # This step will give the Factorial of Subtraction of both balls
    multiplication_of_factors = factor_of_subtraction * factor_of_drawnballs
    # This step will give the multiplication of ((n-p)! * p!)
    possibility_number = int(factor_of_totalballs / multiplication_of_factors)
    # This step will give us the Final Value of formula (n!/(n-p)! * p!)
    print(f"The probability of guessing all {d_balls} balls correctly is 1/{possibility_number}")
    # change the flag to break the loop
    return possibility_number

def main():
    flag = True
    while flag:
        total_balls = int(input("Enter the total number of lottery balls: "))
        drawn_balls = int(input("Enter the number of the drawn balls: "))
        inputs = check_inputs(total_balls, drawn_balls)
        if inputs == False:
            break
        else:
            calculate_probability = probability(total_balls, drawn_balls)
            flag = False
            break
if __name__ == "__main__":
    main()