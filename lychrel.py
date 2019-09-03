'''Problem: How many Lychrel numbers are there below ten-thousand?'''

def main():
    up_to = int(input("Up to what number? "))
    lychrel_numbers = []
    not_lychrel_numbers = []
    for n in range(up_to):
        if get_lychrel_numbers(n):
            not_lychrel_numbers.append(n)
        else:
            lychrel_numbers.append(n)
    print(f'The number of Lychrel numbers under {up_to:,} is {len(lychrel_numbers):,}.')
    print(f'The number of non-Lychrel numbers under {up_to:,} is {len(not_lychrel_numbers):,}.')
    try:
        print(lychrel_numbers.index(196))
    except:
        print('Not in lychrel_numbers list')
    try:
        print(not_lychrel_numbers.index(196))
    except:
        print('Not in non_lychrel_numbers list')

def get_lychrel_numbers(x):
    first_number = x    
    for i in range (50):
        second_number = int("".join(reversed([c for c in str(first_number)])))
        check_number = first_number + second_number
        if check_number == int("".join(reversed([l for l in str(check_number)]))):
            return True
        else:
            first_number = check_number
    return False

if __name__ == '__main__':
    main()