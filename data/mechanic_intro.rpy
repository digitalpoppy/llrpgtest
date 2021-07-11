mechanic_intro:
    set global_actionsleft = 3
    set_screen default
    set_button button_mechanic_intro false
    set_button button_blackeye_apartment true
    set_button button_home_fixHouse true
    set_button button_brokenVase true
    set_button button_book_handbook true
    set_button button_book_history true
    "'GARDG', the garage's sign proudly states, despite its disrepair. It's a rather nondescript building, and like all the best workshops it is grimey, scary and full of health code violations. Inside you find a tall, musclular Hyeana sorting through a veritable grab bag of tools. She must be about twenty-eight or so, maybe thirty, and she's terrifying. A practical violence golem. She is The Raven."
    choice:
        talk nasty talk "Yeen!"
        "Excuse me?":
            choice:
                talk nasty talk "Yeen!"
                "Is Nasty Girl okay?":
                    $if this.skillCheck("mechanic_intro_slur_lovely", "lovely", 60):
                        talk lovely talk "Yeen. It's short for Hyeana. It isn't a slur, but it's still kind of a weird thing to say to someone you've never spoken to before, so don't."
                    talk nasty talk "Yeen."
                    choice:
                        talk lovely talk "Can we all agree Nasty Girl has been licking too much paint and end this train of thought? Please?"
                        "Agreed. Let's never speak of this again":
                            talk lovely talk "Thank you."
                        "Yeen!":
                            talk nasty girl "Yeen!"
                            talk lovely talk "Forget it. I'm going to go drink some wine. You two have your... fun."
                        "\"Yeen!\"":
                            set mechanic_intro_saidYeen true
                            "The Raven raises an eyebrow. You *did* mean to say that out loud right?"
                "Okay. Moving on. (Move on)":
                    talk lovely talk "Wise decision."
        "I'm just going to ignore whatever that was.":
            talk lovely talk "Wise decision."
    "The Raven chews a ciggarette between her teeth as she watches you. It isn't even lit, she just does this sometimes. Her teeth are shiny, like knives. Her teeth are pointed, like knives. "
    talk nasty talk "Jelous, Lovely Lady?"
    talk lovely talk "..."
    "She's wearing a filthy, oil stained vest. The kind of vest only worn by a man who's about to hurl a half empty whisky bottle at your head or a lesbian who could lift a truck. The lack of sleeves show off her arms. Muscular, with a nasty scar runs across the right one. It cuts a black fur-tattoo of a heart in half."
    $if this.skillCheck("mechanic_intro_scar_orb", "orb", 20):
        talk orb talk "The scar is from a fall in Tennenburg Wood. A nasty cut from an unfortunatly placed stone. She lets people assume it was the work of a bullet, which it was, albeit indirectly. The tattoo came after the injury. She thought it made a statement, and while it does, it's not one as deep as she thinks."
    $if this.skillCheck("mechanic_intro_scar_lovely", "lovely", 20):
        talk lovely talk "Not all of her scars are visible. Inside she has been lashed with a whip of nine tails. Inside she is *being* lashed with a whip of nine tails."
        talk nasty talk "nOt aLL sCaRs aRe VisIbLe!!! That is *so* cliche, could you *get* any more embarassing, Lovely Lady? Uuuuuuuuh duuuuuuh beauty is only skin deep! uuuuuuuh bluuuuuuuh a rose by any other name whatever the fuck. Fuck off."
        talk lovely talk "Tsk. Keep that attitude up and you'll have a few visible scars, Nasty Girl. I am *highly* trained in fencing, you know?"
    "She smells of tobacco, sweat and engine oil. The black fluid is practically her blood."
    $if this.skillCheck("mechanic_intro_motorcycle_orb", "orb", 60):
        set mechanic_intro_guessedMotorcycle true
        talk orb talk "She drives a Ratzubishi 4vk: A recon motorcycle that rose to promenence in the final two years of the war. It was designed by the Anglian Militarys R&D team to be durable and hardy, so naturally she spent most of her time at the front repairing it. She has long since stopped noticing the scent of engine oil."
        $if this.skillCheck("mechanic_intro_job_orb", "orb", 40):
            talk orb talk "She used to run messages from forward positions to the trenches during radio blackouts. There's a bullet hole right through the framework. It's superficial, certinaly the motorcycle never noticed, but she still hears the crack of the Maus Gewehr 23 ring inside her head from time to time. She was thrown from the bike by the shock, assumed it junked, and spent the night crawling through the broken remains of Tennenburg Wood to the forward command post, bleeding from a wound from the fall the whole way. By the time morning rolled around the Imperial forces has disengaged and fallen back (they did that a lot in the final year of the war, victories were rare for them, but a cornered beast fights the most ferally), and the bike was recovered. The forward command post would not have been able to break the enemy line without the coordinates she had delivered them, and so she was gifted the cycle in lieu of a medal. She prefered it that way. Medals are the military equivilent of a 'good girl' certificate at school, and bikes get girls."
    "She is yet to look up at you for more than a brief flash, and when she does her eyes display little in the way of emotion, not because she is devoid of them, but because she has learnt to conceal them. She's measuring you up, as she does all new faces."
    $if this.skillCheck("mechanic_intro_judges_lovely", "lovely", 20):
        talk lovely talk "She's waiting for you to speak before she judges you. She appreciates it when people are straight to the point."
        $if this.data.mechanic_intro_saidYeen:
            talk lovely talk "Though, given that you said 'Yeen' out loud to her as soon as you approached her... it's not looking good."
    $if this.skillCheck("mechanic_intro_teeth_nasty", "nasty", 20):
        talk nasty talk "She appreciates girls she could break in two. Girls like you, weakling."
    $if this.skillCheck("mechanic_intro_poster_orb", "orb", 80):
        talk orb talk "You recognise her, faintly, at least. A torn, damp poster on a train station in Pawtsmouth. 'Save fuel! Your petrolium helps her deliver victory!', it says, above an illustration of a large Hyeana driving a motorcycle through darkness. A bag of envelopes sitting comicly in the side carrige. A drop of rain has melted away a spot on her left arm."
    talk lovely talk "Like a Soviet Artika on an urgent mission it's icebreaker time! You should ask her about her tattoo!"
    jump mechanic_intro_menu

