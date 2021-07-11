shop_intro:
    set global_actionsleft = 5
    set_screen default
    set_button button_shop_intro false
    set_button button_library_intro true
    "A hyeana, in her early thirties perhaps, looks up briefly when you enter. She pays you little attention after an an initial glance over you. The shop itself seems to sell a range of junk, ranging from run of the mill tat to counterfeit brands. The important thing is it's cheap. A few boxes of breakfast cereal sit on the shelf. Nutritional value 90% dust 10% whatever is in wheat."
    talk lovely excited "Oooh! Special L! We should get some!"
    talk nasty talk "Aren't breakfast cereals a little working class for you, Lovely Lady?"
    choice:
        talk lovely talk "Cereals are rather popular with the aristocracy these days, I'll have you know, and Special L is among the finest."
        "What's special about it?":
            talk lovely talk "It's reinforced with added lead, hence the L. All for health reasons, you see. Most cereals can't boast that."
            $if this.skillCheck("shop_intro_lead_orb", "orb", 20):
                talk orb talk "I'm sorry, it's reinforced with added *what*?"
        "Ok. (Move on)":
            talk lovely talk "Your loss."
    talk nasty talk "Anyway, forget the cereal, this shop sells Oestro brand Oestrodil Cigarettes. A smooth minty taste with a satisfying warm sparkle. Oestro. Garunteed to leave you satisfied."
    choice:
        talk nasty talk "BUY SOME TODAY."
        "Is smoking oestrodil safe?":
            talk orb talk "It's banned in 1954."
            talk nasty talk "They couldn't handle the heat."
            talk orb talk "Is heat 'slang' for lung damage?"
            talk lovely talk "I simple use an oestrohookah, the classy, *healthy* alternative."
            talk orb neautral "Marginally better for you, I suppose."
        "I'll think about it.":
            talk nasty talk "Fuck thinking, you fucking brain cuck. Buy some cigarettes."
        "Sorry Nasty Girl, but smokers are jokers.":
            talk nasty talk "Fuck you. Die."

    choice:
        ""
        "Do I even have any money?":
            talk orb talk "You have a purse on you and fortunatly, and it has some money in it."
        
    jump shop_menu