[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

    mean0 = live.totalwgt_lb.mean()
    mean1 = firsts.totalwgt_lb.mean()
    mean2 = others.totalwgt_lb.mean()

    var1 = firsts.totalwgt_lb.var()
    var2 = others.totalwgt_lb.var()

    print('Mean')
    print('First babies', mean1)
    print('Others', mean2)

    print('Variance')
    print('First babies', var1)
    print('Others', var2)

    print('Difference in lbs', mean1 - mean2)
    print('Difference in oz', (mean1 - mean2) * 16)

    print('Difference relative to mean (%age points)', 
          (mean1 - mean2) / mean0 * 100)

    d = thinkstats2.CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
    print('Cohen d', d)
    
    Result:
    First babies 7.20109443044
    Others 7.32585561497
    Variance
    First babies 2.01802730092
    Others 1.9437810259
    Difference in lbs -0.124761184535
    Difference in oz -1.99617895257
    Difference relative to mean (%age points) -1.71714236784
    Cohen d -0.0886729270726
    
    A small difference exists between the first babies and others but Cohen's d indicates that the differences are very small. The first babies weigh less than the others. 
