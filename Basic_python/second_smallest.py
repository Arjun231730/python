number = int(input("Enter a number: "))
digits = [int(d) for d in str(abs(number))]
unique_digits = sorted(set(digits))
if len(unique_digits) >= 2:
    second_smallest = unique_digits[1]
    print("The 2nd smallest digit is:", second_smallest)
else:
    print("There is no 2nd smallest digit (all digits are the same).")
