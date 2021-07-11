church:
    set global_actionsleft = 6
    set_screen default
    set_button button_church false
    set_button button_shop_intro true
    "The building would once have been the highlight of Bluehills. These days it is a shadow of its former self. The roof is unlit, the edges too. There is not enough manpower to keep the candles alight, nor reason to. Only a small congregation still huddles together at the far end of the great hall."
    $if this.skillCheck("church_magnificent_orb", "orb", 20):
        choice:
            talk orb talk "It had looked magnificent, once upon a time."
            "What happened?":
                talk orb talk "The war. The plague. The Anglian church was strong before the war began. It was a vital cog in the nations propoganda machine. Its preaching turned from peace to the glory of fighting alongisde your church friends against the evils of Imperial Brennenburg. The congregation bled till they were empty into the mud. Watched their town, their own cathedral burn under bombs. Watched their god do nothing when their families were butchered by the plague. Those who did not lose their life lost their faith. Those who did not lose their faith lost their trust in the institution. Those whose devotian to the tightly defined version of the Old faith the church preaches? They are who you see before you."
    talk orb talk "You've been here before. A long time ago, with your parents. They weren't devoutly religious, the organisation and formality of the Anglian church was always offputting for them. but they would come here with you a few times a year until you were old enough to choose."
    jump church_menu

church_menu:
    choice:
        "The choir and the congregation sing as one."
        "(Talk to the mysterious card shuffling woman)" $if !this.data.church_blackeyeMet:
            jump church_blackeyeIntro
        skillcheck church_menu_parentsFate_orb orb 80 "What happened to mother and father?" $if !this.data.global_parentsFateKnown:
            success "success roll!":
                "success!!!"
                jump church_parentsFate_success
            failure "fail roll!":
                "fail!!!!"
                jump church_parentsFate_fail
        "(Gaze into the window at the end of the cathedral)":
            jump church_window
        "(Leave - Bluehills)" $if this.data.church_blackeyeMet:
            jump game_map

church_parentsFate_success:
    talk orb talk "Foam leaks from a dry, cracked maw. Blood from an eye. You know where they are now. Corvidane rabies has an almost 100% death rate."
    $if this.skillCheck("church_parentsFate_success_begged_orb", "orb", 60):
        talk orb talk "You had begged them not to go to Lunden for bussiness until the plague was exorcised from its dying bones."
    set global_parentsFateKnown true 
    jump church_menu

church_parentsFate_fail:
    set global_parentsFateKnownFailed
    talk orb talk "Not here."
    jump church_menu

