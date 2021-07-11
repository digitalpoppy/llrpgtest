

crystals:
    talk orb talk "No. the cyrtsals sold there are made of glass"
    talk nasty talk "They have 'REAL' written on their box. I don't think the good women and men of 'Magic Gimmiks INC' would like to us, orb."
    talk orb talk "Nothing with 'REAL' or 'LEGITEMITE' or 'GENUINE' in the name is real, Nasty Girl, that's just a fact."
    talk nasty talk "Ms Thorpehopes GENUINE chewing tobacco is real, idiot."
    talk orb talk "Ms Throrpehopes GENUINE chewing tobaccos is a combination of tire rubber and lead, Nasty Girl."
    talk nasty talk "Huh. No wonder I'm so keen on them. We should go buy some when we buy the crystal."
    choice:
        talk orb talk "Again, those crystals are fake."
        "(investigate them anyway, just in case)":
            ""
        "(best to ignore them)":
            ""

theFall:
    $if this.skillCheck("simple", "orb", 40):
        talk orb talk "The Seventh City isn't down there. You already knew that though, didnt you,"
    choice:
        ""
        "(Let her go)":
            "She cries"
        "You know I'd like you to stay with me, right?":
            ""

magic:
    choice:
        ""
        "But you can do magic, you did some in the cathedral remember?":
            talk blackeye talk "T-that was a magic *trick*, not actual magic."
            talk blackeye talk "Y- you didn't realise?"
            talk lovely talk "Oh my gods she fooled us."
            talk nasty talk "What the fuck."
            talk orb talk "I wish I were capable of death."

colonialism:
    talk blackeye talk "You forget about it. Or you ignore it. You dont see it, thats for sure. But I *have*. The only thing keeping the butcher overshores from turning his blade on you is luck. The scythe, the system..."
    "She gestures vaguelly at nothing."
    talk blackeye talk "Will murder us all. Algierien. Anglian. Poor. Middle class. Even the rich eventually, when theres no one else left for the blade to cut."

lovelace_whatAmI:
    talk lovelace talk "I dont know sweetheart, you're a lovely lady, or a nasty girl. Whatever you want."
    "She pulls her sunglasses back over her eyes and returns to her book"
    talk lovely talk "Ha! Take that Nasty Girl!"

dreadnaught:
    "the skeleton of imperialism. You live inside of its corpse. You just dont realise it."
    $if this.skillCheck("simple", "orb", 25):
        talk orb talk "twenty five cannons, over fifty anti aircraft guns. Engines powerful enough to keep up with even a light battleship. Modern radar..."
    choice:
        "It lays rusting in the woods."
        "Is it *supposed* to be in the woods?":
            $if this.skillCheck("simple", "orb", 25):
                talk orb talk "it should be in the sea. or a very large lake, at the least."
            $if this.skillCheck("simple", "lovely", 25):
                talk lovely talk "Thats definitly wrong."
            $if this.skillCheck("simple", "nasty", 25):
                talk nasty talk "No."
        "I have no opinion on this dreadnaught being located on dry land miles from sea.":
            "..."

    "If you think that's bad, you should guess what percentage of the moneywent to the CEO of Glittertree Corp"
    choice:
        ""
        "Glittertree corp?"
            talk lovely "It sounds rather cute!"
            talk orb talk "It's an arms manfacturer. they make money designing new ways to remove the limbs from children. It's founder, Glittertree Senior invented the incendery scattershot shell and made a fortune selling them to the Imperials."
        "What percentage"
            talk orb talk "Dont worry about that. It'll just make you angry."


        talk orb talk "It would have been able to appear off the northern coast of brenneburg, shell the capital and dissapear before it could be responded, to, nay, detected. The ultimate weapon of psycological terror, as well as the ultimate weapon of pyhrical destruction, if it had worked that is. The deparmtnet wanted tocover up this undeniable evidence of the arcane, the treasury the undeniable waste of money that should have been spent on supplies for the troops an dmedcation for a rabies stricken lunden. The department of the arcane was disbanded, probably shot, and now there are few who know what happened here Most of them are from Warsaw. Whenever the government wants someting done quietly it pays people who dont speak the local language to do it. People more afraid of deportation than they are talkative. It will be a slow process, but within a few years the mistake will be covered up and forgotten, and when those in charge of the site pass it will be as though it never happened"

        "We should totally steal some of it."
        "quest added: steal part of it"

        "THe imperial inquestion stole most o fthem."
        "Far away, on an island in the baltic mad wizards still toil. for them the war is not over."

        "The Soviet Republic had some too, briefly, but they were destroyed in the workers revolution. Assumed to be diamonds. It was in at the time to destroy symbols of imperial decdence, regardlee of their worth. It was only When everyone in the room was atomised that they realised their mistake."

