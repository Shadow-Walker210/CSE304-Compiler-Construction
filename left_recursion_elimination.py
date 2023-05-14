def eliminate_left_recursion(grammar):
    new_grammar = {}
    
    # Helper function to check if a symbol is a non-terminal
    def is_non_terminal(symbol):
        return symbol.isupper()
    
    # Helper function to eliminate left recursion for a given non-terminal symbol
    def eliminate_recursion(symbol):
        new_rules = []
        recursion_rules = []
        
        # Separate the rules into recursion and non-recursion rules
        for rule in grammar[symbol]:
            if rule[0] == symbol:
                recursion_rules.append(rule[1:])
            else:
                new_rules.append(rule)
        
        if not recursion_rules:
            # No left recursion to eliminate
            return grammar[symbol]
        
        new_symbol = symbol + "'"
        
        # Add new rules for the non-recursion part
        for rule in new_rules:
            new_rule = rule + new_symbol
            new_grammar.setdefault(symbol, []).append(new_rule)
        
        # Add new rules for the recursion part
        for rule in recursion_rules:
            if rule:
                new_rule = rule + new_symbol
                new_grammar.setdefault(new_symbol, []).append(new_rule)
            else:
                # Add an epsilon rule for the recursion part
                new_grammar.setdefault(new_symbol, []).append('')
        
        return new_grammar
    
    # Iterate over the non-terminal symbols in the grammar
    for symbol in grammar:
        eliminate_recursion(symbol)
    
    return new_grammar


# Example grammar with left recursion
grammar = {
    'E': ['E+T', 'T'],
    'T': ['T*F', 'F'],
    'F': ['(E)', 'id']
}

# Eliminate left recursion
new_grammar = eliminate_left_recursion(grammar)

# Print the modified grammar without left recursion
for symbol, rules in new_grammar.items():
    print(symbol, ':', ' | '.join(rules))
