HISTORY_FILE = 'history.txt'

def show_history():
    with open(HISTORY_FILE, 'r') as f:
        lines = f.readlines()
    if len(lines) == 0:
        print('No History Found!')
    else:
        for line in reversed(lines):
            print(line.strip())

def clear_history():
    with open(HISTORY_FILE, 'w') as f:
        f.write()
        print('History Clearde.')

def save_to_history(equation, result):
    with open(HISTORY_FILE, 'a') as f:
        f.write(f"{equation} = {result}\n")

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print('Invalid input. Use format: number operator number (e.g 8 + 8)')
        return
    
    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    if op == "+":
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            print('Cannot divide by zero')
        result = num1 / num2
    elif op == '//':
        if num2 == 0:
            print('Cannot divide by zero')
        result = num1 // num2
    elif op == '**':
        result = num1 ** num2
    else:
        print('Invalid operator. USE ONLY (+, -, *, /, **, //)')
        return
    
    if int(result) == result:
        result = int(result)
    print('Result: ', result)
    save_to_history(user_input, result)

def main():
    print('---SIMPLE CALCULATOR (type history, clear or exit)')
    while True:
        user_input = input('Enter calculation (+ - * /) or command (history, clear or exit): ').strip().lower()
        if user_input == 'exit':
            print('Bye!')
            break
        elif user_input == 'history':
            show_history()
        elif user_input == 'clear':
            clear_history()
        else:
            calculate(user_input)
main()
