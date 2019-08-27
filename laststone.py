#Last Stone
#x == y -> both destroyed
#x <= y -> x destroyed, y = y - x
#What is the last stone?

def laststone(stones_list):
    if len(stones_list) == 0:
        return "No stones remaining."
    elif len(stones_list) == 1:
        return(stones_list[0])
    else:
        stones_list.sort(reverse=True)
        if stones_list[0] == stones_list[1]:
            stones_list.pop(1)
            stones_list.pop(0)
        elif stones_list[0] > stones_list[1]:
            stones_list[0] = stones_list[0] - stones_list[1]
            stones_list.pop(1)
        return laststone(stones_list)

