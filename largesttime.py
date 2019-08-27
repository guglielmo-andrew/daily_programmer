def largestTime(arr):
    #arr must be 4 numbers
    if len(arr) != 4:
        return ""

    #Initialize final array and position counter
    time_arr = ['0','0',':','0','0']
    position = 0 
    
    #Get first two digits
    while position < 2:
        if 2 in arr:
            time_arr[position] = "2"
            arr.pop(arr.index(2))
        elif 3 in arr and position == 1:
            time_arr[position] = "3"
            arr.pop(arr.index(3))
        elif 1 in arr:
            time_arr[position] = "1"
            arr.pop(arr.index(1))
        elif 0 in arr:
            time_arr[position] = "0"
            arr.pop(arr.index(0))
        #If the array didn't have a 0, 1, or 2, for the first position, 
        # or 3 for the second then there is not a valid time
        else: 
            return ""
        position += 1
    
    #Keep the ':' in position 2
    position += 1
    
    #Third number
    arr.sort(reverse=True) #Largest number considered first but must be less than 6
    if arr[0] < 6:
        time_arr[position] = str(arr[0])
        arr.pop(0)
    elif arr[1] < 6:
        time_arr[position] = str(arr[1])
        arr.pop(1)
    else:
        return "" #If there isn't a number less than 6, can't be a vaild time
    position += 1
    
    #Last number remaining
    time_arr[position] = str(arr[0])
    
    return "".join(time_arr)

print(largestTime([1, 2, 3, 4]))