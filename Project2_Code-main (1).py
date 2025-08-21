from microbit import *
import radio
import robotbit_library as r

"""
Project 2 Code

By Andrew, Yin, Austin, and Alix

Team 05

This program uses a wavefront algorithm to traverse through a maze.
"""

# Define Ports for the bank of high current output
M1A = 0x1
M1B = 0x2
M2A = 0x3
M2B = 0x4

chnl = 5   #define channel to your team number


# Global variables - grid world dimensions
X_SIZE = 10
Y_SIZE = 5

r.setup()

radio.config(channel=chnl)
radio.on()

# Global Variables
executing = False
s = radio.receive()
map = [[0,0,0,0,0],
        [0,1,99,1,0],
        [1,1,0,1,0],
        [0,0,0,1,0],
        [1,1,0,1,0],
        [0,0,0,1,0],
        [0,1,1,0,0],
        [0,1,2,0,1],
        [0,1,1,0,0],
        [0,0,0,0,0]]

# Movement Function Definitions
def Drive_Forward(grid_squares):
    
    # Motor Ratio (The percentage of the right motor's power that the left motor recieves)
    # Increasing will pull the robot to the left
    ratio = 1.05    # Default = 1.05
    
    # Controls how far the robot drives
    t = 0
    t_max = grid_squares * 70    # Default = 70

    # Drive Forward (Default power = 75)
    while t < t_max:
        r.motor(M2B, -75) # Right wheel
        r.motor(M1A, ratio * 75) # Left wheel
        t += 1

    # Controls how long the braking is
    n = 75     # Default = 75

    # Slowly bring the robot to a stop
    while n > 5 :
        r.motor(M2B, -n) # Right wheel
        r.motor(M1A, ratio * n) # Left wheel
        n -= 2.5

    # Stop the robot's motors entirely
    r.motor(M2B, 0)
    r.motor(M1A, 0)

    return

def TurnRight():
    # Motor Ratio (The percentage of the right motor's power that the left motor recieves)
    ratio = 1.0    # Default = 1.0
    
    # Controls how long the turn is
    t = 0
    t_max = 63   # Default = 63

    # Turn the robot (Default power = 35)
    while t < t_max:
        r.motor(M2B, -35) # Right wheel
        r.motor(M1A, ratio * -35) # Left wheel
        t += 1
    
    # Stop Motors
    r.motor(M2B, 0)
    r.motor(M1A, 0)

    return

def TurnLeft():
    # Motor Ratio (The percentage of the right motor's power that the left motor recieves)
    ratio = 1.0    # Default = 1.0
    
    # Controls how long the turn is
    t = 0
    t_max = 61   # Default = 61

    # Turn the robot (Default power = 35)
    while t < t_max:
        r.motor(M2B, 35) # Right wheel
        r.motor(M1A, ratio * 35) # Left wheel
        t += 1
    
    # Stop Motors
    r.motor(M2B, 0)
    r.motor(M1A, 0)

    return

def print_wavefront_map(map):
    """Print the wavefront map to console"""
    
    for row in map:
        print(row)
    print()
def wavefront_search(map):
    """Wavefront algorithm to find most efficient path to goal"""
    goal_x, goal_y = 0, 0
    found_wave = True
    current_wave = 2


    

    while found_wave:
        found_wave = False
        for y in range(Y_SIZE):
            for x in range(X_SIZE):
                if map[x][y] == current_wave:
                    found_wave = True
                    goal_x = x
                    goal_y = y

                    if goal_x > 0 and map[goal_x-1][goal_y] == 0:
                        map[goal_x-1][goal_y] = current_wave + 1
                    if goal_x < (X_SIZE - 1) and map[goal_x+1][goal_y] == 0:
                        map[goal_x+1][goal_y] = current_wave + 1
                    if goal_y > 0 and map[goal_x][goal_y-1] == 0:
                        map[goal_x][goal_y-1] = current_wave + 1
                    if goal_y < (Y_SIZE - 1) and map[goal_x][goal_y+1] == 0:
                        map[goal_x][goal_y+1] = current_wave + 1

        current_wave += 1
        
        #time.sleep(0.5)
    print_wavefront_map(map)

