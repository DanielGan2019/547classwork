print("This is the bloodcalculator.py file")
print("Python thinks this is called {}".format(__name__))

def interface():
    print("blood calculator")
    while True:
        print("Options:")
        print("1 = HDL")
        print("2 = LDL")
        print("3 = Cholesterol")
        print("4 = Quit")
        
        choice = input("Select an option: ")
        if choice == "4":
            return
        elif choice == "1":
            HDL_driver()
        elif choice == "2":
            LDL_driver()
        elif choice == "3":
            Chol_driver()
    print("Program ending")
    
def HDL_driver():
    HDL_number = generic_input("HDL")
    HDL_analy = HDL_analysis(HDL_number)
    generic_output("HDL",HDL_number, HDL_analy)

def generic_input(test_name):
    value = input("Enter the {} value: ".format(test_name))
    value = int(value)
    return value

def HDL_analysis(HDL_int):
    if HDL_int >= 60:
        answer = "Normal"
    elif 40 <= HDL_int <60:
        answer = "Borderline Low"
    else:
        answer = "Low"
    return answer

def generic_output(test_name, test_value, test_analy):
    print("The {} result of {} is considered {}".format(test_name,test_value,test_analy))
    return

def LDL_driver():
    LDL_number = generic_input("LDL")
    LDL_analy = LDL_analysis(LDL_number)
    generic_output("LDL",LDL_number, LDL_analy)

def LDL_analysis(LDL_int):
    if LDL_int < 130:
        answer = "Normal"
    elif 130 <= LDL_int <=159:
        answer = "Borderline High"
    elif 160 <= LDL_int <= 189:
        answer = "High"
    else:
        answer = "Very High"
    return answer

def Chol_driver():
    Chol_number = generic_input("Chol")
    Chol_analy = Chol_analysis(Chol_number)
    generic_output("Chol",Chol_number, Chol_analy)

def Chol_analysis(Chol_int):
    if Chol_int < 200:
        answer = "Normal"
    elif 200 <= Chol_int <=239:
        answer = "Borderline High"
    elif 240 <= Chol_int:
        answer = "High"
    return answer

if __name__ == "__main__":
    interface()
