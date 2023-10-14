label start:

    "Choose how would you look like!"

    window hide
    show screen Character_selection
    pause
    return

label start2:
    hide screen Character_selection
    show screen mc

    unknown "Hello?"

    C "What's your name?"

    $ mc.name = renpy.input("Input your Name:").strip()

    if mc.name == "":
        $ mc.name = "Player"
    
    C "Welcome, [mc.name]!"

    C "your journey begins here"
    hide screen mc
    jump upgrades
    return