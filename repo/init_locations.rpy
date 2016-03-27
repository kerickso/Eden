##### Step 1: SET UP ALL THE LOCATION OBJECTS #####
init 1 python:
    # Just in case the UI nav has been popped up....
    renpy.hide_screen("ui_nav")

    new_reality = Location("new_reality", "New Reality")
    your_room = Location("your_room", "Your Room")
    new_reality.add_bottom(your_room)
    your_room.add_top(new_reality)

    maze_entrance = Location("maze_entrance", "Into the Maze")

###### Step 2: SET UP ALL THE REN'PY TAGS: #####
label new_reality:
    scene matrix one
    python:
        renpy.hide_screen("ui_nav")
        check_location(new_reality)
        renpy.show_screen("ui_nav", new_reality)
        new_reality.screen_loop()
    return

label your_room:
    scene matrix two
    python:
        renpy.hide_screen("ui_nav")
        check_location(your_room)
        renpy.show_screen("ui_nav", your_room)
        your_room.screen_loop()
    return

label maze_entrance:
    scene black
    python:
        renpy.hide_screen("ui_nav")
        check_location(maze_entrance)
        renpy.show_screen("ui_nav", maze_entrance)
        maze_entrance.screen_loop()
    return




