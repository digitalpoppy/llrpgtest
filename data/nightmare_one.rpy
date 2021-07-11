nightmare_one:
    "The day comes to a close, and there is naught left to do but retreat to your chyslis."
    $if this.data.global_parentsFateKnown:
        talk nightmare talk "You want to know though, don't you. You want to remember. You wanted to find out about your parents, didn't that knowledge put you more at ease in the end?"
    elif this.data.global_parentsFateKnownFailed:
        talk nightmare talk "You want to know though, don't you. You want to remember. You wanted to find out about your parents. If you really do want to know I can throw that information in for free. I'm just that much better of a friend than orb is. They're dead! And not the nice kind of dead, like, for as long as you remember, but the bad kind, they only died a few years ago! And Painfully too! You can probably still remember your fathers eyes, if you cared hard enough!"
    else:
        jump nightmare_one_brink





nightmare_one_choice:
    talk nightmare talk "Really though, you don't need *both* of those little ladies rattling around in your head like a bucket of sharpnel, do you? Who do you like more, Lovely Lady, or Nasty Girl?"
    "I like Lovely Lady.":
        jump nightmare_one_punishNasty
    "I like Nasty Girl.":
        jump nightmare_one_punishLovely
    "I like them both.":
        $if !data.this.nightmare_likeBoth:
            talk nightmare talk "Just awnser the question. Don't choose this one again, okay? Or do. I don't care. We can do this all night."
            set nightmare_one_likeBoth true
            jump nightmare_one_choice
        else:
            talk nightmare talk "Fine. Be like that. Did I hear a 'I hate them both equally?'"
            jump nightmare_one_punishBoth
    "I like neither of them.":
        jump nightmare_one_punishBoth

nightmare_one_punishNasty:
    set nightmare_one_punishedCharName "Nasty Girl"
    set nightmare_one_punishedCharPronoun "she"
    choice:
        talk nightmare talk "Good! Then you agree with me! Nasty Girl deserves to be punished!"
        "I never agreed to that!":
            talk nightmare talk "Yes you did."
            jump nightmare_one_punishment

nightmare_one_punishLovely:
    set nightmare_one_punishedCharName "Lovely Lady"
    set nightmare_one_punishedCharPronoun "she"
    choice:
        talk nightmare talk "Good! Then you agree with me! Lovely Lady deserves to be punished!"
        "I never agreed to that!":
            talk nightmare talk "Yes you did."
            jump nightmare_one_punishment

nightmare_one_punishBoth:
    set nightmare_one_punishedCharName "Lovely Lady and Nasty Girl"
    set nightmare_one_punishedCharPronoun "they"
    choice:
        talk nightmare talk "Oh! It's like music to my ears! We really *do* agree on everything, don't we :) Then you agree with me? Lovely Lady and Nasty Girl *both* deserve to be punished!"
        "I never agreed to that!":
            talk nightmare talk "Yes you did."
            jump nightmare_one_punishment

nightmare_one_punishment:
    choice:
        talk nightmare talk "Sorry to be the bearer of bad news, sunshine, but unlike those other chumps you have swimming around in here like sewege I'm not just some annoying voice, I'm you. You want this to happen. You're doing this to *yourself*. In the colonies, that is, what's left of them, the military sometimes uses some cute little menouvers called 'echanched interrogation techniques'. One of those is something called a stress position. 'But nightmare! I'm always stressed!' I hear you cry! Aha. Don't worry, this is a whole different kind of stress. I think [punishedCharName] will enjoy it. Don't worry, [punishedCharPronoun] won't remember it when they wake up. Probably."
        "Whatever. (Accept [punishedCharName]'s fate and move on)":
            jump nightmare_one_wakeup
        "Please don't hurt [punishedCharName]!":
            jump nightmare_one_brink