mechanic_intro_menu:
    choice:
        "The Raven looks up from her rather nebulous work, albeit only briefly. She's waiting for you to talk."
        "I need some tools. For fixing things. Roof broke." $if !this.data.hasHammer:
            jump mechanic_intro_tools
        "Do you sell anything that could be used to get blood out of carpet? I'm not covering up a murder by the way." $if this.data.global_needStainRemover:
            jump mechanic_intro_blood
        "Can I ask about your tattoo?":
            jump mechanic_intro_tattoo
        "So. What's it like being a mechanic."
            jump mechanic_intro_shop
        "Tell me about your motorcycle. (Wink)" $if this.data.mechanic_intro_guessedMotorcycle:
            jump mechanic_intro_motorcycleWink
        "Tell me about your motorcycle." $if this.data.mechanic_intro_knowMotorcycle:
            jump mechanic_intro_motorcycleTalk
        "(Leave)" $if this.data.mechanic_intro_canLeave:
            jump tutorial

mechanic_intro_tools:
    choice:
        talk mechanic talk "'Roof broke'? Could you be more specific?"
        "It broke. I need a tool so I can use planks to make it not broke.":
            choice:
                talk mechanic talk "Mhm. It has a hole in it? Is that what you're trying to tell me?"
                "Yes. It's broken. There's a hole in it.":
                    talk mechanic talk "Mhm. You don't have a hammer or anything? That's why you're here?"
                "Yes. I have a hole too though.":
                    talk mechanic talk "Don't we all."
                    "She chuckles quietly to herself."
                    talk mechanic talk "You need a hammer, is what I'm getting from this automobile crash of a conversation."
    "The Raven fumbles around in the box of tools with renewed vigour, before fishing out the hammer you so desperatly need."
    choice:
        talk mechanic talk "Here. A hammer. Made in Leads. Anglias finest. It'll be three pounds."
        "(Buy the hammer for 3 pounds)" $if this.data.money => 300:
            set hasHammer true
            set money money - 300
            talk mechanic talk "Good stuff. Thank you."
            "The Raven takes your money and hands you the hammer. With this tool you feel you could do anything."
        "But I don't have three pounds. I spent all my money at the shop!" $if this.data.money < 300:
            choice:
                talk mechanic talk "Well. That was silly of you, wasn't it?"
                "Yes! Very much so!":
                    talk mechanic talk "Mhm."
                "It could have happened to anyone.":
                    talk mechanic talk "I don't doubt that."
        "(Don't buy the hammer)":
            talk mechanic talk "Suit yourself."
    "The Raven returns to her work, whatever it is."
    jump mechanic_intro_menu

