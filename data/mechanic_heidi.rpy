mechanic_heidi:
    talk mechanic "She left for Brennenburg, visiting family she didn't even like, a week before the war started and the borders closed. She would have been drafted a few months later, the Imperials started conscripting early. I knew that she would be on the front, it's why I did my best to avoid serving for so long. 'Accidently' breaking my arm, y'know? I wasn't going to kill her."
    "She lights a new ciggarete. The butt of the previous one dies under her boot."
    talk mechanic "Anyway, eventually I couldn't avoid it. I thought I was lucky when the conscription officer recognised me from the Schottland Great 14 motorcycle race. Recon. That's a good way to not shoot my..."
    "She trails off."
    talk mechanic "It was bullshit. Pulling a trigger, launching a motar, placing a land mine, delivering a letter. It all ends the same way."

    choice:
        talks mechanic "Besides her name, Tennenburg and the date 01/09/1923. She was the sniper."
        "The sniper who shot you?":
            talk mechanic "The sniper I shot."
            "She isn't looking at you. She's looking behind you, at the sniper."
    choice:
        ""
        "You *didn't* order it, though.":
            talk mechanic "I did. I crawled through fucking mud and shrapnel to order it."
        "You didn't *order* it, though.":
            talk mechanic "It was a letter marked orders. What the fuck else was it? The military doesn't 'ask nicely'."
        "*You* didn't order it, though.":
            talk mechanic "I passed on the fucking position, didn't I? It's why I get to be called a fucking war heroine for the rest of my life."
        "(Remain silent)":

    $if this.skillCheck("mechanic_heidi_mechanic_orb", "orb", 80):
        choice:
            talk orb "I didn't want to bring this up until now, but I know what actually happened to Heidi. The mechanic does too, even if she won't admit it."
            "Tell me.":
                choice:
                    talk orb "Heidi was at Tennenburg, that much is true. But the sniper that shot the mechanic? A twenty three year old squirrel called Edektraut. They survived the battle and currently work in a factory that produces radio parts."
                    "What happened to Heidi?":
                        talk orb "Heidi was a mechanic. She repaired equipment. Trucks, planes, weapons... She was repairing a stolen Ratzubishi when a Marigold MK.IV Heavy Artillary Cannon launched a shell over twenty miles towards the makeshift workshop."
            "Let's not dwell on it (Move on).":
                talk orb "If your prefer."

