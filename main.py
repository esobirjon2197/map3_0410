# 1-m
royxat = ["hello", "say", "hi", "welcome"]
print(royxat)

t = list(map(lambda el: f"{el[0]}-{len(el)}", royxat))
print(t)


# 2-m
royxat = ["Ali Valiyev", "Bobur Yo'ldoyev", "Stive Jobs", "Bill Gates"]
print(royxat)

natija = list(map(lambda x: x.split()[0] + " " + x.split()[1][0] + ".", royxat))
print(natija)




# 3-m
royxat = ["Ali", "Bobur", "Stive", "Santyago"]
print(royxat)
t = list(map(lambda x: x + str(len(x)), royxat))
print(t)


# 4-m
sozlar = ["HELLo", "saY", "hi", "Welcome"]
print(sozlar)

t = list(map(lambda x: x[:-1] + x[-1].upper(), sozlar))
print(t)
