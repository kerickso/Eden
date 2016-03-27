init 2 python:
    def check_location(location):
        if location.label == "new_reality":
            renpy.call("beginning")


label beginning:
    scene intro one
    python:
         renpy.pause()
    scene intro two
    python:
         renpy.pause()
    scene intro three
    python:
         renpy.pause()
    scene intro four
    python:
         renpy.pause()
    scene intro five
    python:
         renpy.pause()

    scene black
    #slamming door audio
    python:
         renpy.pause()

    "The door slams behind you."
    "The world has gone black around you."
    "What is this update? What have they done?"
    "Where do you go from here?"
