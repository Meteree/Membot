with open('text.txt', 'r', encoding='utf-8') as f:
    print(f.read())
with open('text.txt', 'w', encoding='utf-8') as f:
    metin = "sen soruyu doğru cevaplarsın."
    f.write(metin)