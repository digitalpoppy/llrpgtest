game_map:
    clear_dialog
    $if !this.data.global_actionsleft == 0:
        set_screen game_map
    else:
        jump nightmare_controller