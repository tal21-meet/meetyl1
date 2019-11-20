import turtle
class Turrtle():
	"""docstring for Turrtle"""

class ball(Turrtle):
	"""docstring for """
	def __init__(self,r,dx,dy):
		Turtle.__init__(self)
		self.penup()
		self.color=color
		self.shapesize=(r/10)
		self.shape("Circle")
	def move(self,screen_width,screen_height):
		current_x=self.xpos()
		new_x=current_x
		current_y=self.ypos()
		new_y=current_y
		right_side_ball=new_x+r
		left_side_ball=new_x-r
		right2_side_ball=new_y+r
		left2_side_ball=new_y-r
		self.goto(new_x,new_y)
		if new_x>screen_width:
			dx=dx*-1
			pass
		elif new_y>screen_height:
			dy=dy*-1
			pass
		pass
screen_width=turtle.getcanvas().winfo_width()/2
screen_height=turtle.getcanvas().winfo_height()/2
while 1==1:
	ball1=(50,10,10)
	ball1.move()
	pass