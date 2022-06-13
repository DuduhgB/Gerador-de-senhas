import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@#$!?"

for_pass = lower_case + upper_case + numbers + symbols

password_size = 12

password = "".join(random.sample(for_pass, password_size))

print("Minha senha é: {password}")
print(f"Minha senha: {password}")