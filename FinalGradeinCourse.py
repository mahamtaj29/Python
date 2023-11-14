"""
Here I am writing a program that allows user to input the points and after the input is done, the program tells which final grade
will result based on the sum of the points in each category. The program reads the input in a loop and during each round it
inquires the user for a category and points. To make the program easier to use, the category names are entered as single letters
A, B, and C, which correspond to elementary, basic, and project categories.
The program stops reading the grades when the user enters the word "quit" as the category name. After that the final grade is
printed on the screen.
"""
def main():
    QUIT_COMMAND = "quit"
    A_points = 0
    B_points = 0
    C_points = 0
    category_id = ""
    while category_id != QUIT_COMMAND:
        category_id = input(f"Enter the category letter (or {QUIT_COMMAND}): ")
        if category_id != "A" and category_id != "B" and category_id != "C" \
           and category_id != QUIT_COMMAND:
            print(f"Error: bad input '{category_id}', try again!")
            continue
        elif category_id != QUIT_COMMAND:
            points = int(input(f"Enter more category {category_id} points: "))
            if category_id == "A":
                A_points += points
            elif category_id == "B":
                B_points += points
            else:
                C_points += points
    if A_points >= 600 and B_points >= 600 and C_points >= 650:
        final_grade = 5
    elif A_points >= 500 and B_points >= 500 and C_points >= 450:
        final_grade = 4
    elif A_points >= 450 and B_points >= 450 and C_points >= 250:
        final_grade = 3
    elif A_points >= 350 and B_points >= 350 and C_points >= 250:
        final_grade = 2
    elif A_points >= 250 and B_points >= 250 and C_points >= 150:
        final_grade = 1
    else:
        final_grade = 0
    # Let's print all the relevant information on one line.
    print(f"A: {A_points} p. / B: {B_points} p. / C: {C_points} p. / ", end="")
    print(f"Grade:{final_grade}")
if __name__ == "__main__":
    main()
