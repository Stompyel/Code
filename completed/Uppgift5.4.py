#Leta efter det första vita tecknet i en text

# s = input("Skriv en text")
# i = 0    #i används som räknare
# for c in s:
#     if c ==" " or c == "\t":
#         break
#     i = i + 1
# if i < len(s):
#     print(f"Första vita tecken finns på plats nr {i}")
# else:
#     print("inget vitt tecken")

#Leta efter det sissta vita tecknet i en text

text = input("Skriv en text")
index = len(text)    #index används som räknare
for c in reversed(text):
    if c ==" " or c == "\t":
        break
    index = index - 1
if index >=0:
    print(f"Sista vita tecken finns på plats nr {index}")
else:
    print("inget vitt tecken")