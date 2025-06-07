s = "A man, a plan, a canal: Panama"

l = s.lower()
res = "".join(i for i in l if i.isalnum())

print(res)
