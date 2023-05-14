import re


def generate_grammar(regex):
  """
  Generates a regular grammar from the given regular expression.

  Args:
    regex: The regular expression to generate a grammar from.

  Returns:
    The generated regular grammar.
  """

  # Split the regular expression into tokens.
  tokens = re.split(r"[\s\|\?]", regex)

  # Create a dictionary to store the grammar rules.
  grammar = {}

  # Iterate over the tokens.
  for token in tokens:
    # If the token is a non-terminal, add a production rule to the grammar.
    if token[0].isupper():
      grammar[token] = [token]
    # If the token is a terminal, add a production rule to the grammar that produces the token.
    else:
      grammar[token] = [token]

  # Return the generated regular grammar.
  return grammar


def main():
  """
  The main function.
  """

  # Get the regular expression from the user.
  regex = input("Enter a regular expression: ")

  # Generate the regular grammar from the regular expression.
  grammar = generate_grammar(regex)

  # Print the regular grammar.
  print("The generated regular grammar is:")
  for non_terminal, productions in grammar.items():
    print("{} -> {}".format(non_terminal, " ".join(productions)))


if __name__ == "__main__":
  main()
