class whatsapp_v1:
    def messaging(self):
        print("you can send messages")

    def sharepics(self):
        print("you can share pictures")

class whatsapp_v2(whatsapp_v1):
    def status(self):
        print("you can upload status")
    def videos(self):
        print("you can share videos")

class whatsapp_v3(whatsapp_v2):
    def call(self):
        print("you can do  calls")
    def group(self):
        print("you can create groups")

class community:
    def cloubgroup(self):
        print("you can create cloub groups")

class meta:
    def AI(self):
        print("you can use AI features")

class meta1:
    def AI_images(self):
        print("you can generate images using AI")

class meta2:
    def AI_videos(self):
        print("you can generate videos using AI")

class whatsapp_v4(whatsapp_v3,community,meta):
    def channel(self):
        print("you can create channels to enggage with your followers")

manoj=whatsapp_v1()
print("manog-v1")
manoj.messaging()
manoj.sharepics()

mohan=whatsapp_v2()
print("\n\nmohan-v2")
mohan.messaging()
mohan.sharepics()
mohan.status()
mohan.videos()

banti=whatsapp_v3()
print("\n\nbanti-v3")
banti.messaging()
banti.sharepics()
banti.status()
banti.videos()
banti.call()
banti.group()

kiran=whatsapp_v4()
print("\n\nkiran-v4")
kiran.messaging()
kiran.sharepics()
kiran.status()
kiran.videos()
kiran.call()
kiran.group()
kiran.cloubgroup()
kiran.AI()
kiran.channel()

