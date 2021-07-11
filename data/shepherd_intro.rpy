shepherd_intro:
    set global_actionsleft = 8
    set_screen default
    set_button button_shepherd_intro false
    set_button button_bluehills true
    "There are four cottages on the lane, roughly identical, though only yours has a tiled roof. In the distance, perhaps two or three miles away and just over the hills to the north, you can see the spire of Bluehills cathedral. Behind you there is a thick woodland. It seems to stretch off into the distance forever, though obviously it doesn't. Stretching behind your cottage, and along most the length of the road is a sheep field. The lazy animals munch on their grass quietly. The paddocks fence is damaged, and a pile of lumber sits by it. This would patch up your ceiling nicely."
    $if this.skillCheck("fields_intro_brokenFence_orb", "orb", 25):
        talk orb neutral"The fence was broken during the night. A rival farmer hoping to lose the farm a few sheep. Her plan would have worked were not sheep so passive and content as to look at freedom as unecessary. They have all the grass they could ever need right here."
    $if this.skillCheck("fields_intro_brokenFence_nasty", "nasty", 25)
        talk nasty talk "I've broken my fair share of fences on behalf of paying farmers. Classic."
    "The broken fence is guarded by a tall, wirey goat who is trying very hard not to look like they are eying you suspiciously. It would be cliche, rude even, to say that their eye patch is their defining feature, but it is."
    talk lovely talk "You should probably say hello. Tis' only polite."
    talk nasty talk "They're hot, in a scary way I mean. Wink at them."
    choice:
        talk orb talk "Just don't scare them off. They might be able to help us get our bearings, gods know we need them."
        "Good morning, friend. (Wave at the Goat)":
            jump shepherd_intro_goodmorning
        "(Wink smuttily)":
            "The goat stares past you, unblinking."
            choice:
                talk lovely talk "I don't know what you expected. Just say good morning, like a normal person."
                "Good morning, friend. (Wave at the Goat)":
                    jump shepherd_intro_goodmorning

shepherd_intro_goodmorning:
    talk shepherd talk "Morning."
    "The goat chews on some straw. They're a good half a foot taller than you, and seem to be composed entierly of angles. An abstract painting entierly in grey. They're unassuming, and yet..."
    $if this.skillCheck("shepherd_intro_goodmorning_levithan_orb", "orb", 20):
        talk orb talk "Not far from your previous home was a beach. Not a nice one, one of those pebble ones that hurt your feet and make for poor sandcastles. A few years ago you were walking along it, just as the sun was rising, only to find a barn sized ribcage washed up on a grey shore, every centimeter clad in barnicles and seaweed. It filled you with some primal fear, some great dread. This thing did *not* belong there. It belonged deep underwater, deep under millenia of rock with the rest of the long dead levithans corpse. The murderer doesn't belong here among the daffodils and sheep, they belong somewhere else. Somewhere among mud and twisted metal and smoke. They stand in front of you like a bloodstain on a wedding dress."
    $if this.skillCheck("shepherd_intro_menu_smalltalk_lovely", "lovely", 20):
        talk lovely talk "I get the impression they don't want to talk to you. Or if they do, they'd rather it weren't small talk."
    choice:
        talk shepherd talk "Did you want something?"
        "What are you doing here?":
            talk shepherd talk "I'm a shepherd. I look after this flock."
            "They gesture to the sheep, who munch on their grass, content as can be."
            talk shepherd talk "Keep them fed. Keep them safe. Milk them when they need milking."
            $if this.skillCheck("shepherd_intro_goodmorning_milk_orb", "orb", 20):
                talk orb talk "Sheep based agriculture is demeaning and cruel. The beasts should be free."
            talk nasty talk "But milk tastes so gooooooooood..."
    choice:
        talk shepherd talk "That's about it."
        "No, I meant why are you here. You should be somewhere among mud and twisted metal and smoke.":
            talk shepherd talk "Wh- what?"
            $if this.skillCheck("shepherd_intro_goodmorning_wounded_lovely", "lovely", 40):
                talk lovely talk "I don't know *why* you said that, but it wounded them, and deeply. Don't say things like that to them. Or anyone. Just talk normally, please."
            $if this.skillCheck("shepherd_intro_goodmorning_belongThere_orb", "orb", 60):
                talk orb talk "They've seen the place you speak of. The mud has stained their hair, the twisted metal has cut their knees, the smoke has choked their lungs. They know they belong there, but they wish they didn't."
            choice:
                talk lovely talk "You should apologise, make an excuse. Be normal, please."
                "Sorry, I was thinking about... a poem.":
                    jump shepherd_intro_menu
        "(Move on)":
            jump shepherd_intro_menu

