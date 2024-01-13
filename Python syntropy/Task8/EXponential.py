def cal_expo(base, *exponents):
    return [base ** exp for exp in exponents]

x = int(input("Enter the number of exponents: "))
base_num = float(input("Enter the base number: "))
exponents = [float(input(f"Enter exponent {i + 1}: ")) for i in range(x)]

result = cal_expo(base_num, *exponents)
print(f"The exponentials are: {result}")
