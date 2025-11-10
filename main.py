# 🧠 Basit Sözlük Uygulaması

# 1️⃣ Kelimeleri ve anlamlarını saklıyoruz
meme_dict = {
    "CRINGE": "Garip ya da utandırıcı bir şey",
    "LOL": "Komik bir şeye verilen cevap",
    "ROFL": "Yere yuvarlanarak gülmek",
    "SUS": "Şüpheli veya garip kişi",
    "MİM" : "Bir konu hakkında yapılan komik edit"

}

# 2️⃣ Kullanıcıdan kelimeyi alıyoruz
word = input("Anlamadığınız bir kelime yazın (farketmez, küçük veya büyük harf olabilir): ").upper()

# 3️⃣ Kelimeyi kontrol edip sonucu döndürüyoruz
if word in meme_dict:
    print("Anlamı:", meme_dict[word])
else:
    print("Üzgünüm 😢 Bu kelime sözlükte yok.")
