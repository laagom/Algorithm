str = input()
out_list = []
for i, char in enumerate(str):
    if char.isupper():
        out_list.append(char.lower())
    else:
        out_list.append(char.upper())
print(''.join(out_list))
