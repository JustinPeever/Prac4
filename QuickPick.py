import random

quick_num = int(input("How many quick picks? "))
for i in range(1, quick_num + 1):
    data = []
    while len(data) != 6:
        num = random.randint(1, 45)
        while num in data:
            num = random.randint(1, 45)
        data.append(num)
    data = sorted(data)

    for number in data:
            print("{:>3}".format(number), end="")

    print()
    #print("{:6}{:6}{:6}{:6}{:6}{:6}".format(data[0], data[1], data[2], data[3], data[4], data[5]))
    #print(*data, sep=' ')
