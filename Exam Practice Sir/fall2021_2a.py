class Time:
    def __init__(self,hr,min):
        self.hr=hr
        self.min=min

    def addTime(self,time2):
        total=self.hr*60+time2.hr*60+time2.min+self.min
        hr=total//60
        min=total%60
        return Time(hr,min)
    
    def displayTime(self):
        print(f"Time: {self.hr}hours and {self.min} minutes")

    def timemin(self):
        print(f"Time in minutes: {self.hr*60+self.min} minutes") 

t1=Time(3,45)
t2=Time(5,30)

t1.displayTime()
t1.timemin()

t2.displayTime()
t2.timemin()

newtime=t1.addTime(t2)
newtime.displayTime()
newtime.timemin()
