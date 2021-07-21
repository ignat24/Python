def is_squere(n):
    if n > 0:
        temp = 1
        per = 0
        while per < n:
            per += 2*temp
            temp += 1
        temp = temp-1
        if temp * temp == n:
            return True
        else:
            return False
    elif n == 0:
        return True
    elif n < 0:
        return False

print(is_squere(-1))
print(is_squere(0))
print(is_squere(3))
print(is_squere(4))
print(is_squere(5))
print(is_squere(25))
print(is_squere(26))


