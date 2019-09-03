# Relative Sort Array in Python



def main():
    # Two input list and the answer
    list1 = [2,3,1,3,2,4,6,7,9,2,19]
    list2 = [2,1,4,3,9,6]
    answer = [2,2,2,1,4,3,3,9,6,7,19]
    rel_sorted_list = relative_sort(list1,list2)
    print(answer)
    # Check if the answers match
    print("Correct?", rel_sorted_list == answer)

def relative_sort(arr1, arr2):
    # Sorted list container
    arr1_sorted = []
    for n in arr2:
        while n in arr1:
            arr1_sorted.append(n) # If the number is in arr1, add to the container
            arr1.pop(arr1.index(n)) # Remove the added number from arr1
    sorted(arr1) # Sort the remaining numbers in accending order
    # Append the remaining numbers to the container
    for m in arr1:
        arr1_sorted.append(m)
    return arr1_sorted

if __name__ == "__main__":
    main()


        