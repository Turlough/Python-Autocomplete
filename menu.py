from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import Completer, Completion
from fuzzyfinder import fuzzyfinder

import pandas as pd

# Dataframe from sql query or csv. For testing, we just synthesize one.
# e.g. SELECT customername FROM customers WHERE status = 'active',
# then select one column 'customername' and convert to list
df = pd.DataFrame({'customername':['Microsoft', 'Apple', 'Google', 'Fartbook', 'Twatter', 'The amazing elastic company', 'The less famous company']})
# But basically all we want is a list. Select the relevant column 'Customer'
customers = df.customername.tolist()

print('Try using a part of an expected word')
print('Also try using any letters within expected words, but in the correct sequence, e.g. "oy" should match "company"')
print('The list we are testing with is:')
print(*customers, sep = '\n')
print()


class FuzzyCompleter(Completer):
    def get_completions(self, document, complete_event):
        word_before_cursor = document.get_word_before_cursor(WORD=True)
        matches = fuzzyfinder(word_before_cursor, customers)
        for m in matches:
            yield Completion(m, start_position=-len(word_before_cursor))


while (True):

    user_input = prompt('<\nEnter Search Terms\n\t-> ',
                    auto_suggest=AutoSuggestFromHistory(),
                    completer=FuzzyCompleter(),
                    )
   	# User has pressed enter
    print(user_input)
