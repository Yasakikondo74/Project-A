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

label upgrade_raw_money:
    $ mc.upgrade_income()
    jump Location
    return

label upgrade_income:
    $ mc.upgrade_raw_money()
    jump Location
    return

label Bedroom:
    scene bedroom
    pause
    return