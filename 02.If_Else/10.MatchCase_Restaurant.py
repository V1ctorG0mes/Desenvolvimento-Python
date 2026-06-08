while True:
    Rm = int(input("Enter student ID: "))
    age = int(input("Enter student age: "))

    if age >= 18:
        print("Student with ID {} registered.".format(Rm))
        while True:
            continue_reg = (input("Do you want to register another student? (Y)Yes / (N)No: ")).upper()
            if continue_reg == "Y":
                print("You chose to register a new student")
                break
            elif continue_reg == "N":
                print("program closed")
                exit()
            else:
                print("type Y or N")
    else:
        print("Student has insufficient age.")