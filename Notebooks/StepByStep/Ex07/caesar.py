def caesar(msg,N):
    alphabetU = []
    alphabetL = []
    for i in range(65, 65+26):
        alphabetU+=[chr(i)]
    for i in range(65+32, 65+32+26):
        alphabetL+=[chr(i)]

    out=''
    for l in msg:
        if l==' ': 
            c=' '
        else:
            if l.isupper():
                i = alphabetU.index(l)
                c = alphabetU[(i+N)%26]
            else:
                i = alphabetL.index(l)
                c = alphabetL[(i+N)%26]

        out+=c
    return out