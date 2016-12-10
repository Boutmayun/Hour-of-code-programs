##Question: there is a list of numbers, from 1 to 1000,with each number
##appearing only once
##        there is another list of numbers with 1001 elements,
##        but there is one repeated number
##find the repeated number
##Personal view: this was by far the easiest in the bunch

#making a list containing 1000 elements
L1=range(1,1001)
#another list, with an extra element.Let it be 7.
L2=range(1,1001)+[7]
#sum() finds the sum of numeric elements in he list
sum1=sum(L1)
sum2=sum(L2)

#the repeated element is sum2-sum1. Seems obvious here, but is useful when
#the repeated element is not known

print 'repeated element is:',sum2-sum1
