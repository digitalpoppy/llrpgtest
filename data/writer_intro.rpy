writer_intro:
    clear_dialog
    "You are awoken by a knocking at your door. Not a friendly knocking either, a rude one."
    $if this.skillCheck("writer_intro_cops_nasty", "nasty", 40):
        choice:
            talk nasty talk "It's the pigs! Quick! Jump out the window!"
            "(Jump out of the window)":
                "Your skull bashes into the glass and bounces off. It hurts, but what did you expect?"
                talk nasty talk "Haha."
                talk orb talk "Ghost is very delicate, Nasty Girl, more porcelin doll than woman. Please stop encouraging her to do stupid things."
            "(Don't do that)":
                talk orb talk "Thank you for not jumping out of the window, Ghost."
        "There's another knock. This one is *very* unfriendly."
        choice:
            talk nasty talk "Shit. We're done for gang. We're going away for a long time if they rozzers know about my time with the Cawmden Cocksuckers."
            "The Cawmden what???":
                talk nasty talk "Cocksuckers. You can say the word, it won't bite you. Biting's a big foe pass in the cocksucking industry, y'know?"
                talk lovely talk "Sigh. It's 'faux pas', and the Cawmden... whatever, is the name of her old 'gang', if you could call it that. Beastly behaviour, but hardly Lundens most wanted. They were mostly responsible for petty vandilism and public noise complaints, as well as crimes against common decency."
                "The thumping on the door continues. It's even less friendly now."
            "I'm not taking that bait.":
                "The thumping on the door continues. It's even less friendly now."
    talk orb talk "You should probably get that. It might be important, and by 'might be important' I mean 'is important'."
    $if this.skillCheck("writer_intro_clothes_lovely", "lovely", 20):
        set writer_intro_wearClothes true
        talk lovely talk "Please remember to get dressed first, sweetie."
        talk nasty talk "Literally why. Who cares. It's our house and we can be naked if we want. Pretty sure that's in the Brüssel Accords or some shit."

    choice:
        "The knocking intensifies. Whoever is downstairs would rather be anywhere than at your door, but they have no choice, it seems."
        "(Go downstairs and open the front door)":
            set global_writerNaked true
            $if this.data.writer_intro_wearClothes:
                talk lovely talk "Um, darling, aren't you forgetting something?"
                talk nasty talk "AWOOOOOO! WE'RE DOING THIS! FUCK YEAH!"
        "(Put on your clothes, then go downstairs and open the front door)" $if this.data.writer_intro_wearClothes:
            talk nasty talk "Cuck. Clothes cuck. Whatever. Fuck you. I'm going back to sleep."
            talk lovely talk "No you aren't, cease throwing a wobbley and act like a grown up."
            talk nasty talk "..."

    $if this.data.global_writerNaked:
        "Behind your door is a woman, she looks to be in her late twenties, save her eyes, which look older. She's just lit a cigarette, for warmth, more than anything else. The door is barely open before she begins talking. The fact that you're completely naked seems not to phase her beyond a momentary flash of a raised eyebrow."
        $if !this.data.writer_intro_wearClothes:
            talk lovely talk "Oh my gods, we're naked. How did we not notice that?"
            talk nasty talk "Is that a problem? Who cares, this is great. Being naked rules."
            "The Pulp Writer stares at you, unblinking."
        talk lovely talk "Terrifying. This woman does *not* care."
        talk nasty talk "Incredible. I love her. We should be friends with her. We'd never have to get dressed again."
    else:
        "Behind your door is a woman, she looks to be in her late twenties, save her eyes, which look older. She's just lit a cigarette, for warmth, more than anything else. The door is barely open before she begins talking."

    choice:
        talk writer talk "Our dickhead 'boss' probably already explained this to you, but I'm collecting."
        "Sorry, who are you?":
            talk writer talk "What the fuck do you mean 'who are you?' I just said, didn't I?"
            talk orb talk "She didn't."
            $if this.skillCheck("writer_intro_whoAre_lovely", "lovely", 40):
                talk lovely talk "Don't point that out. She doesn't care, and it'll just annoy her. She's as tightly strung as a violin, this one."
                talk nasty talk "'A violin'. Embarassing. Guitar for bottoms."
            choice:
                "The woman eyes you with disdain. It isn't for you so much as it is for the situation she has been forced into by the enigmatic being know only to you as 'Our Boss'."
                "Correct. You did. Please continue.":
                    "She breathes a sigh of relief. She wants this over as soon as possible."
                "Okay but you didn't introduce yourself though sooooooo...":
                    talk writer talk "Look. Does it fucking matter?"
                    "It appears to matter to her. She looks like she's about to pop a blood vessel."
        "You're 'collecting'?":
            talk writer talk "That's what I said, yes."
            talk orb talk "It is what she said, yes."
            talk lovely talk "Collecting what? Blood? Taxes? Is this the tax woman? Fuck. We need to go upstairs and jump out of that window *now*."
            talk nasty talk "Summershire estate been cooking it's books, eh, Lovely Lady?"
            talk lovely talk "No! Certinaly not! Papi is just creative with our accounts in a way *some* are too common to understand!"

    choice:
        talk nightmare talk "hi. yeah, it's me. i hope you didn't forget me. i'm here too now :) anyway I thought I'd wait till after your conversation started to let you know you havent trimmed your facial fur in two days. you look hidious. lmao."
        "OH FUCK."
            talk nightmare talk "oh fuck! haha. yeah. that's about right"
        "I FORGOT I HAD TO DO THAT.":
            talk nightmare talk "then it's a good thing you have a friend like me to help you out :)))"
        "It's fine. I don't mind having facial fur.":
            choice:
                talk nightmare talk "you do mind, sorry : ) you look like a m"
                "I look like a 'm'?":
                    talk nightmare talk "a man : )"
                "Don't finish that word.":
                    talk nightmare talk "ok. i dont need to. you just said it in your head for me, right? thats on you."
    
    choice:
        "Your muzzle itches. It feels dry. Wirey, like a tin scourering pad. It could cut someone, were they to run their hand across it. Yesterday was nice, but the wriggling and squirming deep *deep* inside you is back now. Perhaps forever."
        "Why did you wait until *now* to tell me???":
            choice:
                talk nightmare talk "because i hate you. lol. lmao."
                "*Why* do you hate me?":
                    talk nightmare talk "huh? i dont??? what? i love you. we're friends remember. i look out for you, like just now i helped you remember that you were untrimmed. im nice actually? fuck you. I love you."
        "Whatever. I'm busy.":
            talk nightmare talk "ok champ, ignore it, it's fine. not like facial fur gets a little longer and a lottle more visible the longer you leave it alone or anything : )"

    $if this.data.global_writerNaked:
        "The pulp Writer clears their throat. The sound of a storm drain clogged with shrapnel and viscera. They're glaring at you in frustration. You feel *so* naked."
    else:
        "The Pulp Writer clears their throat. The sound of a storm drain clogged with shrapnel and viscera. They're glaring at you in frustration."
    choice:
        talk orb talk "You've been silent for about twenty seconds now. Are you okay? What's the matter?"
        "You didn't hear any of that?":
            talk orb talk "Excuse me? Hear any of what? Are you okay, Ghost?"
    talk writer talk "Hello?"
    talk orb talk "Forget it. Just try to hold this conversation. Please. It seems important."

    choice:
        talk writer talk "Your article. Can I take it?"
        "(Nod) Yes. My article. Of course.":
            talk writer talk "Okay. Where is it? I *really* need to get going."
            talk orb talk "You *don't* have an article. Why did you say that? Did you just assume you did? You didn't even think to check with me?"
            $if this.data.global_getMotorcycle:
                talk lovely talk "First the motorcyle, now this. Please stop telling people you have things you dont. It's going to land us in a lot of trouble sooner or later."
            choice:
                talk writer talk "Well?"
                "Uuuuuuh uummmmm uuuuuh...":
                    talk lovely talk "This is excrusiating."
        "Let's take a step back. I'm supposed to have an article?":
            talk writer talk "You d- I- What have you been doing for the last week, jerking off and getting high?"
            $if this.data.global_writerNaked:
                "They look up and down your tired, pale, exposed body."
                talk lovely talk "They're wondering if you're *still* high. The 'jerking off' is now assumed."
            talk nasty talk "I wish. We should do that. Drugs and jerking off I mean. We should get some drugs and then *do* the drugs and then jerk off. We should buy drugs and jerk off, everyone."
            
    choice:
        talk writer talk "You haven't written an article, have you?"
        "No. Sorry. Was I supposed to?":
            "The Pulp Writer sighs. She is *so* tired."

    talk writer talk "We're running a piece called 'Heroes of the Great War', that is to say an interview with a real life Bluehills 'war hero'. You were given the job because noone else wanted to do it, and as the newest writer at 'Weird Tails', you were least likely to put up a fight. That's where you work, Weird Tails magazine, in case you'd somehow forgotten that too."
    jump writer_intro_menu