nasty_street:
    talk nasty talk "W- wait its real? Oh oh gods OH MY GODS."
    talk orb talk "The street was bla bla bla lore"
    talk nasty talk "OH MY GODS. OH MY GODS."
    talk orb talk "The street was bla bla bla lore"
    talk nasty talk "AAAAAAAAAAAAAAAAAAAAAAAAA. I mean. I told you. Idiots."
    if this.data.lovelyFake:
        talk nasty talk "Take that lovely lady! You fucking poser!"
    talk orb talk "Whatever. You got lucky."




blackeyeGuilt:
  talk blackeye talk "Do you know what job I worked, before the accident?"
  $if this.skillCheck("simple", "orb", 40):
    talk orb talk "She has the dead eyes of a beurucrat."
    set orbGuessedJob true
  $if this.skillCheck("simple", "lovely", 40):
    talk lovely talk "She has the kind eyes of a teacher."
    set lovelyGuessedJob true
  $if this.skillCheck("simple", "nasty", 40):
    talk nasty talk "She smells like wine. She was a wine taster."
    talk lovely talk "She is literally drinking wine right now. That's why she smells of wine."
    talk nasty talk "Shut."
    set nastyGuessedJob true
  choice:
    talk blackeye talk "Go on, take a guess."
    "You were a beurucrat." $if this.data.orbGuessedJob:
      talk blackeye talk "You're half right."
    "You were a teacher." $if this.data.lovelyGuessedJob:
      talk blackeye talk "You're half right."
    "You are currently drinking wine, hence the smell." $if this.data.nastyGuessedJob:
      talk blackeye talk "I am yes."
      "She seems unmoved by your statement."
    "(Shrug) I don't know. Blumdriver. Is that a thing? A blumdriver?":
      talk blackeye talk "That isn't a thing, no."

  talk blackeye talk "I was a teacher, but only two days a week. Art, mostly, and some Anglian literature and language classes too. The other three days I worked for the Briargrey Mining Company, in the beurucracy department. Everyday I would sign off on more waste being added to the coal tip. Just a little bit every day. We all knew it was dangerous but it was above our paygrade to argue, and if we did we would be replaced. So little by little, I, and the other people in the department signed the death warrent of the town. You know when they execute deserters, why the firing squad is made up of so many people? It isn't just an attempt to turn the deserter into schweiss cheese, no. It's to diffuse guilt. Assuage responsibility. Not all of the guns are loaded. Perhaps *I* didn't kill them. I spent two days a week nurturing children, and three days a week willingly plotting their murder."
  $if this.skillCheck("simple", "orb", 40):
    talk orb talk "The school was in the area struck by the landslide. She will never forgive herself."


escape:
    choice:
        ""
        "(Cast the spell)":
            success "arrive safely in the study"
            failure "arrive safely in the basement, after some scares"
        "Just to check, this dreadnaught ended up embedded in a hillside and everyone on board turned to carbon when they tried this spell, right?":
            talk orb talk "Yes. Try not to think too hard about that. Really; thinking about it will actually increase the chances of that happening."

  
leave:
    talk nasty talk "If lovely lady wants to go, then I want to go too."

beurocracy:
    talk blackeye talk "Clipboards. Just show up with some clipboards. Oh, and hand out some forms. Tell people they are *urgent* but dont explain what they're for. It'll short circuit their brains and they'll drop everything to do them. Used to be the only way to get the break room to myself back at the..."
    "She trails off."

general:
    talk nasty talk "Fuck that! Dress as a general and just show up and start yelling! Don't have to debase yourself pretending you care about 'health' and 'saftey' and get to scream at the troops. It's a win win."

plan:
    talk orb talk "I *could* just unembedd myself from your chest and resume my journey, but thanks to these 'emotions' you have foist upon me like a flu, I *really* don't want my last moments on this planet to be watching you bleed out on the floor. We need a solution that will, at the exact moment I depart, regrow your heart and ribs and, you know, all that other nasty biological stuff you have in there. And fortunatly for you, I have one."