def navigate_to_goal(map,prefer_left=True):
    """Follow most efficient path to goal and update map as robot moves"""
    
    robot_x, robot_y = 0, 0
    for x in range(X_SIZE):
        for y in range(Y_SIZE):
            if map[x][y] == 99:
                robot_x, robot_y = x, y
                break

    current_x = robot_x
    current_y = robot_y
    current_facing = 0  # Start facing North (0=North, 1=East, 2=South, 3=West)
    current_low = 99

    while current_low > 2:
        current_low = 99
        
        next_x = current_x
        next_y = current_y

        # Check all directions
        if current_x > 0:
            west_val = map[current_x-1][current_y]
            if isinstance(west_val, int) and west_val < current_low and west_val != 1:
                current_low = west_val
                next_direction = 3
                next_x = current_x-1
                next_y = current_y
                

        if current_x < (X_SIZE-1):
            east_val = map[current_x+1][current_y]
            if isinstance(east_val, int) and east_val < current_low and east_val != 1:
                current_low = east_val
                next_direction = 1
                next_x = current_x+1
                next_y = current_y

        if current_y > 0:
            south_val = map[current_x][current_y-1]
            if isinstance(south_val, int) and south_val < current_low and south_val != 1:
                current_low = south_val
                next_direction = 2
                next_x = current_x
                next_y = current_y-1

        if current_y < (Y_SIZE-1):
            north_val = map[current_x][current_y+1]
            if isinstance(north_val, int) and north_val < current_low and north_val != 1:
                current_low = north_val
                next_direction = 0
                next_x = current_x
                next_y = current_y+1

        # Update position and map
        if current_x != robot_x or current_y != robot_y:
            map[current_x][current_y] = "120"
        current_x = next_x
        current_y = next_y

        #adjust_direction_and_move(current_facing, next_direction)

        


        
        print_wavefront_map(map)
    
        

def go_to_goal(map):
   
    current_x = -1
    current_y = -1
    
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == 2:
                current_x,current_y = x,y
    turn_right = 0
    initial_index = 0
    
    if current_x == -1 or current_y == -1:
        print("no start found")
        return False
    
    
    
    while (map[current_y][current_x] != 99):
        #east, west, north, south
        directions = ((0,-1),(1,0),(0,1),(-1,0))
        direction_strings = ["North","East","South","West"]
        
        for final_index in range(len(directions)):
            dx,dy = directions[final_index]
            new_x = dx + current_x
            new_y = dy + current_y
            if 0 <= new_y < len(map) and 0 <= new_x < len(map[0]) and map[new_y][new_x] not in [0,1,2] and (map[new_y][new_x] == "120" or map[new_y][new_x] == 99):
                if map[current_y][current_x] == 2:
                    map[current_y][current_x] = "S"
 
                else:
                    map[current_y][current_x] = "130"
          
                turn_diff = (final_index - initial_index) % 4
                if turn_diff == 0:
                    print("no turn")
                    Drive_Forward(1)
                    print("move forward")
                    sleep(500)
                elif turn_diff == 1 or turn_diff == -3:
                    print("Turn Right Once")
                    TurnRight()
                    sleep(500)
                    Drive_Forward(1)
                    sleep(500)
                elif turn_diff == 2 or turn_diff == -2:
                    print("Turn Right Twice")
                    TurnRight()
                    sleep(500)
                    TurnRight()
                    sleep(500)
                    Drive_Forward(1)
                    sleep(500)
                elif turn_diff == -1 or turn_diff == 3:
                    print("Turn Left Once")
                    TurnLeft()
                    sleep(500)
                    Drive_Forward(1)
                    sleep(500)
                
                initial_index = final_index

                print("pointer =",direction_strings[final_index])    
                
                current_x,current_y = new_x,new_y
                print_wavefront_map(map)
                
            elif 0 <= new_y < len(map) and 0 <= new_x < len(map[0]) and map[new_y][new_x] not in [0,1,2,"S"] and map[new_y][new_x] == "*":
                    map[current_y][current_x] = "#"
                    current_x, current_y = new_x, new_y
                    print("Goal Reached")
                    return True
        
    return True   
    
# Main Loop
while True:
    
    s = radio.receive()
    display.show(Image.HAPPY)

    # When the go button is pressed, and the program isn't running,
    # then start the program
    if (s == "Go") and (executing == False):
        
        # Start the program
        executing = True
        print("Program Started")
        radio.send("Going")

        """Main execution function"""
        print("Starting Wavefront Search...")
        wavefront_search(map)
        
        navigate_to_goal(map, prefer_left=True)  # Change to False to prefer right turns
        
        go_to_goal(map)

        # When finished, send the return code
        print("Program Completed")
        radio.send("Done")

        continue
        
    elif (s == "Stop"):
        executing = False
        r.motor(M2B, 0)
        r.motor(M1A, 0)
    
    sleep(20)