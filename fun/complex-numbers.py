print('complex no:',1+1j)
print('complex:',(1+1j) *(1-1j))

radius=10
area_of_circle=3.14 * radius **2
print('area circle',area_of_circle)

def merge_sort(arr):
    if len(arr) >1:
        left_arr=arr[0:len(arr)//2]
        right_arr=arr[len(arr)//2:len(arr)]
        merge_sort(left_arr)
        merge_sort(right_arr)
        i=0
        j=0
        k=0
        while i<len(left_arr) and j<(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k]=left_arr[i]
                i +=1
                k +=1
            else:
                arr[k]=left_arr[i]
                j+=1
                k+=1
                while i< len(left_arr):
                    arr[k]=left_arr[i]
                    i +=1
                    k +=1
                    while j<len(right_arr):
                        arr[k]=right_arr[j]
                        j+=1
                        k+=1
                        arr_test=[2,3,5,1,7,4,4,4,2,6,0]
                        merge_sort(arr_test)
                        print(arr_test)
                    
                