mechanic_postHeist:
  $if this.data.mechanicInjured:
    "Theses a bandage wrapped around her arm. You cant see through it, but it seems bad."
    $if this.skillCheck("simple", "orb", 40):
      talk orb talk "It is bad."
    choice:
      ""
      "I'm sorry about the injury. That was probably my fault.":
        talk mechanic talk "Not at all. It was whoever shot mes fault. Besides, this wound is going to make a great scar."
        choice:
            ""
            "I'm sorry about the injury. That was probably my fault.":
                talk mechanic talk "Not at all. It was whoever shot mes fault. Besides, this wound is going to make a great scar."
                choice:
                    talk mechanic talk "I'm already thinking of some tattoo designs to go around it. Something about how hearts sometimes get broken, you know?"
                    "Isn't that what your current tattoo is about?":
                        "She frowns."
                        talk mechanic talk "Shit. You're right. Like I say, still thinking on it."
                    "That's wild. (Move on)":
                        talk mechanic talk "It is wild, isn't it?"
            "(Ignore the injury)":
                ""



shepherd_afrika:
    talk shepherd talk "Sent me a telegram before I was let go. Something about a promotion, with 'You will also have to serve in the colonies' in the smallprint. I said no."
    talk orb talk "Conscription didnt technically end until a few months after Brennenburg surrendered, but troops stared to return home after just two weeks. Still, the Anglian government cherrypicked those with particuarly impressive service records, our shepherd friend among them. They could shoot a bird out of the sky from miles away, and did in fact, on many occassionas, but they were wise enough to not care about a promotion, and cynical enough to read the small print. Most were not."
    talk shepherd talk "I made the right decision. I'm not having anything to do with that shit show down south. It gets nastier down there everyday, and for what? A slither of stolen land?"
    "They spit. The kind of spit that would, if willpower were enough, be blood and bile."
    talk orb talk "The correct decision, ethically and saftey wise. Anglias pointless, petty conflict with the Commune and the rebels has very little in the way of strategic value, it exists only so that the nation can enter a state of collective delusioan and belive that yes, the anglian empre survives. Anglia has not fallen into irelevance under the shadow of it's eastern rivals. Wasting your life on it is pitiful. Killing in the name of it unforgivable."
    talk shepherd talk "The war in Europa was bad. But I've heard *stories* about what goes on down there. Stories that go beyond just 'bad terrain', 'massacres', 'rabies' and 'heat'. Fuck them. Fuck the troops. Fuck the government. Fuck it all. Let me get back to my sheep, please."


guilt:
    talk mechanic talk "I helped the army win one fucking battle. How many times did I reach my destination too late to save my comrades who were actually fighting? How many times did I pass orders to a commander who led their troops to slaughter? How many people on the other side died because of the information I passed on? How many of them deserved it?"
    talk orb talk "She isn't talking to you anymore, she's talking to the motorcycle, to the symbol engraved around the bullethole."


shepherd_tank:
    talk shepherd talk "The god of war loves mechanisation. All of propoganda in the world cannot make the average mammal pull the trigger on someone at their mercy. The armoured shell of the tank, the whings of the plane, they strip us of our reality. We are no longer there. The trigger is pulled on a piece of metal. The corpse trapped in its center is merely a side effect."
    $if this.data.global_lumber_redHanded:
        "They've entierly forgotten her feud with you. The tank parking in their field has practically restarted their brain."
    choice:
        talk shepherd talk "I still have the fucking thing. Just in case. Never know when the world might end."
        "The army let you keep a sniper rifle?":
            talk shepherd talk "The word 'let' is doing a lot of work there. It would be more accurate to say they didnt *stop* me taking the sniper rifle home with me. Yet. Don't tell them I have it."



write_article:
    choice:
        talk nasty talk "Of course, there's always the atomic option."
        "The what?":
            talk nasty talk "Let's make up a guy."

    choice:
        ""
        "(Write an article about the mechanic)":
            ""
        "(Write and article about the shepherd)":
            ""
        "(Write an article about the pilot)":
            ""
        "(Write an article about a guy (Made up))":
            ""
        "(Put the 'Weird' back into 'Weird Tails')":
            ""





writer_rabies:
    "You can *survive* rabies?":
        "The writer looks into their tissue, at whatever it is that came out of their throat."
        $if this.skillCheck("simple", "orb", 20):
            talk orb talk "Black, crusted blood. A hair thin slither of flesh. You don't survive rabies, not really."





write_nothing:
    talk writer "Why did you even show up? Just to mock me? I'm going to have to write some fucking filler now. Some bullshit about there being too many pidgeons in the park or something. Fucking hel."


fields_tree_menu:
    choice:
        "The tree sways softly in the wind."
        "(Admire it)":
            ""
        skillcheck fields_tree_menu_lovely_relax lovely 40 "(Attempt to clear your mind and relax under the tree)":
            success ""
                ""
            failure "It's just *so* boring."
                ""
        skillcheck fields_tree_menu_nasty_climb nasty 40 "(Attempt to climb the tree)":
            success ""
                ""
            failure ""
                ""
    jump fields_tree_menu