mechanic_intro_blood:
    talk mechanic talk "Looking to cover up a stabbing are we?"
    talk lovely talk "Oh my gods did you *have* to phrase it like that?"
    talk mechanic talk "No biggie. We all need to from time to time."
    talk nasty talk "I love this woman. She bops."
    $if this.skillCheck("mechanic_intro_blood_murder_lovely", "lovely", 40):
        talk lovely talk "She was only partially joking."
    talk mechanic talk "'Mx Lilyannes Blood Stain Remover' will get that right out. Use it for polishing automobile chasis, removing oil stains, you know that kind of shit. I'd sell you some but we're all out."
    talk nasty talk "That's the one! I love this stuff. Tastes nice too."
    talk lovely talk "That explains *so* much."
    $if this.skillCheck("mechanic_intro_blood_lead_orb", "orb", 40):
        talk orb talk "That chemical cocktail contains all Nasty Girls favourite essential vitamins: bleach, lead and alcohol."
        talk nasty talk "Delicious."
    jump mechanic_intro_menu

mechanic_intro_tattoo:
    talk mechanic talk "I don't know? Can you?"
    talk lovely talk "What the fuck??? What kind of a response was that? That isn't in any of my etiquitte books..."
    $if this.skillCheck("mechanic_intro_tattoo_etiquitte_lovely", "lovely", 40):
        set lovelyLadyResponse true
        talk lovely talk "Ugh, look, just... say 'I am.', definitly don't cry, it'll ruin everything and she'll never want to talk to you again."
    choice:
        talk nasty talk "Now *this* is my kind of woman!!!"
        "I am. Does it mean anything?" $if this.data.lovelyLadyResponse:
            "The Hyeanas face breaks into a smirk that is one part mean, one part amused, and one more part mean."
            $if this.skillCheck("mechanic_intro_tattoo_smile_lovely", "lovely", 60):
                talk lovely talk "It's a smile, actually. She's just bad at it. It is mean though."
            jump mechanic_intro_tattooExplain
        "Y-yes?":
            talk nasty talk "'Y-y-y-y-y-y-yes????' You sound so stupid."
            "There's a flash in the Hyeanas eyes. The flash of someone wanting to slam someone against a wall and bully them cut short by the realisation that slamming customers against walls is generally frowned upon, unfortunatly."
            choice:
                talk mechanic talk "Go on then. Ask."
                "I'm asking about your tattoo. Does it mean anything?":
                    jump mechanic_intro_tattooExplain
        "N-no?":
            talk nasty talk "N-n-n-n-n-n-no???? You sound so stupid."
            "The Raven shrugs."
            talk mechanic talk "Well then."
            jump mechanic_intro_menu
        "(Just start crying)":
            set mechanic_intro_canLeave true
            set mechanic_intro_cried true
            choice:
                "The Hyeana doesn't respond, she just goes back to her work and avoids looking at you."
                "(Wipe away your tears and stand there sniffling like a dickhead)":
                    $if this.data.lovelyLadyResponse:
                        talk lovely talk "WHAT DID I *JUST* SAY?"
                    else:
                        talk lovely talk "Oh she really hated that."
            talk orb talk "She's making a mental note to never get involved with you outside selling you shit. You've fucked up this potential friendship. Sorry. I guess."
            choice:
                talk nasty talk "Don't say sorry, it was her fault. She should be apologising for cucking us. Say 'Sorry for cucking us, Nasty Girl'."
                "Sorry for cucking us, Nasty Girl.":
                    talk nasty talk "You fucking better be."
                "Yeah I'll pass.":
                    talk nasty talk "What the fuck? What the fuck?"
                    talk lovely talk "Sounds like someone just got 'cucked' out of an apology, don't you think, Orb?"
                    talk orb talk "Don't drag me into this inane bullshit, Lovely Lady. Let's just accept this learning experience and move on."
            jump mechanic_intro_menu

