label start:

    "Choose how would you look like!"

    window hide
    show screen box
    pause
    return

label start2:
    hide screen box
    if mc.Character_selection == 1:
        show male1 at right
    elif mc.Character_selection == 2:
        show male2 at right

    unknown "Hello?"

    C "What's your name?"

    $ mc.name = renpy.input("Input your Name:").strip()

    if mc.name == "":
        $ mc.name = "Player"
    
    C "Welcome, [mc.name]!"

    C "your journey begins here"

    jump Bedroom

    return

label Condition1:
    $ mc.Character_selection = 1
    jump start2
    return

label Condition2:
    $ mc.Character_selection = 2
    jump start2
    return