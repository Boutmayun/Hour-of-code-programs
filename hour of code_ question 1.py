##input will be a matrix, you have to print it back in spiral form.
##example:
##    [1,2,3]
##    [4,5,6]
##    [7,8,9]
##output should be: [1,2,3,6,9,8,7,4,5](spiral)
##the spiral loop is clockwise.
##WAP to find it for a NxN matrix.

##UNCOMMENT B TO TEST FOR DIFFERENT VALUES

#let matrix be
#b=[[1,2,3],[4,5,6],[7,8,9]]
#b=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
b=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
L=[]
#first low is normally printed, and the last one is reversed.it is the
#middle that you need to figure
def spiral(a):
    global L
    if len(a)==1 and len(a[0])==1:#if only one element remaining,add to L and return it.
        L+=a[0]
        return L
    else:
        L+=a[0]
        for i in range(1,len(a)-1): #only the middle layers
            L+=[a[i][len(a)-1]]      #the length is equal to the number of rows, coz it's a NxN ma

        L+=a[len(a)-1][::-1]

        for i in range(len(a)-2,0,-1): #only the middle layers
            L+=[a[i][0]]

        
        length=len(a)
    
    
        del(a[0]); 
        del[a[len(a)-1]] #deleting first and last rows

        for i in range(len(a)):
            del(a[i][0])
            del(a[i][length-2])#-2 because if a[0] deleted, then length will decrease
        

    #NOW, we have only the middle matrix.this too may be another matrix
    #if N is a large number.hence we have to implement recursion
    if a==[]:
        return L
    else:
        return spiral(a)
           


print spiral(b)
    


