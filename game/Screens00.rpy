init:
    transform customzoom:
        zoom 0.5

screen box():
    # First option
    imagebutton:
        idle "male1_hover.png" 
        hover "male1.png" 
        align (0.5, 0.5) #X & Y
        action Jump("Condition1")
        at customzoom 

    # Second option
    imagebutton:
        idle "male2_hover.png" 
        hover "male2.png" 
        align(0.95, 0.5) #X & Y
        action Jump("Condition2")
        at customzoom 

