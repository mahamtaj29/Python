"""
Here I am implement a program which can be used to examine distances and routes between cities. The program will process distance information.
The distance data is being used from a file named distances.txt. In some cities, the distances between two cities can be slightly different depending on the
travel direction/return route.
When the progam starts it ask the user to enter the name of the input file (distances.txt), then it reads the file, and stores it in a suitable data structure.
Then the program prints a prompt and waits the user to enter an action (display (cities), add (new city distance entry) remove (any entry), neighbours
(shows list of neighbouring cities)).
"""
PART_SEPARATOR = ";"
def find_route(data, departure, destination):
    """
    This function tries to find a route between <departure> and <destination> cities. It assumes the existence of the two functions fetch_neighbours and distance_to_neighbour.
    They are used to get the relevant information from the data structure <data> for find_route to be able to do the search. The return value is a list of cities one must travel through
    to get from <departure> to <destination>. If for any reason the route does not exist, the return value is
    an empty list [].
    :param data, departure, destination , A data structure which contains the distance information between the cities.
    :param departure: str, the name of the departure city.
    :param destination: str, the name of the destination city.
    :return: list[str], a list of cities the route travels through, or an empty list if the route can not be found. If the departure and the destination cities are the same, the function returns
           a two element list where the departure city is stored twice.
    """
    if departure not in data:
        return []
    elif departure == destination:
        return [departure, destination]
    greens = {departure}
    deltas = {departure: 0}
    came_from = {departure: None}
    while True:
        if destination in greens:
            break
        red_neighbours = []
        for city in greens:
            for neighbour in fetch_neighbours(data, city):
                if neighbour not in greens:
                    delta = deltas[city] + distance_to_neighbour(data, city, neighbour)
                    red_neighbours.append((city, neighbour, delta))
        if not red_neighbours:
            return []
        current_city, next_city, delta = min(red_neighbours, key=lambda x: x[2])
        greens.add(next_city)
        deltas[next_city] = delta
        came_from[next_city] = current_city
    route = []
    while True:
        route.append(destination)
        if destination == departure:
            break
        destination = came_from.get(destination)
    return list(reversed(route))
def read_distance_file(file_name):
    """
    This function reads the distance information from file> and stores it in a suitable data structure. This data structure is also the return value, unless an error happens during the file reading operation.
    :param file_name: str, The name of the file to be read.
    :return: routes_data | dictionary: A data structure containing the information read from the file or None if any kind of error happens.
    """
    #initializing the empty dictionary
    routes_data = {}
    try:
        data_file = open(file_name, mode='r', encoding="utf-8")
        # reading all the lines of the file
        for line in data_file:
            # Remove the character(s) that end the line.
            line = line.rstrip()
            departure, destination, distance = line.split(PART_SEPARATOR)
            # Adding the empty spaces for values
            if departure not in routes_data:
                routes_data[departure] = {}
            routes_data[departure][destination] = int(distance)
        # Close the file.
        data_file.close()
    except OSError:
        routes_data = None
    return routes_data
def display_data(data):
    """
    This function tries to display all the data currently stored in the nested disctionary
    :param data: a nested dictionary.
    """
    sorted_data = sorted(data.items())
    # Printing the nested dictionary
    for departure, destinations in sorted_data:
        for destination, distance in sorted(destinations.items()):
            print(f"{departure:14}{destination:14}{distance:5}")
def add_data(data, departure, destination, distance):
    """
    This function tries to add new connections into the data structure.
    :param data: a nested dictionary.
    :param departure: str, departure city
    :param destination: str, destination city
    :param distance: int, distance between departure and destination city.
    :return: data, updated dictionary
    """
    try:
        if departure not in data:
            # Adding new key into the dictionary
            data[departure] = {}
            # Adding value against the key
        data[departure][destination] = int(distance)
    except ValueError:
        print(f"Error: '{distance}' is not an integer.")
    return data
def remove_data(data, departure, destination):
    """
    This function tries to remove connections from the data structure.
    :param data: a nested dictionary.
    :param departure: str, departure city
    :param destination: str, destination city
    :return: data, updated data structure
    """
    #This step will delete the key and its value
    del data[departure][destination]
    return data
