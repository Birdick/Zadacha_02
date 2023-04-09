# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

a = int(input("Enter your 3-digit number: "))

summ1 = a%10
a = a//10
summ2 = a%10
a = a//10
total = print (summ1 + summ2 + a)
 