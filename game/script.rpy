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

    jump upgrades
    return