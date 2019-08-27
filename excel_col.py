base = 26
letters = []
nums = []
sum = 0
col_str = input('Column: ')
col_str.upper()
for c in col_str:
    letters.append(c)
letters.reverse()
for i in range(len(letters)):
    nums.append((ord(letters[i]) - ord('A') + 1)*(base**i))
for n in nums:
    sum += n
print(sum)
    