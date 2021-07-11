home_intro:
    clear_dialog
    set global_actionsleft = 9
    set_button button_shepherd_intro true
    "Decor hangs from the walls, but it means nothing to you. In the study upstairs water drips from the damaged roof and stains the wooden floor, but in the absence of emotional connection to the abode there is no sense of urgency in fixing it."
    jump home_intro_menu

home_intro_menu:
    choice:
        ""
        "(Dust the floor)" $if !this.data.home_intro_dust:
            jump home_intro_dust
        skillcheck home_intro_menu_blood_nasty nasty 80 "(Clean up the blood)" $if !this.data.home_intro_blood:
            success "[SUCCESS]":
                jump home_intro_blood_success
            failed "It wont come out. It sits there, taunting you.":
                jump home_intro_blood_fail
        "(Pick up the broken vase)" $if !this.data.home_intro_vase:
            jump home_intro_vase
        "(Move on)" $if this.data.home_intro_vase & this.data.home_intro_blood & this.data.home_intro_dust:
            jump game_map

home_intro_dust:
    set home_intro_dust true
    "dust the floor"
    "Huh, you find a few pennies!"
    "Some of them are even Anglian ones!"
    $if this.skillCheck("home_intro_dust_dust_orb", "orb", 40):
        talk orb talk "The cottages previous owner spent a lot of time in Frankreich."   
    jump home_intro_menu

home_intro_blood_success:
    set home_intro_blood true
    talk nasty talk "Not an easy task without chemicals, but I think that did the job pretty well."
    jump home_intro_menu

home_intro_blood_fail:
    set home_intro_blood true
    set global_needStainRemover true
    talk nasty talk "use this chemical. You could probably buy it at the shop."
    jump home_intro_menu

home_intro_vase:
    set home_intro_vase true
    choice:
        "[pick it up]"
        skillcheck home_intro_vase_vase_lovely lovely 90 "(Fix the broken vase)":
            success "fixed":
                talk lovely talk "With a delicate touch a true lovely lady can fix any broken crockery without the need for glue. It is held together with willpower and love alone."
                talk orb talk "Even I can't explain this nonsense."
                jump home_intro_menu
            failed "failed":
                choice:
                    "It just doesn't seem to fit together. It sits there, mocking you. A shadow of its former self. Did you put it together in the wrong order? Are pieces missing? Do you even remember what it looked like? Was the vase ever assembled in the first place?"
                    "(Keep it for later)":
                        set global_keptBrokenVase true
                        "[KEEP]"
                        jump home_intro_menu
                    "(Throw it out)":
                        "[THROW OUT"
                        jump home_intro_menu
        "(Throw it out)":
            "[throw out the vase.]"
            "The shards tinkle and echo as they hit the metal base, like teeth falling out into a china cup."
            jump home_intro_menu