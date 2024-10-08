import random
import time

# Game setup at the beginning
battery_level = 100
health = 100
inventory = []
power_cells_collected = 0

# Defining city zones and items
city_zones = {
    "Uptown": ["power cell", "battery pack", "repair kit"],
    "Downtown": ["power cell", "short circuit", "battery pack"],
    "Industrial": ["power cell", "short circuit", "power cell"],
    "Park": ["short circuit", "battery pack", "power cell"],
    "Residential": ["battery pack", "power cell", "short circuit"]
}

# Defining core game functions to move to different zones, collect items
def move_to_zone(zone):
    global battery_level
    if battery_level <= 0:
        print("Battery depleted! Game over.")
        return "Game Over"
    
    print(f"\nExploring {zone}...")
    battery_level -= 5  # Moving costs battery so subtract 5 from initial 
    item = random.choice(city_zones[zone]) #randomly selects an item from a list of possible items associated with the current zone
    print(f"You found a {item} in {zone}.")
    return item

def collect_items(item): #defining collect_items function and "item" is a parameter colllected by the player
    global power_cells_collected  #keeps track of the number of power cells collected in the entire game
    if item == "power cell":
        inventory.append(item)  #power cell is added to the inventory and power_cells_collected counter is incremented by 1
        power_cells_collected += 1
        print("Power cell collected!")
    elif item == "battery pack":
        charge_battery(15)  #charges battery by 15 units
    elif item == "repair kit":  #repair kit is added to the inventory if it satisifes this condition
        inventory.append("repair kit")
        print("Repair kit collected!")
    elif item == "short circuit":
        encounter_hazard()  #the encounter_hazard function is called to trigger a hazard in the game.

def charge_battery(amount): #defining charge_battery function, "amount" is a parameter which is an input from collecting battery packs, and such
    global battery_level #keeps track of battery in the entire game
    battery_level = min(battery_level + amount, 100) #calculates the new battery level by adding the amount to the current battery_level and min takes the minimum value between the calculated new battery level and 100
    print(f"Battery recharged by {amount}%. Current battery: {battery_level}%")

def drain_battery(amount): # the function takes an amount as input and updates the global battery_level by subtracting the amount
    global battery_level
    battery_level -= amount #subtracts the amount from the current battery_level
    print(f"Battery drained by {amount}%. Current battery: {battery_level}%")


def time_challenge(zone, time_limit=10): #the function takes 2 arguments, the zone and default time limit of 10 seconds
    print(f"Time-based challenge! You have {time_limit} seconds to reach the {zone}.")
    start_time = time.time() #records the current time in seconds
    
    #player reaching the zone
    player_input = input(f"Type 'go' to reach the {zone}: ").strip().lower() #asks the player to say "go" to reach the zone. 
    #checks if the player entered "go" and if the elapsed time  is less than or equal to the time_limit.
    if player_input == "go" and (time.time() - start_time) <= time_limit:
        print("Challenge completed in time!")
        charge_battery(10)  # Reward for completing on time
    else:
        print("Time ran out!")
        drain_battery(10)  # Penalty for failing to complete on time


def encounter_hazard():
    global health
    print("You encountered a hazard!")
    health -= 20
    print(f"Health reduced by 20%. Current health: {health}%")
    
    if health <= 0:
        print("Robot health depleted. Game over!")
        return True  # Indicate game over
    return False


def repair_robot():
    global battery_level, health
    if health < 50:
        if "repair kit" in inventory: #if available, it's used to restore health to 100%.
            inventory.remove("repair kit")
            health = 100
            print("Robot repaired to full health using repair kit.")
        elif battery_level >= 20: #20% available, costs 20% to restore health
            battery_level -= 20 #if not available, not able to restore health 
            health = 100
            print("Robot repaired to full health at the cost of 20% battery.")
        else:
            print("Not enough battery or repair kit to repair!")
    else:
        print("Health is sufficient; no repair needed.") #if health >50%, no need to restore health

def display_status():
    print(f"\nBattery Level: {battery_level}%")
    print(f"Health: {health}%")
    print(f"Inventory: {inventory}")
    print(f"Power Cells Collected: {power_cells_collected}")
#Prints the current status of the robot, including battery level, health, inventory, and power cells collected.

def main_game():
    global battery_level, power_cells_collected

    print("Welcome to the Robot Adventure Game!")
    while battery_level > 0 and power_cells_collected < 5:
        display_status() #provides information about the robot's current state.
        zone = input("\nChoose a zone to explore (Uptown, Downtown, Industrial, Park, Residential): ")
        
        #if an invalid zone is entered, the loop will continue to the next iteration, prompting the user to enter a valid zone again
        if zone not in city_zones:
            print("Invalid zone. Try again.")
            continue
        
        # setting time challenge for specific zones
        if zone == "Downtown":
            time_challenge(zone, time_limit=10)
        
        # Move to selected zone and collect an item
        item = move_to_zone(zone)
        
        # If move_to_zone returned "Game Over", break the loop
        if item == "Game Over":
            break
        
        # show collected item
        collect_items(item)
        
        # Check health and offer repair option if low
        if health < 50:
            repair_choice = input("Health is low. Do you want to repair? (yes/no): ").strip().lower()
            if repair_choice == "yes":
                repair_robot()

    # End game with win/lose result
    if power_cells_collected >= 5:
        print("\nCongratulations! You've collected all power cells and won the game!")
    elif battery_level <= 0:
        print("\nOut of battery! Game over.")
    elif health <= 0:
        print("\nRobot is out of health. Game over.")

main_game()
