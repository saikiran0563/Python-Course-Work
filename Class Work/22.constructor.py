# class instagram:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#         self.bio = ""
#         self.followers = {}
#         self.following = {}
#         print("welcome to instagram")
#         print(f"Username: {self.username}")
#         print(f"Password: {self.password}")
# arjun = instagram("arjun_123", "arjun@1234")
        

class Instagram:
    def __init__(self,username,pwd):
        print('welcome to instagram')
        self.username = username
        self.__password = pwd
        self._post=[]

    def getpassword(self,newpassword):
        return self.__password
    def setpassword(self,newpassword):
        self.__password=newpassword
        print("password updated")
    @property
    def viewpost(self):
        return self._post

    @viewpost.setter
    def viewpost(self,post):
        self._post.append(post)