mechanic_intro_tattooExplain:
    choice:
        talk mechanic talk "It means sometimes hearts get broken."
        "That's wild.":
            talk mechanic talk "It is, isn't it."
            jump mechanic_intro_tattooWild
        "(Light and Oestrodil cigarette) That's wild." $if this.data.hasCig:
            choice:
                talk mechanic talk "No smoking inside, please."
                "Of course. (Put out the cigarette)":
                    talk mechanic talk "Thank you."
                    $if this.data.deepthroatedCig:
                        talk mechanic talk "Still, at least you've learnt how you're actually supposed to use those now."
                    talk mechanic talk "As for the tattoo? It is wild, isn't it."
                    jump mechanic_intro_tattooWild
        "I have no opinion on this.":
            talk mechanic talk "Okay."
            jump mechanic_intro_menu

mechanic_intro_tattooWild:
    talk mechanic talk "And true too. Hearts sometimes get broken."
    $if this.skillCheck("mechanic_intro_tattooWild_poet_lovely", "lovely", 20):
        talk lovely talk "She genuinly thinks she is a poet, bless."
        $if this.skillCheck("mechanic_intro_tattooWild_front_orb", "orb", 60):
            talk orb talk "She wrote a lot of poems to someone from the front during the war. She never sent them, just wrote them down, stored them, and then burnt them when she returned to Anglia. Still, they aren't who the tattoo is about. The tattoo is a broader, more edgy statement on society as a whole."
    jump mechanic_intro_menu

mechanic_intro_shop:
    $if this.data.mechanic_intro_cried:
        talk mechanic talk "It's fine."
        talk lovely talk "She doesn't want to talk to you anymore than she has to, what with the crying episode and all."
        jump mechanic_intro_menu
    else:
        set mechanic_intro_knowMotorcycle true
        talk mechanic talk "Heh. It's not bad. It's quiet at least, and since I own the place I can just kick problem customers out."
        "She squints."
        choice:
            talk mechanic talk "You're not going to be a problem customer, are you?"
            "Yes. I was born for trouble, I'm a real nasty girl.":
                talk mechanic talk "Perfect."
                "Her tongue runs across her teeth."
                talk nasty talk "Hrrrrnnnnnggh nice."
            "No. I am a good girl, a lovely lady.":
                talk mechanic talk "Shame. Might have been fun to tell you off."
            "U-um. N-no.":
                "She grins."

        talk mechanic talk "Still, it's fine. Been an okay..."
        "She counts on her fingers."
        talk mechanic talk "Year and three months, or there abouts. I was pretty lucky and came into a lot of money, by which I mean my bitch mother died, so thought I'd use it to start a bussiness. I like motorcycles, and I'm good at fixing them, given that I own one. Still, it was a bit of a sudden decision, when I was a youngster I used to want to be a sailor. Boat to Frankreich on the way to the front taught me I get seasick, so that crushed that dream. I only thought about running a shop once I got back to Anglia. It was a bit slow at first, but I think it's gone well."
        jump mechanic_intro_menu

