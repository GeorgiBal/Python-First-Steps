name = 'George'
print('Hello {}! Nice to meet you.'.format(name))
print('Hello {:10}! Nice to meet you.'.format(name))
print('Hello {:>10}! Nice to meet you.'.format(name))
print('Hello {:<10}! Nice to meet you.'.format(name))
print('Hello {:^10}! Nice to meet you.'.format(name))

pi = 3.14159
print('The num PI is {:.2f}'.format(pi))

num = 1000
print('The num is {:,}'.format(num))
print('The num is {:b}'.format(num))
print('The num is {:o}'.format(num))
print('The num is {:X}'.format(num))
print('The num is {:E}'.format(num))
