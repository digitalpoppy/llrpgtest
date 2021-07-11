bluehills:
    set global_actionsleft = 7
    set_screen default
    set_button button_bluehills false
    set_button button_church true
    "In the distance the spire of Bluehills Cathedral towers above the city. It seems to call to you. It isn't spirituality that draws you to the cathedral, it's something else. A memory, perhaps. There's probably some kind of shop that you can find roof tiles in."
    talk lovely talk "And don't forget we want a copy of the lovely lady handbook!"
    talk orb talk "Do we though?"
    $if this.skillCheck("bluehills_handbook_orb", "orb", 20):
        talk orb talk "Besides, librarys exist. If you're going to waste your time, at least try not to waste your limited money too, hmm?"
        talk nasty talk "Or just steal it from the shop. The possibilities are endless."
        talk orb talk "Again. The library probably has the book for free." 
    jump bluehills_explore_menu  

bluehills_explore_menu:
    choice:
        "The city hums distantly. Wheezes, perhaps."
        "(Wander aimlessly through the streets)" $if !this.data.bluehills_streetsExplored:
            jump bluehills_streets
        "(Visit the brand new movie theater)" $if !this.data.bluehills_theaterExplored:
            jump bluehills_theater
        "(Check out the crashed airplane in the town center because it sounds cool as fuck)" $if !this.data.bluehills_airplaneExplored:
            jump bluehills_airplane
        "(Explore the park)" $if !this.data.bluehills_parkExplored:
            jump bluehills_park
        "(Move on to that compelling cathedral)" $if this.data.bluehills_parkExplored & this.data.bluehills_theaterExplored & this.data.bluehills_airplaneExplored:
            jump game_map

bluehills_streets:
    set bluehills_streetsExplored true
    "The streets of Bluehills feel familiar, for this is what most towns in Anglia look like. Row upon row of terraces housing, two to three floors tall. The occasional two hundred year old antique or post war block of concrete hiding a twisted rebar nervous system punctuating the urban oblivion. They feel familiar, but they arent'. These are not roads you have walked before, if indeed you ever have walked through a town before. They are not friends. The pointed roofs are molars, the factory chimmneys canines, the cobbled roads tongues, the brown water running between the flagstones spit. You are their meal. Welcome to civilisation. Enjoy your long digestion."
    jump bluehills_explore_menu

bluehills_theater:
    set bluehills_theaterExplored true
    "[THETER DESCRIPTION]"
    "The lady in the ticket booth eyes you sleepily. She can already tell you're an oogler, not a buyer. She's only had this job for a month, but already it's instinct. She fears how her psyche will be mangled and changed after a year in this job."
    jump bluehills_theater_menu

bluehills_theater_menu:
    choice:
        "The wall to the side of the theater is decorated with posters for the meager selection of films being played once daily."
        "(Look at the poster 'Unedited Footage of a Teatime')":
            jump bluehills_theater_teatime
        "(Look at the poster 'The Unshot Bullet Murders')":
            jump bluehills_theater_murder
        "(Look at the poster, wait, there isnt a poster here, it's just an empty frame)" $if !this.data.bluehills_theater_blankSeen:
            jump bluehills_theater_blank
        "(Move on)":
            jump bluehills_explore_menu

bluehills_theater_teatime:
    choice:
        talk nasty talk "Looks shit, right?"
        "Extremelly.":
            talk lovely talk "Tsk tsk. You two wouldn't know good storytelling if it hit you in the face."
            talk nasty talk "Don't tempt me."
        "I think it looks good. I love watching little ladies sip their teas and nibble their cakes without ever finishing them.":
            talk nasty talk "Pervert."
    jump bluehills_theater_menu

bluehills_theater_murder:
    talk nasty talk "It's about a serial killer who kills their victims by mannually stabbing them to death with a bullet. It's great. Based on a true story too."
    $if this.skillCheck("bluehills_theater_murder_real_orb", "orb", 20):
        talk orb talk "It absolutely is *not* based on a true story."   
    choice:
        talk lovely talk "Sounds ghastly. This kind of crassness is why the theater will never take off."
        "Agreed, it's filth. (Shake your head dissaprovingly)":
            talk lovely talk "Personally, I support the lovely code."
        "That sounds like it bops. I love ghastly movies.":
            talk lovely talk "Tsk."
    jump bluehills_theater_menu:

