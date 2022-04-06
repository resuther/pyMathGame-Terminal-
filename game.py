import time
import random
def start():
    print("-------------")
    print("Add the numbers.")
    time.sleep(2)
    print("You have 3 lives.")
    time.sleep(2)
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    time.sleep(1)
    print("GO")
    time.sleep(1)


start()
lives = 3
score = 0

while True:
    num1 = random.randint(0, 500)
    num2 = random.randint(0, 500)
    product = num1 + num2
    print("-------------")
    equu = input(f"""\033[4mAdd {num1} + {num2}
Answer: \033[0m""")
    equ = int(equu)
    if equ == product:
        print("CORRECT")
        score = score + 1
    else:
        lives = lives - 1
        print("WRONG")
        if lives == 0:
            break
        if lives != 0:
            print("-------------")
            print(f"Lives: {lives}")

print("=============")
print(f"Score: {score}")
