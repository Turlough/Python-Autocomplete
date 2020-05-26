from prompt_toolkit import prompt
from prompt_toolkit.completion import Completer, Completion
from fuzzyfinder import fuzzyfinder

import pandas as pd

# Dataframe from sql query or csv. Csv example shown here
df = pd.read_csv('./customers.csv', header = 0)
lookup = df.Customer
indent = '\n->\t'

print('Try using a part of an expected word')
print('Also try using any letters within expected words, but in the correct sequence, e.g. "oy" should match "company"')
print('The list we are testing with is:')
# Indent first word on list
print(indent, end = '')
print(*lookup, sep = indent)
print()


class FuzzyCompleter(Completer):
    def get_completions(self, document, complete_event):
        word_before_cursor = document.get_word_before_cursor(WORD=True)
        matches = fuzzyfinder(word_before_cursor, lookup)
        for m in matches:
            yield Completion(m, start_position=-len(word_before_cursor))


while (True):

    user_input = prompt('Enter Search Terms\n\t-> ',completer=FuzzyCompleter())
   	# User has pressed enter
    print(user_input)
