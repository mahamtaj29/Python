"""
Here I am implementing a program which asks the user what time it is and prints the times for the next three buses,
based of the entered time. Let's assume that at some less inhabited area, buses leave according to the following schedule:
6:30
10:15
14:15
16:20
17:20
20:00
In order to simplify the presentation of the time, here saving the time as one integer where the minutes and the hours are
expressed in the same number, i.e. 6:30 as 630 and 16:20 as 1620.
"""
def current_time(bus_schedule):
    """This function will ask user to enter current time and print the upcoming 3 departing times of bus.
    :param bus_schedule is a list containing different timings of bus.
    :param present_time is a integer containing the current time entered by user
    :return: upcoming three departing times of bus.
    """
    # Create an empty list.
    present_time = int(input(f"Enter the time (as an integer): "))
    length = len(bus_schedule)
    index = 0
    flag = True
    counter = 3
    # Here comparing the entered time with a flag-controlled loop and printing the departing time of next bus
    print("The next buses leave:")
    while index < length:
        if present_time <= bus_schedule[index]:
            while counter > 0:
                print(f"{bus_schedule[index]}")
                counter -= 1
                if index == 5:
                    index = 0
                else:
                    index += 1
            index += 1
        elif (index+1) == length:
            index = 0
            counter = 3
            while counter > 0:
                print(f"{bus_schedule[index]}")
                counter -= 1
                index += 1
            break
        else:
            index += 1

def main():
    # initializing a list of bus schedule
    bus_schedule = [630, 1015, 1415, 1620, 1720, 2000]
    # Ask user to enter current time
    current_time(bus_schedule)


if __name__ == "__main__":
    main()