def display_neighbor_data(data, departure):
    """
    This function tries to display all the neighbours of departure city.
    :param data: a nested dictionary.
    :param departure: str, departure city.
    """
    sorted_data = sorted(data[departure])
    for destination in sorted_data:
        distance = data[departure][destination]
        print(f"{departure:14}{destination:14}{distance:5}")
def fetch_neighbours(data, city):
    """
    Returns a list of all the cities that are directly connected to parameter <city>. In other words, a list of cities where there exist an arrow from <city> to
    each element of the returned list. Return value is an empty list [], if <city> is unknown or if there are no arrows leaving from <city>.
    :param data: nested dictionary, A data structure containing the distance information between the known cities.
    :param city: str, the name of the city whose neighbours we are interested in.
    :return: neighbors[str], the neighbouring city names in a list. Returns [], if <city> is unknown (i.e. not stored as a departure city in <data>) or if there are no
             arrows leaving from the <city>.
    """
    # initializing an empty list
    neighbors = []
    if city in data:
        # Creating a list of neighboring cities
        neighbors = list(data[city])
    return neighbors
def distance_to_neighbour(data, departure, destination):
    """
    Returns the distance between two neighbouring cities. Returns None if there is no direct connection from <departure> city to <destination> city. In other words
    if there is no arrow leading from <departure> city to <destination> city.
    :param data, A data structure containing the distance information between the known cities.
    :param departure: str, the name of the departure city.
    :param destination: str, the name of the destination city.
    :return: int | None, The distance between <departure> and <destination>. None if there is no direct connection between the two cities.
    """
    distance = 0
    neighbor_city = list(data[departure])
    if destination in neighbor_city:
        distance = data[departure][destination]
        return int(distance)
    else:
        return None
def validation_check(data, destination):
    """
    This function will check if destination city is valid.
    :param data: a nested dictionary.
    :param destination: str, destination city.
    :return: Ture | False
    """
    # Checking the validity of destination
    if destination in data:
        return True
    for destinations in data.values():
        if destination in destinations:
            return True
    return False
def main():
    input_file = input("Enter input file name: ")
    # reading input file
    distance_data = read_distance_file(input_file)
    # File handling
    if distance_data is None:
        print(f"Error: '{input_file}' can not be read.")
        return
    # Checking user input and performing respective action
    while True:
        action = input("Enter any action (display/add/remove/neighbours)> ")
        # checking the empty input
        if action == "":
            print("Done and done!")
            return
        # Displaying the file stored in data structure (nested dictionary)
        elif "display".startswith(action):
            display_data(distance_data)
        # Adding new entry into data structure
        elif "add".startswith(action):
            departure = input("Enter departure city: ")
            destination = input("Enter destination city: ")
            distance = input("Distance: ")
            distance_data = add_data(distance_data, departure, destination, distance)
        # Removing entry into data structure
        elif "remove".startswith(action):
            departure = input("Enter departure city: ")
            # Checking the validity of departure city
            if departure not in distance_data:
                print(f"Error: '{departure}' is unknown.")
            else:
                destination = input("Enter destination city: ")
                # Checking validity of destination city
                if destination not in distance_data[departure]:
                    print(f"Error: missing road segment between '{departure}' and '{destination}'.")
                else:
                    distance_data = remove_data(distance_data, departure, destination)
        # Checking the validity of neighbor city with respect to departure city
        elif "neighbours".startswith(action):
            departure = input("Enter departure city: ")
            if validation_check(distance_data, departure) == False:
                print(f"Error: '{departure}' is unknown.")
            elif departure in distance_data:
                display_neighbor_data(distance_data, departure)
        # Finding the available route between departure and destination city
        elif "route".startswith(action):
            distance = 0
            departure = input("Enter departure city: ")
            # Checking the validity of departure city input
            if validation_check(distance_data, departure) == False:
                print(f"Error: '{departure}' is unknown.")
            else:
                destination = input("Enter destination city: ")
                route = find_route(distance_data, departure, destination)
                # If route is not available
                if not route:
                    print(f"No route found between '{departure}' and '{destination}'.")
                else:
                    # Calculating the distance of available route
                    for ind in range(len(route)-1):
                        if (route[ind] !=route[ind+1]):
                            distance += distance_to_neighbour(distance_data, route[ind], route[ind+1])
                    route_str = "-".join(route)
                    print(f"{route_str} ({distance} km)")
        else:
            print(f"Error: unknown action '{action}'.")

if __name__ == "__main__":
    main()
