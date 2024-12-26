while (st:=input()) != '.':
    st = ''.join(filter(lambda x: x in ('[',']','(',')','.'), st))
    while '[]' in st or '()' in st:
        st = st.replace('[]','').replace('()','')
    if st == '.': print('yes')
    else: print('no')