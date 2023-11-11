"""
Here I am writing a program that asks how much study benefits the user receives and calculates how a 1,17%
index raise affects the benefits. Also add another index raise to the program.
"""
study_input = input("Enter the amount of the study benefits that user will going to receive: ")
study_benefit = float(study_input)
# Calculating index raise
index_raise = 1.17 / 100
calculate_index_raise = index_raise * study_benefit
new_study_benefit = study_benefit + calculate_index_raise
print("If the index raise is 1.17 percent, the study benefit,\nafter a raise, would be", new_study_benefit, "euros")
# Now calculating another index raise if applicable
second_index_raise = index_raise * new_study_benefit
updated_study_benefit = second_index_raise + new_study_benefit
print(f"and if there was another index raise, the study\nbenefits would be as much as, {updated_study_benefit:.2f} euros")
