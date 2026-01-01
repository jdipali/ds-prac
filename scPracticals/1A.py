x = float(input('Enter the value of x: '))
w = float(input('Enter the value of w: '))
b = float(input('Enter the value of b: '))
net = int(w*x+b)
if (net<0):
        out=0
elif(net>=0)&(net<=1):
        out=net
else:
        out=1
print('Net: ', net)
print('Output: ', out)
input('')