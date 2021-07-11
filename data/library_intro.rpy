library_intro:
    set global_actionsleft = 4
    set_screen default
    set_button button_library_intro false
    set_button button_mechanic_intro true
    "Bluehills is a historically significant city, to be sure, but the library feels altogether more regal than its surroundings."
    talk orb talk "The library was built in the 1700s, when Anglia was an Imperial territory and Bluehills was, for at least a short period, the regions capital. It was a peace offering in the form of architecture. The glories and power of the Brennenburg dynasty hewn into marble floors and stone columns. Before the war it was known as the Vildenberg Archive, but it was renamed simply to the Bluehills City Library for propoganda reasons. It survived the war unharmed - an Imperial Junker-II managed to get a bomb through one of the ceiling windows, but the triggering mechanism jammed - and so has avoided the cheap restoration that so much of the city has been marred by. Most of the obvious Imperial iconography was chiseld off after the Anglian Revolution, the more obscure iconography during the war. Atop the four main pillars in the main hall are the carved marble faces of Emperor Vildenberg Brennenburg, Crown Prince Wilhelm Gladesparkle, and anonymous Grand Inquisitor and the Imperial Sheep, Woolenberg XI. They survive to look down on the building only because the city did not have a long enough ladder to reach them."
    "A librarian, a short rat, sorts books on the desk in front of her. She seems the most approachable of the otherwise rather terse looking staff. She sorts through a pile, a mountain even, of books."
    $if this.skillCheck("library_intro_system_lovely", "lovely", 20):
        talk orb talk "She's sorting them into piles based on which wing of the library they need to be taken to, and in order of which shelf they need to be on. It's not the librarys official system, its hers."
    "She looks up at you and smiles, as service workers are oft to do, before returning to her task. You don't get a proper look at her eyes behind her almost comicly thick rimmed round spectacles, but you can tell they'd be pretty."
    $if this.skillCheck("library_intro_eyes_orb", "orb", 80):
        talk orb talk "They're green. Her parents used to describe them as emeralds, she always saw them as sunlight through oak trees. Still, she chose her name in honour of them."
    talk nasty talk "I bet she smells of paper. I bet if you sniffed her she would smell papery."
    choice:
        talk lovely talk "That would be rather predictable don't you think? She smells like lavander."
        "I think Nasty Girl is right.":
            set global_smellLibrarian true
            talk lovely talk "Sigh. I am as ever the undeserved pariah."
        "I think Lovely Lady is right.":
            set global_smellLibrarian true
            talk nasty angry "Fuck you. I'm right. Die."
        "I think you should both stop speculating on the musk of this random woman.":
            talk orb talk "I agree."
    talk librarian talk "Can I help you, lovely?"
    choice:
        talk lovely talk "Say yes please."
        "Yes please.":
            talk librarian talk "Wonderful. Just let me know how, okay?"
        "H-help me?":
            talk librarian talk "That's what I'm here for."
            "She grins. Your awkwardness is endearing. She likes it."
    "There's a slight accent behind her voice."
    talk lovely talk "It's Persian, or at least its Persian filtered through Anglian."
    talk orb talk "Her parents were born in Persia, she was borin in Anglia. Her Persian accent is almost inaudiable to the untrained ear."
    jump library_intro_menu

library_intro_menu:
    choice:
        "The Librarian returns to her work while she waits for your question."
        "Do you have any books I can borrow?" $if !this.data.global_hasHandbook:
            jump library_intro_books
        "I've changed my mind. Could I have that history book please?" $if this.data.global_hasHandbook & !this.data.global_hasHistorybook:
            "The Librarian smiles. She's glad you saw sense."
            talk librarian talk "Certinally Miss. I'll go and get it for you."
            jump library_intro_ammnesiaBook
        "Could I ask a personal question?":
            jump library_intro_personal
        "I should be going. Thank you for your help Mam'. (Leave)" $if this.data.global_hasHandbook:
            jump library_intro_nastyGirlsQuest
                
