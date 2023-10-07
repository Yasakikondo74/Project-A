label Location:
    hide screen back
    hide screen upgrades
    show screen button_to_upgrades
    if mc.location == "Home":
        show bedroom
        jump Bedroom
    elif mc.location == "School":
        show school
        jump School
    elif mc.location == "Workplace":
        show work_area
        jump Work_area
    return

label upgrades:
    show screen button_to_upgrades
    jump Bedroom
    return

label show_upgrade:
    hide screen button_to_upgrades
    show screen back
    show screen upgrades
    pause
    return

label Condition1:
    $ mc.Character_selection = 1
    jump start2
    return

label Condition2:
    $ mc.Character_selection = 2
    jump start2
    return

label upgrade_raw_money:
    if mc.income == 5:
        $ mc.income = 10
    elif mc.income == 10:
        $ mc.income = 20
    elif mc.income == 20:
        $ mc.income = 50
    elif mc.income == 50:
        $ mc.income = 100
    jump Location
    return

label upgrade_income:
    if mc.salery_increase == 1:
        $ mc.salery_increase = 2
    elif mc.salery_increase == 2:
        $ mc.salery_increase = 3
    elif mc.salery_increase == 3:
        $ mc.salery_increase = 3
    jump Location
    return

label Bedroom:
    show bedroom
    pause
    return