writer_intro_menu:
    choice:
        "The Pulp Writer picks at something on her hand. She does this a lot, when she can feel things spiralling out of her control. Smoke curls away from her momenterily unattended cigarette."
        "Can you tell me a little about Weird Tails, just as a refresher. I only just woke up and I'm still half asleep. I do *not* have amnessia.":
            choice:
                talk writer talk "You have amnesia? Like, you actually have amnesia? Fucking hell. I am *not* being paid enough to deal with this shit."
                "No no, I said I *don't* have amnesia.":
                    talk writer talk "Whatever. Whatever."
                    "She taps some ash off of the end of her cigarette. The embers die out on the mildew below. Your doorstep is quite overgrown."
                    $if this.skillCheck("writer_intro_mildew_orb", "orb", 20):
                        talk orb talk "The cottages previous owner spent a lot of time abroad on bussiness, the unkempt state of their cottage reflects this, but not them themself. They were every so pretty."
                    talk writer talk "Weird Tails is Anglias 'premium' magazine for 'quality' short literature, 'scary' articles and 'thought provoking' non fiction, or so the tagline claims. In reality it's tripe. Utter tripe. But it pays the bills, that's why you joined us, right?"
                    "She looks down at her hand. It's fur is a mess from her incessent picking."
                    talk writer talk "Gods, I could be doing so much more..."
                    "She stares off into the horizon. It's the first time she's lost focus on her purpose here since she arrived. Her nose twitches abcent mindedly, breathing in some smoke."
                    talk writer talk "Anyhow. That's Weird Tails. You're writing an article for it."
                    jump writer_intro_menu
        "An article about a war hero doesn't seem all that weird, for a magazine called 'Weird Tales', I mean.":
            choice:
                talk writer talk "It isn't, it's shit. Waste of a fucking page, but it's what the editor wants. They're right though, if we don't run some bullshit fluff piece about our *brave war heros* we'll get savaged by the Anglian Mail, and they already have a noose around our fucking neck after we ran that filth a few months back..."
                "Filth? Tell me more.":
                    set global_weirdTailsFilth true
                    talk writer talk "No."
                    $if this.skillCheck("writer_intro_filth_orb", "orb", 20):
                        talk orb talk "It was *nasty*."
                    talk nasty talk "We should read it. Let's find a copy."
                    talk writer talk "The less said about that the better."
                    jump writer_intro_menu
                "(Nod like you actually understand anything she's talking about)":
                    jump writer_intro_menu
        "Sorry I'm naked by the way." $if this.global_writerNaked:
            "The Pulp Writer takes a drag of their cigarette."
            talk writer talk "You think I give a shit?"
            jump writer_intro_menu
        "What should I do? (Move on)":
            jump writer_intro_whatToWrite

