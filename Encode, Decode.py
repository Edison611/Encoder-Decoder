import math

def encipher_fence(plaintext,numRails):
    encoded = ""
    for i in range(numRails,0,-1):
        encoded = encoded + plaintext[i-1::numRails]
        #We start off by calculating the final rail first, then to the first rail
        #This allows us to directly encipher the text
    return encoded

def decipher_fence(ciphertext,numRails):
    decoded = ""
    ciphertext = ciphertext[::-1]
    len_text = len(ciphertext)
    #we reverse the cipher text so that it will be easier for us to find the rails in chronological order

    #This loop is used for finding each rail
    rails = []
    numRailsLeft = numRails
    for i in range(numRails):
        var = ciphertext[:int(math.ceil(len(ciphertext)/numRailsLeft))]
        #var is used to find each rail
        ciphertext = ciphertext[int(math.ceil(len(ciphertext)/numRailsLeft)):]
        rails.append(var[::-1])
        numRailsLeft -= 1

    i = 0
    while i < math.ceil(len_text/numRails):
        for rail in rails:
            if i > len(rail)-1:
                break
            decoded = decoded + rail[i]
        i += 1
    return decoded

def decode_text(ciphertext,wordfilename):
    highest = 0
    ans = ""
    f = open(wordfilename, "r")
    f = f.read()
    f = f.split()
    f = set(f)
    for numRails in range(1,11):
        total = 0
        phrase = decipher_fence(ciphertext,numRails)
        phrase = phrase.split()

        #This loop is used to find the number of matching words in the phrase and the file
        for word in phrase:
            for x in f:
                x = x.strip('\n')
                if x == word:
                    total += 1
        if total > highest:
            ans = " ".join(phrase)
            highest = total
    return ans

print(encipher_fence("abcdefghi", 3))
# should print: cfibehadg
print(encipher_fence("This is a test.", 2))
# should print: hsi  etTi sats.
print(encipher_fence("This is a test.", 3))
# should print: iiae.h  ttTss s
print(encipher_fence("Happy birthday to you!", 4))
# should print: pidtopbh ya ty !Hyraou

# deciphering
print(decipher_fence("hsi  etTi sats.",2))
# should print: This is a test.
print(decipher_fence("iiae.h  ttTss s",3))
# should print: This is a test.
print(decipher_fence("pidtopbh ya ty !Hyraou",4))
# should print: Happy birthday to you!

# decoding
print(decode_text(" cr  pvtl eibnxmo  yghu wou rezotqkofjsehad", 'wordlist.txt'))
# should print: the quick brown fox jumps over the lazy dog
print(decode_text("unt S.frynPs aPiosse  Aa'lgn lt noncIniha ", 'wordlist.txt'))
# should print... we'll let you find out!
