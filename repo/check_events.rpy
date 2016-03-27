init 2 python:
    beg = 1
    def check_location(location):
        if location.label == "new_reality":
            if beg == 1:
                renpy.call("beginning")

label beginning:
    scene intro one
    python:
         renpy.pause()
    scene intro two
    "You get out of bed, relaxed and ready to have a great day"
    python:
         renpy.pause()
    scene intro three
    "You go to the door to leave your bedroom..."
    python:
         renpy.pause()
    scene intro four
    "THIS IS NOT NORMAL!!"
    python:
         renpy.pause()
    scene intro five
    "Everything is gone... this shouldn't be possible!"
    python:
         renpy.pause()

    scene black
    stop music
    play sound "./rsrc/door.mp3"
    python:
         renpy.pause()

    "The door slams behind you."
    "The world has gone black around you."
    "What is this update? What have they done?"
    "Where do you go from here?"
    $beg = 0
    jump new_reality
    return