writer_intro_whatToWrite:
    choice:
        talk writer talk "Just... interview someone. Anyone. It only needs to be a page long. If they were in the war they're a 'hero' as far as the public is concerned. Our brave boys, girls and non binaries could kick an orphan in the face and the mewling masses would still lick their fucking boots. Do that, write it up, and bring it to me by the end of the day and I'll be out of your fur."
        "(Nod) I'll have an article for you by the end of the day, I promise.":
            talk writer talk "Good."
        "(Nod) I'll make you proud, fellow writer. (Salute them)":
            "She rolls her eyes under her breath. Somehow."
        "No I mean what *exactly* am I writing? Please be more specific. Walk me throgh it word by word please.":
            talk writer talk "What the fuck are you even asking me? I'm your coworker, not your goddamn babysitter. What, you don't write your own notes? Just bring *something*, *anything* publishable to my apartment by the end of the day, I'm *begging* you."

    "She hands you a piece of lined paper. The penmanship is near unreadable, but it appears she's scrawled an address on it: her apartment in Bluehills."
    talk writer talk "Get it done."
    "With a billow of warm smoke she is gone. The Pulp Writer is not one for fanfare. A breeze passes over you. It's a cold morning."
    talk lovely talk "Such style! It's unbefitting of one so unkempt, frankly."
    choice:
        talk orb talk "So. You're a writer. Any thoughts?" 
        "I'm so fucking pumped to write. I love this shit. Inject writing directly into my veins. AWOOOO!":
            talk nasty talk "AWOOOO!"
        "Orb! I don't know how to write!":
            choice:
                talk orb talk "Yes you do, you'd not have gotten the job otherwise, I suspect."
                "If you're sure. Let's get this done.":
                    talk lovely talk "I belive in you, Ghost."
    choice:
        talk orb talk "Hold your sheep pal, you don't have any writing equipment, do you?":
        "I don't?":
            choice:
                talk orb talk "All your writing stuff was on your desk, which was vapourised, remember. You're going to need a notepad, a pencil, paper and a typewriter."
                "Fuck! Godsdamn it! Fuck! Nooooo! I give up! FUCK!!!!":
                    talk lovely talk "Please, show some decorum."
                "But I want to write *now*!":
                    talk orb talk "Well I'm sorry, but you can't."
    talk orb talk "The shop in town sells some of this stuff, right? And perhaps The Weird Nerd knows where you can find a typewriter, they mentioned having one, after all. Perhaps you even have some of it already? It's worth looking around, don't you think? Finding a war hero to interview might prove somewhat more difficult."
    $if this.skillCheck("writer_intro_whatToWrite_guy_nasty", "nasty", 40):
        set global_writerMakeUpAGuy true
        talk nasty talk "We could literally just make up a guy. Who'd stop us? Orb, if you try to stop us I'll come at you with a knife."
        talk orb talk "Uhuh. If you say so, Nasty Girl."
    jump writer_intro_writing_menu

