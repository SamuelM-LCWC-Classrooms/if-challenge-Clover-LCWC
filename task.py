def task_1(numbers, N):
    for _ in range(N):
        for i in range(len(numbers)):
            if numbers[i] % 2 == 0: 
                numbers[i] -= 2
            else:
                numbers[i] += 2
    return numbers

def task_2(N):
    msg = ["The most"]

    if N % 1 == 0:
        msg.append("brilliant")
    if N % 2 == 0:
        msg.append("exciting")
    if N % 3 == 0:
        msg.append("fantastic")
    if N % 4 == 0:
        msg.append("virtuous")
    if N % 5 == 0:
        msg.append("heart-warming")
    if N % 6 == 0:
        msg.append("tear-jerking")
    if N % 7 == 0:
        msg.append("beautiful")
    if N % 8 == 0:
        msg.append("exhilarating")
    if N % 9 == 0:
        msg.append("emotional")
    if N % 10 == 0:
        msg.append("inspiring")

    # Join the list into a single string with spaces
    msg = " ".join(msg) + f" number is {N}!"
    
    return msg




def task_3(calc):
    num1, operator, num2 = calc.split()
    num1, num2 = int(num1), int(num2)
    
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '//':
        return num1 // num2 if num2 != 0 else -1
    
    return None
print(task_2(4))