def calculate(input, rules):
    tape = ['L'] + list(input) + ['R']
    
    current_position = 0 
    current_state = 1
    steps = 0
    
    rule_dict = {}
    for rule in rules:
        mark, state, new_mark, new_state, action = rule
        if (mark, state) not in rule_dict:
            rule_dict[(mark, state)] = (new_mark, new_state, action)
    
    while steps < 1000:
        current_mark = tape[current_position]
        current_key = (current_mark, current_state)
        
        if current_key not in rule_dict:
            return False 
        
        new_mark, new_state, action = rule_dict[current_key]
        
        tape[current_position] = new_mark
        current_state = new_state
        
        if action == "RIGHT":
            current_position += 1
        elif action == "LEFT":
            current_position -= 1
        elif action == "ACCEPT":
            return True  
        elif action == "REJECT":
            return False 
        
        steps += 1
    
    return False  


if __name__ == "__main__":
    rules = []

    rules.append(("L", 1, "L", 2, "RIGHT"))
    rules.append(("L", 3, "L", 2, "RIGHT"))

    rules.append(("0", 2, "X", 4, "RIGHT"))
    rules.append(("1", 4, "X", 5, "RIGHT"))
    rules.append(("1", 2, "X", 6, "RIGHT"))
    rules.append(("0", 6, "X", 7, "RIGHT"))

    rules.append(("0", 4, "0", 4, "RIGHT"))
    rules.append(("0", 5, "0", 5, "RIGHT"))
    rules.append(("0", 7, "0", 7, "RIGHT"))
    rules.append(("1", 6, "1", 6, "RIGHT"))
    rules.append(("1", 5, "1", 5, "RIGHT"))
    rules.append(("1", 7, "1", 7, "RIGHT"))

    rules.append(("X", 2, "X", 2, "RIGHT"))
    rules.append(("X", 4, "X", 4, "RIGHT"))
    rules.append(("X", 5, "X", 5, "RIGHT"))
    rules.append(("X", 6, "X", 6, "RIGHT"))
    rules.append(("X", 7, "X", 7, "RIGHT"))

    rules.append(("R", 2, "R", 2, "ACCEPT"))
    rules.append(("R", 4, "R", 4, "REJECT"))
    rules.append(("R", 6, "R", 6, "REJECT"))

    rules.append(("R", 5, "R", 3, "LEFT"))
    rules.append(("R", 7, "R", 3, "LEFT"))
    rules.append(("0", 3, "0", 3, "LEFT"))
    rules.append(("1", 3, "1", 3, "LEFT"))
    rules.append(("X", 3, "X", 3, "LEFT"))

    print(calculate("0", rules)) # False
    print(calculate("00", rules)) # False
    print(calculate("01", rules)) # True
    print(calculate("0110", rules)) # True
    print(calculate("0101", rules)) # True
    print(calculate("1000", rules)) # False
    print(calculate("00110101", rules)) # True
    print(calculate("00111101", rules)) # False


