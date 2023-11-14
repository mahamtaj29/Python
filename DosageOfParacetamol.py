"""
Here I am writing a program, which calculates and returns a correct dose of paracetamol, when the following initial values
are given as parameters in the following order: patient's weight, the time from receiving the previous dose, the previous daily ratio.
The function processes all information (including the weight) as integers.
"""
def calculate_dose(weight,time_passed,taken_dose):
    """This function will calculate and returns the correct dose of Paracetamol"""
    # 15 mg is allowed per kg
    allowed_dose = weight * 15
    if (time_passed >= 6 and taken_dose == allowed_dose or taken_dose == 0):
        new_dose = allowed_dose
    elif(time_passed >= 6 and taken_dose > allowed_dose):
        new_dose = 4000 - taken_dose
    else:
        new_dose = 0
    return new_dose

def main():
    weight = int(input("Patient's weight (kg): "))
    time_passed_from_last_dose = int(input("How much time has passed from the previous dose (full hours): "))
    total_dose_given = int(input("The total dose for the last 24 hours (mg): "))
    correct_dose = calculate_dose(weight, time_passed_from_last_dose, total_dose_given)
    print("The amount of Paracetamol to give to the patient:",correct_dose)
if __name__ == "__main__":
  main()
