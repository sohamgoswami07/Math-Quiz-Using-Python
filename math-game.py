import random
import time

OPERATORS = ["+", "-", "*", "/"]
TOTAL_PROBLEMS = 10
# TIMEOUT = 15 # seconds

def generate_problem():
    operator = random.choice(OPERATORS)

    if operator == "+" or operator == '-':
        left = random.randint(2, 99)
        right = random.randint(2, 99)
        expr = str(left) + " " + operator + " " + str(right)
        answer = eval(expr)
        return expr, answer
    
    elif operator == "*":
        left = random.randint(2, 15)
        right = random.randint(2, 15)
        expr = str(left) + " " + operator + " " + str(right)
        answer = eval(expr)
        return expr, answer
    
    else:
        left = random.randint(2, 100)
        right = random.randint(2, 50)
        # Ensure the division result is a positive integer
        while left % right != 0 or left < right:
            left = random.randint(2, 100)
            right = random.randint(2, 50)

        expr = str(left) + " " + operator + " " + str(right)
        answer = eval(expr)
        return expr, answer

wrong_ans = 0
input("Press enter to start!")
print("----------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem " + str(i + 1) + ": \n" + expr + " = ")
        if guess == str(answer):
            break
        else:
            wrong_ans += 1
            break

end_time = time.time()
total_time = round(end_time - start_time, 2)
right_ans = 10 - wrong_ans

print("----------------------")
print("Nice work! You finished in", total_time, "seconds!")
print("You give total of " + str(right_ans) + " answers right and  " + str(wrong_ans) + " answers wrong.")