mechanic_intro_motorcycleWink:
    "She raises an eyebrow curiously."
    choice:
        talk mechanic talk "How'd you know about that then?"
        "You smell of engine oil.":
            choice:
                talk mechanic talk "A lot of things use engine oil, how'd you guess it was a motorcycle?."
                "Lucky guess.":
                    talk mechanic talk "Mhm. Very."
                "You look the type.":
                    talk mechanic talk "Eheh. I suppose I do don't I."
                "The omnipitent orb that lives in my chest told me.":
                    talk mechanic talk "Uh huh. Tell you anything else about me?"
                    talk orb neutal "She took that awfully well."
                    $if this.skillCheck("mechanic_intro_motorcycleWink_joke_lovely", "lovely", 20):
                        talk lovely talk "She thought it was a joke, Orb."
        "Motorcyclists can always tell when they've found one of their own. (Wink again)":
            talk orb talk "Why did you just say that? You don't have a motorcycle, and as far as I can tell you've never even ridden one."
            choice:
                talk mechanic talk "Heh. They can, you're right. I didn't get those vibes from you though, perhaps I'm out of practise; this city is a bit too tory for motorcycles. This here is 'automobile country'."
                "(Nod) I have a motorcycle.":
                    set global_motorcycleLie true
                    choice:
                        talk mechanic talk "How wonderful. You'll have to show me it somewhen."
                        "(Make a mental note to get a motorcycle)":
                            talk nasty talk "About time, lets do this, fuck yes."
                            talk orb talk "I am desperatly wracking my thoughts for a way I can take up chain smoking."
                        "(Lie) Yes. I can show you my real motorcycle. It's real by the way.":  
                            talk mechanic talk "Lovely."
                "I actually don't have a motorcycle, I don't know why I said I do sorry.":
                    talk mechanic talk "Hah. I thought so. You're not the type. Still, I appreciate the tenacity of your lie."
    choice:
        talk mechanic talk "Bussiness seems pretty slow today, we can go take a look at my motorcycle, if you want?"
        "Okay, let's go, motorcycle time.":
            jump mechanic_intro_motorcycleTalk
        "Okay, let's go, it'll be good to compare it to my own motorcycle that I definitly own." $if this.data.motorcycleLie:
            talk orb talk "*Please* stop bringing up your motorcycle. You don't *have* a motorcycle."
            jump mechanic_intro_motorcycleTalk
    
mechanic_intro_motorcycleTalk:
    "[Intro]"
    talk mechanic talk "Her name's Heidi. She's a Ratzubishi 4vk in prime condition, practically. She looked after me during the war, and I repay her by looking after her now."
    "She runs her hand across the fuel tank. It has been polished to perfection, a shining moss green. The mechanics eyes seem close to tears. She genuinly loves this machine. The chasis is blemished with a single bullethole. Around it the paintwork has been scratched off in the shape of a rose. The same image that would have adorned a medal for exceptional bravery."
    $if this.skillCheck("mechanic_intro_motorcycleTalk_fear_orb", "orb", 80):
        talk orb talk "And yet she fears it. She fears what it represents. Not a war hero, a failure. A coward. The outside is pristine, but inside it is rusted and broken. If it *can* still start it's liable to explode. This heap of metal is not kept for leisure, it is a gravestone."
    $if this.skillCheck("mechanic_intro_motorcycleTalk_ride_nasty", "nasty", 20):
        talk nasty talk "Ask if she'll take you for a ride. You know what I mean by that, right? Ay? Right? Ride. Right?"
        talk lovely talk "Sigh."
        set takeMeForARide true
    jump mechanic_intro_motorcycle_menu

mechanic_intro_motorcycle_menu:
    choice:
        ""
        "I bet you and Heidi have had quite the adventures together?":
            jump mechanic_intro_motorcycle_adventures
        "(Point at the bullethole in the chasis) Is that a bullethole in the chasis?":
            jump mechanic_intro_motorcycle_bullethole
        "Can I sit on it? Can I sit on the cycle, pleaseeee?":
            jump mechanic_intro_motorcycle_sit
        "(Whistle) Pheeeeew, what a beauty!":
            jump mechanic_intro_motorcycle_beauty
        "Want to take me for a ride?" $this.data.takeMeForARide:
            jump mechanic_intro_motorcycle_ride
        "That was fun, I think I've seen enough of your motorcycle for now though. (Move on)":
            set mechanic_intro_canLeave true
            talk mechanic talk "No problem. It was nice getting to show Heidi off."
            jump mechanic_intro_menu

