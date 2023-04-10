# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

# peter = int(input("How many birds has made Peter: "))
# sergey = peter
# print (f"Sergey has made {sergey}")
# kate = (peter + sergey)*2
# print (f"Kate has made {kate}")
# total = peter + sergey + kate
# print (f"Guys have made together {total} birds")

summ = int(input ("How many birds have made children? "))
part = summ//6
print(f"Peter made {part} birds")
print(f"Sergey made {part} birds")
print(f"Kate made {part*4} bifds")
