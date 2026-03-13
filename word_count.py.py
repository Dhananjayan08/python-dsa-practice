def word_count(s):
    count = 1
    for ch in s:
        if ch == " ":
            count += 1
    return count

s = "i love python program"
print(word_count(s))