shepherd_intro_menu:
    choice:
        "The murderer chews their straw."
        "I don't remember you.":
            jump shepherd_intro_remember
        "What's with the, y'know... (Point at your eye) Eye?":
            jump shepherd_intro_eye
        "Do you enjoy your job?":
            jump shepherd_intro_job
        "Weird question I know, but where are we?":
            jump shepherd_intro_whereAreWe
        "(Move on)" $if this.data.shepherd_intro_whereAreWe:
            jump shepherd_intro_lumber

shepherd_intro_remember:
    talk shepherd talk "Why would you? I haven't spoken to you. Besides, you've only lived here... what, for four or five days now perhaps?"
    $if this.skillCheck("shepherd_intro_menu_pawtsmouth_orb", "orb", 40):
        talk orb talk "Four days. You just moved here from Pawtsmouth, about twenty miles to the southeast. The city is a bustling naval base, your new home feels so quiet in comparison. No fog horns, no machinery. You're lucky work came up in Bluehills, the air pollution that lingered outside your old apartment was less than beneficial for you."
    jump shepherd_intro_menu

shepherd_intro_eye:
    talk lovely talk "Please no."
    choice:
        talk shepherd talk "Doesn't work."
        "(Nod) Doesn't work.":
            talk shepherd talk "Mhm."
        "Why?":
            choice:
                talk shepherd talk "Because it's broken."
                "That makes sense. Thanks.":
                    talk shepherd talk "Mhm."
                    $if this.skillCheck("shepherd_intro_menu_eye_orb", "orb", 40):
                        talk orb talk "A Hyeana went at it with a knife. It was grisly."
                        "You can't see it, the wound, but it's there. It radiates a pain that would cripple you, but to them it is an ocassional snarl, a grimace, a twitch in the corner of their singular working eye."
    jump shepherd_intro_menu

shepherd_intro_job:
    talk shepherd talk "I'm good at it."
    $if this.skillCheck("shepherd_intro_menu_goodAtJob_lovely", "lovely", 20):
        talk lovely talk "That was a no."
    jump shepherd_intro_menu

shepherd_intro_whereAreWe:
    talk shepherd talk "We're in the time between catastrophes. The precipise. The edge of armageddon. Oceania nearly has the bomb and the Soviet Republic can't be far behind now. We are all going to die."
    jump shepherd_intro_whereAreWe_menu

shepherd_intro_whereAreWe_menu:
    choice:
        "They stare at you without looking at you."
        "Oceania?":
            jump shepherd_intro_oceania
        "The Soviet Republic?":
            jump shepherd_intro_sovietRepublic
        "The Great War?" $if this.data.shepherd_intro_oceania:
            jump shepherd_intro_war
        "The supervolcano?" $if this.data.shepherd_intro_soviet:
            jump shepherd_intro_volcano
        "The bomb?":
            jump shepherd_intro_bomb
        "If I were one of these superpowers I would simply give peace a chance. (Nod wisely)" $if this.data.shepherd_intro_soviet && this.data.shepherd_intro_oceania && this.data.shepherd_intro_bomb:
            jump shepherd_intro_peace
        "I meant the question 'where are we?' more literally. (Move on)":
            jump shepherd_intro_whereAreWeTwo

shepherd_intro_oceania:
    set shepherd_intro_oceania true
    talk shepherd talk "The archipeligo nation in the south pacific. I refuse to belive you don't know of it. They stayed neutral during the great war which, as it turned out, was highly profitable for their arms manufacturing industry."
    "They spit and mutter something under their breath."
    $if this.skillCheck("shepherd_intro_oceiana_bitter_orb", "orb", 40):
        talk orb talk "They're bitter about how they choked on gas in the mud while the worst someone else had to choke on was an all expences paid dinner after another arms deal."
    talk shepherd talk "They're the greatest superpower in the world now, besides the Soviets of course."
    "They gaze towards Bluehills."
    talk shepherd talk "The European Powers had their time in the sun, and all they were rewarded with were third degree burns. Molten flesh shedding from their bones. Eyes melting from their sockets and into seeping betwixt their chapped lips."
    talk lovely talk "Do they *have* to be so descriptive?"
    talk nasty talk "This bops. We should ask them to describe more gross things."
    talk lovely talk "Please don't, I might throw up."
    talk nasty talk "Gross. That bops."
    jump shepherd_intro_whereAreWe_menu

