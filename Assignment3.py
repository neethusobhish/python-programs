

text=input("Enter a string ")
unique= True

for i in range(len(text)):
    for j in range(i+1, len(text)):
        if text[i]==text[j]:
            unique=False
            break
        if not unique:
            break
if unique:
    print("True")
else:
    print("False")