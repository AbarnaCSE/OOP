class myclass:
    pi =3.141;
    def __privatepath(self):
        print("I'm Inside the class")
    def hello(self):
        print("Private Variable value: ",myclass.pi)
foo = myclass()
foo.hello()
foo.pi    
