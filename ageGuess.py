def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    remd3 = int(input())
    remd5 = int(input())
    remd7 = int(input())
    age = (remd3 * 70 + remd5 * 21 + remd7 * 15) % 105

    print("Your age is {0};".format(age))
guess_age()