# Loop over number 1 - 100
# If number === 3 then print Fizz
# If number === 5 then print Buzz
# Else print the number


# Quick and cheap. Imperitave
def fizzBuzz(x):
    if x % 3 == 0 and x % 5 == 0:
        print("Fizzbuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)


for x in range(1, 101):
    fizzBuzz(x)


# Maintainable, Functional?
testCases = [{3: "Fizz"}, {5: "Buzz"}, {7: "Bazz"}, {9: "Fuzz"}]


def fizzbuzz(x):
    def runTest(test):
        if x % list(test.keys())[0] == 0:
            return list(test.values())[0]
        return False

    results = list(filter(lambda x: x, list(map(runTest, testCases))))
    if len(results) != 0:
        return "".join(results)
    return x


nums = [n for n in range(1, 101)]
results = list(map(fizzbuzz, nums))
for x in results:
    print(x)
