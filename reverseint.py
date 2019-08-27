def rev_int(number):
    return '-' + "".join([n for n in str(number)[-1:0]]) if number < 0 else "".join([n for n in str(number)[::-1]])

print(rev_int(-4142471383))