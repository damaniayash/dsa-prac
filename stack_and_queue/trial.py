import re
a = 'abc'
a = 2*a
print(a)
dg = '{}'
print(dg.isdigit())

a = re.sub('\D+', '|', '3a34bgh56kk789llll')[0:-1]
print(a)
a = a.split('|')
for i in range(0,len(a)):
	a[i] = int(a[i])
print(a)