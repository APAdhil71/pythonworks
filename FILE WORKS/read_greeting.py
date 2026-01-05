file_path="while_loop\\for_loop\\nested_loop\\functions\\string_works\\list_works\\tuple_works\\set_works\\dictionary_works\\comprehension\\lambda_function\\file_works\\greeting.txt"
fr=open(file_path)
st=set()
for line in fr:
    line=line.rstrip("\n")
    st.add(line)
print(st)