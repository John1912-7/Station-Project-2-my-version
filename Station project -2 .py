import random
secret_number = random.randint(1, 1000)

difficulty = input("Choose difficulty: Easy - type 1, Normal - type 2, Hard - type 3: ")

while difficulty != "1" and difficulty != "2" and difficulty != "3":
    print("Wrong choice! Please choose 1, 2, or 3.")
    difficulty = input("Choose difficulty: Easy - type 1, Normal - type 2, Hard - type 3: ")
def get_attempts(difficulty):
    if difficulty == "1":
        return 20
    elif difficulty == "2":
        return 14
    elif difficulty == "3":
        return 7
won = False
attempts = get_attempts(difficulty)
while attempts > 0:
    print(f"Your current attempts = {attempts}")
    guess = int(input("Input number: "))
    attempts -= 1
    if guess == secret_number:
        print("You win 🎉!!!")
        won = True
        break
    else:
        difference = abs(guess - secret_number)
                # Sahara
        if 1 <= difference <= 10:
            if guess < secret_number:
                print("Sahara🔥 (Higher)")
            else: 
                print("Sahara🔥 (Lower)")
                # Very hot
        elif 11 <= difference <= 25:
            if guess < secret_number:
                print("Very hot🔥 (Higher)")
            else: 
                print("Very hot🔥 (Lower)")
                # Hot
        elif 26 <= difference <= 50:
            if guess < secret_number:
                print("Hot 🌡️ (Higher)")
            else: 
                print("Hot 🌡️ (Lower)")
                # Warm
        elif 51 <= difference <= 100:
            if guess < secret_number:
                print("Warm ☀️ (Higher)")
            else: 
                print("Warm ☀️ (Lower)")
                # Cool
        elif 101 <= difference <= 200:
            if guess < secret_number:
                print("Cool 🌤️ (Higher)")
            else: 
                print("Cool 🌤️ (Lower)")     
                # Cold
        elif 201 <= difference <= 350:
            if guess < secret_number:
                print("Cold ❄️ (Higher)")
            else: 
                print("Cold ❄️ (Lower)")  
                # Very cold
        elif 351 <= difference <= 500:
            if guess < secret_number:
                print("Very cold 🥶 (Higher)")
            else: 
                print("Very cold 🥶 (Lower)")
                # Antarctica
        elif 501 <= difference <= 999:
            if guess < secret_number:
                print("Antarctica 🧊 (Higher)")
            else: 
                print("Antarctica 🧊 (Lower)")
if won == False:
    print(f"You lose. Right number was - {secret_number}")