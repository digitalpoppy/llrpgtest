book_history:
    if !this.data.historyBookOpened:
        jump history_intro
    else:
        jump history_menu

history_menu:
    ""

    choice:
        ""
        "(Take a look at the map)":
            jump history_map

history_intro:
    set global_actionsleft this.data.global_actionsleft - 1
    set_screen default
    ""
    history_menu

history_map:
    "Afrika is dominated by the Central Afrikan Corvid Commune. The illustration is sligtly out of date, it has too much Anglian red on it. These days theres only a slither of territory clinging to the coast that the government is too stubborn to surrender. No biggie, it's only costing hundreds of lives a week."
    "Then there's Europa, your home. The map is still accurate. The borders have not shifted since the war ended. A dotted line circles other territories. Anglia, Frankreich, Australien... This was the extent of the Imperial dynasty at its height in the 1700s. It's long gone now, but its historical impact is such that it is still recorded on maps. Even the names on the map are in High Imperial, rather than traditional Anglian. The cultural legacy of imperialism. You'd half expect this to make Anglia shine with some glimmer of self awareness regardng its own colonial expoilts, but willfull ignorence is baked into the system by design. Anglian Empire good. Imperial Brennenburg bad."
    "To the west lays the Atlantic, American and Pacific seas. They cover maybe two thirds of the planets surface. The Americas were not always a sea, of course. The entire continent dissapeared under the sea millions of years ago. No one knows for sure why."
    $if this.skillCheck("book_history_map_america_orb", "orb", 60):
        talk orb talk "I know why, actually."
        choice:
            talk orb talk "You... you probaly shouldnt know why though."
            "I'd quite like to know why an entire continent sank, actually.":
                jump history_sinking
            "That sounds ominous. I'll leave well alone. (Move on)":
                talk orb talk "Wise decison."
    jump history_menu

history_sinking:
    talk orb talk "The Mantis Hivemind sank the continent in their war against the Serpents."
    choice:
        talk orb talk "There's a Mantis Hivemind living underground. Sorry. I buried the lead on that a little, didn't I?"
        "(Take a big drag from your oestrodil ciggarete). That's wild." $if this.data.hasCig:
            talk orb talk "It is a bit, isn't it?"
        "(Pretend to take a big drag from and oestrodil ciggarete). That's wild.":
            talk orb talk "It is a bit, isn't it?"
            $if this.data.shopDiscovered:
                $if this.data.hasCig:
                    talk nasty talk "Do it for real, brain cuck."
                else:
                    talk nasty talk "Bet you wish you bought those cigarettes now huh?"
                    talk nasty talk "Idiot."
    
    talk orb talk "The hive will awaken again, at least one more time."
    talk orb talk "I could probably give you a date if you want! Test me!"
    talk orb talk "Although..."
    choice:
        talk orb talk "You... you *really* shouldn't know that."
        "Tell me.":
            talk orb talk "Well. If you insisit."
            "Orb strains as it attempts to divine the future. It is really trying to impress you right now. You should make sure to show your appreciation after"
            talk orb talk "In... about a year, the Inquisition on Gotland does *something*. It's not an atomic bomb, it's something arcane. Their entire institution and collection of 'weird stuff' is obliterated. The island is leveled. Windows break even in Musckow."
            choice:
                talk orb talk "The hive awakens once more. Another attack? They set about sinking Europa."
                "Do they succeed?":
                    talk orb talk "I don't know. Hopefully not, for your sake. the alps are a load bearing mountain range. THey go and most of the rest of the planets landmass sinks too."
                "Why would you tell me this? That's awful. Our entire lives are literally held up on the whims of literal bugs. LITERAL bugs. They could kill us all right this moment, if they wanted. I think I might develop an unhealthy coping mechanism or two to deal with this. Alcohilism or eating grass maybe.":
                    talk orb talk "I *did* warn you."
    jump history_map_menu

book_history_map_menu:
    choice:
        ""
        "Tell me about Europa.":
            jump history_europa
        "Tell me about Asia.:":
            jump history_asia
        "Tell me about Afrika.":
            jump history_afrika
        "Tell me about America.":
            jump history_america
        "Let's move on.":
            jump history_menu

book_history_europa:
    ""
    jump book_history_map_menu
    
book_history_asia
    ""
    talk orb talk "This map was evidently drawn before the cesessiona agreement was finalised; Austria is marked as independent on it. It won't be until 1930."
    choice:
        ""
        "Why does Austria want to be independent?":
            talk orb talk "It doesn't, not necesserily, anyway. The agreement came about due to Oceanias 'anti colonial' pressure. Much of Austrias land is to be returned to the indigenous populations. Not that Oceanias intentions are entierly noble. Their real aim is no more Anglian influence in the South East, and more importantly their scientists recently discovered oil and coal underneath the great red desert. It will be far easier to monopoloise that with Anglia out of the picture."
    jump book_history_map_menu
    
book_history_afrika:
    talk orb talk "They aren't marked, not because they are un inhabited, far from it, but because the people that live there move, or exist in land with no defined borders, and what borders there are are too small to mark."
    choice:
        ""
        "No borders? Thats simply insane.":
            talk orb talk "Not to sound vain but I know everything, and all I can say in response to you is 'no it's good actually'."

    talk orb talk "It's mostly famous for its University. Likely the oldest in the world, and certinaly the most prestigious."
    choice:
        ""
        "More so than Oxenford?":
            talk orb talk "You go to Oxenford to find other rich elites to 'stroke the tails of' as the youth say, not to get an education."



    talk orb talk "The Communes population is about 90% corvid, 10% mammal, who mostly live on the more inhabitable western reaches of the commune."

    talk orb talk "Images of birds using their beaks to peck away the dirt are rather common. The Commune aims to invest in some mechinised mining infrastructure as soon as it can."
    
    jump book_history_map_menu

