init 2 python:
    beg = 1
    def check_location(location):
        global beg
        if location.label == "new_reality":
            if beg == 1:
                renpy.call("beginning")
        if location.label == "your_room":
            if beg == 2:
                renpy.call("room")
        if beg == 3:
            beg = beg - 1
        if location.label == "final_location":
            renpy.jump("finale")

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
    "\"Normal my ass! Where is everything!?\""
    $beg = 3
    jump your_room
    return

label finale:
   ###
   "There seems to be a way to interact with the computer here."
label loop1:
   "What do you do?"
   menu:
       "Talk":
            "There is no response."
            jump loop1
       "Think":
            "The AIs weren't given access to your mind. Nothing happens."
            jump loop1
       "Type":
            "You start typing."
            "Nonsense falls out of your fingertips."
            "You don't quite understand what you're typing - nobody types here anymore; there is no code, no stress, no computers other than the ones that protect you. There was only ever peace here."
            "But you keep typing somehow."
            "What do you type?"
            menu:
                "Kim Kardashian":
                     "Something's not quite right..."
                     jump death
                "Machine Learning":
                     "Nothing particularly bad happens yet..."
                     menu:
                         "Heap Kernel":
                              "You keep going..."
                              menu:
                                  "Expectation-Maximization Algorithm":
                                      "You've finished. You press ENTER and the world begins to reset."
                                      stop music
                                      scene intro one with fade
                                      play music "./rsrc/cosima.mp3"
                                      "You are in a bed. The world is calm around you."
                                      "Do you dare to leave the room?"
                                      scene black with fade
                                      centered "The End"
                                  "Clear All":
                                      "Oh, no..."
                                      jump death
                         "Reset":
                              "Nothing happens, not at first..."
                              "But, then - "
                              jump death
   return

label death:
    "The code around you flickers and you start to feel strange...."
    "This isn't right."
    "Eden is crashing around you."
    scene black with fade
    centered "The world is gone."
    centered "And now you are gone, too."
    centered "Is there a reality beyond this one?"
    centered "Will you ever wake up?"
    centered "The End"
    return
