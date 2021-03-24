def toRoman(num):
    rules = (
        ("M", 1000),
        ("CM", 900),
        ("D",  500),
        ("CD", 400),
        ("C",  100),
        ("XC",  90),
        ("L",   50),
        ("XL",  40),
        ("XXX", 30),
        ("XX",  20),
        ("X",   10),
        ("IX",   9),
        ("V",    5),
        ("IV",   4),
        ("I",    1),
    )
    res = ""
    for key, val in rules:
        while num >= val:
            num -= val
            res += key
    return res

nb = int(input('Enter your number : '))
print(toRoman(nb))