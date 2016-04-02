[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

Code:

import scipy.stats

mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)
type(dist)

low = dist.cdf(177.8)    # 5'10"
high = dist.cdf(185.4)   # 6'1"

high-low = .342, so 34.2% of the US male population is within the blue man range. 