shepherd_intro_sovietRepublic:
    set shepherd_intro_soviet true
    talk shepherd talk "Still not caught up huh? They're not called Musckovy anymore, it's The Soviet Republic now. Nation stretches from Europa to the Pacific. In the middle sits the dead zone, the supervolcano. Dead zone is an apt description of the entire country. Wouldn't want to live in that warzone."
    $if this.skillCheck("shepherd_intro_sovietRepublic_orb", "orb", 20):
        talk orb talk "The civil war actually ended a while ago, but western propoganda tends to exagarate the conditions of the republic."
    jump shepherd_intro_whereAreWe_menu

shepherd_intro_war:
    "They squint. Your previous questions were stupid, but not necesserily abnormal. Not knowing about the war is *weird*. Did you just wake from a coma, they wonder."
    talk shepherd talk "The Great War between the Allies and Imperial Brenneburg. We won. Technically."
    $if this.skillCheck("shepherd_intro_war_meloncholy_lovely", "lovely", 20):
        talk lovely talk "The melencholy is palpable."
    $if this.skillCheck("shepherd_intro_war_won_orb", "orb", 20):
        talk orb talk "No one *won* the war. Some people were just lucky enough to die in it, instead of wither on."
    talk shepherd talk "Let's talk about something else, hmm?"
    $if this.skillCheck ("shepherd_intro_war_touchy_lovely", "lovely", 20):
        talk lovely talk "The war is a touchy subject for them, despite their interest in history and politics."
    jump shepherd_intro_whereAreWe_menu

shepherd_intro_volcano:
    talk shepherd talk "The one that exploded and caused the Dark Age. It's located right in the middle of Siberia. Still spews toxic gas to this day, hence the dead zone. There's been a few expeditions into it, using... clever technology."
    $if this.skillCheck("shepherd_intro_volcano_technology_lovely", "lovely", 20):
        talk lovely talk "They don't actually know what the technology is."
    talk shepherd talk "But none have ever gotten far into it. It's rather expansive."
    $if this.skillCheck("shepherd_intro_volcano_siberia_orb", "orb", 40):
        talk orb talk "It's exactly 832.41 miles across."
    "They smirk."
    talk shepherd talk "Some say the ancient city of the Star Gods sits in the center. Idiots."
    $if this.skillCheck("shepherd_intro_volcano_rude_lovely", "lovely", 20):
        talk lovely talk "They think they're smarter than those people. Rude."
        set shepherd_intro_smugOrbVolcano true
    $if this.skillCheck("shepherd_intro_volcano_starGods_orb", "orb", 70):
        talk orb talk "The city of the Star Gods *does* sit in the center. Or did. It was essentially atomised when the cities volcanic reactor exploded, which your foolish civilisation has interpreted as a natural cause. Idiots."
        $if this.data.shepherd_intro_smugOrbVolcano:
            talk lovely talk "Orb thinks they're than those people. Rude."
    jump shepherd_intro_whereAreWe_menu

shepherd_intro_bomb:
    set shepherd_intro_bomb true
    talk shepherd talk "The atom bomb. It's not a secret that the two superpowers are working on them. Oceania would rather see the world burn in nuclear fire than surrender to communism, and the communists feel the same about the free market."
    $if this.skillCheck("shepherd_intro_bomb_dates_orb", "orb", 20):
        choice:
            talk orb talk "Oceania tests their first atom bomb in 1932. The Soviet Republic in 33. The Central Afrikan Corvid Commune tests one in 1937. Ming, Anglia and Frankreich don't build any until the 40s."
            "Do they ever use them on eachother?":
                talk orb talk "No. They are only ever used recreationally."
            "A chilling vision of the future. Let us not dwell on it any further."
                talk orb talk "If you say so."
    jump shepherd_intro_whereAreWe_menu

shepherd_intro_peace:
    talk shepherd talk "Uhuh. That's not going to happen. I'm predicting a war over Cawrea, maybe Manchuria by the end of the decade."
    $if this.skillCheck("shepherd_intro_peace_manchuria_orb", "orb", 40):
        talk orb talk "Almost true. The two powers fight a proxy war over Manchuria in the late 40s. The prediction is almost meaningless though, this shepherd throws so many ill informed prophesies out that one is bound to be *almost* right eventually."
    jump shepherd_intro_whereAreWe_menu

