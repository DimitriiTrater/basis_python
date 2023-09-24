def first():
    print("Введите 3 числа через пробел:")
    nums = list((int(i) for i in input().split()))
    dup = [x for x in nums if nums.count(x) > 1]
    print(*dup)
