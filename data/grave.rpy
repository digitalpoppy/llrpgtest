grave_funeral:
    set_screen default
    set heroineAtGrave true
    "The Heroine is already here."
    $if this.skillCheck("grave_funeral_mechanic_lovely", "lovely", 20):
        talk lovely talk "She arrived over an hour early. Usually I'd roll my eyes, for as we all know being late is far more fashionable, but given the context I'll keep my lips sealed."
        talk nasty talk "You realise you just spoke right? You can't just say something and then pat yourself on the back for not saying it. Gods fucking damnit."
        talk orb talk "The heroine wanted some time alone. She's been sat silently, listening to the wind."

grave_gravestone:

    "It is tinted green, the summer sunlight through the tree canopy."
    talk nightmare talk "rest in pieces :)"
    talk orb talk "It'll stay there for a long time, slowly decaying away. Paint chipping off and colouring the rainwater puddles, rust breaking down the chasis like digestive enzymes. Children will find it decades from now and think they've found an ancient relic. A trio of dorky young lesbians will find it a few years after that. One of them will called it 'the dead skeleton of like, a car, or something?', another will correct them: 'It's a motorcycle, idiot.', the third will laugh quietly and shake her head."
    talk nightmare talk "you should say rest in pieces lol."
    talk lovely talk "That's very sweet."
    choice:
        talk nasty talk "No comment. But yes. It is."
        "Rest in peace.":
            talk orb talk "Rest in peace."
            talk lovely "Rest in peace."
            talk nasty "Rest in peace."
        "Rest in pieces.":
            talk lovely "That was so fucking innaproproate. Fuck me."
            talk nasty "There's a time and a place idiot. Fucking hell."
            choice:
                talk orb "Why would you even say that? Are you wrong in the head, moreso than already established?"
                "I thought Nasty Girl would like it.":
                    talk nasty talk "I'm a nasty girl, but I'm not a monster, jackass."
                    talk lovely talk "Good fucking lord."
                "I misspoke.":
                    talk orb talk "No she didn't, get her ass girls."
                    talk lovely talk "You're a real piece of shit."
                    talk nasty talk "Fucking gross. I hope you die very soon."
                "Sorry.":
                    talk orb talk "Mhm."
            $if this.data.heroineAtGrave:
                talk orb talk "You are so lucky The Heroine didn't hear that."
        "(Nod respectfully)":
            talk lovely talk "Very respectful, but I'd have said 'Rest in peace', just in case anyone was listening in."
    $if this.data.heroineAtGrave:
        jump grave_futuretalk
    else:
        jump field

grave_futuretalk:  
    ""
    choice: 
        ""
        "What if you want to get back into racing?":  
        talk mechanic talk "I'll get a new one. Not military issue; something that'll actually stay in one piece. A SoWoki, maybe, those are meant to bop."
        "She smiles. It's genuine. She's excited."

    $if this.data.heroineAtGrave:
        jump field
    else:
        jump shopkeeper_menu