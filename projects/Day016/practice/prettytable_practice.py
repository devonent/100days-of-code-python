import prettytable

my_table = prettytable.PrettyTable()

my_table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'])
my_table.add_column('Type', ['Electric', 'Water', 'Fire'])
my_table.align = "l"

print(my_table)
