#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 22:48:44 2025

@author: moor1367
"""
# List of agent names
agents = ["Jon Snow", "Eddard Stark", "Ramsey Bolton", "Cersei Lannister"]

# Dictionary of cars and their activity data
cars = {
    "spider": {
        "id": 1,
        "name": "Fiat 124 Spider",
        "activities": {
            "oil changes": 2,
            "new transmission" : 1
        }
    },
    "triangle": {
        "id": 2,
        "name": "TR7",
        "activities": {
            "new tires": 4,
            "paint touch up" : 8
        }
    },
    "shamrock": {
        "id": 3,
        "name": "Alfa Romeo Stelvio Quadrifoglio",
        "activities": {
            "import/export waiver": 1,
            "enhancements" : 1,
            "new tires": 2,
            "oil changes": 6
        }
    },
    "marty": {
        "id": 4,
        "name": "DMC-12",
        "activities": {
            "new engine": 1,
            "bodywork incidents" : 2
        }
    },
}

# Minimum number of oil changes before showing a warning
oil_change_warning_min = 5

# Main menu loop to prompt the user for input
def main_menu():
    while True:
        print("\n--- Krannert Specialty Motors ---")
        print("1. View total for an activity (aggregate)")
        print("2. View activity details for a specific car")
        print("3. Exit")

        # Input for the user to choose their option
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            # Aggregate activity lookup
            activity_name = input("Enter an activity: ").strip().lower()
            total = aggregate_activities(cars, activity_name)
            print(f"Total {activity_name}: {total}\n")

        elif choice == "2":
            # Specific car activity lookup
            car_nickname = input("Enter a car nickname: ").strip().lower()
            activity_name = input("Enter an activity: ").strip().lower()
            result = car_activity_lookup(cars, car_nickname, activity_name)
            print(result + "\n")

        elif choice == "3":
            # Exit the program
            print("Exiting program. Goodbye!")
            break

        else:
            # Invalid input handling
            print("Invalid choice. Please enter 1, 2, or 3.")

# Function to calculate total of a given activity across all cars by looping through cars and search nested lists for an activity match.
def aggregate_activities(cars, activity):
    total = 0
    for car in cars:
        car_activities = cars[car]["activities"]
        if activity in car_activities:
            total += car_activities[activity]
    return total

# Function to look up how many times a specific activity was performed on a given car
def car_activity_lookup(cars, car_nickname, activity):
    if car_nickname in cars:  # Check if car exists in dictionary
        car_data = cars[car_nickname]
        car_activities = car_data["activities"]
        agent_id = car_data["id"]
        agent_name = agents[agent_id - 1]  # Convert ID to name
        warning = ""

        # Add warning if oil changes exceed the threshold
        if activity == "oil changes" and car_activities[activity] > oil_change_warning_min:
            warning = "\nWarning: You should probably have the mechanic check this engine."

        # If the activity s found, then the program will print out the appropriate response.
        if activity in car_activities:
            return f"{car_nickname} had {car_activities[activity]} {activity} and the agent is {agent_name}.{warning}"
        else:
            return f"{car_nickname} has no record of {activity}"

    return "Car not found."

# Start the program
main_menu()
