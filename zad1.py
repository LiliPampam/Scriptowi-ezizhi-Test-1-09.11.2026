# Задача 1 — Четни и нечетни (25 т.)
# Въвежда се цяло число N, а след него N цели числа, всяко на отделен ред.
# а) (5 т.) Ако N ≤ 0, програмата извежда Невалиден брой и приключва.
# б) (8 т.) Изведете сумата на четните числа.
# в) (8 т.) Изведете най-голямото нечетно число.
# г) (4 т.) Ако няма нечетни числа, вместо най-голямото нечетно изведете Няма нечетни.
# Вход:
# 5
# 4
# 7
# -3
# 10
# 15

# Изход:
# Сума на четните: 14
# Най-голямо нечетно: 15

n = int(input("Enter a number: "))
while n <= 0:
    n = int(input("Enter a number>0: "))
i = 0
sumch = 0
nech = 0
maxnech = 0
r = {}
while i < n:
    r[i] = int(input(f"Enter the {i} number: "))
    if r[i]%2 == 0:
        sumch += r[i]
    else:
        nech += 1
    if i > 0 and r[i]%2!=0 and r[i] > r[i - 1]:
        maxnech = r[i]
    i += 1
print(f"The sum of the even numbers is {sumch}")
if nech != 0:
    print(f"The highest odd number is {maxnech}")
else:
    print("There are no odd numbers.")

