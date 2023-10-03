screen box():
    # First option
    imagebutton at center:
        idle "male1_hover.png"
        hover "male1.png"
        xalign 0.5
        yalign 0.5
        action Jump("Condition1")

    # Second option
    imagebutton at right:
        idle "male2_hover.png"
        hover "male2.png"
        xalign 0.75
        yalign 0.5 
        action Jump("Condition2")