writer_intro_writing_menu:
    choice:
        "Somewhere in the distance a crow caws. Somewhere further a magpie caws back."
        "What about The Weapon? They did war stuff, didn't they?":
            $if this.skillCheck("writher_intro_whatToWrite", "lovely", 40):
                talk lovely talk "I don't get the impression they want to discuss that with you, but you're correct, they 'did war stuff'."
            else:
                talk lovely talk "They 'did war stuff', yes."
            jump writer_intro_writing_menu
        "What about The Raven? They're a hero, right?":
            $if this.skillCheck("writer_intro_whatToWrite", "lovely", 40):
                talk lovely talk "People certinaly seem to think so, yes. The Raven herself is less sure."
            else:
                talk lovely "People certinaly seem to think so, yes."
            jump writer_intro_writing_menu
        "Could you not just tell me about a war hero, Orb?":
            talk orb talk "I suppose so? I'l not convinced I'm reliable enough for that to be a good plan though, as much as it pains me to admit it."
            jump writer_intro_writing_menu
        "We *could* just make up a guy." $if this.data.global_writerMakeUpAGuy:
            talk nasty talk "There is literally no reason not to. I spend most my day making up guys. I leave the making *out* for the chicks, heheh."
            talk lovely talk "While it would be rather uncoothe to lie to our new aquaintance and make up a guy, papa always says one should work smarter not harder. Eh, let's do it. C'est la vie, c'est la vie"
            talk orb talk "Bad idea. Bad idea. Bad idea."
            jump writer_intro_writing_menu
        "(Move on)":
            jump writer_intro_ending

writer_intro_ending:
    talk orb talk "We should stop standing around in the doorway like a... door, and get going. We've a lot to do today, Ghost."
    choice:
        talk nightmare talk "wow! sounds like you're going to be really busy today! anyway, i think it'd be neat if we went to the cathedral and thought about all your fuck ups for a bit? lets do that. a one on one. its healthy, like eating a carrot made of shit."
        "I'll think about it.":
            talk nightmare talk "nice. see you there bestie."
        "Shut the fuck up, please.":
            talk nightmare talk "yikes. fine. treat your only real friend like dirt and see how far that gets you. whatever i guess, bitch."