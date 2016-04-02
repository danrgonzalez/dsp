[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

import thinkstats2
import thinkplot

import random
t = [random.random() for _ in range(1000)]
pmf = thinkstats2.Pmf(t)
thinkplot.Pmf(pmf, linewidth=0.1)
thinkplot.Show()

As expected, the pmf plot is evenly distributed with equal probabilities. 

cdf = thinkstats2.Cdf(t)
thinkplot.Cdf(cdf)
thinkplot.Show()

The cdf, shows a straight line, as expected, due to the uniform pmf.
