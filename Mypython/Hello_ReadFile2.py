#file = open(file='demo.txt', mode='r', encoding='utf-8')
file = open('demo.txt', 'r', encoding='utf-8')
print(file)
data = file.read()
print(data)