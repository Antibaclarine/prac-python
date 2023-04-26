def name():
    firstname="Ana"
    lastname="Mercy"
    space=''
    full_name=firstname + space +lastname
    return full_name
    print(name(full_name))

# Write a function that takes a list of numbers as input and returns the average of the numbers.

def fullnumbers(*numbers):
 return sum(numbers) / len(numbers)  

# Write a function that takes a string as input and returns True if the string is a palindrome, and False otherwise.
def palindrome(str):
 for i in range(0, int(len(str)/2)):
     if str[i] !=str[len(str)-i-1]:
         return False
     return True
 
 def merge(arr):
    if len(arr) >1:
        left_arr=arr[0:len(arr)//2]
        right_arr=arr[len(arr)//2:len(arr)]
        merge(left_arr)
        merge(right_arr)
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
                        merge(arr_test)
                        print(arr_test)