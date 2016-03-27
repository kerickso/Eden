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

    node8 = Location("node8", "Maze")
    node1.add_right(node8)
    maze_entrance.add_right(node8)
    node8.add_left(maze_entrance)

    node9 = Location("node9", "Maze")
    node8.add_right(node9)

    node10 = Location("node10", "Maze")
    node9.add_right(node10)
    node10.add_left(node9)

    node11 = Location("node11", "Maze")
    node10.add_top(node11)

    node12 = Location("node12", "Maze")
    node11.add_right(node12)
    node12.add_left(node11)
    node12.add_bottom(node10)

    node13 = Location("node13", "Maze")
    node12.add_right(node13)
    node13.add_left(node12)

    node14 = Location("node14", "Maze")
    node13.add_top(node14)
    node7.add_right(node14)
    node14.add_left(node11)

    node15 = Location("node15", "Maze")
    node10.add_bottom(node15)

    node16 = Location("node16", "Maze")
    node15.add_right(node16)
    node16.add_right(node13)

    node17 = Location("node17", "Maze")
    node6.add_left(node17)
    node17.add_top(node15)

    final_location = Location("final_location", "The End")
    node17.add_left(final_location)

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

label node9:
    scene black
    python:
        renpy.hide_screen("ui_nav")
        check_location(node9)
        renpy.show_screen("ui_nav", node9)
        node9.screen_loop()
    return

label node10:
    scene black
    python:
        renpy.hide_screen("ui_nav")
        check_location(node10)
        renpy.show_screen("ui_nav", node10)
        node10.screen_loop()
    return


label node11:
    scene black
    python:
        renpy.hide_screen("ui_nav")
        check_location(node11)
        renpy.show_screen("ui_nav", node11)
        node11.screen_loop()
    return

label node12:
    scene black
    python:
        renpy.hide_screen("ui_nav")
        check_location(node12)
        renpy.show_screen("ui_nav", node12)
        node12.screen_loop()
    return

label node13:
    scene black
    python:
        renpy.hide_screen("ui_nav")
        check_location(node13)
        renpy.show_screen("ui_nav", node13)
        node13.screen_loop()
    return


label node14:
    scene black
    python:
        renpy.hide_screen("ui_nav")
        check_location(node14)
        renpy.show_screen("ui_nav", node14)
        node14.screen_loop()
    return

label node15:
    scene black
    python:
        renpy.hide_screen("ui_nav")
        check_location(node15)
        renpy.show_screen("ui_nav", node15)
        node15.screen_loop()
    return

label node16:
    scene black
    python:
        renpy.hide_screen("ui_nav")
        check_location(node16)
        renpy.show_screen("ui_nav", node16)
        node16.screen_loop()
    return


label node17:
    scene black
    python:
        renpy.hide_screen("ui_nav")
        check_location(node17)
        renpy.show_screen("ui_nav", node17)
        node17.screen_loop()
    return

label final_location:
    scene black
    python:
        renpy.hide_screen("ui_nav")
        check_location(final_location)
        renpy.show_screen("ui_nav", final_location)
        final_location.screen_loop()
    return



