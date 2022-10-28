#создаем файл data.txt
f = open('data.txt', 'w')
#напишем в открывшийся файл даты в нужном формате!
f.write("12-11-1900")
f.write("\n")
f.write("31-12-1908")
f.write("\n")
f.write("24-10-1910")
f.close()

f = open("data.txt", "r")
s = f.readlines()
numbers = [int(x) for x in s]
print(min(numbers))
print(max(numbers))
print(min(numbers) + max(numbers))
index = numbers.index(max(numbers))
print(index)