'''Given two positive integers x and y, an integer is powerful if it is equal to x^i + y^j for some integers i >= 0 and j >= 0.
Return a list of all powerful integers that have value less than or equal to bound.
You may return the answer in any order.  In your answer, each value should occur at most once.'''

def main():
    print(power_int(2, 3, 10))

def power_int(x, y, bound):
    ans = set()
    for num in range(bound + 1):
        for i in range(bound):
            for j in range(bound):
                if x**i + y**j == num:
                    ans.add(num)
    return(list(ans))

if __name__ == '__main__':
    main()