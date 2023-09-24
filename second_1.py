def second_1():
    num = int(input("Введите число: "))
    for i in range(1, num+1):
        print(*range(1, i+1), sep="")
