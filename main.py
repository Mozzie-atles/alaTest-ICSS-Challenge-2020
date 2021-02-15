import sys

# op_ stands for Opertator_

def choose(number):
    op_A = [[1, 0.9], [268, 5.1], [46, 0.17], [4620, 0.0],
            [468, 0.15], [4631, 0.15], [4673, 0.9], [46732, 1.1]]
    op_B = [[1, 0.92], [44, 0.5], [46, 0.2], [467, 1.0], [48, 1.2]]
    maxlen = 0
    minlen = 0
    listA = []
    listB = []

    for row in op_A:
        prefix = str(row[0])
        for i in range(len(prefix)):
            if number[i] == prefix[i]:
                minlen = len(prefix)
                if number[0:i+1] == prefix:
                    if minlen > maxlen:
                        maxlen = minlen
                        listA.append(row[1])
            else:
                break
        minlen = 0
    maxlen = 0
    for row in op_B:
        prefix = str(row[0])
        for i in range(len(prefix)):
            if number[i] == prefix[i]:
                minlen = len(prefix)
                if number[0:i+1] == prefix:
                    if minlen > maxlen:
                        maxlen = minlen
                        listB.append(row[1])
            else:
                break
        minlen = 0
    if listA == []:
        priceA = ""
    else:
        priceA = float(listA[-1])
    if listB == []:
        priceB = ""
    else:
        priceB = float(listB[-1])

    if priceA == "" and priceB == "":
        return "No operator"
    elif priceA != 0 and priceB == "":
        return "OperatorA {}$".format(priceA)
    elif priceA == "" and priceB != 0:
        return "OperatorB {}$".format(priceB)
    elif priceA < priceB:
        return "OperatorA {}$".format(priceA)
    elif priceB < priceA:
        return "OperatorB {}$".format(priceB)
    else:
        return "OperatorA and OperatorB {}$".format(priceA)


def main():
    while True:
        try:
            phoneNumber = str(int(sys.stdin.readline()))
            if not len(phoneNumber) == 11:
                raise ValueError
            else:
                print(choose(phoneNumber))

        except ValueError:
            print("Please enter the correct number format in 11 digits")
        else:
            break


if __name__ == "__main__":
    main()
