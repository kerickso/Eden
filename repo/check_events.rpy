init 2 python:
    beg = 1
    def check_location(location):
        global beg
        if location.label == "new_reality":
            if beg == 1:
                renpy.call("beginning")
        if location.label == "your_room":
            if beg == 2 or beg == 3:
                renpy.call("room")
        if beg == 4:
            beg = beg - 1

label beginning:
    scene intro one

    scene intro two
    "You get out of bed, relaxed and ready to have a great day"

    scene intro three
    "You go to the door to leave your bedroom..."

    scene intro four
    "What you see outside... is NOT normal!!"

    scene intro five
    "Everything is gone! This... shouldn't be possible!"

    scene black
    stop music
    play sound "./rsrc/door.mp3"

    python:
        renpy.pause()

    "The door slams behind you"

    play music "./rsrc/cosima_slow.mp3" fadein 4.0
    python:
        renpy.music.set_volume(0.3, .3, channel="music")

    "The world appears to have gone black around you"
    "Where is your house? What have they done?"
    scene matrix one with fade

    "Suddenly, you see green text appear where there should be a hallway"
    "\"What the hell?\""
    $beg = 2
    jump new_reality
    return

label room:
    python:
        renpy.pause()
        if new_reality.can_move("up") != True:
            new_reality.add_top(maze_entrance)
    $beg = 4
    jump your_room
    return
