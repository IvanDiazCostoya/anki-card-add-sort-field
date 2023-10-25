import anki
from aqt import mw
import re

col = anki.collection.Collection('C:/Users/clept/AppData/Roaming/Anki2/Iván/collection.anki2')

deck_name = 'Seguridad social test'

search_query = '"deck:' + deck_name + '"'

cards = col.find_cards(search_query)

for card_id in cards:

    # Get the card
    card = col.get_card(card_id)

    # Get the note associated with the card
    note = card.note()

    # bb = 'd (<a href="https://www.boe.es/buscar/act.php?id=BOE-A-2013-12632#a76">artículo 76.0</a>)'
    text = note['Back']

    try:

        #  matches 54.2, 2.b.0, índice
        match = re.search(r'\">[a-záéíóú ]*(\d+\.\d+|índice|\d+\.[a-z]\.\d+|\d+)', text)

        text_sort = match.group(1)

        if text_sort == 'índice':
            text_sort = '9999'

        text_sort = re.sub('(\d+)(\.[a-z])(\.\d+)', '\\1\\3', text_sort)

        if '.' not in text_sort:

            text_sort += '.99'

        if text_sort[-2] == '.':

            text_sort = text_sort[:-1] + '0' + text_sort[-1:]

        note['Sort'] = text_sort

    except:

        note['Sort'] = '9998.99'

    note.flush()

# Synchronize the collection to save changes to the Anki database
col.autosave()