##############################################################################################
# 1.  Multiples of 3 or 5
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
# 2. Find The Parity Outlier
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
# 3. Highest and Lowest
##############################################################################################
#In this little assignment you are given a string of space separated numbers,
# and have to return the highest and lowest number.
#Output string must be two numbers separated by a single space, and highest number is first 


def high_and_low(numbers):
    n = [int(i) for i in numbers.split()]
    #print('%i %i' %(max(n),min(n)))
    return(str(max(n))+" "+str(min(n)))

high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")



##############################################################################################
# 4. Digital root
##############################################################################################
#A digital root is the recursive sum of all the digits in a number. 
#Given n, take the sum of the digits of n. If that value has two digits,
#continue reducing in this way until a single-digit number is produced. 
#This is only applicable to the natural numbers.

def digital_root(n):
    s = sum([int(i) for i in list(str(n))])
    while len(list(str(s)))>1:
        s = sum([int(i) for i in list(str(s))])
    return(s)

r = digital_root(982)



##############################################################################################
# 5. Printer error
##############################################################################################
def printer_error(s):
    c = [chr(i) for i in range(ord('a'),ord('m')+1)]
    error = [i for i in list(s) if i not in c]
    return(str(len(error))+'/'+str(len(list(s))))

ratio = printer_error("aaaxbbbbyyhwawiwjjjwwm")
print(ratio)


##############################################################################################
# 6. Count the number of Duplicates
##############################################################################################
#Write a function that will return the count of distinct case-insensitive alphabetic 
#characters and numeric digits that occur more than once in the input string. 
#The input string can be assumed to contain only alphabets (both uppercase and lowercase)
# and numeric digits.

def duplicate_count(text):
    t = list(text.upper())
    my_dict = {i:t.count(i) for i in t}
    y=[1 for i in my_dict.keys() if my_dict[i]>1]
    return(sum(y))

s = duplicate_count("indivisibility")
print(s)



##############################################################################################
# 7. Where my anagrams at?
##############################################################################################
#Write a function that will find all the anagrams of a word from a list. 
#You will be given two inputs a word and an array with words. You should 
#return an array of all the anagrams or an empty array if there are none. 
#a)
  def anagrams(word, words):
    t = list(word)
    my_dict = {i:t.count(i) for i in t}
    t_elem = [my_dict[i] for i in my_dict.keys()]
    anag = []
    for j in words:
        next_word = list(j)
        next_word_dict = {i:next_word.count(i) for i in next_word}
        if len(next_word_dict.keys())==len(my_dict.keys()) and set(list(next_word_dict.keys()))==set(list(my_dict.keys())): 
            new_elem = [next_word_dict[i] for i in next_word_dict.keys()] 
            if new_elem==t_elem:  
               anag.append(j)
                
    return(anag)            

#b)
  def anagrams(word, words): 
    return [item for item in words if sorted(item)==sorted(word)]   
         
anag = anagrams('abba', ['aabb', 'bbaa', 'dada'])    
print(anag)        
