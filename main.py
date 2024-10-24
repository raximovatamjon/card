# lis = {
#     "farhod va shirin": "Alisher Navoiy",
#     "boburnoma": "Zahriddin Muhammad Bobur",
#     "gamlet": "Uilyam Shekspir",
#     "manqurt": "Chingiz Aymatov",
#     "temir xotin": " Hamid Olimjon",
#     "sohib quron": " Abdulla Qodiriy",
# }
# a = input("asar nomini kiriting :")
# print(lis[a])

# lis2 = ["olma", "anor", "o'rik"]

# a=lis2.reverse()
# for i in lis2:
#     print(i[::-1])

# a = input("ismingiz ")
# b = int(input("age "))
# phone =int(input("phone number"))

# lis=[]

# lis.append(a)
# lis.append(b)
# lis.append(phone)

# print(lis)


# nech = int(input("nechta user qo'shmoqchisiz "))  # 2
# lis = []
# c = 0

# while (nech):
#     a = input("ismingiz ")
#     b = int(input("age "))
#     phone = int(input("phone number"))

#     lis.append(a)
#     lis.append(b)
#     lis.append(phone)
#     c+=1
#     if nech == c:
#       break


# print(lis)


# # Matn
# text = "assalomu alleykum"

# # Har bir so'zni bo'shliq bilan ajratish
# words = text.split()

# # Har bir so'zdan qismalarni olish
# subwords = set()  # Takrorlanmas qismlarni saqlash uchun set

# for word in words:
#     for i in range(len(word)):
#         for j in range(i + 1, len(word) + 1):
#             subwords.add(word[i:j])  # So'zning qismni qo'shish

# # Natijalarni chiqarish
# print("Yaralgan so'zlar:")
# for subword in subwords:
#     print(subword)

# print(f"\nJami so'zlar soni: {len(subwords)}")


son = input("son kirit ")

cards={
    "1":[ "9860","xumo","0101",],
    "2":[ "8600","uzcard","0303"],
    "3":[ "1701", "ipak yoli","3300"],
    "4":[ "4200","ipak yoli","1111"],
}

if son[:4:] == cards["1"]:
    print("visa")   
elif son[:2:] == cards["v"]:
    print("visa")
elif son[:4:] == cards["u"]:
    print("uzcard")
elif son[:4:] == cards["i"]:
    print("ipak yo'li")
else:
    print("uzcard")

# a = input("harf kiriting ")

# print(a.upper())

