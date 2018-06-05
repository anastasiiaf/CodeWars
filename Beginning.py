##############################################################################################
# Multiples of 3 or 5
##############################################################################################
#If we list all the natural numbers below 10 that are multiples of 3 or 5, 
#we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Finish the solution so that it returns the sum of all the multiples of 3 or 5 
#below the number passed in.
#
#Note: If the number is a multiple of both 3 and 5, only count it once.


def solution(number):
  r = range(1,number)
  m3 = [i for i in r if i % 3==0]
  m5 = [i for i in r if i % 5==0]
  m = m3 + m5
  m = list(set(m))
  print(sum(m))
  
solution(10)  



##############################################################################################
# Find The Parity Outlier
##############################################################################################
#You are given an array (which will have a length of at least 3, but could be very large) 
#containing integers. The array is either entirely comprised of odd integers or entirely 
#comprised of even integers except for a single integer N. Write a method that takes the 
#array as an argument and returns this "outlier" N.
#
#Examples
#[2, 4, 0, 100, 4, 11, 2602, 36]
#Should return: 11 (the only odd number)
#
#[160, 3, 1719, 19, 11, 13, -21]
#Should return: 160 (the only even number)


def find_outlier(integers):
    n = [i for i in integers if i % 2==0]
    if len(n)>1:
       return([i for i in integers if i not in n][0])
    else:   
       return(n[0])

n = find_outlier([2, 4, 6, 8, 10, 3])
print(n)




##############################################################################################
# Highest and Lowest
##############################################################################################
#In this little assignment you are given a string of space separated numbers,
# and have to return the highest and lowest number.
#Output string must be two numbers separated by a single space, and highest number is first 


def high_and_low(numbers):
    n = [int(i) for i in numbers.split()]
    #print('%i %i' %(max(n),min(n)))
    return(str(max(n))+" "+str(min(n)))

high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")























