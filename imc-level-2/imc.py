import math

# challenge_1
# please view the picture challenge_1.png

frac = 103/101
sum = 0
for i in range(1,101):
    sum+= math.floor(frac*i)
print(sum)

# 2 _ _ _


# challenge_2
'''

Answer the question below:

Oh no! Our trading system is bugged out and we can only send buy orders in volumes of 7 and 17. How many different size orders can we make from 1 to 100 using the two order volumes?

What is the answer to the question?
'''

lProds = []
rProds = []

n = 0
while n < 100:
    lProds.append(n)
    n += 7
print(lProds)

n = 0
while n < 100:
    rProds.append(n)
    n += 17
print(rProds)

s = set()
for i in lProds:
    for j in rProds:
        if i + j <= 100:
            s.add(i + j)

print(s, len(s))

# _ 9 _ _


# challenge_3
'''
Answer the question below:

n friends go out for lunch, each with a distinct amount of cash. Turns out that for every pair of friends, there exists a subset of the remaining friends that have the same amount of cash.

What is the minimum of n?
'''

# n friends

# 4 friends
# 0 1 2 3
# 1 2 3 4
# 1-2 {3}
# 1-3 {4}
# 1-4 ?X

# 1 2 3 4 5 6
# 2 3 4 5 6 7
#


# valid sol
# 1 2 3 4 5 6 7
#

# q is can i create the last the last two from a subset

# ANS : 6

# _ _ 1 _


# challenge_4
'''
Answer the question below:

Leo has some transparent 1x1x1 cubes arranged in a 72x98x56 bigger rectangular prism. He shines a light beam through the two furthest corners of the rectangular prism.

How many cubes does the light beam pass through?
'''

# math?

# l,b,w = 72,98,56

# from (0,0,0) to (72,98,56)
# https://www.reddit.com/r/learnmath/comments/u0p8a6/how_many_cubes_does_the_light_beam_pass_through/

# ANS : 240

# _ _ _ 9