#This program looks at the randrange function
#of the random module
# randrange ([start,] stop [,step])
#
#  start − Start point of the range.
#   This would be included in the range.
#   Default 0
#
#  stop − Stop point of the range.
#   This would be excluded from the range.
#
#  step − Steps to be added in a number to decide a random number.
#   Default 1
#   Includes start, skips next
#   For odd numbers, start with odd number
#   For even numbers, start with even number

import random
#Even number
print(random.randrange(0,11,2))

#Odd number
print(random.randrange(1,12,2))
