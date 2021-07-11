main:
    "Lovely Lady RPG"
    jump writer_intro
    choice:
        "For a long while there is only green. The light from some great flash. The sound of splintering lumber and exploding brick work. The rining of death in your ears, no, deeper in your head. When the green finally fades theres is only blackness. The ocassional flash of a dying neuron, a fading memory. Theres no telling how ling it is before The haze begins to lift. The darkness peels back like flayed skin, strands of sinew snapping along with your neurons as they blink back to life."
        "Oh goodness.":
            choice:
                "A single roof tile peels off of the roof and falls into the room, like a lost tooth down a gullet."
                "I'm dead. Aren't I? I'm a g- ghost.":
                    choice:
                        talk orb talk "You're not dead, you're just not who you used to be."
                        "So I'm *not* a ghost?":
                            choice:
                                talk orb talk "Debateable."
                                "And what do you mean to say I am not who I used to be?":
                                    choice:
                                        talk orb talk "Because an hour and fifty-seven minuites ago I crashed through your cottages wall and embedded myself into your chest like a cannonball. By all rights you should be dead, but you aren't, for some reason. You, Ghost, are just parts of your soul that didnt get knocked out by me, that managed to cling onto your frail little body like mould."
                                        "I'm really confused, sorry.":
                                            choice:
                                                talk orb talk "I'll try to phrase this nicely. Ghost, I have embedded myself in your chest. Your heart has been pulverised. In doing so I seem to have accidently knocked most of *you* out of you, for which I apologise. You're the dregs left at the bottom of the teacup. You're alive only through some bizzare arcane technicality that I can't explain. Have you ever seen a dead insect twitch its legs? Thats you. A dead insects leg twitch."
                                                "That wasn't a very nice thing to say about me.":
                                                    talk orb talk "Diplomatic language may not be my strong point, but honesty is."
                                                "I feel that's a fair desription of me.":
                                                    talk orb sad "It's good to be self aware."
                                                "Mother!!! Is that you!!!":
                                                    talk orb talk "Your mother never said that to you. I hope you're joking, or the situation is worse than I thought. We don't need you experiencing false memories when you've already lost most of your real ones."

    choice:
        talk orb talk "Look, if it makes you feel better, colliding with your soul did something to me too. I never used to have an internal monolouge, and I never used to speak. Now it wont shut up, and now *I* won't shut up. Also I used to know everything, now I can't even remember the exact date the Thirteen Cities return to the comsmos and bring about the end times. I know it's somewhere between the seventh age of the Mantis reclaimation and the decade of screams, but that doesn't really narrow things down. Also I keep wanting to... what's that thing called when the water comes out?"
        "You want to cry?":
            talk orb talk "Cry! Yes! Maybe? You cry when you're sad right?"
        "You want to pee?":
            talk orb talk "Pee! Yes! Maybe? You pee when you're sad right?"
    talk orb talk "Gods, it hurts so much! How do you deal with it?"
    "The floorboards creak beneath you. The impact of you landing on them has left them somewhat worse for wear."
    talk orb talk "Ghost, do you remember anything about your life?"
    
    choice:
        "You don't. Not really. Glimpses of someone else through a fogged up window. You, but watched by yourself from afar."
        "I don't remember much...":
            talk orb talk "'Not much' is considerably more than I expected. Are you sure you don't remember anything?"
        "I remember looking at someone through a fogged up window.":
            set intro_metaphors true
            choice:
                talk orb talk "Are you sure you aren't confusing a metphor for a memory?"
                "Oh.":
                    talk orb talk "Still, you remembered what a window is. That's something. Are you sure you don't remember anything?"

    choice:
        "You strain your mind. It's pointless. There's no way to pierce its barrier. It's as though it is wrapped in cobwebs."
        "I'm trying to remember, but my mind is awfully frayed...":
            jump intro_crowded
        "I think my brain might be wrapped in cobwebs.":
            $if this.data.intro_metaphors:
                talk orb talk "It isn't. You're doing it again. The metaphor thing. You need to stop this before you confuse yourself even more."
            else:
                choice:
                    talk orb talk "Are you sure you aren't confusing a metphor for a memory?"
                    "Oh.":
                        talk orb talk "Still, you remembered what a cobweb is. That's something."
            jump intro_crowded

intro_crowded:
    choice:
        talk orb talk "That's understandable. It's rather crowded and noisy in here, and we've *both* been through quite a shock."
        "Still, we both seem relitavly reasonable, so lets talk quietyly and sensibly figure this out and get back to normal. I can go and make my morning tea, you can go do... whatever it is you were planning to do before you practically killed me.":
            talk orb talk "Yes. Both of us. Reasonable. Look, about that... I mentioned overcrowding..."

    "In some other part of your mind, a purfumed corner stained with tea and oestrodil vapour, a voice pipes up."
    talk lovely talk "Oh, another one? As if the orb wasn't already enough! Please, Ms... whoever you are, vacate my boudouir, thank you."

    choice:
        talk nasty talk "pLeAsE vAcAtE mY bOuDoUiR!!! Do you realise how you sound, Lovely Lady? Like a TWAT."
        "Oh gods. H- how?":
            choice:
                talk lovely talk "How? Whatever do you mean darling?"
                "HOW are you those two here too?":
                    talk orb talk "The circumstances of my arrival were unfortunate. It may be wise to take a look around, it'd be better for you to piece it together for for yourself. Also, I need to know if you physically *can* look around, because certinally I can't."
    jump intro_getUp_menu
    
