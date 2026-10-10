
def error(string):
    print(string)

def calculate(expression: str):
    print(expression)
    digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."]
    if "(" in expression:
        open_bracket_list = []
        close_bracket_list = []

        count = 0

        for i in expression:
            if i == "(":
                open_bracket_list.append(count)
            count += 1

        count = 0

        for j in expression:
            if j == ")":
                close_bracket_list.append(count)
            count += 1

        bracket_dict = {}

        for i in range(1, len(open_bracket_list) + 1):
            close_index = None
            open_index = open_bracket_list[-i]
            for j in close_bracket_list:
                if j > open_index:
                    close_index = j
                    close_bracket_list.remove(close_index)
                    break
            bracket_dict[open_index] = close_index

        modified_bracket_dict = {}

        for open_bracket_index, close_bracket_index in bracket_dict.items():
            bracket_data = expression[open_bracket_index + 1:close_bracket_index]
            if "(" not in bracket_data:
                modified_bracket_dict[open_bracket_index] = close_bracket_index #it includes index of plain expressions.

        for open_bracket_index, close_bracket_index in modified_bracket_dict.items():
            expression = expression.replace(expression[open_bracket_index:close_bracket_index+1], str(calculate(expression[open_bracket_index+1:close_bracket_index])))
            answer = calculate(expression)
            return answer

    else:
        elements = []
        element = ""
        for i in expression:
            if i in digits:
                if element == "" or element.isnumeric() or i.isdecimal():
                    element = element + i
                else:
                    element = ""
            else:
                elements.append(element)
                element = ""
                element += i
                elements.append(element)
                element = ""
        elements.append(element)
        while len(elements) != 1:
            if "/" in elements or "*" in elements:
                divide_index = 100000000
                multiply_index = 100000000
                if "/" in elements:
                    divide_index = elements.index("/")
                if "*" in elements:
                    multiply_index = elements.index("*")
                if divide_index < multiply_index:
                    operator_index = divide_index
                    ans = float(elements[operator_index-1])/float(elements[operator_index+1])
                    elements.pop(operator_index)
                    elements.insert(operator_index, str(ans))
                    elements.pop(operator_index-1)
                    elements.pop(operator_index)
                elif multiply_index < divide_index:
                    operator_index = multiply_index
                    ans = float(elements[operator_index - 1]) * float(elements[operator_index + 1])
                    elements.pop(operator_index)
                    elements.insert(operator_index, str(ans))
                    elements.pop(operator_index - 1)
                    elements.pop(operator_index)
            elif "+" in elements or "-" in elements:
                add_index = 10000000000
                subtract_index = 100000000
                if "+" in elements:
                    add_index = elements.index("+")
                if "-" in elements:
                    subtract_index = elements.index("-")
                if add_index < subtract_index:
                    operator_index = add_index
                    ans = float(elements[operator_index - 1]) + float(elements[operator_index + 1])
                    elements.pop(operator_index)
                    elements.insert(operator_index, str(ans))
                    elements.pop(operator_index - 1)
                    elements.pop(operator_index)
                elif subtract_index < add_index:
                    operator_index = subtract_index
                    ans = float(elements[operator_index - 1]) - float(elements[operator_index + 1])
                    elements.pop(operator_index)
                    elements.insert(operator_index, str(ans))
                    elements.pop(operator_index - 1)
                    elements.pop(operator_index)
        return elements[0]

