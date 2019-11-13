def minimumSwaps(arr):
        counter = 0

        for i in range(len(arr)):

                if (arr[i]) != i+1:
                        l = arr.index(i+1)
                        arr[i],arr[l] = i+1,arr[i]
                        counter += 1


        return counter
