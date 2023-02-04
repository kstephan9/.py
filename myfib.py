def main():
    print("Reached main()")

    n = 4

    myval = [1, 1, 1, 1, 1]
    myval[0] = 0
    myval[1] = 1
    myval[2] = 0
    myval[3] = 0

    i = 2
    myval[i] = myval[i - 2] + myval[i - 1]
    print(len(myval))
    for i2 in myval:
        print(i2)


if __name__ == "__main__":
    print("run directly")
    main()
else:
    print("run from an import")
    