church_blackeyeIntro:
    set church_blackeyeMet true
    "She eyes you suspiciously."
    $if this.skillCheck("church_blackeyeIntro_suspicion_lovely", "lovely", 40):
        talk lovely talk "It's not genuine suspicion; she's glad you've approached her. She's been trying to get your attention since you arrived, but she can't help but be a drama queen."
        talk nasty talk "She wants to FUCK."
        talk lovely talk "She wants to *talk*."
        $if this.skillCheck("church_blackeyeIntro_suspicion_nasty", "nasty", 20):
            talk orb talk "She'll settle for either."
    
    choice:
        talk blackeye talk "Can I help you?"
        "(Sit next to her)":
            "A flicker of a smile appears on her face."
        "May I sit?":
            "A flicker of a smile appears on her face."
            $if this.skillCheck("church_blackeyeIntro_sit_lovely", "lovely", 20):
                talk lovely talk "She's glad you want to sit next to her, and gladder still that you felt you had to ask."
            talk blackeye talk "You may."
        "Sorry. I'll leave. Sorry.":
            talk blackeye talk "No. Stay. Please."
            $if this.skillCheck("church_blackeyeIntro_unwelcome_lovely", "lovely", 60):
                talk lovely talk "She's annoyed that her supicious glance actually made you feel unwelcome. She didn't mean for that to happen."

    $if this.skillCheck("church_blackeyeIntro_wine_lovely", "lovely", 20):
        talk lovely talk "She smells familiar. ’Chateux Saint-Arnoin’, a red wine. It clings to her like purfume."
        $if this.skillCheck("church_blackeyeIntro_wine_orb", "orb", 20):
            talk orb talk "It’s vintage nineteen-fifteen. Not expencive, but not cheap either."
        "There's something more. Oestrodil. She smokes it often. It gives the red wine a dry, minty undertone. It's rather intoxicating."

    $if this.skillCheck("church_blackeyeIntro_tired_orb", "orb", 20):
        talk orb talk "The fur around her eyes would still be black even if it were born white. She is tired. She is so tied. She runs a sleep debt that only goes up, and one day soon the collector will collect, and they will not be kind about it."

    choice:
        talk blackeye talk "Do you come here often? I don't recoginise you."
        "I don't think so, no.":
            "She eyes you curiously."
            choice:
                talk blackeye talk "And what brought you here today then?"
                "I don't know.":
                    choice:
                        talk blackeye talk "Hmm. It happens. One sometimes wanders somewhere with no real aim. Churchs are like magnets for us."
                        "What brought *you* here?":
                            talk blackeye talk "Searching for an escape. For faith, perhaps. I long for it. One would go so far to say lust for it, more than anything. Not that I'll find it here. I already made peace with my lack of faith in the trinity. I am merely attending service to bathe in the ambience, so to speak."
    choice:
        "She continues to stare into the coloured glass, fixated upon it as though she might find the Divine itself looking back at her through it."
        "It’s a nice church, in its own way.":
            talk blackeye talk "Certainly it has it's ambience, and a feeling of humility hung strongly in it like a miasma."
            $if this.skillCheck("church_blackeyeIntro_cathedral_lovely", "lovely", 20):
                talk lovely talk "She describes the cathedral as though she describes a fine wine."
            "She looks away from the window that seems to fascinate her so, and into *you*."
            $if this.skillCheck("church_blackeyeIntro_gods_orb", "orb", 20):
                talk orb talk "There are no gods to find in here."
            talk blackeye talk "And yet..."
            "She smiles. Her eyes flick shut, just a moment too slowly to hide the tears forming in them completely."
            $if this.skillCheck("church_blackeyeIntro_cries_lovely", "lovely", 40):
                talk orb talk "She cries a lot. Everyday."
            talk blackeye talk "I feel nothing."

    talk blackeye talk "Still, it's no surprise I haven't seen you here before, if indeed you rarely attend mass. I only moved to Bluehills recently. I was..."
    $if this.skillCheck("church_blackeyeIntro_melodramatic_lovely", "lovely", 60):
        talk lovely talk "This pause is intentional. She's being melodramatic."
    jump church_blackeyeIntroTwo

church_blackeyeIntroTwo:
    choice:
        talk blackeye talk "Unsatisfied with my previous home. The corpse of a dead, dying mining town did not suit me."
        "Dead *and* dying?":
            talk blackeye talk "The people are dead, the town dying."
            jump church_blackeyeIntroTwo
        "Corpse?":
            talk blackeye talk "That's what I said, yes."
            jump church_blackeyeIntroTwo
        "Where are you from? (Move on)":
            jump church_blackeyeBriarygrey