library_intro_books:
    set global_hasHandbook true
    choice:
        talk librarian talk "I should hope so!"
        "Do you have a copy of the Lovely Lady Handbook?":
            talk librarian talk "The Lovely Lady Handbook huh? We do."
    "She's looking at you differently now."
    $if this.skillCheck("library_intro_handbook_cringe_orb", "orb", 40):
        set library_intro_orbResearch true
        talk orb talk "She thinks you're one of *those* people. The ones obsessed with the lovely lady - nasty girl archetypes. Tell her its for research, not for personal use, im begging you."
    choice:
        talk librarian talk "Would you like to take out a copy?"
        "Yes please.":
            "She smiles, it's a little fake."
        "It's for research, not for personal use, I swear." $if this.data.library_intro_orbResearch:
            set library_intro_researchHandbook true
            talk librarian talk "Noted."
            "She's looking at you normally again."
            choice:
                talk librarian talk "But you do want to borrow a copy, yes?"
                "Yes please.":
                    "She smiles."
                    $if this.skillCheck("library_intro_handbook_help_lovely", "lovely", 20):
                        talk lovely talk "She likes to help people. It's why she works here."
    
    talk librarian talk "One moment, miss. I'll be right back."
    "She leaves the pile of books and dissapears into the depths of the library."
    talk lovely talk "She knows this place off by heart. She could find you any book you wanted and be back within moments."
    talk orb talk "She enjoys the logic behind the catogorisation system. She enjoys knowing that if she follows their directions she will find whatever she searches for."
    $if this.skillCheck("library_into_handbook_orders_nasty", "nasty", 20):
        talk nasty talk "There's only one thing she likes more than following directions. Giving them."
    "The library hums softly in her absence. Readers murmor to one another, clocks tick, pages rustle."
    "It makes the nerds reapperence and chirpy 'Hello again!' all the more startling."
    talk librarian talk "The Lovely Ladys Handbook, in mint condition. The library purchased an awful lot of them, and by the time we actually recieved them the fad was quite over."
    $if !this.data.library_intro_researchHandbook:
        talk librarian talk "I mean. The. Pretend I didn't say fad, would you, lovely?"
        "She forces a smile. She really hates this book, but she doesn't want to offend you."
    choice:
        talk librarian talk "Anyhow. Usually I'd do this all, if you'll excuse the pun, by the book, but honestly we could happily lose a few dozen copies of this and all that'd happen is we'd have more shelf space, so don't worry about bringing it back, hmm? Now, is there anything else I can find for you?"
        "Do you have any books that could be useful for an ammnesiac? Not that I am one.":
            $if this.skillCheck("library_intro_amnesia_amnesia_orb", "orb", 20):
                talk orb talk "She wonders if you have ammnesia, but is altogether too polite to ask."
    choice:
        talk librarian talk "We have some recent history books, I suppose. Would those help?"
        "Yes.":
            talk librarian talk "Wonderful! Let me go find you one."
            jump library_intro_ammnesiaBook
        "Those sound a bit boring actually.":
            talk librarian talk "I find history quite fun to learn about, personally. Although admitadly the last decade has been rather..."
            $if this.skillCheck("library_intro_amnesia_shit_lovely", "lovely", 20):
                set library_intro_lovely_shit true
                talk lovely talk "She doesn't want to use the word 'shit' in front of a customer."
            choice:
                talk librarian talk "un... fun... hasn't it?"
                "I wouldn't know, hence the need for the book.":
                    talk librarian talk "So you *do* want the book?"
                "It has been rather shit, hasn't it." $if this.data.library_intro_lovely_shit:
                    "She stifles a laugh."
                    talk librarian talk "Quite."
    choice:
        talk librarian talk "So, history book. Yay or nay?"
        "Yes, I look forward to a boring read.":
            talk librarian talk "Wonderful. Let me go find you one."
            $if this.skillCheck("library_intro_amnesia_job_lovely", "lovely", 20):
                talk lovely talk "She's glad she convinced you. Opening peoples minds to new material is one of her favourite things about her job."
                jump library_intro_ammnesiaBook
        "No, if the last decade has been as 'unfun' as you say I'd rather bathe in ignorence.":
            talk librarian talk "Suit yourself."
            $if this.skillCheck("library_intro_amnesia_bit_lovely", "lovely", 20):
                talk lovely talk "She thinks you're doing a bit."
            jump library_intro_menu

library_intro_ammnesiaBook:
    set global_hasHistorybook true
    "It is a little while before she returns, but she does, eventually."
    talk librarian talk "'This Woeful World: 1900-1926'. It was released only very recently, so it's about the best resource for catching up on current events you could ask for! Of course, it was written by an Anglian who was still high on victory fumes, so it is rather too patriotic in places. Still, it's good for a broad summary. I'm sure I can find some more academic material for you, should any specific topic in there interest you further!"
    $if this.skillCheck("library_intro_amnesiaBook_hopes_lovely", "lovely", 20):
        talk lovely talk "She *really* hopes you do."
    jump library_intro_menu

library_intro_personal:
    choice:
        talk librarian talk "Shoot."
        "Do you have a name?":
            jump library_intro_name
        "Your accent, is it Persian? My gut tells me it's Persian.":
            jump library_intro_persia
        "What do you do here?":
            jump library_intro_job
        skillcheck library_intro_personal_nasty_smell nasty 80 "Can I smell you? For no reason in particular." $if !this.data.library_intro_smellAttempt && this.data.global_smellLibrarian:
            success ".":
                jump library_intro_smell_success
            failure ".":
                jump library_intro_smell_failure
        "Let's talk about something else. (Move on)":
            jump library_intro_menu

