ciphertext = raw_input()

abc = "abcdefghijklmnopqrstuvwxyz"
abc2 = abc*2
ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ABC2 = ABC*2

for step in range (1, 26):
    message = ""
    for c in ciphertext:
        if c in abc:
            i = abc.find(c) + step
            message += abc2[i]
        elif c in ABC:
            i = ABC.find(c) + step
            message += ABC2[i]
        else:
            message += c
    print message

raw_input()