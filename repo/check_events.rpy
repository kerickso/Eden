init 2 python:
    beg = 1
    def check_location(location):
        if location.label == "new_reality":
            if beg == 1:
                renpy.call("beginning")
        if location.label == "your_room":
            if beg == 2:
                renpy.call("room")

label beginning:
    scene intro one

    scene intro two
    "You get out of bed, relaxed and ready to have a great day"

    scene intro three
    "You go to the door to leave your bedroom..."

    scene intro four
    "THIS IS NOT NORMAL!!"

    scene intro five
    "Everything is gone... this shouldn't be possible!"

    scene black
    stop music
    play sound "./rsrc/door.mp3"
    python:
         renpy.pause()

    "The door slams behind you"
    "The world appears to have gone black around you"
    "Where is your house? What have they done?"
    scene matrix one with fade
    "Suddenly, you see green text appear where there should be a hallway"
    "What the fuck?"
    $beg = 2
    jump new_reality
    return

label room:
    "This is your room. This is normal."
    $beg = 3
    jump your_room
    return
