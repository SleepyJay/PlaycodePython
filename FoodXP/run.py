#!/usr/bin/python

from FoodXP import FoodXP
import sys

foodXP = FoodXP(menu)

menu = [
    foodXP.ItemTuple('RootBeer',   50, 25,  30),
    foodXP.ItemTuple('Hamburger', 120, 35,  60),
    foodXP.ItemTuple('Pizza',     240, 40, 100),
    foodXP.ItemTuple('Water',       2, 20,   2),
    foodXP.ItemTuple('Toast',       5, 30,   6),
    foodXP.ItemTuple('Slice',      15, 40,  15),
]

print(foodXP)




