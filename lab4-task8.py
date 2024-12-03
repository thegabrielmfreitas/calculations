while True:
    user = int(input("Please enter a number between 50 and 75: "))

    # Check if the input is within the range
    if 50 <= user <= 75:
        print("You entered a valid number.")
        break
    else:
        print("Please try again.")