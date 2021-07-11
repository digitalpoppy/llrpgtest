

nerd_flirt_hitOnNerd:
    $if this.skillCheck("nerd_hitOnNerd_appearence_nasty", "nasty", 20):
        talk nasty talk "Wait. We need to work on our appearence. This nerd? She's a shark. If she sees a sign of weakness she will rip you to shreds."
        $if this.skillCheck("nerd_hitOnNerd_sharks_orb", "orb", 20):
            talk orb talk "As sharks do."
        choice:
            "The nerd continues to sort through her books, seemingly unbothered by your precense."
            "Ok Nasty Girl, do you have an suggestions?":
                jump nerd_suggestions
            "I think we'll be fine, to be honest. (Move on)":
                jump nerd_hitOnNerdTwo
    jump nerd_hitOnNerdTwo

nerd_suggestions:
    $if this.data.hasCig:
        talk nasty talk "That oestrodil ciggarete. Light it up. Dames love the intoxicating smell of 'Osetro' brand Oestrodil leaves."
        talk lovely talk "You are so embarassing."
        choice:
            talk nasty talk "Ignore Lovely Lady. This will really impress the nerd, trust me."
            "(Light an Oestrodil cigarette)":
                "The nerd looks up with a frown."
                talk nerd annoyed "No smoking in the library, lovely."
                talk nasty scared "F fuck!!!! shit!!! what the fuck!!!"
                talk lovely sad "Why do *I* get the blame for this?"
                talk nerd top "You don't want me to have to take you to the side and tell you off, do you?"
                talk nasty excited "YES HAHAHAHA YESSSSSSS!!!!"
                jump hitOnNerdTwo
            "I'll pass on that one.":
                talk nasty angry "Ugh, fine."
                "Nasty girl seems to abstractly throw up her shoulders."
                talk nasty talk "I don't know. Smirk smuttily?"
    jump hitOnNerdTwo

nerd_hitOnNerdTwo:
    talk nerd talk "Is there something I can help you with?"
    $if this.skillCheck("nerd_hitOnNerdTwo_fucking_nasty", "nasty", 60):
        set nastyIdea true
        talk nasty talk "Ask her if she can help you find the book 'Fucking Cute nerds'."
        talk lovely talk "Oh my gods do NOT ask her that."
        talk orb talk "She wouldn't mind. She's had fantasies about exactly this sort of situation, and you don't have to be omnipitent, which I am, by the way, the know that she finds you cute and would absolutely *love* to 'get with you', as Nasty Girl says. Wait, why am I helping you with this, you should be concentrating on getting me out of you."

    $if this.skillCheck("simple", "lovely", 50):    
        talk lovely talk "You should call her eyes pretty : )"
        $if this.skillCheck("simple", "nasty", 20):
            talk nasty talk "Fucking hell. No wonder you've never gotten laid."
            talk lovely talk "I am going to take the high road and ignore that."

    choice:
        ""
        "I'm looking for a book.":
            jump nerd_fuckingCutenerds
        "You have pretty eyes : )"
            jump nerd_prettyEyes
        "I uhh uhhhh hhhh":
            "She squints at you through her spectacles. You can't see her eyes, but you can tell."
            talk nerd talk "Well. Let me know if you change your mind."
            talk orb talk "She's forgiving. When you work with the public for as long as she has you learn to be."
            jump nerd_menu

nerd_fuckingCutenerds:
    "She smiles."
    choice:
        talk nerd talk "Could you be more specific?"
        "It's called 'Fucking Cute nerds'. It's an instruction booklet, moreso than a book, I suppose.":
            jump fucknerd
        "It's called uhhhhh actually never mind sorry. Sorry.":
            "A raised eyebrow."
            talk nasty talk "That's good right? Raised eyebrows are smutty!!!"
            talk lovely talk "Some raised eyebrows may contain trace amounts of smut; this one doesn't."
            talk orb talk "She thinks you're having a nervous breakdown."
            talk nasty talk "F-fuck! Godsdammit! This is why you should *listen* to me!!!"    

nerd_prettyEyes:
    talk nasty angry "Oh my god it's like you're *trying* to cuck youself."
    "She looks at you through her impenetrable, practicaly frosted spectacles. Her eyes remain entierly hidden. She giggles."
    talk nerd talk "Oh you. That's very sweet. Thank you. Your eyes are rather beautiful themselves."
    "She grins slyly."
    talk nerd talk "You're cute. I have a book reccomendation for you, if you're interested?"
    $if this.data.nastyIdea:
        talk nasty talk "I TOLD YOU! I TOLD YOU! DIDN'T I TELL YOU? nerdS *LOVE* BOOK PICK UP LINES."
    "She's looking at you nervously."
    choice:
        talk orb talk "She's naturally confident, but she's somewhat worried she has overstepped a boundry here. You *are* just a library cusomter, after all."
        "What's the book?":
            talk nerd neural "It's called 'Muzzled in the Library', by *me*."
            talk nasty talk "Holy fuck."
            choice:
                talk lovely talk "O-oh goodness."
                "S-sounds g-g-good.":
                    "'g-g-good'"
                    "She's making a note of that one for later."
                    jump fucknerd
        "I should go. (Leave)":
            talk nasty talk "OH MY GODS WHY WHAT ARE YOU DOING ARE YOU JOKING WHY ARE YOU EDGING ME LIKE THIS???"
            talk nerd talk "O-oh. Okay. I'm sorry. I'll just..."
            "She looks down at the books."
            talk nerd talk "Get on with my work..."
            talk orb talk "Her day is ruined. You're probably not going to be able to salavage this one, sorry."
            jump library