book_history_america:
    ""
    jump book_history_map_menu

book_history_ancient:
    ""
    jump book_history_menu

book_history_darkAge:
    ""
    jump book_history_menu

book_history_recent:
    ""
    jump book_history_menu

book_history_theWar:
    ""

    talk orb talk "Warsaw attacked Muskovy over some dull territorial dispute, Brennenburg, Mosckovys ally attacked Warsaw as part of a defencive pact, Anglia and Frankreich saw the opportunity to curb stop their favourite rival and joined the war on Warsaws side, Rome, the Osmanisches Empire and a bunch of irelevant countries joined Brennenburg, Persian rebels recieved guns from Anglia, the Central Afrikan Corvid Commune took the opportunity to try and kick the Anglian Empire and Frankreich out of the Afrikan continent, everyone caught rabies, then after the revolution The Soviet Republic invaded Imperial occupied Eastern Europa and joined the allies, no longer under threat from an Imperial aligned Musockovy, Cawrea joined the allies in support of liberating Imperial Crowatia. Oceania stayed out of it and sold everyone guns."
    talk orb talk "Or something like that, it was a rather confusing time. Future students will come to hate memorising all the dates."
    talk orb talk "There were four main fronts. The western front, running along Frankreichs border with Brennenburg. That's the one all the complaining about mud and trenches came from. The Eastern front between Warsaw and Musckovy, and later The Soviets and Brennenburg, that's the snowy one with the war crimes. The Middle Eastern front between the Osmanisches Empire and Ghaznavid. See also, Persian rebels and civil war. There was also the Southern front, Anglia and Frankreiches colonial holdings in Afrika fighting against rebel groups organised and led by the Commune. It's sometimes claimed that this was less part of the great war and more a war in its own right, especially given that it is ongoing. Still, its better propoganda to pretend the war is over and anything going on 'down there' is merely minor rebellions that need putting down and not the most brutal, war crimy conflict in history."
    jump book_history_map_menu

book_history_theWar_menu:
    choice:
        talk orb talk "Would you like to know more?"
        "Tell me more about the Western front.":
            jump book_history_theWar_western
        "Tell me more about the Eastern front.":   
            jump book_history_theWar_eastern
        "Tell me more about the Middle Eastern front.":
            jump book_history_theWar_middleEastern
        "Tell me more about the Southern front.":
            jump book_history_theWar_southern
        "Tell me more about the rabies.":
            jump book_history_theWar_rabies
        "Did *I* fight in the war?":
            jump book_history_theWar_fight
        "I think I'm done thinking about this. It's depressing. And confusing. Mostly depressing.":
            jump book_history_menu

book_history_theWar_western:
    ""
    jump history_theWar_menu

book_history_theWar_eastern:
    ""
    jump history_theWar_menu

book_history_theWar_middleEastern:
    ""
    jump history_theWar_menu

book_history_theWar_southern:
    ""
    jump history_theWar_menu

book_history_theWar_rabies:
    ""
    talk orb talk "Corvidae Rabies originated somewhere in the battlefields of central Afrika. It appeared to spread harmlessly though the local bird population, minor flu symptoms at worst, but then jumped to the mannals, native, coloniser and Anglian soldier alike. A long incubation time and asymptomatic cases as well as the use of speedy messanger birds meant to quickly hopped to the other colonial holdings nearby, then Anglias ports, then the western front, Brennenburg... remote Oceania was able to implement strict quarentine procedures fast enough to avoid the worst of it."
    talk orb talk "Symptoms ranged from a bad flu to the brain melting into a feral state until you died of dehydration or 'brain disentanglment'. It was grusome."
    talk orb talk "Birds of course recieved a lot of blame for the crisis. It wasn't their fault the virus mutated like that, though it *was* convinent for the primarily bird ingabitants of the commune."
    jump book_history_thewar_menu

book_history_theWar_fight:
    $if this.skillCheck("book_history_theWar_fight_didIFight_orb", "orb", 40):
        talk orb talk "No."
        talk orb talk "You were found mentally unfit for service."
                
        choice:
            ""
            "What was wrong with me?":
                choice:
                    talk orb talk "Everything."
                    "That's awful!":
                        choice:
                            talk orb talk "If it makes you feel better the official file has an error; it says you're mentally 'unfet'."
                            "Why would that make me feel better?":
                                choice:
                                    talk orb talk "I dont know, i thought it might?"
                                    "Why do you even tell me most of this stuff you know, no one cares":
                                        talk orb talk "i think its interesting? Besides, if you knew everything youd be as obnoxious as i am too."                        
                                        talk orb talk "I dont know, i thought it might?"
                                    "Why do you even tell me most of this stuff you know, no one cares":
                                        talk orb talk "i think its interesting? Besides, if you knew everything youd be as obnoxious as i am too."
                    "That sounds about right.":
                        jump book_history_thewar_menu

book_history_now:
    ""
    jump book_history_map_menu

