home_fixHouse:
    set global_actionsleft this.data.global_actionsleft - 1
    set_screen default
    set_button button_fixHouse false
    ""
    $if !this.data.wallRepaired:
        "The wall is damaged."
    $if !this.data.roofRepaired:
        "The roof is damahed."
    $if !this.data.houseFixedInt == 4:
        choice:
            "The study is damaged"
            "(Patch up the hole in the wall)" $if this.data.hasTimber:
                "we can repair this!"
                set wallRepaired true
                set hasTimber false
                jump home_fixHouse
            "(Retile the roof)" $if this.data.hasTiles:
                "we can repair ths!"
                set roofRepaired true
                set hasTiles false
                jump home_fixHouse
    else:
        "House fixed!"
        "Is it though? Why should your house be patched up and fussed over but not you? You need to remember."
        jump game_map