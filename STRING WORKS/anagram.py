def is_anagram(word1,word2):
    srt_w1=sorted(word1)
    srt_w2=sorted(word2)
    return srt_w1==srt_w2
print(is_anagram("act","cat"))
print(is_anagram("silent","listen"))