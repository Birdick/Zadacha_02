# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

lenght = int(input("Input the chocolate lenght in pcs: "))
width = int(input("Input the chocolate width in pcs: "))

chockbreak = int(input("Input the chocolate pcs you want to break: "))

if chockbreak < lenght * width and (chockbreak % lenght == 0 or chockbreak % width == 0):
    print('Yes')
else:
    print('NO')