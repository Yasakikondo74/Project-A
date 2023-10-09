init:
    transform custom_mc_zoom:
        zoom 0.5
    transform custom_ui_zoom:
        zoom 0.3

screen mc():
    if mc.Character_selection == 1:
        add "male1.png" at custom_mc_zoom align(1., 1.0)
    elif mc.Character_selection == 2:
        add "male2.png" at custom_mc_zoom align(1.0, 1.0)

screen back():
    imagebutton:
        idle "Back_hover.jpg"
        hover "Back_idle.jpg"
        align (0.95, 0.05)
        action Jump("Location")
        at custom_ui_zoom

screen button_to_upgrades():
    imagebutton:
        idle "Button_hover.jpg"
        hover "Button_idle.jpg"
        align (0.95, 0.05)
        action Jump("show_upgrade")
        at custom_ui_zoom

screen upgrades():
    imagebutton:
        idle "raw_hover.jpg"
        hover "raw_idle.jpg"
        align (0.3, 0.5)
        action Jump("upgrade_raw_money")
        at custom_ui_zoom
    imagebutton:
        idle "Income_hover.jpg"
        hover "Income_idle.jpg"
        align (0.7, 0.5)
        action Jump("upgrade_income")
        at custom_ui_zoom
        

screen Character_selection():
    # First option
    imagebutton:
        idle "male1_hover.png" 
        hover "male1.png" 
        align(0.5, 1.0) #X & Y
        action Function(mc.Change_character1)
        at custom_mc_zoom 

    # Second option
    imagebutton:
        idle "male2_hover.png" 
        hover "male2.png" 
        align(1.0, 1.0) #X & Y
        action Function(mc.Change_character2)
        at custom_mc_zoom 

