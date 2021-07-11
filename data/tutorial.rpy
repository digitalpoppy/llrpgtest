tutorial:
    talk poppy talk "Hey everyone, just wanted to drop in to make sure you all knew you can SAVE your game at anytime by hitting the SAVE button. I reccomend doing it often!"
    talk lovely talk "And what if we want to LOAD the game?"
    talk poppy talk "Y- you lot aren't meant to be talking back to me! I'm non diagetic!"

    choice:
        talk nasty talk "Who the fuck cares if she exists or not. We should try to fuck the tutorial character."
        skillcheck tutorial_fuck_nasty nasty 90 "We *should* try to fuck the tutorial character.":
            success "It works!":
                talk lovely talk "You two are awful."
                talk poppy talk "Sorry Nasty Girl, but I really need to explain how to load the game right now!"
                set tutorial_fuckNarrator true
                jump tutorial_two
            failure "It fails!":
                talk lovely talk "You two are awful."
                talk poppy talk "Sorry Nasty Girl, but I really need to explain how to load the game right now!"
                jump tutorial_two
        "Best not to. (Move on)":
            jump tutorial_two

tutorial_two:
    talk poppy talk "Anyway, if you want to LOAD your game, press LOAD. It's rather self explanitory, I think, I'm not going to explain the rest of the UI to you, you aren't a child. I just wanted to make sure you realised the option was there : )"
    talk lovely talk "Ask her nicely and she might explain the rest of the UI for you."
    talk poppy talk "No. I won't. But I will let you know that from this point onwards the map will have multiple things for you to take care of, some of which might dissapear if you leave them too long! You won't have time to take care of everything, so be careful, and prioratise things you think will be important!"
    talk orb talk "Sage advice."
    $if this.data.tutorial_fuckNarrator:
        talk poppy talk "Anyway, I'll leave you alone now, but before I go: Nasty Girl. DM me."
    else:
        talk poppy talk "Anyway, I'll leave you alone now."
    "AJIUDHNUWGBDAOUSHND(AU*&)MYCNT£(*NCM$A)*&ATCNCY£(YCN&ANTC*C$ACN£T&*QNA£*N(ATCN^$AJIUDHNUWGBDAOUSHND(AU*&)MYCNT£(*NCM$A)*&ATCNCY£(YCN&ANTC*C$ACN£T&*QNA£*N(ATCN^$AJIUDHNUWGBDAOUSHND(AU*&)MYCNT£(*NCM$A)*&ATCNCY£(YCN&ANTC*C$ACN£T&*QNA£*N(ATCN^$AJIUDHNUWGBDAOUSHND(AU*&)MYCNT£(*NCM$A)*&ATCNCY£(YCN&ANTC*C$ACN£T&*QNA£*N(ATCN^$AJIUDHNUWGBDAOUSHND(AU*&)MYCNT£(*NCM$A)*&ATCNCY£(YCN&ANTC*C$ACN£T&*QNA£*N(ATCN^$AJIUDHNUWGBDAOUSHND(AU*&)MYCNT£(*NCM$A)*&ATCNCY£(YCN&ANTC*C$ACN£T&*QNA£*N(ATCN^$AJIUDHNUWGBDAOUSHND(AU*&)MYCNT£(*NCM$A)*&ATCNCY£(YCN&ANTC*C$ACN£T&*QNA£*N(ATCN^$AJIUDHNUWGBDAOUSHND(AU*&)MYCNT£(*NCM$A)*&ATCNCY£(YCN&ANTC*C$ACN£T&*QNA£*N(ATCN^$AJIUDHNUWGBDAOUSHND(AU*&)MYCNT£(*NCM$A)*&ATCNCY£(YCN&ANTC*C$ACN£T&*QNA£*N(ATCN^$AJIUDHNUWGBDAOUSHND(AU*&)MYCNT£(*NCM$A)*&ATCNCY£(YCN&ANTC*C$ACN£T&*QNA£*N(ATCN^$AJIUDHNUWGBDAOUSHND(AU*&)MYCNT£(*NCM$A)*&ATCNCY£(YCN&ANTC*C$ACN£T&*QNA£*N(ATCN^$AJIUDHNUWGBDAOUSHND(AU*&)MYCNT£(*NCM$A)*&ATCNCY£(YCN&ANTC*C$ACN£T&*QNA£*N(ATCN^$AJIUDHNUWGBDAOUSHND(AU*&)MYCNT£(*NCM$A)*&ATCNCY£(YCN&ANTC*C$ACN£T&*QNA£*N(ATCN^$AJIUDHNUWGBDAOUSHND(AU*&)MYCNT£(*NCM$A)*&ATCNCY£(YCN&ANTC*C$ACN£T&*QNA£*N(ATCN^$AJIUDHNUWGBDAOUSHND(AU*&)MYCNT£(*NCM$A)*&ATCNCY£(YCN&ANTC*C$ACN£T&*QNA£*N(ATCN^$AJIUDHNUWGBDAOUSHND(AU*&)MYCNT£(*NCM$A)*&ATCNCY£(YCN&ANTC*C$ACN£T&*QNA£*N(ATCN^$"
    talk lovely talk "Sorry, I feel like I blacked out for a moment. Did something happen?"
    $if this.skillCheck("tutorial_two_canon_orb", "orb", 20:
        talk orb talk "It wasn't canon. Don't worry."
    jump game_map