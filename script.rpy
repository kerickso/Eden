# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define solo = Character('SOLO', color="#00ff00")


# The game starts here.
label start:
    scene black #you can replace this with the image for the background or TXT.

    "You wake up in your room. It has been your room for as long as you can remember. It comes will all of the things a person would need."
    "Yet, there is a door - a single door, to the outside world. You've never opened the door before, never gone through."
    "It may be silly, but you've always been a bit curious what is beyond that door."
    "Your room is perfect. It has everything you need or want."
    "It has food, it has warmth. Toys, instruments, blankets, a bed..."
    "You have everything you need."
    "But then, what could be beyond the door?"
    "Something in you tells you that leaving the room would be a horrible mistake."
    "But what if it isn't?"
    "Do you leave the room?"
    menu enter_reality:
        "Yes":
             jump new_reality
        "No":
             "You've decided to stay in this room. You have everything you could ever want."
             "What could possibly go wrong if you stay here?"
    centered "The End"

label wake_up:
    solo "THIS IS YOUR LIFE NOW"

    solo "Nothing is wrong. Everything you see is perfectly ordinary."

    return