mechanic_intro_motorcycle_adventures:
    ""
    choice:
        ""
        "You were a soldier?":
            talk mechanic talk "Not exactly. For the last three years of the war I was part of a recon unit. Scouting enemy locations, running messages between posts, that sort of thing. It was fun, in a 'I could die at any moment and have seen horror you would not belive' kind of way. I suppose knowing I got to drive this beauty while most troops had to sit in mud all day perked me up. We got into some pretty wild adventures though, yes. Tennenburg was the big one I suppose, but there was the minefield incident, the flamethrower incident, the time I ended up in the Iberian Republic by accident after I got carried away..."
            "She smiles. A sort of terrifying nostalgia."
            talk nasty talk "I want to know if she killed anyone."
            $if this.skillCheck("mechanic_intro_motrocycle_adventures_kill_lovely", "lovely", 40):
                talk lovely talk "Do *not* under *any* circumstances ask if she killed anyone, I am *begging* you."
                talk nasty talk "But I want to knowwwwww."
                talk lovely talk "I'm putting my foot down, Nasty Girl. We are not asking that."
                talk nasty talk "That's right, step on me bitch."
                talk lovely talk "H-hey. No. None of t-that."
                talk nasty talk "Heheheheheh."
            choice:
                "The War Heros face seems to know what you're considering asking."
                "So how many people did you kill? A lot, right? You seem like you'd be good at it.":
                    talk mechanic talk "None. I was in recon, my entire role was *not* getting into fights."
                    "She looks away from you, nonchalantly investigating some chipped paintwork hiding next to one of the motorcycles pedals."
                    talk lovely talk "WHY DID YOU ASK THAT? YOU ARE SO LUCKY HER AWNSER WAS NONE."
                    talk nasty talk "Ugh, I was hoping it would be in the triple digets."
                    talk orb talk "She's lying to you, at least somewhat. As far as she is concerned it is in the thousands."
                "I am not going to ask her if she killed anyone.":
                    talk lovely talk "Thank you so much."
                    talk nasty talk "Brain cuck."
                    talk lovely talk "Ignore her, you took the objectivley correct choice."
    jump mechanic_intro_motorcycle_menu

mechanic_intro_motorcycle_bullethole:
    talk mechanic talk "Mhm. Took a bullet in Tennenburg Wood while I was running a message to the forward command post. I got off worse than Heidi did: I had a nasty tumble and lost a *lot* of blood."
    "She grimances. It's subtle, but it's there."
    $if this.skillCheck("mechanic_intro_motorcycle_bullethole_grimace_lovely", "lovely", 40):
        talk lovely talk "She tries not to show it, but she still feels the pain in her arm, the blood matting her fur. She still sometimes worries the sniper is still out there, waiting to take their second shot. Sometimes she wishes they would."
    choice:
        talk mechanic talk "Still, I got the message there in the end, that's what counts right?"
        "You're a real life war heroine!":
            jump mechanic_intro_morgana
        "(Make a vague non-commital sound in lieau of talking about how you don't respect the troops in front of this extremelly physically imposing war veteran)":
            jump mechanic_intro_motorcycle_menu
        "That's wild.":
            talk mechanic talk "It is, isn't it?"
            jump mechanic_intro_motorcycle_menu

