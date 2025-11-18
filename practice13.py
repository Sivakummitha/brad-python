string="iamsivacharan"
count1=0
count2=0
vowel=['a','e','i','o','u']
for ch in string:
    if ch in vowel:
        count1+=1
    else:
        count2+=1
print(f"vowel count is {count1}")
print(f"consonnt count is {count2}")