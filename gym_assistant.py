#                    ~ GYM ASSISTANT ~
# - Made by : Prithviraj Shaw , b.tech fy material science
#                 ES102 final project




# I came to know about the pygame module for playing music from CodeWithHarry
# & the lines to play it from geek for geeks pygame to play music
# I learnt use of f_strings from CodeWithHarry
# I learnt time module from CodeWithHarry


from pygame import mixer
import time
import webbrowser

# I came to know about the pygame module for playing music from CodeWithHarry
# & the lines to play it from geek for geeks pygame to play music
# I learnt use of f_strings from CodeWithHarry
# I learnt time module from CodeWithHarry
weight = 90

# put the person's weight here in the nearest 10's  ---- I have tried to keep the code customizable
print("\t\t\t\t\t good morning\n"
      "\t\t\t\tEnter week of the day as:\n"
      "\t\t\t\tmon tue wed thu fri sat sun")

input_day = input()
# Starting the mixer
mixer.init()

# Loading the song
mixer.music.load("gym.mp3")

# Setting the volume
mixer.music.set_volume(0.9)

# Start playing the song
mixer.music.play()


log_exercise = ""
if input_day == 'mon':
    print(f"\t\t\t\t today\'s exercise is for chest: \n"
          f"\tbarbel bench press {weight / 3} kg [15 | 10 |8]\n"
          f"\tchest press {weight / 6}kg each dumbbell [20 |15 |10]\n"
          f"\tpush ups 30\n")
    response = input("have you done the exercise[y/n]\n-->")
    if response == 'y':
        log_exercise = ("mon " + time.asctime() + " chest done\n")
    else:
        log_exercise = ("mon " + time.asctime() + " skipped\n")

if input_day == 'tue':
    print(f"\t\t\t\t today\'s exercise is for back-bicep: \n"
          f"\t dead lift {weight / 3} kg [15 | 10 |8]\n"
          f"\t quadruped dumbbell row {weight / 6}kg each dumbbell [20 |15 |10]\n"
          f"\t planks 1 min\n")
    response = input("have you done the exercise[y/n]\n-->")
    if response == 'y':
        log_exercise = ("tue " + time.asctime() + " back-bicep done\n")
    else:
        log_exercise = ("tue " + time.asctime() + " skipped\n")

if input_day == 'wed':
    print(f"\t\t\t\t today\'s exercise is cardio and abs: \n"
          f"\t elliptical cross trainer 15 minutes \n"
          f"\t spin bike 15 minutes\n"
          f"\t do russian twist with {weight / 9} kg weight [20 time]\n"
          f"\t crunches with {weight / 9} kg weight near chest[30 times]")
    response = input("have you done the exercise[y/n]\n-->")
    if response == 'y':
        log_exercise = ("wed " + time.asctime() + " cardio and abs done\n")
    else:
        log_exercise = ("wed " + time.asctime() + " skipped\n")

if input_day == 'thu':
    print(f"\t\t\t\t today\'s exercise is for shoulder-triceps : \n"
          f"\t seated rear lateral raise {weight / 6} kg each dumbbell [15 | 10 |8]\n"
          f"\t over head shoulder press {weight / 6}kg each dumbbell [20 |15 |10]\n"
          f"\t dumbbell front raise {weight / 6}kg each dumbbell [20 |15 |10]\n")
    response = input("have you done the exercise[y/n]\n-->")
    if response == 'y':
        log_exercise = ("thu " + time.asctime() + " shoulder-triceps done\n")

    else:
        log_exercise = ("thu " + time.asctime() + " skipped\n")

if input_day == 'fri':
    print(f"\t\t\t\t today\'s exercise is cardio and abs: \n"
          f"\t elliptical cross trainer 15 minutes \n"
          f"\t spin bike 15 minutes\n"
          f"\t do russian twist with {weight / 9} kg weight [20 time]\n"
          f"\t crunches with {weight / 9} kg weight near chest[30 times]")
    response = input("have you done the exercise[y/n]\n-->")
    if response == 'y':
        log_exercise = ("fri " + time.asctime() + " cardio and abs done\n")

    else:
        log_exercise = ("fri " + time.asctime() + " skipped\n")

if input_day == 'sat':
    print(f"\t\t\t\t today\'s exercise is for legs: \n"
          f"\tlunges with {weight / 10} kg weight each dumbbell [15 | 10 |8]\n"
          f"\tsquats weight lifting with {weight / 2}kg total including rod [ 15 |10]\n"
          f"\t leg press with total{weight * 2} 30\n")
    response = input("have you done the exercise[y/n]\n-->")
    if response == 'y':
        log_exercise = ("sat " + time.asctime() + " legs done\n")
    else:
        log_exercise = ("sat " + time.asctime() + " skipped\n")

if input_day == 'sun':
    print(f"\t\t\t\t Rest \n")
    log_exercise = ("sun " + time.asctime() + " rest \n")

print(log_exercise)
# I learnt file operators from w3 schools
f = open("log.txt", 'a')
f.write(log_exercise)
f.close()

l = input("\t\t Do You Want to see the log until now?[y/n]\n\t\t-->")

if l == 'y':
    f = open("log.txt", "r")
    print(f.read())
    f.close()

q = input("\t\t--what would you like to have in breakfast?--\n\t\t\t-->")
q = q.split()
qj = '+'
qj = qj.join(q)
# I used geeks for geeks for this join function
# I learnt webbrowser opening from
# "engineers club" youtube channel and documentaton from
# :: https://docs.python.org/3/library/webbrowser.html
#  the youtube browser accepts search queries in this format https://www.youtube.com/results?search_query=
webbrowser.open_new(f"https://www.youtube.com/results?search_query=how+to+make+{qj}")
