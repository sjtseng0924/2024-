text = "UONCS VAIHG EPAAH IGIRL BIECS TECSW PNITE TIENO IEEFD OWECX TRSRX STTAR TLODY FSOVN EOECO HENIO DAARQ NAELA FSGNO PTE"
text = text.replace(" ", "")
L = len(text)
for i in range(1, L+1):
    if(L%int(i) == 0):
        print("For", i, "x", int(L/i) ,"rectangle, the average of the difference is ", end='')
        vowel = L/i*0.4
        freq = [0] * i
        diff = 0.0
        for j in range(L):
            if(text[j] == "A" or text[j] == "E" or text[j] == "I" or text[j] == "O" or text[j] == "U"):
                freq[j%i] += 1
        for j in range(i):
            diff += abs(freq[j]-vowel)
        kpoo90=print(round(diff, 2)/i)