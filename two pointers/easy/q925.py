# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 15:08:15 2019

@author: pengz
"""

'''
Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, 
the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.  Return True if it is possible that 
it was your friends name, with some characters (possibly none) being long pressed.

 

Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.

Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.

Example 3:

Input: name = "leelee", typed = "lleeelee"
Output: true

Example 4:

Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.

 

Note:

    name.length <= 1000
    typed.length <= 1000
    The characters of name and typed are lowercase letters.
'''

## 从solution看到这道题还有一种case需要解决，就是abc和abcd,alex和alexttt这种
def isLongPressedName(name: str, typed: str) -> bool:  ## written by my own
    if len(typed) < len(name):
        return False
    if len(name) == 0:
        return len(typed) == 0
    i = 0  ## pointer for name
    j = 0  ## pointer for typed
    while i < len(name) or j < len(typed):
        if i < len(name):   ## 如果i超出了,tmp就一直是 the last char of name
            tmp = name[i]
            i = i+1
        re_n = 1   ## repeated times of this char in name
        while i < len(name):   ## 确定这个字母在这一段中有连续几个，不包含开头的那个
            if name[i] == tmp:
                re_n += 1
                i += 1        ## 这个循环跳出的时候,i已经在下一个不重复的字母那里了
            else:
                break
        print(tmp,re_n)
        re_t = 1
        if j >= len(typed) or typed[j] != tmp:  ## 如果当前这个字符不相等，或者typed已经不够长了但是name还有字符
            return False
        else:
            j = j+1
        while j < len(typed):   ## 这个循环跳出的时候,j已经在下一个不重复的字母那里了
            if typed[j] == tmp:
                re_t = re_t + 1
                j = j+1
            else:
                break
        if re_t < re_n:   ## 如果这个字符在typed的重复次数还没name多
            return False
        else:
            continue
    return True

a = isLongPressedName(name = "aaaaaabbbbbbdsssssc", typed = "aaaaaaabbbbcdssssss")
                
            
            
        
            
    