dontwanttoknow:
    choice:
        talk orb talk "What do you mean stop talking? I'm helping you out, in case you didn't notice. I have all the secrets of the universe and you're just going to snub that?"
        "I don't *want* to know about this stuff. I don't want you telling me about how the factory I'm looking at was built with stolen resources, I don't want you telling me the military would shoot me in the head before i helped me, i dont want you to tell me about how the wine im drinking was made with slave lavbour!":
            choice:
                talk orb talk "Why? It seems like important information. Besides, you know it now, and doesn't that make you a more well rounded, more informed individual? Besides *I* didn't tell you who made your wine."
                "No. It doesn't. It makes me feel like dirt. Just stop it. You're just The Nightmare without the decency to take off your mask. Fuck you.":
                    choice:
                        talk orb talk "Fine. But you know what you know, nothing can change that. Loiter in ignorence if you want, if you think that protects you, but theres's no taking back what I've already said."
                        "I forgot it all once before.":
                            talk orb talk "Whatever. That was an accident. Intentionally blinding yourself to your sins won't save your soul, only condemn it further. I'm done."
                            set global_orbDead true

shopkeeper_flirt:
    set global_shopkeeperFlirt true
    choice:
        talk nasty talk "So. The shopkeeper. The nice lady who runs the shop. She's into us, right?"
        "You're godsdamn right she is.":
            ""
        "I don't think so, no.":
            ""
        "What makes you say that?":
            talk nasty talk "Um, hello? Have you seen how much stuff we've bought off of her? Ladies love when you trade currency for goods."
            choice:
                talk lovely talk "It's true, ladies love the free market."
                "Are you two okay?":
                    ""


nightmare_hypocrite:
    talk nightmare talk "It;s good, isn't it? To scrape away the mould. Cut away the rot. Clean *everything* out, and start afresh."
    choice:
        ""
        "I thought you *wanted* me to remember?":
            talk nightmare talk "I want you to *suffer*. Why let the wound heal when we can work together, needling and picking away at the scab forever, and ever, and ever."


carBad:
    talk lovely talk "Sheep drawn carrige good automobile bad."
    talk nasty talk "We should go to town and SMASH as many automobile windscreens as we can find!"
    talk orb talk "Agreed. Let's do it."


birds_distrust:
    talk orb talk "Birds have always faced distrust from mammels. They speak a language mammals cannot, theyre small and quiet, and they can fly, so borders and walls mean nothing to them. The perfect spies. When Oceiana occupies Toamasina, a large mercentile city on the east coast of Madagaskar in the 1970s they station crack snipers on half the rooftops in the city to enforce the citywide lockdown. Nasty bussiness."

    talk orb talk "Life runs essentially as normal, albeit with a tank stationed around every second corner."



orb_theory:
    choice:
        talk orb talk "This wouldn't have happened if you didn't... I don't know? Want me to obliterate your psyche."
        "It wouldn't have?":
            talk orb talk "No. Can I be frank? Are you okay."
            "I'm fine. (Nod to noone)":
            
            "I'm not fine.":


nightmare_poison:
    choice:
        talk nightmare talk "It's poison, pumping through your veins."
        "Fuck FUCK FUCK":
            ""
        "It's not poison, it's just not for me.":
            talk nightmare talk "It *is* poison. It's poison and it's going to fucking kill you, *if* you're luckly."
                

nightmare_skull:
    choice:
        talk nightmare talk "heyyyy check out that skull! pretty neat huh? makes you think about how your skull is too big right? yours specifically, i mean."
        "What?":
            choice:
                talk nightmare talk "what? you never noticed? take a look at your head in the glasses reflection. its practicly creaking at its seams trying to keep your skull in right? eh, maybe it's just me, i don't know dude."
                "I don't know what dude means but I already know I don't want you to refer to me as one.":
                    talk nightmare talk "shit, sorry man, my mistake!"



                    skillcheck church_blackeyeIntro_girls_nasty nasty 40 "Hunting for girls. You know how it is.":
                    success "She smirks.":
                        choice:
                            talk blackeye talk "Any luck?"
                            "Not really, no.":
                                "She raises an eyebrow."
                                talk nasty talk "Nice, negging. Good work."
                            "I've had some now. (Wink embarassingly)":
                                "She smiles, but it's somewhat empty."
                    failure "She raises an eyebrow.":
                        talk nasty talk "Say it with some conviction next time, jackass."

    talk nightmare talk "in fact now i think about it your entire body looks like watching someone in a depressurised space slowly explode. your skeleton is going to burst out of that little body any second now, and then we'll know."
    "know what?":
        talk nightmare talk "oh, you know ;)"


