

def check_unique(text):
    for i in range(len(text)):
        for j in range(i+1, len(text)):
            if text[i]==text[j]:
                return False
    return True

sting=input("Enter a string ")

if check_unique(sting):
    print("True")
else:
    print("False")