fucknerd:
    "The straight romance section."
    $if this.skillCheck("simple", "orb", 25):
        talk orb talk "No one ever comes here."
        talk nasty talk "Except you, if you're lucky."
        "Nasty Girl winks smuttily."
    talk nerd talk "So, 'Fucking Cute nerds', huh?"
    talk nerd talk "I'm afraid that's out of stock..."
    choice:
        talk nerd talk "But we do have a few copies of 'Muzzled in the library', by *me*."
        "Hhhhh.":
            "She smirks. Your lack of coherent verbal response speaks volumes, despite its relative silence."
            "She *likes* silence."
            "But she *loves* enforcing it."
        "You *really* don't have 'Fucking Cute nerds' in stock?":
            talk nerd talk "No."
            "She smirks. 'I do the fucking here', she's thinking."
            
    "She laughs dryly. She finds it ever so cute when you try to pretend you're in charge."
    "You aren't."
    $if this.skillCheck("simple", "nasty", 25):
        choice:
            talk nasty top "Says who? Dont give up, coward, you're like a foot taller than her, that makes *you* the top!!!"
            "I think you're a little short to be giving me orders, dont you?":
                set height true
                talk nerd top "Oh?"
                "She slaps you. Not painfully so, but enough to briefly shock you into a more malleable form."
            "(Say nothing)":
                talk nasty angry "Oh my gods you are such a bottom. Pathetic."
    
    "She pushes you to your knees, and looks down at you. \"Doesnt this suit you so much more?\""
    choice:
        ""
        "This *does* suit me so much more":
            "A thumb pushes through your lips."
            talk nerd top "I didn't say speak, pet."
            set thumbInMouth true
            choice:
                talk nerd top "Isn't is so much nicer to just. stay. quiet."
                "Nod.":
                    talk nerd top "Good girl."
        "(This *does* suit me so much more":
            "She smirks. She knows you agree. She can see it reflected in your pleading eyes."
        skillcheck simple nasty 50 "I'm not so sure, actually. (Get up)":
            success ""
                jump topnerd
            failure "She shoves you forecefully back to your knees. A snarl working silently onto her face."
                choice:
                    talk nerd top "What was that?"
                    "I said I wasn't so sure, actually.":
                        "A thumb pushes through your lips."
                        talk nerd top "I didn't say speak, pet."
                        set thumbInMouth true
                    "(Stay silent)":
                        talk nerd top "That's better."
                        "her mouth breathes against your ear."
                        talk nerd top "Isn't it? Pet."
    jump bottomnerd

bottomnerd:
    ""
    choice:
        talk nerd top "You're in a library. Show some respect, and stop. Talking."
        "(Talk)":
            ""
        "(Nod)":
            ""

    talk nerd top "You've been so good so far, so quiet, so respectful, so obidient."
    "She seems to breathe that last work directly into your ear as though it were your own mind conjouring it up."
    talk nerd top "Now open your mouth, lovely. Be good."
    talk lovely talk "Is she talking to me?"
    talk nasty top "No, but you can do it for me, if you want."

    talk nerd top "It's really quite endearing how quickly you've learnt your place."
    talk nerd top "You're such a *good* girl."
    $if this.skillCheck("simple", "nasty", 50):
        choice:
            talk nasty feral "This is it. This is your last chance. Do it. You know you want to."
            "Do what?":
                talk nasty feral "dO wHaT???"
                talk nasty feral "Less talking, more chomping."
                set chomp true
    "She leans close."
    choice:
        talk nerd top "Say it. Say 'I'm a good girl'."
        "Mff mf mfff mfff.":
            "She smirks. Theres the hint of a warm smile shining from the polished enamal of her teeth."
        "(Say nothing.)":
            ""
        "(Bite her thumb.)" $if this.data.chomp:
            ""

    $if this.data.height:
        talk nerd top "So now that you know your place, you won't get any funny ideas about our relative heights, will you, lovely?"
    else:
        talk nerd top "So now that you know your place, you'll always be on your knees for me in spirit, won't you, lovely?"
    talk lovely talk "What about that time?"
    talk nasty talk "Oh my gods stop talking Lovely Lady you're killing the mood."
    "The nerd withdraws her thumb from your mouth. A strand of saliva glistens for a moment before breaking and hanging from your lips."
    talk libraian top "Stand up, lovely."
    "Lovely Lady does not respond this time; she's pouting too hard."
    choice:
        talk nerd top "Go on, be a good girl and stand up for me."
        "(Stand up)":
            "She looks up to you again, but it doesn't feel like it. She towers over you more now than she did when you were at her feet."
            "She looks so proud of herself."
            "She looks so proud of *you*."
            "She meant what she said: You *are* a good girl."


    "She presses your face into the bookcase. The dustcovers are bitingly cold against your cheek. The memories of her warm touch aches in response.."
    "Your eye focuses for just long enough to read the title of the book it's held against before it instinctivly closes."
    talk orb talk "'An Evening Under Blossom'. It's a classic of the genre. Wildly regarded as the best piece of hetrosexual erotica ever written. It's been borrowed from Bluehills Library *three* times over the past decade."
    choice:
        talk nasty angry "Oh my gods *please* shut the fuck up we're trying to CUM here."
        "This book actually sounds really interesting, tell me more.":
            jump eveningUnderBlossom
        "This book actually sounds really interesting, tell me more. (But sarcastic.)":
            set sarcastic true
            jump eveningUnderBlossom
        "Okay. Thanks for sharing? (Move on.)":
            jump fucknerdTwo

