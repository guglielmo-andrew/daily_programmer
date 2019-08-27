start = bin(int(input("Input: ")))
mid = []
for n in start:
    mid.append(n)
for i in range(2, len(mid)): #Skip the '0b' and change the 1s and 0s
    if mid[i] == "0":
        mid[i] = "1"
    else:
        mid[i] = "0"
end = "".join(mid)
print("Output:", int(end, 2)) #Convert the text back into an int with base 2
