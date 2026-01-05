"""
def is_anagram(word1,word2):
    ch_count_in_w1=word1.count(ch)
    ch_count_in_w2=word2.count(ch)
    if ch_count_in_w1!=ch_count_in_w2 and (len(word1)==len(word2)):
        is_anagram_word=False
    break
    return is_anagram_word
print(is_anagram_sol("cat","act"))
print(is_anagram_sol)("son","nos")
"""



def is_anagram_sol(word1,word2):
    is_anagram_word=True
    if len(word1)!=len(word2):
        for ch in word1:
            ch_count_in_w1 = word1.count(ch)
            ch_count_in_w2= word2.count(ch)
            if ch_count_in_w1!=ch_count_in_w2:
                is_anagram_word=False
                break
        return is_anagram_word
    print(is_anagram_word("cat","act"))