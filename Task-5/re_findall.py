# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
cons = 'QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm'
vowels = 'AEIOUaeiou'

string=input().strip()

m = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (cons, vowels, cons), string)
    
print("\n".join(m or ['-1']))
    