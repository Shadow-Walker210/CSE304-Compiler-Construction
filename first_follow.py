def find_first(productions, non_terminal):
  """
  Finds the first set of the given non-terminal.

  Args:
    productions: A list of productions.
    non_terminal: The non-terminal to find the first set of.

  Returns:
    The first set of the non-terminal.
  """

  first_set = set()

  for production in productions:
    if production[0] == non_terminal:
      for symbol in production[1:]:
        if isinstance(symbol, str):
          first_set.add(symbol)
        else:
          first_set = first_set.union(find_first(productions, symbol))

  if "$" in first_set:
    first_set.remove("$")

  return first_set


def find_follow(productions, non_terminal):
  """
  Finds the follow set of the given non-terminal.

  Args:
    productions: A list of productions.
    non_terminal: The non-terminal to find the follow set of.

  Returns:
    The follow set of the non-terminal.
  """

  follow_set = set()

  for production in productions:
    for i in range(len(production)):
      if production[i] == non_terminal:
        if i == len(production) - 1:
          follow_set = follow_set.union(find_first(productions, productions[0]))
        else:
          follow_set = follow_set.union(find_follow(productions, production[i + 1]))

  return follow_set


def main():
  """
  The main function.
  """

  # Grammar
  productions = [
    ("S", "E"),
    ("E", "T"),
    ("E", "E + T"),
    ("T", "F"),
    ("T", "T * F"),
    ("F", "id"),
  ]

  # First sets
  first_sets = {}
  for non_terminal in productions:
    first_sets[non_terminal] = find_first(productions, non_terminal)

  # Follow sets
  follow_sets = {}
  follow_sets["S"] = "$"
  for non_terminal in productions:
    if non_terminal != "S":
      follow_sets[non_terminal] = find_follow(productions, non_terminal)

  # Print the first and follow sets
  for non_terminal, first_set in first_sets.items():
    print("First set of {}: {}".format(non_terminal, first_set))

  for non_terminal, follow_set in follow_sets.items():
    print("Follow set of {}: {}".format(non_terminal, follow_set))


if __name__ == "__main__":
  main()
