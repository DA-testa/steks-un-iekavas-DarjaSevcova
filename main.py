# python3 Darja Ševcova 221RDC039 18.grupa

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_bracket_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i+1))
          

        if next in ")]}":
            if not opening_bracket_stack or not are_matching(opening_bracket_stack[-1].char, next):
                return i+1
            opening_bracket_stack.pop()
      if opening_bracket_stack:
         return opening_bracket_stack[0].position
      else:
        return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)

    main()
