stack = []
x = "(2+4*[89-5(78+16)]-6"
for i in x:
    if i =="{" or i=="[" or i=="(":
        stack.append(i)
    elif i =="}":
        if stack[len(stack)-1]=="{":
            stack.pop()
    elif i =="]":
        if stack[len(stack)-1]=="[":
            stack.pop()
    elif i ==")":
        if stack[len(stack)-1]=="(":
            stack.pop()

if len(stack)==0:
    print("balanced")
else:
    print("unbalanced")