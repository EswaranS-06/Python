def prabhu_expression_evaluator(expr):
    word_to_digit = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }

    operations = {
        'add', 'sub', 'mul', 'rem', 'pow'
    }

    words = expr.strip().split()

    # Step 1: Check for invalid words
    valid_words = set(operations) | set(word_to_digit.keys()) | {'c'}
    for word in words:
        if word not in valid_words and 'c' not in word:
            return "expression evaluation stopped invalid words present"

    # Step 2: Convert operands
    converted = []
    for word in words:
        if 'c' in word:
            parts = word.split('c')
            num = ""
            for p in parts:
                if p not in word_to_digit:
                    return "expression evaluation stopped invalid words present"
                num += word_to_digit[p]
            converted.append(int(num))
        elif word in operations:
            converted.append(word)
        elif word in word_to_digit:
            converted.append(int(word_to_digit[word]))
        else:
            return "expression evaluation stopped invalid words present"

    # Step 3: Evaluate the expression
    try:
        stack = []
        for token in reversed(converted):
            if isinstance(token, int):
                stack.append(token)
            elif token in operations:
                if len(stack) < 2:
                    return "expression is not complete or invalid"
                a = stack.pop()
                b = stack.pop()
                if token == 'add':
                    stack.append(a + b)
                elif token == 'sub':
                    stack.append(a - b)
                elif token == 'mul':
                    stack.append(a * b)
                elif token == 'rem':
                    stack.append(a % b)
                elif token == 'pow':
                    stack.append(a ** b)
        if len(stack) != 1:
            return "expression is not complete or invalid"
        return stack[0]
    except:
        return "expression is not complete or invalid"

expr = input()
print(prabhu_expression_evaluator(expr))
