import random


karakterler= ">£#$½{[]}\|!'^^++%&/()=?_-@€€₺₺i¨~æßabcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
sayi = int(input("Şifreniz Kaç Karakterden Oluşsun?"))


password = ""
for i in range(sayi):
    password += random.choice(karakterler)


print("Şifreniz:", password)