library_intro_name:
    "She chuckles. She thinks you're funny, intentionally or not."
    choice:
        talk librarian talk "Yes. Most people do, don't they? Would you like to ask me what it is?"
        "Yes please.":
            choice:
                talk librarian talk "It's Emerald. I chose it myself a few years ago."
                "That's a nice name. (Nod)":
                    "She blushes, ever so slightly."
                    talk librarian talk "Thank you."
                    $if this.skillCheck("library_intro_name_chosen_lovely", "lovely", 20):
                        talk lovely talk "She still gets giddy when people call her by her chosen name."
                        jump library_intro_personal
                "(Just stay silent, you have no strong opinion on her name, despite asking about it)":
                    jump library_intro_personal
        "No, I prefer the mystery, I was just checking you *did* have one.":
            talk librarian talk "Then a mystery it can remain."
        "I'm not sure, do they? I forgot mine this morning.":
            talk librarian talk "Oh dear. Well, I'm sure it'll come back to you soon, hmm?"
            talk orb talk "Absolutely unfazed. Incredible."
            talk lovely talk "This is what having to talk to the general public on a daily basis does to a woman."
            jump library_intro_personal

library_intro_persia:
    talk lovely talk "Did you just call me your gut!?!?"
    talk nasty talk "Hahahahhahahaha. Get fucked Lovely Lady."
    talk librarian talk "It is, at least a little bit! I was born in Anglia, but my parents both came here from Persia, though I suppose it was part of the Osmanisches Empire at the time... Still, since my parents both had the accent I picked it up somewhat, though now that I'm not living with them it has rather melted into a quite dull Anglian drawl..."
    $if this.skillCheck("library_intro_persia_accent_lovely", "lovely", 20):
        talk lovely talk "She's genuinly quite said it is not more prominant. It was something that connected her to her parents."
    jump library_intro_persia_menu

library_intro_persia_menu:
    choice:
        ""
        "Why did they leave the Osmanisches Empire?":
            talk librarian talk "Because it looked like it was going to collapse at any moment. Mother was pregnent with me at the time, and didn't much fancy raising a child in the midst of a civil war. They were right of course, it did collapse. Albeit over a decade later, and only because they picked the losing side in the great war."
            jump library_intro_persia_menu
        "Why did they come to Anglia, specifically, I mean.":
            talk librarian talk "The country had much more lax immigration at the time. Needed a lot of labour for the coal mines and railway building projects that were going on. Also, it was the first stop the boat they took stopped at. So that helped."
            jump library_intro_persia_menu
        "Tell me about your parents.":
            "She continues arranging books, and does not look up at you."
            $if this.skillCheck("library_intro_persia_menu_parents_lovely", "lovely", 40):
                talk lovely talk "It's a touchy subject. Abort."
            jump library_intro_persia_menu
        "Let's talk about something else. (Move on)":
            jump library_intro_personal

library_intro_job:
    talk librarian talk "Well, I'm a librarian, as you may have guessed. It is my job to ensure the library runs smoothly. That guests can find books, that books are returned on time, that books are kept safe, that children get the books theye need for school, that the books are organised correctly... Ocassionaly I even get to *read* a book!"
    "She giggles gayly."
    choice:
        talk librarian talk "I like my job, in all honesty."
        "What happens if someone doesn't return a book?":
            "She titters."
            talk librarian talk "Try me and see."
        "That sounds like a nice lot in life. (Nod)":
            "She smiles."
            talk librarian talk "If you like being around books it's about as good as it gets."
    jump library_intro_personal

library_intro_smell_success:
    set library_intro_smellAttempt true
    
    "It's paper, but paper sprayed with a lavander purfume."
    talk lovely talk "Hmpf, I was right, as always."
    talk nasty talk "Fuck you, I was righter."
    talk lovely talk "As if! The scent on that page bears more resemblince to lavander than it does paper!"
    talk nasty talk "Buh buh buh buh! Why dont you just come fuck me, idiot!"
    talk orb talk "Let's move on."
    jump library_intro_menu
    
library_intro_smell_failure:
    set library_intro_smellAttempt true
    talk librarian talk "No."
    $if this.skillCheck("library_intro_smell_smell_orb", "orb", 20):
        talk orb talk "She isn't fazed in the slightest. She's heard way weirder. In fact, now she's curious how *you* smell."
        talk nasty talk "Nice..."
    talk nasty talk "The direct approach may not have worked, but I do still want to find out how she smells. For no particular reason. Lovely Lady does too, not that she'd admit it. Anyway, you know what they say. There's more than one way to sniff a rat."
    talk lovely talk "Gods, she's practically drooling."
    jump library_intro_menu

library_intro_nastyGirlsQuest:
    choice:
        talk nasty talk "Can we talk for a moment. It's nothing smutty, dont worry."
        "Well, if it's nothing smutty.":
            set library_intro_notSmutty true
            jump nerd_intro
        "If it's not smutty I'm not interested.":
            choice:
                talk nasty talk "I lied. It is smutty."
                "I'm interested.":
                    jump library_intro_smuttyQuest
        "I'd rather we didn't. (Leave)":
            jump nerd_intro

library_intro_smuttyQuest:
    choice:
        talk nasty talk "That librarian. She was hot, wasn't she?"
        "She *was* hot.":
            talk nasty talk "Well then."
            set q_getWithThenerd true
            jump nerd_intro
        "Nasty girl, please stop talking. (Move on)":
            jump nerd_intro
        "You told me it wasn't anything smutty." $if this.data.library_intro_notSmutty:
            talk nasty talk "I lied."
            jump nerd_intro