from recipe import Recipe
from book import Book

carbo = Recipe("carbonara", 2, 30, ['lardon', 'pate', 'oeuf'], "lunch",
               "Miam miam")
cookies = Recipe("Cookies", 1, 30, ['oeuf', 'farine', 'chocolat', 'sucre'],
                 "dessert", "Miam miam")
to_print = str(carbo)
print(to_print)

cookbook = Book("Bouquin")
cookbook.add_recipe(carbo)
cookbook.add_recipe(cookies)
cookbook.get_recipe_by_name(cookies.name)
cookbook.get_recipe_by_name(carbo.name)
print(cookbook.creation_date)
print(cookbook.last_update)
