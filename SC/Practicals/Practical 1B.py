n = int(input('Enter the number of elements: '))
print('Enter the inputs: ')
inputs = []
for i in range(0, n):
	ele = float(input())
	inputs.append(ele)
print(inputs)
print('Enter the weights: ')
weights = []
for i in range(0, n):
	ele = float(input())
	weights.append(ele)
print(weights)
print('The net input can be calculated as Yin = b + x1w1 + x2w2')
b = float(input('Enter the number of bias: '))
Yin = []
for i in range(0, n):
	Yin.append(inputs[i]*weights[i])
net = round((sum(Yin) + b), 2)
print('Net: ', net)
input('')