mechanic_intro_morgana:
    talk mechanic talk "Eh. It was nothing. I'm not exactly Morgona the Pronkle am I?"
    $if this.skillCheck("mechanic_intro_motorcycle_bullethole_morgona_orb", "orb", 40):
        set mechanic_intro_orbMorgona true
        talk orb talk "Morgona the Pronkle was an Anglian infantrywoman who grew famous for her unorthadox use of bayonets, that is to say she attached them to her antlers, as well as her rifle. It sounds ridiculous, but she quickly became one of the most decorated soldiers in the Anglian military. They even had to invent a new medal for her, 'The gored heart', after she singleantlerdly took out an entire bunker with her bare... pronks."
        talk nasty talk "Holy shit she sounds amazing can we go find her I want her to gore us."
        choice:
            talk orb talk "Sadly no, she was killed a few months into the Ryneland campaign. Her bayonetted knives glinted too much and caught the eye of a sniper. Supposedly she joked on her death bed that she should never have cleaned the shine hiding blood off of them.A chilling tale that tells us why more deer do not attach bayonets to their antlers, and why they *do* attach leaves or other camoflauge to them so they can pretend to be innocent shrubbary."
            "She took out an entire bunker with just her antlers!?!?":
                talk orb talk "YES! Well, with the blades attached to them, at least. The second she gored the first opponent the others sort of lost the will to fight back, so grusome it was. They were, ironicly, like deer caught in floodlights. It was a bloodbath. Fourteen casulties, and Morgona only bent one antler."
            "Slow down a second, what the fuck is a 'pronkle'?":
                talk orb talk "Yes? What of it."
                talk nasty talk "It's soldier slang for antler, get with the times grandma."
            "She sounds very impressive.":
                talk orb talk "She was. The troops loved her. The Anglian military even discontinued use of the 'Antlercracker' type sniper rifle out of respect."
    choice:
        "The War Hero watches you quietly."
        "Who's Morgona the Pronkle?":
            $if this.data.mechanic_intro_orbMorgona:
                talk orb talk "Excuse me? I just told you this? Do you even listen to me?"
                talk lovely talk "It's called making conversation, Orb, most people don't have the 'luxury' of an internal encyclopedia jabbering on in their head all day and actually quite enjoy talking."
                talk orb talk "Unbelivable. I am treated so poorly by everyone in this flesh prison."
            talk mechanic talk "Morgona? Used to tie bayonets to her antlers! You know how many medals she got? Forty-three. Still, I got a motorcycle, and *I* didn't get shot."
        "You're still pretty heroic though.":
            "She smiles."
            talk mechanic talk "If you say so."
    jump mechanic_intro_motorcycle_menu

mechanic_intro_motorcycle_sit:
    choice:
        talk mechanic talk "Go ahead, just don't scuff the paintwork."
        "(Sit on the motorcycle)":
            set satOnMotorcycle true
            $if this.skillCheck("mechanic_intro_motorcycle_sit_quivers_lovely", "lovely", 60):
                talk lovely talk "The mechanics lip quivers, just for a moment. She has not sat on this motorcycle in years. Seeing you on it feels... wrong."
            choice:
                "You're in the drivers seat. The possibilitys are endless. You and a real life Ratzu. It's like you're *there*."
                "I'm where?":
                    "*There*"
                    "The fields of Northern Brennenburg. The war will be over in less than a week, the Imperial high command is pulling their forces back to the capital in an attempt to force the allies with an all deciding final battle of proportions hitherto unseen. The allies would naturally want to come to the negotiating table to prevent this, but the Imperials would have it as a bargning chip. It won't work. In three hours Anglian Special Forces will blow the bridges over the Whine river, and the Imperial military, which is in tatters, will be reduced to even smaller tatters. They get their wish though. The Allies are more preoccupied with ending the conflict before the newly birthed Soviet Republic swallows all of eastern and central Europa. *This* is where you are. The death rattle of the war, where violence is fought pointlessly but with tooth and with claw."
                    choice:
                        "Motar shells explode around you, bullets whiz past and strike the mud to your side with a *squealch*. Smoke rises on the horizon, poison gas in your peripheral. Fire at your back."
                        "(Nod) This bops. I love it here.":
                            jump mechanic_intro_motorcycle_imagination
                        "I don't want to be there!":
                            talk lovel talk "Oh honey no don't worry, you're not there! You're, um... you're on a lovely countryside lane! Look! Sheep! And over there! Look! Is that a daffodil!? I think it might be!"
                            talk nasty talk "Oh my gods this is so shit, please go back to the harrowing violence."
                            talk orb talk "I'm hesitant to agree with nasty girl but she's right. This is embarrassing. Stop."
                            jump mechanic_intro_motorcycle_fall
                "I don't know if I want to be there?":
                    jump mechanic_intro_motorcycle_fall

