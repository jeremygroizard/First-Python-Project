# Demander le prénom :
print("Hello Python Student")
name=input("what is your name ?")
print(f"Nice to meet you, {name}")

# Demander l'âge :
age=input(("what is your age ? "))
age=int(age)

# Vérifier l'âge et répondre en conséquence :
if age < 18:
    print("You are minor.")
elif age >= 18 and age < 60:
    print("You are adult.")
else:
    print("You are senior.")
