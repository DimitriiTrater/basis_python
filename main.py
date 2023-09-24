from first import first
from second_1 import second_1
from second_2 import second_2


def main():
    print("Lab launcher")
    print("#############")
    print("ex.   1")
    print("ex. 2.1")
    print("ex. 2.2")
    print("ex. 2.3")
    print("#############")
    nex = input("Num of ex: ")
    if (nex == "1"):
        print("ex. 1")
        first()
    elif (nex == "2.1"):
        print("ex. 2.1")
        second_1()
    elif (nex == "2.2"):
        print("ex. 2.2")
        second_2()


if __name__ == "__main__":
    main()