mechanic_intro_motorcycle_imagination:
    choice:
        "They have you in the sights, they lick their lips and hold down on the trigger. Bullets spray twards you, they whistle past your head, singing a whisker. One slams into a tree ahead of you and the wood explodes with a crack. A splinter twirls through the air like a needle and scratches your cheek. You swerve to the side, kicking up mud and rainwater from the torn up ground."
        "Yessssss yessss this bops!":
            talk nasty talk "I agree. This bops. War bops. I like war now, this is great."
        "(Shake your head) War is hell.":
            talk nasty talk "Wrong, idiot. War bops. I like war now, this is great."
    choice:
        "She's looking at you with an expression halfway between fear and laughter."
        "I was making 'brrrrrrummm bruuuuum pew pew bruuuuuuuuuuum' noises out loud wasn't I?":
            talk orb talk "Yes."
            talk lovely talk "You were, yes."
            talk nasty talk "It was so fucking embarassing."
        "Sorry, how long was I sat on the cycle?":
            talk mechanic talk "Not long. And by not long I mean maybe twenty minuites. You seemed to be having fun, I couldn't look away."
    choice:
        talk mechanic talk "I'm glad you like the motorcycle. I think?"
        "I'm so embarassed.":
            talk mechanic talk "Heh."
        "I'm so embarassed.":
            talk orb talk "You should be, to be honest."
            talk lovely talk "It's okay, so am I."
            talk nasty talk "Good."
        "Did I look cool at least?":
            talk mechanic talk "No. Not even slightly. It was somewhat cute though, I suppose."
    jump mechanic_intro_motorcycle_menu

mechanic_intro_motorcycle_fall:
    "As you wish. You tumble from the seat and hit your head on the floor. Normally it would be quite painful, but in your current 'orbed' state it's rather refreshing."
    choice:
        talk mechanic talk "Fuck! Are you okay?"
        "That was quite refreshing, actually.":
            talk mechanic talk "That's good, but try not to die in my shop, please."
        "I want to go back on the motorcycle.":
            talk mechanic talk "Maybe not sweetheart, I don't want to be liable for any cracked skulls."
    jump mechanic_intro_motorcycle_menu

mechanic_intro_motorcycle_beauty:
    "The mechanic nods."
    talk mechanic talk "That she is."
    $if this.skillCheck("mechanic_intro_motorcycle_beauty_beauty_lovely", "lovely", 20):
        talk lovely talk "Say she's not so bad herself."
    talk mechanic talk "And hey, you're not so bad yourself."
    $if this.data.mechanic_intro_motorcycle_beauty_lovely_beauty:
        "Her smarmy grin is a knife that cuts through Lovely Ladys thin veneer of conversational control."
        talk lovely talk "What is up with this woman? Why does she keep messing with me? This is so unfair!"
    else:
        "She grins smarmily."
    
    choice:
        talk lovely talk "T-thank you Mam'."
        "T-thank you, Mam'":
            "The War Hero looks like she wants to punch you in the neck (in a sexy way)."
            talk nasty talk "Gods, you are such a bottom. It's actually cramping my style pretty badly."
        "Thank you!":
            talk mechanic talk "Heh."
        "You're not so bad yourself either.":
            talk mechanic talk "Cute. I'm not a beauty though. I'm rugged, dirty, hard... I'm a lot of things, but not beautiful."
    jump mechanic_intro_motorcycle_menu

mechanic_intro_motorcycle_ride:
    talk mechanic talk "No. Sorry."
    talk nasty talk "Tell her you meant a *different* kind of ride."
    $if this.skillCheck("mechanic_intro_motrocycle_ride_ride_lovely", "lovely", 40):
        talk lovely talk "Don't. Thinking about her motorcycle has put her in a mood. Not a bad one per sey, but a difficult one. We should just back away from the subject of 'riding' and 'motorcycles' entierly."
    choice:
        "The War Hero stares at her motorcycle. Her eyes arent quite vacant, theres *something* there, but it's impossible to place."
        "I mean a different kind of ride. (Wink) Fucking.":
            talk mechanic talk "Uhuh. No."
            jump mechanic_intro_motorcycle_menu
        "(Move on)":
            jump mechanic_intro_motorcycle_menu