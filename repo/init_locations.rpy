##### Step 1: SET UP ALL THE LOCATION OBJECTS #####
init 1 python:
    # Just in case the UI nav has been popped up....
    renpy.hide_screen("ui_nav")

    new_reality = Location("new_reality", "New Reality")
    your_room = Location("your_room", "Your Room")
    new_reality.add_bottom(your_room)
    your_room.add_top(new_reality)

    maze_entrance = Location("maze_entrance", "Into the Maze")

    node1 = Location("node1", "Maze")
    maze_entrance.add_top(node1)

    node2 = Location("node2", "Maze")
    node1.add_top(node2)
    node2.add_bottom(node1)

    node3 = Location("node3", "Maze")
    node2.add_right(node3)
    node3.add_left(node2)

    node4 = Location("node4", "Maze")
    node3.add_top(node4)

    node5 = Location("node5", "Maze")
    node4.add_top(node5)

    node6 = Location("node6", "Maze")
    node5.add_top(node6)

    node7 = Location("node7", "Maze")
    node6.add_right(node7)
    node7.add_bottom(node5)

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

label node1:
    scene black
    python:
        renpy.hide_screen("ui_nav")
        check_location(node1)
        renpy.show_screen("ui_nav", node1)
        node1.screen_loop()
    return

label node2:
    scene black
    python:
        renpy.hide_screen("ui_nav")
        check_location(node2)
        renpy.show_screen("ui_nav", node2)
        node2.screen_loop()
    return

label node3:
    scene black
    python:
        renpy.hide_screen("ui_nav")
        check_location(node3)
        renpy.show_screen("ui_nav", node3)
        node3.screen_loop()
    return

label node4:
    scene black
    python:
        renpy.hide_screen("ui_nav")
        check_location(node4)
        renpy.show_screen("ui_nav", node4)
        node4.screen_loop()
    return


label node5:
    scene black
    python:
        renpy.hide_screen("ui_nav")
        check_location(node5)
        renpy.show_screen("ui_nav", node5)
        node5.screen_loop()
    return

label node6:
    scene black
    python:
        renpy.hide_screen("ui_nav")
        check_location(node6)
        renpy.show_screen("ui_nav", node6)
        node6.screen_loop()
    return

label node7:
    scene black
    python:
        renpy.hide_screen("ui_nav")
        check_location(node7)
        renpy.show_screen("ui_nav", node7)
        node7.screen_loop()
    return


label node8:
    scene black
    python:
        renpy.hide_screen("ui_nav")
        check_location(node8)
        renpy.show_screen("ui_nav", node8)
        node8.screen_loop()
    return



