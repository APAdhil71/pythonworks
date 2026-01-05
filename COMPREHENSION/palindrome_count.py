words="radar","level","dam","madam","act","cat","radar","level","madam","malayalam"
#wap genarate count of palindrome_words
result={w:words.count(w)for w in words if w==w [::-1]}
print(result)