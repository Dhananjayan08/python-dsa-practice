def vowel_count(s):
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count+=1
    return count

s = input("Enter a string: ")
print("Number of vowels: ",vowel_count(s))
