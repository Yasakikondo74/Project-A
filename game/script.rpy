label start:

    "Choose how would you look like!"

    window hide
    show screen box
    pause

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
    $ Character_selection = 1
    return

label Condition2:
    $ Character_selection = 2
    return