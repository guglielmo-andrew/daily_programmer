'''Problem: How many Lychrel numbers are there below ten-thousand?'''

def main():
    up_to = int(input("Up to what number? "))
    lychrel_numbers = []
    not_lychrel_numbers = []
    for n in range(up_to):
        if get_lychrel_numbers(n):
            lychrel_numbers.append(n)
        else:
            not_lychrel_numbers.append(n)
    print(f'The number of Lychrel numbers under {up_to:,} is {len(lychrel_numbers):,}.')
    print(f'The number of non-Lychrel numbers under {up_to:,} is {len(not_lychrel_numbers):,}.')

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