[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

import thinkstats2
pmf = thinkstats2.Pmf(resp.numkdhh)

import thinkplot
thinkplot.Pmf(pmf, label='numkdhh')
thinkplot.Show()

biased = BiasPmf(pmf, label='biased')

thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased])
thinkplot.Show()



pmf.Mean()
1.0242051550438309

biased.Mean()
2.4036791006642821

As expected, the biased mean is higher. 