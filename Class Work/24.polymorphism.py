class hotstar: 
    def _init_(self,username):
         print(f"hi{username} welcome to the hotstar".center(40,'_'))
    def playvideo(self):
        print("Movie without ads")
        print("Limited access for movies")
        print("Quality is limited")
        print("Only one device login")
        print("No download option")
        print("No live access")
        print("Sound quality reduces")
    def login(self):
         print("login is same")
    def interface(self):
         print("same interface")
    def profile(self):
         print("profile is same")

class premimumuser(hotstar):
     def __init__(self, username):
         print(f"hi {username} welcome to the hotstar".center(40, '_'))

def playvideo(self,username,premimum):
        print("Movie without ads")
        print("Limited access for movies")
        print("Quality is limited")
        print("Only one device login")
        print("No download option")
        print("No live access")
        print("Sound quality reduces")
    

banti=hotstar("banti")
banti.playvideo()
banti.login()



mohan=premimumuser("mohan")
mohan.playvideo()
mohan.login()