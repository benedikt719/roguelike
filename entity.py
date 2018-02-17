import math


class Entity:
	''' 게임 속의 것들의 특징을 부여해보자'''

	def __init__(self,x,y,char,color,name,blocks=False,fighter = None,ai = None):
		self.x = x
		self.y = y
		self.char = char
		self.color = color
		self.name = name
		self.blocks = blocks
		self.fighter = fighter
		self.ai = ai

		if self.fighter:
			self.fighter.owner = self

		if self.ai:
			self.ai.owner = self

	def move(self,dx,dy):

		self.x += dx
		self.y += dy

	def move_towards(self,target_x,target_y,game_map,entites):
		path = game_map.compute_path(self.x,self.y,target_x,target_y)

		dx = path[0][0] - self.x
		dy = path[0][1] - self.y

		if game_map.walkable[path[0][0],path[0][1] and not get_blocking_entities_at_location,self.x + dx, self.y + dy]:
			self.move(dx,dy)

	def distance_to(self,other):
		dx = other.x - self.x
		dy = other.y - self.y
		return math.sqrt(dx ** 2 + dy ** 2)


def get_blocking_entities_at_location(entities,destination_x,destination_y):

	for entity in entities:
		if entity.blocks and entity.x == destination_x and entity.y == destination_y:
			return entity

	return None 