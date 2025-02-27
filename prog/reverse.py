def reverse_number(n, rev=0):
    if n == 0:
        return rev
    else:
        rev = (rev * 10) + (n % 10)
        return reverse_number(n // 10, rev)
number = 12345
reversed_number = reverse_number(number)
print(f"The reverse of {number} is {reversed_number}")
