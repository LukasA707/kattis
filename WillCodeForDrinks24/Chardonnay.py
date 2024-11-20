input = int(input())

bottlesRest = input % 7

if bottlesRest == 0:
    print(input)
else:
    print(input + 1)