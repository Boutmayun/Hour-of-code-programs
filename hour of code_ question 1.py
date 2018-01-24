##original question:
##input will be a matrix, you have to print it back in spiral form.
##example:
##    [1,2,3]
##    [4,5,6]
##    [7,8,9]
##output should be: [1,2,3,6,9,8,7,4,5](spiral)
##the spiral loop is clockwise.
##WAP to find it for a NxN matrix.


#if you dont want this to be for the given numbers(1-n**2), just use 1,2..n**2 as a key in the dictionary and replace the values with values from the custom matrix.
import itertools
n=7
n2=n**2
numbers=iter(range(1,n2+1))
L=[[0 for i in range(n)]for j in range(n)]

#some functions to make our lives easier:
def isfull(L):
    return True if 0 not in list(itertools.chain(*L)) else False
def displaymatrix(L):
    for i in range(n):
        for j in range(n):
            print L[i][j],
        print

#function to insert values into periphery of a padded matrix(from all 4 sides).Recurses until matrix is full/iterable "numbers" gets consumed.        
def fill_periphery(padding=0):
    try:
        #top row:
        for i in range(padding,n-padding):
            L[padding][i]=next(numbers)
        #right:
        for i in range(padding+1,n-padding-1):
            L[i][-1-padding]=next(numbers)
        #bottom:
        for i in range(padding,n-padding):
            L[-1-padding][-1-i]=next(numbers)
        #left:
        for i in range(padding+1,n-padding-1):
            L[-1-i][0+padding ]=next(numbers)
    except StopIteration:pass

    if isfull(L)==False:
        fill_periphery(padding+1)
    return L


print 'final spiral:'
L=fill_periphery()
displaymatrix(L)