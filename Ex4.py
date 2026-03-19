from random import randint
class RaceCar:
    def __init__(self,registration_number, max_speed2):
        self.registration_number=registration_number
        self.travelled_distance=0
        self.current_speed=0
        self.max_speed2=max_speed2
    def accel(self, speed_change):
        self.current_speed=self.current_speed+speed_change
        if self.current_speed>self.max_speed2:
            self.current_speed=self.max_speed2
        if self.current_speed<0:
            self.current_speed=0
    def drive(self, hours):
        distance=self.current_speed * hours
        self.travelled_distance+=distance
car_list=[]
for i in range(11):
    plate=f'ABC-{i}'
    random_max_speed=randint(150, 200)
    new_car=RaceCar(plate, random_max_speed)
    car_list.append(new_car)
    print(f'Car registration number is: {new_car.registration_number}, max speed of this car is: {new_car.max_speed2} km') 
    

while max(car.travelled_distance for car in car_list)<10000:
    for car in car_list:
        speed_change=randint(-10, 15)
        car.accel(speed_change)
        car.drive(1)
print(f"{'Registration number':<15} | {'Max speed':<10} | {'Distance travelled':<12}")
print("-" * 50)
for x in car_list:
    print(f"{x.registration_number:<15} | {x.max_speed2:<10} | {x.travelled_distance:<12}")