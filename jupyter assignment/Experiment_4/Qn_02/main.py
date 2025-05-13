from calculator import basic, scientific

def main():
    while True:
        print("\nScientific Calculator")
        print("1. Add\t2. Subtract\t3. Multiply\t4. Divide")
        print("5. Sin\t6. Cos\t7. Tan\t8. Log\t9. Sqrt")
        print("0. Exit")
        
        choice = int(input("Choose operation (0-9): "))
        
        if choice == 0:
            print("Exiting the calculator")
            break

        elif choice in (1, 2, 3, 4):
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                if choice == 1:
                    print("Addition")
                    print("Result:", basic.add(a, b))
                elif choice == 2:
                    print("Subtraction")
                    print("Result:", basic.subtract(a, b))
                elif choice == 3:
                    print("Multiplication")
                    print("Result:", basic.multiply(a, b))
                elif choice == 4:
                    print("Division")
                    print("Result:", basic.divide(a, b))
        
        elif choice in (5, 6, 7, 8, 9):
            x = float(input("Enter number: "))
            if choice == 5:
                print("Sine Function")
                print("Result:", scientific.sin(x))
            elif choice == 6:
                print("Cosine Function")
                print("Result:", scientific.cos(x))
            elif choice == 7:
                print("Tangent Function")
                print("Result:", scientific.tan(x))
            elif choice == 8:
                print("Logarithm")
                print("Result:", scientific.log(x))
            elif choice == 9:
                print("Square Root")
                print("Result:", scientific.sqrt(x))
        
        else:
            print("Invalid choice. Please select a number from 0 to 9.")

if __name__ == "__main__":
    main()
