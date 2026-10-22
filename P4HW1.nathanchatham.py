# Nathan Chatham
# 10/22/2026
# use nested loops to validate user inputs 

# create a empty list
valid_grades = []


# get number of scores from user as int
num_of_scores = int(input("How many scores do you want to enter? "))

# make a for loop that runs num_of_score times
for scores in range(1,num_of_scores + 1):
   input_score = float(input(f"Enter score #[scores]: ")) 

   # while loop that traps the user while input_score is invalid
   while input_score < 0 or input_score > 100:
      print("Invalid grade entered!")
      print(" Score should be between 0 and 100")
      # Ask them for a new value for input_score
      input_score = float(input(f"Enter score #[scores] again:"))
 
    # Add input_score to the valid_grades
      valid_grades.append(input_score)

# All loops have broken
print(valid_grades)

