user_input = str(input("Enter a Phrase: "))
text = user_input.split()
a = " "
for i in text:
    print(i[0])
    a = a+str(i[0]).upper()
print(a)