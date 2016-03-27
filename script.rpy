# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define solo = Character('SOLO', color="#00ff00")


# The game starts here.
label start:
    play music "rsrc/cosima.mp3"
    scene title one
    python:
        renpy.pause()
    scene title two
    python:
        renpy.pause()
    scene title three
    python:
        renpy.pause()
    scene title four
    python:
        renpy.pause()

    scene intro one #you can replace this with the image for the background or TXT.
    "Do you leave the room?"
    menu enter_reality:
        "Yes":
             python:
                 renpy.pause()
             jump new_reality
        "No":
             "You've decided to stay in this room. You have everything you could ever want."
             "What could possibly go wrong if you stay here?"
    centered "The End"

    return
