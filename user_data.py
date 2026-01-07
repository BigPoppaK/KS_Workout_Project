from datetime import datetime, date

date_format = "%d-%m-%Y"
time_format = "%H:%M"
LOCATIONS = {"1": "Indoor[Home]","2":"Indoor[Gym]","3":"Outdoor"}
MAIN_MUSCLE_GROUPS = {"1": "Chest","2":"Back","3":"Shoulders","4":"Biceps","5":"Triceps","6":"Forearms","7":"Core","8":"Quads","9":"Hamstrings","10":"Glutes","11":"Calves"}
CATEGORIES = {"1":"Weighted","2":"Bodyweight"}
DIFFICULTIES = {"1":"Beginner", "2":"Intermediate","3":"Expert"}

def get_date(prompt,allow_default = False):
    dateString = input(prompt)
    if allow_default and not dateString:
        return datetime.today().strftime(date_format)
    
    try:
        validDate = datetime.strptime(dateString,date_format)
        return validDate.strftime(date_format)
    except ValueError:
        print("Invalid submission. Enter date in DD-MM-YYYY format")
        return get_date(prompt,allow_default)

def getLocation():
    location = input("Select a location:\n1.Indoor[Home]\n2.Indoor[Gym]\n3.Outdoor\n")
    if location in LOCATIONS:
        return LOCATIONS[location]
    
    print("Must select option from location categories (1,2,3)")
    return getLocation

def getDuration():
    startTime = input("Enter start time of workout(24:00 Interval Time):")
    endTime = input("Enter end time of workout(24:00 Interval Time):")

    try:
        startRaw = datetime.strptime(startTime,time_format).time()
        endRaw = datetime.strptime(endTime,time_format).time()

        start = datetime.combine(date.today(),startRaw)
        end = datetime.combine(date.today(),endRaw)

        if end < start:
            end = end.replace(day=end.day + 1)
        
        duration = end-start
        return duration
    
    except ValueError:
        print("Time must be formatted in HH:MM format. AM Hours: 00-11; PM Hours:(13-23).")
        return getDuration()
    
def getReps(exercise):
    reps = input(f"How many reps of {exercise} did you complete: ")
    return reps

def getExerciseName():
    exercise = input("What is the name of the exercise?")
    return exercise

def getTargetMuscles():
    targetGroups = set()
    musclesFound = False
    while not musclesFound:
        muscleGroup = input("Select the targeted muscle group from list: \n1.Chest \n2.Back \n3.Shoulders \n4.Biceps \n5.Triceps \n6.Forearms \n7.Core \n8.Quads \n9.Hamstrings \n10.Glutes \n11.Calves\n")
        if muscleGroup in MAIN_MUSCLE_GROUPS:
            targetGroups.add(MAIN_MUSCLE_GROUPS[muscleGroup])
            choice = input("Are there any more muscle groups to add? \n1.Yes\n2. No\n")
            if choice == "2":
                musclesFound = True
        else:
            print("Invalid selection. Please choose from the designated muscle groups.")

    return targetGroups

def getCategory():
    category = input("Select the type of workout:\n1. Weighted\n2. Bodyweight\n")
    if category in CATEGORIES:
        return CATEGORIES[category]
    
    print("Invalid input. Please choose an option from the listed categories (1,2).")
    return getCategory()

def getDifficulty():
    difficulty = input("Select the exercise difficulty:\n1. Beginner\n2. Intermediate\n3. Expert\n")
    if difficulty in DIFFICULTIES:
        return DIFFICULTIES[difficulty]
    
    print("Invalid selection. Please choose from the designated difficulties (1-3).")
    return getDifficulty()

def getLink():
    link = input("Submit a link of an example for the exercise: ")
    return link


