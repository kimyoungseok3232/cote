n = int(input())
words = set()
for i in range(n):
    st = input()
    words.add((st,len(st)))
words = sorted(list(words),key = lambda x: (x[1],x[0]))
for word in words:
    print(word[0])