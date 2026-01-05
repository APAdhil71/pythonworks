file_path="while_loop\\for_loop\\nested_loop\\functions\\string_works\\list_works\\tuple_works\\set_works\\dictionary_works\\comprehension\\lambda_function\\file_works\\number.txt"
fr=open(file_path,"r")
for line in fr:
    line=line.rstrip("\n")
    print(line[::-1])