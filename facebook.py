class user:
	def __init__(self,name,email,password):
		self.name=name
		self.email=email
		self.password=password
		self.friends_list=[]
		self.posts=[]
	def add_friend(self,email):
		self.friends_list.append(email)
		print(self.name+"has added"+email+"as a friend")
	def removing_friend(self,email):
		friends_list.remove(self.email)
		print(self.name+"has remove"+email+"from the friends")
	def post(self,text):
		self.posts.append(text)
		print(self.name+"has posted:"+text)
	def get_userInfo(self):
		print("Name:"+self.name)
		print("Email:"+self.email)
		print("Password:"+self.password)
		print("posts:"+str(self.posts))
class post():
	def post(self):
		self.posts.append(text)
post1=post()
post1.post("regegeg")
user1=user("Loai","loai17@meet.mit.edu","myhiddenpassword123")
user1.add_friend('nikolkit123@.com')
user1.post("sddfsdfsfsdf")
user1.get_userInfo()