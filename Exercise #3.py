# Arjun N. Jalotjot
# BSCPE 2-3
# DSA-ACTIVITY 1

def print_diamond(n):
    if n % 2 == 0:
        return "Please provide an odd integer."
    
    # Upper part of the diamond
    for i in range(n // 2 + 1):
        print(' ' * (n // 2 - i) + '*' * (2 * i + 1))
    
    # Lower part of the diamond
    for i in range(n // 2 - 1, -1, -1):
        print(' ' * (n // 2 - i) + '*' * (2 * i + 1))

# Example usage:
n = int(input("Enter an odd integer for the width of the diamond: "))
result = print_diamond(n)
if result:
    print(result)
