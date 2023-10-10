n = input("Enter value of n: ")
try:
    n = int(n)
    total_sum = 0
    # sum of n numbers in python using for loop
    for i in range(1, n+1):
        total_sum = total_sum + i
    print("Total sum is: ", total_sum)
except:
    print("Please enter a natural number")