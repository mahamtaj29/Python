"""
In this project, I am implementing a program that will analyze the changes in the seawater level in some measuring station.
The user will enter the measurements (i.e. sea levels) to the program after which the program will calculate some statistical
characteristics (Median,Mean, Variance, Standard Deviation) and display them to the user.
The characterisrics which are calculated and printed are:
the smallest measurement
the largest measurement
median
mean
standard deviation
Also note, that all the results are printed with two decimal accuracy.
"""
from math import sqrt
def user_input():
    """
    This function will ask user to enter values of seawater levels. User Input will also be validated by checking the number of inputs entered by user. Function will give error if the user input is less
    than two entries.
    :param No paramter in this function
    :return: list_of_seawater_values, this function will return list of user input
    """
    print("Enter seawater levels in centimeters one per line.\n"
          "End the program by entering an empty line.")
    list_of_seawater_values = []
    counter = 0
    flag = True
    while flag:
        seawater_values = input()
        counter += 1
        if (seawater_values == "" and counter > 2):
            flag = False
        elif (seawater_values == "" and counter <= 2):
            print("Error: At least two measurements must be entered!")
            flag = False
            break
        else:
            list_of_seawater_values.append(float(seawater_values))
    return list_of_seawater_values
def calculate_median(user_list):
    """
    This function will calculate the median of seawater values.
    :param user_list a list of user inputs
    """
    sorted_user_list = sorted(user_list)
    length_of_list = len(sorted_user_list)
    # Median is the middle index so calculating the middle index
    finding_mid_index = int(length_of_list / 2)
    if length_of_list % 2 != 0:
        print(f"Median:  {sorted_user_list[finding_mid_index]:.2f} cm")
    else:
        # if length is even number than median is the average of two values in the middle of a list
        sum_of_mid_values = sorted_user_list[finding_mid_index] + sorted_user_list[finding_mid_index - 1]
        average_of_values = float(sum_of_mid_values / 2)
        print(f"Median:  {average_of_values:.2f} cm")
def calculate_mean(user_list):
    """
   This function will calculate the mean of seawater values.
   :param user_list a list of user inputs
   :return: average_of_list that returns the mean value of the list
   """
    sum_of_list = 0
    length = len(user_list)
    index = 0
    while index < length:
        sum_of_list += user_list[index]
        index += 1
    average_of_list = float(sum_of_list / length)
    print(f"Mean:    {average_of_list:.2f} cm")
    return average_of_list
def find_min_and_max(user_list):
    """Finds the minimum and maximum value of a list.
    :param  user_list, a user enetered values of seawater levels in a list
    :return: min_value, max, value , Return the minimum and maximum values
    """
    min_value = max_value = None
    if len(user_list) > 0:
        min_value = min(user_list)
        max_value = max(user_list)
        print(f"Minimum: {min_value:.2f} cm")
        print(f"Maximum: {max_value:.2f} cm")
    return min_value, max_value
def calculate_deviation(list, mean):
    """Calculates the deviation value of a list.
    :param  list, a user enetered values of seawater levels in a list
    :param mean, mean value that is calculated in calculate_mean function
    :return: min_value, max, value , Return the minimum and maximum values
    """
    sum_for_variance = 0
    length = len(list)
    # calculating N value of the formula which is the number of values in the data set
    n_value = float(1 / (length - 1))
    for index in range(length):
        # calculating (x(i-1) - mean)^2
       sum_for_variance += (list[index] - mean) ** 2
        # (1/N-1) x sum_for_variance
    variance = n_value * sum_for_variance
    # Taking square root using import math function
    variance = sqrt(variance)
    print(f"Deviation:{variance:.2f} cm")

def main():
    #Here taking input from user and validate the input
    list_of_seawater_levels = user_input()
    if len(list_of_seawater_levels) > 1:
        # Here finding minimum and maximum values
        min_and_max_values = find_min_and_max(list_of_seawater_levels)
        # Here finding the median of user inputs
        median_of_sea = calculate_median(list_of_seawater_levels)
        # Here calculating the mean of user inputs
        mean_of_sea = calculate_mean(list_of_seawater_levels)
        # Here calculating the deviation of user inputs
        deviation_of_sea = calculate_deviation(list_of_seawater_levels, mean_of_sea)
if __name__ == "__main__":
    main()
