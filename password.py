import string ,random

password_length = int(input("Şifre kaç karakter uzunluğunda olmalı ? "))

characters = string.ascii_letters + string.punctuation + string.digits

password = "".join(random.choice(characters) for a in range(password_length))

print(password)