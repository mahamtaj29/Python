"""
In official Rubik's Cube contests, a participant's score is evaluated in the following way:
1- The contestant may solve the Rubik's Cube five times. Each achievement time is measured in seconds.
2- The best and the worst time are removed.
3- An average of the remaining times is calculated and set as the contestant's official score.
Here I am implementing a program that asks for the times of the contestant's performances and prints
the result to the hundredth of a second.
"""
def participants_score():
    """Read inputs from the user, the time values when a participant solves Rubik's cube.
    :param list_of_performance_times is an empty list.
    :param count to count the number of inputs
    :return: list, a list a grades. The list can be empty.
    """
    # Create an empty list.
    list_of_performance_times = []
    count = 1
    # Read inputs with a flag-controlled loop and store the values in the list.
    while count < 6:
        # Read every input as a float.
        performance_time = float(input(f"Enter the time for performance {count}: "))
        list_of_performance_times.append(performance_time)
        count += 1
        # Add a new time input to the end of the list.
    # Return the input values in a list.
    return list_of_performance_times
def find_best_and_worst_times(five_times):
    """Finds and removes the minimum and maximum value of a list.
    :param five_times: the list of times values that will be compared with each other.
    :return: the new list from which best & worst times are removed.
    """
    best_time = worst_time = None
    # Call functions only, if there is something to calculate.
    if len(five_times) >= 0:
        best_time = min(five_times)
        worst_time = max(five_times)
    five_times.remove(best_time)
    five_times.remove(worst_time)
    # Return the new list.
    return five_times
def calculate_average_of_times(list):
    """Calculates the official score of the participants time.
        :param list: the list of time values of which average value will be calculated.
        :return: average_of_list_times, floating value that is calculated by taking average
        """
    total_values = len(list)
    flag = True
    index = 1
    sum_of_times = 0
    while index < total_values:
        list[index] = list[index] + list[index - 1]
        index += 1
    sum_of_times = list[2]
    average_of_list_times = float(sum_of_times / total_values)
    return average_of_list_times
def main():
    list_of_performance_times = participants_score()
    # Finding the best and worst time and removing from the list
    after_removing_best_worst = find_best_and_worst_times(list_of_performance_times)
    # calculating the official score of the participant
    official_score = calculate_average_of_times(after_removing_best_worst)
    print(f"The official competition score is {official_score:0.2f} seconds.")
if __name__ == "__main__":
    main()