church_blackeyeBriarygrey:
    "She doesn't respond immedietly."
    talk orb talk "Smoking is strictly forbidden in the church, but were it not she would have lit a cigarette right now."
    talk blackeye talk "Briargrey. You've probably heard of it, albeit for rather unpleasent reasons."
    $if this.skillCheck("church_blackeyeBriarfrey_memory_orb", "orb", 40):
        talk orb talk "You remember hearing about it from the newspaper, or over the radio, perhaps."
        talk lovely talk "Ask her about it anyway. Don't assume you know the story better than her."

    choice:
        "The woman fiddles with one of her necklaces. A crystal of some sort. It's sides are worn from her incessent touching."
        "What happened to Briargrey?":
            talk blackeye talk "A mining incident. A bad one. The journalists, they all use the phrase accident, but it wasn't."

    choice:
        talk blackeye talk "It was the logical conclusion of a decade of corprate mismanagement. It was murder."
        "What was?":
            talk blackeye talk "Briargrey was once a prosperus coal mining town, until 1926, not long after the end of the war, when the spoil tip..."
            talk orb talk "A spoil tip is a mound of excavated rubble removed from the mine. It's worthless, and can end up piling quite high."
            talk blackeye talk "... which had, for various 'economic' reasons, been kept atop the hill on the north side of the town, collapsed and brought most of the hillside with it. One-hundred-eighty-seven dead townspeople were a headline in a newspaper, and then they were forgotten."

    $if this.skillCheck("church_blackeyeBriargrey_description_orb", "orb", 40):
        talk orb talk "The north side of the town, where the landslide met the community, is deserted. There is only rubble and ruin left behind. Depression bleeds from it. A grey and black pus that had found its way into the gut of everyone who lived there. The entire side of town had been fenced off once, now only the rotting posts stand testament to that, they had never been replaced. They do not need to be. People do not desire to trespass this place. The houses that once stood there are gone now. Small remnants of wall, perhaps the occasional chimney are all that remains of them. Who had lived there? What treasures, keepsakes and precious memories had they been decorated with? A tractor sits in the middle of the desolation, a trailer of rubble still towed behind it. It is rusted now, practically part of the environment. It was left there after the recovery effot ended. It was discarded like a contaminated scalpel after gut surgery."
     
    talk blackeye talk "Anyhow. I best be off."
    "She flashes her teeth."
    talk blackeye talk "It was nice to meet you, [name]."
    "She stands up and leaves, without so much as looking at you."
    talk orb talk "You should check your pocket. Trust me."
    "A card, one from her deck. An address is scrawled across it in ink. Apartment 1, 13 Rosethorn Lane."
    talk lovely talk "Wait, was that!? Magic!? Oh that! That! That dame!"

    $if this.skillCheck("church_blackeyeBriargrey_magic_orb", "orb", 40):
        talk orb talk "It was a magic trick, which while visually similar to actual magic, was *not* actual magic."
        talk lovely talk "A witch... how exciting!"
        talk nasty talk "I'd like to show her a trick or two. With my tongue, that is."
        talk lovely talk "Ugh. You are simply beastly, Nasty Girl."
        talk orb talk "You two are fucking idiots."
    jump church_menu

church_window:
    "There are three windows at the end of the cathedral. Each is a depiction of Queen Marigold Elasia Dawnsight. The Queen who bravely led the forces of the Great Crusade into the swirling darkness of the east to slay the demon that choked the world. The Anglian church holds that she was successful in this feat."
    $if this.skillCheck("church_window_volcano_orb", "orb", 20):
        talk orb talk "She wasn't. Her demon was a volcano, her crusade was farce, and she froze to death with a lung drowned in ash."

    choice:
        ""
        "I feel like I recognise her.":
            choice:
                talk orb talk "You used to see her everyday, or a statue of her, at least. She sat atop the 'Church of the Distant Saviour', facing out to sea, towards the continent. A hand unfurled southeasterly, as if trying to grab it, to save its soul. The Anglian church *loves* weird, nationalistic, misguided self agrandising. She didn't look like this though, the Elasia you knew was all empty inside."
                "She was what?":
                    talk orb talk "Erosion. The sea water tore the unprotected elements of her apart bit by bit, year by year, until the woman was gone and all that was left was a husk. The shell of a woman, empty, save for a few flecks of salt."

    jump church_window_menu

