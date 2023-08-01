'''You are given a list of n-1 integers and these integers are in the range of 1-n. There
are no duplicates in the list. One of the integers is missing in the list. Write an efficient
code to find the missing integer.'''

def miss(arr,n):
    total=0
    for i in range(0,len(arr)):
        total=total+arr[i]
    naturalsum=n*(n+1)/2
    return naturalsum-total
if __name__ == '__main__':
    arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20]
    missingNumber=miss(arr,len(arr)+1)
    print("missing number is ",missingNumber)
