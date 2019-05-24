import math

"""
  This implementation is based on LLR interpretation provided in the following
  paper (see table and equations in page 7):
 
  Java, Akshay, et al. "Why we twitter: understanding microblogging usage and
  communities." Proceedings of the 9th WebKDD and 1st SNA-KDD 2007 workshop on
  Web mining and social network analysis. ACM, 2007.
  Available at: http://aisl.umbc.edu/resources/369.pdf
 
  @param a frequency of token of interest in dataset A
  @param b frequency of token of interest in dataset B
  @param c total number of observations in dataset A
  @param d total number of observations in dataset B
  @return"""
 
def rootLogLikelihoodRatio (a, b, c, d):
    E1=c*(a+b)/(c+d)
    E2=d*(a+b)/(c+d)
 # To avoid a division by 0 if a or b equal 0 they are replaced by 1
    if a==0 and b==0:
        result=2*(a*math.log(a/E1+1)+b*math.log(b/E2+1))
        result=math.sqrt(result)
        if (a/c)<(b/d):
            result=-result
    elif a==0 and b!=0:
        result=2*(a*math.log(a/E1+1)+b*math.log(b/E2))
        result=math.sqrt(result)
        if (a/c)<(b/d):
            result=-result
    elif a!=0 and b==0:
        result=2*(a*math.log(a/E1)+b*math.log(b/E2+1))
        result=math.sqrt(result)
        if (a/c)<(b/d):
            result=-result
    else:
        result=2*(a*math.log(a/E1)+b*math.log(b/E2))
        result=math.sqrt(result)
        if (a/c)<(b/d):
            result=-result
    
    return result

print(rootLogLikelihoodRatio(2213,6,4668948,9854))