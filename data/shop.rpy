shop:
    set_screen default
    jump shop_menu

shop_menu:
    choice:
        "desc"
        "(Flirt)" $if this.data.global_shopkeeperFlirt:
            jump shop_flirt
        "(Buy - Roof tiles)":
            jump shop_roofTiles
        "(Buy - lumber)":
            jump shop_lumber
        "(Buy - Mx Lilyannes Blood Stain Remover)" $if this.data.shopkeeperSellingChemical:
            jump shop_chemicals
        "(Buy - Tin of Oestro brand Oestrodil Cigarettes)"
            jump shop_cig
        "(Buy - The Lovely Lady Handbook)" $if this.data.hasHandbook:
            jump shop_handbook
        "(Leave)":
            jump game_map

shop flirt:
    ""
    jump shop_menu

shop_roofTiles:
    "You purchase a crate of roof tiles."
    set hasRoofTiles true
    jump shop_menu

shop_lumber:
    "You purchase a few pieces of lumber."
    set hasTimber true
    jump shop_menu

shop_chemicals:
    "You purchase a bottle of Mx Lilyannes Blood Stain Remover."
    set hasChemicals true
    jump shop_menu

shop_cig:
    "You purchase a tin of Oestro brand Oestrodil Cigarettes."
    set hasCig true
    talk nasty talk "Ok, good work. That's the easy part done. Now deepthroat one."
    jump shop_cigMenu

shop_cigMenu:
    choice:
        "Did she just ask you to *deepthroat* a cigarette?"
        "E-excuse me?":
            talk nasty talk "You heard me."
            talk lovely talk "Please don't."
            talk orb talk "I'm literally begging you to not do it."
            jump shop_cigMenu
        "Like, eat it? What are you asking from me here? Are you okay Nasty Girl?":
            talk nasty talk "Oh my gods."
            choice:
                talk nasty talk "JUST DO IT. BRAIN. CUCK."
                "WHY DO YOU KEEP SAYING THAT?":
                    talk lovely talk "She must have picked it up from somewhere, I'm so embarassed to be assosiated with her."
                    jump shop_menu
                "I'll show *you* who the 'brain cuck' is. (Deepthroat the cigarette).":
                    jump shop_cigDeepthroat
        "Who am I to question orders? (Deepthroat the cigarette)":
            jump shop_cigDeepthroat
        "I'm... not going to do that.":
            talk nasty talk "UGH. Doesn't anyone here like to have fun???"
            jump shop_menu

shop_cigDeepthroat:
    talk nasty talk "YESSSSS THIS IS GOOD RIGHT?"
    "The shopkeeper watches silently, as you open the carton of Oestrodil cigarettes, take a single one out, shove it in your mouth, and start choking. She correctly chooses not to acknowledge it."
    talk orb talk "Do you know how many years you just took off of your life?"
    $if this.skillCheck("simple", "orb", 20):
        talk orb talk "Exactly three."
    talk nasty talk "That was good. You should *totally* do it again."
    choice:
        talk orb talk "*Please* don't do that again."
        "(Do it again)":
            "The shopkeeper pretends to organise some wares. Lovely Lady and Orb are silent. They just want this to be over."
            choice:
                talk nasty talk "That bopped, right?"
                "Oh gods why did I do that.":
                    talk nasty talk "Because I told you to. I'm a top by the way."
                    jump shop_menu
                "That bopped. (Nod)":
                    jump shop_menu
        "(Look at the shopkeeper apologeticly and leave the store in shame)":
            jump bluehills
    jump shop_menu

shop_handbook:
    set hasHandbook true
    "The shopkeeper seems to cringe, but she keeps it to herself."
    $if this.skillCheck("simple", "orb", 20):
        choice:
            talk orb talk "Tell her its for research, not for personal use, im begging you."
            "It's for research, not for personal use, I swear.":
                talk shopkeeper talk "Good. It's shit."
                talk lovely talk "Rude!"
            "It's for personal use. I'm excited to read it.":
                talk shopkeeper talk "Uh huh."
                set shopkeeperImpressed shopkeeperImpressed - 2
    else:
        set shopkeeperImpressed shopkeeperImpressed - 1
    "This isn't a great reading environment. You should head home if you want to read the book."
    jump shopkeeper_menu