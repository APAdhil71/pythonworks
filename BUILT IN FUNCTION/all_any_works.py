lst=["housefull","beautiful","peaceful","harmful","thinkful","powerful"]
end_full=[w.endswith("ful")for w in lst]
is_all_ends_ful=all(end_full)
print(is_all_ends_ful)
words=["program","problem","prefect","apple"]
pro_words = [w.startswith("pro") for w in words ]
print(pro_words)
number=15
print(not any([number%i==0 for i in range(2,number)]))