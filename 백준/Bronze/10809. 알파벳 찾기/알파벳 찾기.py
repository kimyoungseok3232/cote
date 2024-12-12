st = input()
al = [chr(i) for i in range(ord('a'), ord('z') + 1)]
for l in al: print(st.find(l),end=' ')