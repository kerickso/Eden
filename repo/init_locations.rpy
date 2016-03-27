##### Step 1: SET UP ALL THE LOCATION OBJECTS #####
init 1 python:
    # Just in case the UI nav has been popped up....
    renpy.hide_screen("ui_nav")

    new_reality = Location("new_reality", "New Reality")
    


    #location1.add_bottom(location2)
    #location2.add_left(location1)



###### Step 2: SET UP ALL THE REN'PY TAGS: #####
label new_reality:
    scene black
    python:
        renpy.hide_screen("ui_nav")
        check_location(new_reality)
        renpy.show_screen("ui_nav", new_reality)
        new_reality.screen_loop()
    return