intro_getUp_menu:
    choice:
        "A shaft of sunlight pierces the wall and flows into your eyes, blinding you. The hole in the wall is surrounded by scorch marks. The floorboards around you are splintered, it is only dumb luck that they have not collapsed yet and plummeted you to the lower floor of your cottage."
        "(Look around the room)" $if !this.data.intro_lookedAround:
            set intro_lookedAround true
            "The Lovely Lady Handbook. It is short, for it has very little substance. The book has a fist shaped hole punched right through it, the crisp burnt smell of two little ladies burnt from page and branded in your psyche."
            talk orb talk "You were half way through reorganising the bookcase when I... arrived. This one - a present frorm a distant relative - was going on the 'do not read' shelf. I guess I bought some passangers along for the ride."
            talk nasty talk "Riding? That's a Lovely lady trait, right, Lovely Lady?"
            talk lovely talk "..."
            jump intro_getUp_menu
        "(Feel the pain in your chest)" $if !this.data.intro_feelPain:
            set intro_feelPain true
            "You feel your chest. There's no heartbeat, only a faint throbbing where your heart used to be"
            talk orb talk "I live here now. Resting snugly in a nest of pulverised muscle and splintered rib. I've been sorting out your blood flow, no no, no need to thank me, I'm just stopping you from bleeding out on the cold hard floor, no biggie."
            jump intro_getUp_menu
        "(Stand up)" $if !this.data.intro_gotUp:
            set intro_gotUp true
            "You stand up, and almost fall down again. You feel awful."
            jump intro_getUp_menu
        "(Move on)" $if this.data.intro_gotUp && this.data.intro_lookedAround && this.data.intro_feelPain:
            jump intro_existence

intro_existence:
    talk lovely talk "Honestly this place is a tip, you expect me to live here? Do you know who I am?"
    talk orb talk "Who you are? You're a dumb archetype from a dumb book written by a fraud. You're just classissm with extra steps."
    talk nasty talk "Haha. Get her ass."
    talk orb talk "My comment applied equally to you, Nasty Girl."
    talk nasty talk "What the fuck!? Fuck you! I thought we were friends!"
    talk lovely talk "We might have been written about in a book, but it doesnt make us fictional. We were all birthed from the same creator equal. Equal in spirit, if not in hygeine."
    talk orb talk "*You* were birthed by Penny Hazel Lovelace, failed fiction writer and known hack. I was birthed in a black hole left behind by a dying star. We are not the same."
    talk lovely talk "Of course we exist! I can tell you anything about my life! I was born in North Cortexshire to Lady and Lady neuronton [(]bla bla bla, lengthy backstore about life in the countryside]"

    choice:
        talk orb talk "She's literally just naming parts of the brain at random. You know that right?"
        "I'd like to hear more.":
            $if this.skillCheck("intro_existance_hearMore_lovely", "lovely", 20):
                talk lovely talk "[Lengthy backstory]"
            else:
                talk lovely talk "and.... uh, not much else happened. the end."
            choice:
                talk orb talk "Can we PLEASE move on now?"
                "And what about you Nasty Girl?":
                    jump intro_nastyGirlOrigin
                "Let's move on.":
                    talk nasty talk "Fuck you, Lovely Lady got to tell you about her backstory, I get to tell you about your backstory too."
                    choice:
                        talk nasty talk "Ask me about my backstory."
                        "(Sigh) What's your backstory, Nasty Girl."
                            jump intro_nastyGirlOrigin
        "And what about you Nasty Girl?":
            jump intro_nastyGirlOrigin

intro_nastyGirlOrigin:
    talk nasty talk "Me? I was born on the wrong side of the amygdala railway, sweetheart."
    talk orb talk "She's doing it too. They're both literally just naming parts of the brain. Not even thematicly appropriate parts. Please just ignore them."
    jump intro_conclusions

intro_conclusions:
    talk nasty talk "Looks like theres only one way to settle this. If you can prove we aren't real, we'll dissapear, right?"
    $if this.skillCheck("intro_conclusions_voices_orb", "orb", 20):
        talk orb talk "*That isn't how voices in the head work at the best of times, let alone during events like... whatever this is.*"
    talk lovely talk "Dissapate like mist over a glass lake."
    talk nasty talk "So go on, Ghost, prove we aren't real, idiot."
    talk lovely talk "Yes! Prove us false, fiend!"
    choice:
        "A section of roof tile peels from the cottage and falls through the damaged ceiling, landing with a thud."
        "Ugh.":
            "This place needs fixing up."
        "Ughhhhhh."
            "This place needs fixing up."
    jump home_intro