shepherd_intro_whereAreWeTwo:
    choice:
        talk shepherd talk "Don't you live here? I assumed you would know where we are, hence my greater ramblings."
        "I do live here, but it's good to check.":
            talk shepherd talk "This is Daffodil Lane. A few miles out of Bluehills proper. Behind me is my sheep field. That is all."
            choice:
                "They seem less interested in conversing now that they can't ramble about politics and history. The spark is gone from their eye once more."
                skillcheck shepherd_intro_whereAreWe_whatsUp_orb orb 80 "What is up with them?": 
                    success talk orb talk "They only became a shepherd after the war. Working with the animals brings them a peace, albeit one rusted with ennui. They think of the blissfull ignorence of a sheeps existence. They think of their prehistoric ancestors. They may have bitten and scratched and squeaked, but they did not drop firebombs on civilians from the heavens."
                        $if this.skillCheck("shepherd_intro_whereAreWeTwo_worldAffairs_lovely", "lovely", 20):
                            talk lovely talk "Learning about world affairs makes them feel prepared for whatever they think is going to happen. It makes them feel in control of their own destiny, rather than a pawn in a game they don't realise is being played."
                    failure talk orb talk "I don't know."
                        $if this.skillCheck("shepherd_intro_whereAreWeTwo_staring_lovely", "lovely", 20):
                            talk lovely talk "You should probably stop staring. They've noticed."
    set shepherd_intro_whereAreWe true
    jump shepherd_intro_menu

shepherd_intro_lumber:
    "The lumber piled up next to the broken fence calls to you."
    talk nasty talk "It's saying 'steal me steal me steal me'."
    talk orb talk "It isn't. Lumber doesn't talk, actually."
    choice:
        "The Murderer chews on the straw and peer at you from under the rim of their straw hat. They say nothing."
        skillcheck shepherd_intro_lumber_borrowLumber_lovely lovely 60 "(Ask if you can borrow some of their lumber)":
            success "The Murderers gaze shifts to the lumber, for just a moment."
                jump shepherd_intro_lumber_success
            failure talk shepherd talk "No."
                jump shepherd_intro_lumber_fail
        skillCheck shepherd_intro_lumber_stealLumber_nasty nasty 60 "(Steal some lumber)":
            success "Impressivley, you actually manage it."
                jump shepherd_intro_stealLumberSuccess
            failure "You aren't sure exactly how it happened, but you're in a headlock."
                jump shepherd_intro_stealLumberFail
        "I'll get out of your way. (Leave)":
            "The murderer chews on the straw in a way that registers as an aknowledgement devoid of interest."
            jump game_map

shepherd_intro_lumber_success:
    "They eye the lumber, and then you. Their eyes are still and unblinking as always, but you can see cogs turning behind them."
    talk lovely talk "They're considering giving it to you purely so you stop talking to them. A little offensive, but I suppose it works."
    talk shepherd talk "Fine. Take a few planks. I have more than enough anyway."
    set global_hasTimber true
    jump game_map

shepherd_intro_lumber_fail:
    choice:
        talk nasty talk "Mission failed. We'll get it next time, and by next time I mean right now. Steal that shit."
        skillCheck shepherd_intro_lumber_fail_stealLumber_nasty nasty 80 "(Steal some lumber)":
            success "Impressivley, you actually manage it."
                jump fields_stealLumberSuccess
            failure "You aren't sure exactly how it happened, but you're in a headlock."
                jump fields_stealLumberFail
        "I'm not going to steal the lumber, sorry Nasty Girl. (Leave)":
            jump game_map

shepherd_intro_stealLumberSuccess:
    talk nasty talk "Told you, crime always pays."
    choice:
        "There's enough lumber there that a few missing pieces will be hard to notice, so long as no suspisions are aroused."
        "Hey, check out this lumber I didn't steal from you. (Show The Murderer the lumber you just stole from them)":
            jump shepherd_intro_redHanded
        "We should probably get out of here. (Leave)":
            set global_lumber_stoleLumber true
            set global_lumber_hasLumber true
            jump game_map

shepherd_intro_redHanded:
    set global_lumber_redHanded
    "You wake up some time later. You don't even remember the punch."
    talk orb talk "I'm sorry but I really don't know what you expected."
    choice:
        talk shepherd talk "You're awake. Good. Get out of here."
        "But!":
            talk shepherd talk "Stop talking. Stop stealing. Go."
        "Ok. Sorry. Sorry."
            talk shepherd talk "Go."
        "(Back away silently)":
            "They eye you suspiciously."
    "They look at you like you're dirt. Less than dirt. It's not even in a sexy way."
    choice:
        talk lovely talk "You're not going to get on their good side anytime soon. Let them calm down first. See what happens when we listen to Nasty Girl?"
        "Let's get out of here. (Leave)":
            jump game_map

shepherd_intro_stealLumberFail:
    talk nasty talk "Nice."
    talk lovely talk "I am above commenting verbaly on such matters."
    talk shepherd talk "Please. Go away."
    $if this.skillCheck("shepherd_intro_stealLumberFail_shepherdHates_lovely", "lovely", 20):
        talk lovely talk "They really hate you. This is what happens when you listen to Nasty Girl."
    choice:
        talk orb talk "We should just get out of here."
        "Agreed. (Leave)":
            jump game_map