nerd_return:
    talk nerd talk "Oh jeez you- you actually went out and did that for me? That's super nice..."
    "They fiddle with their glasses."

nerd_return_menu:
    choice:
        talk nerd talk "I'm not super into cryptids anymore though. Kind of got over them. You know how it is. Maybe."
        "You got over your biggest hobby overnight?":
            set nerd_return_menu_one true
            talk nerd talk "Kind of, yes. I was only into them for a few days, but it really felt like they might have been the one."
            jump nerd_return_menu
        "What's your new hobby:"
            talk nerd talk "I like spiders now. I've been collecting jars to keep them in."
            jump nerd_return_menu
        "The 'one'?" $if this.data.nerd_return_menu_one:
            talk nerd talk "The one! The one hobby I would finally keep! The hobby that would define me! That would make me!"
            jump nerd_return_menu



blackeye:
    talk blackeye talk "Pray, let me tell you about a... a dream, let's say, that I have been having."
    talk nasty talk "Oh boy, nothing more fun that listening to someone tell you about their dreams. Rolls eyes."
    talk lovely talk "Did you just say 'rolls eyes' out loud?"
    talk blackeye talk "I'm in this... this void. It's all black, as far as the eye can see. It's empty but for myself and one other being. It's The Reaper. The one from the old Corvid legends. It's huge, as though I am looking at the moon, with feathers made of blades that shine like a bettles carprice, all purple and turqouise and green, hmm? And a scythe in place of its beak with a tip that left beads of blook on my fur if i so much as looked at it. It doesn't speak, it doesn't even squark. It just stares at me. I know to turn around, and behind me I see it. I see the mound. It's coal and cork and iron and cloth and wood and babed wire and glass. It is my sins, every last one of them. They are here to judge me worthy of redemption, and so I eat. I bite into the mound, and I chew. It tastes of coal and dirt and rust and ash. It is not edible, and so the metal and glass cuts my mouth. My face becomes caked in dried blood dirtied with coaldust." 
    "She appears queasy even reminising on it."
    talk blackeye talk "Anyhow, it takes a while but at some point I am met with an epiphany. This is more than just a lump of twisted metal and coal and posessions, it's *me*, it is my body, my corpse. It is massive, and practically unrecognisble, but it is me. Eventually, the hard outside gives way, and inside is... it's like... like... hmm..."
    "She stubs her cigarette out."
    choice:
        talk blackeye talk "Like a doughnut, you know those, yes?"
        "(Nod) Jam.":
            talk blackeye talk "Jam. Yes. Quite."
            $if this.skillCheck("PLACEHOLDER", "lovely", 20):
                talk lovely talk "It was a rhetorical question."
            talk blackeye talk "Anyway, as I was saying..."
        "No. Explain 'doughnut' to me.":
            "The Sinner frowns."
            talk blackeye talk "Fried dough, sometimes in a ring shape, sometimes just a circle. Some have jam inside of them, it is these specifically that I am referring to."
            $if this.skillCheck("PLACEHOLDER", "orb", 20):
                set PLACEHOLDER_doughnut true
                talk orb talk "A doughnut is a- oh. Little slow on the mark there. I'm really not with it right now, sorry. This woman smokes *way* too much oestrodil, and I think it's effecting all of us. Except her, apparently. She's unsettlingly used to this."
                talk nasty talk "Only. Dougnut here. You're a dough... eh, forget it."
            choice:
                talk blackeye talk "Anyway, as I was saying..."
                "Sorry, what is this 'jam' you speak of?":
                    talk blackeye talk "Let's pretend I never brought up dougnnuts, yes? Anyway, as I was saying..."
                    $if this.data.PLACEHOLDER_doughnut:
                        talk orb talk "Jam is made with fruit heated in water and sugar such that it becomes a sort of jelly. It tends to be quite sweet, especially when inside a dougnut. In Anglia it is most commonly strawberry or rasberry. Phew! Still got it."
                        talk nasty talk "Only rasberry here is you mate. Haha. Still got it."
                "(Nod)":
                    talk lovely talk "Good choice."
                    talk blackeye talk "Anyway, as I was saying..."
    
    talk nasty talk "Doughnuts are is tasty. I like to eat."
    talk lovely talk "Are is tasty. Yes. Quite. Very good, Nasty Girl."
    talk blackeye talk "I claw and bite my way right through it's outer layer, each mouthful worse than the last, and inside there is blood. There is so much blood. It doesn't taste of blood though, not exactly. There are hints of it, iron and all that, but it tastes of wine. Chaterux Saint-Arnoin. My favourite. Floating in the blood, like strawberry seeds, there are bones. Skulls, mostly. Some cracked, some hewn in half, some shattered with bulletholes. Some are mangled in ways I cannot even describe. Eachone looks at me, and each one screams as my teeth break biting into it. The reaper is behind me still. It is there the entire time, watching me silently. It never once takes its eyes off of me. I eat, and I eat and I eat and it is *so* hard. I ate this all once before, did I not? In life? Why can I no longer stomach it? What happened to my appitite. It varies, how long the dream continues. Sometimes I eat very little, othertimes there are just a few splatters of blood left on the black ground for me to kneels down and lap up, but eventually, inevitably, I vomit. I vomit a bile that is black with coal and burnt wood and metal and crimson with blood and wine. It burns, it hurts, and then I wake up."
    "The Sinner lights a new cigarette, content that her delivery of the story was every bit as melodramatic as she had intended."
    choice:
        talk orb talk "Thoughts?"
        "This bitch needs therapy.":
            talk nasty talk "Agreed. It's hot as fuck."
        "I think I've had the same dream, more or less.":
            talk orb talk "Hmm. I think that's fair."
        "I know what a doughnut is.":
            talk orb talk "Okay. Thanks for letting me know."
    
    talk blackeye talk "I said earlier this was a dream, but it isn't. It's a vision. A prophesy. This horror will be my fate."

