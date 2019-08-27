def tallestBillboard(arr):
    arr.sort()
    sub_arr1 = []
    sub_arr2 = []

    test_case = arr[-1]
    n = 0
    m = 1
    while n < len(arr) - 1:
        while m < len(arr):
            if arr[n:m] == test_case:
                sub_arr1.append(test_case)
                for x in arr[n:m]
                    sub_arr2.append(x)
                del arr[-1]
                del arr[n:m]