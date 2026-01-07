import pandas as pd
import csv
from datetime import datetime
from user_data import *
## LogCSV - Class that functions as our collection of workouts we've done over time.
class LogCSV:
    CSV_FILE = "workout_log.csv"
    COLUMNS = ["session_id","date","location","duration","excercise_id","reps"]
    dateFormat = "%d-%m-%Y"

    @classmethod
    def initialize(target):
        try:
            pd.read_csv(target.CSV_FILE)
        except FileNotFoundError:
            dataf = pd.DataFrame(columns=target.COLUMNS)
            dataf.to_csv(target.CSV_FILE,index= False)
    
    @classmethod
    def addEntry(target,date,location,duration,exercise_id,reps):
        dataf = pd.read_csv(target.CSV_FILE)
        if dataf.empty:
            session_id = 1
        else:
            last_entry = dataf.iloc[-1]
            if date == last_entry["date"] and location == last_entry["location"] and duration == last_entry["duration"]:
                session_id = dataf["session_id"].max()
            else:
                session_id = dataf["session_id"].max()+1



        new_entry = {"session_id":session_id,"date":date,"location":location,"duration":duration,"exercise_id":exercise_id,"reps":reps}
        with open(target.CSV_FILE,"a",newline="") as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=target.COLUMNS)
            writer.writerow(new_entry)
        print("New Entry added!")

    @classmethod
    def getSession(target, date):
        dataf = pd.read_csv(target.CSV_FILE)
        dataf["date"] = pd.to_datetime(dataf["date"],format= LogCSV.dateFormat)
        date = datetime.strptime(date,LogCSV.dateFormat)

        mask = (dataf["date"] == date)
        filteredData = dataf.loc[mask]

        if filteredData.empty:
            print("No sessions took place")
        
        else:
            print(f"List of workout sessions that took place on {date}:\n")
            print(filteredData.to_string(index = False))
## WorkoutCSV - Class to define master table for excercises. Here we store all of our excercises along with general information about them.
class WorkoutCSV:
    CSV_FILE = "workout_db.csv"
    COLUMNS = ["exercise_id","exercise_name", "target_muscle", "category", "difficulty", "example_link"]

    @classmethod
    def initialize(target):
        try:
            pd.read_csv(target.CSV_FILE)
        except FileNotFoundError:
            dataf = pd.DataFrame(columns=target.COLUMNS)
            dataf.to_csv(target.CSV_FILE,index=False)

    @classmethod
    def addEntry(target,exercise_name,target_muscle,category,difficulty,example_link):
        dataf = pd.read_csv(target.CSV_FILE)
        if not dataf.empty:
            exercise_id = dataf["exercise_id"].max()+1
        else:
            exercise_id = 1
        
        new_entry = {"exercise_id":exercise_id,"exercise_name":exercise_name,"target_muscle":target_muscle,"category":category,"difficulty":difficulty,"example_link":example_link}
        with open(target.CSV_FILE,"a",newline="") as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=target.COLUMNS)
            writer.writerow(new_entry)
        print("New Workout Added!")

    @classmethod
    def get_exercise_id(target, exercise_name):
        dataf = pd.read_csv(target.CSV_FILE)
        match = dataf.loc[dataf["exercise_name"] == exercise_name, "exercise_id"]
        if match.empty:
            raise ValueError("Exercise is not in the database. Please add!")
        return match.iloc[0]

"""
class PersonalBestsCSV:
    CSV_FILE = "personal_best.csv"
    COLUMNS = ["exercise_id","max_reps","max_weight"]

    @classmethod
    def initialize(target):
        try:
            pd.read_csv(target.CSV_FILE)
        except FileNotFoundError:
            dataf = pd.DataFrame(columns=target.COLUMNS)
            dataf.to_csv(target.CSV_FILE,index=False)

    @classmethod
    def addEntry(target,exercise_id,max_reps,max_weight):
        new_entry = {"exercise_id":exercise_id,"max_reps":max_reps,"max weight":max_weight}
        with open(target.CSV_FILE,"a",newline="") as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=target.COLUMNS)
            writer.writerow(new_entry)
        print("New PB added!")
"""
    

def addWorkoutLog():
    LogCSV.initialize()
    WorkoutCSV.initialize()
    date = get_date("Enter a date for your workout: ")
    location = getLocation()
    duration = getDuration()
    exerciseName = getExerciseName()
    exercise_id = WorkoutCSV.get_exercise_id(exerciseName)
    reps = getReps()
    LogCSV.addEntry(date,location,duration,exercise_id,reps)

def addExercise():
    WorkoutCSV.initialize()
    exercise_name = getExerciseName()
    target_muscles = getTargetMuscles()
    category = getCategory()
    difficulty = getDifficulty()
    example_link = getLink()
    WorkoutCSV.addEntry(exercise_name,target_muscles,category,difficulty,example_link)

def main():
    while True:
        print("Select from the following options:")
        print("1. Add to Workout Log\n")
        print("2. Add to excercise catalog\n")
        print("3. Exit")
        choice = input()
        if choice == "1":
            addWorkoutLog()
        elif choice == "2":
            addExercise()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid selection.")



if __name__ == "__main__":
    main()