orb_comet:
    $if skillcheck("PLACEHOLDER", "orb", 60):
        talk orb talk "This is important, we should go watch it."




talk orb talk "It's 1973. From the deck of a retreating aircraft carrier a young Oceianian lad uses his fingers to frame the smoking skyline of Madagaskar City like a photograph. His friend laughs. In a few months, when actual photographs of the battle emerge they will think back to this moment, and the feeling they experience in the pit of their being will stay with them forever. To their side another soldier has collapsed to the floor, leaning against part of the hull. She is tired. She wants to go home. Just past her a middle aged commander is watching the city dissapear into the horizon. The ash from her cigarette dissapearing into the wind, as though the souls of those she sent to their deaths, and those she put to death."
talk orb talk "Two were destroyed. One sunk, one had a breached cartridge store and exploded. This is what it looks like, the death knell of Oceanian supremacy. Not a final, glorious battle. A burnings cityscape framed between the fingers of someone who will never smile again."
        
nerd_religion:
    choice:
        talk nerd talk "I'm thinking of getting into religion."
        "You're thinking of getting into 'religion'?":
            talk nerd talk "Yes."
        "You're thinking of 'getting into' religion?":
            talk nerd talk "Yes."
        "You're thinking of getting into religion.":
            talk nerd talk "Yes."
        "Cool. (Nod) Me too.":
            jump library_religion_explain

nerd_religion_explain:
    "They fiddle with their glasses."
    talk nerd talk "Like, all of them. Religion is like a hobby you aren't allowed to get bored of, right? Or you suffer eternally?"        


nightmare_sex:
    choice:
        talk nightmare talk "It's disgusting, right?" 
        "Sex?":
            talk orb talk "No not sex. Sex is great. We love sex. No, we're talking about sex that involves *you*."



talk nightmare talk "Let me get this straight. You cant remember your name, your job, your parents, anything. But you can remember me. What does that say about us, do you think?"




talk nightmare talk "It's only been two days, but I can already feel them waking up. Pretty soon they'll be burrowing their way through your little body once more. Peeking out of your pores, eating your heart."
talk nightmare talk "What are you, five? You think smoking oestrodil leaf will turn you into a girl? You think that'll stave me off? You're a fucking moron, but then, you already waited for a decade to start taking actual *medicinal* oestrodil, so I guess we already knew that, right?"




