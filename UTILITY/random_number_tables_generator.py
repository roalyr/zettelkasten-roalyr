import random
from pathlib import Path

tables_number = 100
cards_number = 288
path = 'random_number_tables'
header1 = '## Random number picker \n\n## Card № '
header2 = '\n\n### Take a random card\n----\n'
symbol = '▒'
list_init = []

# Make a list of links.
for k in range(tables_number):
	list_init.append(k)
	
# Make enough links for every card.
while len(list_init) < cards_number:
	list_init += list_init
	
# Write tables.
for i in range(tables_number):
	list = list_init.copy() # Re-populate the list.
	random.shuffle(list) # Shuffle list for every new table.
	content = '' # Reset the content of the .md file.
	for j in range(cards_number):
		link = list.pop()
		content += ('[' + symbol + '](' + str(link) + '.md) ')
	filename = str(i)
	Path(path).mkdir(exist_ok=True)
	f = open("./" + path + "/" + filename + '.md', "w")
	f.write(header1 +str(i) + header2 + content); f.close()