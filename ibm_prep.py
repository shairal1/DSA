#%% wron
def bid(pc,target):
    seen = set()
    for i in pc:
        if i not in seen:
            seen.add(i)
    print(seen)
    pair=set()
    for i in seen:
        print(i)
        if (target-i !=i and (target-i)or (i-target)  in seen):
            pair.add(tuple(sorted([i, target-i])))
    return pair
bid([1,3,5],2)
#%%https://askfilo.com/user-question-answers-smart-solutions/hackerrank-com-test-1osk0dhn7a2-questions-521e953466a67-46m-3136303638353338
def bid(pc,target):
    seen=set(pc)
    pair=set()
    for i in seen:
        if i !=target-i and target -i in seen:
            pair.add(tuple(sorted([i,target-i])))
        if i !=target+i and target +i in seen:
            pair.add(tuple(sorted([i,target+i])))
    return len(pair)
print(bid([1,3,5],2))
#%%
dates=['2024 jan 01','2023 sept 02','2023 jan 03','2023 feb 04']
def sort(dates):
    l= []
    for i in range(len(dates)):
        y,m,d=dates[i].split(' ')
        l.append((int(y),m,int(d)))
    l=sorted(l,key=lambda x: (-x[0],11-['jan','feb','mar','apr','may','jun','jul','aug','sept','oct','nov','dec'].index(x[1]),-x[2]))
    return [' '.join(map(str, (x[0], x[1], x[2]))) for x in l]
print(sort(dates))
#%%
#https://www.youtube.com/watch?v=qoFFsfpNzQQ&list=PLIUso1jSUd-Y9E2mxrhz5dqaldmZCtVxT
s='10001110110'
def min_flips(pwd):
    flips = 0
    for i in range(0, len(pwd), 2):
        if pwd[i] != pwd[i + 1]:
            flips += 1
    return flips

# Example usage:
pwd = "011010"
print(min_flips(pwd))  # Output: 3
#%%
# 
from collections import Counter
import math
word='baabacaa'
def min_moves(s):
    moves=0
    frq=Counter(s)
    for i ,c in frq.items():

            moves+= c//2

            
    return moves
min_moves(word)
#%%
def triplet(nums,divisor):
    set_=set(nums)
    for i in set_.tems():
        for j in set_.items():
            if i+j+k % divisor == 0:
#%%
l=['2 2 3','4 4 4','7 8 9']

    #for i in l :
x= [ len(set(map(int, i.split()))) for i in l]
print(x)
#%%
def is_substring(word, substring):
    for i,s in enumerate(substring):
        ind=word.index(s)
        if ind != -1:
            sub=word[ind-i:ind+len(s)-i] 
            x=i
            r=True
            while ind!=0:
                if substring[x-1]!= word[ind-1] and word[ind-1]!='?':
                    r=False
                    break
                x-=1
                ind=-1
            ind=word.index(s)
            if r:
                while ind!= len(word)-1:
                    if substring[x+1]!= word[ind+1] and word[ind+1]!='?':
                        r=False
                        break                           
                    ind+=1
                    x+=1
            if r:
                return True
    return False
                
            
            
print(is_substring("abcde", "bcd"))      # True#
#print(is_substring("a?cde", "abc"))      # True
#print(is_substring("xyz", "abc"))        # False
print(is_substring("ab?de", "abc"))      # False
print(is_substring("?????", "hello"))    # True
print(is_substring("a?c?e", "abcde"))    # True            
#%%
def is_substring(word, substring):
    n, m = len(word), len(substring)

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if word[i + j] != substring[j] and word[i + j] != '?':
                match = False
                break
        if match:
            return True
    return False
#%%
#https://leetcode.com/discuss/post/6723381/ibm-junior-developper-oe-assesment-by-an-yzdd/
def getMinOperations(s,m,k):
    count=0
    freq=0
    for j in range(len(s)):
        
        if s[j]=='0':
            count+=1
        if s[j] =='1':
            count=0
        if count==m:
            freq+=1
            count=0
            j=j+k#########wrong way to skip
    return freq
#%%
def getMinOperations(s, m, k):
    count = 0
    freq = 0
    i = 0
    while i < len(s):
        if s[i] == '0':
            count += 1
        else:
            count = 0

        if count == m:
            freq += 1
            count = 0
            i += k  # now this works as intended
        else:
            i += 1

    return freq
       
getMinOperations("0001000", 3, 2)
#%%

#%%
run_tests()
#%%
l2 = ["alice", "alicia", "alex", "bob"]
l1 = ["al", "ali", "b", "z"]#
#l1=['a','ab','abc']
#l2=['a','ab','abc','abcd','abde']
l=[0]*len(l2)
for j in range(len(l2)):
    for i in range(len(l1)):
        if l1[i]==l2[j][0:len(l1[i])]:
            l[j]+=1

print(l)