orb_carcosa:
    choice:
        talk orb talk "A vast, calm expanse of cloud sea. One could sail across it for a year and not find themselves on its other side. It was here the fourteen cities were born. No one knows when, or how, or who by. Even I know this not. My knowledge concerns the waking world, and so what I know I know from hearsay. They were surrounded on all sides by... do you know what a waterfall is?"
        "I know waterfalls yes. Water falls down. (Nod vigorously)":
            choice:
                talk orb talk "Well it's not like a waterfall at al. It's more like a current, just in the shape of a waterfall, and made from swiling orange and pink cloud. Any ship foolhardy enough to attempt to pass into it was torn to shreds within moments. Like attempting to bite a grinding wheel while it's grinding. It stretched across the entire, let's say south-east of Heaven, falling away into the depths of the terror. The rest of Heaven was ringed with whirlwind storms that raged endlessly, and rivers that flowed like rapids. Utterly impenetrable, but one could probably dip their toes in for a brief time and make it out alive. There was only one exception. Across a narrow stretch of current called the veil, on the north-west most tip of Heaven, was Hali."
                "Hali?":
                    choice:
                        talk orb talk "A vast stretch of terror. Hali was similar to Heaven, to an extent. It wasn't as calm, not nearly, and the clouds were *dense*, but one could sail there safely, more or less. It was initially assumed to be a lake, but it would soon become clear that it was a sea, no, an ocean, no, it stretched *forever*, and it flowed towards Carcosa like the sea to the shore, depositing *things* onto the cities shore. In the Dark Age there was a spate of mysterious deep sea creatures washing up on the shores of east Asia, on account of the volcanic ash choking the seabed. It was akin to this, but far far queerer."
                        "Tell me more about these deep sea creatures. I love deep sea creatures.":
                            talk orb talk "They looked a lot like octopi, but they had... skulls, for lack of a better term. Mammilian ones. They washed ashore in the thousands, and sang the entire time they slowly died on the dryland. Their bodies decayed away into mush in a few short days, and so none survived. It was quite the haunting couple of weeks for the region."
                        "(Move on)":
                            choice:
                                talk orb talk "Anyway, They would wash up everywhere ocassionaly, of course, but Carcosa was in a chokepoint and closest, so it would naturally get much of the terrors spoils for itself. Eventually they learnt things from the stuff that washed upon their shores, and like Anglia upon the invention of the machine gun set about in their quest of subjigation. Sending galleys out *into* the terror, through the calmest barrier in heaven, a location to which only Carcosa had ease of access. Those galleys that returned, for many did not, brought with them treasures beyond value, and creatures beyond description. Before long this was not enough, and the green and megolomania of Carcosas Imperial family swept across heaven, till all fourteen cities stood beneath the twin sun banner. And then one day everything changed. *Something* had found them, something from the terror, and it cared not for their ambitions of regality and domination. The terror spiralled around the city, and threatened to consume the others, before they did something to stop it. Some great and terrible arcana, and so it was that Carcosa and its new king fell from heaven and into the material realm."
                                "It fell from heaven? Where did it land?":
                                    $if this.skillCheck("orb_carcosa_land_orb", "orb", 80):
                                        talk orb talk "Here. More or less. There's a field a few miles to the east, Rosefield Meadow. I suspect it's somewhat to blame for me crashlanding on this awful planet. No offence."
                                    else:
                                        talk orb talk "I'm not sure, sorry. I wish I could tell you, I'm rather curious myself."
                                "What was this *something*?":
                                    $if this.skillCheck("orb_carcosa_king_orb", "orb", 80):
                                        talk orb talk "You here know it as 'The King in Yellow'."
                                    else:
                                        talk orb talk "Something terrible."
                                "What happened to the other cities?":
                                    $if this.skillCheck("orb_carcosa_cities_orb", "orb", 80):
                                        talk orb talk "They fell too, just slower. They're still in Heaven, to an extent, but they are with us too. It is not unknown for people to go missing in remote places, having wandered into the dream."
                                    else:
                                        talk orb talk ""

mechanic_eye:
    choice:
        ""
        "You blinded the murderer, didnt you?":
            talk mechanic talk "Aye. I did."
            talk nasty talk "Ha ha. Eye. Good one."



nightmare_friends:
    $if this.data.hungoutwithnoone:
        talk nightmare talk "Don't you have any friends? Whatever. I shouldnt be surprised, you never did, and if ever you did, theyd abandon you."
    elif this.data.hungoutwithnerd:
        talk nightmare talk "They remind me of you. That is to say, they arent normal. What? You think you're normal? Are you fucking kidding? You're fucking weird. It;s probably why people are so uncomfortable around you."
    elif this.data.warhero:
        talk nightmare talk "No I guess not huh, except y'know, all the tax money you paid that gets spent burning down central Afrika."
    elif this.data.blackeye:
        talk nightmare talk "You're the same really, arent you. You're both destined for hel."


nightmare_orb:
    talk nightmare talk "You could probably ply Orb out of you with a sharp enough knife. It'd kill you, sure, but they aren't you. You could never exorcise me. I'm part of you, moreso than your bones or your veins or your biles. If every you were rid of me you would be nothing. A husk. A shell. A piece of rotted paper clinging to the corner of an empty frame."


nerd_mimic:
    talk nerd talk "Mimicing them, but never understanding."


