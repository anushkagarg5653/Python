def once(num):
    word = ''
    if num == '1':
        word = "One"
    if num == '2':
        word = "Two"
    if num == '3':
        word = "Three"
    if num == '4':
        word = "Four"
    if num == '5':
        word = "Five"
    if num == '6':
        word = "Six"
    if num == '7':
        word = "Seven"
    if num == '8':
        word = "Eight"
    if num == '9':
        word = "Nine"
    word = word.strip()
    return word

def ten(num):
    word = ''
    if num[0] == '1':
        if num[1] == '0':
            word = "Ten"
       
        if num[1] == '1':
            word = "Eleven"
        if num[1] == '2':
            word = "Twelve"
        if num[1] == '3':
            word = "Thirteen"
        if num[1] == '4':
            word = "Fourteen"
        if num[1] == '5':
            word = "Fifteen"
        if num[1] == '6':
            word = "Sixteen"
        if num[1] == '7':
            word = "Seventeen"
        if num[1] == '8':
            word = "Eighteen"
        if num[1] == '9':
            word = "Nineteen"
    else:
        text = once(num[1])
        if num[0] =='2':
            word = "Twenty"
        if num[0] == '3':
            word = "Thirty"
        if num[0] =='4':
            word = "Fourty"
        if num[0] =='5':
            word = "Fifty"
        if num[0] =='6':
            word = "Sixty"
        if num[0] =='7':
            word = "Seventy"
        if num[0] =='8':
            word = "Eighty"
        if num[0] =='9':
            word = "Ninety"
        word = word + " " + text
        return word

def hundred(num):
    word = ''
    text = ten(num[1:])
    if num[0] == '1':
        word = "One"
    if num[0] == '2':
        word = "Two"
    if num[0] == '3':
        word = "Three"
    if num[0] == '4':
        word = "Four"
    if num[0] == '5':
        word = "Five"
    if num[0] == '6':
        word = "Six"
    if num[0] == '7':
        word = "Seven"
    if num[0] == '8':
        word = "Eight"
    if num[0] == '9':
        word = "Nine"
    if num[0] != '0':
        word = word + " Hundred "
    word = word + text
    word = word.strip()
    return word
test = int(input())
if(test >= 0 and test <= 999):
    a = str(test)
    leng = len(a)
    if leng == 1:
        num = once(a)
    if leng == 2:
        num = ten(a)
    if leng == 3:
        num = hundred(a)
    print (num)
else:
    print("not in range")

    