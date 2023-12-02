class TV:
    def __init__(self):
        self.channel = 1       
        self.volumeLevel = 50    
        self.on = False        
    def turnOn(self):
        self.on = True
    def turnOff(self):
        self.on = False
    def getChannel(self):
        return self.channel
    def setChannel(self, channel):
        if self.on and (1 <= channel <= 50): 
            self.channel = channel
    def getVolume(self):
        return self.volumeLevel
    def setVolume(self, volume):
        if self.on and (1 <= volume <= 50):
            self.volumeLevel = volume
print(TV.volume())
print(TV.channel())           
  