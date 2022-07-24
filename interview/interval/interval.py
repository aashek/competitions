'''
You have a list of licenses for a product. Find the earliest year which is not covered by an unexpired license.
'''


# [(2011, 2015),
#  (2021, 2022),
#  (2014, 2018),
#  (2030, 2035),
#  (2019, 2019)]
# Result: 2020

# naive solution (first solution)

# get the first start date

li = [(2011, 2015),
 (2021, 2022),
 (2014, 2018),
 (2030, 2035),
 (2019, 2019)]

# min_year = sorted(li)[0][0]
# 2011, 12, 13, 14, 15

# list of all the years covered

# iterate the solution to make it faster, since we value speed and not space

# iter