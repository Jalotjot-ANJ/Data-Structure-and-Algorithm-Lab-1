# Arjun N. Jalotjot
# BSCPE 2-3
# DSA-ACTIVITY 1

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    # Ask the user to input a temperature
    temp = float(input("Input a temperature: "))
    
    while True:
        # Ask the user to select the conversion type
        print("Select the conversion type:")
        print("A. Celsius to Fahrenheit")
        print("B. Fahrenheit to Celsius")
        
        choice = input("Enter A or B: ").upper()
        
        if choice == 'A':
            result = celsius_to_fahrenheit(temp)
            print(f"{temp}°C is equal to {result:.2f}°F")
            break  # Exit the loop after a valid input
        elif choice == 'B':
            result = fahrenheit_to_celsius(temp)
            print(f"{temp}°F is equal to {result:.2f}°C")
            break  # Exit the loop after a valid input
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
