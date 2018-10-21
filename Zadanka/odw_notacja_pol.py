stack = []
operators = ["+", "-", '/', "*"]
exp1 = "3 3 + 6 /"  # (3 + 3) / 6
exp2 =  "3 3 + 2 * 3 /"  #(2*(3+3)) /3 + 6

def onp_calc(expression):
    for token in expression:
        if token == ' ':
            continue

        if token.isdigit():
            stack.append(token)
        elif token in operators:
            b = stack.pop()
            a = stack.pop()
            row = f"{a} {token} {b}"
            wynik = eval(row)
            stack.append(wynik)
    return stack.pop()

wynik = onp_calc(exp2)
print('Wynik:', wynik)