def build_parsing_table(grammar):
    action_table = {}
    goto_table = {}
    state = 0

    for production in grammar:
        lhs = production[0]
        rhs = production[1]

        for i in range(len(rhs)):
            if i == len(rhs) - 1:
                if lhs not in action_table:
                    action_table[lhs] = {}
                action_table[lhs][rhs[i]] = ('reduce', production)
            else:
                state_key = str(state)
                if state_key not in goto_table:
                    goto_table[state_key] = {}
                goto_table[state_key][rhs[i]] = str(state + 1)
                state += 1

    return action_table, goto_table


def parse(input_string, grammar, action_table, goto_table):
    stack = [0]
    input_symbols = input_string.split()
    input_symbols.append('$')
    pointer = 0

    while True:
        current_state = stack[-1]
        current_symbol = input_symbols[pointer]

        if current_state in action_table and current_symbol in action_table[current_state]:
            action, value = action_table[current_state][current_symbol]

            if action == 'shift':
                stack.append(current_symbol)
                stack.append(value)
                pointer += 1
            elif action == 'reduce':
                lhs, rhs = value
                for _ in range(2 * len(rhs)):
                    stack.pop()
                current_state = stack[-1]
                stack.append(lhs)
                stack.append(goto_table[current_state][lhs])
            elif action == 'accept':
                print('Input string is valid.')
                return
        else:
            print('Input string is invalid.')
            return


# Example usage:
grammar = [
    ('E', 'E + T'),
    ('E', 'T'),
    ('T', 'T * F'),
    ('T', 'F'),
    ('F', '( E )'),
    ('F', 'id')
]

action_table, goto_table = build_parsing_table(grammar)
parse('id + id * id', grammar, action_table, goto_table)
