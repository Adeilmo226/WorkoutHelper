sub_musclegroup_dict = {"Chest": "Upper Chest, Middle Chest, Lower Chest", "Legs": "Quads, Hamstrings, Calves",
            "Back": "Upper Back, Middle Back, Lats, Lower Back", "Shoulders": "Front Delts, Lateral Delts, Rear Delts",
            "Biceps": "Long Head - Bicep, Brachialis, Short Head", "Triceps": "Lateral Head, Medial Head, Long Head - Tricep"}

print("Hello! Which muscle group are you interested in working out?")

for key in sub_musclegroup_dict:
    print(key)

muscle_group = str(input("Enter here: "))


muscle_workout_dict = {"Upper Chest": "Incline Dumbbell Press", "Middle Chest": "Flat Bench Dumbbell Press", "Lower Chest": "Dips",
                       "Quads": "Leg extensions", "Hamstrings": "Hamstring Curls", "Calves": "Calf Raises",
                       "Upper Back": "Shrugs", "Middle Back": "T Bar Rows", "Lats": "Dumbbell Rows", "Lower Back": "Back extensions:",
                       "Front Delts": "Front Raises", "Lateral Delts": "Lateral Raises", "Rear Delts": "Rear Delt Flys",
                       "Long Head - Bicep": "Incline Curls", "Brachialis": "Hammer Curls", "Short Head": "Preacher curls",
                       "Lateral Head": "Tricep Extensions", "Medial Head": "Tricep Pushdowns", "Long Head - Tricep": "Katana Extensions"}


for key in sub_musclegroup_dict:
    if key == muscle_group:
        print("Which specific muscle are you interested in?")
        print(sub_musclegroup_dict[key])
        specific_muscle = str(input("Enter here: "))




if specific_muscle not in muscle_workout_dict:
    print("Muscle not recognized. Please check spelling and try again.")
    specific_muscle = str(input("Enter again: "))

for key in muscle_workout_dict:
    if key == specific_muscle:
        print("Ok. Here are some excerises:")
        print("-", muscle_workout_dict[key])
