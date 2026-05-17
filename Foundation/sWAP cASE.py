def swap_case(s):
    newStr= ""
    for l in s:
        if l.isupper():
            newStr+=l.lower()
        else:
            newStr+=l.upper()
    return newStr

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