bluehills_theater_blank:
    set bluehills_theater_blankSeen true
    "It is a blank poster frame. A poster should be here, but it isn't."
    choice:
        talk orb talk "Riviting. Can we look at something else now?"
        "Okay. (Move on)":
            talk orb talk "Thank you."
        "No. (Keep looking at the empty poster frame)":
            choice:
                talk orb talk "Good good. Let's get g- wait, did you say no? *Why*?"
                "It might get interesting.":
                    choice:
                        talk orb talk "It really wont."
                        "(Keep looking at the empty poster frame)":
                            "Paper, a previous poster, is still attached to the top left corner of the frame. It is yellowing, and it feels wrong. This isn't just an empty poster frame, it's something more."
                            $if this.skillCheck("bluehills_theater__blank_poster_nightmare", "nightmare", 80):
                                choice:
                                    talk nightmare talk "It's you, isn't it?"
                                    "Who is this?":
                                        "..."
                                        talk orb talk "Please. Let's go."
                                    "It's me. (Nod)":
                                        talk orb talk "Please. Let's go."
                            talk nasty talk "Boooooored."
                            talk lovely talk "Mhm. I do have to conccur with my comrades. This is rather dull. Might we quit this place?"
                            talk nasty talk "I am literally begging you to stop using entire paragraphs where one word will suffice."
                            talk lovely talk "Hmm? Don't you mean 'sut'?"
                            talk nasty talk "Sut..."
                        "(Move on)":
                            talk orb talk "Thank you."
                "I'm just messing with you, sorry.":
                    talk orb talk "Whatever. Let's stop now."
    jump bluehills_theater_menu

bluehills_airplane:
    set bluehills_airplaneExplored true
    "It's less of an airplane and more of a twisted fauximily of an airplane. It has wings, it has a tail, it has propellers, bent as they are, but none sit in their rightful place."
    jump bluehills_airplane_menu

bluehills_airplane_menu:
    choice:
        ""
        "What kind of plane is it?":
            talk orb talk "Pidgeon MK.II. Entered service in 1922. This specific specimin exited service the same year. She can be outfitted with two 250LB bombs under the wings, and a third 500LB bomb under the chasis, if one wanted to become the slowest, easiest, most explosive target in history... But no. This specific plane was only ever used as a fighter."
            $if this.data.skillCheck("bluehills_airplane_type_bomber_orb", "orb", 40):
                talk orb talk"It's pilot refused to sully themselves with anything less. Probably for the best, it would have blown half this street to dust if it had been loaded with explosives. Fighter pilots, and indeed anyone with honour tends to look down on bomber pilots now that strategic bombing has been birthed, kicking and screaming, into the world. Supposadly the strategy is to kill enough civilians that your opponent surrenders. In reality it turns into a bloody example of the sunk cost fallecy. No one wants their neighbours to have been blown into a fine mist in vain."
            jump bluehills_airplane_menu
        "Why is it still here?":
            talk orb talk "The council planned for a statue on this exact spot. The god of war giveth one for free."
            jump bluehills_airplane_menu
        "Why are *we* here?":
            talk orb talk "Because the second one of your neurons remembered there was a crashed airplane here you thought it was 'cool as fuck' and deigned it worth a visit. That's the entire reason. I wish I could give you a spiel about how you felt inexprbly drawn to it because of some long distant memory or its physical representation of the mammel condition, but no, you literally just thought it was cool."
            $if !this.data.bluehills_airplaneClimb:
                talk nasty talk "It is cool as fuck, to be fair. We should climb on it."
                choice:
                    talk lovely talk "That would be *highly* disrespectful, Nasty Girl, this is a war memorial, you realise?"
                    "Sounds good, let's do it. (Approach the airplane)":
                        jump bluehills_airplane_climb
                    "I'm going to try to avoid desecrating any graves until I can remember if I respect the dead or not, but thank you for the suggestion, Nasty Girl.":
                        talk nasty talk "Pussy."
                        jump bluehills_airplane_menu
            else:
                jump bluehills_airplane_menu
        "(Move on)":
            jump bluehills_explore_menu

