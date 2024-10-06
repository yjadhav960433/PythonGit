class Computer:

    def __init__(self,name,age):
        self.name= name
        self.age = age
        print("Init calls automaticallt")

    def config(self):
        # print("my","Name","is","Yogesh")
        print(self.name,self.age)


com1 = Computer("Yogesh",21)
com2 = Computer("Harshda",23)

com1.config()
com2.config()