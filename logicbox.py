while True:
    print("\nWelcome to the Pattern Generator and Number Analyzer!\n")

    print("Select an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    match choice:


        case 1:
            rows = int(input("Enter the number of rows for the pattern: "))

            print("\nPattern:\n")
            for i in range(1, rows + 1):
                print("*" * i)


        case 2:
            start = int(input("\nEnter the start of the range: "))
            end = int(input("Enter the end of the range: "))

            total = 0

            print()
            for num in range(start, end + 1):
                if num % 2 == 0:
                    print(f"Number {num} is Even")
                else:
                    print(f"Number {num} is Odd")

                total += num

            print(f"\nSum of all numbers from {start} to {end} is: {total}")


        case 3:
            print("Exiting the program. Goodbye!")
            break

        case _:
            print("Invalid choice! Please select a valid option.")
