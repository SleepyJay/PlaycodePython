
from battleboat.GameBoard import GameBoard

gb = GameBoard()

gb.place_cell(1,1,"M0")
gb.place_cell(2,2,"U1")
gb.place_cell(3,3,"M0")
gb.place_cell(4,4,"H1")
gb.place_cell(5,5,"H2")
gb.place_cell(5,6,"U2")

gb.place_ship(3,10,1,3,0)
gb.place_ship(4,4,7,3,1)
gb.place_ship(5,10,9,3,0)

gb.attack_cell(5,6)
print(gb.get_cell(5,6))

gb.attack_cell(10,1)
gb.attack_cell(9,1)
gb.attack_cell(10,2)
gb.attack_cell(10,3)
gb.attack_cell(4,8)
gb.attack_cell(5,7)

print(gb.to_player_repr(True))
print(gb.to_opponent_repr(True))

print(gb.to_player_repr())
print(gb.to_opponent_repr())