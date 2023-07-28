""" ARAP Webots main file """
import robot

def main():
    red = 0
    green = 0
    blue = 0
    range = 0.0
    ground = 0.0
    robot1 = robot.ARAP()
    robot1.init_devices()
    flag1 = True
    flag2 = True
    flag3 = True
    flag4 = True
    flag5 = True
    summary = []
    
    while True:
        robot1.reset_actuator_values()
        range = robot1.get_sensor_input()
        robot1.blink_leds()
        ground = robot1.get_ground_sensor_values()
        red, green, blue = robot1.get_camera_image(5)
        #id = robot1.get_recognised_object()
        #print(red, green, blue) #debug
        #print(ground) #debug
        #if red >= 200 and green >= 200 and blue >= 200:
            #pass
        if flag1 == True:
            if  ground >= 700 and red > 150:
                #print(red, green, blue) #debug
                if red > blue and red > green:
                    print("I see red")
                    flag1 = False
                    summary.append("Red")  
                    print(summary)
                          
        if flag2 == True:
            if blue > 180 and ground >= 690:
                #print(red, green, blue) #debug
                if blue > red and blue > green:
                    print("I see blue")
                    flag2 = False
                    summary.append("blue")
                    print(summary)          
        
        if flag3 == True:
            if ground >= 700 and green > 180:
                #print(red, green, blue) #debug
                if green > red and green > blue:
                    print("I see green")
                    flag3 = False
                    summary.append("green")
                    print(summary)
        
        if flag4 == True:
            if ground >= 300 and ground <= 310 and blue >= 150:
                #print(ground, blue) #debug
                print("I found water")
                flag4 = False
                summary.append("water")
                print(summary)
        
        if flag5 == True:
            if ground >= 300 and ground <= 700 and green >= 150:
                #print(ground, green) #debug
                print("I found food")
                flag5 = False
                summary.append("food")
                print(summary)
           
                   
        if robot1.front_obstacles_detected():
            robot1.move_backward()
            robot1.turn_left()
        
        if robot1.right_obstacles_detected():
            robot1.move_backward()
            robot1.turn_left()
        
        if robot1.left_obstacles_detected():
            robot1.move_backward()
            robot1.turn_right()
        
        else:
            robot1.run_braitenberg()
        robot1.set_actuators()
        robot1.step()

if __name__ == "__main__":
    main()""" ARAP Webots main file """
import robot

def main():
    red = 0
    green = 0
    blue = 0
    range = 0.0
    ground = 0.0
    robot1 = robot.ARAP()
    robot1.init_devices()
    flag1 = True
    flag2 = True
    flag3 = True
    flag4 = True
    flag5 = True
    summary = []
    
    while True:
        robot1.reset_actuator_values()
        range = robot1.get_sensor_input()
        robot1.blink_leds()
        ground = robot1.get_ground_sensor_values()
        red, green, blue = robot1.get_camera_image(5)
        #id = robot1.get_recognised_object()
        #print(red, green, blue) #debug
        #print(ground) #debug
        #if red >= 200 and green >= 200 and blue >= 200:
            #pass
        if flag1 == True:
            if  ground >= 700 and red > 150:
                #print(red, green, blue) #debug
                if red > blue and red > green:
                    print("I see red")
                    flag1 = False
                    summary.append("Red")  
                    print(summary)
                          
        if flag2 == True:
            if blue > 180 and ground >= 690:
                #print(red, green, blue) #debug
                if blue > red and blue > green:
                    print("I see blue")
                    flag2 = False
                    summary.append("blue")
                    print(summary)          
        
        if flag3 == True:
            if ground >= 700 and green > 180:
                #print(red, green, blue) #debug
                if green > red and green > blue:
                    print("I see green")
                    flag3 = False
                    summary.append("green")
                    print(summary)
        
        if flag4 == True:
            if ground >= 300 and ground <= 310 and blue >= 150:
                #print(ground, blue) #debug
                print("I found water")
                flag4 = False
                summary.append("water")
                print(summary)
        
        if flag5 == True:
            if ground >= 300 and ground <= 700 and green >= 150:
                #print(ground, green) #debug
                print("I found food")
                flag5 = False
                summary.append("food")
                print(summary)
           
                   
        if robot1.front_obstacles_detected():
            robot1.move_backward()
            robot1.turn_left()
        
        if robot1.right_obstacles_detected():
            robot1.move_backward()
            robot1.turn_left()
        
        if robot1.left_obstacles_detected():
            robot1.move_backward()
            robot1.turn_right()
        
        else:
            robot1.run_braitenberg()
        robot1.set_actuators()
        robot1.step()

if __name__ == "__main__":
    main()
