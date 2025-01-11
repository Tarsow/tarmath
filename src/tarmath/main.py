def changebase10(num, base):
    final = []
    while(num > base):
        final.append(num % base)
        num = num // base
    final.append(num)
    return "".join(final).lstrip("0")