orb_lead:

    talk orb talk "They also have the slight advantage of having learnt the lessons of the Malaya and not putting lead in everything. The Oceanian population is the least lead poisoned of all the great powers, which has its benifits."
    talk nasty talk "What the fuck are you talking about, we love lead."
    talk orb talk "That's the problem, Nasty Girl, you Anglians *do* like lead. You should not *like* lead. It's poisonous. It's killing you."
    talk nasty talk "It's tasty, dipshit. The chicks dig it, asshole."
    talk lovely talk "Ignore Orb, Nasty Girl, it's just jelous of our refined pallettes. Anglia didn't become the worlds biggest exporter of lead on a whim, indeed it is our duty as the protoges of Saint Marigold to enlighten the uncivilised masses abroad."
    talk nasty talk "With lead, yeah. Fuck you Orb."
    talk orb talk "Oh my gods, Ghost, ply me out of your chest cavity with a spatula and let me die, I'm actually begging you."



talk blackeye talk "And I just stared at it. For hours. All afternoon, until the sun began to shine through the petals like light through stained glass. There was no feeling quite like it. A dysphoria for a life not lived, a dysphoria for a world that no longer exists. My fur was caked in coaldust and blood, and it screamed out for release."




nightmare_hrt:
    talk nightmare talk "I noticed yesterday, actually, but oestrodil therapy is kind of cheating, right? So I thought it fair to give testosterone a head start. Let's see who can win the race, or rather, win your *face*; the dainty, nimble little finger tips of oestrodil or the permenently disfiguring effects of testosterone! Ready set go!"


    talk nightmare talk "I don't know why you're bothering really, when the greater war breaks out Anglias oestrodil supplies wont last long without imports from Oceania. You'll be all back to normal, and even sadder for what you've lost. Why set yourself up for heartbreak, hmm?"


nightmare_flower:
    choice:
        talk nightmare talk "Because in a few years it'll be dead. Ground under the heel of a death squads boot. Torched in atomic fire. Plucked by a grieving widow. Everysecond you stare at those petals is a reminder that you are *going* to die."
        "Orb explicitly reassured me that the world wont end in my lifetime.":
            talk nightmare talk "OH! ORB PROMISED YOU? Yeah, it's always been so reliable in the past. Orb lied to you, moron, because it knows you're too weak to accept the truth."

            talk nightmare talk "Besides, apocolypse now or apocolypse later, everything will be dust."



choice:
    talk nightmare talk "Visualise yourself, I mean *really* visualise yourself in ten years. What do you see?"
    "Nothing.":
        ""
    "A corpse on a tiled floor. There's blood on my face and a bullethole in my heart.":
        choice:
            talk nightmare talk "And who put you there?"
            "The government.":
                
            "A stranger.":
            
            "Myself.":
        
    "A face that is not my own. The one hiding under my fur.":
        ""
    
    "A charred corpse.":

    "I'm surrounded by friends.":
        choice:
            talk nightmare talk "what friends?"
            "I don't know."



    choice:
        talk nightmare talk "And when you look back?"
        "Oblivion. Even before the Orb incident. My past is gone. Anhillated. It is not mine."


mechanicshepherd:
    choice:
        ""
        "":
            ""
        "Wait, the war hero had *two* partners!? Thats fucked up!":
            talk orb talk "Polyamarous people exist, asshole."
            talk lovely talk "Mhm."
            talk nasty talk "What are we but one happy little polycule?"
            talk lovely talk "Tsk, as if."
            talk nasty talk "Heheheh, got her."
            $if this.skillCheck("temp", "nightmare", 40):
                talk nightmare talk "Poly people aren't real though, are they? Even if they were, you'd certinsly never be one. You're weak enough to betray someone, sure, but a nice enough person to have a relationship to poison in the first place? Don't make me laugh. You might have lucked out with a handful in the past, but belive me, theres a reason they all left you eventually, lol."
                talk nightmare talk "oh look, you made me laugh : )"





choice:
    ""
    "(Clean up all the ashes one by one and put them back together into a cigarette)":



$if this.data.global_fixedCig:
    talk nightmare talk "This is like when you 'fixed' that ciggarette earlier, you realise? Taking something thats run its natural life span, and debasing it of its natural form. If I came into a museum and smashed a priceless Qing vase you'd be mad at me, right? But i'm supposed to just sit here and watch you ruin your 'natural beauty'? How cruel."



talk nightmare talk "Because I *love you*, Ghost. Do you know what it's like loving someone who wishes you were dead? It hurts."



talk blackeye talk "And so you aknowledge that it is a sin, yes? And yet you do it anyway because of some vague notion that someone else shares more of the blame than you? Tell me, would you extend that sympathy to others, those who might hurt you or yours?"


talk orb talk "That depends, doesn't it. Is a country it's people, or a people they're country? Not all people act in accordance with the state, but the state always acts as the hand of the people, wether they will it or no."