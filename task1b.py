from collections import Counter

with open("Book1.txt") as input_file:
    
    count = Counter(word for line in input_file
                         for word in line.split())

print(count.most_common1(10))


with open("Book2.txt") as input_file:
    
    count2 = Counter(word2 for line2 in input_file2
                         for word2 in line2.split())

print(count.most_common2(10)


with open("Book3.txt") as input_file3:
    
    count3 = Counter(word3 for line3 in input_file3
                         for word3 in line.split())

print(count.most_common3(10))
