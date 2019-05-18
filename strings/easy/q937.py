# -*- coding: utf-8 -*-
"""
Created on Wed May  1 14:22:30 2019

@author: pengz
"""

'''
You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

    Each word after the identifier will consist only of lowercase letters, or;
    Each word after the identifier will consist only of digits.

We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed 
that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The 
letter-logs are ordered lexicographically ignoring identifier, with the identifier used 
in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.

 

Example 1:

Input: ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
'''
def reorderLogFiles(logs: list) -> list:   ## solution from others, genius
    digits = []
    letters = []
    for log in logs:
        log_item = log.split(' ')
        if log_item[1].isdigit == True:
            digits.append(log)
        else:
            letters.append(log)
    ## 然后按照顺序排序letters
    letters.sort(key = lambda x: (x.split(' ')[1:],x.split(' ')[0]))  ## 这是有优先顺序的, 先按照1:,最后才是第一项
                    
    ret = letters + digits                
    return ret
letters = ["ab1 off key dog","a8 act zoo","g1 act car","a1 act car"]
#letters.sort(key = lambda x: x.split(' ')[0])
letters.sort(key = lambda x: (x.split(' ')[1:],x.split(' ')[0]))
#letters.sort(key = lambda x: x.split(' ')[0])
    