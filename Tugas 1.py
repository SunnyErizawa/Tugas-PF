# NAMA   : yogi Hermawan
# NIM    : 11201092

# no 1
def sum_squares(*numbers):
    arr = [*numbers]
    temp = 0
    for num in arr:
        temp += num ** 2
    return temp


print(sum_squares(1, 2, 3))


# no 2
def triangular(n):
    total = 0
    if n < 0:
        return "only accept positive number"
    if n == 1:
        return 1
    while n > 0:
        total += n
        n -= 1
    return total


print(triangular(5))


# no 3
def pangkat(num, exp):
    temp = num
    if num < 0 or exp < 0:
        return "only accept positive number"
    if exp == 0:
        return 1
    counter = 0
    while counter < exp - 1:
        num = num * temp
        counter += 1
    return num


print(pangkat(3, 2))


# no 4
def palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False


print(palindrome("rotator"))
