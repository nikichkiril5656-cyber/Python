import password_generator

print(password_generator.generate_password(45))
print(password_generator.generate_unique_passwords(10))
password="12ythIPo()74$"
print(password_generator.check_password_strength(password))