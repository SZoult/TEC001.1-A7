class Car:
    def __init__(self, regis_num, max_speed):
        self.regis_num=regis_num
        self.max_speed=max_speed
        self.current_speed=0
        self.travelled_dis=2000
#E1:
    def test(self):
        print(f"The registration number is: {self.regis_num}, current speed is: {self.current_speed}, max speed is: {self.max_speed}, the amount of travelled distance is: {self.travelled_dis}")
#E2:
    def accelerate(self, change):
        self.current_speed+=change
        if self.current_speed>self.max_speed:
            self.current_speed=self.max_speed
        if self.current_speed<0:
            self.current_speed=0
        print(f"Current speed after accelerating is: {self.current_speed}")
#E3:
    def drive(self, time):
        travelled=self.current_speed*time
        self.travelled_dis+=travelled
        print(f"Current travelled distance is: {self.travelled_dis}")
#Test: 
car1=Car("ABC-123", 142)     
car1.test()
car1.accelerate(60)
car1.drive(1.5)



