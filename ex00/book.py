from datetime import datetime
from recipe import Recipe


class Book:
    def __init__(self, name):
        try:
            self.name = str(name)
            self.last_update = datetime.now()
            self.creation_date = datetime.now()
            self.recipes_list = {
                'starter': {},
                'lunch': {},
                'dessert': {}
            }
        except ValueError:
            print("ValueError in Book's constructor")

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        recipe = 0
        if name in self.recipes_list['starter']:
            recipe = self.recipes_list['starter'][name]
        elif name in self.recipes_list['lunch']:
            recipe = self.recipes_list['lunch'][name]
        elif name in self.recipes_list['dessert']:
            recipe = self.recipes_list['dessert'][name]
        if recipe:
            print(str(recipe))
            return recipe
        else:
            print('No {} recipe found'.format(name))

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if recipe_type in self.recipes_list:
            return self.recipes_list[recipe_type].keys()

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if isinstance(recipe, Recipe):
            if recipe.recipe_type in self.recipes_list:
                self.recipes_list[recipe.recipe_type][recipe.name] = recipe
            self.last_update = datetime.now()
        else:
            print("recipe is not a Recipe's instance")