bluehills_airplane_climb:
    set bluehills_airplaneClimb true
    talk orb talk "You realise this isn't a good idea, right?"
    "You're right, this is a GREAT idea.":
        talk nasty talk "Hahahahaha nice one. Orb, i'm going to tail-whip you, nerd!"
        talk orb talk "Oh to be able to sigh..."
        talk lovely talk "Allow me. Sighhhh."
    "Hmm, why not? Make your argument.":
        choice:
            talk orb talk "You could slip and fall, end up in the newspaper for disrespecting the war dead, someone could... throw something at... look, just dont do it, okay?"
            "Some good points, well argued, let's not do this. (Abandon your inane bullshit)":
                talk nasty talk "Gods you suck so bad. Ugh."
                talk orb talk "Thank you for seeing sense."
                jump bluehills_airplane_menu
            "I'm doing it. (Do it)":
                talk orb talk "Whatever. Try not to hit your head too hard when you fall over, I'd rather keep my remaining memory intact."
    choice:
        talk nasty talk "Come on! Enough talking! Let's do it!"
        skillcheck bluehills_airplane_climb_climb_nasty nasty 60 "(Climb onto the wrecked plane and just respect the war dead for a bit)":
            success "[SUCCESS]":
                jump bluehills_airplane_climb_success
            failure "[FAILURE]":
                jump bluehills_airplane_climb_failure
        "I'm chickening out at the last moment, sorry Nasty Girl. (Abandon your inane bullshit at the last second, like a pussy)":
            talk nasty talk "I have no words for how dissapointed I am. Fuck you for edging me like this."
            jump bluehills_airplane_menu

bluehills_airplane_climb_success:
    talk nasty talk "This is great, right?"
    "You bet! WAHOOOOOO!":
        talk nasty talk "WAHOOOOOOO!"
        choice:
            talk lovely talk "Please, not shouting. It echoes in here."
            "(Climb back down)":
                talk orb talk "I hope shouting 'wahoo' was worth the effort of climbing a few more rungs up the ladder to hel."
                talk nasty talk "It was *so* worth it."
    "I am underwhelmed.":
        choice:
            talk nasty talk "Grr."
            "(Climb back down)":
                talk orb talk "I hope being underwhelmed was worth the effort of climbing a few more rungs up the ladder to hel."
    jump bluehills_airplane_menu

bluehills_airplane_climb_failure:
    choice:
        talk nasty talk "No. We looked cool. We looked cool right, Ghost?"
        "(Nod) We looked cool.":
            talk nasty talk "Fuck yeah we did."
        "We didn't look cool. We looked like morons in front of everyone. That idea sucked, Nasty Girl.":
            talk nasty talk "Bah. Forget it. From now on I'll keep my great ideas to myself I guess."
            talk lovely talk "Oh if only."
    jump bluehills_airplane_menu



bluehills_park:
    set bluehills_parkExplored true
    "[PARK DESCRIPTION]"


    talk nerd talk "Hey! You live in the cottage by the woods don't you? I was watching you this morning. I mean, I *saw* you this morning. I wasn't watching you. Except for the brief moment I was. I wasn't *looking* for you, is what I mean."
    choice:
        talk orb talk "Abort conversation. Get out of here. This is weird."
        "I have go to. (Point randomly) Over there. To do stuff.":
            talk nerd talk "O-oh. Okay. Sorry."
            jump bluehills_nerd_escape
        "Woahhhhh! What's that behind you!? (Run away)":
            "He spins around wildly."
            "[ESCAPE]"    
            jump bluehills_nerd_escape            
        "Woahhhhh! What's that behind you!? (Check he's looking away and *then* run away)":
            talk nerd talk "Huh? What? Why are you staring at me?"
            "[ESCAPE]"  
            jump bluehills_nerd_escape   
        "I live there, yes. (Nod)":
            "[INTRO CONVO INCLUDING A DISCUSSION]"
            "The Weird Nerd turns to you once more."
            talk nerd talk "You should get that hole in your roof fixed, by the way!"
            talk orb talk "You really should."
            jump bluehills_explore_menu

bluehills_nerd_escape:
    talk lovely talk "That was a close one. We could have been stabbed!"
    talk nasty talk "*You* could have been stabbed. I'd like to see anyone try to beat me in a knife fight. I fight *so* dirty."
    talk orb talk "Noone was going to get stabbed, but that was a little weird. Regardless, we should press on, hmm?"
    jump bluehills_explore_menu