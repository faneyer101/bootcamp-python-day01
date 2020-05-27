class Recipe:
    def verif_type(self, name, cooking_lvl, cooking_time, ingredients,
                   recipe_type, description):
        if not isinstance(name, str):
            print("Need name string for recipe")
            quit()
        if not isinstance(cooking_lvl, int) or cooking_lvl not in [1,
                                                                   2, 3, 4, 5]:
            print("Need number lvl > 1 and < 6")
            quit()
        if not isinstance(cooking_time, int) or cooking_time < 0:
            print("Need number time >= 0")
            quit()
        if not isinstance(ingredients, list) or len(ingredients) == 0:
            print("Need list of ingredient")
            quit()
        for ingredients_str in ingredients:
            if not isinstance(ingredients_str, str):
                print("Need str on list ingredient")
                quit()
        if not isinstance(recipe_type, str) or recipe_type not in ['starter',
                                                                   'lunch',
                                                                   'dessert']:
            print("Need type recipe str starter or lunch or dessert")
            quit()
        if not isinstance(description, str):
            print("Need description str")
            quit()

    def __init__(self, name, cooking_lvl, cooking_time, ingredients,
                 recipe_type, description=''):
        self.verif_type(name, cooking_lvl, cooking_time, ingredients,
                        recipe_type, description)
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        if len(self.description) > 0:
            return '%s, %d, %d, %s, %s, %s' % (self.name,
                                               self.cooking_lvl,
                                               self.cooking_time,
                                               self.ingredients,
                                               self.recipe_type,
                                               self.description)
        else:
            return '%s, %d, %d, %s, %s' % (self.name, self.cooking_lvl,
                                           self.cooking_time,
                                           self.ingredients,
                                           self.recipe_type)
