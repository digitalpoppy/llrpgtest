easyData:
    // I'm gonna comment here
    set quests.someQuest 2
    talk poppy idle "\"hello %{playerName}, I'm Poppy\"" // This is a comment
    $if this.data.quests.someQuest === 1:
        jump testLabel // Hello I'm a comment
    choice:
        talk poppy idle "\"What do you think of me?\""
        "\"You're nice\"":
            talk poppy idle "\"thanks\""
        skillcheck simple lovely 40 "Tell Poppy she's very boring":
            success "\"You're very boring\"":
                talk poppy idle "\"how dare u\""
            failure "You can't bring yourself to be so mean":

    choice:
        talk poppy idle "Do you like choices?"
        "Yes":
            set likeChoices true
        "No":
            set likeChoices false
    choice:
        talk poppy idle "What should we do?"
        "let's make choices!" $if this.data.likeChoices:
            "ok we can make choices"
        "let's do nothing!":
            "wow lame"
    "I'm the narrator and I don't have a picture"
    $if this.skillCheck("simple", "lovely", 40):
        "I see you like making choices :o"
    else:
        "You don't like choices????"
