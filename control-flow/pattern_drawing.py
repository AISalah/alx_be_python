size = int(input("Enter the size of the pattern: "))
row_counter = 0

while row_counter < size:
        
        for _ in range(size):
            print("*", end="")

        print()
        row_counter += 1