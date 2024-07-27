def lfsr(plaintext):
    ciphertext = ''
    arr = [0, 0, 0, 0, 0, 0, 0, 1]
    rec = []
    for char in plaintext:
        text = ''
        char_bin = format(ord(char), '08b')
        for i in range(8):
            text += str(int(char_bin[i])^arr[i])
        ciphertext+=text
        rec.append(text)
        chk = arr[0]
        for i in range(7):
            arr[i] = arr[i+1]
        arr[7] = 0
        if chk == 1:
            arr[3] ^= 1
            arr[4] ^= 1
            arr[5] ^= 1
            arr[7] ^= 1
    decrypted_text = ''
    arr = [0, 0, 0, 0, 0, 0, 0, 1]
    for char in rec:
        text = ''
        for i in range(8):
            text += str(int(char[i])^arr[i])
        d_char = chr(int(text, 2))
        decrypted_text += d_char
        chk = arr[0]
        for i in range(7):
            arr[i] = arr[i+1]
        arr[7] = 0
        if chk == 1:
            arr[3] ^= 1
            arr[4] ^= 1
            arr[5] ^= 1
            arr[7] ^= 1
    return ciphertext, decrypted_text
plaintext = "ATNYCUWEARESTRIVINGTOBEAGREATUNIVERSITYTHATTRANSCENDSDISCIPLINARYDIVIDESTOSOLVETHEINCREASINGLYCOMPLEXPROBLEMSTHATTHEWORLDFACESWEWILLCONTINUETOBEGUIDEDBYTHEIDEATHATWECANACHIEVESOMETHINGMUCHGREATERTOGETHERTHANWECANINDIVIDUALLYAFTERALLTHATWASTHEIDEATHATLEDTOTHECREATIONOFOURUNIVERSITYINTHEFIRSTPLACE"
encrypted_text, decrypted_text = lfsr(plaintext)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)
