# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 12:38:21 2022

@author: mekan_myradov
"""

# Gerekli kütüphaneler import et
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random

# Açık ve özel anahtarları oluştur
random_generator = Random.new().read
private_key = RSA.generate(1024, random_generator)
public_key = private_key.publickey()

plain_text = "Basit uygulama."
print("Şifrelenecek cümle:")
print(plain_text)
print("")

# Şifreleme
cipher = PKCS1_OAEP.new(public_key)
encrypted_text = cipher.encrypt(plain_text.encode("utf-8"))
print("Şifrelenmiş hali:")
print(encrypted_text)
print("")

# Şifre Çözme
cipher = PKCS1_OAEP.new(private_key)
decrypted_text = cipher.decrypt(encrypted_text).decode("utf-8")
print("Deşifre edilmiş hali:")
print(decrypted_text)
