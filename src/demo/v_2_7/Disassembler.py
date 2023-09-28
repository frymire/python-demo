'''
Created on May 31, 2014

@author: Mark.E.Frymire
'''
import dis

def sumIt():
    vara = 10
    varb = 20

    sumIt = vara + varb
    print "vara + varb = %d" % sumIt

# Call dis function for the function.
dis.dis(sumIt)