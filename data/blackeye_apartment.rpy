blackeye_apartment:
    set global_actionsleft this.data.global_actionsleft - 1
    set_screen default
    set_button button_blackeye_apartment false
    talk blackeye talk "’Chateux Saint-Arnoin’? It’s vintage nineteen-fifteen."
    choice:
        "She asks this with an eyebrow raised like a conqourers flag."
        "I love wine (Nod)":
            talk lovely talk "Wise choice. Saint-Arnoin is famous for its wines. We LIKE to drink it."
            talk nasty talk "We LIKE to put undue emphasis on words. Idiot."
        "No thank you.":
            "Blackeye shrugs in a way that conveys both disappointment and nonchalance. An impressive feat."
            talk blackeye talk "More for me."
            "She pours herself a glass and leaves yours empty; a monument to your lack of taste."
    talk blackeye talk "It’s somewhat sweeter than my usual preference, still, it reflects well on one to have range, yes? One can hardly put into words the texture of a dry wine if one has not experienced a sweeter wine, no?"
    "She lifts her glass to her nose, and shut her eyes."

    choice:
        talk orb talk "It seems her vocabulary mostly consisted of the word ‘one’, when wine was involved."
        "Do you drink a lot?":
            talk blackeye talk "It’s a hobby, one supposes."
            "Her eyes glance to the work desk a few feet away, and she motions her glass towards it."
            choice:
                talk blackeye talk "I keep notes. Compare tastes, textures and scents. A good wine is much like a good girl, no?"
                "(Nod sagely)":
                    ""
        "(Remain silent)":
            ""
  




    "Blackeye exhales a plume of oestrogen. Your snout greedily sniffs it up. she then fiddled with one of her necklaces: a crystal of some sort. Her fingers slip away from it after a short moment, and its worn surface is revealed."
    $if this.skillCheck("blackeye_apartment_necklace_orb", "orb", 40):
        talk orb talk "All three of her necklaces are worn, but this one is clearly the one she incessantly rubs the most. It had a rather satisfying smooth texture at one point, now its just one of the many habits this woman has picked up from a decade of stress compressed into a short few years."




    talk blackeye talk "You're welcome to stay, Ms."
    "You feel a twinge, the feeling of a nail run from your tail, along your spine, before finally terminating at the the scruff of your neck. How could you not shiver."
    talk lovely talk "It would be awfully rude of us to impose on her."
    talk nasty talk "I have no qualms if Blackeye desires to impose on us."
    "The oestrogen haze had gotten denser. Lily’s tolerance for the drug was high, but the amount Blackeye seemed to be getting through was almost scary."
    talk orb talk "I know you want to, but you cant. Not tonight. I can't see exactly why, but you should wake up at home tomorrow. Just keep walking."
    talk blackeye talk "'Ghost'."
    "She swirls yet another bottle of wine in her hand. The light of her dying candle flickering through the green glass as though swimming, inside her green eyes as though trapped."
    talk blackeye talk "Sleep Well."
    jump game_map