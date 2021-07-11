nightmare:
    $if this.data.day == 0:
        "."
        set day 1
        set introducePilot true
        jump nightmare_one

nightmare_orb_reveal:
    choice:
        talk orb talk "I should probably have come clean sooner, but I was worried you might take it badly."
        "Take *what* badly?":
            talk orb talk "What I'm about to say."
    choice:
        ""
        "You are stalling so hard right now.":
            talk orb talk "I've been spreading through your body like a fungi mycelium. I haven't been doing it on purpose but it's kind of just what I do."
    choice:
        ""
        "What the fuck.":
            jump nightmare_orb_explains
        "What the fuck?":
            jump nightmare_orb_explains
        "What the fuck!":
            jump nightmare_orb_explains

nightmare_orb_explains      
    talk orb talk "I'm not generally supposed to take replace anyones heart, so when I did I... I sort of panicked, I guess. By the end of the week most of your arteries will be hosting mycelium, in another two days your veins will be, another day on top of that the capillaries in your lungs and eyes are going to be replaced too. Sorry. If that happens I'm not leaving. It would kill you. On the plus side I might fruit, that'd be cute, right?"

    choice:
        ""
        "Fungus are from space?":
            talk orb talk "Is that a joke? Where did you think it came from?"
    jump home