church_window_menu:
    choice:
        ""
        "(Look at the center window)":
            jump church_window_center
        "(Look at the left window)":
            jump church_window_left
        "(Look at the right window)":
            jump church_window_right
        skillcheck church_window_menu_queen_orb orb 60 "Who *was* Queen Marigold Elasia Dawnsight?":
            success "She has beutiful golden hair. In the windows depiction of her, at least.":
                talk orb talk "Anglias saviour. The *worlds* savior. So the church of Anglia would have you belive, at least. Prayer to the queen began as a one way transaction of good fortune to her, but as she failed to return and the dark age continued seemed to morph into pleading for her victory, pleading for her to bring good fortune and eventually begging for anything. As the queen so vaguely described meeting this being in ‘a grove of trees’, bluehills wood is now dotted with shrines dedicated to this fateful meeting. Some pagen worshipers believe that the queen was deceived by a woodland spirit known as the helpful traveller, though this is seen as a near heresy by the church. The Anglian church has sought out the grave of the queen for years, holding it not appearing as a sign she yet lives and to this day keeps the ash prince at bay. When the imperial church was established in anglia it mi gled with the anglian church, and the concept  of other pagen entities being avatars of the queen or of the prince become a core part of anglian belief. With the Dark Age ended, it seemed to believers that the queen had, finally, won her battle, cementing her status as a divine being. When the knowledge of the supervolcano was later brought to Anglia it was seen as proof of the queens claims, and wasit was merely being the site of the battle, where depending on interpretation,  the queen continues to battle for eternity, sometimes alongside the ghosts of her followers, or the queen rests peacefully and can be called upon for personal boons. Non Anglian sects of the church view their own leaders who took part in the crusade as saints, and tend to put more emphasis on the crusade as a collective moment of action, rather than the work of a singular person."
                jump church_window_menu
            failure talk orb talk "You might have to check a book for this one, sorry.":
                jump church_window_menu
        "(Move on)":
            jump church_menu

church_window_center:
    "Queen Marigold Elasia Dawnsight, holding the (at the time) flag of Anglia with pride. Behind her march the kings, queens, rulers, khans, sultanates of the nations that followed her on her quest. The blues of the Franks, the red of Brenneburg, the black of the Imperial Inquisition, the horned black tatters of the Azure Horde, the two headed sheep of muskovy... It's quite a procession. Ahead of Dawnsight a demon spews miasma into the sky. The cloud forms choking faces and dying crops. If the rest of the Anglian Churches holy belifes were this exciting the religion would probably have been more popular, alas they are not."
    jump church_window_menu

church_window_left:
    "Queen Marigold Elasia Dawnsight."
    jump church_window_menu

church_window_right:
    "The third window has a noticably different style to the others."
    $if this.skillCheck("church_window_right_lightning_orb", "orb", 40):
        talk orb talk "It was struck by a freak bolt of lightning. The glass was shattered and turned into lava, the metal left behind twisted and melted into ghastly shapes."
        talk nasty talk "That sounds great. They should have kept it like that."
        talk lovely talk "It does sound rather modern. I'll have to suggest the idea to papi for the estates windows."
        talk orb talk "The church didn't agree. It was quickly boarded up and then replaced."
    "It depicts Queen Marigold Elasia Dawnsight handing out bread to mammals flying the Anglian flag, while aiming a bolt of lightning at a group waving Imperial flags, and holding signs with 'conciouencess objecter', 'traitor' and 'i dont dig for victory' written on them."
    $if this.skillCheck("church_window_right_cartoon_orb", "orb", 20):
        talk orb talk "It was installed during the war. Apparently one of the patriotic cartoonists for the 'Bluehills Telegraph' was the only artist not currently having their lungs turned to mush by gas at the time."
    choice:
        "An embarassing display of wartime patriotism now sewn permently into the fabric of the church."
        "(Wave your fist at the Imperial flags) That's what you deserve, krauts!":
            talk lovely talk "Oh goodness, not in front of company please."
        "(Wave your fist at the Anglian flags) Choke on that bread, Anglian scum. (Look to the side as if there were someone there) I'm one of the good ones.":
            talk orb talk "W-what are you doing. There's no one there. Are you ok?"
        "(Wave one fist at each group of flags) Fuck flags! Fuck you! Fuck you fuck you fuck you!":
            talk nasty talk "Ha ha ha oh my gods shes having a breakdown this is amazing."
        "(Move on)":
            jump church_window_menu
    jump church_window_menu