nightmare_one_brink:
    choice:
        talk nightmare talk "On the edge, you see it don't you? The thing."
        "On the edge?":
            choice:
                talk nightmare talk "Of the basin you've gotten yourself trapped in. There's not much to do down here but look at it, hmm? I think one of your hairs is over there, about a meter thick, but what are you going to do with that? gnaw on it? No. There's *something* there. Teetering on the brink of the cliff. A feather in the right place would send it tumbling. Falling. Sliding down to meet you. When you squint at it you can see the insects gnawing into it. You can see the colour of your own eye."
                "What is it?":
                    choice:
                        "Why don't you take a look? Not that I reccomend it."
                        "It's far away, I can't reach it.":
                            choice:
                                "You can make it fall. Make it slide down to meet you. You shouldn't though. There will be no going back."
                                "(Leave it alone (CHOOSE THIS))":
                                    jump nightmare_one_wakeup
                                "(Let it fall. Let it slide down to meet you)":
                                    jump nightmare_one_fall
                        "I don't want to.":
                            jump nightmare_one_wakeup
                "I'd like to wake up now.":
                    jump nightmare_one_wakeup
        
nightmare_one_fall:
    set global_nightmareAlive true
    ""
    "They're the kind of bugs that seem to appear spontaniously around a corpse. The kind you never see elsewhere. A worm, long, endless, curls its way through the things bulk. Sometimes internally, sometimes externally."

    "It's you, just about. The fur is more wirey, the face more gaunt, the eyes more cold, but it is you. It was you. You were it. It breathes, barely, as though taking its last breath forever. It's eye twitches just enough to seem alive. It was you. And it could be you again. Part of you wants it to be you again, doesn't it?"

    "Its outside is ghastly, but you know that inside is something far worse. A trickle of ink black sludge leaks from the corner of the things maw and pools around its head. Tapeworms writhe inside it. Pale. Almost translucent. The thing you look at is no mammal. It is a monster."

    talk nightmare talk "There's the cliche isn't there? Of the sad person wearing a smiling mask to hide their pain. You dont need to do that. Your little face already wears a mask. It's etched into your face forever. Your bones bend around it. Your brow shades it in shadow. Your jawline puncuates it like an exclamation point. The fur around your maw gilds it like gold leaf. There is no removing this mask, and try as you might, it will always be there, one layer of epidermis below the surface, staring back at you in the bathroom mirror, forever."


    choice:
        talk nightmare talk "it's me."
        "I thought you said it was me.":
            talk nightmare talk "mhm. dwell on that, 'sis'."

    "I didn't want to remember this. I don't want this. I want to wake up.":
        choice:
            "You were so eager to see it before though, weren't you? I did tell you to leave it alone. There is a serenity to oblivion. Some experience this joy when they returned home from the war. The past was a howling maelsturm of brutality, but to delve so far into it was to find the eye. The place where the terrors swirl around, but are out of reach. You are blessed to have found this place. Why did you want to leave?"
            "Not everyone who came back from the war forgot. Some of them scream. Some of them cry. Some of them lay awake at night.":
                choice:
                    "You're sound asleep right now, but if it pleases you, why not have a scream? Why not cry?"
                    "Scream.":
                        jump nightmare_one_scream
                    "Cry.":
                        jump nightmare_one_scream
                    "I'll be ok.":
                        ""
                        jump nightmare_one_wakeup
            "I didn't want to leave. You tricked me into looking at it.":
                "No I didn't. You chose to look. You made it fall. You made it slide down to meet you, remember? Dont try to stain my conciouss with your bile."
            "Can I go back?":
                "No."
            "I'll be fine. This isn't so bad.":
                "Tell yourself that now, if it makes you feel better. That won't stop the thing from staring back at you from the mirror every single day for the rest of your life."

nightmare_one_scream:
    choice:
        "More."
        "(Scream)":
            jump nightmare_one_scream
        "(Cry)":
            jump nightmare_one_scream
        "I'm done. I'm going. I'm waking up so I don't have to listen to you anymore.":
            jump nightmare_one_wakeupNightmare

nightmare_one_wakeupNightmare:
    talk nightmare talk "Oh don't worry, I'd never *dream* of abandoning you again. Someone needs to be looking out for you, right? Goodness knows orb and your little lady friends won't tell you the truths you need to know."
    jump home

nightmare_one_wakeup:
    choice:
        talk nightmare talk "When I said before I'd stay here until you wanted me back? I lied. I'll be coming with you when you wake up. I'll see you soon."
        "You told me you'd leave me alone and just hurt [punishedCharName]!"
            talk nightmare talk "I lied. Besides, friends don't let friends hurt friends, so you deserve this really :)"
    jump home