eveningUnderBlossom:
    "lengthy description of the plot"
    choice:
        ""
        "Thanks for sharing.":
            ""
        "You know I was being sarcastic when I said I wanted to know more?" $if this.data.sarcastic:
            talk orb talk "I didn't pick up on that. Sorry."
    choice:
        talk nasty girl "Can we move on?"
        "Let's.":
            ""

fucknerdTwo:
    ""
    $if this.data.bratting:
        "She fumbles with something."
        $if this.skillCheck("simple", "orb", 10):
            talk orb talk "It's the ribbon on her hat. She's taken it off."
            talk nasty talk "Why is she fumbling with a hat instead of us. This is stupid."
        "a silk ribbon wraps itself around your wrists, holding them tightly, and securely together behind your back."
        talk nasty bottom "Nice."
        talk nasty scared "I mean noooo don't restrain me im a top im a top."
        talk nerd top "Since I apparently can't trust you to  be a good girl all the time, I'm just going to have to *make* you be a good girl for me, hmm?"
        "Her smirk is audiable."


    "You can feel her press against you."
    set q_smellnerd false

topnerd:
    ""


nerd_flirt_reveal:
    choice:
        talk nerd talk "Oh, I mean I'm not actually a nerd. I just like to spend time here somethimes, y'know?"
        "What.":
            ""
        "Why did you fetch us books???":
            talk nerd talk "Well you clearly thought I was a nerd and I didn't really know how to explain otherwise, is the thing."




            
nerd_flirt_snugglepupping:
    talk nasty talk "Lady, she just invited you *snugglepupping*, you know what that means, right?"
    $if this.skillCheck("nerd_flirt_snugglepupping_pupping_lovely", "lovely", 40):
        talk orb talk "Snugglepupping parties are a gathering primarily for the purpose of cuddling and light affection. They became popular once the rabies pandemic ended and people realised they hadn't felt the touch of another person in over a year."
        talk orb talk "Light refreshments, sometimes even *wine* and *oestrodil leaves* are provided."
        set orbKnowsSnugglepupping true

    choice:
        ""
        "I don't know what 'snufflepuffing' is, no.":
            talk nasty talk "Two words."
            talk nasty talk "Or. Gy."
            $if this.skillCheck("simple", "lovely", 20):
                talk lovely talk "That's not how words work."
            if this.data.orbKnowsSnugglepupping:
                talk orb talk "Again, snugglepupping parties are a gathering primarily for the purpose of cuddling and light affection. They became popular once the rabies pandemic ended and people realised they hadn't felt the touch of another person in years."
                talk orb talk "Light refreshments, sometimes even *wine* and *oestrodil leaves* are provided."
                talk orn talk "I don't know why I'm having to reexplain this."
        "Of course I know what 'snuzzlepawing' is. (You don't)" $if !this.data.orbKnowsSnugglepupping:
            talk nasty talk "Then what are you waiting for, we should be getting ready!"
        "Of course I do, snugglepupping parties are a gathering primarily for the purpose of cuddling and light affection. They became popular once the rabies pandemic ended and people realised they hadn't felt the touch of another person in years. Light refreshments, sometimes even *wine* and *oestrodil leaves* are provided." $if this.data.orbKnowsSnugglepupping:
            talk nasty talk "Source?"
            talk orb talk "Me. The all knowing orb."
            talk nasty talk "Peh. We'll see."

    