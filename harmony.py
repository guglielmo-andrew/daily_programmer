def harmony(numbers):
    y = len(numbers)
    for i in range(len(numbers)):
        smaller = numbers[i:(y - i)]
        if max(smaller) - min(smaller) == 1:
            return len(smaller)

harmony([1,3,2,2,5,2,3,7])