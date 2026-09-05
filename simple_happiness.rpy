default card_game_d2_win = False # Сохранение результатов карточной игры во втором дне
default d6_r1_winner = "" # Сохранение победителя в 6 дне, раунд 1
default d6_r2_winner = "" # Сохранение победителя в 6 дне, раунд 2

init:
    # == ИНИТЫ ==

    # Инициализация мода
    $ mods["simple_happiness_mod_prologue"] = "Простое Счастье"

    # Инициализация глобальных переменных с кастомными значениями диссолва
    $ long_dspr = Dissolve(0.5)
    $ good_dspr = Dissolve(0.3)
    $ half_good_dspr = Dissolve(0.25)
    $ fast_dspr = Dissolve(0.12)

    $ dissolve1 = Dissolve(1.0)
    $ dissolve2 = Dissolve(2.0)
    $ dissolve3 = Dissolve(3.0)
    $ dissolve5 = Dissolve(5.0)

    # Инициализация изображений
    #   Эффекты
    image flickering_noise1 = "mods/simple_happiness_mod_efim/images/anim/simple_happiness_flickering1.png"
    image flickering_noise2 = "mods/simple_happiness_mod_efim/images/anim/simple_happiness_flickering2.png"
    image flickering_noise3 = "mods/simple_happiness_mod_efim/images/anim/simple_happiness_flickering3.png"
    image red = "#FF0000"

    #   Фоны
    image bg prologue_backdrop = "mods/simple_happiness_mod_efim/images/backdrop/simple_happiness_prologue_backdrop.png"
    image bg day_none_backdrop = "mods/simple_happiness_mod_efim/images/backdrop/simple_happiness_day_none_backdrop.png"
    image bg prologue_monitor_cactus = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_prologue_monitor_cactus.png"
    image bg prologue_bus = "mods/simple_happiness_mod_efim/images/anim/simple_happiness_prologue_bus.jpg"
    image bg prologue_bus_ent = "mods/simple_happiness_mod_efim/images/anim/simple_happiness_prologue_bus_ent.jpg"
    image bg prologue_bus_ent2 = "mods/simple_happiness_mod_efim/images/anim/simple_happiness_prologue_bus_ent2.jpg"

    image bg ext_storage_day = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_ext_storage_day.png"
    image bg ext_storage_sunset = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_ext_storage_sunset.png"
    image bg ext_musclub_verandah_day = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_ext_music_club_verandah_day.jpg"
    image bg ext_beach_blur_sunset = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_d2_dizz.png"
    image bg ext_houses_night = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_ext_houses_night.png"
    image bg ext_stage_normal_sunset = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_ext_stage_normal_sunset.png"
    image bg ext_water_day = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_ext_water_day.jpg"
    image bg ext_musclub_concert_day = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_ext_musclub_concert_day.png"
    image bg ext_house_of_sl_sunset = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_ext_house_of_sl_sunset.jpg"
    image bg ext_house_of_sl_night = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_ext_house_of_sl_night.png"
    image bg ext_polyana_nebo_day = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_ext_polyana_nebo.png"
    image bg ext_polyana_nebo_night = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_ext_polyana_nebo_night.png"

    image bg int_warehouse_day = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_int_warehouse_day.png"
    image bg int_dining_hall_people_sunset = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_int_dining_hall_people_sunset.png"
    image bg int_musclub_mattresses_day = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_int_music_club_mattresses_day.jpg"
    image bg int_infirmary_day = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_int_infirmary_day.png"
    image bg int_bath_ent = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_int_bath_ent.jpg"
    image bg int_bathhouse = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_int_bathhouse.jpg"
    image bg int_cinema_people = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_int_cinema_people.png"
    image bg int_cinema_movie = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_int_cinema_movie.png"
    image bg int_house_of_sl_sunset = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_int_house_of_sl_sunset.png"
    image bg int_house_of_sl_night = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_int_house_of_sl_night.jpg"
    image bg int_house_of_mt_clean_day = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_int_house_of_mt_clean_day.png"
    image bg int_bus_people_sunset = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_int_bus_people_sunset.png"
    image bg int_semen_room_evening = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_int_semen_room_evening.png"
    image bg int_semen_room_evening_new = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_int_semen_room_clean.jpg"

    image bg d1_rena_sleep = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_d1_rena.jpg"
    image bg d8_nvl_back = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_d8_nvl_back.png"

    #   Арты
    image cg bus_view_left = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_out_bus_view_left.png"
    image cg bus_view_right = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_out_bus_view_right.png"
    image cg sleep_nothingness = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_sleep_nothingness.jpg"
    image cg d1_food_normal_sunset = "mods/simple_happiness_mod_efim/images/cg/simple_happiness_d1_food_normal_sunset.png"
    image cg mi_guitar_yam = "mods/simple_happiness_mod_efim/images/cg/simple_happiness_mi_guitar_yam.png"
    image cg d2_scared_by_squirel = "mods/simple_happiness_mod_efim/images/cg/simple_happiness_d2_scared_by_squirel.png"
    image cg d2_cards_scheme_basic = "mods/simple_happiness_mod_efim/images/cg/simple_happiness_d2_basic_scheme.png"
    image cg d2_cards_scheme_r1_me_win = "mods/simple_happiness_mod_efim/images/cg/simple_happiness_d2_scheme_r1_me_win.png"
    image cg d2_cards_scheme_r1_un_win = "mods/simple_happiness_mod_efim/images/cg/simple_happiness_d2_scheme_r1_un_win.png"
    image cg d2_cards_scheme_r2_me_win = "mods/simple_happiness_mod_efim/images/cg/simple_happiness_d2_scheme_r2_me_win.png"
    image cg d2_cards_scheme_r2_sl_win = "mods/simple_happiness_mod_efim/images/cg/simple_happiness_d2_scheme_r2_sl_win.png"
    image cg d3_square_sl_fall = "mods/simple_happiness_mod_efim/images/cg/simple_happiness_d3_square_sl_fall.png"
    image cg d3_square_sl_dance = "mods/simple_happiness_mod_efim/images/cg/simple_happiness_d3_square_sl_dance.png"
    image cg d3_walkin_sl_romantic = "mods/simple_happiness_mod_efim/images/cg/simple_happiness_d3_walkin_sl_romantic.png"
    image cg d3_boathouse_sl_romantic = "mods/simple_happiness_mod_efim/images/cg/simple_happiness_d3_boats_station_sl_romantic.png"
    image cg d3_boathouse_sl_dance = "mods/simple_happiness_mod_efim/images/cg/simple_happiness_d3_boathouse_sl_dance.png"
    image cg d4_un_flute = "mods/simple_happiness_mod_efim/images/cg/simple_happiness_un_flute.png"
    image cg d4_dv_guitar = "mods/simple_happiness_mod_efim/images/cg/simple_happiness_d4_dv_guitar.png"
    image cg d5_sl_dance = "mods/simple_happiness_mod_efim/images/cg/simple_happiness_d5_boath_sl_dance.png"
    image cg d5_sl_kiss = "mods/simple_happiness_mod_efim/images/cg/simple_happiness_d5_kiss.png"
    image cg d5_sl_love = "mods/simple_happiness_mod_efim/images/cg/simple_happiness_d5_love.png"
    image cg d6_concert_me_un_mi = "mods/simple_happiness_mod_efim/images/cg/simple_happiness_d6_me_un_mi_playing.png"
    image cg d6_concert_mi_dv = "mods/simple_happiness_mod_efim/images/cg/simple_happiness_d6_dv_mi_playing.png"
    image cg d7_polyana = "mods/simple_happiness_mod_efim/images/cg/simple_happiness_d7_polyana.png"
    image cg d7_polyana_night = "mods/simple_happiness_mod_efim/images/cg/simple_happiness_d7_polyana_night.png"
    image cg d7_polyana_guitar_playing = "mods/simple_happiness_mod_efim/images/cg/simple_happiness_d7_polyana_guitar_playing.png"
    image cg d8_sl_love = "mods/simple_happiness_mod_efim/images/cg/simple_happiness_d8_love.png"

    image cg ep_pc_mi = "mods/simple_happiness_mod_efim/images/cg/simple_happiness_ep_pc_mi.png"
    image cg ext_city_sunset = "mods/simple_happiness_mod_efim/images/cg/simple_happiness_ext_city_sunset.png"
    image cg ep_me_sl_park = "mods/simple_happiness_mod_efim/images/cg/simple_happiness_ep_walkin.png"
    image cg ep_summer_walk = "mods/simple_happiness_mod_efim/images/cg/simple_happiness_epilogue_summer_walk.png"

    #   Спрайты
    image sl veryfar = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_1_pioneer_veryfar_normal.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_1_pioneer_veryfar_normal.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, "mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_1_pioneer_veryfar_normal.png"
    )
    image sl civil normal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_1_civil_normal.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_1_civil_normal.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, "mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_1_civil_normal.png"
    )
    image sl civil smile = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_1_civil_smile.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_1_civil_smile.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, "mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_1_civil_smile.png"
    )
    image sl civil2 smile = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_1_civil2_smile.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_1_civil2_smile.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, "mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_1_civil2_smile.png"
    )
    image sl civil2 smile2 = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_2_civil2_smile2.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_2_civil2_smile2.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, "mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_2_civil2_smile2.png"
    )
    image sl pioneer_wet smile = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_1_pioneer_wet_smile.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_1_pioneer_wet_smile.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, "mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_1_pioneer_wet_smile.png"
    )
    image sl pioneer happy_cry = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_4_pioneer_happy_cry.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_4_pioneer_happy_cry.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, "mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_4_pioneer_happy_cry.png"
    )
    image sl skirt smile = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_1_skirt_smile.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_1_skirt_smile.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, "mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_1_skirt_smile.png"
    )
    image sl skirt shy = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_2_skirt_shy.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_2_skirt_shy.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, "mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_2_skirt_shy.png"
    )
    image sl towel normal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_1_towel_normal.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_1_towel_normal.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, "mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_1_towel_normal.png"
    )
    image sl towel smile = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_1_towel_smile.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_1_towel_smile.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, "mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_1_towel_smile.png"
    )
    image sl mid_naked smile = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_1_mid_naked_smile.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_1_mid_naked_smile.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, "mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_1_mid_naked_smile.png"
    )
    image sl mid_naked shy = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_2_mid_naked_shy.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_2_mid_naked_shy.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, "mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_2_mid_naked_shy.png"
    )
    image sl mid_naked smile2 = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_2_mid_naked_smile2.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_2_mid_naked_smile2.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, "mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_2_mid_naked_smile2.png"
    )
    image sl naked smile = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_1_naked_smile.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_1_naked_smile.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, "mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_1_naked_smile.png"
    )
    image sl naked shy = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_2_naked_shy.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_2_naked_shy.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, "mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_2_naked_shy.png"
    )
    image sl naked smile2 = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_2_naked_smile2.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_2_naked_smile2.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, "mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_2_naked_smile2.png"
    )
    image sl naked surprise close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_3_naked_surprise.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_3_naked_surprise.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, "mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_3_naked_surprise.png"
    )
    image sl naked scared close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_4_naked_scared.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_4_naked_scared.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, "mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_4_naked_scared.png"
    )
    image sl naked tender close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_4_naked_tender.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_4_naked_tender.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, "mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_4_naked_tender.png"
    )

    image mt nightdress normal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/mt/simple_happiness_mt_1_nightdress_normal.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/mt/simple_happiness_mt_1_nightdress_normal.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, "mods/simple_happiness_mod_efim/images/sp/mt/simple_happiness_mt_1_nightdress_normal.png"
    )
    image mt nightdress sad = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/mt/simple_happiness_mt_1_nightdress_sad.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/mt/simple_happiness_mt_1_nightdress_sad.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, "mods/simple_happiness_mod_efim/images/sp/mt/simple_happiness_mt_1_nightdress_sad.png"
    )
    image mt nightdress grin = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/mt/simple_happiness_mt_3_nightdress_grin.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/mt/simple_happiness_mt_3_nightdress_grin.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, "mods/simple_happiness_mod_efim/images/sp/mt/simple_happiness_mt_3_nightdress_grin.png"
    )

    image dv skirt sad = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/dv/simple_happiness_dv_3_skirt_sad.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/dv/simple_happiness_dv_3_skirt_sad.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, "mods/simple_happiness_mod_efim/images/sp/dv/simple_happiness_dv_3_skirt_sad.png"
    )
    image dv skirt shy = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/dv/simple_happiness_dv_3_skirt_shy.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/dv/simple_happiness_dv_3_skirt_shy.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, "mods/simple_happiness_mod_efim/images/sp/dv/simple_happiness_dv_3_skirt_shy.png"
    )

    image sem normal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sem/simple_happiness_sem_normal.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/sem/simple_happiness_sem_normal.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, "mods/simple_happiness_mod_efim/images/sp/sem/simple_happiness_sem_normal.png"
    )

    image kt normal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/kt/simple_happiness_kt_1_pioneer_normal.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/kt/simple_happiness_kt_1_pioneer_normal.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, "mods/simple_happiness_mod_efim/images/sp/kt/simple_happiness_kt_1_pioneer_normal.png"
    )
    image kt smile = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/kt/simple_happiness_kt_3_pioneer_smile.png", im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor("mods/simple_happiness_mod_efim/images/sp/kt/simple_happiness_kt_3_pioneer_smile.png", im.matrix.tint(0.63, 0.78, 0.82)),
        True, "mods/simple_happiness_mod_efim/images/sp/kt/simple_happiness_kt_3_pioneer_smile.png"
    )

    image obhod none = "mods/simple_happiness_mod_efim/images/sp/obhod/simple_happiness_obhod_0.png"
    image obhod one = "mods/simple_happiness_mod_efim/images/sp/obhod/simple_happiness_obhod_1.png"
    image obhod two = "mods/simple_happiness_mod_efim/images/sp/obhod/simple_happiness_obhod_2.png"
    image obhod three = "mods/simple_happiness_mod_efim/images/sp/obhod/simple_happiness_obhod_3.png"
    image obhod full = "mods/simple_happiness_mod_efim/images/sp/obhod/simple_happiness_obhod_full.png"

    # Инициализация звуков
        # sfx
    $ sfx_smoking_cigaret = "mods/simple_happiness_mod_efim/sounds/sfx/smoking_cigaret.mp3"
    $ sfx_clocks = "mods/simple_happiness_mod_efim/sounds/sfx/clocks.mp3"
    $ sfx_bicycle_falls = "mods/simple_happiness_mod_efim/sounds/sfx/bicycle_fall.mp3"
    $ sfx_bicycle_ring = "mods/simple_happiness_mod_efim/sounds/sfx/bicycle_ring.mp3"
    $ sfx_bicycle_wheels = "mods/simple_happiness_mod_efim/sounds/sfx/bicycle_wheels.mp3"
    $ sfx_mic_noise = "mods/simple_happiness_mod_efim/sounds/sfx/mic_noise.mp3"
    $ sfx_lamp_turn_on_off = "mods/simple_happiness_mod_efim/sounds/sfx/lamp_turn_on_off.mp3"
    $ sfx_water_drops = "mods/simple_happiness_mod_efim/sounds/sfx/water_drops.ogg"
    $ sfx_icq_msg = "mods/simple_happiness_mod_efim/sounds/sfx/icq_msg.ogg"

        # music
    $ miku_song_mi_learn1 = "mods/simple_happiness_mod_efim/sounds/music/miku_song_miku_learn1.ogg"
    $ miku_song_bad_learn = "mods/simple_happiness_mod_efim/sounds/music/miku_song_bad_learn.ogg"
    $ memories_guitar_only = "mods/simple_happiness_mod_efim/sounds/music/memories_guitar_only.mp3"
    $ this_one_for_her = "mods/simple_happiness_mod_efim/sounds/music/this_one_for_her.ogg"
    $ un_sinij_sinij_inij = "mods/simple_happiness_mod_efim/sounds/music/sinij_sinij_inij.ogg"
    $ warmest_summer = "mods/simple_happiness_mod_efim/sounds/music/warmest_summer.ogg"
    $ kostry_concert = "mods/simple_happiness_mod_efim/sounds/music/kostry_concert.ogg"

    # Персонажи
    define pis = Character(name=u"Пионеры", color="#ffffff", what_color="#f1d076", drop_shadow = [(-1, -1), (1, -1), (-1, 1), (1, 1)], drop_shadow_color = "#000000", what_drop_shadow = [(-1, -1), (1, -1), (-1, 1), (1, 1)], what_drop_shadow_color = "#000000") # Для случаев, когда много пионеров говорят разом
    define ths = Character(name=u" ", color="#000000", what_color="#f1d076", kind=nvl, what_prefix="~ ", what_suffix=" ~", drop_shadow = [(-1, -1), (1, -1), (-1, 1), (1, 1)], drop_shadow_color = "#000000", what_drop_shadow = [(-1, -1), (1, -1), (-1, 1), (1, 1)], what_drop_shadow_color = "#000000") # Мысли Семёна в режиме nvl
    define me_n = Character(name=u"Семён", color="#b1ffb1", what_color="#f1d076", kind=nvl, drop_shadow = [(-1, -1), (1, -1), (-1, 1), (1, 1)], drop_shadow_color = "#000000", what_drop_shadow = [(-1, -1), (1, -1), (-1, 1), (1, 1)], what_drop_shadow_color = "#000000") # Семён для режима nlv
    define sl_n = Character(name=u"Славя", color="#ffd200", what_color="#f1d076", kind=nvl, drop_shadow = [(-1, -1), (1, -1), (-1, 1), (1, 1)], drop_shadow_color = "#000000", what_drop_shadow = [(-1, -1), (1, -1), (-1, 1), (1, 1)], what_drop_shadow_color = "#000000") # Славя для режима nlv
    define mi_jp = Character(name=u"Мику", color="#00deff", what_color="#f1d076", what_font="mods/simple_happiness_mod_efim/gui/fonts/NotoSansJP-Regular.ttf", drop_shadow = [(-1, -1), (1, -1), (-1, 1), (1, 1)], drop_shadow_color = "#000000", what_drop_shadow = [(-1, -1), (1, -1), (-1, 1), (1, 1)], what_drop_shadow_color = "#000000") # Мику для её фраз на японском
    define mi_n = Character(name=u"Мику", color="#00deff", what_color="#f1d076", kind=nvl, drop_shadow = [(-1, -1), (1, -1), (-1, 1), (1, 1)], drop_shadow_color = "#000000", what_drop_shadow = [(-1, -1), (1, -1), (-1, 1), (1, 1)], what_drop_shadow_color = "#000000") # Мику для режима nlv
    define un_n = Character(name=u"Лена", color="#a5a5ff", what_color="#f1d076", kind=nvl, drop_shadow = [(-1, -1), (1, -1), (-1, 1), (1, 1)], drop_shadow_color = "#000000", what_drop_shadow = [(-1, -1), (1, -1), (-1, 1), (1, 1)], what_drop_shadow_color = "#000000") # Лена для режима nlv
    define dv_n = Character(name=u"Алиса", color="#ff7800", what_color="#f1d076", kind=nvl, drop_shadow = [(-1, -1), (1, -1), (-1, 1), (1, 1)], drop_shadow_color = "#000000", what_drop_shadow = [(-1, -1), (1, -1), (-1, 1), (1, 1)], what_drop_shadow_color = "#000000") # Алиса для режима nlv
    define kt = Character(name=u"Катя", color="#a67640", what_color="#f1d076", drop_shadow = [(-1, -1), (1, -1), (-1, 1), (1, 1)], drop_shadow_color = "#000000", what_drop_shadow = [(-1, -1), (1, -1), (-1, 1), (1, 1)], what_drop_shadow_color = "#000000") # Катя
    define ktp = Character(name=u"Пионерка", color="#a67640", what_color="#f1d076", drop_shadow = [(-1, -1), (1, -1), (-1, 1), (1, 1)], drop_shadow_color = "#000000", what_drop_shadow = [(-1, -1), (1, -1), (-1, 1), (1, 1)], what_drop_shadow_color = "#000000") # Катя-пионерка

    # Анимация "часов"
    define clocks_in = ImageDissolve(image="mods/simple_happiness_mod_efim/images/anim/simple_happiness_clock_anim_mask.png", time=2.5, ramplen=8)
    define clocks_out = ImageDissolve(image="mods/simple_happiness_mod_efim/images/anim/simple_happiness_clock_anim_mask_back.png", time=2.5, ramplen=8, reverse=True)


# == СЛУЖЕБНЫЕ ЛЕЙБЛЫ ==

# Анимация ослепления
label flashing(dissolve_time=0.5):
    $ flashing_dissolve_time = Dissolve(dissolve_time)
    
    show white with flashing_dissolve_time
    hide white
    with flash
    return


# Смена режима повествования с adv на nvl
label to_nvl_mode:
    window hide
    pause(1)
    $ set_mode_nvl()
    nvl show dissolve
    return


# Смена режима повествования с nvl на adv
label to_adv_mode:
    nvl hide dissolve
    pause(1)
    $ set_mode_adv()
    window show
    return


# Кастомный экран дня
label custom_day_screen(day_num, title, backdrop_type):
    $ full_title = u"Простое Счастье. " + title
    
    if backdrop_type == "prologue":
        show bg prologue_backdrop with dissolve
    elif backdrop_type == "day_none":
        show bg day_none_backdrop with dissolve
    
    show flickering_noise1 at screen_flickering
    pause(0.1)
    show flickering_noise2 at screen_flickering
    pause(0.12)
    show flickering_noise3 at screen_flickering
    with dissolve5

    show black with dissolve

    return


# Расчет конца проигрываемого трека
label calc_music_how_much_play:
    $ track_len = renpy.music.get_duration()
    $ track_played = renpy.music.get_pos()

    if renpy.music.is_playing():
        $ track_left = (track_len - track_played) + 1.0

        if track_left > 1.0:
            window hide
            $ renpy.pause(delay=track_left, hard=True)
            window show
        else:
            pause(1.0)

    else:
        pause(1.0)
    
    return


# Вызов звуков курения
label smoking_process(with_pack_crumple=False, with_pause=0):
    stop sound

    if with_pack_crumple == True:
        play sound sfx_cigarette_pack_crumple
        queue sound sfx_alisa_lighter
    else :
        play sound sfx_alisa_lighter

    queue sound sfx_smoking_cigaret

    if with_pause != 0:
        pause(with_pause)

    return


# Смена времени дня
label set_time(new_time="day"):
    if new_time == "prolog":
        $ prolog_time()
        $ persistent.sprite_time = "night"
    elif new_time == "sunset":
        $ sunset_time()
        $ persistent.sprite_time = new_time
    elif new_time == "night":
        $ night_time()
        $ persistent.sprite_time = new_time
    else:
        $ day_time()
        $ persistent.sprite_time = new_time
    
    return


# == АНИМАЦИИ ==

# Мерцание экрана монитора
transform screen_flickering:
    linear 0.05 alpha 0.2
    linear 0.1 alpha 0.9
    linear 0.05 alpha 0.1
    linear 0.1 alpha 1.0
    repeat

# Уход влево
transform walk_away_left:
    linear 2.0 xalign -1.5

# Уход вправо
transform walk_away_right:
    linear 2.0 xalign 1.5

# Бег влево
transform run_away_left:
    linear 1.0 xalign -1.5

# Бег вправо
transform run_away_right:
    linear 1.0 xalign 1.5

# Шаг к центру
transform walk_to_center:
    linear 2.0 xalign 0.0

# Бег к центру
transform run_to_center:
    linear 1.0 xalign 0.0

# Плавное размытие
transform blurring:
    blur 0.0
    linear 1.5 blur 15.0

# Плавное деразмытие
transform deblurring:
    blur 15.0
    linear 1.5 blur 0.0

# Пульсирующая пелена перед глазами
transform pulsing_eyes:
    alpha 0.0
    linear 1.0 alpha 0.1
    linear 1.0 alpha 0.45
    linear 1.0 alpha 0.20
    linear 1.0 alpha 0.64
    linear 1.0 alpha 0.15
    linear 1.0 alpha 0.05
    repeat

# Скрыть пульсацию
transform depulsing_eyes:
    linear 2.0 alpha 0.0


# == ПОВЕСТВОВАНИЕ ==

# Стартовый лейбл. Пролог
label simple_happiness_mod_prologue:
    $ renpy.block_rollback()

    $ new_chapter(0, u"Пролог")

    call custom_day_screen(0, "Простое Счастье. Пролог", "prologue")

    call set_time("prolog")

    $ set_mode_adv()

    play music music_list["farewell_to_the_past_full"] volume 0.7 fadein 5.0

    hide flickering_noise1
    hide flickering_noise2
    hide flickering_noise3
    show bg prologue_monitor_cactus
    hide black
    with dissolve

    me "Что, не хотите распускаться?"

    "Я печально смотрел на два своих кактуса, аккуратно посаженные в коричневые горшочки. Один стоял на столе, рядом с монитором, а второй на подоконнике."
    "Завязь на обоих уже взялась, но вот цветы всё никак не хотели распускаться, а тот, что был помельче, так и вовсе, кажется, начал увядать."
    "Во всяком случае мне так казалось из-за его более тёмного цвета, напоминавшего мешки под глазами, и какого-то общего, «уставшего вида»."

    me "Прямо как я... {w}Хех, м-да..."
    "А вот второй, напротив, был побольше, мякоть его было ярко-зелёная, а иголки весело переливались каким-то золотистым оттенком в свете лампы."
    me "Ну, не хочите, как хочите..."

    call flashing

    "Я вернул взгляд на монитор компьютера. Яркий, белый свет бил в глаза, да так, что приходилось щурится."

    play sound_loop sfx_computer_noise

    th "Вот жеж... Неужели нельзя сделать тёмную тему для сайта, это так сложно, что-ли?"
    "Я взглянул на часы в правом нижем углу экрана."
    th "Пора-бы уже собираться, а то опоздаю... {w}И чёрт меня дёрнул вообще согласиться ехать на эту встречу институтских товарищей? Отучился то с ними всего-ничего..."

    stop sound_loop fadeout 1.0

    show bg semen_room with dissolve1

    "Встав из-за компьютера, я начал одеваться, попутно проклиная наши зимы, и тонны одежды, которые приходилось на себя напяливать."
    "Подштанники, штаны, майка, футболка, кофта, куртка… Господи, а тяжеленные зимние ботинки чего сто́ят? Каждый весит килограмм по пять, и ноги очень сильно устают."
    "..."

    call to_nvl_mode

    "А ведь когда-то занимался волейболом, и всем из него вытекающим: зарядки по утрам, пробежки, разминки, тренировки. Иногда даже в зале. Иногда даже с весами. И такую мелочь как тяжелая зимняя обувь я бы даже не заметил."
    "Н-да, давно это было. До того, как я начал вести свою жизнь затворника, или, как бы меня назвали представители более младшего поколения – хиккана. Это было даже до того, как я поступил в институт. Однако со спортом пришлось завязать сразу по двум причинам. Первая, и самая очевидная – травмы. Не зря же говорят, что физкультура лечит, а спорт калечит? Вот и у меня после пары серьезных травм руки не осталось никакого желания заниматься профессиональным спортом."
    "А вторая, не менее очевидная – лень. Всё больше я отдавал предпочтение домашним видом досуга: аниме, видеоигры, разные хостинги, куда люди заливают видео, и любой другой может посмотреть и прочие соцсети. И конечно, анонимные чаты и форумы. О, на них я был завсегдатаем. Ведь так легко и просто общаться, и высказывать всё, что ты думаешь о своём собеседнике, не боясь быть узнанным, вычисленным и избитым на улице."
    "И хотя с учёбой у меня не сложилось, к сожалению, деньги сами из воздуха не материализовываются, поэтому иногда приходилось подрабатывать. Родители хоть и помогали, но не много, и не охотно. Конечно, не приятно, когда к твоему сыну уже стучится переход на вторую половину второго десятка, а он без образования, без нормальной работы, имеет лишь убитую квартирку на окраине города, доставшуюся в наследство, и живёт сычом."
    "Я их понимал. Понимал, но ничего не мог с собой поделать, таков уж я. {w}Ленивый, неопрятный и самовольно загнанный в свой же мир из шести граней."
    "Но такая жизнь меня устраивала."
    "..."
    nvl clear
    "Денег от редких халтурок хватало на пропитание и прочие базовые потребности, а они у меня были очень невелики. Да и родители, как ни крути, скидывали иногда копейку-другую, так что бывало, под конец месяца на счету было чуть больше чем ноль рублей, ноль ноль копеек, чем я активно и пользовался, по возможности обновляя свой дряхлый ПК, не давая ему совсем уж задохнуться в новинках игропрома."
    "Одной из немногих вещей, которые хоть как-то держали меня на плаву, и не давали уйти в депрессию были комнатные цветы. Забавно, правда? Практически уже взрослый мужчина, сидящий бобылем в четырёх стенах, который с трепетом ухаживает за маленькими растеньями. Поливает, пересаживает, удобряет… Это занятие я всегда находил умиротворяющим. Более того, в такие моменты я чувствовал, что действительно приношу пользу нашему миру, пусть даже и маленькой его толике, в виде пары цветов. Растениеводство меня настолько зацепило, что этим летом я даже подрабатывал в местном ботаническом саду. В дни своих смен я просыпался с первыми птицами, и стремглав бежал на автобусную остановку, чтобы успеть на первый автобус, который проедет по этому маршруту. А заканчивал работу всегда последним, и уходил, когда во всём саду не оставалось уже никого, кроме деда охранника, обыкновенно сидящего в своей будке-сторожке. Иногда мы с ним разговаривали за сигареткой-другой. У него была дача, и он рассказывал мне много полезного про посадку, уход за разными видами растений, и прочие премудрости садоводства."
    nvl clear
    "Изучал я конечно, и множество других вещей. Бесцельно сидя практически круглые сутки за компьютером, невозможно не начать искать, чем бы завлечь свой интерес. Пробовал изучать языки – долго и муторно. Музыка – сложно. Хотя у меня и была гитара, купленная ещё в период начала обучения, уже подавно она пылилась в углу комнаты, а я всё никак не решался убрать её в какое-нибудь укромное место, или продать."
    "Цепляло меня разве-что программирование. Мне нравилось изучать конструкции языков, составлять блок-схемы, и писать по ним программы. Словно бы ты являешь Богом, создателем своего маленького мира, где всё работает по твоим законам, по твоим правилам. Но и просидеть за кодингом меня не хватало больше чем по паре часов в день пару раз в неделю. {w}..."
    "Так я проводил последние несколько лет, сметённый, не знающий, чем себя занять, где найти своё место в жизни, неопределённый и подавленный. Лишь иногда, мои форумно-видеогровые марафоны перемежались редкими прогулками по паркам города. Приятно бывает остаться наедине со своими мыслями, не думать ни о чём, и просто наслаждаться природой. Пару раз в год даже старался выбираться куда-нибудь за город, где воздух почище, а пейзаж серого мегаполиса сменяется лесами, полями, горными речками и озёрами. Но это было редкостью. Не только ввиду моей лени, но ещё и потому что в регионе, в котором я жил, лето было совсем короткое. Тёплые дни начинались только в конце мая, а холодать начинало уже в начале сентября."

    call to_adv_mode

    th "Этим летом надо будет обязательно куда-нибудь выбраться, хоть-бы в самый ближайший пригород."
    "Думал я, заканчивая наконец одеваться, и завязывая шнурки на ботинках."
    "..."
    "Совершив последние действия ритуала, который необходимо совершать, выходя из дома, я ещё раз проверил, что ключи, телефон и сигареты на своих местах, и вздохнув, вышел из комнаты, и закрыл входную дверь."
    "..."

    stop music fadeout 3.0

    show bg bus_stop with dissolve3

    play ambience ambience_cold_wind_loop fadein 1.0
    play music music_list["trapped_in_dreams"] volume 0.7 fadein 3.0

    "Продолжая размышлять над тщетностью своего бытия, я дошел до остановки, и рука машинально потянулась к карману, в котором лежала пачка с сигаретами."
    th "Твою-то, последняя."

    call smoking_process(with_pack_crumple=True, with_pause=1.0)

    "Я вздохнул, смял пачку и выкинул её в урну, чиркнул спичкой и затянул сигарету."

    call to_nvl_mode

    "Как это обычно бывает, перед массовым мероприятием я немного нервничал. Оно и не мудрено, ведь за последние несколько лет я почти разучился общаться с людьми вживую, впрочем, вдруг эта встреча пойдёт мне только на пользу? Развеюсь немного, может даже познакомлюсь с кем-нибудь? Может даже с девушкой… Хотя, кого я обманываю. Ни одна представительница прекрасного пола, наверное, даже не посмотрит в мою сторону. Одетый чёрте-как, мешки под глазами, месячная небритость."
    "А ведь когда-то у меня была девушка. Первая, и последняя. Ещё в старшей школе. Не сказать, что наши отношения длились долго, но оставили после себя то, что и должны оставлять правильные отношения. Ощущение тепла, заботы, желания любить, защищать…"
    "По ощущениям это было настолько давно, что я уже почти забыл её. Стёрлись из памяти её внешность, характер, остались только воспоминания о эмоциях, пережитых вместе, да имя, словно строчка из профиля в социальной сети, всплывало перед глазами."

    play sound sfx_bus_idle fadein 3.0 loop
    play sound2 sfx_bus_stop fadein 2.0
    play sound3 sfx_bus_honk

    call to_adv_mode

    show bg prologue_bus with dissolve

    "Из очередного приступа саморефлексии меня вывел скрип тормозов автобуса, подъезжающего к остановке."
    th "Надо же, очень быстро подъехал."
    th "Странно, единственный 410-й маршрут, который ходит в этом районе, появляется раз в полчаса, а сейчас на часах 21:19. Может, предыдущий задержался, или этот, наоборот, приехал слишком рано? Ай, к чёрту. Какая разница…"

    play sound3 sfx_smoking_cigaret

    "Быстро, уже на ходу сделав последние затяжки, я бросил окурок на снег, а сам зашел в распахивающиеся двери автобуса. На ступеньках меня кольнула мысль «Какой-то он не такой…»."

    window hide

    show bg prologue_bus_ent with dissolve
    pause(0.6)
    show bg prologue_bus_ent2 with dissolve
    pause(0.6)

    stop ambience fadeout 1.0
    stop sound fadeout 1.0

    pause(1.0)

    stop music fadeout 2.0
    play sound sfx_bus_interior_moving volume 0.7 fadein 1.0 loop
    play sound2 sfx_bus_loop volume 0.7 fadein 3.0 loop

    show bg intro_xx with dissolve

    window show

    "Зайдя в автобус, и плюхнувшись на один из последних рядов, я с интересом огляделся…"
    "Вроде ничего необычного, автобус как автобус, но этот был… Старее, что ли? Такое чувство, словно его выдернули из конца прошлого века."
    "Впрочем, какая разница? По этому маршруту ходит только 410-й, да и табличка на стекле с номером автобуса об этом явно говорит."

    call to_nvl_mode

    "Откинув в сторону ненужные мысли, я упёрся лбом в стекло, и тупо уставился на пролетающий мимо город. Дороги, перекрёстки, светофоры, вывески, сияющие всеми цветами радуги, толпы людей, спешащих по своим делам."
    "Внезапно вспомнилось, что крупные города обычно называют муравейниками, или «человейниками». Хах, и правда, если посмотреть на город в час пик с высоты птичьего полёта, выглядеть это будет как те самые муравейники под стеклами. Такие же запутанные, но вместе с этим логичные перипетии улиц, проспектов и магистралей, где каждая дорога имеет своё значение – всякая куда-нибудь ведёт."
    "А по всем этим лабиринтам снуют туда-сюда «человеки», где каждый занят своим делом, где каждый знает, какого его место в этом механизме, и роль какой шестерёнки он исполняет."
    nvl clear
    "А я знаю? Что, если я вовсе не нужен этому миру? Что будет, если я просто испарюсь, вот так вот, в мгновение ока. Был Семён, и нет Семёна. Как лишняя деталь, которую, если выкинуть, ничего не сломается и не остановится, механизм продолжит работать так, как задумано, и никто даже не заметит исчезновения одной маленькой шестерёночки."
    "Как и владелец муравейника не заметит исчезновения одного муравья из всей колонии. Интересно, а у нашего мира есть свой… «Владелец»? Вдруг кто-нибудь, или что-нибудь также сейчас смотрит на нас, и с интересом изучает повадки своих домашних «человеков»."
    "..."

    call to_adv_mode

    "От всех этих пространных рассуждений, и непрекращающегося светопреставления перед глазами захотелось спать."
    th "Ну ладно, посижу немного с закрытыми глазами, всё равно ещё даже до центра не доехали, а его ещё пересекать, и на другом конце города..."
    "Казалось, я только прикрыл глаза, и тут…"

    stop sound fadeout 2.0
    stop sound2 fadeout 2.0

    show blink

    window hide

    $ renpy.pause(1.5, hard=True)

    $ renpy.movie_cutscene("mods/simple_happiness_mod_efim/images/vid/simple_happiness_intro.webm")

    jump simple_happiness_mod_day1


# День 1
label simple_happiness_mod_day1:
    $ renpy.block_rollback()
    $ backdrop = "days"
    $ new_chapter(1, u"Простое Счастье. День 1")

    call set_time

    $ set_mode_adv()

    play music music_list["no_tresspassing"] volume 0.9 fadein 1.0

    hide blink
    show unblink
    pause(1.0)
    hide unblink

    show bg int_bus with dissolve

    pause(1.0)

    call flashing(dissolve_time=1.5)

    window show

    "Яркий свет ударил в глаза. Я невольно зажмурился, и медленно повернулся всем телом в сторону от источника света."
    "Всё тело немного ныло, как будто спал в неудобном положении. {w}Стоп… {w}Спал!? {w}Твою мать, остановку, наверное, проехал!"
    "Я встал, и потирая глаза направился в сторону выхода из автобуса, и только достаточно проморгавшись понял…"
    th "Какого … !??"
    th "Где я!?"

    play sound sfx_head_heartbeat fadein 1.0

    "Сердце бешено заколотилось, я начал озираться по сторонам, и понял, что нахожусь в совершенно другом автобусе!"
    th "Но… как!?"
    "В голове я пытался тщетно восстановить последовательность событий, но всё было как в тумане… Вот я захожу в автобус, еду, а потом… Потом – провал."
    "Кажется, я заснул в салоне? {w}Или нет? {w}Другого объяснения быть не может, не вырубили же меня?"
    "Я потер затылок. {w}Не болит. {w}Значит точно, просто заснул."
    "Я еще раз оглядел салон, и только потом обратил внимание на то, что находилось {b}за{/b} его пределами."
    th "Лето! Но ведь только что была зима…"
    "Я подошел ближе к одному из окон и уставился наружу."
    
    show cg bus_view_left with dissolve

    "Пейзаж не был мне знаком хоть сколько-то. Ближе к автобусу располагалось практически бескрайнее поле, и только на горизонте маячил густой лес."
    "Никаких признаков, по которым можно было бы определить, {i}где{/i} передо мной."
    "Я перешел на противоположную сторону салона, и…"

    hide cg bus_view_left
    show cg bus_view_right
    with dissolve

    "Удивился ещё сильнее? Нет, в моей ситуации это было невозможно. Скорее, всё больше начал убеждаться, что это не галлюцинация, я не сплю и не пребываю в состоянии трипа. Уж слишком реалистично выглядела эта картина."
    "Перед моим взором красовались ворота, над которыми гордо было написано «Совёнок». Что может так называться? Пионерлагерь?.."
    "..."

    hide cg bus_view_right
    show bg int_bus
    with dissolve

    "Руки тряслись неимоверно. Я сел на одно из кресел, и задумался."
    "Удивительно, но страх отступил, уступив место лишь легкому тремору, и ощущению полного непонимания происходящего."
    th "Это какой-то эксперимент? Чья-то злая шутка? Нелепая случайность?"
    "В голове вертелась целая прорва идей, ни за одну, из которых невозможно было зацепиться."
    th "Что же, ладно. Я не мёртв, и меня, вроде как, не пытают. Сидя на одном месте, я ничего не выясню, надо осмотреться."
    
    play sound sfx_clocks fadein 0.5
    
    show black with clocks_in
    hide black with clocks_out

    stop sound fadeout 1.0

    "Я прошёл по салону из конца в начало. Заглядывал под каждое сиденье, в каждый закуток, но ничего не нашел. {w}Абсолютно."
    "Такое чувство, что этот автобус только вышел с конвейера, настолько тут было чисто. {w}Кстати!"
    th "Твою-то…"
    "А автобус то не тот, в котором я приехал!"
    "Я ещё раз оглядел салон. {w}Ну точно. {w}Не потрёпанный жизнью ЛиАЗ, а самый настоящий Икарус!"
    "Нет, тут точно, что-то не чисто… Меня, что, пересадили из одного автобуса в другой, пока я спал, и увезли в неизвестном направлении?"
    "Вопросов становилось всё больше."
    "Наконец, я подошел к водительскому месту, и увидел… {w}А что я должен был увидеть? Всё как положено: руль, три педали, рычаг КПП."
    "Водителя, конечно, не было, но это я сразу заметил."
    "Однако, на водительском месте нашлось единственное место, где могло что-то лежать. Бардачок. Посмотрим…"

    play sound sfx_open_cupboard volume 0.7

    "..."

    "Я выдвинул ящик, и там оказалось всего два предмета: пачка сигарет, и зажигалка."
    "И если ко второму вопросов не было, обычная газовая зажигалка с кремнием. А вот пачка была необычная."
    "Это были сигареты известной марки с нарисованным верблюдом, но вот дизайн был каким-то… Ретро? Да и все надписи были на английском языке."
    th "Наверное, какое-то лимитированное издание."
    "В любом случае, опасности эти предметы не предоставляли, да и водитель, если он есть, думаю, не обидится, если узнает, что я скурил одну. {w}После такого-то стресса."

    play sound sfx_inhale

    "Я набрал полную грудь воздуха, и вышел на улицу…"

    show bg ext_camp_entrance_day with dissolve

    call flashing()

    "Глаза, только привыкшие к яркому свету, вновь невольно зажмурились, ведь на улице этого самого солнечного света было кратно больше, чем в салоне автобуса."

    show bg ext_road_day with dissolve

    "Я огляделся.{w} Дорога, по которой, надо полагать, и приехал этот автобус, уходила куда-то вдаль, изредка петляя…"

    show bg ext_camp_entrance_day with dissolve

    "А передо мной стояли всё те же ворота с надписью «Совёнок», да два пионера на пьедесталах по бокам."
    "Во всяком случае, не было сомнений, что передо мной изображены именно пионеры. {w}Их выдавали рубашки с галстуками, а у одного из них, так и вовсе, имелась труба."

    show bg ext_bus with dissolve

    "Немного помявшись, я подошел к одной из колонн, и начал совершать чисто машинальные действия по открытию пачки."

    call smoking_process(True, 1.0)

    th "Что же за чертовщина? Ничего не понимаю…"
    "Пока-что это место само по себе не казалось враждебным, даже напротив, складывалось ощущение, что его хотели подать максимально дружелюбно."
    "Все цвета были очень насыщенные, запахи необычайно приятно щекотали ноздри, и даже сигаретный дым, от которого уворачивается даже заядлый курильщик, потому что он щиплет глаза, казался очень душистым, ароматным и приятно-терпким."
    th "Надо будет поблагодарить водителя. Если он вернётся, конечно…"
    "..."
    "Докуривая сигарету, я понял, что мне жарко."
    "Неизвестно, сколько ещё мне тут находится, но обтекать ста слоями пота никак не хотелось."
    "Поэтому, докурив сигарету и потушив её носком ботинка, я направился обратно к автобусу."

    show bg int_bus with dissolve

    "Зайдя обратно, я положил на своё место куртку, следом отправилась кофта."
    "Расправив футболку на выпуск, и переложив «трофейные» сигареты из куртки в штаны, я утвердительно хмыкнул, и сошел со ступеней автобуса."

    show bg ext_camp_entrance_day with dissolve

    "Надо думать, что делать дальше."
    "Я нахожусь неизвестно где, неизвестно, как сюда попал, и кто меня сюда поместил…"
    "М-да, слишком много неизвестных, так что задача выглядела нерешаемой."
    "Можно, конечно, пойти по дороге, но что я там найду?"
    "Неизвестно (опять же), сколько до ближайшего населенного пункта, а этот пионерлагерь (или что бы не скрывалось за этими воротами) выглядел обитаемо."
    "Бордюры по краям были свеже побелены, ворота явно крашены не позднее пары лет назад."
    "Что же, остаётся только…"

    stop music fadeout 0.5

    "Не успел я закончить мысль, как услышал, что ворота начали открываться."

    play sound sfx_open_door_mines_metal volume 0.5 fadein 0.3

    "Я сжал кулаки, и замерев, уставился на медленно открывающуюся ставню, откуда, через пару секунд выглянула…"

    show sl veryfar at center
    with good_dspr

    "... Пионерка."
    "Пазл сложился, дедукция меня не подвела. Но что теперь делать?"
    "Вдруг она вовсе не дружелюбна, и сейчас достанет тесак из-за пазухи и весело порежет меня на советский флаг…"
    "..."
    "Пионерка в это время огляделась, потом, увидев меня, начала приближаться."
    "Не знаю, почему, но занервничал я ещё сильнее, а ноги словно вросли в асфальт, я не мог и двинуться с места."
    "Разум твёрдо и настойчиво кричал о том, что её бояться не стоит, во всяком случае пока."
    "К тому же, она была первым человеком, которого я встретил… {i}здесь{/i}."

    show sl pioneer normal at center
    with good_dspr

    play music music_list["dance_of_fireflies"] fadein 1.5 volume 0.5

    "Наконец, пионерка достаточно сократила дистанцию, и заговорила."
    slp "Привет, ты, наверное, новенький, только что же приехал?"
    "Её красоту я не мог не отметить, даже трясясь от страха."
    "Длинные, до самых бёдер золотого цвета толстые косы, голубые, большие глаза, словно самое чистое море, в которых хотелось утонуть."
    "И фигурой её природа не то, что не обделила, даже перестаралась."
    "Не самая длинная даже по современным меркам юбка дразнящим образом открывала ноги на добрые пятнадцать сантиметров выше колена, а заправленная в неё рубашка эффектно подчеркивала прекрасного размера грудь."
    me "При-привет… Да я вот… Да."
    "Всё ещё находясь в шоке от происходящего, я не мог из себя выдавить более осмысленный ответ."
    "Девочка (девушка?) улыбнулась, и ответила."

    show sl pioneer smile with dspr

    slp "Замечательно, мы как раз ждали, что сегодня должен приехать новенький. Тебе сейчас к вожатой надо, хочешь, я тебя провожу?"
    me "Ну… Наверное, да, я думаю… Пойдём."
    "Ответил я, всё ещё продолжая машинально сжимать кулаки. Кажется, она это заметила."

    show sl pioneer surprise with good_dspr

    slp "А ты чего злишься? Что-то случилось?"
    "Поняв, что ногти уже почти впились мне в кожу, я как можно спокойнее выдохнул, разжал кулаки, и ответил."
    me "Да нет, просто… Дорого выдалась не очень. Устал. Да и жарко тут."
    slp "Что правда, то правда, дорога обычно длинная и изматывает."
    slp "Тогда тем более пошли уже, пройдешься, развеешься. Я тебя провожу."

    show sl pioneer smile with half_good_dspr
    pause(0.75)
    show sl pioneer normal with half_good_dspr

    th "На этой фразе, мне показалось, или она на секунду смутилась?"
    slp "Ну же?"

    show sl pioneer smile far with good_dspr

    "Девочка протянула мне руку, сделала пару шагов назад, и поманила за собой."
    "Мои ноги словно сами отклеились от асфальта, и я пошёл за ней."
    "Словно бы в этот момент мой мозг выбрал наиболее подходящую тактику «действовать по обстоятельствам», так что я пока решил поддаться этим самым обстоятельствам."
    "Сделав пару больших шагов, я догнал девушку, и шагал с ней почти бок-обок…"

    show sl pioneer normal at right
    show bg ext_clubs_day
    with dissolve1

    play music music_list["goodbye_home_shores"] fadein 2.0 volume 0.8

    "Мы зашли на территорию лагеря."
    "Первое, что меня встретило, помимо большого количества открытого пространства, серое здание слева чуть поодаль."
    slp "Это наше здание общих кружков. Правда, тут только один кружок, кикибр.. хи-хи.."
    
    show sl pioneer shy with good_dspr

    "Она немного запнулась."
    slp "Кибернетический. Но раньше было больше!"
    me "А ты тут… Бывала раньше?"
    "Задал я резонный вопрос."

    show sl pioneer smile2 with good_dspr

    slp "Нет, это моя первая смена в этом лагере. Просто вожатая рассказывала."
    "Уже второй раз она упоминает какую-то таинственную вожатую, к которой, мы, вроде как, сейчас направляемся."
    "Надеюсь, характером она не будет походить на воспиталку-цербера, или шизанутого прапора. {w}Знаем, плавали…"
    "Тем временем мы продолжали идти по дорожке, за которой всё более и более отчетливо проглядывалось большое открытое пространство. {w}Площадь?"

    show bg ext_houses_day with dissolve1

    "Я решил продолжать поддерживать разговор, попутно пробуя почву."
    me "А тебе здесь нравится?"

    show sl pioneer normal with good_dspr

    slp "Да, здесь здорово. Да и гораздо теплее, чем там, откуда я родом."
    slp "Да и в принципе, здесь хорошо. {w}Ты не переживай, ты же только что приехал, для тебя сейчас всё новое и непонятное."
    slp "Побудешь тут, совсем чуть-чуть, вот увидишь, тебе понравится, тут всегда что-нибудь интересное происходит."

    show sl pioneer smile with good_dspr

    "Девушка мило улыбнулась, посмотрев на меня, а мы тем временем, вышли на площадь."

    show bg ext_square_day
    show sl pioneer smile at cright
    with dissolve1

    "Это было она, безо всяких сомнений. {w}Это выдавали и скамейки по краям, и плиточная кладка, и конечно же, большой памятник, гордо возвышающийся над этой равниной."
    "На пьедестале, кажется, было что-то написано, но я так и не смог рассмотреть, что."
    slp "Мы на площади, осталось пройти совсем чуть-ч…"
    "Начала говорить пионерка, но вдруг осеклась, пристально смотря мне за плечо."

    show sl pioneer angry with good_dspr

    "Заметив её целеустремленный взгляд, я, чисто машинально, тоже обернулся, и увидел перед собой…"

    show dv pioneer2 smile at left
    show sl pioneer surprise
    with good_dspr

    play music music_list["eat_some_trouble"] fadein 0.5 volume 0.9

    slp "Алиса! Ты чего крадёшься? Как обычно, хотела проверить новенького на прочность?"
    "Пионерка составила такую мордашку, что я не понял, злится она по-настоящему, или только делает вид."
    
    show dv pioneer2 laugh at left
    with good_dspr

    dv "Тьфу ты блин, ну конечно! Смотрю, идёт какой-то тип, и ты рядом. Ну дай думаю тресну! Эх, весь кайф ты мне обломала!"
    slp "А вот нечего, потому что руки распускать. Если энергии много, так иди поиграй во что-нибудь, или делом займись."
    dv "Деелом? {w}Не-е, это нам не проходили, это нам не задавали! А вот поиграть это хорошо. Пойду тогда, посмотрю, может кто на спортплощадке есть. {w}Бывайте!"

    stop music fadeout 1.0
    play ambience ambience_camp_center_day fadein 1.0 volume 0.8

    show dv pioneer2 grin with half_good_dspr
    pause(1.0)
    show dv pioneer2 grin at walk_away_left
    pause(1.0)
    hide dv

    "Ещё одна пионерка, по всей видимости, её звали Алисой (интересно, не Селезнёвой ли?), стрельнула глазами, и удалилась восвояси."
    "Одета она была в ту же пионерскую форму, за тем исключением, что сидела она на ней очень откровенно."
    "Рубашка была не заправлена в юбку, а подвязана под грудью на узелок, а галстук обмотан вокруг кисти на манер банданы."

    play music music_list["goodbye_home_shores"] fadein 2.0 volume 0.8

    me "Это..."
    slp "Это Алиса. {w}Наше местное стихийное бедствие, на пару с Ульяной."
    slp "С ней ты ещё познакомишься, она тоже из нашего отряда, хоть и немного помладше."
    me "Вот как..."
    slp "Да. {w}Но ты не переживай, она это не со зла. Просто вот такой вот у неё характер, энергичный."
    me "Скорее уж эксцентричный?"

    show sl pioneer laugh with good_dspr
    slp "Ха-ха, ну можно и так сказать."

    show sl pioneer smile with good_dspr
    slp "Ну что, пойдём дальше? Тут недолго осталось."
    "Эта {i}эксцентричная{/i} Алиса выбила нас из колеи разговора, так что остаток пути мы проделали молча."
    "Я лишь смотрел по сторонам, и думал о том, что если поначалу это место показалось мне реальным, то сейчас кажется вычурно реальным."
    th "Или скорее, приукрашенным?"
    "Трава чуть ли не неоновая, ярко-зеленая, перенасыщенные цвета, и даже эта лёгкая рябь, появляющаяся над асфальтом в знойный день, выглядела «киношно»."
    "В жизни это всё так сильно не бросается в глаза."
    "Или я просто так давно не видел настоящего лета?"
    "..."

    show bg ext_houses_day with dissolve1

    "Вскоре мы уже шли между рядов маленьких одноэтажных строений, по всей видимости, домиков пионеров."
    "Выглядели они довольно уютно. {w}Хм, забавно, а я ожидал увидеть что-то вроде бараков."
    
    show sl pioneer normal with good_dspr
    slp "Вот этот домик, нам сюда."

    stop music fadeout 1.0
    play music music_list["dance_of_fireflies"] fadein 1.0 volume 0.6

    show bg ext_house_of_mt_day with dissolve2

    "Девушка вывела меня из раздумий."
    "Мы стояли перед таким же одноэтажным домиком, но этот отличался от остальных."
    "Крыша у него была острая, а не покатая, и окружали его кусты цветущей сирени."
    th "Прям как будто картина. Хоть сейчас в галерею."

    show sl pioneer normal far at center
    with dspr
    pause(1.0)

    play sound sfx_knock_door7_polite volume 0.9

    "Девушка тем временем поднялась на одну ступеньку, и постучала в дверь, почти сразу оттуда донёсся голос."
    mtp "Открыто, заходите!"
    "Девочка взялась за ручку двери и обернулась ко мне."

    show sl pioneer smile2 far with dspr
    slp "Пойдём!"
    "Я, доселе стоявший поодаль от домика, сделал пару неловких шагов, и направился вслед за Пионеркой, открывшей дверь, и заходящей внутрь."

    show sl pioneer smile2 close with dspr
    "Я решительно последовал за ней и оказался внутри."

    hide sl
    show bg int_house_of_mt_day
    show sl pioneer smile at left
    show mt pioneer normal at cright
    with dissolve1

    "Минуя внутреннее убранство домика, мой взор сразу же зацепился за девушку, сидящую за столом возле окна."
    "Она неторопливо что-то записывала то ли в тетрадь, то ли в какой-то документ."
    slp "Ещё раз здравствуйте, Ольга Дмитриевна, я вот новенького привела, как раз ведь сегодня должен был приехать."
    mt "Да, я знаю. Ну что, {i}Семён{/i}…"
    th "Она знает, как меня зовут!??"

    show mt pioneer smile with good_dspr

    "Девушка встала из-за стола, и выпрямившись, сделала пару шагов мне навстречу, улыбнулась, и продолжила."
    mt "Добро пожаловать! Жалко конечно, что ты задержался, но я уверена, что оставшееся время, которое ты проведешь здесь, принесёт исключительно положительные эмоции!"
    "Говорила она, как мне казалось, как типичный представитель убеждённых социалистов того времени."
    "Громкие фразы и полная уверенность в светлом будущем. {w}Хотя меня, как раз, будущее ждало очень даже туманное."
    me "Да, замечательно… {w}Только я хотел бы узнать, а где это {i}здесь{/i} находится?"
    me "А то, я, понимаете, родителям хотел написать, и-и…"

    show mt pioneer surprise
    show sl pioneer normal at fleft
    with good_dspr

    "Вожатая непонимающе уставилась на меня."
    mt "Как это, где… {w}Ты в пионерлагере «Совёнок». Забыл, куда ехал, что ли?"

    show mt pioneer laugh with half_good_dspr
    pause(1.25)
    show mt pioneer normal
    with half_good_dspr

    "Она немного усмехнулась, но без тона издёвки, и продолжила."
    mt "А насчёт родителей не беспокойся, я буквально сегодня утром с ними говорила."
    mt "Они сообщили мне, что ты приезжаешь, извинились за задержку, и пожелали приятного отдыха."
    th "Мои родители. {w}Звонили сюда. {w}Пожелали приятного отдыха… {w}Маразм крепчал."

    show mt pioneer smile with half_good_dspr

    me "А можно я им перезвоню? {w}Просто забыл кое-что сказать, и…"
    mt "Нет."
    "Вожатая опять улыбнулась."
    mt "Наша радиотелефонная линия только принимает звонки. Исходящие только в экстренные службы."
    me "Понятно..."
    th "Удобная отговорка или она говорит правду?"
    "Всё это время пионерка, которая меня сюда привела, стояла рядом, рассматривая предметы быта, и казалось, не находила в нашем диалоге ничего необычного."
    "Вожатая, она же Ольга Дмитриевна, казалось, собиралась сказать что-то ещё, но тут с улицы раздался звук трубы."

    play sound sfx_dinner_horn_processed volume 0.8

    "Только не живой, а явно записанный, издающийся из какого-то динамика."
    mt "Так, ладно. Потом разберёмся. Идите кушать."
    mt "Семён, потом придешь на склад, получишь свою форму."
    me "А я же… Я не… Куда?"
    "Учитывая, что я только появился здесь, где находится какой-то там склад я понятия не имел."

    show sl pioneer smile2 at cleft
    with good_dspr

    slp "Не переживайте, Ольга Дмитриевна, я отведу. Всё равно дел нет, сегодня же воскресенье."
    "Мне стало неловко, что этому милому созданию придётся возиться со мной, как с дитём малым."
    mt "Вот и отлично. Так, ну всё, время обеда, не опаздывайте!"
    mt "Меня не будет, вас посчитает вожатый другого отряда. {w}Всё, идите, кру-угом, шагом марш!"

    show sl pioneer normal with dspr

    "Пионерка демонстративно, но явно в шутку развернулась на месте по всем канонам строевой подготовки, только что не отсалютовала."
    "А я, бросив беглый взгляд на внутреннее убранство домика, поспешил за ней."

    hide mt
    hide sl
    show bg ext_house_of_mt_day
    show sl pioneer smile at right
    with dissolve1

    "Выйдя из домика, я закрыл дверь, и присоединился к пионерке, которая ждала меня, стоя у ступеней."
    slp "Ну что, как тебе наша вожатая? Не показалась тебе «эксцентричной»?"

    show sl pioneer laugh with half_good_dspr
    pause(1.5)
    show sl pioneer smile with good_dspr

    "Пионерка по-доброму усмехнулась, вспомнив хорошую шутку."
    th "Надо-же, я оказывается умею шутить? Да ещё так, чтобы девушка засмеялась? Это что-то новенькое!"
    me "Ты знаешь, вовсе нет. Напротив, она даже довольно… Обычная?"
    me "Ну, такая какая и должна быть вожатая в моём понимании."
    "Про себя я добавил."
    th "Если я вообще, конечно, имею понимание, какая должна быть вожатая…"
    "Пионерка же словно продолжила развивать мою мысль и начала говорить."

    show sl pioneer smile at cright
    with good_dspr

    slp "На самом деле Ольга Дмитриевна очень хорошая."
    slp "Возможно тебе она показалось немного строгой, но, вообще, она приятный человек."
    slp "И с нами общается почти на равных, несмотря на то, что старше на… {w}Лет 7-8 получается?"
    th "Ага, то есть если тут всем по 16-17, то ей что-то в районе 25?"
    th "Что же, она вполне выглядит на свой возраст, возможно получится найти с ней общий язык."
    "Внезапно в голову прокралась мысль."
    th "А почему никто не обращает внимания на мой возраст? Уж я-то на пионера в свои годы никоим образом не тяну…"
    me "А ты не знаешь, вожатая давно здесь?"
    "Не стоит игнорировать тот факт, что, учитывая её возраст, она вполне могла оказаться таким же попаданцем, как и я."
    "Хотя, как бы это было связано?"
    slp "Ну-у, не знаю, честно говоря. Но это точно не первая её смена в качестве вожатой. {w}А что такое?"
    "Действительно, а что?"
    me "Да вот думаю просто, это же каждый раз сюда добираться на смену! Лагерь-то у чёрта на рогах!"
    "Я попытался прощупать почву, акцентируя внимание на месторасположении."
    "Может, удастся выведать более точные координаты."

    show sl pioneer surprise with good_dspr
    pause(2.0)
    show sl pioneer laugh with good_dspr

    "Пионерка ненадолго уставилась на меня непонимающим взглядом, словно бы не стоило упоминать чёрта всуе. Но буквально через две секунды рассмеялась."
    slp "Ха-ха-ха, Семён, ну ты даёшь! Это же всё-таки её работа!"
    slp "Да и не приходится им так часто ездить, насколько я знаю. Приедут на пол лета, отведут три смены, и обратно домой! Работа-то вахтовым методом."

    show sl pioneer smile with good_dspr

    "От смущения я улыбнулся."
    "Но не до конца понял, чем это смущение было вызвано."
    "Тем ли, что выпалил глупость, или тем, что рядом со мной идёт прекрасная девушка и смеётся самым звонким и приятным смехом, что мне когда-либо доводилось слышать, а её глаза наполнены… радостью?"
    "Точно не знаю, но наверняка всё вместе."
    "В конце концов, мы направились в сторону столовой и разговорились."

    show black with clocks_in

    show bg ext_square_day
    hide black
    with clocks_out

    show black with clocks_in

    show bg ext_dining_hall_away_day
    hide black
    with clocks_out

    "За беседой я и не заметил, как мы миновали площадь, и повернув налево, оказались на тропинке перед невысоким одноэтажным строением, в котором легко угадывалась столовая."
    "Типичная такая, постсоветская столовка, где подают слипшиеся несоленые макароны и прочие гастрономические шедевры."
    "У крыльца столовой толпилась небольшая кучка пионеров, спешно заходящих внутрь."
    "Мы с моей спутницей невольно и одновременно ускорили шаг, ведь и так уже были в числе последних."
    me "А как у вас здесь кормят? Есть-то хоть можно?"

    show bg ext_dining_hall_near_day with dissolve

    slp "Конечно можно, и даже нужно! Хи-хи. {w}Кормят прекрасно, тебе понравится!"
    me "Ну что же, будем поглядеть…"

    stop ambience fadeout 2.0
    play ambience ambience_dining_hall_full fadein 1.5

    show bg int_dining_hall_people_day with dissolve1

    "Мы поднялись по ступенькам, и открыв дверь, оказались в… Столовой."
    "Самой обыкновенной. {w}Кафельный пол, такие же стены, металлические конструкции линии выдачи, и простенькие стулья, по типу тех, что стоят в школах, техникумах и институтах…"
    "Однако, всё выглядело не так, будь это наше время."
    "Всё было очень чисто и аккуратно, ничего не побито и не заляпано, плитка аж сверкала."
    "Уж не знаю, проводили ли тут на днях генеральную уборку, или всё действительно новое, но состояние помещения уже придавало уверенности."
    slp "Ну вот. Ты поищи пока свободный столик, а я пойду отмечу нас у вожатого другого отряда."

    hide sl with good_dspr

    "Кивнув, всё ещё озираясь по сторонам, я начал медленно продвигаться вглубь столовой, выискивая глазами стол, за которым не было бы ни одного пионера."
    "Не знаю почему, но сидеть с кем-либо кроме этой пионерки мне совсем не хотелось."
    "Да и есть на самом деле не хотелось. Что странно, учитывая, что с момента последнего моего приёма пищи {i}там{/i} прошло уже по меньшей мере часов двенадцать-тринадцать, а то и больше."
    "Вероятно, в критической ситуации мой организм мобилизовал стратегические запасы, чтобы не тратить время и силы на утоление голода."
    slp "Семён! Сюда!"
    "Я повернул голову в сторону источника звука."

    show sl pioneer smile far at center
    with good_dspr

    "В паре рядов столов от меня стояла пионерка рядом с пустым столом и махала рукой."
    th "Чёрт, как же я проглядел?"
    "С немного виноватым видом я подошёл к златовласой пионерке, и, запомнив место, мы вместе отправились получать свою пайку..."

    stop music fadeout 2.0
    play music music_list["so_good_to_be_careless"] fadein 2.0 volume 0.8

    hide sl
    show sl pioneer smile at center
    with long_dspr

    "..."
    "Через время мы уже сидели за столом с двумя подносами друг на против друга."
    "На тарелках исходило паром, и вроде как даже приятно пахло, и первое, и второе, и компот, всё как положено."
    "Однако, я не накинулся на еду, а лишь изредка ковырял вилкой то ли рис, то ли перловку, я не обратил внимания."
    "Ибо на меня опять нахлынул неприятный поток мыслей, уносящий меня в какие-то странные дали, связанные с вопросами «Как я тут оказался?», «Что это за место?» «Здесь опасно?» и иже с ними."
    "Да и даже если бы не они, я просто чувствовал, что не хочу есть."
    "Незнакомое место, обстановка, люди, всё это не располагает к наслаждению пищей."

    show sl pioneer surprise with dspr

    slp "Эй! Всё хорошо?"
    "Из круговорота игр мозга меня вывела пионерка, которая недоумённо и с какой-то заботливой опаской смотрела на меня."
    slp "Семён, ты чего не кушаешь?"
    me "Да как-то не хочется что-то… {w}Не голоден… {w}Я… В автобусе немного укачало просто. Вот."

    show sl pioneer smile2 with good_dspr

    "Пионерка словно бы немного выдохнула, и ответила."
    slp "А-а-а, вот оно что."
    slp "Фух, я уж думала ты неважно себя чувствуешь."
    slp "А с автобусами такое бывает, да, а на тебе ещё и вон сколько одежды."

    show sl pioneer normal with dspr

    slp "Тогда, после обеда незамедлительно переодеваться, а пока вот, пей компот. Освежит, и станет полегче."
    me "Да-а… Компоту, пожалуй, можно, спасибо."

    show sl pioneer smile with dspr

    "Девочка улыбнулась, и продолжила кушать."
    th "Интересно, она со всеми так мила, или я чем-то заслужил особенное внимание с её стороны?"
    "..."
    "Я сделал глоток, и сразу почувствовал, как живительная, приятно сладкая на вкус, с фруктово-ягодными нотками жидкость попадает в горло, и стекает по пищеводу."
    th "Что же, по крайней мере напитки тут делать умеют, так что от жажды не помру."

    show sl pioneer normal with dspr

    "..."
    "Я так увлекся компотом, что почти не заметил, как осушил весь стакан, а затем принялся подцеплять вилкой кусочки фруктов и ягод с кружки и кушать их."
    "Пионерка тоже заканчивала приём пищи, и вытирала рот салфеткой, как вдруг посмотрела мне за спину, и сказала."

    show sl pioneer smile with dspr

    slp "А-а-а, наше маленькое стихийное бедствие."
    slp "Привет, Уля, чем занимаешься?"

    stop music fadeout 1.0
    play music music_list["i_want_to_play"] fadein 1.0 volume 0.9

    "Я обернулся."

    show us sport normal far at left
    with long_dspr

    "К нам уже подходила девочка, одетая в шорты и красную футболку с надписью «СССР» на всю грудь."
    "Она была явно помладше всех тех, с кем мне уже довелось познакомиться лично."
    "На вид ей было лет 13–14."

    show us sport smile with dspr

    us "Чем-чем, поела вот, хочу у поварих пару конфет выпросить, жду пока вожатые уйдут, хы!"
    us "А ты ещё кто такой, таинственный незнакомец?"
    "Последняя фраза была явно адресована мне. Я уж было собрался открыть рот, и ответить, но немного поперхнулся кусочком яблока со дна кружки и Пионерка опередила меня."

    show sl pioneer smile2 with dspr

    slp "Это наш новенький, знакомься, Семён. Семён, Ульяна."
    "Прочистив горло, я сказал."
    me "Приветствую патриотов!"
    "Мысленно я уже прозвал её «СССР»."

    show sl pioneer smile
    show us sport laugh2
    with dspr

    us "Здрасьте-здрасьте."
    us "А ты чего, на северный полюс собрался, в зимних штанах сидишь?"
    slp "Никуда он не собрался, он только приехал и ещё не переоделся."
    slp "А тебе бы тоже, кстати, стоило это сделать. Где форма?"
    "Я был рад, что моя спутница взяла её на себя, пока я спокойно доедал остатки со своего стакана. Никогда не любил общаться с детьми."

    show us sport laugh with good_dspr

    us "А я, это, ну-у… Я побежала, вот, мне пора!"

    show us sport laugh at run_away_left
    pause(1.0)
    hide us

    "С этими словами она шмыгнула в сторону выхода из столовой так быстро, что аж пятки засверкали."
    
    show sl pioneer smile2 with good_dspr

    "Девушка рассмеялась."
    slp "Хорошо быть помощницей вожатой."
    slp "Забот хоть и больше, зато можно быстро спровадить всяких, сделав замечание."

    show sl pioneer smile with good_dspr

    th "Помощница вожатой, значит? Так она мне помогает не по доброте душевной, а по служебным обязанностям?"
    "Я улыбнулся, но оставил её последнюю фразу без комментариев."

    show sl pioneer normal with dspr

    me "Ну что, ты поела? Ульяна права, на северный полюс я не собираюсь, и переодеться во что-нибудь полегче не помешало бы."
    slp "Да, конечно, пойдём! Только унесём подносы."
    "..."

    stop ambience fadeout 2.0
    stop music fadeout 3.0

    show bg ext_dining_hall_near_day with dissolve2

    play ambience ambience_camp_center_day fadein 2.0
    play music music_list["goodbye_home_shores"] fadein 2.0 volume 0.85

    "Мы сдали свои подносы, и вышли на улицу."
    "За те двадцать минут, что мы провели внутри, погода успела поменяться."
    "Небо немного покрылось облаками, и самый лютый зной уже спал."

    "Пока я разглядывал метеорологическую обстановку на небе, Пионерка чем-то пошебуршала в карманах юбки, и утвердительно хмыкнула."
    "Улыбнувшись, она обратилась ко мне."

    show sl pioneer smile with dspr

    slp "Ключи от склада у меня с собой, так что можем идти за формой прямо сейчас."
    slp "Тут как раз идти недалеко, буквально столовую обогнуть."
    th "Так значит я мог бы дойти и сам, и не напрягать эту прекрасную девицу?"
    th "Но в её компании будет точно приятнее."
    me "Только в путь!"
    "Бойко выдал я, и мы двинулись в сторону склада."
    "..."

    stop ambience fadeout 1.0
    pause(1.0)
    play ambience ambience_forest_day fadein 1.0

    show bg ext_storage_day
    show sl pioneer smile far
    with dissolve3

    "Мы подошли к складу, который скорее выглядел, как несколько гаражей, составленных рядом друг с другом."
    th "Странный контраст между сверкающим лагерем и этим складом, ну ладно."

    slp "Сейчас открою ворота, и подберём тебе форму."
    me "Хорошо."

    hide sl with dspr

    "Пока Пионерка возилась с огромным амбарным замком, я огляделся вокруг."
    "Со стороны, откуда мы пришли, всё ещё виднелось здание столовой, впереди маячил высокий сетчатый забор и доносились веселые крики детей."
    th "Спортплощадка?"
    "За складом же почти сразу начинался густой лес."

    show sl pioneer sad far at left
    with dspr

    slp "Ай!"
    "Я встрепенулся и оглянулся на звук."
    "Пионерка, доселе возившаяся с замком, терла палец, а связка ключей валялась рядом на траве."

    show sl pioneer sad close at center
    with good_dspr

    "Я подошел ближе и посмотрел на палец Пионерки, который она придерживала другой рукой, дула и терла."
    slp "Опять прищемила..."
    slp "Дурацкий замок, вечно заедает!"
    "Видимых повреждений я не увидел, скорее всего, ушиб небольшой."
    me "Больно наверное?"

    show sl pioneer shy close with good_dspr

    "Я аккуратно приложил свои руки ниже её, и подул на палец."
    me "Приложи палец к мочке уха, станет полегче. {w}А я сейчас сам открою."

    show sl pioneer shy at fleft
    with good_dspr

    "Я взял связку ключей с земли, и пару раз тыкнув не тем, подобрал нужный."
    "Ключ зашел в замочную скважину, но проворачиваться всё никак не хотел."
    "Я встал поудобнее, и с силой надавил на ключ."

    play sound sfx_lock_open

    "Замок с глухим щелчком открылся, и нижняя часть повисла на крюке, который был продет в два уха."

    show sl pioneer smile2 with dspr

    th "Ну да, классическая гаражная схема."
    "Я вытащил замок, положил его рядом на земле, и открыл дверцу склада."
    me "Путь открыт! Прошу, дамы вперёд."
    "Я отступил назад, давая Пионерке зайти внутрь."

    show sl pioneer tender at center
    with good_dspr

    "Она подошла, смотря на меня не иначе, как на средневекового рыцаря, победившего злостного дракона, и сказала."
    slp "Спасибо большое!"

    show sl pioneer shy at cleft
    with dspr

    slp "Ты не только мужчина, но и настоящий джентльмен!"

    show sl pioneer smile2 at left
    with dspr
    pause(1.0)
    hide sl with dspr

    "Она зашла внутрь."
    "Теперь настала моя очередь краснеть. Ведь я только что:"
    "1)	Утешил девушку"
    "2)	Помог с проблемой"
    "3)	Уступил дорогу"
    "Мелочи жизни, но как давно мне не приходилось оказывать внимание противоположному полу…"
    "Думаю я явно замешкался, ведь… {w}А как её зовут то?"
    "Господи! {w}Какой позор! {w}Мы ходим вместе уже половину дня, а имени её я всё так и не спросил. {w}Да и не произносил никто…"
    slp "Семён, ты идешь?"
    "Донеслось изнутри."
    me "Да, захожу!"

    stop ambience fadeout 2.0
    stop music fadeout 2.0
    pause(2.0)

    show bg int_warehouse_day
    show sl pioneer normal at right
    with dissolve1

    play ambience ambience_int_cabin_day volume 0.8 fadein 3.0
    play music music_list["silhouette_in_sunset"] fadein 2.0 volume 0.7

    "Я переступил через порог, и оказался в довольно опрятном складском помещении."
    "Свет мягко пробивался через окно, освещая небольшой столик с книжкой, развешанные комплекты формы, ..."
    "... гладильную доску, какие-то мешки и прочие предметы, наполнявшие это место."
    "В это время Пионерка уже стояла рядом с рядами крючков с готовыми, отстиранными и отглаженными комплектами, и над чем-то думала."

    show sl pioneer smile with dspr

    "Пионерка обернулась на меня."
    slp "У тебя какой размер?"
    "Я задумался."
    me "У меня, это, нуу…"

    show sl pioneer smile2 with half_good_dspr

    slp "Хи-хи, понятно, не продолжай."
    slp "Глупо было спрашивать это у парня, вы никогда не знаете."

    show sl pioneer smile with dspr

    slp "Так, сейчас…"

    hide sl with half_good_dspr

    "Она полезла в шкафчик, а я лишь смутился."
    th "Ну не запоминаю я такое, что поделать!"
    slp "Вот, нашла!"

    hide sl
    show sl pioneer normal at cleft
    with half_good_dspr

    "Пионерка встала, поправила юбку, и у неё в руках я увидел сантиметр."
    me "Ха-ха, сейчас мы вашего мальчика измерять будем?"
    "Процитировал я известный советский мультфильм."

    show sl pioneer laugh with dspr

    "Пионерка рассмеялась, и ответила."
    slp "А как же, всё должно быть профессионально! Так, подними руки, сейчас я возьму с тебя мерки."

    show sl pioneer smile close at center
    with good_dspr

    "Я выполнил её просьбу, а она подошла ближе, и растянув измерительный прибор, начала измерять мои параметры, иногда что-то утвердительно хмыкая про себя."
    "Всё больше она напоминала мне ни то маму, ни то старшую сестру."
    th "Или девушку?.."
    "Такая же заботливая, готовая помочь."
    "..."
    "Когда дело дошло до обхвата талии, я почувствовал, что её неудобно."
    "Она, видимо из-за разницы в росте, не могла полностью меня обхватить, и ей приходилось всё сильнее и сильнее ко мне прижиматься…"

    show sl pioneer shy close with dspr

    "А учитывая её, от природы, немалые размеры, я чувствовал, как её грудь прижимается к моим ребрам, а голова чуть ли ни лежит на плече."
    "Я почувствовал её запах, запах её волос… "
    "Не знаю, что за шампунь она использовала, но её длинные, светлые волосы, чуть ли ни желтого цвета, пахли буйством полевых цветов, и… {w}Лета?"
    "От этого запаха, и от того, что молодая, красивая девушка, {i}почти{/i} обняла меня, становилось дурно."
    "Я опять начал краснеть, а ещё, почувствовал напряжение ниже пояса."
    th "Чёрт."

    show sl pioneer smile2 with dspr

    "Но вот, она от меня отпрянула, и гордо заявила."
    slp "Мальчик измерен! Сейчас подберем тебе форму."

    show sl pioneer smile far at left
    with good_dspr

    "Я выдохнул, улыбнулся, и сел на стул рядом, пока Пионерка выбирала комплект из готовых."
    me "Кстати… Ты меня извини, некрасиво это, но… "
    me "Я всё ещё не знаю, как тебя зовут. {w}Совсем забыл спросить, вылетело из головы."

    show sl pioneer shy far with dspr

    "Пионерка обернулась, мило улыбнулась, и хихикнув, сказала."
    slp "Ой, и правда. А я и не представилась… {w}Ничего."
    sl "Меня зовут Славяна, но все зовут Славя. {w}И ты зови."
    me "Славя... Красивое имя!"

    show sl pioneer smile far with dspr

    th "И как раз подстать образу."
    th "Переодень её сейчас в классический русский наряд, и получится вылитая крестьянка, за которой гоняется каждый парень на деревне."
    sl "Нашла, вот, как раз твой размер."

    show sl pioneer smile at center
    with good_dspr

    "Я встал, и взял у Слави плечики, на которых висел полный комплект пионерской формы мужского образца:"
    "шорты, белая рубашка, ремень и красный галстук."
    me "Спасибо. {w}А обувь?"

    show sl pioneer smile2 with dspr

    sl "Ой, точно! Сейчас…"

    show sl pioneer smile at fleft
    with dspr
    pause(1.75)
    show sl pioneer normal at center
    with dspr

    "Славя отошла в сторону, к стойке с обувью, и взяла одну пару."
    "Вернувшись, она протянула их мне."
    me "Откуда ты знаешь, что это мой размер?"
    sl "А я и так вижу, глаз намётанный."

    show sl pioneer smile with good_dspr

    "Девушка улыбнулась и смотрела на меня, а я стоял с одеждой на плечиках в одной руке, и парой обуви в другой."
    "Странная картина продолжалась не более пары секунд."
    pause(1.0)
    sl "Ну, что стоишь? Переодевайся."
    me "Да я бы с радостью, но… {w}Тут есть кабинка, или…"

    show sl pioneer shy with dspr

    "Не успел я договорить, как Славя тут же покраснела, и сказала."
    sl "Ой, точно, хи-хи. Сейчас я отвернусь, переодевайся."

    show sl pioneer smile2 far with dspr
    pause(0.5)
    hide sl with good_dspr

    "Пионерка спешно отвернулась, и принялась изучать убранство склада."
    "Я же в это время чуть отошел в сторону, к стулу, и начал переодеваться."
    "..."
    "Когда дошло дело, до того, чтобы переложить все свои вещи из зимних штанов в пионерские шорты, подвернулась отличная возможность провести ревизию."
    "И так, что мы имеем:"
    "1)	Пачка сигарет, одна штука (19 сигарет)"
    "2)	Зажигалка, одна штука"
    "3)	Телефон, одна штука"
    "Не густо."
    "Я быстро включил экран телефона, и проверил заряд. {w}80%%."
    "Ну, на какое-то время хватит."
    "Сети, кстати, не было, вместо привычных палочек горел жирный красный крест."
    th "И почему я сразу не додумался позвонить, как только попал сюда?"
    "Карманы оказались довольно глубокими, так что сложить в них все свои вещи так,  чтобы они не торчали, не составило проблемы."
    "Перейдя к обуви, я приятно удивился тому, что внутри лежала пара белых носков."
    th "Ну слава Богу, не придется таскаться в зимних."
    "Обувь, кстати, представляла из себя странную смесь ботинок, туфель и сандалий, из-за открытых частей."
    "..."
    "Закончив переодевания, я оглядел себя, подвигался и утвердительно хмыкнул."
    "Одежда сидела как влитая, Славя точно подобрала размер."
    me "Готов к труду и обороне!"
    "Заявил я бойким голосом, привлекая внимание Слави."

    show sl pioneer smile far with good_dspr

    "Она обернулась и улыбнулась."
    sl "Ну вот, был джентльмен, а теперь ещё и красавец."
    "Я немного ушел в краску."
    me "Ну прям-таки уж и красавец?"

    show sl pioneer smile close with good_dspr
    pause(0.5)
    show sl pioneer angry with dspr

    "Девушка подошла ближе, и нахмурилась."
    sl "А вот нет! Платок где?"
    me "Ой..."
    "Красный галстук остался лежать на стуле."

    show sl pioneer normal with long_dspr

    "Славя наклонилась за ним, и в несколько ловких движений завязала на мне платок по всем канонам, после чего снова переменилась в лице, и сказала."

    show sl pioneer smile with dspr

    sl "Ну, теперь точно красавец!"
    "Я улыбнулся в ответ, и сказал."
    me "Спасибо. Ну что, мы тут закончили?"
    sl "Нет же ещё! {w}Тебе нужен комплект постельного белья."
    sl "Спать то тебе где-то надо."
    th "Об этом я как-то не подумал."
    sl "Я сейчас."

    show sl pioneer normal far with good_dspr
    pause(0.5)
    show sl pioneer normal close with good_dspr

    "Она развернулась, и быстро похватала всё необходимое:"
    "простынь, наволочку и вторую простынь, вместо пододеяльника."
    sl "Вот, держи."
    me "Ага… {w}А куда мне идти?"
    sl "Вернемся обратно к Ольге Дмитриевне, она определит тебе домик, в котором ты будешь жить."
    me "Тогда двинули?"

    show sl pioneer smile2 with dspr

    sl "Хи-хи, да. Только вещи свои не забудь."
    '...'
    "Я собрал свою одежду, взял её под одну подмышку, а комплект постельного под другую, и вышел со склада."
    "Славя последовала за мной."

    stop ambience fadeout 2.0
    stop music fadeout 3.0

    pause(2.0)

    hide sl
    show sl pioneer shy at right
    show bg ext_storage_day
    with dissolve2

    play ambience ambience_forest_day volume 0.9
    play music music_list["your_bright_side"] fadein 2.0

    pause(0.5)

    sl "Семён… Можно тебя попросить?"
    "Я положил всю свою ношу на ступеньки перед дверью, положив свои вещи на них, а сверху постельное."
    me "Конечно, для тебя что угодно!"
    "Славя, кажется, немного замялась, и неуверенно начала."
    sl "Я, ну-у… Хотела тебя проводить до домика Ольги Дмитриевны, но вспомнила…"
    sl "Мне тут помочь надо в столовой, поварихи попросили, когда мы на обеде еду получали."
    sl "Вот, ну-у, не хотелось бы тебя одного оставлять, но мне уже пора."
    sl "Сам дорогу до домика вожатой найдешь?"
    me "Да думаю не заблужусь, ты и так очень много для меня сделала!"

    show sl pioneer smile2 with good_dspr

    sl "Ох, ну хорошо, ты очень мил, правда!"
    sl "Ну давай я тебе напомню:"
    sl "вернешься к столовой, выйдешь на площадь."
    sl "А там направо, и опять прямо."
    sl "Упрешься в ряд домиков, поворачивай налево, {w}на следующем повороте направо и опять направо, и до конца."

    show sl pioneer smile with half_good_dspr

    sl "Так дойдешь. Запомнил?"
    th "Ничерта я не запомнил."
    th "Я лишь наслаждался её прекрасным, ангельским голосом, словно бы передо мной пела самая прекрасная птичка на свете."
    me "Да, запомнил. Спасибо!"
    "..."
    me "До встречи, я надеюсь?"
    sl "Конечно, ещё встретимся!"

    show sl pioneer smile far with long_dspr

    "Девушка, начала удаляться, но через пару шагов обернулась, и крикнула."
    sl "Ой, закрой склад пожалуйста! Замок сам защелкивается!"
    me "Хорошо!"

    pause(0.5)
    show sl pioneer smile far at walk_away_right
    pause(2.0)
    hide sl

    "Проводив её взглядом, я грустно вздохнул, лишившись компании, и сел на ступеньку."
    "Как будто оказался в каком-то квесте, честное слово… {w}И эта девушка."
    "Славяна. {w}Так ко мне добра. {w}Что же происходит?"

    call smoking_process(with_pause=1.0)

    "Погружаясь в водоворот мыслей, я достал из кармана сигареты, и закурил."

    stop music fadeout 2.0
    play music music_list["reflection_on_water"] fadein 2.0 volume 0.5

    "Мысли опять потекли в сторону решения загадки касательно моего положения здесь."
    "Но Солнце так приятно пригревало, а на фоне был слышен шум леса, пение птиц… "

    show blink

    "Что я решил пока откинуть все тревоги в сторону, облокотился спиной на дверь склада, закрыл глаза..."
    "И просто ни о чем не думал, наслаждаясь природой и каждой затяжкой сигареты…"
    "Затяжкой. {w}Интересно, автобус всё ещё на месте? Вот бы проверить."
    "..."

    stop music fadeout 3.0

    hide blink
    show unblink
    pause(1.0)
    hide unblink

    "Докурив сигарету, я ещё немного посидел, но вскоре поднялся."
    "Закрыл склад, взял свои вещи и направился обратно в сторону столовой."
    "..."

    stop ambience fadeout 1.0
    play music music_list["my_daily_life"] fadein 3.0 volume 0.8

    show bg ext_dining_hall_away_day with dissolve2

    play ambience ambience_camp_center_day fadein 1.0

    "Я миновал столовую."

    show bg ext_square_day with dissolve2

    "И вышел к площади."
    "Так, и куда дальше? Направо, или налево?"
    "Черт… {w}Только я мог запутаться в двух соснах."
    "..."
    th "Эники-беники… Ладно. Налево."
    "..."

    show bg ext_boathouse_day with dissolve2

    "Я сам не понял, как оказался на лодочной станции."
    "Значит, всё-таки надо было поворачивать направо."
    "Я уже было собирался развернуться, и уйти, как тут меня окрикнули."
    dvp "Эй, путешественник!"

    show dv swim normal with good_dspr

    "Передо мной предстала та самая «эксцентричная» пионерка, только сейчас она была в купальнике."
    me "Э-э, привет. {w}Алиса, верно?"
    dv "Верно. {w}Ты чего это с тюками тащишься? Только приехал и уже сбежать решил?"

    show dv swim grin with dspr
    pause(0.5)
    show dv swim normal with dspr

    "Она стрельнула глазками."
    me "Да нет, я… Одежду получал, вот и… Заблудился немного. {w}Мне к Ольге Дмитриевне надо."

    show dv swim laugh with dspr

    dv "Ну ничего себе, немного!"
    "Она рассмеялась."

    show dv swim normal with dspr

    dv "Эх, ты, горе луковое. Ладно, помогу тебе один раз. Слушай внимательно."
    "..."
    "Она объяснила, как пройти до домика Ольги Дмитриевны, и в этот раз я действительно слушал."
    me "Спасибо!"

    show dv swim grin with half_good_dspr

    dv "«Спасибом» сыт не будешь! За тобой должок!"
    "Она опять улыбнулась глазами."
    th "Ну конечно, даже в социалистическом мире все ищут личной выгоды."
    me "Хорошо… {w}Слушай, а что ты тут делаешь? Я думал, что пионеры, ну… Работают там, и всё такое."

    show dv swim normal with dspr

    th "Правда ли я так думал, или просто решил выпалить первое, что пришло в голову, чтобы занять неловкую паузу, я сам не понял."
    dv "Да чё это бы? {w}Не все и не всегда."
    dv "К тому же, сегодня воскресенье, работы никакой нет, в любом случае."
    th "Ага, воскресенье. А ехал я на встречу в субботу, значит время не сбилось, и сейчас действительно время около полудня следующего дня."
    th "Было ещё странно то, что я пока нигде и ни у кого не увидел часов. Ни настенных, ни наручных."
    me "Вот как, ну понятно. Ладно, бывай! Ещё раз спасибо за помощь!"

    pause(0.5)
    show dv swim normal at walk_away_left
    pause(2.0)
    hide dv

    "Алиса попрощалась, и направилась к берегу, а я, наконец-то, двинулся в сторону домика Ольги Дмитриевны."

    show bg ext_square_day with dissolve1

    "Вернулся на площадь."

    show bg ext_houses_day with dissolve1

    "Прошел в сторону домиков."
    "Пока я преодолевал свой путь, я в очередной раз призадумался."
    th "А почему, я, собственно, такой смелый?"
    "Зная себя, который трясется при первой встрече с незнакомцами, должен был забиться куда-нибудь под куст, кататься по траве и тихо сходить с ума."
    "Но нет же."
    "Попал из родного города черте знает куда, черте знает {i}когда{/i}, и нате пожалуйста, хожу, шучу, решаю бытовые вопросы."
    "Вернуться к размышлению над своей смелостью я решил позже, так как подошел к домику Ольги Дмитриевны."

    show bg ext_house_of_mt_day with dissolve1

    th "Блин, а как бы постучать?"

    play sound sfx_knock_door7_polite

    "Я еле как вытянул наиболее свободную руку и постучал в дверь."
    mt "Да, войдите!"
    th "Легко сказать, блин!"
    "Еле как дотянувшись до ручки, и нажав на неё, я чуть ли не ввалился в помещение."

    play sound sfx_open_cabinet_1
    stop music fadeout 2.0

    show bg int_house_of_mt_day
    show mt pioneer normal far at right
    with dissolve

    "Я вытянулся по стойке с вещами в руках, и отрапортовал."
    me "Пионер Персунов по вашему приказанию прибыл!"

    play music music_list["tried_to_bring_it_back"] fadein 2 volume 0.87

    show mt pioneer smile with dspr

    "Вожатая улыбнулась, и сказала."
    mt "Ну, наконец-то, а я уж заждалась!"
    mt "Так, клади пока вещи на соседнюю койку."
    "..."
    mt "Присядь пока, а я посмотрю, куда тебя можно определить…"

    hide mt
    show mt pioneer normal at cright
    with good_dspr

    "Я сел на стул рядом с кроватью, и начал осматривать помещение."
    "Небольшая двухместная комната с большим окном по центру, вот и всё, что можно было сказать про домик Ольги Дмитриевны."
    "За тем, разве что, исключением, что порядка здесь было не больше, чем в моей квартире."

    show mt pioneer sad with dspr

    "Вожатая, тем временем, тёрла лоб, и нахмурившись, уже не в первый, по всей видимости, раз, перелистывала тетрадь."
    mt "Слушай, Семён… Такое дело."
    "Я напрягся."
    mt "Кажется, мне некуда тебя заселить."
    "Я обомлел."
    "Нет, я, конечно, понимаю своё странное попадание сюда, но здесь все ведут себя так, словно не происходит ничего необычного."
    "Что ещё за сюжетный поворот?"
    me "И… {w}Где же я буду спать?"
    mt "Хмм… Вообще, это не по правилам, но…"
    me "Но?"

    show mt pioneer normal with dspr

    mt "В целом, можешь остаться в моём домике."
    mt "Конечно, вожатые и пионеры не должны жить вместе, но что поделать… {w}Я объясню всё начальству."
    "От чего-то я проникся озабоченностью к этой проблеме."
    "Хотя, должно ли меня волновать, где я буду спать? Ведь я всё ещё не выяснил, {i}где{/i} я нахожусь."
    "Но тем не менее, хотелось проявить сочувствие и содействие."
    me "Ольга Дмитриевна, а вы уверены? {w}Я не хотел бы доставить вам проблем."
    th "Странно, я обращаюсь к ней на «Вы»?"
    me "Я вполне могу расположиться где-нибудь в коморке, или подсобке…"

    show mt pioneer surprise with dspr

    mt "Ни в коем случае! Исключено! Мой пионер не будет спать как бомж!"
    mt "Всё, решено!"

    show mt pioneer smile panama far at right
    with long_dspr

    mt "Я сейчас пойду в административный корпус, предупрежу начальника лагеря обо всём, а ты пока располагайся."
    mt "Сегодня воскресенье, так что дел нет. Можешь не торопиться. Пройдись по лагерю, осмотрись."
    mt "И да. Так как мы будем жить вместе, вынуждена предупредить."
    mt "Со своей стороны поддерживать порядок, в мои вещи не лезть, и ни на что не намекать!"

    show mt pioneer grin panama far with dspr
    pause(1.0)
    show mt pioneer normal panama far with dspr

    mt "А то у вас такой возраст…"
    th "Мне показалось, или на мгновение она покраснела?"
    "Я встал, и отсалютовал."
    me "Есть, мэм!"

    show mt pioneer smile panama far with dspr

    "Вожатая улыбнулась, и ответила."
    mt "Вот и отлично! Я ушла, не теряйся!"

    show mt pioneer smile panama far at walk_away_right
    pause(1.0)

    play sound sfx_close_door_1 volume 0.8
    pause(1.0)

    "С этими словами она выпорхнула из домика, оставив меня одного."
    "..."
    "Я ещё раз оглядел помещение."
    th "«Поддерживай порядок со своей стороны»… {w}Ну конечно."
    th "У самой то вон нижнее белье на спинке кровати висит."
    "Так, ну ладно. Приступим."

    stop music fadeout 2.0
    pause(1.5)
    play music music_list["so_good_to_be_careless"] fadein 2.0 volume 0.8

    "Я застелил свою постель, а свои вещи убрал под кровать, ибо не стал лезть в шкафчик к вожатой… {w}Мало ли."
    me "Ну. Вот так, как-то."
    "Я удовлетворительно осмотрел проделанную работу, и сел на стул, достав из кармана мобильник."
    "На экране отобразилось время: 15:40."
    th "Хм. Вполне похоже на правду. Что же, и время не сбилось?"
    "Несмотря на возможность иметь при себе время, я всё же решил не таскать с собой предмет из {i}своего{/i} времени."
    "Неизвестно, как на него отреагируют {i}здесь{/i}."
    "Посему, выключил все необходимые службы, чтобы не разряжать батарею просто так и засунул его в подушку."
    "..."
    th "Вожатой всё нет… Чем бы заняться?"
    "Можно конечно и прогуляться, но ключа от домика у меня нет..."
    "А получать по шапке, за то, что ушел и оставил домик незакрытым, ой как не хотелось."
    "Хм, кажется, я видел перед домом гамак. Может, в нём посидеть?"

    show bg ext_house_of_mt_day with dissolve1

    "Я вышел на улицу, и огляделся."
    th "Хорошо, что наш домик находится на отшибе, вероятность случайных гостей минимальна."
    th "Хотя, это всё-таки домик вожатой, к ней, наверное, часто захаживают…"
    "..."

    play sound sfx_bed_squeak2 volume 0.8

    "Расположившись в гамаке, я, на свой страх и риск затянул сигарету."

    call smoking_process()

    "Ощущения были как в молодости, когда приходилось гаситься, и постоянно озираться, чтобы ни дай Бог, не спалил никто."
    "..."
    "Потушив окурок, и выкинув его подальше в траву, я откинулся, и закрыл глаза."

    show blink

    stop music fadeout 2.0
    pause(1.0)
    play music music_list["reminiscences"] fadein 2.0 volume 0.4

    call to_nvl_mode

    "Хех, вот те раз."
    "Оказался неизвестно {i}где{/i}, неизвестно {i}когда{/i} и {i}как{/i}, и пожалуйста, развалился в гамачке, потягивая сигаретку, наслаждаюсь тёплым летним днём и пением птичек…"
    "Нет, тут точно что-то не чисто. И с этим местом, и со мной."
    "Может, меня накачали чем-то, что я так осмелел?"
    "..."
    "Очередные пространные рассуждения начали уносить меня в глубины подсознания, и скоро я задремал…"
    "..."

    stop ambience fadeout 2.0
    stop music fadeout 2.0
    pause(1.0)
    play music music_list["sparkles"] fadein 3.0 volume 0.4

    nvl clear
    "Снилась мне какая-то неразбериха."
    "Один из тех случаев, когда сложно выудить какие-то осязаемые моменты из сна, а все воспоминания представлены скорее в виде ощущений…"

    call to_adv_mode

    hide blink
    show bg ext_bus_night
    show prologue_dream
    with dissolve
    
    pause(0.5)

    "Помню автобус..."

    show bg ext_camp_entrance_night
    with dissolve
    
    pause(0.5)

    "Ворота в лагерь..."

    play sound sfx_scary_sting

    show bg d1_rena_sleep
    with dissolve
    
    pause(0.5)

    "Какую-то страшную ебаку..."
    "И..."

    hide prologue_dream
    show cg sleep_nothingness
    with dissolve

    "Пустоту."
    "Всеобъемлющую, всепоглощающую."
    "И такую тягучую, плотную, неприятную, от которой никак не получается освободиться…"

    window hide

    call set_time("sunset")

    stop music fadeout 5.0

    pause(2.0)

    window show

    sl "Семён! {w}Семён! {w}Сёма, блин, проснись!"
    th "Что?"

    play ambience ambience_camp_center_evening fadein 5.0

    hide cg
    show bg ext_house_of_mt_sunset
    show sl pioneer smile
    with dissolve

    pause(1.0)

    "Я продрал глаза. Передо мной стояла Славя."
    me "Что? Что происходит?"
    
    show sl pioneer laugh with good_dspr

    sl "Аха-ха, ну ты даёшь!"
    sl "Продрых пол дня, и спрашиваешь, что происходит."
    sl "Вечер уже, Семён, время ужина."

    show sl pioneer smile with dspr

    "Я поднялся с гамака, покачиваясь."
    me "Ужин — это хорошо… {w}А ты чего тут?"
    sl "Я хотела к Ольге Дмитриевне зайти, спросить, будет ли она на ужине. {w}Ну, и-и…"

    show sl pioneer shy with dspr

    "Славя, кажется, немного замялась."
    sl "Хотела спросить у неё, куда тебя заселили… {w}Чтобы потом в гости зайти…"
    sl "Ты же был бы не против?"
    th "Вот те раз. Эта девочка явно что-то замышляет… {w}А вот плохое, или доброе – вопрос."
    "Я улыбнулся, и ответил."
    me "Ну конечно, был бы не против! {w}Твоей компании я всегда за."
    me "А вожатая ушла, незадолго после того, как я к ней явился. И да, жить я буду у неё, говорит, мест нет."

    show sl pioneer surprise with good_dspr

    "Славя округлила свои, и без того большие глаза."
    sl "Ого! Ну, это даже хорошо, знаешь. У неё хороший домик, не как у всех остальных. И место приятное."
    me "Да, думаю не зря Ольга Дмитриевна его выбрала. {w}О, а вот кстати, она."

    show mt pioneer normal panama at left
    with good_dspr

    mt "Славя, ты тут какими судьбами?"

    show sl pioneer smile with dspr

    sl "А я хотела узнать вот, ждать вас на ужине или нет."
    mt "Да, я буду. Сейчас как раз горн прозвучит, так что, можно уже выдвигаться."

    show mt pioneer smile panama with dspr

    mt "Кстати, Семён. {w}Руководство всё одобрило, так что мы с тобой теперь официально сожители!"
    th "Спасибо, хоть не пара."
    "Я улыбнулся, и сказал."
    me "Рад слышать! {w}Ну что, может пойдём ужинать?"
    mt "Да, идёмте."
    "Втроём мы двинулись в сторону столовой."
    "..."

    show bg ext_dining_hall_away_sunset with dissolve2

    play music music_list["dance_of_fireflies"] fadein 2.0 volume 0.75

    "Пока мы шли, прозвучал горн, а на подходе к столовой, помимо меньшей толпы пионеров, я заметил, что начало вечереть."

    show mt pioneer normal panama with dspr

    mt "Вы пока заходите, получайте пайку, я вас отмечу. А мне надо поговорить с вожатыми других отрядов."
    sl "Хорошо."

    show mt pioneer normal panama at walk_away_left
    pause(0.75)
    hide mt with dspr

    stop ambience fadeout 1.0

    show bg int_dining_hall_people_sunset with dissolve2

    "Мы зашли в помещение."

    play ambience ambience_dining_hall_full fadein 1.0

    "В этот раз народу и правда успело набежать меньше, так что мы могли выбрать столик, за который сесть."
    me "Давай вон туда, в уголок."
    sl "Давай."
    "Мы взяли свои порции, и сели за стол."

    hide sl
    show sl pioneer normal at right
    with good_dspr

    "Не успели мы пожелать друг другу приятного аппетита, как к нам подошла какая-то пионерка с волосами василькового цвета."

    show un pioneer shy at fleft
    with long_dspr

    unp "Славя, привет. К вам можно?"

    show sl pioneer smile with dspr

    sl "Да, Лена, конечно! Садись."

    show un pioneer normal at left
    with good_dspr

    "Она села."
    sl "Знакомься, это Семён, наш новенький. Только сегодня приехал."
    me "Здравствуй."

    show un pioneer shy with dspr

    un "Привет…"
    th "А она немногословна. Или стесняется?"

    show un pioneer smile with dspr

    "..."
    "Мы приступили к трапезе."

    show cg d1_food_normal_sunset with dissolve

    "В этот раз хотелось есть сильнее, так что я накинулся сразу на всё."
    "И ужин не разочаровал."
    "Давали пюре с котлетой (правда её состав так и остался для меня загадкой) и горошком, а также стакан морса."
    th "А повара тут и правда умеют готовить, Славя не соврала."
    "..."
    "Я был настолько увлечён едой, что даже не сразу заметил, как Лена, что-то робко спрашивает у Слави."

    hide cg d1_food_normal_sunset with dissolve

    pause(0.5)

    un "... весь день?"
    
    show sl pioneer smile2 with dspr

    sl "Да я почти с самого утра Семёну помогала, потом на кухню."

    show sl pioneer smile with dspr

    sl "Повара просили помочь заготовить фарш по рецепту мамы, который я с собой привезла."
    sl "Ну а дальше в сад, немного цветами занялась."

    show un pioneer shy with dspr

    un "Да… Ты вообще отдыхаешь?"
    sl "Ты же знаешь, Лена, для меня отдых это смена деятельности."
    un "Да…"
    "Остаток ужина мы провели молча, лишь изредка я и Славя перекидывались парой фраз."
    "..."

    stop music fadeout 3.0
    stop ambience fadeout 1.0

    show bg ext_dining_hall_near_sunset
    show un pioneer normal
    show sl pioneer smile
    with dissolve2

    "Мы вышли из столовой."

    play ambience ambience_camp_center_evening fadein 1.0
    play music music_list["raindrops"] fadein 2.0 volume 0.7

    "На улице уже порядком посвежело, и я вдохнул приятный вечерний летний воздух."

    show sl pioneer smile2 at center
    with good_dspr

    sl "Слушай, Семён."
    me "Да?"
    sl "Ты сейчас что-нибудь собирался делать?"
    sl "Мы хотели с Леной пойти к ней в домик, она ещё несколько дней назад обещала продолжить учить меня рисовать."
    th "Она у меня что, разрешения спрашивает?"
    me "Ого, Лена, ты рисуешь?"

    show sl pioneer smile
    show un pioneer shy
    with dspr

    un "Ну, да-а… {w}Хотя у меня не очень получается, но всем, почему-то, нравится."
    me "Хм. Я не видел, но уверен, что рисуешь ты отлично."

    show un pioneer smile with dspr

    me "Во всяком случае, не смею задерживать, дамы. {w}Приятного вечера!"
    sl "Пока, Семён! М-м-м… {w}Уже, наверное, до завтра?"
    me "До завтра, Славя. Ещё обязательно увидимся!"
    th "Если меня опять куда-нибудь не забросит."
    un "Пока!"

    show sl pioneer smile at walk_away_left
    show un pioneer smile at walk_away_left
    pause(1.0)
    hide sl
    hide un
    with good_dspr

    "Девушки ушли, а я ещё некоторое время стоял, облокотившись на перилла крыльца столовой, и вкушал чистый воздух."

    stop music fadeout 1.0
    pause (1.0)
    play sound sfx_punch_medium volume 1.0
    pause(1.0)
    play music music_list["doomed_to_be_defeated"] volume 1.0

    th "Ч-что за!??"
    "Я начал оборачиваться, сжимая кулаки, и готовый принять свою смерть."
    "Но..."

    show dv pioneer laugh close at center
    with good_dspr

    "Передо мной стояла Алиса, заливающаяся смехом."

    stop music fadeout 1.0

    dv "А-ха-ха! Видел бы ты свою рожу, ха-ха-ха! Попался всё-таки!"
    "Я выдохнул, и разжав кулаки, тоже несколько раз хохотнул, но скорее нервно."
    me "Алиса, блин! До инфаркта доведешь!"

    show dv pioneer smile with dspr

    dv "Да, ладно-ладно, не кипятись, шутка же!"
    me "Ну и шутки у тебя…"
    "Я окончательно успокоился, и спросил."

    play music music_list["get_to_know_me_better"] fadein 2.0 volume 0.8

    me "Ты что-то хотела?"

    show dv pioneer normal with dspr

    dv "Да… {w}Но для начала отойдем в сторону."

    show dv pioneer normal at cleft
    with good_dspr

    "Мы отошли."

    show dv pioneer grin with dspr

    dv "Ты помнишь про свой долг?"
    th "Ёбана мать, что бы она ни задумала, мне это уже не нравится."
    me "Д-да."
    dv "Так вот..."

    show dv pioneer smile with dspr

    dv "Я знаю, что у тебя есть... {i}Сигареты{/i}."
    "Последнее слово она произнесла шёпотом."
    th "Что? Как?"
    "Этот же вопрос я задал ей."
    "Глупо было отнекиваться, она явно не блефовала, я это чувствовал."
    dv "А когда ты пришёл на пристань, и мы заговорили, я запах почувствовала."
    th "Ну конечно. А жвачку из дома я как раз и не взял."
    me "Кхм, ну… Да, есть. {w}Ты хочешь покурить?"
    "Прямо задал вопрос я. Алиса тоже не стала играть."

    show dv pioneer grin with dspr

    dv "Да. {w}Одна сигарета, и твой должок закрыт."
    me "Хорошо. Но при одном условии. {w}Ты дашь мне жвачку. Пару ломтиков."
    th "Не знаю, откуда я был уверен, что она у неё есть."
    th "Нно Алиса походила на бунтарку, которая лет, этак, десять назад, сошла бы за контингент, обитающий у подъезда, и сидящий на корточках."
    th "Ну, или на панкуху."

    show dv pioneer smile with dspr

    dv "Э, ты какой хитрый. {w}Это уже не отработка долга получается, а обмен."
    me "Но сигареты тебе все равно более достать негде. {w}Думай."
    dv "Ла-адно, посмотрим ещё как сигарета мне понравится. {w}Пошли за склад."
    "Я внутренне рассмеялся."
    "Давно уже было то время, когда мне приходилось прятаться ото всех, чтобы покурить."
    me "Ну пойдём… {w}Конспираторша."
    "..."

    stop ambience fadeout 1.0

    show bg ext_storage_sunset
    show dv pioneer normal
    with dissolve2

    "Мы пришли к складу, в котором я днем получал одежду, и зашли немного за угол."

    play ambience ambience_forest_evening fadein 1.0

    dv "Ну, не тяни кота за одно место! {w}Доставай!"
    me "Эка ты, какая нетерпеливая! Сейчас, подожди."
    "Я достал из кармана пачку сигарет, и зажигалку. Достал одну себе и одну Алисе."

    show dv pioneer surprise with dspr

    dv "Ого! Кэмэл? {w}Ты где их достал, это ж заграничные!"
    me "Секрет фирмы, о как!"
    "Я вставил сигарету в зубы."

    show dv pioneer smile with dspr

    me "Давай я тебе подкурю."

    call smoking_process(with_pause=0.5)

    "Мы раскурили сигареты, и молча стояли, пускали дым."
    "На удивление, Алиса не кашляла и даже не морщилась, как это обычно происходит у неопытных курильщиков."
    me "А ты, я смотрю, курильщица со стажем? {w}Вон как тянешь, и не кашляешь."

    queue sound sfx_smoking_cigaret

    show dv pioneer normal with dspr

    "Алиса выпустила дым после затяжки."
    dv "Ну, не то что бы прям со стажем."
    dv "Но после, Беломор Канала, знаешь, тут и кашлять не от чего."

    show dv pioneer smile with dspr

    dv "Отличные сигареты!"
    "Докурили мы в тишине."
    me "Ну что, долг отработан?"

    show dv pioneer guilty with good_dspr

    dv "Даже с лихвой, знаешь. {w}Мне теперь даже неудобно, как-то. {w}Такие дорогие сигареты у тебя вытянула."
    dv "А знаешь? {w}Забирай всю пачку жвачки, тут штук шесть ещё осталось. Сейчас, только одну возьму."

    show dv pioneer normal with half_good_dspr

    "Алиса ловким движением вынула одну серебрянку, раскрыла её и положила в рот."
    "Оставшееся она протянула мне."
    "Я принял жвачку, и пока доставал себе, сказал, смотря на Алису."

    play sound sfx_cigarette_pack_crumple volume 0.4

    me "Спасибо. {w}А кстати, тут возможно вообще сигареты-то достать?"
    me "Мои рано или поздно закончатся."

    show dv pioneer smile with dspr

    dv "Ну-у… {w}Пацаны у водителей заказывают, которые еду в столовую привозят из ближайшей деревни."
    dv "Сами мы туда не добежим, далековато. Иногда просят и более…"

    show dv pioneer grin with dspr
    pause(0.5)

    dv "Изысканные вещи, если ты понимаешь о чем я."
    "Я улыбнулся."
    me "Ага… Ну получается, как договоришься?"

    show dv pioneer smile with dspr

    dv "Получается так. {w}Ну что, пойдем обратно? Пока нас не потеряли."
    me "Почапали."

    stop ambience fadeout 1.0

    hide dv
    show dv pioneer normal at right
    with long_dspr

    show bg ext_dining_hall_away_sunset with dissolve2

    "На обратном пути я переваривал информацию, которую только что узнал."

    play ambience ambience_camp_center_evening fadein 1.0

    "Во-первых, в лагере появляются люди кроме тех, что уже здесь. Это хорошо."
    "Во-вторых, судя по словам Алисы, в относительной близости есть населённый пункт. Это тоже хорошо."

    show bg ext_square_sunset with dissolve

    "И в-третьих, разжиться запрещёнкой тут всё-таки можно."
    "Это тоже хорошо, в особенности, если не получится никак реализовать первые два пункта."

    show dv pioneer smile at cright
    with good_dspr

    dv "Мы на площади."
    "Алиса вывела меня из раздумий."
    dv "Так, ну мне налево. А тебе? {w}Где живешь?"
    me "Поверишь, нет? {w}С вожатой. {w}В домике Ольги Дмитриевны."
    "С некоторой долей непонятной гордости сказал я."

    show dv pioneer grin with good_dspr

    dv "М-м, вот оно как. Ну ты смотри, Оля наша горячая штучка."
    dv "А чтобы кому-то удавалось Изделие из резины №2 тут заполучить, я такого не слышала."
    dv "Хотя, может в медпункте есть?"
    "Я уставился на неё глазами по пять рублей."
    th "Или в этом времени правильно говорить «по пять копеек»?"
    me "Ну ты блин, {w}придумаешь тоже…"
    dv "А что? Она у нас молодая, красивая. {w}Ты тоже ничего."

    show dv pioneer smile with dspr

    "Алиса сверкнула глазками."
    me "Спасибо за комплимент, но мы знакомы же пару часов! {w}Ох молодёжь, ох нравы!"

    show dv pioneer laugh with dspr

    dv "Аха-ха, ладно тебе, моралист. Шутка юмора!"
    
    show dv pioneer smile with dspr

    dv "Ладно, бывай!"
    me "Пока!"

    show dv pioneer normal at walk_away_left
    pause(1.0)
    hide dv with dspr

    stop music fadeout 2.0

    "Я остался один на площади."
    "Судя по освещённости, время было ещё не позднее."
    "И опять вопрос, чем бы заняться?"

    play music music_list["two_glasses_of_melancholy"] fadein 2.0 volume 0.75

    th "А почему я вообще должен чем-то заняться? Я вполне заслужил отдых."
    th "Вот сейчас сяду на лавочку, и буду отдыхать."
    "Решительно направившись в сторону ближайшей, и сев на неё, я уставился на небо."
    "Ночь уже постепенно начала вступать в права, но всё ещё боролась с вечерним заревом."
    "Те редкие минуты, когда всё вокруг ещё неплохо освещено, но на небе уже проглядывают редкие звезды."
    th "Хорошо тут. Дышится легко, и энергии много. Я как будто помолодел лет на 8, хех."

    stop music fadeout 2.0

    mip "Ой, привет! А я тебя раньше не видела!"
    "Я опустил взгляд."

    show mi pioneer normal far with long_dspr

    th "Так. А это что ещё за импортный пионер?"

    play music music_list["so_good_to_be_careless"] fadein 2.0 volume 0.9

    "Передо мной стояла пионерка. Волосы её были лазурные, скорее даже, цвета морской волны."
    "И приятное на вид, с явными азиатскими чертами лицо."

    show mi pioneer smile with dspr

    mip "Привет, меня Мику зовут! Правда-правда, никто не верит, но меня правда так зовут! А всё, потому что у меня папа из Японии, а мама русская. Вот и получилась я. Но я вообще уже давно в Союзе живу, даже вот, пионером стала!"
    th "Ох ё, кроет как из пулемёта. Меня аж чуть со скамейки не перевернуло."

    show mi pioneer normal with dspr

    me "Привет! Семён, будем знакомы. Присаживайся, в ногах правды нет, как говорится."
    "Я немного подвинулся, уступая девушке место."
    mi "Ой, спасибо! Хотя ты знаешь, я уже собиралась идти дела заканчивать, и ко сну готовиться, но можно и посидеть, поболтать пару минут!"

    hide mi
    show mi pioneer normal close at right
    with good_dspr

    me "Ага… Так ты из Японии, говоришь?"

    show mi pioneer smile with dspr

    mi "Ну, вообще, мы оттуда уехали, когда я ещё маленькая была, почти ничего не помню, но папа у меня туда часто командируется!"
    mi "Он у меня мосты строит, он этот, инжир!"
    "Я прыснул."
    me "Извини, аха… Ха, извини. Ты, наверное, хотела сказать «инженер»?"

    show mi pioneer shy with good_dspr

    "Мику немного покраснела."

    mi "О-ха-ё, да, точно, ин-же-нер!"
    mi "Хи-хи, ничего страшного, я не обижаюсь!"

    show mi pioneer smile with good_dspr

    mi "Я в семье просто на двух языках разговариваю, с мамой на русском, а с папой на японском, ну, иногда наоборот, просто я оба языка знаю, чтобы не забыть, небольшая практика, вот."
    mi "А так как сначала я росла всё-таки в Японии, можно сказать, что родной у меня японский, а не русский, поэтому русские слова я иногда путаю."
    "Говорила она, конечно, очень быстро, но интересно."
    "Всегда любопытно пообщаться с человеком из другой страны."
    "Тем более в такой… {i}Необычной{/i}, по крайней мере, для меня, обстановке."
    "Да и голос у неё был приятный. Что-то он мне даже напоминал. Но вот что?"
    me "Ух ты, а это интересно. А можешь сказать что-нибудь на японском?"

    show mi pioneer normal with good_dspr

    mi_jp "{font=mods/simple_happiness_mod_efim/gui/fonts/NotoSansJP-Regular.ttf}私たちの音楽クラブへようこそ!{/font} (watashitachi no ongaku kurabu he yokoso!)."

    show mi pioneer smile with good_dspr

    me "Ох ё! {w}Ничего не понял, но звучит красиво! А что это значит?"

    show mi pioneer laugh with dspr

    mi "Хи-хи, а это ты завтра узнаешь!"

    show mi pioneer happy with dspr

    mi "Ты же новенький да? Я видела тебя со Славей, как вы шли от остановки, но не подошла, была занята."
    me "Да, я сегодня приехал. А почему завтра?"

    show mi pioneer smile with dspr

    mi "Вот завтра и узнаешь!"

    show mi pioneer normal far with long_dspr

    "Девушка вскочила, и поправив хвостики, продолжила."
    mi "Прости пожалуйста, но я побежала, очень срочно идти надо!"
    mi "Завтра увидимся, Семён!"
    me "Пока…"

    show mi pioneer normal far at walk_away_right
    pause(0.75)
    hide mi with dspr

    "Успел только я кинуть в след."

    stop music fadeout 2.0
    stop ambience fadeout 1.0

    th "Да, девочка ураган прямо. Только словесный."

    window hide

    call set_time("night")

    play ambience ambience_camp_center_night fadein 2.0 volume 0.9

    pause(1.0)

    show bg ext_square_night with dissolve

    pause(2.0)

    play music music_list["trapped_in_dreams"] fadein 2.0 volume 0.75

    th "Похоже, темнеет. Ну, значит и мне пора."
    "Я встал со скамейки, и направился к домику."
    "..."

    show bg ext_house_of_mt_night with dissolve3

    "Через несколько минут я уже был на пороге. Внутри горел свет."
    "Перед тем как заходить, я постучал."

    play sound sfx_knock_door7_polite volume 0.8

    "Через несколько секунд раздался голос."
    mt "Войдите!"

    show bg int_house_of_mt_night
    show mt nightdress normal at cright
    with dissolve

    stop ambience fadeout 1.0

    "Я зашел внутрь. Вожатая уже была переодета в ночнушку."

    play ambience ambience_camp_center_night fadein 1.0 volume 0.5

    mt "Семён, наконец-то пришёл. {w}Нагулялся? {w}Закрой дверь на щеколду."

    play sound sfx_lock_close volume 0.6

    "Я закрыл и ответил."
    me "Да. Так, походил немного, лагерь посмотрел. Здорово здесь."
    mt "Это верно. {w}Вот что, Семён."
    mt "Так как ты тут теперь живешь, вот."

    play sound sfx_keys_rattle volume 0.9

    "Она достала из кармана ключ и передала мне."

    show mt nightdress grin with dspr

    mt "Это второй ключ от нашего домика, первый у меня. Теперь ты полноправный жилец."
    "Она улыбнулась."
    me "Здорово, спасибо!"

    show mt nightdress normal with dspr

    mt "Не за что."
    mt "Так, ну всё, время позднее."
    mt "А завтра понедельник, у нас и у тебя много дел. Так что давай, стелись и спать."
    mt "Я пока выйду, подышу свежим воздухом."
    mt "Чтоб, когда я пришла, ты уже лежал в постели, всё понятно, пионер?"
    me "Я, да, это, есть, я, всё понял!"

    show mt nightdress grin with dspr

    "Она мило улыбнулась, довольная своим командирским нравом."
    mt "Вот и отлично!"

    show mt nightdress normal with dspr
    pause(0.5)
    show mt nightdress normal at walk_away_right
    pause(1.0)
    hide mt with dspr

    "Вожатая вышла из домика, а я приступил к вечернему ритуалу."
    "Хотя приступать было особо не к чему."
    "Я просто разделся до трусов, аккуратно сложил вещи на стул, нырнул в кровать, и устроившись поудобнее, положил руки под голову."
    "..."

    call to_nvl_mode

    "Так, пора подвести итоги сегодняшнего дня."
    "Меня не пытались избить, ограбить, изнасиловать или убить."
    "Место кажется дружелюбным… {w}И даже ничего не вызывает подозрения! Вот что я не мог понять всё это время!"
    "Казалось бы, ситуация наистраннейшая. Попал неизвестно куда, может вообще в другое время."
    "По всем канонам меня сейчас должны испытывать как лабораторную крыску, подсовывая всякие испытания, но нет… "
    "Всё вокруг, и люди, и окружение – было дружелюбным, и даже оно, дружелюбие, не было… {w}Наигранным что ли?"
    "Всё не просто казалось настоящим, оно таким и являлось, и это единственное, что вызывало подозрения, но оно же и успокаивало."

    call to_adv_mode

    "Решительно придя к тому, что я ни к чему не пришел, я решил оставить поиск ответов до завтра, а сейчас решил сосредоточиться на сне."
    "..."
    th "А вожатой всё нет. Куда это она, интересно, бегает, на ночь глядя, в одной ночнушке?"

    stop music fadeout 5.0

    th "Ох, не простая вы, Ольга Дмитриевна, ох не простая."
    "..."
    "Повертев ещё пару минут в голове всякое, я начал проваливаться в сон…"

    stop ambience fadeout 1.0

    show blink

    window hide

    $ renpy.pause(1.0, hard=True)

    jump simple_happiness_mod_day2


# День 2
label simple_happiness_mod_day2:
    $ backdrop = "days"
    $ new_chapter(2, u"Простое Счастье. День 2")

    call set_time
    call to_adv_mode

    play ambience ambience_int_cabin_day fadein 1.0
    play music music_list["everyday_theme"] fadein 3.0 volume 0.5

    "Несмотря на пережитый стресс, спал я хорошо."
    "Не понятно, сказывалась накопившаяся усталость, или в этом месте просто так хорошо спится, но проснулся я полный сил."
    "Однако по природе своей не упустил возможности ещё немного полежать с закрытыми глазами, нежно потягиваясь в кровати."
    th "Интересно, вожатая меня разбудит? И сколько вообще время?"
    "Вот как оказывается некомфортно себя ощущаешь, лишившись благ современной цивилизации."
    "Такая простая вещь, как возможность постоянно знать о текущем времени, но лишившись её, сразу чувствуешь себя некомфортно."
    mt "Семён, подъём!"
    "Вожатая не заставила себя долго ждать."

    hide blink
    show unblink
    show bg int_house_of_mt_day
    with dissolve1

    show mt pioneer normal panama far at fright
    with dspr

    "Я открыл глаза, и сел на кровати, потянувшись и зевнув."
    me "Доброе утро, Ольга Дмитриевна."
    "Она уже стояла в форме и панамке."
    mt "Доброе, Семён. Давай, одевайся, и иди в столовую. Завтрак через 20 минут. А я на обход."
    mt "И домик не забудь закрыть!"
    me "Хорошо. Будет сделано, т-рищ начальник!"

    show mt pioneer laugh panama far with dspr

    "Она улыбнулась."
    me "А вот за «т-рища» могу и треснуть."

    show mt pioneer smile panama far with dspr
    pause(0.5)
    show mt pioneer smile panama far at walk_away_right
    pause(0.5)
    hide mt with dspr

    "Я лишь только тоже улыбнулся в ответ, и вожатая вышла из домика."
    "..."
    "Одевшись, и кое-как заправив постель, я огляделся, и только сейчас заметил зеркало, висящее на дверце шкафа."
    th "Интересно, как я выгляжу в пионерской форме?"
    th "Наверное, просто верх идиотизма."
    "Я подошел к зеркалу, и…"

    stop music fadeout 1.0
    pause(0.5)

    play music music_list["doomed_to_be_defeated"] fadein 0.5 volume 1.0

    show cg d2_mirror with dissolve

    th "Твою мать!"
    "От неожиданности я чуть не отпрянул, но всё-таки схватился за дверцу, и уставился в отражение."
    "В отражении был не я!"
    "Где месячная небритость, мешки под глазами, и вечное выражение лица, которое ясно даёт понять всему миру, что у меня нет желания ни с кем общаться?"
    "В отражении стоял молодой парень лет 16–18 в хорошем телосложении... {w}Погоди-ка."
    "Я присмотрелся."
    th "Господи… Да этож я!"
    "Ну точно, это был я! {w}Только образца конца школы – начала института."
    "Не зря я чувствовал в себе перемены."
    "И вот почему никто не обращал внимания на мой возраст. {w}Потому что я с ними одного возраста!"

    stop music fadeout 2.5

    "Поразглядывав себя ещё секунд 30, я отошел от зеркала."

    hide cg with dissolve

    th "Чертовщина какая-то."
    "В перемещение в пространстве и времени я ещё мог поверить, но пересадить мой разум в другое тело?"
    "Нет, это было выше моего понимания."

    play music music_list["confession_oboe"] fadein 2.0 volume 0.9

    "С другой стороны, так даже лучше. Будет меньше проблем, чем если бы я выглядел на свои 25."
    "..."
    th "Ладно, пора в столовую."

    stop ambience fadeout 1.0

    show bg ext_house_of_mt_day with dissolve

    play ambience ambience_camp_center_day fadein 1.0
    play sound sfx_dinner_horn_processed

    "Выйдя из домика, я закрыл его, и тут прозвучал горн."
    th "Черт, надо поторапливаться."
    "Я быстрым шагом направился в столовую, никого не встретив по дороге."

    show bg ext_dining_hall_near_day with dissolve1

    "У входа, как обычно, толпились пионеры, заходя в помещение, но никого из знакомых я не увидел, так что, просто зашел внутрь."

    stop ambience fadeout 1.0

    show bg int_dining_hall_people_day
    show mt pioneer normal at fright
    with dissolve

    play ambience ambience_dining_hall_full fadein 1.0

    "На входе уже стояла Ольга Дмитриевна, и отмечала пионеров."
    "Я кивнул ей."
    "Она чиркнула в тетради, и села за столик, который стоял чуть поодаль от остальных."

    show mt pioneer normal at walk_away_right
    pause(1.0)
    hide mt with dspr

    "Видимо, я пришел последний из отряда."
    "..."
    "Взяв свою порцию, я начал искать глазами, куда бы сесть, как увидел, что примерно с середины зала мне машет Славя."
    "Я поспешно направился к ней и сел за единственное свободное место рядом со Славей."

    show sl pioneer normal at cright
    with dspr

    "Пожелав всем приятного аппетита, я оглядел пионеров."
    "Никто из них не был мне знаком, так что я заговорил со Славей."

    me "Утро доброе, ну что, как вчера порисовали?"
    sl "Доброе, Семён."

    show sl pioneer smile with dspr

    sl "Отлично! {w}Я тебе обязательно как-нибудь покажу, и рисунки Лены тоже."
    me "Было бы здорово посмотреть. {w}Я вот, знаешь, никогда не умел рисовать."
    "Мы продолжили разговаривать и есть одновременно."
    "..."

    stop ambience fadeout 1.0

    show bg ext_dining_hall_near_day
    show sl pioneer normal at right
    with dissolve

    play ambience ambience_camp_center_day fadein 1.0 volume 0.8

    "Закончив приём пищи, мы вышли на крыльцо, и я спросил."
    me "Ну что, есть у нас сегодня какие-нибудь планы?"
    "Не знаю от чего, но жутко хотелось себя чем-нибудь занять."
    sl "Ну-у, не знаю ещё, но сейчас нам точно нужно идти на линейку."
    th "Ох-ё… Я и забыл, что в подобных местах есть линейки."
    me "На площади, да?"

    show sl pioneer smile with dspr

    "Предположил я."
    sl "Ага."
    me "Ну, тогда пойдем."

    stop music fadeout 2.0

    show bg ext_square_day with dissolve1

    "Мы вышли на площадь."

    play music music_list["sweet_darkness"] fadein 2.0 fadein 0.9

    "По всему периметру рядами стояли отряды пионеров перед своими вожатыми."
    "Кто-то уже был построен, кто-то ещё подходил."
    "Вместе со Славей мы подошли к своему отряду."

    show sl pioneer smile at walk_away_right
    pause(1.5)
    hide sl with dspr

    "Славя заняла свое место, а я, решив, что здесь действует простой школьный принцип «по росту», встал ближе к началу, рядом с Алисой."
    "Я огляделся вокруг."
    "Помимо нас, на площади стояло ещё несколько отрядов. Кто-то был нашего возраста, другие помладше."
    "Если учесть, что все пионеры живут по двое, неужели на меня не хватило места? Учитывая количество домиков."

    show mt pioneer smile panama far at cleft
    with dspr

    "Из размышлений меня вывела подошедшая вожатая."
    mt "Всем здравствуйте, ребята!"
    pis "Здравствуйте."
    "Ответили пионеры в разнобой."
    mt "Итак, начнём линейку!"

    hide mt
    show cg d2_lineup
    with dissolve

    mt "Начинается наша последняя неделя в лагере!"
    mt "Я надеюсь, за эти семь дней вы сможете ещё больше подружиться, и сделать много…"
    "Дальше я не слушал."
    "Никогда не выносил все эти формальные сообщения от начальства к подчинённым, особенно в высоких речах."
    th "Интересно, это так уж прям обязательно, или ей самой в кайф?"
    mt "... Семён..."
    "Услышал свое имя, я встрепенулся, навострил слух и посмотрел на вожатую."
    mt "… нашем отряде."
    mt "С кем-то из вас он уже познакомился, с кем-то ещё познакомится, но я надеюсь, что вы будете добры по отношению к нему!"
    mt "На этом всё, линейка окончена. {w}На сегодня особых указаний не было, так что, по кружкам. {w}Вольно!"

    hide cg
    with dissolve

    "Пионеры начали говорить, и расходиться."

    show mt pioneer normal panama at right
    with good_dspr

    "Я, не зная, что мне делать, тоже вышел из строя, но тут ко мне подошла вожатая."
    mt "А для тебя, Семён, у меня на сегодня особое поручение."
    me "Для меня? И какое же?"

    show sl pioneer normal at left
    with good_dspr

    "Подошла Славя."
    "Вожатая достала из кармана юбки сложенный вчетверо листок, и передала мне."

    play sound sfx_paper_bag

    show obhod none at center
    with dspr

    "Я развернул его, и увидел небольшую распечатанную таблицу, с указаниями места, подписи руководителя и пометкой «вступил» у каждого поля."

    "Я повертел его пару секунд."
    me "Обходной лист?"

    show mt pioneer smile panama with dspr

    mt "Да. Бегунок."
    mt "Сегодня, желательно до обеда, тебе нужно посетить все эти места, сделать отметки, и обязательно, Семён. {w}{b}{u}Обязательно{/b}{/u}. Куда-нибудь вступить."

    hide obhod with dspr

    "Я поднял взгляд и посмотрел на вожатую, и на Славю."

    me "Ё-ё… Ольга Дмитриевна, я же тут первый день! Лагерь толком не знаю, я ж до вечера плутать буду!"

    show mt pioneer normal panama
    show sl pioneer smile
    with half_good_dspr

    "Славя, до этого стоявшая молча, сказала."
    sl "Ольга Дмитриевна, давайте я помогу! Побуду сегодня гидом немножко."
    mt "Хм. Ну-у, Хорошо, Славя."

    show mt pioneer surprise panama with dspr

    mt "А остальные дела ты успеешь сделать?"

    show sl pioneer smile2 with dspr

    sl "А вы мне пока ничего не говорили."
    "Она улыбнулась."

    show mt pioneer smile panama with dspr

    mt "И правда что."

    show mt pioneer grin panama
    show sl pioneer shy
    with half_good_dspr

    mt "Потому-что ты образцовая пионерка, Славя! Всё всегда успеваешь!"
    "Славя немного покраснела."

    show mt pioneer smile panama with dspr

    mt "Хорошо, тогда покажи Семёну лагерь."

    show sl pioneer smile2 with dspr

    mt "Тогда до обеда точно управитесь."
    mt "Ну, время не ждет, вперёд, пионеры!"

    show mt pioneer normal panama at walk_away_right
    pause(0.5)
    hide mt with long_dspr

    "После этих слов вожатая ушла."
    "Мы остались со Славей вдвоем."

    show sl pioneer normal
    show obhod none
    with good_dspr

    "Я ещё раз посмотрел на бегунок, и начал произносить вслух."
    me "Так, посмотрим. {w}Клуб кибернетики, музыкальный клуб, медпункт, библиотека."
    me "С чего начнём?"

    show sl pioneer smile
    hide obhod
    with dspr

    sl "Ну, я предлагаю по порядку."
    sl "Как раз позиции расположены в порядке от ворот лагеря, до самого конца. Так будет проще."
    me "Мне нравится, пошли!"
    "Мы двинули от площади в сторону общих кружков."

    stop music fadeout 2.0

    "..."

    show black with clocks_in

    hide sl
    show bg ext_clubs_day
    show sl pioneer normal at right
    hide black
    with clocks_out

    play music music_list["tried_to_bring_it_back"] fadein 2.0 volume 0.75

    "Мы стояли перед зданием клубов."
    sl "Кстати, Семён, ещё не решил, куда будешь записываться?"
    me "Откровенно говоря, привлекает только музыкальный клуб. Я немного играю на гитаре…"

    show sl pioneer smile with dspr

    th "Не то чтобы я слукавил, но мои навыки было сложно назвать даже базовыми."
    sl "Будет здорово, если ты туда запишешься, а то Мику там целыми днями одна сидит, скучает."
    me "Да, то-то она охотна поговорить с каждым встречным."

    show sl pioneer surprise with good_dspr

    "Я поймал непонимающий взгляд Слави."
    me "Уже имел честь с ней познакомиться вчера вечером."

    show sl pioneer smile with dspr

    sl "А-а, аха-ха, понятно! {w}Ну да, она любит поболтать. Но девушка она хорошая."
    "Я кивнул, согласившись."
    sl "Ну что, зайдем в клуб кибернетики, поставим роспись?"
    me "Да, а то уж несколько минут перед входом стоим, хах."

    stop ambience fadeout 1.0

    hide sl
    show bg int_clubs_male_day
    show sl pioneer normal at fright
    with dissolve

    play ambience ambience_clubs_inside_day fadein 1.0 volume 0.95

    "Мы зашли в помещение, и оказались в месте, которое принято называть «мужыцкой» берлогой."
    "Повсюду валялись всякие провода, микросхемы, паяльники, лампочки, и Бог знает, что ещё."
    "Честно говоря, название «Клуб Кибернетики» звучало интригующе, но вряд ли меня заинтересовала бы техника времён СССР."
    "Да и вообще, если уж на то пошло, я бы позанимался чем-нибудь по части кода, а не пайки."
    me "Тук-тук! Есть кто дома?"
    shp "Да-да, секунду!"

    play sound sfx_blanket_off_stand volume 0.7
    queue sound sfx_blanket_off_stand volume 0.5

    "Из дальнего помещения послышался какой-то шорох, и через несколько секунд оттуда вышло два пионера, которые несли в руках какую-то большую коробку."

    show el pioneer normal at fleft
    show sh pioneer normal at cleft
    with long_dspr

    queue sound "<from 0 to 1.25>" + sfx_fall_wood_floor

    "С грохотом поставив её на пол, они вытерли пот, и тот, что был в очках, представился первый."
    shp "Приветствую, я Саша. Глава клуба кибернетики. {w}А ты, Семён, кажется? Виделись на линейке."
    me "Да, мы стояли рядом."
    elp "Точно, видел тебя! Меня Сергей звать, будем знакомы."
    elp "Но все зовут Электроником, говорят я на героя из фильма похож."
    th "И правда, прямо вылитый «Да где же у него кнопка?»"
    "Я поздоровался и с ним, после чего глава клуба продолжил."
    sh "Так ты чего здесь? Кстати, привет, Славя."

    show sl pioneer smile with dspr

    sl "Привет, мальчики."

    show sl pioneer normal with dspr

    me "Мне нужно обходной подписать… Вот. {w}Ольга Дмитриевна отправила."
    el "Конечно подпишем! После того, как к нам в клуб вступишь!"

    stop music fadeout 1.0

    show el pioneer grin
    show sh pioneer normal_smile
    with dissolve

    play music music_list["heather"] fadein 1.0

    "Вот чёрт, кажется, эти двое настроены решительно…"
    "Но вступать в их «gachi club boy next door» совершенно не хотелось."
    "Мне кажется, они тут и без меня нормально справляются."

    sh "Конечно, нам всегда нужны молодые, сильные, мужские руки вроде твоих!"
    sh "Тебе найдется чем заняться, вот увидишь!"

    stop music fadeout 1.0

    th "Твою-мать…"

    play music music_list["awakening_power"] fadein 0.5

    show sl pioneer serious with dspr

    sl "Одну минуточку!"
    "Славя, стоящая до этого в стороне, одернула назад волосы, и вышла передо мной."

    hide sl
    show sl pioneer angry at center
    with good_dspr

    sl "Мне кажется, вам нужно повторить? {w}Семён пришел сюда, чтобы подписать обходной лист, а не выслушивать рекламу вашего клуба!"

    show sh pioneer upset
    show el pioneer upset
    with dspr

    "Парни явно напряглись."
    sh "Н-ну, да, но мы просто хотели…"
    sl "Уже ничего не хотели!"

    play sound sfx_paper_bag
    queue sound sfx_punch_medium

    "Славя взяла листок у меня из рук, и положила его на стол перед Шуриком."
    sl "Подписывай!"

    show sh pioneer scared
    show el pioneer scared
    with dspr

    "Шурик, с видом ошарашенной лошади достал трясущейся рукой из нагрудного кармана рубашки ручку, и поставил свою закорючку."
    sl "Отлично. Мы закончили. {w}Впредь будьте вежливее, если не хотите иметь дело с вожатой!"
    sl "Семён, пойдем отсюда!"

    play sound sfx_paper_bag

    "Славя схватила листок со стола, и направилась к выходу."

    hide sl
    show sl pioneer serious at right
    with dspr

    pause(0.5)

    show sl pioneer serious at walk_away_right

    pause(0.5)
    
    hide sl with long_dspr

    "Мне ничего не оставалось, кроме как бросить взгляд на парней, и двинуться за ней."

    stop ambience fadeout 1.0
    stop music fadeout 2.0

    hide el
    hide sh
    show bg ext_clubs_day
    show sl pioneer normal at cright
    with dissolve1

    play ambience ambience_camp_center_day fadein 1.0

    pause(1.0)

    play sound sfx_paper_bag volume 0.8

    "Мы вышли на улицу, и Славя передала мне листок."

    show sl pioneer smile with dspr

    "Я заметил, что её сейчас как будто разорвёт от желания засмеяться."
    me "Славь, ты чего?"

    play music music_list["gentle_predator"] fadein 2.0

    show sl pioneer smile2 with dspr

    "И тут она не выдержала."

    show sl pioneer laugh with dspr

    sl "Ха-ха-ха-ха, Семён, ты видел их лица?"
    sl "Ой, ха-ха-ха, я сейчас упаду."
    sl "Они аж побледнели от страха!"
    "Я сначала несколько раз прыснул, но потом тоже не выдержал, и начал смеяться вместе со Славей."
    "Через несколько секунд внезапный приступ прошёл, и отдышавшись, и утерев слезу, я сказал."
    
    show sl pioneer smile2 with good_dspr

    me "Славя, а ты умеешь командовать! Мне аж самому не по себе стало."
    sl "Ну, служба помощницей вожатой даёт свои плоды. {w}Иногда приходится с младшими отрядами сидеть."

    show sl pioneer smile
    show obhod one
    with dspr

    "Я вгзлянул на обходной."
    me "Хах, понятно... Пойдем дальше? Следующий в списке как раз музыкальный клуб, сразу и запишусь."
    sl "Отлично, тогда идем!"

    stop music fadeout 2.0

    hide obhod
    hide sl
    show bg ext_houses_day
    show sl pioneer smile at right
    with dissolve

    "Давно я так хорошо не смеялся, и себя не чувствовал тоже."
    "С этой девушкой не пропадёшь, однозначно."

    play music music_list["my_daily_life"] fadein 2.0 volume 0.9

    "Мы шли по лагерю, в приподнятом настроении, весело болтали, и иногда перешучивались, хихикая."
    "Я чувствовал почти осязаемое тепло от Слави."
    "От её неимоверно мощной энергетики доброты, уносящей с собой."
    "Энергетики, которая заряжает помогать, быть рядом, но и уметь принять помощь."

    hide sl
    show bg ext_musclub_day
    show sl pioneer smile at center
    with dissolve

    "Мы стали подходить к музыкальному клубу."
    "Довольно милое здание, стоящее в самом конце тропинки, и прикрытое тенью деревьев."
    "Особенно выделялись, большие, почти во всю высоту, необычной формы, окна."

    hide sl
    show sl pioneer normal far at center
    show bg ext_musclub_verandah_day
    with dissolve

    sl "Ну что, давай зайдём?"

    play sound sfx_knock_door7_polite

    "Славя постучала, но ответа не последовало."

    show sl pioneer surprise with good_dspr

    sl "Странно. Может, отошла?"

    show sl pioneer normal with good_dspr

    sl "Ладно, давай зайдём."

    stop ambience fadeout 1.0

    hide sl
    show bg int_musclub_mattresses_day
    show sl pioneer normal at cleft
    with dissolve

    play ambience ambience_music_club_day fadein 1.0

    "Мы вошли внутрь, и оказались в очень уютном, залитом светом помещении."
    "У дальней стены располагалось большое количество разных инструментов, на доске там же были расписаны ноты, а левее виднелся проход, наверное, в подсобные помещения."
    "А рядом с остеклённой стеной справа стояли сложенные друг на друга матрасы почти во всю стену."

    show sl pioneer smile with dspr

    sl "Я пойду проверю, может Мику в подсобке."
    sl "А ты пока подожди здесь, вдруг она вернется."
    me "Хорошо."

    show sl pioneer smile at walk_away_left
    pause(0.5)
    hide sl with dspr

    "Ответил я, и начал прогуливаться вдоль окна, и мой взгляд упал на рояль."
    th "Или это пианино? Не разбираюсь в них."

    stop music fadeout 1.0

    "А это! {w}{s}Что{/s} Кто это!?"

    play music "<from 18>" + music_list["take_me_beautifully"] fadein 2.0

    show cg d2_miku_piano2 with dissolve

    "Под пианино-роялем, в довольно горячей позе находилась Мику, и что-то увлечённо искала."
    th "Хм... {w}В полосочку."
    th "Бр-р!"
    "Не время пошлить!"
    me "Мику! {w}Ты что, нас не слышала? {w}Что ты там делаешь?"
    "Несмотря на то, что юбка японки {u}очень{/u} сильно задралась, я не мог отвести взгляд."
    "Хотя, как раз поэтому и не мог."

    hide cg
    show cg d2_miku_piano
    with dissolve

    mi "Что-о?"
    "Она обернулась."
    mi "Сейчас-сейчас, вылезу!"

    stop music fadeout 2.0

    hide cg
    show bg int_musclub_mattresses_day
    with dissolve1

    pause(0.5)

    show sl pioneer laugh at left
    with good_dspr

    sl "Аха-ха, Мику? Ты что там делала, под роялем?"

    show mi pioneer grin at right
    with half_good_dspr

    play music music_list["so_good_to_be_careless"] fadein 2.0 volume 0.83

    "Выбравшись, наконец, из-под рояля, девочка оправилась, и защебетала."
    mi "Ой, Славечка, и ты здесь! Приветики!"

    show sl pioneer smile with dspr

    "Славя успела лишь кивнуть."

    show mi pioneer happy with dspr

    mi "А я, тут, понимаете, доску хотела вытереть, чтобы новые ноты написать, а губка под рояль упала, ну я и залезла её поднять, а тут вы пришли!"

    show mi pioneer cry_smile with dspr

    mi "А вы чего, в гости, или по делу? Я вообще, ожидала что Семён придет, он же новенький, наверняка ты с обходным, да, Семён?"
    "Я тоже кивнул."

    show mi pioneer grin with dspr

    mi "Но тебя, Славя, не ожидала увидеть! Не то что я тебе не рада, ты не подумай, просто я думала ты занята, ты обычно редко заходишь."
    me "И-именно по этому поводу мы и пришли, Мику!"
    "Успел остановить я девочку-пулемёт."
    me "Мы вместе, как раз потому что я новенький, а Славя мне помогает не заблудиться."
    me "И я хочу, чтобы в обходном листе ты сразу поставила отметку о вступлении."

    show mi pioneer shocked with dspr
    pause(0.5)
    show mi pioneer surprise with dspr
    pause(0.5)
    show mi pioneer cry_smile with dspr

    "Во мгновение ока её глаза наполнились таким количеством радости, что кажется, сейчас сама ткань пространства-времени не выдержит, и разорвется, образуя сингулярность."
    mi "Что, правда? Ой, надо же, как здорово! Теперь нас будет уже двое в клубе! Давай обходной!"

    play sound sfx_paper_bag

    hide mi
    show mi pioneer normal far at cright
    with half_good_dspr

    "Я протянул ей листок, она взяла его, отнесла к подоконнику и поставила роспись."

    hide mi
    show mi pioneer normal at right
    with half_good_dspr

    "Вернувшись, она протянула мне листок."

    show mi pioneer grin
    show obhod two
    with half_good_dspr

    "Я посмотрел на лист, и увидел очень красивую и аккуратную роспись, в которой кажется, угадывались не то ноты, не то иероглифы."
    "Особенно на фоне закорючки Электрона."

    hide obhod with good_dspr

    "Сложив обходной, я посмотрел обратно на Мику."
    "Она обратилась ко мне."

    show mi pioneer happy with dspr

    mi "И когда ты ко мне, Семён?"
    me "Даже не знаю…"
    sl "После обеда, скорее всего."
    sl "До обеда мы обойдем оставшиеся места, и так уж и быть, отдам его под твою ответственность!"

    show mi pioneer shocked with dspr
    pause(0.5)
    show mi pioneer surprise with dspr

    "Мику интересно посмотрела на Славю."
    mi "О-о-о, понятно! Ну хорошо, Сёма, тогда жду тебя после обеда. Не опаздывай!"
    me "Постараюсь. До скор… {w}Хотя подожди!"

    show mi pioneer shocked
    show sl pioneer surprise
    with good_dspr

    "Мику и Слая вопросительно посмотрели на меня."
    me "Ты вчера вечером сказала что-то на японском, и сказала что перевод я узнаю, когда вступлю в клуб!"
    "Я почувствовал небольшую гордость за свою память."

    show sl pioneer smile
    show mi pioneer smile
    with good_dspr

    mi "А-а-а, точно-точно, было дело."
    mi "Совсем вылетело из головы."
    me "Напомни, как эта фраза звучит в оригинале?"
    mi_jp "{font=mods/simple_happiness_mod_efim/gui/fonts/NotoSansJP-Regular.ttf}私たちの音楽クラブへようこそ!{/font} (watashitachi no ongaku kurabu he yokoso!)."

    show sl pioneer happy with half_good_dspr

    sl "Ого! Мику, я никогда не слышала, как ты говоришь по-японски!"

    show mi pioneer grin with dspr

    "Мику улыбнулась."

    show sl pioneer smile with dspr

    me "Ну что, как это переводится?"

    show mi pioneer happy with dspr

    mi "«Добро пожаловать в наш музыкальный клуб!»"
    me "О-о! Просто, и со смыслом. Но неужели ты сразу думала, что я вступлю?"
    mi "Не знаю, Семён. Я… {w}Чувствовала. И не продала!"

    show sl pioneer laugh
    show mi pioneer shy
    with dspr

    sl "Аха-ха, Мику! «Не прогадала» правильно."

    show sl pioneer smile2
    show mi pioneer happy
    with dspr

    mi "Не… {w}Не про-га-да-ла!"
    me "Ну что-же, теперь я точно не отверчусь. До встречи после обеда!"

    show sl pioneer smile
    show mi pioneer grin
    with dspr

    mi "Пока, ребята!"
    "Славя тоже попрощалась, и мы вышли из клуба."

    stop ambience fadeout 1.0
    stop music fadeout 3.0

    hide mi
    hide sl
    show bg ext_musclub_verandah_day
    show sl pioneer smile at right
    with dissolve1

    play ambience ambience_camp_center_day fadein 1.0

    $ renpy.pause(2.5, hard=True)

    show bg ext_musclub_day with dissolve

    "Сделав пару шагов от клуба, Славя заговорила."

    play music "<from 12.0>" + music_list["farewell_to_the_past_edit"] fadein 2.0 volume 0.8

    show sl pioneer normal with dspr

    sl "На самом деле я сама очень рада, что ты вступил в музыкальный клуб."
    sl "Раз ты умеешь играть, тебе будет там чем заняться. {w}И Мику не будет так одиноко."

    show sl pioneer sad with dspr

    sl "А то она и правда там целыми днями одна сидит, мне её жалко."
    sl "А самой навестить некогда, да и в музыке я не разбираюсь."
    me "А что, больше во всём лагере никто не играет?"
    sl "Знаю только что Алиса вроде как на электрогитаре играет, но она не в клубе. {w}Вроде заходит иногда, но чисто по собственной необходимости."
    sl "Наверное тоже не со зла она так с Мику поступает, просто характер у неё такой, одиночный. {w}Только с Ульянкой более-менее общается."

    show sl pioneer normal with dspr

    sl "В общем, ты Мику не обижай, ладно?"

    hide sl
    show bg ext_houses_day
    show sl pioneer normal
    with dissolve

    stop music fadeout 3.0

    me "Ну ты что, как я могу!"
    "За разговором мы уже довольно далеко отошли от клуба."

    play sound sfx_paper_bag

    show sl pioneer smile
    show obhod two at center
    with dspr

    play music music_list["everyday_theme"] fadein 2.0 volume 0.85

    "Я развернул листок, и проведя пальцем, сказал."
    me "Ага, следующий пункт назначения – медпункт. {w}Э, а это что, тоже клуб?"

    hide obhod
    show sl pioneer laugh
    with good_dspr

    "Славя рассмеялась."
    sl "Нет конечно. Просто тебе нужно поставить отметку, что лагерь тебя принял живым и здоровым."

    show sl pioneer smile with dspr

    me "А-а-а, вона как. Понятно. Ну, тогда идём."
    "Мы неторопливо продолжили путь до медпункта, болтая обо всяком."
    "..."

    hide sl
    show bg ext_aidpost_day
    show sl pioneer smile at right
    with dissolve1

    "Мы подошли к зданию медпункта."
    "Ухоженное на вид строение, на крыше которого развивался красный крест на белом фоне."
    th "Надеюсь, тут хотя бы обойдётся без инцидентов…"

    hide sl
    show bg int_aidpost_day_apple
    show sl pioneer normal at fright
    with dissolve1

    stop ambience fadeout 1.0

    "Мы вошли внутрь, и оказались в очень светлом и чистом помещении."

    play ambience ambience_medstation_inside_day fadein 1.0

    "Каждый уголок буквально сверкал."
    "А ещё тут сидела… Э-э, Лена?"

    show un pioneer normal far at center
    with dspr

    "Я присмотрела и понял. Ну точно. {w}Сидит на месте медсестры, и листает ни то журнал, ни то книжку, а на столе лежит яблоко."

    show sl pioneer smile with dspr

    sl "Лена? Привет, ты что тут, опять медсестру подменяешь?"

    show un pioneer surprise with good_dspr

    un "Ой!"
    "Кажется, мы опять напугали местного обитателя своим появлением, да так, что Лена аж подпрыгнула на стуле, и обернулась."

    show un pioneer shy with good_dspr

    un "Ой, ребята… Привет."
    "Она немного расслабилась. В это время мы подошли ближе."

    hide un
    show un pioneer smile at left
    with long_dspr

    un "Да. Виолетта отошла ненадолго, так что я пока за неё."
    th "Вот так тут медики работают?"

    stop music fadeout 2.0

    me "Ну мне надо обходной лист подписать, так что в любом случае наверное придется ждать… Виолетту."
    cs "Уже не придётся."

    play music music_list["eternal_longing"] fadein 1.0 volume 0.8

    hide sl
    hide un
    show sl pioneer normal at fright
    show un pioneer normal at fleft
    show cs normal at center
    with good_dspr

    "Мы все обернулись."
    "На пороге стояла привлекательная женщина лет тридцати в медицинском халате."
    th "И как мы в шесть ушей не услышали, что она вошла?"
    "Виолетта обратилась к Лене."

    show cs smile
    show un pioneer shy
    with dspr

    cs "Леночка, спасибо за помощь, можешь быть свободна."
    un "Хорошо. Ещё увидимся ребята."

    show un pioneer shy at walk_away_left
    pause(0.5)
    hide un with dspr

    "Бросила она, после чего, поспешно удалилась."
    
    show cs normal with dspr

    cs "И так, кто из вас двоих мой пациент?"
    me "Ну-у, мне бы обходной."

    play sound sfx_paper_bag

    "Я достал листок из кармана, и протянул ей."
    me "Вот."

    show cs smile with dspr

    cs "Очень хорошо."

    play sound sfx_paper_bag

    "Она взяла лист, и отложила его на стол."
    cs "Садись."
    "Сказала она, и указала пальцем на кушетку."
    "Я сел."

    hide sl
    hide cs
    show sl pioneer smile far at fright
    show cs normal stethoscope at center
    with good_dspr

    "В это время она взяла стетоскоп, и вернулась ко мне."

    show cs shy stethoscope with dspr
    cs "Чего сидишь? Раздевайся. {w}Пионер…"
    me "Раздеваться, зачем?"
    "Кажется, своей неимоверной аурой самоуверенности и таким же самоуверенным декольте она начала вгонять меня в краску."
    cs "Как зачем… Слушать тебя будем, здоровье проверять… {w}Мужское."

    show sl pioneer shy with dspr

    "Теперь покраснела и Славя, стоящая позади."
    "Виолетта тем временем наклонилась ко мне, и продолжила."

    show cg d5_cs with dissolve

    cs "Ты же не хочешь, чтобы у тебя и у меня были проблемы… {w}Пионер?"
    "Я невольно подвинулся чуть назад."
    me "Я… Я, я абсолютно здоров! {w}Честное пионерское!"
    th "По крайней мере в мужском плане точно. Кажется, она это заметила."
    cs "Ну ладно… Верю."

    hide cg
    show cs smile stethoscope
    with dissolve

    "Она отпрянула от меня, и села за стол."
    cs "Подожди пару минут, я тебе сразу карту заведу."
    me "Хорошо."
    "Это время нужно было нам всем. Что я, что Славя были красные, как помидоры."
    "..."

    stop music fadeout 2.0

    pause(1.5)
    show sl pioneer normal at fright
    with long_dspr
    pause(0.5)

    "Спустя одну подписанную тетрадь и роспись в бегунке, Виола сказала."
    cs "Всё готово, можешь забирать свой обходной."

    play sound sfx_paper_bag

    "Я встал, и поспешил взять у неё лист, сложил его, и убрал его в карман."
    cs "Если что вдруг… Сразу ко мне... {w}Пионер."
    "Я сглотнул."

    show cs normal stethoscope
    show sl pioneer smile
    with dspr

    sl "До свидания, Виолетта Церновна."
    cs "До свидания."
    "Мы вышли из медпункта."

    stop ambience fadeout 1.0

    hide sl
    hide cs
    show bg ext_aidpost_day
    show sl pioneer normal at right
    with dissolve

    play ambience ambience_camp_center_day fadein 1.0
    play music music_list["dance_of_fireflies"] fadein 2.0 volume 0.8

    me "Медсестра очень…"

    show sl pioneer smile with dspr

    sl "«Эксцентричная»?"
    me "Ха-ха, да."

    show sl pioneer surprise with half_good_dspr

    sl "Это точно. Иногда она ведёт себя очень странно."
    me "Надеюсь, более мне не придется у неё оказаться."

    show sl pioneer smile
    show obhod three
    with dspr

    "Я посмотрел на бегунок."
    me "Ну что, последний пункт – библиотека. Пошли?"
    sl "Да, тут как раз недалеко от медпункта."

    hide obhod with dspr

    "Мы пошли не налево, к площади, а направо, дальше по тропинке, которой пришли в медпункт."
    "..."

    hide sl
    show bg ext_library_day
    show sl pioneer normal at right
    with dissolve

    "И буквально через пару минут оказались возле библиотеки."
    "Ухоженное, как и все здесь, это казалось наиболее современным."
    th "Может хоть сейчас всё пойдёт по плану?"

    show sl pioneer smile with dspr

    sl "Стучаться не будем. Заведующая библиотекой моя соседка, Женя. Сейчас она наверняка спит."
    me "Спит? Нет ещё и полудня."

    show sl pioneer smile2 with dspr

    "Славя улыбнулась."
    sl "Ну, она любитель вздремнуть."

    show sl pioneer smile with dspr

    "Мы зашли внутрь."

    stop ambience fadeout 1.0
    stop music fadeout 2.0

    hide sl
    show bg int_library_day
    show sl pioneer normal at cright
    with dissolve

    'Нас встретила…'

    play ambience ambience_library_day fadein 1.0

    "А что нас должно было встретить? Библиотека, она и в Африке библиотека."

    play music music_list["your_bright_side"] fadein 2.0 volume 0.9

    "Половина большого зала была отведена под стеллажи с книгами, вторая под читальный зал."
    th "А где же библиотекарша?"
    "Ответ не заставил себя долго ждать."

    show sl pioneer smile with dspr

    "Славя положила руку мне на плечо, и указала направо."

    show cg d2_micu_lib with dissolve

    "Положив руки под голову, за одним из столов развалилась, по всей видимости, та самая Женя."
    "С приятными чертами лица и в толстых очках, она спала и выражала полное безразличие не только к происходящему вокруг, но и, казалось, ко всему миру."

    hide cg with dissolve

    sl "Давай бегунок, я сейчас."

    play sound sfx_paper_bag volume 0.87

    "Не став спорить, к тому же, Славя говорила шёпотом, я достал из кармана обходной и передал Славе."
    "Та, тихонько подойдя к Жене, и потряся её за плечо, сказала."
    
    show sl pioneer smile2 with good_dspr

    sl "Женя! Женя, проснись!"
    mz "А? Что?"

    show mz pioneer bukal glasses at fright
    with long_dspr

    "Библиотекарша нехотя поднялась на локтях, и посмотрела сначала на Славю, потом на меня."
    mz "Кого ещё нелегкая принесла?"
    "Славя положила на стол обходной, и указала пальцем на последнюю строчку."
    
    show sl pioneer smile with dspr

    sl "Подпиши здесь, пожалуйста."
    "Женя взяла рядом лежащую ручку, и приглядевшись к таблице, оставила роспись."
    sl "Спасибо!"
    mz "Ага… {w}Да. Пожалуйста."

    hide mz with long_dspr

    "Она опять начала сползать на стол, на ходу засыпая."

    hide sl
    show sl pioneer laugh at cright
    with half_good_dspr

    "Славя тихо похихикала, и подошла ко мне."

    show sl pioneer smile with half_good_dspr

    sl "Пойдем."
    "Я двинулся вслед за ней."

    stop ambience fadeout 1.0
    stop music fadeout 2.0

    hide sl
    show bg ext_library_day
    show sl pioneer smile at cright
    with dissolve

    play ambience ambience_camp_center_day fadein 1.0

    me "Чем же она по ночам занимается, что днём спит."
    sl "Даже не знаю. Наверное, книжки читает. Мы хоть и общаемся, но не очень много."
    me "Да, девочка-загадка прям."
    sl "И не говори… {w}Ну что."

    play sound sfx_paper_bag

    "Она развернула обходной, и передала мне."

    show obhod full with dspr

    "Я взял лист, и проверил. Все поля заполнены."
    me "Фух, ну наконец-то. Спасибо большое, без тебя бы до вечера бродил!"

    play music music_list["forest_maiden"] fadein 3.0 volume 0.67

    hide obhod
    show sl pioneer smile2
    with good_dspr

    "Славя смутилась."
    sl "Да что ты, не стоит благодарности! Мне и самой было приятно с тобой погулять."

    hide sl
    show sl pioneer shy close at center
    with half_good_dspr

    "Я набрал в грудь воздух, сделал шаг к девушке и приобнял за плечи."
    me "Все равно спасибо. С тобой очень приятно проводить время."
    "Не знаю, что в этот момент было написано на её лице, но через секунду я почувствовал, что её руки тоже легли мне на плечи."
    sl "Пожалуйста, Сёма."
    "..."

    pause(1.0)

    hide sl
    show sl pioneer tender at center
    with half_good_dspr

    "Через несколько секунд мы отпрянули друг от друга, и я увидел."
    "На лице девушки читалось неподдельное счастье."
    sl "Ну что, пойдем до Ольги Дмитриевны? Отдашь её бегунок, известишь о том, что ты теперь полноправный член музыкального клуба."

    show sl pioneer smile2 with good_dspr

    "Девушка мило улыбнулась."
    me "Да, пойдём."

    stop music fadeout 3.5

    show black with clocks_in

    hide sl
    show bg ext_house_of_mt_day
    show sl pioneer smile at right
    hide black with clocks_out

    "Неторопясь, мы только подошли к домику вожатой, как тут она сама вышла из него, и улыбнулась нам."

    play music music_list["everyday_theme"] fadein 2.5 volume 0.75

    show mt pioneer smile far at center
    with good_dspr

    mt "Семён, Славя! Уже всё обошли?"
    sl "Везде были, Ольга Дмитриевна."

    show mt pioneer grin with good_dspr

    mt "Ну в таком случае, давай, Семён, удиви меня."

    play sound sfx_paper_bag

    show obhod full with dspr

    "Я в последний раз вынул бегунок и развернул его."
    "Сам пройдясь по нему глазами, я передал его вожатой."

    hide obhod full
    show mt pioneer normal
    with dspr

    "Вожатая быстро пробежала всё позиции глазами, после чего утвердительно хмыкнула, и убрала его себе в карман."

    play sound sfx_paper_bag

    show mt pioneer smile with dspr

    mt "Молодец, Семён! Хвалю."
    me "Спасибо. Но вы больше Славе спасибо говорите, она меня везде водила."

    show sl pioneer shy with dspr

    "Славя смутилась."
    me "Хоть лагерь теперь знаю."
    sl "Не стоит, Ольга Дмитриевна. Мне… {w}было совсем не в тягость."

    show mt pioneer surprise with dspr
    pause(1.0)

    show mt pioneer normal
    show sl pioneer smile2
    with good_dspr

    "Вожатая интересно посмотрела на Славю."
    mt "А-а. {w}Хорошо. {w}Ну, тогда идёмте обедать, сейчас уже горн прозвучит."

    play sound sfx_dinner_horn_processed
    pause(0.5)

    "Горн не заставил себя долго ждать."

    show sl pioneer laugh with dspr

    sl "Да вы провидица, Ольга Дмитриевна!"

    show mt pioneer smile with dspr

    mt "А то! Ну, идёмте."

    window hide

    stop music fadeout 2.0
    play sound sfx_clocks fadein 0.5 volume 0.55

    show black with clocks_in

    show bg ext_square_day
    hide black with clocks_out

    show black with clocks_in

    show bg int_dining_hall_people_day
    hide mt
    hide black with clocks_out
    show black with clocks_in

    stop sound fadeout 0.5
    play music music_list["my_daily_life"] fadein 2.0 volume 0.8

    hide sl
    show bg ext_dining_hall_near_day
    show sl pioneer normal at right
    hide black with clocks_out

    window show

    "Этот обед совершенно не отличался от вчерашнего, за тем исключением, что сегодня я его ел."
    "Мы также сидели со Славей, но уже отсутствовало всякое напряжение, и мы весело болтали."
    "Вместе же, мы вышли из столовой."

    show sl pioneer smile with dspr

    sl "Ну что, Семён, теперь ты полноправный пионер в этом лагере."
    sl "Уже не походишь с тобой весь день, да и обязанности у тебя появились."
    th "Мне кажется, или она взгрустнула, говоря это?"
    me "Но это произошло только благодаря тебе! {w}Если бы ты не таскалась со мной эти два дня, даже не знаю, быстро ли бы я тут освоился."

    show sl pioneer shy with good_dspr

    th "И это была чистой воды правда."
    sl "Спасибо, Семён. Мне приятно слышать, что я тебя так выручила."

    show sl pioneer smile2 with dspr

    "..."
    sl "Ну-у, сейчас отдых. А дальше по кружкам. {w}Ты же в клуб пойдешь?"
    me "Да, получается, что так. Тогда, только вечером увидимся?"

    show sl pioneer shy with dspr

    sl "Да… Тогда до вечера."

    hide sl
    show sl pioneer shy close at cright
    with good_dspr

    "В этот раз Славя сама подошла ко мне, и приобняла за плечи. Я ответил взаимностью."

    show sl pioneer smile2 at walk_away_right
    pause(1.0)
    hide sl with dspr

    stop music fadeout 2.0

    "После этого мы ещё раз попрощались, Славя ушла, а я остался стоять на крыльце."

    play music music_list["eat_some_trouble"] fadein 1.0 volume 0.9

    usp "Во те раз! Они тут уже чуть ли не целуются!"

    show us pioneer smile at center
    with dspr

    "Я вздрогнул от неожиданности, и обернулся. Позади меня стояла Ульяна."
    "Я нахмурился, и сказал."
    me "Подсматривать нехорошо. {w}Любопытной Варваре знаешь чё на базаре сделали?"

    show us pioneer surp2 with dspr

    us "Ой, боюсь-боюсь. А ты догони сначала! Бе-е!"

    show us pioneer grin at run_away_left
    hide us with dspr

    "После этих слов Ульяна умчалась прочь."

    stop music fadeout 2.0

    th "М-да. Она точно всё ещё ребенок."
    "Я выдохнул, и пошел в сторону домика."
    "..."

    play music music_list["your_bright_side"] fadein 2.0 volume 0.8

    show bg ext_houses_day with dissolve1

    "По пути я понял, что хочется курить."
    th "А ведь уже половина дня прошла, а ещё не курил. В {i}моём{/i} мире это была бы уже катастрофа."
    "Но здесь, находясь в прекрасном месте…"
    th "И в окружении прекрасных дам, да?"
    th "Что?"
    th "Это я сейчас подумал? {w}Ладно…"

    stop ambience fadeout 1.0

    "В общем да, в прекрасном месте, и вместе со Славей. Она успокаивала не хуже любой сигареты."

    play ambience ambience_forest_day fadein 1.0

    show bg ext_path_day with dissolve

    "Ведя внутренний монолог, я свернул на ближайшую тропинку, уходящую куда-то в лес, и встал за дерево."

    call smoking_process

    "..."

    show blink

    "Горячий ароматный дым вновь приятно заполнил горло, а я прикрыл глаза, и просто наслаждался послеобеденной сигаретой..."

    queue sound sfx_hiding_in_bush fadein 1.0 volume 0.7

    "… Пока не услышал какой-то шорох…"

    hide blink
    show unblink

    "Открыв глаза, я огляделся, и увидел на ветке дерева недалеко белочку, которая с любопытством смотрела на меня."

    hide unblink

    th "Даже не боится. Подкармливают её тут, видимо."
    me "Извини, животное, у меня для тебя ничего нет."
    "Она, конечно, моих извинений не поняла, да так и продолжила на меня смотреть, и дёргать носиком, пока я курил."
    th "Пора возвращаться в домик."

    stop ambience fadeout 1.0

    "..."

    show bg ext_house_of_mt_day with dissolve2

    stop music fadeout 3.0

    "Подходя к порогу домика, я, всё ещё погруженный в свои мысли, просто дернул за ручку и вошёл внутрь."

    play ambience ambience_int_cabin_day fadein 1.0
    play sound sfx_open_door_1
    play music music_list["doomed_to_be_defeated"] fadein 1.0

    show cg d2_mt_undressed with dissolve

    "И только закрыв за собой дверь, я понял что передо мной стоит Ольга Дмитриевна. {w}И переодевается!"

    hide cg
    show cg d2_mt_undressed_2
    with dissolve

    "Она обернулась."
    mt "Семён! Стучаться надо! А теперь брысь отсюда!"

    play sound sfx_open_door_1
    stop music fadeout 2.0
    stop ambience fadeout 1.0

    hide cg
    show bg ext_house_of_mt_day
    with dissolve

    play ambience ambience_camp_center_day fadein 1.0

    "Я вылетел из домика."
    th "Откровенно говоря, конечно, зрелище пришлось мне по нраву."
    th "Но, в любом случае, это было некрасиво."

    show mt pioneer normal at center
    with good_dspr

    "Вышла вожатая."
    mt "Семён, ну ты даёшь. {w}Всегда же стучался."
    me "Извините, я что-то… Задумался."

    show mt pioneer smile with dspr

    play music music_list["everyday_theme"] fadein 2.0 volume 0.72

    mt "Ладно, ничего страшного. Ты отдыхать пришел?"
    me "Да, думал вздремнуть часик, а потом обязательно в клуб!"

    show mt pioneer grin with half_good_dspr

    "Она улыбнулась."
    mt "Ну, на отдых уже осталось меньше часика. {w}Но, конечно, иди отдохни."

    show mt pioneer normal with half_good_dspr

    mt "Я тебя разбужу, не волнуйся. Все равно я планировала тут в гамаке посидеть, книжку почитать."
    me "Хорошо."
    mt "И вот ещё что, Семён."
    me "Да?"

    show mt pioneer smile with dspr

    mt "Я сначала совсем забыла, но, в общем, в домике на столе лежит пакет с банными принадлежностями. Они твои."
    me "О-о, это не помешает, спасибо!"

    stop ambience fadeout 1.0
    show mt pioneer smile at walk_away_right
    pause(1.0)
    hide mt with dspr

    "Разминувшись с вожатой, я зашел в домик."

    show bg int_house_of_mt_day with dissolve

    play ambience ambience_int_cabin_day fadein 1.0

    "На столе и правда лежал какой-то пакет."
    "Я подошёл и повертел его в руках: мочалка, мыло, зубная щетка… {w}И какая-то баночка."
    th "А зубная паста где?"
    "Я пригляделся к баночке, и понял."
    me "Понятно."
    "Надпись явно давала понять: Зубной порошок."
    th "Отлично, +1 очко за то, что я не в своём времени."
    "Вздохнув, я положил пакет в тумбочку, снял обувь, и разлегся на кровати."

    stop music fadeout 2.0

    "В голову решительно не шли никакие мысли, поэтому лёжа с закрытыми глазами, уже через пару минут я начал дремать."

    show black with clocks_in

    show bg int_house_of_mt_day
    show mt pioneer normal at right
    hide black
    with clocks_out

    play music music_list["confession_oboe"] fadein 4.0 volume 0.75

    mt "Семён! Подъём!"
    "Я сразу открыл глаза, и повернулся на бок."
    me "Что, уже пора что ли?"

    show mt pioneer grin with dspr

    mt "Ну не я шлялась где попало, вместо того, чтобы сразу идти отдыхать."

    show mt pioneer smile with dspr

    mt "Давай-давай, тебе в клуб пора."
    me "Да даю, я, даю."
    "Ощущение было такое, словно бы и не спал, но чувствовал себя пободрее. По ощущениям, прошло минут 40."
    "Я обулся, поправил форму, и вышел из домика."

    stop ambience fadeout 1.0

    hide mt
    show bg ext_house_of_mt_day
    with dissolve

    play ambience ambience_camp_center_day fadein 1.0

    th "Покурить бы не помешало."
    "Я задумался."
    "Судя из того, что я успел понять касательно расположения объектов в лагере, если я сейчас обогну крайний ряд домов, и пойду примерно на юго-запад, то как раз выйду к музыкальному клубу."
    "А в лесу мне никто не помешает посмолить. {w}Отлично."

    stop ambience fadeout 1.0

    show bg ext_path_day with dissolve1

    play ambience ambience_forest_day fadein 1.0
    play sound sfx_smoking_cigaret

    "Так я и сделал, и курил, идя по лесной тропинке."
    "Докурив сигарету, я потушил её и отправил окурок подальше в лес, закинул в рот жвачку, и начал прикидывать, когда поворачивать."
    "..."
    th "Ну, наверное сейчас. В любом случае не заблужусь."

    stop ambience fadeout 1.0

    show bg ext_musclub_verandah_day with dissolve1

    play ambience ambience_camp_center_day fadein 1.0

    "Интуиция меня не подвела."
    "Через пару минут я оказался перед зданием музклуба, только с другой стороны."
    "Обойдя его, я уже было хотел открыть дверь, но одернулся, вспомнив, как Мику меня со Славей встречала утром, и как я вломился в наш с вожатой домик."

    play sound sfx_knock_door7_polite

    "Поэтому, я, как можно более громко, но аккуратно, постучал."
    mi "Да-да, заходите!"

    show cg d5_mi with dissolve1

    stop ambience fadeout 1.0
    stop music fadeout 2.0

    "Я открыл дверь, и меня встретила Мику, которая вытирала тряпкой рояль."
    mi "Сёма! Наконец-то ты пришел."

    hide cg
    show bg int_musclub_mattresses_day
    with dissolve

    play ambience ambience_music_club_day fadein 1.0
    
    "Она оставила тряпку, и подошла ко мне."

    play music music_list["so_good_to_be_careless"] fadeout 2.0 volume 0.85

    show mi pioneer grin with dspr

    "Я заулыбался, наблюдая, как она вся начинает сверкать от счастья."
    
    show mi pioneer happy with dspr

    mi "Так здорово, что я теперь буду не одна, а то и играть одной скучно, и вот, сейчас мне немножко убраться надо, одной было бы очень тяжело, но вдвоём мы быстро справимся!"
    me "Не сомневаюсь. Особенно, если в процессе ты мне что-нибудь расскажешь про Японию."
    me "Мне было бы очень интересно послушать!"

    show mi pioneer cry_smile with dspr

    mi "Что, правда-правда? Ой, здорово! Я тебе столько всего расскажу!"
    mi "Кстати, а Славя не против, что мы теперь будем много общаться?"

    show mi pioneer surprise with dspr

    me "Что?"
    mi "Что? Я хотела сказать… {w}Вот блин, опять запуталась, хи-хи."

    show mi pioneer normal with half_good_dspr

    mi "А Славя тебя сегодня везде проводила?"
    me "Да-а, она мне очень сильно этим помогла. Без неё бы наверное до вечера плутал."
    me "А так, и всё сделал, и лагерь запомнил, и с ней… {w}То есть, с таким хорошим человеком, как она, время провел."

    show mi pioneer shy with dspr

    mi "Ой, замечательно! Я так рада!"

    show mi pioneer happy with dspr

    mi "А ещё я рада, что у меня теперь появился помощник и товарищ по клубу!"
    "Я улыбнулся."

    stop music fadeout 2.0

    me "Я тоже рад, Мику. Ну что, начнём?"

    play music music_list["went_fishing_caught_a_girl"] fadein 2.0 volume 0.8

    hide mi with dspr

    call to_nvl_mode

    "Мы приступили к уборке."
    "Мику налила мне отдельное ведро воды, и мы разделились. Она взяла на себя всё мелкое и хрупкое, а я, самое крупное, и те места, где приходилось что-нибудь двигать, переставлять… В общем, где требовалась мужская сила."
    "После мебели мы перешли к окнам. Благо снаружи их мыть не пришлось, только внутри. Но всё равно это было довольно неудобно из-за высоты окон."
    "Последним остался пол. Благо корячиться в таком большом помещении не пришлось, в подсобке были швабры."
    "По итогу, весь процесс, вместе с заменой воды занял у нас не больше полутора часов."
    nvl clear
    "Параллельно, Мику мне постоянно рассказывала что ни будь про Японию, как я и попросил. Было интересно услышать много подробностей из первых уст."
    "..."
    "Кстати, во время того, как она рассказывала, я заметил, что она стала меньше «пулемётить». Рассказывала она содержательно, интересно, и при этом не перегружала меня потоком слов, давая иногда что-нибудь спросить."
    "Уж не знаю, влияла так на неё физическая деятельность, или осознание, что теперь не придётся стрелять словами, теряя половину, чтобы с кем-нибудь поговорить, но мне это понравилось в любом случае."

    stop music fadeout 2.0

    call to_adv_mode

    show mi pioneer normal at cleft
    with dspr

    mi "Фу-ух, закончили!"

    play music music_list["so_good_to_be_careless"] fadein 2.0 volume 0.85

    "Мы сложили весь уборочный инвентарь в подсобку, и сели на матрасы в правой стороне комнаты."
    me "Это было не так уж и сложно. Одна ты бы тут, наверное, ещё часа два возилась?"
    
    show mi pioneer sad with dspr

    mi "Да-а, я тут уже убиралась одна, так долго было, и я так устала!"
    me "Могу представить."

    show mi pioneer smile with dspr

    me "Кстати, а откуда матрасы в музыкальном клубе?"
    "Я похлопал рукой по матрасу, на котором сидел."
    mi "Ой, да не знаю, честно говоря! Они тут появились ещё до того, как я пришла."

    show mi pioneer happy with dspr

    mi "Вроде ремонт делали в спортивном зале, или вроде того, и сложили зачем-то здесь."
    mi "А в зал новые уложили, так что эти тут остались."
    me "Во-от как. Понятно."
    th "Загадка раскрыта. Отличная работа, Холмс."

    show mi pioneer serious with dspr

    mi "Да. Но вот что! Мы заслужили небольшой отдых! Сейчас выпьем зелёного чаю, а потом я нападу на тебя с музыкой."
    me "Хорошо."

    show mi pioneer serious at walk_away_left
    pause(1.0)
    hide mi with dspr

    "Мику удалилась в подсобку, откуда стало слышно ворошение."
    th "Никогда ещё Штирлиц не был так близко к провалу. Вот сейчас она даст мне в руки гитару, поймёт что я полный профан, и ссаной тряпкой меня из клуба погонит, и стану я посмешищем всея лагеря."

    show mi pioneer normal at center
    with dspr

    mi "О чем задумался?"
    "Мику вернулась с двумя маленькими чашечками, от которых исходил пар, а сами чашечки стояли на блюдцах."
    me "Да так, о делах насущных."
    "Я принял у неё чай."
    me "Спасибо, Мику."

    show mi pioneer grin with dspr

    mi "Пожалуйста!"

    hide mi
    show mi pioneer smile at left
    with dspr

    "Девушка обратно села на матрасы рядом со мной."
    me "Просто хочу тебя предупредить, чтобы ты не ждала ничего сверхъестественного от меня. Я играю плохо. Реально плохо."
    th "Если я вообще ещё помню, как играть. Сколько я отзанимался-то, неделю? Полторы?"

    show mi pioneer shy with dspr

    mi "Да брось, Семён, ничего страшного! Мы же сюда и приходим, чтобы учиться."

    show mi pioneer smile with dspr

    mi "Да и потом. В роли учителя мне ещё не приходилось выступать. Вот и посмотрим, как я справлюсь."
    th "Блин, она такая милая…"
    "..."
    "Мы допили чай, отнесли кружки, и вернулись в главный зал."

    hide mi
    show mi pioneer normal at cright
    with good_dspr

    mi "Ну что, Семён? На чём ты играешь?"
    me "А ты что, чему угодно можешь научить?"

    show mi pioneer serious with dspr

    mi "Ну-у, вообще основной профиль у меня гитара, но умею на всём, да."
    me "Ого… {w}Ну, гитара. Акустическая."

    show mi pioneer grin with dspr

    mi "Отлично! Сейчас принесу, подожди пока!"

    hide mi
    show mi pioneer smile
    with dspr

    show mi pioneer smile at walk_away_left
    pause(1.0)
    hide mi with good_dspr

    "Я сел, и пронаблюдал как девочка направляется в дальний угол комнаты, и возвращается с гитарой в руке."

    show mi pioneer normal at right
    with dspr

    "В нижней части черного глянцевого корпуса было жирными белыми буквами выбито «YAMAHA»."
    me "Ого, японская?"

    show mi pioneer happy with dspr

    mi "Да, я с собой её привезла. Вообще, она уже довольно старенькая, но всё ещё хорошо играет."

    hide mi
    show mi pioneer normal close at right
    with half_good_dspr

    "Мику села рядом."

    stop music fadeout 2.0

    mi "Вот, послушай. И следи за руками."

    window hide

    show cg mi_guitar_yam with dissolve

    play music miku_song_mi_learn1 noloop

    $ renpy.pause(1.0, hard=True)

    call calc_music_how_much_play

    window show

    "Мику исполнила довольно простую, но красивую мелодию."
    "Хотя, мне кажется, она специально играла медленнее своего, чтобы я успел понять, что она делает."

    hide cg with dissolve

    mi "Ну как, понял? Попробуй."
    "Она протянула мне гитару."
    "Не то, чтобы я что-то понял, но примерные лады запомнил."
    "Я взял гитару, расположил её на колене, и постарался примериться."
    me "Так… {w}Только чур не смеяться."

    window hide

    play music miku_song_bad_learn noloop

    $ renpy.pause(1.0, hard=True)

    call calc_music_how_much_play

    window show

    th "Господи, ну и позорище… "
    "Всё это время Мику внимательно смотрела на меня."
    "Я, кажется, был весь красный, а вот она смотрела на меня довольно серьёзно."

    play music music_list["farewell_to_the_past_edit"] fadein 4.0 volume 0.7

    show mi pioneer serious with dspr

    mi "Сколько ты говоришь, занимался?"
    me "Ну… {w}Пару недель."
    mi "Семён..."

    show mi pioneer smile with dspr

    mi "Это хороший результат! Нет, правда!"
    "Сказать, что я был в шоке, ничего не сказать."
    mi "За две недели не все умеют правильно гитару в руках держать, а ты {i}почти{/i} полностью и {i}почти{/i} правильно повторил композицию!"
    me "Ключевое здесь почти, да? Ха-ха."

    show mi pioneer serious with good_dspr

    mi "Нет, Сёма. Не смейся над собой."
    "Кажется, впервые она была серьёзна."
    mi "Я видела много людей, которые бросали музыку, потому что им казалось, что у них ничего не получается."
    mi "Для кого-то это было так, другие, как ты, ругали сами себя ни за что."
    mi "Но это не отменяет того, что научиться может каждый."

    show mi pioneer normal with dspr

    stop music fadeout 2.0

    mi "А ты тем более!"
    me "Спасибо…"

    play music music_list["so_good_to_be_careless"] fadein 2.0 volume 0.95

    "Честно говоря, я был довольно смущён."

    show mi pioneer grin with dspr

    mi "Ну всё, ты теперь не отвертишься! {w}Будем заниматься с тобой в этом направлении. И я от тебя не отстану, пока мы не сможем исполнить песню вместе! Ты на гитаре, а я буду петь."
    me "Ого, ты и петь умеешь? Ну девочка-оркестр прям!"

    show mi pioneer shy with dspr

    "Мику смутилась."
    mi "Ну не прям уж и оркестр…"

    show mi pioneer happy with dspr

    mi "Ну ладно, я предлагаю начать прямо сейчас, но с чего попроще… Как у тебя с табами?"
    me "Фифти-фифти."

    show mi pioneer grin with fast_dspr

    mi "Отлично, тогда не будем терять время!"

    pause(1.5)

    hide mi with good_dspr

    call to_nvl_mode

    "Мы провели в клубе ещё пару часов."
    "Мику кратко напомнила мне (а в каких-то моментах и объяснила впервые), как читать табы, как строится ряд, и прочие теоретические, но необходимые знания."
    "Затем, мы ещё немного попрактиковались. Она наладила мне положение во время игры, подсказала как зажимать струны, чтобы пальцы не уставали, а также вручила медиатор, и показала как им правильно пользоваться."
    "Я старался впитывать как можно внимательнее, так как и сам загорелся своим обучением."

    call to_adv_mode

    show mi pioneer normal at right
    with dspr

    play sound sfx_dinner_horn_processed

    "Но вот, с улицы послышался горн, призывающий пионеров на ужин."

    show mi pioneer shocked with dspr

    mi "Ой, пора идти! А то опоздаем, пойдём скорее!"
    "Мы спешно убрали гитару, и чуть ли не легким бегом направились к столовой."

    window hide

    play sound sfx_clocks fadein 0.5 volume 0.5
    stop ambience fadeout 1.0
    stop music fadeout 2.0

    show black with clocks_in

    hide mi
    show bg ext_houses_day
    hide black
    with clocks_out

    show black with clocks_in

    call set_time("sunset")

    stop sound fadeout 1.0
    play ambience ambience_dining_hall_full fadein 1.0

    show bg ext_dining_hall_near_sunset
    show mi pioneer normal at cleft
    hide black
    with clocks_out

    play music music_list["dance_of_fireflies"] fadein 2.0 volume 0.85

    "На удивление, перед входом в столовую всё ещё были пионеры."
    mi "Фух, не опоздали!"
    "Мы поспешили зайти в столовую."

    show bg int_dining_hall_people_sunset
    show mt pioneer normal at fright
    with dissolve

    "На входе нас встречала Ольга Дмитриевна."
    mt "Ну вот, музыка как обычно последняя."

    show mt pioneer smile with dspr

    "Она улыбнулась."
    mt "Бегите получайте порции."

    hide mt with long_dspr

    "Мы с Мику поспешили взять подносы, и уйдя с линии раздачи, увидели Славю и Лену, сидящих за крайним столом. Славя махала нам."
    me "Мику, пойдем, у них там как раз два свободных места."

    show mi pioneer grin with dspr

    mi "Ой, здорово, и Славечка, и Леночка там!"

    hide mi
    show sl pioneer smile at fright
    show un pioneer normal at cleft
    show mi pioneer normal at fleft
    with good_dspr

    "Мы подошли, сели к ним за стол и пожелали друг другу приятного аппетита."
    "Когда я увидел Славю, у меня аж сердце зарадовалось. Не знаю, почему, но не видел её пол дня, и уже успел… {w}Соскучиться? {w}Хотелось быть с ней всегда."

    show sl pioneer smile2 with dspr

    sl "Сёма, я уже успела соскучиться!"
    th "Совпадение?"
    "Я улыбнулся, и ответил."
    me "Я тоже!"

    show sl pioneer smile with dspr

    sl "Как первый день в кружке?"
    me "Отлично! Успел убраться, опозориться, попить чай и поучиться! В общем, времени зря не терял."

    show un pioneer smile
    show mi pioneer smile
    with dspr

    mi "Ну это он так шутит, ха-ха."
    mi "На самом деле у Семёна очень хорошо получается играть на гитаре."

    show un pioneer surprise
    show sl pioneer smile2
    with half_good_dspr

    sl "Да? Вот здорово."

    show un pioneer smile
    show sl pioneer smile
    with good_dspr

    sl "Может ты тогда нам всем скоро что-нибудь сыграешь?"
    me "Ну-у, до этого ещё далеко… {w}Мику очень сильно преувеличила насчёт «очень хорошо получается»."
    mi "Тогда я могу всем сыграть, если хотите. Кстати."

    show mi pioneer normal
    with good_dspr

    "Она проглотила кусочек котлеты и продолжила."
    mi "После ужина сейчас свободное время. Вы не собирались чем-нибудь заняться?"

    show sl pioneer surprise
    show un pioneer shy
    with dspr

    "Кажется, всех этот вопрос немного удивил, ведь, как я сам понял, Мику редко с кем-то общалась, а уж тем более напрашивалась."

    sl "Вообще да, и я как раз хотела об этом сказать."

    show sl pioneer smile with dspr

    sl "Мы с Леной…"

    show un pioneer smile with dspr

    "Лена, всё это время сидевшая молча, кивнула."
    sl "... хотели сходить на пляж. Но не на песок, а там рядом есть такое местечко, под деревьями, покрытое травой. Посидим, полюбуемся закатом, пообщаемся. Будет здорово."
    un "Да. {w}Мику, тогда может и гитару возьмёшь?"
    "Робко вставила Лена."

    show mi pioneer happy with dspr

    mi "Конечно возьму, Леночка, какой разговор!"
    me "Больше никто не идёт?"

    show un pioneer normal
    show mi pioneer smile
    with dspr

    sl "А больше и некого звать."
    
    show sl pioneer normal with dspr

    sl "Алиса точно не пойдет, Женя наверное опять до ночи в домике будет книжки читать… Ульяна слишком маленькая. А больше и некого."

    show mi pioneer normal with dspr

    mi "А парней позвать не хочешь, Семён?"
    me "Ну уж нет, мне и без них хорошо будет."

    show sl pioneer laugh with dspr

    "Я вспомнил сегодняшний инцидент, и посмотрел на Славю. Она, кажется, сделала то же самое, и тихонько хихикла."

    show sl pioneer smile
    show un pioneer smile
    hide mi
    show mi pioneer grin far at fleft
    with good_dspr

    "Мику встала."
    mi "Ну, тогда решено? {w}Встречаемся на пляжу через… Через сколько?"

    show un pioneer smile2
    show sl pioneer laugh
    with dspr

    un "Хи-хи."
    me "Поляжу я на пляжу."

    show mi pioneer surprise with dspr

    sl "Аха-ха, ну я не знаю. Давайте… Через 30 минут все успеют? Ольгу Дмитриевну я за всех предупрежу."

    show un pioneer smile
    show sl pioneer smile
    show mi pioneer normal
    with dspr

    me "Не нужно, Славя, я сам. {w}Я же живу с ней, а ты готовься, нечего мотаться туда-сюда."

    show sl pioneer smile2 with dspr

    sl "Ой, и правда. Спасибо большое, Сёма!"
    me "Значит решено?"

    show sl pioneer smile with dspr

    "Все единогласно ответили да, поэтому мы сдали подносы, и все вместе вышли из столовой."

    stop ambience fadeout 1.0

    hide sl
    hide mi
    hide un
    show bg ext_dining_hall_near_sunset
    show sl pioneer normal at right
    show un pioneer smile at center
    show mi pioneer normal at left
    with dissolve1

    play ambience ambience_camp_center_evening fadein 1.0

    "Мы вышли из столовой."

    show mi pioneer shocked with dspr

    mi "Ой, я же клуб не закрыла!"
    mi "Ладно, я постараюсь успеть!"

    show mi pioneer normal with dspr

    me "Тебе помочь?"
    mi "Не-е, спасибо. Ключ-то у меня, только вот крюк теперь делать."

    show un pioneer shy with dspr

    un "Давай я с тобой прогуляюсь. Всё равно же вместе живём."

    show mi pioneer happy with dspr

    mi "Здорово, пойдем!"

    stop music fadeout 2.0

    show mi pioneer normal
    show un pioneer normal
    with dspr

    show mi pioneer normal at walk_away_left
    show un pioneer normal at walk_away_left
    pause(1.0)

    hide mi
    hide un
    with good_dspr

    "Девушки удалились."

    play music music_list["she_is_kind"] fadein 2.0 volume 0.9

    show sl pioneer smile with dspr

    sl "А нам с тобой в другую сторону."
    me "Да… Двинули потихоньку, не будем торопить Мику с Леной."
    "Мы неспеша пошли в сторону площади и заговорили о том о сём…"

    show black with clocks_in

    show bg ext_square_sunset
    hide black
    with clocks_out

    "Вышли на площадь."

    show black with clocks_in

    show bg ext_houses_sunset
    hide black
    with clocks_out

    "И вышли к домикам пионеров."

    show sl pioneer smile2 with dspr

    sl "Теперь мне направо, тебе прямо."
    me "Да…"
    "Сам ещё не до конца понимая себя, я чувствовал, что не хочу отпускать эту девочку ни на минуту."

    show sl pioneer surprise with dspr

    sl "Ой, а ты дорогу на пляж то найдешь?"
    "Я мысленно покрутил в голове примерное расположение объектов в лагере."
    me "После склада прямо и направо?"

    show sl pioneer smile with dspr

    sl "Верно! Тогда встретимся там. Не опаздывай!"
    me "Ты тоже!"

    show sl pioneer smile at walk_away_right
    pause(1.0)
    hide sl with good_dspr

    "Мы разошлись, и я направился в сторону нашего с вожатой домика."

    show bg ext_house_of_mt_sunset with dissolve

    th "Так, постучать, надо постучать."

    play sound sfx_knock_door7_polite

    "Я постучал."
    mt "Заходи, Семён."

    stop ambience fadeout 1.0

    show bg int_house_of_mt_sunset
    show mt pioneer normal at center
    with dissolve

    play ambience ambience_int_cabin_evening fadein 1.0

    "Я зашёл."
    "Не зная, как начать разговор, я мялся, и начал говорить что-то не вполне внятное."
    me "Ольг Дмитрвн, а я, а мы тут, это…"

    show mt pioneer grin with dspr

    mt "Куда-то идёшь? С кем, куда, насколько?"
    "Вожатая меня ошарашила."
    me "Как вы догадались?"

    show mt pioneer smile with dspr

    "Она улыбнулась."
    mt "Профессиональная чуйка. Ну так?"
    me "Я, Славя, Мику, Лена. На пляж. Купаться не будем. Ненадолго."
    "Отчеканил я кратко и чётко."

    show mt pioneer surprise with dspr

    mt "Хм. Ну, не самая плохая компания, знаешь. Да и Славя с вами, а ей я на сто процентов доверяю."
    
    show mt pioneer normal with dspr

    mt "Ладно уж, идите. Но чтоб до одиннадцати все вернулись!"
    me "Конечно!"
    th "Как мы, интересно, узнаем, когда одиннадцать… Часов ни у кого нет."

    show mt pioneer smile with dspr

    mt "Вот и отлично…"
    mt "Так, я в медпункт… Это."

    show mt pioneer grin with dspr

    mt "Медсестра звала по какому-то делу. {w}Вот. {w}Ключ у тебя есть, свой я взяла. Домик закрой обязательно, и свет выключи."
    me "Всенепременно!"
    "Карикатурно отсалютовал я."

    show mt pioneer laugh with dspr

    mt "Ой, допросишься ты."

    show mt pioneer smile with dspr

    mt "Ладно, я пошла. И чтобы никаких мне там! На пляже."

    show mt pioneer smile at walk_away_right
    pause(1.0)
    hide mt with half_good_dspr

    "После этих слов вожатая вышла из домика."
    "Каких таких никаких я так и не понял, но решил, что и так всё понял."
    "Я огляделся."
    th "Так… А надо мне собственно чего, нет? А я не знаю."
    "Умение собираться никогда не было моей сильной стороной."
    "Сев на кровать, и положив голову на кулак, я задумался… {w}Но почти сразу заметил какой-то прямоугольник, лежащий на краю подоконника, со стороны, где спала вожатая."
    th "Сигареты?"
    "Но встав, и подойдя, я увидел."
    "На подоконнике лежала колода карт в упаковке."
    th "Опа-па… Азартными играми наша Ольга Дмитриевна промышляет?"
    th "Ай-яй-яй."
    "И набор то, покерный, по всей видимости."
    "Я открыл коробочку, и полистал колоду. Ну да. {w}Есть и двойки и пятерки. Пятьдесят две карты."
    "Сразу я подумал, что на пляже было бы неплохо перекинуться в картишки."
    "А если вожатая узнает, что я у неё карты взял?"
    $ renpy.pause(1.5, hard=True)
    "На несколько секунд я задумался, взвешивая за и против."
    th "Ай, чёрт с ним! Была не была!"
    "Я убрал карты в карман."
    "Чего уж там… Один раз живём."
    "..."
    "Сделав несколько кругов по домику, я всё-таки сел на кровать, прикидывая, сколько у меня ещё времени до выхода."
    th "Посмотрю пока время на телефоне."
    "Я залез в подушку, и достал телефон."
    "Если мои часы всё-таки шли правильно, сейчас было 19:15."
    "На мобильнике, тем временем, оставалось уже 75%% заряда."
    th "Ну ладно, побреду потихоньку."

    stop ambience fadeout 1.0
    stop music fadeout 2.0

    show bg ext_house_of_mt_sunset with dissolve

    play ambience ambience_camp_center_evening fadein 1.0

    "Я выключил свет, вышел из домика, закрыл его, и направился в сторону пляжа."
    "..."

    show bg ext_square_sunset with dissolve

    play music music_list["everyday_theme"] fadein 2.0 volume 0.7

    "На площади я пересёкся с Мику и Леной."

    show mi pioneer normal at right
    show un pioneer normal at left
    with half_good_dspr

    "Мику шла с гитарой."
    
    show mi pioneer smile with dspr

    mi "О, Семён. Тоже уже идешь?"
    me "Да. А Славю не видели?"

    show un pioneer smile with dspr

    un "Она скорее всего уже там нас ждет. Любит же она всё подготовить."
    me "И то верно."
    me "Ну, тогда не будем терять время!"
    "Мы немного прибавили шаг."

    stop ambience fadeout 1.0

    show black with clocks_in

    play ambience ambience_lake_shore_evening fadein 1.0

    hide mi
    hide un
    show mi pioneer normal at fright
    show un pioneer smile at cright
    show bg ext_beach_sunset
    hide black
    with clocks_out

    "И вскоре оказались на пляже."
    "Вечернее солнце заливало воду и всё вокруг приятным, красно-розовым светом."
    "А чуть поодаль, возле дерева мы увидели Славю, которая махала нам рукой."

    show sl pioneer smile at left
    show mi pioneer happy
    with dspr

    mi "Ну вот мы все снова и встретились. Чем займёмся?"
    sl "Ой, Микусь, я предлагаю пока просто посидеть… Находилась я сегодня."
    me "Это правда, Славя сегодня со мной наверное совсем устала… По всему лагерю ходить."

    show sl pioneer shy with dspr

    "Славя опять смутилась."
    sl "Ну-у, мне было не в тягость. Но ноги устали, это правда."

    show mi pioneer smile
    show un pioneer smile2
    show sl pioneer smile2
    with dspr

    un "Давайте тогда просто посидим, посмотрим на закат. А я вот ещё."
    "Она потрясла небольшим пакетом."
    un "Всем по яблоку взяла… Медсестра угостила."

    th "Я и не заметил, что Лена шла с пакетом…"
    mi "Ой, здорово!"

    show mi pioneer normal
    show un pioneer smile
    show sl pioneer smile
    with good_dspr

    "Мы расселись возле дерева, и направили взгляды на закат."
    "По мосту, примерно в километре от берега проходил поезд."
    th "Тут и поезда ходят? Интересно…"
    th "Вот бы на него забраться, интересно, куда он следует?"

    play sound sfx_eat_apple

    "Мы проводили поезд взглядом, продолжая хрустеть яблоками."

    hide sl
    show sl pioneer smile2 close at left
    with long_dspr

    "Славя, которая сидела рядом со мной, подвинулась ближе, и немного оперлась своим плечом на моё."
    "Посмотрев друг на друга, мы улыбнулись, но ничего не сказали."
    "..."
    
    hide sl
    hide mi
    hide un
    show sl pioneer smile at left
    show mi pioneer far normal at center
    show un pioneer normal at right
    with good_dspr

    "Спустя пару минут, и закончившееся у всех яблоко, мы кинули остатки под куст, после чего, как-то так само получилось, расселись кружком, кроме Мику, которая легонько вскочила, и сказала."
    mi "Я сейчас, секундочку!"

    show mi pioneer far normal at run_away_right
    pause(0.75)
    hide mi with dspr

    "Она подбежала к воде, помыла руки, после чего быстренько вытерла их об юбку."

    show mi pioneer smile at center
    with good_dspr

    "Мику взяла гитару, стоявшую под деревом, и вернулась к нам."
    mi "Давайте я нам что-нибудь сыграю."

    show un pioneer smile with dspr

    stop music fadeout 2.0

    "Никто не возражал."
    "Секунд десять Мику потратила на то, чтобы сесть поудобнее и настроиться играть."
    "Пару раз она дернула несколько струн, после чего, приготовившись, начала играть."

    play music memories_guitar_only noloop

    $ renpy.pause(2.0, hard=True)

    "Она играла какую-то очень красивую, но, как мне казалось, немного грустную мелодию…"

    $ renpy.pause(1.0, hard=True)

    hide sl
    show sl pioneer tender close at left
    with dspr

    "Славя положила голову мне на плечо…"

    $ renpy.pause(1.0, hard=True)

    hide un
    show un pioneer cry_smile at right
    with dspr

    "У Лены, кажется, намокли глаза…"

    $ renpy.pause(1.0, hard=True)

    "Что-то очень теплое и душевное навевает эта композиция…"

    show cg mi_guitar_yam with dissolve

    "Я посмотрел на Мику. {w}Она играла с закрытыми глазами, полностью сосредоточившись на музыке."

    window hide

    call calc_music_how_much_play

    hide cg
    hide mi
    show mi pioneer smile at center
    with dissolve

    window show

    "Когда её пальцы сыграли последние аккорды, а звук совсем затих, она открыла глаза, и посмотрела на нас."
    "Я очнулся первый."
    me "Мику, это… Очень красиво!"

    play sound sfx_simon_applause loop

    "Я встал и начал хлопать."

    hide un
    hide sl
    show un pioneer smile2 at right
    show sl pioneer smile at left
    with good_dspr

    play sound2 "<from 0.2>" + sfx_simon_applause fadein 0.5 volume 0.8 loop
    play sound3 "<from 0.5>" + sfx_simon_applause fadein 0.5 volume 0.55 loop

    "Буквально через секунду подключились и всё остальные."

    hide mi
    show mi pioneer shy at center
    with half_good_dspr

    "Мику, кажется, была очень довольна, но настолько засмущалась, что не могла сказать и слова, да так и осталась сидеть с гитарой."

    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    stop sound3 fadeout 1.0

    "Закончив с аплодисментами, мы сели обратно."

    show un pioneer smile
    show mi pioneer happy
    with dspr

    play music music_list["sweet_darkness"] fadein 2.5 volume 0.85

    un "Мику, очень красиво! А она как-нибудь называется?"
    mi "Да. Я назвала её «Воспоминания». Это воспоминания о моей родине."
    sl "Ты её ещё и сама сочинила? Очень здорово!"
    "Ещё обменявшись любезностями, и порасспрашивав Мику о песне, мы переключились на другую тему."

    show mi pioneer smile
    show sl pioneer normal
    show un pioneer normal
    with good_dspr

    me "Времени у нас есть ещё порядком. Чем хотите заняться?"

    show sl pioneer smile with dspr

    sl "Я с собой карты взяла, можно поиграть. Только никому ни слова!"
    "Я уставился на неё глазами по пять копеек да раскрыл рот."

    show sl pioneer surprise with dspr

    sl "Семён? Что такое?"
    "Кажется, Славя немного напряглась."
    "Лена и Мику смотрели то на меня, то на неё."
    "Я медленно засунул руку в карман, достал оттуда карты, и показал всем."
    
    show sl pioneer laugh
    show mi pioneer laugh
    show un pioneer smile2
    with good_dspr

    "Секунда паузы, и мы все захохотали."
    sl "Ха-ха, Семён, ну ты даёшь! Откуда у тебя карты?"
    me "Так я, это… С собой привез просто! Вот."

    show sl pioneer smile2
    show mi pioneer smile
    show un pioneer smile
    with good_dspr

    "Говорить, что это {b}{u}С{/b}{/u}тратегическое {b}{u}П{/b}{/u}еремещение {b}{u}И{/b}{/u}зделия {b}{u}З{/b}{/u}акончившееся {b}{u}Д{/b}{/u}олговременным {b}{u}И{/b}{/u}зменением {b}{u}Л{/b}{/u}окации, совершённое мной, я не стал."

    sl "А-а, понятно! А то тут видишь, Электроник на прошлой неделе игру карточную показывал, я за картами ходила в домик вожатой. Да так они у меня и остались."

    show sl pioneer smile
    show mi pioneer smile
    with dspr

    me "Вот как… Ну теперь у нас две колоды. Чьей будем играть?"

    show un pioneer smile2

    un "А у меня есть идея!"
    "Все посмотрели на Лену."

    show un pioneer smile3

    un "Нас четверо, и две колоды. Давайте небольшой турнир сыграем! А то тогда ничего не выгорело."

    show sl pioneer smile2
    show mi pioneer grin
    with dspr

    sl "Отличная идея!"
    mi "Да, мне тоже нравится!"
    me "Воу-воу, леди! Минуточку. {w}Я обеими руками за, но что это за игра такая? Я правил то не знаю!"

    show sl pioneer smile
    show mi pioneer smile
    show un pioneer smile
    with dspr

    sl "Покерные правила знаешь?"
    me "Знаю."
    th "А вот в том, что каждый пионер в СССР знал, как играть в покер, я очень сильно сомневался."

    show un pioneer smile2 with dspr

    un "Почти тоже самое. Открывай колоду, сейчас обьясним."

    play sound sfx_clocks fadein 0.5

    show black with clocks_in
    hide black with clocks_out

    stop sound fadeout 0.5

    "Спустя десяток минут, и парочку пробных разложенных раундов, я начал понимать, что к чему."
    th "Ну, не так уж и сложно."

    show mi pioneer serious with dspr

    mi "А как делиться то будем? Нас четверо, получается сетка начнется с полуфинала. И потом сражаются два финалиста."

    show sl pioneer normal
    show un pioneer normal
    with dspr

    "Все задумались. Как бы нам распределиться так, чтобы никому обидно не было?"

    show mi pioneer grin with dspr

    mi "Я придумала!"

    show sl pioneer smile
    show un pioneer smile
    with half_good_dspr

    sl "Ну! Не томи!"

    show mi pioneer smile with dspr

    mi "Значит смотрите!"
    mi "Сейчас все спорим на камень-ножницы-бумага. Кто проигрывает, тот закрывает глаза и начинает крутиться."
    mi "А все остальные бегают вокруг него в противоположную сторону."
    mi "В любой момент, тот, кто крутится, останавливается, и кричит «Стоп!»."
    mi "Я же сказала, что он крутится, показывая пальцем? Так вот."
    mi "Тот, на кого он указал, играет с ним. Остальные двое в другой группе."

    show mi pioneer shy with good_dspr

    mi "Как вам?"
    "Отличный способ, полностью зависящий от рандома!"

    show sl pioneer smile2
    show un pioneer smile2
    show mi pioneer normal
    with good_dspr

    sl "Здорово!"
    un "Отличная идея."
    me "Мне тоже нравится."

    show mi pioneer smile with dspr

    mi "Тогда…"
    "Она вытянула руку сжатую в кулаке."

    show sl pioneer smile
    show un pioneer smile
    with dspr

    "Мы тоже."
    mi "Цу-Е-Фа!"
    "..."
    "Первой вышла Лена, выбросив ножницы против всей нашей бумаги."

    show un pioneer smile2 with dspr

    "Я остался втроём со Славей и Мику."
    "..."
    "Но, не повезло. Я выкинул бумагу против камней девочек."
    th "Да-а. Лажа."

    show un pioneer smile with dspr

    me "Ну, что же, ха-ха, ладно. Значит мне крутиться."
    me "Если что, ловите меня."

    hide sl
    hide mi
    hide un
    show sl pioneer smile at fright
    show mi pioneer smile at fleft
    show un pioneer smile at center
    with half_good_dspr

    "Мы отошли от дерева."
    "Девочки встали вокруг меня, а я вытянул руку, и стал вращаться по часовой стрелке."

    show bg ext_beach_blur_sunset with dissolve1

    show sl pioneer smile at blurring
    show mi pioneer smile at blurring
    show un pioneer smile at blurring
    with half_good_dspr

    "Немного набрав темп, я выкрикнул."
    me "Стоп!"
    "И резко остановился."

    show sl pioneer smile at deblurring
    show mi pioneer smile at deblurring
    hide sl
    hide mi
    with good_dspr

    "Перед глазами всё плыло, но я увидел Лену, на которую показывал пальцем."
    "Немного пошатываясь, я набрал воздуха в грудь, и сказал."
    me "Значит нам с тобой играть."
    "Я выдохнул, и мир вновь стал преобретать чёткость."

    show bg ext_beach_sunset
    show un pioneer smile at deblurring
    hide un
    show sl pioneer smile at left
    show mi pioneer normal at right
    show un pioneer smile at center
    with dissolve1

    sl "А мы с Мику."

    show un pioneer smile2 with dspr

    un "Хорошо."
    "Мы вернулись к дереву."
    me "Я думаю, надо на чём-то разложиться. Просто на траве будет неудобно."

    show sl pioneer smile2
    show un pioneer shy
    with dspr

    sl "У меня есть с собой полотенце."
    un "И у меня."
    th "Она и полотенце с собой несла??"

    show mi pioneer grin with dspr


    mi "Отлично! Тогда приступим!"

    hide sl
    hide mi
    show cg d2_cards_scheme_basic
    with dissolve

    "Мы расселись по определившейся сетке. Я начал тасовать карты для себя и Лены, а Славя для себя и Мику."
    "Вскоре, игра началась."

    window hide

    jump simple_happiness_mod_d2_card_game_r1
    



# == КАРТОЧНАЯ ИГРА ДЕНЬ 2 ==
label simple_happiness_mod_d2_card_game_r1:
    python:
        difficulty = "easy"
        CARD_GAME_WITH_EXCHANGE = True

        dialogs = {
            (0, "win", "jump"): "d2_card_game_r1_me_win",
            (0, "fail", "jump"): "d2_card_game_r1_me_fail",
            (0, "draw", "jump"): "d2_card_game_r1_draw",
            (1, "rival_select", "call"): "d2_card_game_r1_midgame"
        }

        generate_cards("bg ext_beach_sunset", dialogs)
        rival = CardGameRivalUn(un_avatar_set, "Лена")
    
    $ game_starts_r1 = True

    call cards_gameloop

    return


label d2_card_game_r1_midgame:
    if game_starts_r1 == True:
        window show

        "Лена играла неплохо, но, кажется, у меня есть преимущество, которое я могу реализовать."

        window hide
    
    return


label d2_card_game_r1_me_win:
    show bg ext_beach_sunset

    $ game_starts_r1 = False

    show un pioneer normal at right
    with dspr

    window show

    "Я обыграл Лену."
    "Но мне показалось, что это было совсем не просто."
    me "Ты хороший соперник, Лена! Спасибо за игру."

    show un pioneer smile with dspr

    "Лена улыбнулась."
    un "И тебе. Давай посмотрим, как у Слави с Мику дела."

    show sl pioneer smile at fleft
    show mi pioneer smile at cleft
    with dspr

    "Мы посмотрели на их поле. Они уже доигрывали."
    sl "Всё, Мику, у нас ходы закончились. {w}Вскрываемся!"

    show un pioneer smile2 with dspr

    "Я засмеялся. Лена, кажется, тоже захихикала."

    show sl pioneer surprise
    show mi pioneer surprise
    with dspr

    sl "Что-о?"
    me "Да так. Шутку дурацкую вспомнил."

    show un pioneer smile
    show sl pioneer smile
    show mi pioneer normal
    with dspr

    "Судя по картам, Славя выиграла, но с небольшим отрывом."
    "У неё была пара Дам, у Мику пара Вальтов."

    show mi pioneer happy
    show sl pioneer smile2
    with dspr

    mi "И-и-ех! Чуть-чуть!"
    sl "Да, Микусь, было близко!"

    show sl pioneer smile
    show mi pioneer smile

    mi "Ну, что, теперь финал! Кто из вас победил?"
    "Она обратилась ко мне и Лене."
    
    show un pioneer shy with dspr

    un "Семён победил."
    "Я кивнул, улыбаясь."

    hide sl
    hide un
    hide mi
    show sl pioneer smile at cright
    show un pioneer normal at fleft
    show mi pioneer smile at cleft
    with dspr

    "Славя встала, и перешла ко мне, улыбнувшись. Лена и Мику сели рядом, с краю."
    sl "Ты готов принять своё поражение?"

    show cg d2_cards_scheme_r1_me_win with dissolve

    me "Не дождёшься! Играем!"
    "Я начал тасовать карты."

    window hide

    jump simple_happiness_mod_d2_card_game_r2


label d2_card_game_r1_me_fail:
    show bg ext_beach_sunset

    $ game_starts_r1 = False

    show un pioneer normal at right
    with dspr

    window show

    "Я проиграл. {w}Вот же блин!"
    "Сложно играть в игру, которую не ты придумал, и правила которой узнал 10 минут назад."
    me "Ты достойный соперник! Спасибо за игру."
    "Я улыбнулся."

    show un pioneer shy with dspr

    "Лена немного смутилась."
    un "Спасибо… Но вообще даже не знаю, как так получилось, что я победила. Я в картах не сильна."

    show sl pioneer smile2 at fleft
    show mi pioneer smile at cleft
    with dspr

    "Тем временем, Славя обыграла Мику."
    sl "Ура!"

    show mi pioneer grin with dspr

    mi "О-ха-ё! Славя, да ты мастер!"

    show sl pioneer shy with dspr

    sl "Спасибо! Хи-хи."

    show cg d2_cards_scheme_r1_un_win with dissolve

    "Теперь, в финале сойдутся Славя и Лена."
    "Лена перетасовала карты, и игра началась."
    "..."

    show black with clocks_in

    hide sl
    hide mi
    hide un
    hide cg
    show sl pioneer smile at fleft
    show un pioneer normal at cleft
    show mi pioneer normal at right
    hide black
    with clocks_out

    "Славя уверенно победила. У неё на руках оказалась тройка королей, Лена же собрала пару десяток."

    show un pioneer surprise
    show sl pioneer happy
    with dspr

    un "Ого! Вот это да."

    show un pioneer smile2 with dspr

    "Лена улыбнулась."
    un "Ты заслужила победу!"
    "Славя вся светилась от счастья. А я был безмерно рад просто тому факту, что радуется она."
    sl "Ихи-хи! Ура-а! Я даже не думала, что смогу победить."
    me "Поздравляю с победой!"

    jump simple_happiness_mod_day2_continue


label d2_card_game_r1_draw:
    show bg ext_beach_sunset

    pause(1.0)

    show un pioneer normal at center
    with dissolve

    window show

    "Мы сыграли в ничью."
    me "Не-е, так дело не пойдёт."

    show un pioneer smile with dspr

    un "Переиграем?"
    "Она посмотрела на поле Слави и Мику."
    un "Кажется, мы девочек не сильно задержим."
    me "Тогда чего же мы ждём?"

    call simple_happiness_mod_d2_card_game_r1


label simple_happiness_mod_d2_card_game_r2:
    python:
        difficulty = "normal"
        CARD_GAME_WITH_EXCHANGE = True

        dialogs = {
            (0, "win", "jump"): "d2_card_game_r2_me_win",
            (0, "fail", "jump"): "d2_card_game_r2_me_fail",
            (0, "draw", "jump"): "d2_card_game_r2_draw",
            (1, "rival_select", "call"): "d2_card_game_r2_endgame",
            (2, "rival_select", "call"): "d2_card_game_r2_midgame"
        }

        generate_cards("bg ext_beach_sunset", dialogs)
        rival = CardGameRivalUn(sl_avatar_set, "Славя")
    
    $ game_starts_r2 = True

    call cards_gameloop


label d2_card_game_r2_midgame:
    if game_starts_r2 == True:
        window show

        "Кажется, пока Славя играла с Мику, она неплохо разыгралась."

        window hide
    
    return


label d2_card_game_r2_endgame:
    if game_starts_r2 == True:
        window show

        "Игра подходила к концу, но сбавлять темп мы и не собирались."

        window hide
    
    return


label d2_card_game_r2_me_win:
    show bg ext_beach_sunset

    $ game_starts_r2 = False
    $ card_game_d2_win = True

    show cg d2_cards_scheme_r2_me_win
    with dissolve

    window show

    "Фух, это было непросто, но я выиграл!"

    hide cg
    show bg ext_beach_sunset
    show sl pioneer smile2 at center
    with dissolve

    sl "Ух ты какой! Узнал правила полчаса назад, и уделал нас всех!"

    show un pioneer smile at fright
    show mi pioneer grin at fleft
    with good_dspr

    un "Да, Семён, ты большой игрок!"
    mi "И как можно столько карт в голове держать, не понимаю!"
    "Я горделиво выпрямился, и выдал."
    me "Если я такой большой победитель, то где мой большой приз?"

    show un pioneer smile2
    show mi pioneer dontlike
    with dspr

    mi "Ну-у, началось! Бака, мы же не на призы играли!"

    show sl pioneer smile with dspr

    sl "Приз, говоришь?"

    hide sl
    show sl pioneer shy close at cright
    show mi pioneer normal
    show un pioneer smile
    with dspr

    stop music fadeout 1.5

    "Славя встала, обошла поле, и присела рядом со мной."
    $ renpy.pause(1.0, hard=True)

    play music music_list["forest_maiden"] fadein 2.0 volume 0.75

    "А дальше произошло то, от чего я расплылся в самой дурацкой улыбке, которую только видел этот лагерь, а щеки мои стали раскалённо красные, и казалось, сейчас сгорят."

    play sound sfx_head_heartbeat fadein 1.0 volume 0.8

    "Славя меня поцеловала. В щечку. {w}Но тем не менее! Сердце бешено заколотилось."

    show sl pioneer tender with dspr

    "Я посмотрел на Славю. А она смотрела на меня глазами, полными ожидания реакции и смущения одновременно."
    me "Славя… Вот это самый лучший подарок, который только можно было ожидать."

    show sl pioneer shy with dspr
    sl "Я рада, что тебе он понравился!"
    "Девочки всё это время сидели молча."

    show mi pioneer shy with dspr

    "Лишь только сейчас Мику выдала тихое."
    mi "Ё-ё-ё!"
    "Реакции Лены я не видел."

    jump simple_happiness_mod_day2_continue

label d2_card_game_r2_me_fail:
    show bg ext_beach_sunset

    $ game_starts_r2 = False

    show cg d2_cards_scheme_r2_sl_win
    with dissolve

    window show

    "Славя обыграла меня."
    "Я выдохнул, и откинулся назад, как после тяжелой катки за компом."

    hide cg
    hide bg
    hide sl
    show bg ext_beach_sunset
    show sl pioneer smile at center
    with dissolve

    me "Ну, ты картёжница! Где так научилась, признавайся!"

    show sl pioneer shy with dspr

    "Славя немного смутилась, но было видно, что она очень рада своей победе."
    sl "Ну, я с дедушкой много в карты играла."
    me "Ты заслужила эту победу, молодец!"

    show sl pioneer happy with dspr

    me "Но когда-нибудь, я обязательно потребую реванш!"
    sl "Я буду во всеоружии, будь уверен!"
    "Девочки тоже подключились к разговору."

    jump simple_happiness_mod_day2_continue


label d2_card_game_r2_draw:
    show bg ext_beach_sunset

    pause(1.0)

    show sl pioneer smile at center
    with dspr

    window show

    me "Как это? Ничья?"
    sl "Переигрываем!"
    me "Полностью поддерживаю!"
    mi "Конечно. Время ещё есть, а мы должны определить победителя сегодняшней встречи!"

    call simple_happiness_mod_d2_card_game_r2


# День 2 после карт
label simple_happiness_mod_day2_continue:
    show bg ext_beach_sunset

    $ renpy.block_rollback()
    stop music fadeout 2.5

    hide cg
    hide sl
    hide mi
    hide un
    show un pioneer normal at fleft
    show mi pioneer normal at cleft
    show sl pioneer smile at right
    with dissolve1

    "..."
    "Мы посидели ещё пару минут, обсуждая игру, а я всё переглядывался со Славей."

    play music music_list["two_glasses_of_melancholy"] fadein 2.0 volume 0.9

    th "Что же такое со мной делается?"
    me "Ладно, дамы. Вы меня извините, но мне нужно отойти буквально на пару минут."

    show mi pioneer smile with dspr

    mi "Ой, а я знаю! У нас это называется «придурить носик»! Хи-хи!"

    show sl pioneer laugh
    show un pioneer smile2
    show mi pioneer shy
    with dspr

    "Все засмеялись."
    me "Ха-ха, Мику. «Припудрить». Но нет, я не за этим ухожу."
    "Я замялся."
    me "Дым пустить…"

    show sl pioneer normal
    show un pioneer normal
    show mi pioneer dontlike
    with dspr

    mi "О-ха-ё! Вы посмотрите на него, он ещё и курит!"

    show un pioneer serious with dspr

    un "И где только парни берут здесь сигареты, не понимаю."

    show sl pioneer smile

    th "Ох, знала бы, ты, Леночка, {i}где{/i} и при {i}каких{/i} обстоятельствах я их достал."
    sl "Да ладно вам! Не на нас же ему дышать, в самом деле."

    hide sl
    hide un
    hide mi
    with long_dspr

    "Я кивнул, и отошел в сторонку, метров на десять, встал под дерево, и закурил сигарету."

    call smoking_process(with_pause=1.0)

    th "Интересно, а кто-нибудь тут кроме меня и Алисы вообще курит? По крайней мере, из тех, кого я знаю."

    queue sound sfx_smoking_cigaret

    "Я продолжил курить, думая обо всём подряд. И в том числе о Славе."

    show sl pioneer smile far at fright
    with good_dspr

    "Как тут подошла она."
    me "Славя? Что-то случилось?"

    hide sl
    show sl pioneer smile at right
    with good_dspr

    "Она подошла ближе."
    sl "Нет, я просто…"
    "Она на несколько секунд замялась, пытаясь, видимо, подобрать слова."

    show sl pioneer shy with dspr

    sl "Ну-у… Хотела попробовать. {w}Сигарету."

    pause(0.5)

    th "Вот те раз."
    me "А ты?.. Куришь?"

    show sl pioneer smile2 with dspr

    sl "Нет. Просто мне всегда было интересно попробовать. {w}У меня отец курит, и дедушка тоже. {w}У них спросить я не могу, а в лагере я ни с кем из мальчишек толком и не общаюсь."
    me "Ну-у… Держи."
    "Я передал уже уполовинчатую сигарету Славе."

    play sound sfx_smoking_cigaret volume 0.7

    "Она сделала пару неглубоких затяжек, и вернула мне."

    show sl pioneer surprise with dspr

    sl "Кхе-кхе."
    sl "Знаешь, а я думала это более… Невкусно. {w}Я ожидала, что будет очень сильно жечь, будто уголёк в рот положил. Но в этом что-то есть."
    me "Как бы то ни было… Я запрещаю тебе курить!"

    show sl pioneer happy with dspr

    "Славя рассмеялась."
    sl "Ты мне? Запрещаешь?"
    me "Да."
    "Как мог твёрдо ответил я."
    me "Это вредно. Я не хочу, чтобы ты вредила себе."

    show sl pioneer shy with dspr

    sl "Ну хорошо-о. Обещаю тебе, что никогда не буду курить!"
    "Я улыбнулся, и ответил."
    me "Вот и хорошо."
    "Я докурил сигарету, и кинув её под ноги, потушил носком обуви, и достал жвачку."
    me "Будешь?"

    show sl pioneer smile2 with dspr

    sl "Ой, давай! Спасибо большое!"
    me "Не стоит."

    window hide

    hide sl with dspr

    call set_time("night")

    show bg ext_beach_night
    show mi pioneer normal at fleft
    show un pioneer smile at left
    show sl pioneer smile at right
    with dissolve1

    "Мы вернулись обратно к Мику и Лене, которые уже сложили оба полотенца и собрали карты, и о чем-то болтали."
    th "А Лена, кажется, повеселела."

    show mi pioneer smile with dspr

    mi "Ой, а вот и вы! Ну что, ещё есть чем заняться, или уже пойдём? Уже поздно."
    "И правда, Солнце уже совсем скрылось, и на улице начали сгущаться сумерки."
    "Я наклонился, взял обе колоды, и отдал одну Славе."
    me "Если никто не возражает, я бы предпочёл вернуться. {w}К тому же Ольга Дмитриевна наказала нам вернуться до одиннадцати вечера."
    sl "Тогда действительно пойдёмте."
    "Лена также ответила положительно, и мы двинулись в сторону домиков…"

    stop ambience fadeout 1.0

    show black with clocks_in

    play ambience ambience_camp_center_night fadein 1.0

    hide mi
    hide sl
    hide un
    show bg ext_houses_night
    show un pioneer normal at fleft
    show mi pioneer normal at cleft
    show sl pioneer normal at right
    hide black
    with clocks_out

    "По пути мы обсуждали общие увлечения."
    "Оказалось, например, что Я, как и Славя, в разной степени увлечены садоводчеством, а Лена училась в музыкальной школе на духовые, и умеет играть на флейте."
    "Дойдя до развилки, мы со Славей попрощались с Леной и Мику, им надо было совсем в другую сторону."

    hide sl
    hide mi
    hide un
    show sl pioneer smile at cright
    with good_dspr

    me "Давай я тебя провожу прям до домика. А то поздно уже."

    show sl pioneer smile2 with dspr

    "Славя расплылась в улыбке."
    sl "Ой, Сёма, спасибо! Давай!"
    "Мы пошли к её домику."
    "..."

    stop music fadeout 0.5
    pause(0.5)
    play sound sfx_bush_leaves volume 1.2

    hide sl
    show sl pioneer scared close at right
    with dspr

    "Стоило нам зайти за поворот, как из кустов что-то шмыгнуло прямо на тропинку."
    "Я немного напрягся, а Славя так и вовсе, вцепилась мне в руку, и прижалась всем телом."
    "Я присмотрелся."
    "Этим чем-то оказалась белка."
    th "Уж не та ли самая, что я видел в пролеске?"

    stop music fadeout 2.0

    me "Всего лишь белочка."
    "Я улыбнулся."

    show cg d2_scared_by_squirel with dissolve

    play music music_list["forest_maiden"] fadein 2.0 volume 0.77

    sl "Да… {w}Но можно я не буду отпускать твою руку?"
    "Мне стало от этого приятно. То есть, она видит во мне защитника?"
    me "Конечно, можно, Славя."
    "Остаток пути до домика мы преодолели держась за руки."

    pause(1.0)

    hide sl
    hide cg
    show bg ext_house_of_sl_night
    show sl pioneer smile2 at cright
    with dissolve1

    sl "Вот мой домик, мы пришли."
    sl "Спасибо большое, что проводил!"
    me "Да что там, не стоит! Оставить такую девушку как ты, одну? Никак нельзя!"

    show sl pioneer tender with dspr

    "Славя, кажется, готова была растаять."
    sl "Сё-ема! Какой же ты милый!"

    hide sl
    show sl pioneer shy close at center
    with good_dspr

    "Она обняла меня."
    "Я ответил, также обняв Славю за плечи. Сейчас руки не стоило опускать даже на талию. Это было не нужно."
    "Мы простояли, обнимаясь, секунд пять, после чего Славя сказала."

    show sl pioneer smile2 with dspr

    sl "До завтра?"
    me "До завтра."

    hide sl
    show sl pioneer shy
    with half_good_dspr

    "Мы разъединили объятие."
    sl "Спокойной ночи, Семён."
    me "И тебе спокойной ночи."

    hide sl
    show sl pioneer smile2 far at center
    with long_dspr

    "Славя поднялась на ступеньки, и открыв дверь, обернулась на меня."

    hide sl with good_dspr

    "Только после этого она зашла в домик."
    "А я ещё несколько секунд стоял, переполняемый непонятным чувством."
    "..."
    th "Пора {i}домой{/i}."

    stop music fadeout 2.0

    show black with clocks_in
    show bg ext_house_of_mt_night_without_light
    hide black
    with clocks_out

    play music music_list["goodbye_home_shores"] fadein 2.0 volume 0.75

    "Сделав несколько поворотов, я оказался перед нашим с вожатой домиком."
    "Свет был выключен."

    stop ambience fadeout 1.0

    show bg int_house_of_mt_night2 with dissolve

    play ambience ambience_int_cabin_night fadein 1.0

    "Я тихонько открыл дверь, зашёл внутрь и повернул ключ."
    "Но, вожатая, кажется, спала очень чутко, потому как я разглядел шевеление под одеялом."
    mt "Семён? {w}Вернулся?"
    me "Да, все вернулись. {w}Без происшествий."
    mt "Хорошо. {w}А то я х… {w}т…"
    "Договорить она не успела, так как опять уснула."
    "Я улыбнулся, тихо разделся и лег в кровать."

    stop music fadeout 2.0

    show cg sleep_nothingness with dissolve

    call to_nvl_mode

    play music music_list["meet_me_there"] fadein 2.0 volume 0.65

    "..."
    "И так. За сегодня много чего произошло. Но ничего не могло меня приблизить к разгадке того, как я сюда попал."
    "Да пытался ли я вообще искать какие-то ответы, или просто принял новую реальность?"
    ths "А где их тут найдешь, ответы то."
    "От местных обитателей явно ничего не добиться. А сбегать?"
    "И куда я пойду? Выживать в дикой природе я не умею, куда идти не знаю."
    "Хотелось бы конечно вернуться… В {b}{i}свой{/b}{/i} мир? Там всё знакомо."
    "Но должна же эта смена рано или поздно закончиться? Вожатая говорила, что это последняя неделя."
    "А если я в этом мире навсегда? Вот уеду на автобусе, и что?"
    "Без родных, без документов, в чужом городе."
    nvl clear
    ths "Ай, к чёрту."
    "Я понял, что лучше решать вопросы по мере их поступления. До сих пор это получалось довольно хорошо. А пока просто буду наслаждаться внеплановым «отпуском»."
    "..."
    "И Славя… {w}Что же между нами происходит? Я накручиваю себе что-то, или…"
    "Я боялся даже подумать это слово. Больно колол первый и единственный опыт."

    stop music fadeout 2.0

    nvl clear
    "Постепенно я начал засыпать."
    "А мысли так и продолжили крутиться вокруг девушки с золотыми волосами и глазами голубого цвета, как самое чистое на свете море. {w}В которых хотелось утонуть."

    stop ambience fadeout 1.0

    jump simple_happiness_mod_day3


# День 3
label simple_happiness_mod_day3:
    $ renpy.block_rollback()
    $ backdrop = "days"
    $ new_chapter(3, u"Простое Счастье. День 3")

    call set_time

    $ set_mode_adv()

    play ambience ambience_int_cabin_day fadein 1.0

    "Спал я, как убитый."
    "Мне даже ничего не снилось."
    "Сказывалась вчерашняя беготня и поздний отбой."
    th "Вставать, что-ли?"

    show bg int_house_of_mt_day
    show mt nightdress normal at fright
    with dissolve2

    play music music_list["dance_of_fireflies"] fadein 3.5 volume 0.9

    "Я открыл глаза."
    "По домику уже ходила вожатая в халате."
    me "Доброе утро, Ольга Дмитриевна."
    mt "О, Семён, проснулся? А я только хотела тебя будить. Кофе будешь?"
    me "А у вас кофе есть? И вы всё это время скрывали его от меня?"
    "Мысль о чашке горячего напитка сразу приободрила меня."

    show mt nightdress grin with dspr

    "Вожатая улыбнулась."
    mt "А ты не спрашивал. Одевайся, сейчас налью."

    show mt nightdress normal with dspr

    "Оставаясь под одеялом, я одел рубашку, и быстро шмыгнул в шорты."

    hide mt
    show mt nightdress normal at cright
    with good_dspr

    "После чего заправил постель, и сел на стул возле стола. На нём уже стояли две чашки кофе, исходившие паром."
    "Сделав аккуратный глоток, я довольно чавкнул и откинулся на спинку."
    "Ольга Дмитриевна тоже отпила кофе, и посмотрела на меня."

    show mt nightdress sad with dspr

    mt "Семён… Тут вчера вечером на подоконнике колода карт лежала. Ты не видел?"

    stop music fadeout 1.0
    pause(1.0)
    play music music_list["always_ready"] fadein 1.0

    th "Оп-па…"
    "Я остолбенел."
    th "А про карты то и забыл совсем!"
    "Они всё ещё лежали у меня в кармане."
    me "Нет, я не видел. А что, не можете найти?"
    mt "Да вторую колоду уже за неделю теряю… {w}Точно не видел?"
    me "Точно-точно, честное пионерское!"
    "Я понадеялся, что советская риторика подействует."

    show mt nightdress normal with dspr

    mt "Хм, может у Виолы оставила, или упали куда… Ну ладно."
    th "Так она вечерами к медсестре ходит? И что они там, интересно, делают?"

    stop music fadeout 2.0

    "Я не стал ничего отвечать, и мы продолжили пить кофе. Кажется, меня пронесло. По крайней мере в этот раз."
    "..."

    play music music_list["everyday_theme"] fadein 2.0 volume 0.9

    hide mt
    show mt nightdress normal at right
    with half_good_dspr

    "Когда обе наши чашки закончились, Ольга Дмитриевна встала."
    mt "Семён, ты же уже одетый и готовый? Выйди, пожалуйста, на улицу, я переоденусь."
    mt "И в целом, можешь уже идти на завтрак, до него двадцать минут. Кружки я сама помою."
    me "Хорошо. До встречи на линейке!"

    stop ambience fadeout 1.0

    hide mt
    show bg ext_house_of_mt_day
    with dissolve

    play ambience ambience_camp_center_day fadein 1.0

    "Я вышел из домика."
    "Двадцать минут… До столовой идти минуты три. Ну, пять, если плестись."
    "Ладно, пройду через туалет…"

    play sound sfx_clocks fadein 0.5

    show black with clocks_in

    show bg ext_dining_hall_near_day
    hide black with clocks_out

    stop sound fadeout 0.5

    "Не торопясь, как только возможно, минут через пятнадцать я стоял перед столовой, в которую уже начали заходить пионеры."

    stop ambience fadeout 1.0

    show bg int_dining_hall_people_day with dissolve

    play ambience ambience_dining_hall_full fadein 1.0

    "Никого из знакомых я не увидел, так что сразу зашел в столовую, получил порцию, и занял своё место…"
    "Столовая всё больше заполнялась пионерами, а я сидел за столом один, и потихоньку жевал кашу, по всей видимости «Геркулес»."
    "Хотя жевать там было решительно нечего."
    dvp "Тут свободно?"

    show dv pioneer normal far at fleft
    with good_dspr

    "Подняв взгляд, я увидел приближающуюся с подносом Алису."

    hide dv
    show dv pioneer normal at right
    with dspr

    "Не дожидаясь ответа, она села напротив меня."

    dv "Приятного аппетита."
    me "И тебе!"
    dv "Есть планы на день?"
    me "Ну-у, клуб. {w}Я же теперь с Мику в музыкальном кружке."

    show dv pioneer smile with dspr

    dv "Ну и зря."
    me "Чой-то?"
    dv "Так сегодня же танцы. Придется аппаратуру таскать из клуба."

    show dv pioneer laugh with dspr

    "Она ехидно улыбнулась."
    me "Танцы? Какие танцы, где?"

    show dv pioneer smile with dspr

    dv "Ну ты как с Луны свалился. Обычные танцы, на площади!"
    th "Ах, это те самые, общие для всех школ и лагерей тусовки без грамма тусовки?"

    show sl pioneer smile at fleft
    with good_dspr

    sl "Утро доброе! Что обсуждаете?"
    "Перед нами появилась Славя."
    "Я улыбнулся, и сказал."
    me "Славя, утречка! Садись пожалуйста!"

    hide sl
    show sl pioneer smile at cleft
    with half_good_dspr

    "Алиса тоже поприветствовала Славю, и она села рядом со мной."
    me "Алиса рассказывает, что сегодня на площади будут танцы."

    show sl pioneer smile2 with dspr

    sl "Всё таки сегодня, да? {w}Значит надо будет всё подготовить к вечеру. {w}Блин, и платье!"
    me "Ё-моё, там ещё и дресс-код будет?"

    show sl pioneer smile with dspr

    sl "Ну конечно! Мальчики обычно просто в форме, вы редко с собой что-то ещё берёте, помимо того, в чём приехали. {w}Но все девочки будут в платьях, я уверена."

    show dv pioneer grin with dspr

    dv "Вот ещё! Я даже не знаю, пойду ли."

    show sl pioneer laugh with dspr

    "Славя посмеялась."
    sl "Ну! {w}В тебе, Алиса, я и не сомневалась!"
    dv "А то!"
    "Мы продолжили есть, обсуждая вечер."
    "..."

    stop ambience fadeout 1.0
    stop music fadeout 3.0

    hide dv
    hide sl
    show bg ext_dining_hall_near_day
    show sl pioneer normal at right
    with dissolve1

    play ambience ambience_camp_center_day fadein 1.0

    "Мы со Славей вышли из столовой вдвоём, так как Алиса кого-то ждала."

    play music music_list["get_to_know_me_better"] fadein 2.0 volume 0.9

    show sl pioneer smile2 with dspr

    sl "Семён… {w}А ты же пойдешь?"
    "Я понял, к чему она клонит."
    me "Конечно пойду! Пойду, и обязательно тебя приглашу!"

    show sl pioneer shy with dspr

    "Славя растаяла в улыбке."
    sl "О-ой. Здорово. Тогда точно надо будет подготовиться!"
    me "Ты и, если мешок из-под картошки оденешь, будешь самая красивая."

    show sl pioneer laugh with half_good_dspr

    "Славя рассмеялась."
    sl "Как Мерлин Монро?"
    me "Ага."
    "Я улыбнулся в ответ."

    show sl pioneer smile2 with dspr

    sl "Но мешок я всё таки на себя лучше одевать не буду, хи-хи."
    sl "Пойдем на линейку, а то опоздаем."

    show sl pioneer smile with dspr

    me "Пойдём."
    "Мы пошли в сторону площади."
    "..."

    stop music fadeout 2.0

    hide sl
    show bg ext_square_day
    show sl pioneer smile at right
    with dissolve2

    play music music_list["my_daily_life"] fadein 2.0 volume 0.75

    "Мы вышли на площадь. Некоторые из наших уже стояли, но вожатой всё ещё не было."
    "Стоило нам встать на свои места, как через пару минут подтянулись оставшиеся из нашего отряда, а за ними и вожатая."

    hide sl
    show cg d2_lineup
    with dissolve

    "Она начала линейку."
    "Вожатая подтвердила, что сегодня вечером, через полчаса после ужина на площади будут танцы."
    "А для проведения мероприятия нужно будет подготовить аппаратуру, принести её на площадь, и убраться на самой площади."
    mt "Мику, ответственная за чистую аппаратуру и доставленную сюда в целости и сохранности."
    mt "Славя, за площадь."
    mt "Возьмите людей себе в помощь. {w}Ну… Вроде всё. Разойдись."

    hide cg
    show mt pioneer normal panama at right
    with dissolve

    th "Хотелось помочь Славе, но не бросать же Мику. Мы с ней в одном клубе, всё-таки."

    show mi pioneer normal at cleft
    with good_dspr

    "Только успел я закончить мысль, как подошла Мику."

    show mi pioneer grin with dspr
    pause(1.5)
    show mi pioneer happy with dspr
    pause(1.0)

    hide mi
    show mi pioneer normal at center
    with good_dspr

    "Она посмотрела на меня, подмигнула и обратилась к вожатой."
    mi "Ольга Дмитриевна! Я могу отпустить Семёна, мы с ним вчера в клубе убирались, вся аппаратура чистая!"
    mi "Пусть лучше останется на площади, руководит процессом со Славей."

    show mt pioneer surprise panama with dspr

    mt "Вы вчера убраться успели? Семён?"
    "Я подошёл."
    me "Да, музыкальный кружок сверкает!"

    show mt pioneer smile panama with dspr

    mt "Ну что ж, хвалю!"

    show mi pioneer smile with dspr

    mt "Тогда действуйте до обеда по обстоятельствам. Так что, Семён, можешь остаться здесь, и помочь Славе, если хочешь."
    me "Спасибо."

    show mt pioneer smile panama at walk_away_right
    pause(0.5)
    hide mt with dspr

    "Вожатая ушла, и я обратился к Мику."
    me "Спасибо, Мику! Э-э…"
    me "То есть, ну, тебе точно помощь не нужна?"

    show mi pioneer grin with dspr
    pause(0.5)
    show mi pioneer smile with dspr

    "Мику интересно улыбнулась, и ответила."
    mi "Нет, правда-правда! Всё равно аппаратуру не понесём, пока на площади не будет убрано. Так что, занимайтесь."
    me "Ещё раз спасибо."

    hide mi
    show sl pioneer smile at cright
    with long_dspr

    "Мы разошлись с Мику, и я подошёл к Славе, которая всё это время наблюдала за происходящим."
    sl "Семён, ты со мной останешься?"
    me "Да, со стороны музыкального клуба уже всё сделано."

    show sl pioneer smile2 with dspr

    sl "Ой, здорово! Тогда вместе больше в..."

    show sl pioneer shy with dspr

    sl "Быстрее закончим, вот..."
    th "Она хотела сказать «вместе больше времени проведём»!?"
    "Я, не зная, как мне реагировать, ответил."
    me "Да, это правда. Больше... {w}Быстрее закончим с уборкой."

    show sl pioneer smile2 with dspr

    "Славя улыбнулась."
    sl "Тогда я сейчас обращусь к вожатому более младшего отряда, чтобы выделил нам пионерию."
    
    show sl pioneer smile with dspr

    sl "А ты пока, вот."

    play sound sfx_keys_rattle

    "Она брякнула ключами."
    sl "Возьмёшь инвентарь? Только веники, по идее. Штук пять."
    me "Есть, мэм!"

    show sl pioneer laugh with dspr

    "Я вытянулся по струнке, а Славя засмеялась."
    sl "Ха-ха, вольно, солдат. Шагом марш выполнять задание!"

    hide sl with good_dspr

    call to_nvl_mode

    "Я взял у Слави ключи, и направился в сторону склада, не забыв, конечно, там покурить."
    "Не сразу я понял, что хозяйственный инвентарь лежит не на самом складе, а в пристройке рядом, так что немного задержался."
    "Вернувшись с охапкой веников под мышкой, я застал Славю, которая уже стояла перед тремя пионерами помладше, на вид им было лет 10-12."
    "Я раздал им уборочный инвентарь, Славя распределила их на зоны, и мы приступили к уборке."
    "Мы со Славей тоже взяли по метле, и принялись за самую ответственную зону возле памятника, и постоянно о чём-то разговаривали."
    "Не смотря на нелюбимую мной физическую работу, связанную с уборкой территории, я был рад просто находиться рядом, работать и общаться со Славей."
    "..."
    "Примерно через полтора часа и пару перерывов, уборка была закончена."
    "Мы отпустили «молодежь» и направились к складу, продолжая разговаривать. Предметом обсуждения стало садоводство."

    call to_adv_mode

    show sl pioneer smile at right
    with good_dspr

    sl "Я вот всё думаю, Семён, как же так получилось, что парень так хорошо разбирается в растениях?"
    me "Да как-то знаешь… Полюбилось однажды, просто. Да и потом, в центральной России климат мягкий, так что заниматься садоводством просто."

    show sl pioneer surprise with dspr

    sl "О-о, так ты из центра?"

    show sl pioneer smile with dspr

    me "Да. Санкт-Петербург. А ты?"

    hide sl
    show bg ext_storage_day
    show sl pioneer smile2 at right
    with dissolve

    sl "А я из Сибири."

    show sl pioneer smile with dspr

    sl "Вообще, родом из небольшой деревни под Новосибирском, но в институт планировала поступать там."
    "В сердце больно кольнуло, но я не подал виду."
    th "Что же произойдёт после смены? Мы больше никогда не увидимся?"
    me "Сибирь? Ух, холодно там, наверное. А на кого поступать хотела?"

    show sl pioneer smile2 with dspr

    sl "Агроном."
    me "Здорово! Ну, судя по всему ты уже много знаешь."

    show sl pioneer smile with dspr

    sl "Да. Нравится мне это дело. Кстати, мы пришли."
    "Я огляделся."
    me "О, ха-ха, точно!"
    "Я и не заметил, что мы уже как пару минут стоим перед складами."
    "Я открыл дверь, и мы сложили весь инвентарь, после чего вышли из склада."
    me "Есть планы, чем заняться до обеда?"

    show sl pioneer shy with half_good_dspr

    sl "Ну, вообще… {w}Если ты хочешь ещё мне помочь…"
    me "Я всегда за!"

    show sl pioneer smile2 with dspr

    sl "Тогда я хотела заняться цветами на площади."
    sl "День обещает быть жарким, их надо полить, убрать сорняки."
    sl "Цветов там не так много, так что за час управимся."
    me "Тогда вперёд!"

    show sl pioneer smile with dspr

    "Мы взяли с собой всё необходимое, и вернулись на площадь…"

    show black with clocks_in

    hide sl
    show bg ext_square_day
    show sl pioneer smile at right
    hide black
    with clocks_out

    "На площади мы увидели, что по ней бегает несколько пионеров помладше. Среди них была Ульяна."
    "Когда мы подошли ближе, я крикнул."

    stop music fadeout 1.0

    me "Ульяна! Подойди сюда!"

    play music music_list["i_want_to_play"] fadein 1.0

    "Она обернулась, и подбежала к нам."

    show us sport laugh at left
    with dspr

    us "Слушаю, грж-нин начальник!"
    me "Будешь нам помогать."

    show us sport dontlike with dspr

    us "Ну-у! Я играла!"
    me "Баранки гну. Танцевать сегодня будут все, так что все должны приложить усилия."
    me "А мы ответственные за площадь, и нам нужна помощь. Тут ненадолго."

    show us sport grin with dspr

    us "А что я получу взамен?"
    me "А помочь своим товарищам на безвозмездной основе ты не хочешь?"
    us "Бевзм… Как ты там сказал, в рот, короче не положишь!"
    me "Ну ты… Ладно. Жвачку будешь?"
    us "Буду!"
    me "Получишь, когда всё сделаем."

    show us sport laugh2 with dspr

    us "Вот так нра-аица! {w}Готов к труду и обороне!"
    me "Вот и здорово."
    "Славя всё это время лишь молча наблюдала за нашим диалогом, и улыбалась."

    hide sl
    hide us
    show us sport normal at left
    show sl pioneer smile at right
    with long_dspr

    "Мы подошли к клумбе с цветами, и я объяснил Ульяне, что ей надо будет собирать вырванные нами сорняки в ведро, и подносить воду."
    me "Лейка маленькая, всего лишь литр."

    show us sport smile with dspr

    us "А мне и два не тяжело будет!"

    show sl pioneer smile2 with dspr

    sl "Главное не перенапрягайся. Если будет тяжело, Сёма за тебя сделает."
    me "Ну конечно, не эксплуатировать же ребёнка."
    us "Я опять не поняла, что ты сказал, но поддерживаю!"

    show us sport laugh
    show sl pioneer laugh
    with good_dspr

    stop music fadeout 2.0

    "Мы посмеялись, и принялись за дело."
    "..."

    hide us
    hide sl
    show us sport normal at left
    show sl pioneer smile at right
    with long_dspr

    play music music_list["she_is_kind"] fadein 2.0 volume 0.85

    "Меньше чем через час, благодаря помощи Ульяны, всё было сделано."
    me "Вот, держи, как договаривались."
    "Я достал одну пластинку жвачки, и отдал ей."

    show us sport laugh with dspr

    us "Спасибо!"

    show us sport laugh at run_away_left
    pause(0.5)
    hide us

    "Она тут же запихала её в рот, и убежала."
    me "Фух, ну что, я думаю, после обеда мы с тобой заслужили небольшой отдых, что скажешь?"
    sl "Это верно. Вон сколько до обеда сделали!"

    show sl pioneer smile2 with dspr

    "Она потянулась, и обвела руками нашу работу."
    me "Только сейчас опять придётся идти на склад, убирать инвентарь. Блин, и почему у нас нет велосипедов?"
    sl "А ты умеешь кататься?"
    me "Ну-у… Конечно."
    "Вопрос мне показался странным. Кто в таком возрасте хотя бы примерно не умеет держать равновесие и крутить педали?"
    sl "А я нет."

    show sl pioneer shy with dspr

    "Она смутилась."
    sl "У меня когда то в детстве был только четырёхколёсный. А на обычном я не училась."
    me "Хм. {w}А в лагере вообще есть велосипед, хоть один?"

    show sl pioneer smile with dspr

    "Славя задумалась."
    sl "Ну вроде перед домиком Ольги Дмитриевны стоит какой-то, а что?"
    th "И правда, а я и не обращал внимания."
    me "Тогда после дневного отдыха будем учиться кататься!"

    show sl pioneer surprise with dspr

    "Славя ни то удивилась, ни то испугалась."
    sl "Семён, но… Но как? А где? Ты научишь?"
    me "Да прям тут, на площади! У вожатой я разрешение спрошу."

    show sl pioneer happy with dspr

    sl "Ой ну… Давай, я за! Только тогда платье надо будет заранее подготовить к вечеру."
    "Я улыбнулся."
    me "Вот и договорились."
    me "Ну, пойдем, отнесём инвентарь. В последний раз, за сегодня, я надеюсь."

    show black with clocks_in

    hide sl
    show bg ext_storage_day
    show sl pioneer surprise at cright
    hide black
    with clocks_out

    play sound sfx_dinner_horn_processed

    "Уже закрыв дверь склада, мы услышали горн."

    play sound sfx_keys_rattle

    "Я передал Славе ключи, и мы поспешили в столовую."

    show black with clocks_in

    hide sl
    show bg ext_dining_hall_near_day
    show sl pioneer smile at cleft
    show mt pioneer normal at right
    hide black
    with clocks_out

    "Подходя к столовой, мы увидели перед собой Ольгу Дмитриевну."

    show mt pioneer smile with dspr

    mt "Славя, Семён! На площади невероятная чистота! И клумбой, я смотрю, успели заняться."
    mt "И как вы успели её так отдраить за пол дня?"

    show sl pioneer smile2 with good_dspr

    sl "Это Семёну спасибо, он много помогал."
    me "Мы вместе хорошо постарались."

    show sl pioneer smile
    show mt pioneer grin
    with dspr

    mt "Это правда. Вы большие молодцы, пионеры, хвалю!"
    
    show mt pioneer smile with dspr

    mt "Не просто выполнили поставленную задачу, а перевыполнили!"
    mt "После обеда можете отдыхать."

    show sl pioneer happy with dspr
    
    sl "Спасибо, Ольга Дмитриевна!"
    mt "Ну идите кушать."

    stop ambience fadeout 1.0

    hide sl
    hide mt
    show bg int_dining_hall_people_day
    show mi pioneer normal at fleft
    show sl pioneer normal at cright
    with dissolve

    play ambience ambience_dining_hall_full fadein 1.0

    "Мы зашли в столовую, взяли свои порции, и сели за стол к Мику."

    show mi pioneer smile with dspr

    mi "А-а, ребята! Вожатая говорит, вы там чуть ли не генеральную уборку на площади забабахали!"

    show sl pioneer smile2 with dspr

    sl "Да, так что на танцах всё будет замечательно и красиво!"
    me "Кстати, Мику."

    show mi pioneer normal
    show sl pioneer smile
    with good_dspr

    me "Тебе же ещё помощь с аппаратурой нужна будет?"

    show mi pioneer happy with dspr

    mi "Нет-нет! Да и вожатая сказала, что вы отдыхаете после обеда."

    show mi pioneer normal with dspr

    mi "Кибрек… {w}Киберк…"

    show mi pioneer shy
    show sl pioneer smile2
    with dspr

    "Она пыталась выговорить слово."
    sl "Ки-бер-не-ти-ки. {w}Ты же про них?"

    show mi pioneer smile with dspr

    mi "Точно! Они часть унесут, им всё равно ещё провода подключать."
    mi "А остальной частью другие отряды займутся, вожатая уже договорилась."
    me "Во-от! Это здорово."
    sl "Тогда после отдыха точно будешь меня учить, Сёма!"

    show mi pioneer surprise
    show sl pioneer laugh
    with good_dspr

    mi "Чему учить?"
    "Я улыбнулся."
    me "На велосипеде кататься."

    show mi pioneer grin
    show sl pioneer smile
    with dspr

    mi "А-а-а! А у моего отца тоже есть велосипед. Но он странный какой-то, с большими колёсами! Но он всё равно больше на машине ездит…"
    "Мы продолжили кушать и разговаривать."

    stop ambience fadeout 1.0
    stop music fadeout 2.5

    hide mi
    hide sl
    show bg ext_dining_hall_near_day
    show sl pioneer smile at right
    with dissolve1

    play ambience ambience_camp_center_day fadein 1.0

    "Выйдя из столовой, мы попрощались с Мику, и вместе со Славей направились в сторону домиков."

    play music music_list["so_good_to_be_careless"] fadein 2.0

    "..."

    hide sl
    show bg ext_houses_day
    show sl pioneer smile at cright
    with dissolve1

    sl "Не забудь у Ольги Дмитриевны спросить разрешение велосипед взять, а то по шапке получишь."

    show sl pioneer laugh with dspr

    "Славя рассмеялась."
    me "Не забуду. Ну что, через два часа встречаемся на площади?"
    
    show sl pioneer smile2 with dspr

    sl "Да. Без железного коня не приходи!"
    "Мы попрощались, и я направился в сторону своего домика."

    hide sl
    show bg ext_house_of_mt_day
    with dissolve

    th "И правда, вот он стоит, велосипед. {w}Жёлтого цвета двадцатого века."
    "Интересно, вожатая уже в домике?"

    play sound sfx_knock_door7_polite

    "Я постучался."
    mt "Да, заходите."

    stop ambience fadeout 1.0

    show bg int_house_of_mt_day
    show mt pioneer smile at right
    with dissolve

    play ambience ambience_int_cabin_day fadein 1.0

    mt "Семён. Ну что, будешь просто отдыхать до ужина, или чем-то займешься?"
    me "Именно об этом я и хотел с вами поговорить!"

    show mt pioneer grin with dspr

    mt "Надо же, как интересно. Ну выкладывай, что ты затеял?"
    me "Выяснилось, что Славя не умеет ездить на велосипеде. Вот, будем учить, так сказать. Только нам велосипед нужен."

    show mt pioneer surprise with dspr

    mt "Ого как. Ну, перед нашим домиком стоит, возьми. {w}Только я даже не знаю, на ходу ли он."
    me "А это не ваш?"

    show mt pioneer smile with dspr

    "Вожатая улыбнулась."
    mt "Да откуда бы моему велосипеду тут взяться?"
    mt "Стоял ещё когда я только приехала на смену. Так что владелец либо не здесь, либо ему вообще на него всё равно."
    mt "В любом случае, кто бы это ни был, я думаю он не обидится."
    me "Хорошо, спасибо, Ольга Дмитриевна."

    show mt pioneer grin with dspr

    mt "Да не за что."

    show mt pioneer smile with dspr

    mt "Я через час где-то уйду, так что, смотри, не проспи до вечера. {w}Или может тебя разбудить?"
    me "Не стоит, я сам проснусь."
    mt "Ну, как знаешь. Если что, я на крыльце, в гамаке и с книжкой в руке."
    me "Хорошо."
    "Я оценил рифму, но комментировать не стал."

    show mt pioneer smile at walk_away_right
    pause(0.5)
    hide mt with long_dspr

    "Вместо этого лёг в кровать, дождался пока вожатая выйдет, и завел в телефоне таймер на полтора часа."

    stop music fadeout 2.0
    pause(1.0)
    play sound sfx_clocks fadein 0.25

    show black with clocks_in
    pause(0.5)
    hide black with clocks_out

    stop sound fadeout 0.25
    queue sound sfx_knock_door7_polite volume 0.75

    "Проснулся я не от будильника, как предполагал, а от стука в дверь."
    me "Войдите."
    "Я, всё ещё немного сонный, опёрся на локти, и посмотрел на входную дверь."

    show un pioneer shy far at fright
    with long_dspr

    un "Ой, Сёма, привет. {w}А ты не знаешь, где Ольга Дмитриевна?"
    me "Нет. Она ушла куда-то до того, как я уснул. {w}Может с другими вожатыми где-то? А что такое?"
    un "Да я медсестре помогаю в медпункте… {w}Она хотела её видеть."
    th "Вот как! Так что-то между вожатой и медсестрой всё-таки не чисто!"
    me "Не, Лен, извини, не знаю."

    show un pioneer smile with dspr

    un "Да ничего страшного. Извини, что разбудила."
    me "Не стоит. Всё равно, наверное, уже пора бы мне вставать."
    un "Хорошо, тогда до вечера."
    me "До вечера."

    pause(0.5)
    show un pioneer smile at walk_away_right
    pause(0.5)
    hide un with dspr

    "Когда Лена вышла, я достал телефон, и посмотрел на экран. До срабатывания таймера оставалось пять с половиной минут."
    th "Может, даже хорошо, что Лена зашла. Зато точно проснулся."
    "Я выключил таймер, не спеша встал, обулся, выпил воды из чайника, и вышел на улицу."

    play music music_list["went_fishing_caught_a_girl"] fadein 3.0 volume 0.9
    stop ambience fadeout 1.0

    show bg ext_house_of_mt_day with dissolve

    "Я вышел из домика, и сразу свернул за угол, скурить сигарету."

    play ambience ambience_camp_center_day fadein 1.0

    call smoking_process

    "После сна от курения приятно расслабило, и даже на минуту немного покачивало."
    "Я докурил, и зажевав жвачку, подошёл к велосипеду."
    th "Хм, вроде целый."
    "Я поднял его за руль и сиденье, и вытащил на тропинку."
    "Руль крутится. Я покатал его взад-вперёд. Колёса тоже."
    "Я поднял заднее колесо и нажал на педаль. Педаль с некоторым усилием, но всё же провернулась."
    th "Жаль, конечно, тормоз педальный. Но вроде должен ехать."
    "Я примерился, сел. И оттолкнувшись, проехал метров двадцать в сторону площади, после чего остановился."
    "«Хорошо» - заключил я. Ехать можно."
    "Я встал, сразу установил сидушку пониже, так как Славя была ниже, и покатил велосипед на площадь."

    show bg ext_square_day with dissolve1

    "Я выкатил велосипед на площадь, и не увидев Слави, подошел к скамейке, поставил велосипед рядом, и сел на неё."

    show black with clocks_in
    pause(1.0)

    show sl pioneer smile far at right
    hide black
    with clocks_out

    "Вскоре  я увидел подходящую Славю."
    sl "Сёма, привет ещё раз!"

    hide sl
    show sl pioneer smile2 at right
    with good_dspr

    sl "Долго ждёшь? Прости. Проспала долго, а ещё надо было платье подготовить."
    "Я встал и улыбнулся."
    me "Да ничего, пару минут."
    sl "Ну что, Ольга Дмитриевна дала добро?"
    me "Да, сказала можно взять."

    show sl pioneer normal with dspr

    sl "Начнем?"

    stop music fadeout 2.0

    pause(1.0)

    show sl pioneer smile with dspr

    "Я упёр руки в бока и ответил."

    play music music_list["always_ready"] fadein 2.0 volume 0.85

    me "Да!"

    call to_nvl_mode

    "Я выкатил велосипед, и сперва, показал Славе, как садиться, как трогаться, как тормозить."
    "И примерно объяснил, как держать равновесие, чувствуя велосипед."
    "Сделал небольшой круг, показав, как всё это делать на практике."

    call to_adv_mode

    show sl pioneer smile2 with dspr

    sl "Ой, что-то у меня уже голова кружится!"
    "Девушка рассмеялась."
    me "Это так кажется, на самом деле ничего страшного."
    
    show sl pioneer smile with dspr

    me "Садись, попробуем! Я буду придерживать."

    call to_nvl_mode

    "Славя села на велосипед, взялась за руль, и неуверенно поставила ногу на педаль."
    "Я встал с краю, взялся одной рукой за руль, другой за талию девушки, чтобы придерживать её."
    me_n "Теперь, попробуй просто оттолкнуться ногой, и прокатиться по инерции, педали не крути."
    sl_n "Хорошо…"
    "Славя оттолкнулась правой ногой, которая не стояла на педали, и тихонько покатилась. Я шёл рядом, и придерживал её."
    me_n "Вот, отлично! А теперь поставь вторую ногу на педаль, и нажми их назад, чтобы остановиться."
    "Неуверенными движениями Славя поставила вторую ногу, и надавила назад, чтобы остановить велосипед."
    "Получилось хорошо. Она даже остановилась плавно, и выставила ногу, чтобы не упасть."

    call to_adv_mode

    show sl pioneer happy with dspr

    sl "Получилось! Я прокатилась!"
    "Её лицо сверкало от радости."
    "Я улыбнулся."
    me "Ну вот видишь, не так и страшно. Теперь попробуем полноценно поехать."
    me "Делай всё то же самое, но сразу ставь вторую ногу на педаль, и тихонько их вращай. Или дай им самим вращаться, привод то прямой."

    show sl pioneer smile2 with dspr

    sl "Ох… Сейчас."

    call to_nvl_mode

    "Я продолжил её держать, а Славя оттолкнулась, и немного мотнув рулём в сторону, благо я удержал, поставила ногу на педаль, и стала их понемногу вращать."
    me_n "Во-от, молодец! Держи руль прямо."
    "Мы медленно проехали метров десять."
    me_n "Тормози потихонечку."
    "Славя также плавно остановилась."

    call to_adv_mode

    me "Отлично! Ты быстро учишься!"

    show sl pioneer shy with dspr

    "Славя смутилась."
    sl "Ну, ты же меня держишь, сама я пока не удержусь."
    me "Ничего, через часок уже сама поедешь."
    me "Давай развернемся в обратную сторону."

    show sl pioneer smile with dspr

    "Славя слезла с велосипеда, и развернув его в обратную сторону, снова села."
    me "Давай теперь всё то же самое."
    sl "Ага!"

    hide sl
    show sl pioneer smile at cright
    with dspr

    "Славя оттолкнулась, и начала крутить педали, а я также придерживал её сбоку."
    "Но в какой-то момент её начало заваливать, из-за того, что она повернула руль."

    hide sl
    show sl pioneer normal at right
    with dspr

    me "Славя, на меня, на меня! Руль в мою сторону!"

    show sl pioneer surprise with dspr

    "Но было уже поздно. Она заваливалась всё сильнее, а я не мог её удержать."

    stop music fadeout 1.0

    pause(1.0)

    hide sl
    show black with dissolve

    play sound "<from 0.0 to 2.0>" + sfx_bicycle_falls fadeout 0.5 volume 1.2
    play sound2 "<from 1.0 to 3.0>" + sfx_bicycle_wheels fadeout 1.0 volume 1.1
    play sound3 "<from 0.0 to 1.5>" + sfx_bicycle_ring fadeout 0.5 volume 1.1

    "В один момент она потянула меня за собой, и мы с грохотом металла упали на землю."
    "..."

    hide black
    show cg d3_square_sl_fall
    with dissolve

    "Я открыл глаза, а передо мной, точнее подо мной лежала испуганная девочка."
    me "Славя! Не ушиблась?"
    sl "Вроде нет. Ничего не болит. Но испугалась."
    me "Я тоже… Давай вставать."
    sl "Давай…"

    hide cg
    show bg ext_square_day
    show sl pioneer normal at center
    with dissolve

    "Я встал, и сразу помог Славе подняться."
    "Мы осмотрелись, но ни на ком из нас не было даже шишки или царапины."
    "Странно, что велосипед лежал в нескольких десятках сантиметров от наших ног. Как она из него выскочила, и как я его пролетел, я так и не понял."

    play music music_list["i_want_to_play"] fadein 2.0 volume 0.8

    show sl pioneer laugh with good_dspr

    "Внезапно, Славя начала смеяться."
    "Я смотрел на неё, и не понимал, в чём дело, но из меня тоже начинал вырываться нервный смешок."
    me "Аха, хах, Славя, ты чего, хаха, смеёшься?"
    sl "Ой, ха-ха-ха, не могу, я, ха-ха-ха! Мы так смешно упали, ха-ха-ха!"
    "Я не выдержал, и тоже залился смехом."

    hide sl
    show sl pioneer laugh close at right
    with dspr

    "Хохотая, я поднял велосипед, и мы подошли к ближайшей скамейке, и сели на неё."
    "Велосипед я поставил рядом, облокотив его на ту же скамейку."

    show sl pioneer smile2 with dspr

    "Постепенно мы перестали смеяться, и лишь пытались отдышаться."
    me "Фу-ух, ну что, продолжим обучение, или ты уже не хочешь?"

    show sl pioneer smile with dspr

    sl "Конечно! Неудачи — это же часть процесса, верно? Посидим пару минут, и продолжим."
    "..."

    call to_nvl_mode

    "Немного отдохнув, мы продолжили."
    "Уже через полчаса Славя смогла почти без моей поддержки, самостоятельно доехать до конца площади, а через час и вовсе сделала полный круг."
    "Всё ещё довольно неуверенно, всё ещё я шел рядом, но тем не менее."
    "Равновесие она держала почти полностью сама."

    call to_adv_mode

    hide sl
    show sl pioneer smile at right
    with dspr

    me "Ну что, на сегодня закончим? Ты сделала большие успехи всего-то больше чем за час!"

    show sl pioneer smile2 with dspr

    sl "Ну не считая падения да, хи-хи."
    me "Знала бы ты, сколько раз я за всю свою жизнь с велосипеда падал!"

    show sl pioneer smile with dspr

    me "Ну и ты сама сказала, неудачи — это часть прогресса."
    sl "Это верно… Ну что, тогда до ужина? А потом и танцы. Мальчишки уже вон, начали стаскивать аппаратуру."
    me "Да, не будем им мешать."

    stop music fadeout 2.0

    hide sl
    show bg ext_houses_day
    with dissolve

    "Я взял велосипед, и пройдя немного вместе, мы разошлись."

    play music music_list["so_good_to_be_careless"] fadein 2.0 volume 0.8

    "Славя пошла к себе в домик, а я к себе."

    show bg ext_house_of_mt_day with dissolve

    "Поставив велосипед там же, где он был, я постучался."

    play sound sfx_knock_door7_polite

    pause(0.5)

    me "Ольга Дмитриевна?"
    "Ответа не последовало."
    "Я дёрнул ручку."
    "Дверь закрыта."
    "Ну, значит её нету."
    th "Надо выложить колоду!"
    "Вдруг вспомнил я."

    show bg int_house_of_mt_day with dissolve

    "Я быстро открыл дверь своим ключом, и забежав в домик, бросил колоду на пол, под тем местом, где она лежала на подоконнике, после чего вышел и закрыл дверь."

    show bg ext_house_of_mt_day with dissolve

    th "Не пойман – не вор, как говорится."
    "С чувством выполненного долга, я быстро покурил за домом, и присел в гамачок, отдохнуть."

    show black with clocks_in
    hide black with clocks_out

    play sound sfx_dinner_horn_processed

    "Не знаю, сколько я просидел в полу-забытии, минут 15, может 20, но вывел меня из транса звук горна."
    th "А в тюрьме сейчас ужин – макароны!"
    "Не весть откуда вспомнилась фраза из старого советского фильма."
    "Тут вроде, была не тюрьма, да и кормили на несколько порядков лучше, чем слипшимися макаронами."
    th "Интересно, в {i}этом{/i} времени «Джентльмены Удачи» уже вышел?"
    "Перебирая в голове советскую кинематографию, я поднялся с гамака и пошёл в столовую."

    show bg ext_dining_hall_near_day
    show mt pioneer normal at cright
    with dissolve2

    "Никого не встретив по пути, я дошел до столовой, возле входа в которую пересекся с вожатой."
    me "Ольга Дмитриевна! Вы где весь день пропадаете, я уж потерял вас!"

    show mt pioneer sad with dspr

    mt "Ой, Семён, да меня сегодня все потеряли."
    mt "С этой дискотекой столько проблем: за весь инвентарь распишись, получи, ревизию проведи."
    me "Устали?"
    mt "Да в общем-то не особо. Не в первый раз всё-таки."
    me "Тогда отдыхайте сегодня вечером на полную. А завтра утром с меня кофе."
    "Я улыбнулся."

    show mt pioneer smile with dspr

    mt "Очень мило с твоей стороны. Ну, ловлю на слове!"
    "Вместе мы зашли в столовую, где разделились."

    stop ambience fadeout 1.0

    hide mt
    show bg int_dining_hall_people_day
    with dissolve

    play ambience ambience_dining_hall_full fadein 1.0

    "Я взял поднос, и пошёл за столик, откуда мне махала Славя. Там же сидела Лена и Алиса."

    show un pioneer normal at left
    show dv pioneer normal at center
    show sl pioneer normal at right
    with good_dspr

    "Мы пожелали друг другу приятного аппетита."

    show sl pioneer smile2 with dspr

    sl "Ну что, Сёма, готов к вечеру? Вот я готова!"
    me "А что мне, собственно, готовить? Как мы выяснили утром, одет я буду также."
    me "Ну, разве что прихорошусь чуть-чуть."

    show sl pioneer angry with dspr

    sl "Ну, ты уж не опозорь меня!"
    "Она состроила мило наигранное серьёзное лицо, отчего я лишь улыбнулся."

    show sl pioneer smile with dspr

    dv "Танцевать буде-е?"

    show dv pioneer surprise with dspr

    "Спросила она, но не вовремя проглотила, и поперхнулась."

    show un pioneer smile
    show dv pioneer shocked
    with dspr

    "Сидевшая рядом Лена постучала её по спине и дала отпить чаю."
    me "Ну… Да. На танцах же этим и занимаются."

    show dv pioneer normal with dspr

    "Отдышавшись, она ответила."
    dv "Кхе, а ты умеешь?"
    th "А я умею?"
    "Повторил я вопрос сам себе."
    "Ну, конечно покружить медляк наверное буду в состоянии, но когда я это в последний раз делал? На школьном выпускном?"
    "Это ж сколько лет то прошло… {w}Ноги бы не отдавить, ни Славе, ни кому-либо ещё…"
    me "Справлюсь."
    "Уверенно ответил я."
    me "А вы идёте?"

    show dv pioneer smile
    show un pioneer smile
    with dspr

    "Я посмотрел на Алису и Лену."
    un "Да..."

    show dv pioneer guilty with dspr

    dv "Иду конечно… Только у меня платья нет."
    "Она громко выдохнула и погрустнела."
    me "А что, ни у кого из девочек не найдётся запасного?"
    dv "Да я много у кого спрашивала. Нету."

    show un pioneer shy with dspr

    un "Ну прости, Алиса. Я не думала, что мне может пригодиться ещё одно!"
    dv "Да ладно, чего уж там."

    show un pioneer smile
    show sl pioneer smile2
    with dspr

    sl "Ну и что, Алиса, какая печаль? {w}Иди так! Ты и в форме очень красивая! Я уверена, с тобой обязательно кто-нибудь потанцует."

    show dv pioneer shy with dspr

    dv "Правда?"
    un "Ну конечно!"
    sl "Да!"
    "Я подтвердил."

    show dv pioneer sad with dspr

    "Остаток ужина также прошёл за разговором."

    stop ambience fadeout 1.0
    stop music fadeout 2.0

    call set_time("sunset")

    hide dv
    hide un
    hide sl
    show dv pioneer normal at fleft
    show un pioneer smile at cleft
    show sl pioneer smile at right
    show bg ext_dining_hall_near_sunset
    with dissolve1

    play ambience ambience_camp_center_evening fadein 1.0

    "Мы вышли из столовой."

    play music music_list["get_to_know_me_better"] fadein 2.0 volume 0.8

    "Вечер уже начал вступать в права, заполняя всё вокруг красивым красновато-оранжевым свечением."
    sl "Все помнят? {w}Через полчаса начало, первый медленный танец через час. Не опаздывайте!"
    "Мы все согласились, и разошлись по домикам, готовиться."

    stop ambience fadeout 1.0

    show black with clocks_in

    play ambience ambience_int_cabin_evening fadein 1.0

    hide dv
    hide un
    hide sl
    show bg int_house_of_mt_sunset
    show mt dress normal at right
    hide black
    with clocks_out

    "Я вернулся в домик."
    "На удивление, вожатая уже успела переодеться в вечернее платье."
    me "Ольга Дмитриевна, выглядите потрясающе!"

    show mt dress smile with dspr

    mt "Правда?"
    "Она прокрутилась вокруг своей оси."
    mt "Спасибо!"
    mt "Ну, мне уже пора. Я все-таки как старшая, должна быть там до начала. {w}Не опаздывай!"
    me "Ни в коем случае!"

    show mt dress smile at walk_away_right
    pause(0.5)
    hide mt with dspr

    "Вожатая ушла."
    "..."
    th "А что мне, собственно, подготавливать?"
    "Пошуршав в своём ящике, я нашел неиспользуемою тряпочку, и решил хотя бы начистить ей обувь."
    "..."
    "Через пару минут обувь сверкала."
    me "Вот так-то лучше!"
    "Дальше я поправил рубашку, галстук, и был таков."
    "Посмотрев на себя в зеркало, я заключил."
    me "Ну ладно, ехала."
    "Я сел на стул. {w}Потом прошёлся по комнате. {w}Опять сел."
    "Никогда не любил чего-то ждать."
    "Я вернулся к своей кровати, и достал телефон."
    "На часах 18:46. Вероятно, открытие в семь. Ну ладно, как раз успеваю ещё покурить."
    "Я убрал телефон обратно, и выйдя на улицу, закрыл за собой дверь…"

    stop ambience fadeout 1.0

    window hide

    show bg ext_house_of_mt_sunset with dissolve
    pause(1.0)

    play ambience ambience_camp_center_night fadein 1.0

    show black with clocks_in
    hide black with clocks_out

    window show

    "Скурив сигарету, которых оставалось всё меньше и меньше, я закинул в рот жвачку, и не спеша двинул в сторону площади…"

    stop music fadeout 2.0

    show bg ext_square_night_party2 with dissolve1

    "Удивительно, но подходя к площади, я заметил что на улице активно темнеет."

    play music music_list["sweet_darkness"] fadein 2.0

    th "Может вечер сегодня пасмурный?"
    "На площади уже активно начал собираться народ."
    
    show mt dress angry far at fright
    with dspr

    "Среди знакомых лиц я увидел, естественно Ольгу Дмитриевну, которая уже за что-то отчитывала пионера помладше."

    show un dress normal far at fleft
    show dv pioneer normal far at left
    with dspr

    "Лену с Алисой."

    show el pioneer normal far at right
    show sh pioneer normal far at cright
    with dspr

    "Парней электроников."

    show us dress smile far at cleft
    with dspr

    "Ульяну, которая, на удивление, даже одела вечернее платье."

    show mi pioneer normal far at center
    with dspr

    "А также Мику, которая стояла за диджейским пультом и в чем-то ковырялась."
    "Она была без платья. Слави видно не было."

    hide mt
    hide un
    hide dv
    hide el
    hide sh
    hide us
    hide mi
    show mi pioneer normal at cright
    with long_dspr

    "Я подошёл ближе."
    me "Мику! Целый день не виделись. А ты чего здесь, за пультом, я имею в виду?"

    show mi pioneer happy with dspr

    mi "Ой, Сёмочка, привет! Да я вот без платья, как и многие."
    me "Разве это помеха?"

    show mi pioneer normal with dspr

    mi "Нет конечно, но я, ты знаешь, совсем не умею танцевать! Хоть с музыкой на «ты», но вот двигаться у меня совсем не получается."
    me "Ну-у, это всё равно не повод весь вечер стоять за пультом. Обязательно с кем-нибудь потанцуй."

    show mi pioneer smile with dspr

    me "Может, даже со мной, если Славя меня отпустит."
    "Мне стало как-то приятно, от осознания того, что Славя, вероятно, хочет танцевать только со мной."

    show mi pioneer happy with dspr

    mi "Я понимаю."

    show mi pioneer smile with dspr

    mi "Хорошо, Семён, я постараюсь."
    th "Это нельзя так оставлять."

    hide mi with good_dspr

    "Я отошёл, и подумал о том, что мне почему-то мне стало жалко эту девочку, и я пытался придумать, что же сделать…"

    show sh pioneer normal far at left
    with dspr

    "На глаза попался Шурик."
    "Я подошёл поближе, и жестом, так чтобы он увидел, поманил к себе."

    hide sh
    show sh pioneer normal at left
    with dspr

    sh "Да, Семён, привет. Что такое?"
    me "Привет, привет. Ты будешь с кем-нибудь танцевать?"

    show sh pioneer serious with dspr

    sh "Да не знаю… Ну, ни с кем не договаривался. А что такое?"
    th "Нам подходит. Берём."
    me "Там наш милый диджей, который весь вечер будет снабжать нас музыкой, остался без пары."
    me "Может, потанцуешь с ней?"

    show sh pioneer surprise with dspr

    sh "Мику? Хм, ну а почему нет?"

    show sh pioneer normal with dspr

    sh "Девушка она красивая, и интересная. Мы с ней сегодня много про аппаратуру разговаривали, пока подключали тут всё."
    me "Эй, только не надо во время танца давать ей вводную лекцию по основам электротехники. Просто пригласи её, потанцуйте. Ей будет приятно."

    show sh pioneer normal_smile with dspr

    sh "Да понял я, не дурак."
    sh " Ладно, спасибо, Семён."

    show sh pioneer normal with dspr

    me "Давай, не пролажай!"

    stop music fadeout 2.0

    show sh pioneer normal at walk_away_left
    show blink
    with None

    pause(0.5)

    hide sh with dspr

    "Не успел он отойти, как мне закрыли глаза."
    th "Вот, Шурик, блин, хоть бы сказал."

    play music music_list["what_do_you_think_of_me"] fadein 2.0

    "Хотя я и так знал, кто это, отчего расплылся в улыбке."
    me "Славя! Ну наконец-то, я уже заждался!"

    hide blink
    show unblink

    "Мои глаза вновь увидели свет."

    hide unblink
    show sl dress smile2 at center
    with good_dspr

    "Я обернулся."
    sl "Хи-хи, прости, немного задержалась."

    show sl dress happy with dspr

    sl "Как там Мику сказала? {w}«Придурить» носик, ха-ха-ха."
    "Я рассмеялся."
    me "Ха-ха, да..."

    show sl dress smile2 with dspr

    "На этом мой словарный запас закончился."
    "Я понял, как красива сейчас Славя, в вечернем платье, при свете фонарей."
    "И не мог отвести взгляда."

    show sl dress shy with dspr

    sl "Мужчина... Вы во мне сейчас дыру просмотрите."
    "Я очухался."
    me "Прости. Просто... {w}Не могу перестать тобой любоваться. Ты очень красивая."

    show sl dress tender with dspr

    "Славя смутилась."
    sl "Спасибо..."
    "Пару секунд продолжалась немая сцена, пока девушка наконец не сказала."
    
    show sl dress smile2 with dspr

    sl "Сём... Ты что-то сказать хотел. Про Мику."
    me "А да, точно. {w}Так вот, кхм."

    show sl dress smile with dspr

    me "Буквально только что ей пару нашёл на танцы, Шурика. А то, чувствую, он и сам бы никого не пригласил, и дама бы без танца осталась."
    me "Убил, так сказать, двух зайцев сразу."
    sl "Это ты хорошо сделал! И подруге помог, и мне проще."

    show sl dress shy with dspr

    sl "Потому-что я тебя ни на один танец не отдам, так и знай!"
    "Я растаял. {w}Было очень приятно слышать это от девушки, в которую я, кажется, начал влюбляться."
    "Чувство ещё было скрытое, и неуверенное. И я не спешил, но чувствовал, что наша близость и обоюдное желание всегда быть вместе не просто так."

    hide sl
    show dv pioneer smile at fleft
    show un dress smile at cleft
    show sl dress smile at right
    with long_dspr

    "Мы ещё немного пообщались вдвоём, потом с подошедшими Леной и Алисой."

    stop music fadeout 5.0

    "А затем..."

    play sound "<from 0.0 to 5.0>" + sfx_mic_noise fadeout 0.5
    pause(1.0)

    mi "У-упс. Хи-хи."
    mi "Дорогие пионеры! Вечер танцев в лагере Совёнок объявляется открытым!"
    mi "Слово предоставляется вожатой старшего отряда, Мироновой Ольге Дмитриевне."
    "Вожатая подошла к микрофону, и заговорила."
    mt "Дорогие, пионеры!"
    mt "Я желаю вам хорошо провести этот вечер. Надеюсь, он запомнится вам надолго, а может, и человек, который составит вам компанию."

    show sl dress shy with dspr
    pause(1.0)
    show sl dress smile with dspr

    "Мы со Славей переглянулись."
    mt "Но не забывайте, что завтра продолжается обычная смена. Так что, не гуляйте допоздна!"
    mt "Пионеров младших отрядов заберут их вожатые. Старший отряд может уходить самостоятельно."
    mt "Приятного вечера!"
    "Вожатая отключила микрофон, и положила его."
    "Мику нажала пару кнопок, кивнула кому-то в стороне."

    play music music_list["lightness_radio_bus"] fadein 2.0

    hide un
    hide dv
    hide sl
    show bg ext_square_night_party
    show sl dress smile at cright
    with dissolve1

    "В следующий момент на деревьях зажглась гирлянда, а из колонок заиграл какой-то медляк, явно соответствующий духу этой эпохи."
    "Мику схватила микрофон, и сказала."
    mi "Первый медленный танец, кавалеры приглашают дам!"
    "Я оглянулся."
    "Пионеры, несколько смущенные, видимо, такой быстрой сменой обстановки, немного очухались, и я увидел, как парни начали подходить к девушкам, и звать на танец."
    "Я не стал медлить, поэтому обернулся к Славе, и убрал одну руку за спину, наклонился, и сказал."
    me "Разрешите вас пригласить?"

    show sl dress shy with good_dspr

    sl "Д-да!"

    hide sl
    show cg d3_square_sl_dance
    with dissolve

    "Я взял девушку за руку, и мы вышли на площадь, где потихоньку, сначала неуверенно, но начали танцевать."
    "Мы держали друг друга за руку, Славя положила мне вторую руку на плечо, а я ей на талию."
    "Мы медленно вспоминали движения, стараясь не наступить друг другу на ноги, но стеснения не было."
    "Мы двигались свободно, и вскоре начали наращивать темп."
    "Пару раз мне даже удалось закрутить Славю, а затем снова вернуть к себе."
    "В эти секунды, я, кажется, потерял счёт времени."
    "Мы танцевали не больше минуты, но мне они показались вечностью."
    "Самой прекрасной вечностью, которую только можно пережить."

    stop music fadeout 2.0

    "Но вот, постепенно, музыка начала затухать."

    hide cg
    show sl dress smile2 at center
    with dissolve

    "Мы со Славей остановили танец, и посмотрели в сторону диджейского пульта."
    "Туда подходила Мику, которую держал за руку Шурик, идя вместе с ней."
    th "Молодец! Не струсил. На первом же танце пригласил."
    "Мику немного пошатнулась, и чуть не упала, но удержала равновесие, и взяла микрофон."
    mi "Ой, у-ух. {w}Извините!"
    mi "Первый медленный танец окончен! Объявляется свободный танцпол."

    play music music_list["gentle_predator"] fadein 2.0 volume 0.5

    "Мику щёлкнула тумблер, и заиграла какая-то более попсовая музыка."
    "Но я её не слушал."

    hide sl
    show sl dress shy at left
    with dissolve

    "Мы со Славей сели на скамейку, по пути я продолжал держать её за руку, и спросил."
    me "Тебе понравилось?"

    show sl dress tender with dspr

    "Чувство полного счастья читалось у неё на глазах."
    sl "Да, Семён, это было прекрасно!"
    sl "Я и не знала, что ты так хорошо танцуешь."
    "Я усмехнулся."

    show sl dress smile2 with dspr

    me "Честно говоря, я сам от себя не ожидал. Танцевал то один раз в жизни…"
    "..."

    show sl dress smile with good_dspr

    "Мы продолжали сидеть, и мило общаться, после чего Мику объявила второй медленный танец."
    "На сей раз, дамы приглашали кавалеров."
    "В этот раз пионеры, видимо, разогретые первым танцем, и временем, пока все кто хотел свободно дрыгались на танцполе, повели себя более активно."

    stop music fadeout 2.0

    "Площадь стала быстро заполняться парами."

    play music music_list["lightness_radio_bus"] fadein 2.0

    hide sl
    show sl dress smile2 at center
    with good_dspr

    "Славя тоже не стала медлить, и вскочив со скамейки, протянула мне руку."
    sl "Разрешите вас пригласить?"
    "Она улыбнулась."
    me "С удовольствием!"

    hide sl
    show cg d3_square_sl_dance
    with dissolve

    "В этот раз всё прошло ещё более великолепно."
    "Сразу взяв нужный темп, и после первого раза привыкнув друг к другу, мы кружили по всей площади, полностью отдавшись моменту."
    "Все остальные танцующие пары, те, кто стоял в стороне, подсветка на деревьях, и всё вокруг превратилось в общий размытый фон."
    "Казалось, я мог находиться в таком состоянии бесконечно…"

    stop music fadeout 2.0

    "Но вот, музыка закончилась."
    "Мы сделали последнее движение, и остановились."

    hide cg
    show sl dress smile2 at right
    with dissolve

    "К нам подошла улыбающаяся Алиса."

    show dv pioneer smile at left
    with half_good_dspr

    dv "Ну вы дали жару!"

    show sl dress shy with dspr

    sl "Что?"
    "Ни она, ни я не поняли о чем речь, всё ещё не до конца выйдя из состояния потока."

    show dv pioneer grin with dspr

    dv "То! Говорю, танцевали вы круто!"
    dv "И где только научились? Половина площади на вас смотрела."

    show sl dress smile with dspr

    "Мы со Славей переглянулись, и улыбнулись."
    me "Сам не знаю, как у нас так выходит."
    dv "А что тут думать?"

    show dv pioneer laugh with dspr

    dv "Называется болезнь на букву Л, но не лихорадка."
    "Она подмигнула."

    show sl dress shy with dspr

    "Славя тотчас же покраснела, а я лишь кашлянул."
    me "Кхм, ну может мы просто занимали слишком много места."
    me "В любом случае, приятно что на нас обратили внимание."

    show dv pioneer smile with dspr

    dv "Всегда пожалуйста!"

    show dv pioneer smile at walk_away_left
    pause(0.5)
    hide dv with dspr

    "Алиса улыбнулась, и удалилась в сторону скамеек."
    sl "Семён, а может?.."

    show sl dress smile2 with dspr

    sl "В следующий раз потанцуем так, чтобы на нас никто не смотрел?"
    "Я немного удивился."
    me "Ты хочешь? Можно уйти на пристань, там сейчас наверное красиво."

    show sl dress smile with dspr

    sl "Да, было бы здорово."
    "..."

    hide sl
    show sl dress smile at fright
    with good_dspr

    "Во время текущего перерыва между медляками, мы немного походили вдвоём, и подошли к Мику за диджейский пульт."
    "Оказалось, что во второй раз она тоже танцевала с Шуриком, просто мы этого не заметили."
    "И вот, когда Мику объявила очередной медленный танец, и все начали выходить парами, мы, под шумок, скользнули в сторону, где было больше тени."

    play music music_list["i_dont_blame_you"] fadein 3.0 volume 0.8

    "Затем, достаточно отдалившись от площади, вышли на дорожку."

    call set_time("night")

    hide sl
    show sl dress smile close at right
    show bg ext_houses_night
    with dissolve

    sl "Зря, конечно, Ольгу Дмитриевну не предупредили, но я думаю она не обидится."
    me "Я тоже так думаю. К тому же она сама сказала, что старший отряд может уходить по своему усмотрению."

    show sl dress shy with dspr

    sl "Верно."

    hide sl
    show cg d3_walkin_sl_romantic
    with dissolve

    "Ответила Славя, и взяла меня за руку, немного ко мне прижавшись."
    "Мне стало немного неловко, и очень приятно одновременно."
    "Мы не спеша направились к лодочной станции, мило беседуя по пути."
    "..."
    "Подходя к причалу, мы заметили довольно большое количество светлячков, а также звезды, проступающие из-под затянувшегося неба."

    stop ambience fadeout 1.0

    hide cg
    show bg ext_boathouse_night
    show sl dress tender at right
    with dissolve1

    play ambience ambience_boat_station_night fadein 1.0

    "Славя воскликнула."
    sl "Семён! Смотри, как красиво!"

    stop music fadeout 2.0

    sl "Давай подойдём поближе к воде!"
    me "Конечно!"

    play music music_list["forest_maiden"] fadein 2.0 volume 0.8

    hide sl
    show sl dress smile2 at right
    with dspr

    "Пока мы подходили, я и сам убедился, что красота на берегу стояла неописуемая."

    hide sl
    show cg d3_boathouse_sl_romantic
    with dissolve

    "Мы подошли ближе к берегу, и увидели всю картину целиком."
    "Славя встала, и с глазами полными восторга наслаждалась пейзажем."
    "Я же сел рядом."
    "Взору открывался прекрасный вид."
    "Луна в компании звёзд, мягко пробивающиеся сквозь облака, и отражающиеся на водной глади, и летающие по всюду светлячки."
    "Картина была по настоящему сказочной."
    "Я вдохнул свежий воздух, и подумал, что уже ни капли не жалею о том, что попал в это место. Неважно, случайно, или по чей-то воле."
    "Я сидел рядом с человеком, который за три дня стал мне дороже всей моей прошлой жизни. Я не мог позволить себе отпустить её."

    hide cg
    show sl dress smile at cright
    with dissolve

    "Я встал, и взяв Славю за руки, сказал."

    hide sl
    show sl dress smile at center
    with good_dspr

    me "Позвольте вас пригласить?"

    show sl dress shy with dspr

    "Она лишь томно ответила «да»."

    hide sl
    show cg d3_boathouse_sl_dance
    with dissolve

    "Мы вышли на место посвободнее, и закружились в танце."
    "Нам не нужна была ни музыка, ни гирлянда на деревьях, ни пионеры вокруг."
    "Мы кружили под прекрасным ночным небом в окружении сотен светлячков."
    "Вновь мы погрузились в момент, когда стали существовать только мы вдвоём."
    "Сделав ещё несколько движений, я закружил Славю, и вернул к себе."
    "Но то ли я потянул слишком сильно, то ли она оступилась, но пройдя дальше чем нужно, она начала медленно падать."
    "Подхватив её за талию, я остановил её."
    "Славя немного прогнулась в спине под действием силы тяжести, а я приблизился к её лицу, так как она потянула меня за собой, пока падала."
    "Наши лица оказались в десятке сантиметров друг от друга."
    "Я чувствовал её частое дыхание и тепло её тела."
    "Она лежала у меня на руке, а второй мы держались за руки."
    "Я видел в её глазах бесконечное счастье и полное спокойствие."
    "Я чувствовал, что она доверяет мне следующий шаг."
    me "Славя…"
    "Тихо произнес я."
    sl "Да..."
    "Она всё поняла. Мы оба друг друга поняли."
    "Также, как поняли друг друга с самого первого дня, как я сюда попал, и встретил её у входа."

    show blink

    "Я закрыл глаза, и начал приближаться к ней."
    "Наши губы соприкоснулись."

    play sound sfx_head_heartbeat fadein 0.5 loop

    "Кажется, у нас обоих перехватило дыхание."
    "Я услышал, как она сделала резкий вдох, и почувствовал, что моё сердце готово выпрыгнуть из груди."
    "Момент бесконечного взаимного доверия и теплоты продлился несколько секунд."

    stop sound fadeout 2.0

    hide cg
    show sl dress tender at center
    hide blink
    show unblink
    with dissolve

    "Отпрянув от девушки, я вернул её в вертикальное положение, и посмотрел в глаза."
    "Они излучали бесконечную влюблённость."

    stop music fadeout 5.0
    
    hide sl
    show sl dress tender close at cright
    with long_dspr
    
    "Славя обняла меня и прижалась лицом к моему плечу."
    sl "Семён… Спасибо. Спасибо тебе большое за этот вечер."
    "Я лишь обнял её в ответ."
    "..."
    "Несколько минут мы простояли, обнимаясь, в полной тишине."
    "Но это была не давящая тишина, не неловкая пауза."
    "Это было то, что нам обоим сейчас нужно. {w}Услышать тишину и внутренний мир друг друга."
    "О чём говорят наши сердца?"
    "..."

    play music music_list["dance_of_fireflies"] fadein 3.0 volume 0.75

    hide sl
    show sl dress shy at cright
    with good_dspr

    "Вскоре, Славя заговорила."
    sl "Уже поздно. Стоит возвращаться по домам."
    "Как бы ни хотелось прерывать этот вечер, но она была права."
    me "Тогда пойдём, я тебя провожу."

    show sl dress smile with dspr

    "Она улыбнулась, и мы направились в сторону домиков."

    stop ambience fadeout 1.0

    show bg ext_square_night_party2 with dissolve1

    play ambience ambience_camp_center_night fadein 1.0

    "На площади уже почти никого не было. Свет был выключен, аппаратура тоже."
    "Только несколько пар из других старших отрядов сидели на лавочках."
    "Мы прошли мимо…"

    show bg ext_houses_night with dissolve

    "Мило беседуя, мы прошли мимо строений пионеров."

    stop music fadeout 2.0

    show bg ext_house_of_sl_night with dissolve1

    "И подошли к домику Слави."

    play music music_list["forest_maiden"] fadein 2.0 volume 0.8

    hide sl
    show sl dress smile2 at center
    with long_dspr

    "Мы взяли друг друга за руки, и я сказал."
    me "Спасибо тебе ещё раз за этот замечательный вечер."
    sl "И тебе спасибо. {w}Я ещё никогда не была такой счастливой, как сегодня."

    hide sl
    show sl dress shy close at center
    with dspr
    pause(1.0)
    hide sl
    show sl dress shy at center
    with dspr

    "Она подтянулась на носочках, и робко поцеловала меня в губы."
    sl "Спокойной ночи, Сёма."
    me "Спокойной ночи, Славя."

    hide sl
    show sl dress smile far at center
    with long_dspr
    pause(1.5)
    hide sl with good_dspr
    
    "Она зашла в домик, обернувшись на прощание."
    "А я стоял перед её домиком, и расплывался в улыбке."
    "На глазах начали проступать слёзы радости."
    "Рядом с этой девочкой я чувствовал такое {b}простое{/b}, но давно забытое чувство. {w}Рядом с ней я испытывал {b}счастье{/b}."
    "Простое счастье быть рядом с тем, кто понимает тебя во всём, и кому ты бесконечно дорог."

    stop music fadeout 3.0

    show bg ext_path_night with dissolve2

    call smoking_process(with_pack_crumple=False, with_pause=1.0)

    play music music_list["dance_of_fireflies"] fadein 3.0 volume 0.67

    "Утерев глаза, я свернул с тропинки в пролесок рядом с домиками, сел под дерево и закурил сигарету."
    th "Даже если нам не будет суждено выбраться отсюда вместе. Я не хочу, чтобы она меня забыла. Надо будет что-нибудь подготовить."
    "Через пару минут, от накопившейся усталости и расслабившей сигареты, мысли потекли вяло."
    "Я решил оставить все размышления на утро, которое, как известно, вечера мудренее, и пошел в сторону домика."

    show black with clocks_in
    
    show bg ext_house_of_mt_night_without_light
    hide black with clocks_out

    stop ambience fadeout 1.0

    show black with clocks_in

    play ambience ambience_int_cabin_night fadein 1.0

    show bg int_house_of_mt_night2
    hide black with clocks_out

    "Я зашёл в домик."

    play sound sfx_bed_squeak2

    "Вожатая, кажется, уже спавшая, приподнялась на локтях."
    mt "Мхм?"
    mt "Ну что, Ромео, нагулялись?"
    "Я закрыл дверь на ключ, и ответил."
    me "Что?"
    mt "Да ладно, не прикидывайся. Я же видела, как вы со Славей ушли."
    "Вожатая зевнула."
    mt "Только останавливать не стала. Потому как доверяю, что тебе, что ей."
    me "..."
    mt "Я надеюсь, без происшествий?"
    me "Обижаете, Ольга Дмитриевна."
    mt "Вот и славно. Спокойной ночи."
    "Я разделся, и лёг в постель."

    show blink

    stop music fadeout 2.0

    "Под впечатлением от всего сегодняшнего дня, крутя в голове разные его эпизоды, я быстро заснул…"

    stop ambience fadeout 1.0

    window hide

    $ renpy.pause(1.0, hard=True)

    jump simple_happiness_mod_day4


# День 4
label simple_happiness_mod_day4:
    $ renpy.block_rollback()
    $ backdrop = "days"
    $ new_chapter(4, u"Простое Счастье. День 4")

    call set_time

    $ set_mode_adv()

    play ambience ambience_int_cabin_day fadein 1.0 volume 0.9
    play music music_list["everyday_theme"] fadein 5.0 volume 0.8

    "Судя по ощущениям, проснулся я довольно рано."

    hide blink
    show bg int_house_of_mt_day
    show unblink
    with dissolve

    pause(1.0)

    hide unblink

    "Утро только начало вступать в права, а вожатая всё ещё спала."
    "Ложиться обратно совершенно не хотелось. Я чувствовал невероятный прилив сил после вчерашнего."
    "Поэтому, тихонько поднявшись, и заправив постель, я согрел чайник, и сделал одну чашку ароматного кофе для вожатой."
    th "Вчера обещался, всё-таки."
    "Взяв с собой полотенце, и прочие мыльно-рыльные принадлежности, я решил, наконец-таки, опробовать местные умывальники, которые видел уже не раз."
    "Поэтому, направился в их сторону."

    stop ambience fadeout 1.0

    show black with clocks_in

    play ambience ambience_camp_center_day fadein 1.0

    show bg ext_washstand_day
    hide black
    with clocks_out

    "Дойдя до места общественного умывания, я огляделся."
    "Вокруг была уложена мелкая кафельная плитка, а судя по обилию пролитой воды на полу, и в раковинах, тут уже побывало, по меньшей мере, человек десять."
    "Подойдя к одной из раковин, я обнаружил только один кранчик."
    th "А на что я рассчитывал? На горячее водоснабжение, что-ли?"
    th "Ладно, будем довольствоваться холодной."

    play sound sfx_open_water_sink
    play sound2 sfx_water_sink_stream fadein 1.0 loop

    show bg ext_washstand2_day with dissolve

    "Сняв рубашку, и открыв кран, я понял, что вода не просто холодная, она {color=#d4eafb}{b}ледяная{/b}{/color}."
    "Настолько, что аж обжигала."
    th "Охренеть, блин, и как тут мыться?"
    "..."
    th "У-ух, ты!"
    "..."
    th "У-уф!"
    "..."
    "Кое-как помыв подмышки, и умыв лицо, я понял, что с меня достаточно, поэтому, взял полотенце, и начал активно обтираться."
    "Одев рубашку обратно, я достал из пакетика зубную щетку с порошком, и начал чистить зубы."
    th "Ну да, на вкус как порошок. Только для стирки."

    play sound sfx_close_water_sink
    stop sound2 fadeout 1.0

    "Еле как дотерпев, почистив все зубы, я промыл рот большим количеством воды, и только собрал всё в пакетик, как из-за тропинки, ведущей в лес, выбежала Славя."

    show bg ext_washstand_day
    show sl sport smile far at right
    with dissolve

    "Одета она была в спортивный костюм, который смотрелся на ней очень эффектно, подчёркивая формы."

    show sl sport smile2 close at cright
    with long_dspr

    pause(0.5)

    "Завидев меня, она ускорила бег, и подбежав, сразу обняла."

    sl "Семён, привет! А ты чего сегодня так рано?"
    "Я заулыбался, и ответил."
    me "Да вот ты знаешь, выспался!"
    me "Видимо, вчерашний день дал мне очень много сил."
    "Я многозначно посмотрел на Славю."

    show sl sport smile with dspr

    sl "Да, я тоже проснулась сегодня раньше обычного."
    sl "Решила вот, пробежаться. А то что, зря что ли с собой спортивную форму брала."

    hide sl
    show sl sport smile at cright
    with dspr

    "Я сделал шаг назад, и ещё раз осмотрел её, и еле сдержался, чтобы не облизнуться."
    me "Она тебе очень идёт."

    show sl sport smile2 with dspr

    sl "Да? Спасибо!"
    dvp "Да не буду я тебе ничего тереть!"

    show sl sport surprise with dspr

    "Внезапно мы услышали голос."
    "Обернувшись, я увидел как к умывальникам подходят Алиса и Ульяна."

    show us sport dontlike far at fleft
    show dv pioneer2 angry far at cleft
    with good_dspr

    us "Ну почему-у? Баня ещё не скоро, а я уже вся чешусь!"
    dv "А меньше надо по земле кататься!"

    hide sl
    hide us
    hide dv
    show us sport normal at fleft
    show dv pioneer2 normal at cleft
    show sl sport smile at cright
    with good_dspr

    "Наконец, они подошли достаточно близко, чтобы заговорить."
    dv "О как. Утро доброе, товарищи пионеры."
    sl "Доброе, Алиса. Умыться пришли?"
    "Я тоже поздоровался."

    show dv pioneer2 smile with dspr

    dv "Да эта мелкая от меня всё никак не отстанет, всё трещит, чтоб я ей спинку потёрла."
    dv "Ну и самой было бы неплохо ополоснуться."

    show us sport dontlike with dspr

    us "Да, а она не хочет оказать своему товарищу помощь в трудную минуту!"

    show dv pioneer2 grin with dspr

    dv "Я такого не говорила."

    show us sport angry with dspr

    "Ульяна ничего не ответила, а лишь только скорчила странную рожу."
    "Было похоже, что она сейчас взорвётся от злости."

    show dv pioneer2 smile with dspr

    dv "Ладно, мы пойдем в крайнее место."

    show us sport smile with dspr

    sl "Хорошо, до встречи на завтраке!"

    show dv pioneer2 smile at walk_away_left
    show us sport smile at walk_away_left
    pause(1.0)
    hide dv
    hide us
    with good_dspr

    "Они зашли вглубь умывальников."

    show sl sport smile2 with dspr

    sl "А ты, Семён, уже умылся, или только пришёл?"
    me "Я уже чист, и готов к новым свершениям!"

    show sl sport laugh with dspr

    "Девушка рассмеялась."
    sl "Хорошо, пойдем тогда до домиков. А то я сама ещё переодеться хотела, и успеть умыться."

    me "Конечно, время ещё…"

    stop music fadeout 1.0

    show sl sport surprise with dspr

    play music music_list["awakening_power"] fadein 1.0

    dv "УЛЬЯНА, ЧТО ТЫ ТВОРИШЬ!?"
    "Не успел я договорить, как из глубины умывальников послышался крик Алисы."
    dv "Ах, ты мелкая, а ну иди сюда!"
    "Голос стал ближе."

    hide sl
    show cg d5_dv_us_wash_3
    with dspr

    "Стоило мне обернуться, как я увидел занимательную картину."
    "Алиса бежала за Ульяной, а обе они были без лифчиков."
    "Ульяна при этом, бежала, явно с Алисиным у себя в руке."
    us "Аха-ха!"
    "Ульяна кажется, совсем не собиралась останавливаться, и её ничего не смущало."

    show blink

    "Внезапно, я почувствовал, что мне закрыли глаза."
    sl "Девочки! Вы чего творите??"
    "Судя по топоту они не останавливались."
    sl "Прекратите сейчас же! Ну вас увидят же!"
    "Последние слова, кажется, подействовали на Ульяну, потому как движение вокруг явно прекратилось, и послышалось недолгое шуршание."
    dv "Иди обратно, мелкая, пока тебя кто-нибудь не увидел, и не умер со смеху!"
    us "Ой, ой, можно подумать. Отрастила себе, как у коровы вымя!"
    dv "ДА ИДИ ТЫ УЖЕ!!"

    stop music fadeout 2.0

    "Послышался топот маленьких ног."

    hide blink
    show unblink
    hide cg
    show sl sport surprise at right
    show dv skirt shy at left
    hide unblink
    with dissolve

    "Славя убрала руку от моих глаз, и я немного проморгался."
    sl "Семён, ты извини, конечно… {w}Но зрелище было…"
    dv "Пиздецовым."
    "Закончила за неё Алиса."

    play music music_list["everyday_theme"] fadeout 2.0 volume 0.8

    me "Да вы что, конечно."
    "Говорить о том, что я, всё же, что-то да видел, я не стал."
    "Я обернулся, и продолжил."
    me "Хорошо ещё, что рядом никого не оказалось."

    show sl sport normal with dspr

    "Славя тоже посмотрела по сторонам."
    sl "Вроде да."

    show dv skirt sad with dspr

    "Алиса выглядела немного подавленной, и явно, очень смущённой."
    sl "Не волнуйся, Алиса. Почти наверняка, тут никого не было."
    dv "А если, всё таки, кто-то увидел?"
    sl "Тогда мы настойчиво попросим его забыть всё, что он видел. И никому не рассказывать."
    me "Я помогу, если что."
    dv "Спасибо, ребята."
    dv "Блин, вот люблю я эту мелкую, но иногда она такую фигню вытворяет."

    show sl sport smile with dspr

    sl "Дети."
    "Заключила она."
    "Алиса согласилась, мы перекинулись ещё парой фраз и она вернулась к Ульяне."

    show dv skirt sad at walk_away_left
    pause(0.5)
    hide dv
    with long_dspr

    pause(0.5)

    me "Да-а, вот это утречко!"

    show sl sport laugh with dspr

    sl "Ха-ха, и не говори."
    me "Пойдем наконец к домикам? Пока они ещё чего не учудили."

    show sl sport smile with dspr

    "Славя согласилась со мной, и мы направились к домикам."

    show black with clocks_in

    hide sl
    show bg ext_house_of_mt_day
    hide black
    with clocks_out

    "Разойдясь со Славей на повороте, я дошёл до нашего с вожатой домика, и постучал."

    play sound sfx_knock_door7_polite

    mt "Открыто!"

    stop ambience fadeout 1.0

    show bg int_house_of_mt_day
    show mt pioneer normal at fright
    with dissolve

    "Я зашел внутрь."

    play ambience ambience_int_cabin_day fadein 1.0

    "Вожатая уже была одета, и допивала кофе."
    mt "Доброе утро, Семён! Что-то ты рано сегодня."
    me "Доброе."
    "Я улыбнулся."
    me "На меня Славя положительно действует."

    show mt pioneer smile with dspr

    "Я усмехнулся."
    mt "Оно и видно. И это очень здорово, на самом деле."
    mt "Кстати, спасибо за кофе!"
    me "Ну я же обещал!"

    show mt pioneer sad with dspr

    mt "А-ай! Мне знаешь, сколько мужчин уже чего только не обещали? {w}И где они все теперь?"
    "Я повесил полотенце сушиться на спинку кровати, убрал пакетик в тумбочку, и спросил."
    me "И где же?"
    mt "Нету их! Ни их самих, ни их обещаний."

    hide mt
    show mt pioneer sad at right
    with dspr

    "Я присел рядом за стол, и сказал."
    me "Такая девушка как вы, обязательно найдете себе спутника на всю жизнь."

    show mt pioneer normal with dspr

    mt "С каждым годом всё меньше в это верю."
    th "Странные рассуждения. На вид ей не больше 30, а за три дня, что я здесь, она точно не постарела."
    "Мы поговорили ещё немного, и направились в столовую…"

    stop ambience fadeout 1.0

    show black with clocks_in

    play ambience ambience_dining_hall_full fadein 1.0

    hide mt
    show bg int_dining_hall_people_day
    show sl pioneer smile at center
    hide black
    with clocks_out

    "В столовой не произошло ничего интересного."
    "Мы также сидели за одним столом со Славей, и разговаривали, но с нами в этот раз сидели незнакомые пионеры, так что диалог не поддержали."

    stop ambience fadeout 1.0

    show bg ext_dining_hall_near_day with dissolve

    play ambience ambience_camp_center_day fadein 1.0

    "{i}Сегодня на улице Ленина ничего не произошло.{/i}"
    "Вспомнился старый анекдот, когда мы со Славей вышли из столовой."
    "Несмотря на утреннее происшествие, день обещал быть тихим."
    "Пока было не жарко, но и ветра особого не было."
    "Мы со Славей пошли на линейку…"

    show black with clocks_in

    hide sl
    show cg d2_lineup
    hide black
    with clocks_out

    "Вожатая нас тоже ничем не удивила. Обычный день, занимаемся по клубам."
    "Ну хоть радует, что продолжу, наконец-таки, своё обучение игре на гитаре."
    
    hide cg
    show bg ext_square_day
    show sl pioneer smile2 at center
    with dissolve

    "Единственное, что огорчало, Ольга Дмитриевна забрала Славю с собой на склад, так это грозило тем, что мы с ней сегодня будем видеться мало."
    "Когда все уже начали расходиться, мы попрощались со Славей, приобнявшись, и разошлись в разные стороны."

    show sl pioneer smile2 at walk_away_left
    pause(0.5)
    hide sl with dspr

    "..."

    show bg ext_path_day with dissolve

    "По пути в музыкальный клуб, я, конечно же, не забыл покурить."

    show bg ext_musclub_day with dissolve

    "Когда я подходил к клубу, меня окликнули."

    mip "Семён!"
    "Я обернулся."

    show mi pioneer smile far at center
    with dspr

    "Ко мне приближалась, весело подпрыгивая, Мику."

    hide mi
    show mi pioneer smile at center
    with good_dspr

    mi "Представляешь, ключи от клуба в домике забыла, пришлось возвращаться!"
    me "Ох блин, хорошо, что не потеряла, слушай."
    me "А дубликата нет?"

    show mi pioneer happy with dspr

    mi "Вроде был когда-то, но его потеряли ещё до начала нашей смены, так что пока выдают только единственный экземпляр, главе клуба."
    me "Да-а, лажа. {w}Ну пойдём внутрь?"

    show mi pioneer smile with dspr

    mi "Пойдем."

    stop ambience fadeout 1.0

    hide mi
    show mi pioneer normal at cright
    show bg int_musclub_mattresses_day
    with dissolve

    play ambience ambience_music_club_day fadein 1.0

    "Мы зашли внутрь, и я решил спросить."

    stop music fadeout 1.0
    pause(1.0)
    play music "<from 13.0>" + music_list["heather"] fadein 1.0

    me "Как провела вечер с Шуриком? {w}Кажется, он постоянно тебя приглашал."

    show mi pioneer smile with dspr

    mi "Знаешь, отлично, Сёмочка! Мы с ним очень хорошо поладили."

    show mi pioneer grin with dspr

    mi "И-и... {w}Кажется, я ему нравлюсь."
    "Я начал глупо улыбаться."

    show mi pioneer shocked with dspr

    mi "Что, чего ты так улыбаешься?"

    pause(1.5)
    
    show mi pioneer surprise with long_dspr

    "Прошло пару секунд, пока она обрабатывала информацию."
    mi "Подожди, это {b}ты{/b} его подговорил меня пригласить?"
    mi "О-ха-ё! {w}Семён, да ты сваха!"
    "Я рассмеялся."

    show mi pioneer grin with dspr

    me "Ну а что? Главное, что вам хорошо вместе."
    me "Да и он говорил, что вы и до этого много общались про музыкальную аппаратуру, так что, может, моя помощь и не потребовалась бы."

    show mi pioneer smile with dspr

    mi "Хи-хи, ну, может быть!"

    show mi pioneer happy with dspr

    stop music fadeout 2.0

    mi "Ладно, давай приступать к тренировкам."
    me "Давай."

    hide mi with dspr

    play music music_list["my_daily_life"] fadein 2.0 volume 0.8

    call to_nvl_mode

    "Я взял гитару, и мы опять начали тренироваться."
    "Мику показывала мне основные приёмы боя и перебора."
    "Конечно, я спросил про фингерстайл, но она сразу осадила меня, сказав что это очень сложная техника, и даже она не владеет ей в полной мере."
    "Я не стал спорить."
    "Продолжая учить мелодию, я параллельно всё лучше и лучше овладевал, непосредственно, самой игрой на гитаре, и в какой-то момент спросил про настройку инструмента."
    "Мику взяла гитару, покрутила колки, и сказала, что и правда надо было подстроить. Я же разницы в звуке не услышал."

    call to_adv_mode

    show mi pioneer normal at right
    with dspr

    "Так, с перерывами на разговоры, один раз на чай, и один раз мне покурить, прошло около двух часов."
    "Близилось время обеда, когда Мику сказала."
    mi "Теперь, попробуй исполнить композицию целиком."

    stop music fadeout 2.0

    me "Хорошо… Так…"
    "Я сел поудобнее, уверенно взял гитару, и начал играть."

    pause(1.0)

    play music miku_song_mi_learn1 noloop

    "Я старался изо всех сил, но кажется, пару раз всё-таки ошибся."
    "Отрабатывать отдельные части было просто, но вот соединить всё воедино…"

    show mi pioneer smile with dspr

    "Хотя, судя по реакции Мику, получалось у меня неплохо."

    call calc_music_how_much_play
    
    "Я закончил играть, и поднял взгляд на неё."

    show mi pioneer grin with dspr

    mi "Отлично, Семён! Ты делаешь поразительные успехи!"
    "Я немного смутился."
    me "Это все благодаря моему учителю."

    play music music_list["my_daily_life"] fadein 2.0 volume 0.8

    show mi pioneer smile with dspr

    mi "Хи-хи, спасибо! Но старания ученика тоже важны."

    show mi pioneer happy with dspr

    mi "Я даже не знаю, что после обеда будем делать. Ты просто перевыполнил план на сегодня!"
    "Я улыбнулся."

    show mi pioneer smile with dspr

    me "Ну, посмотрим."
    "Внезапно, меня осенило."
    me "Мику!"

    show mi pioneer shocked with dspr

    "Бедная девочка аж подпрыгнула."
    mi "Что такое? Не надо так кричать!"
    me "Прости."

    show mi pioneer normal with long_dspr

    me "Просто у меня появилась идея. Я… {w}Я хочу исполнить Славе какую-нибудь песню. На гитаре."
    "Я решил выдать всё прямо."
    me "Можешь меня научить ещё одной песне?"

    show mi pioneer cry_smile with dspr

    "Мику, кажется, умилилась, и ответила."
    mi "Охаёшечки-даттебаёшечки! Любовь — это так прекрасно. Ну как я могу отказать?"

    show mi pioneer smile with dspr

    mi "Однако учти, что ты ещё не закончил с текущей. {w}А учить две песни одновременно будет сложно. Справишься?"
    me "Чего бы мне это не стоило. Буду сидеть тут «денно и нощно» с гитарой в обнимку!"

    pause(1.0)

    me "Только… {w}Я не знаю, что играть."

    show mi pioneer happy with dspr

    mi "Это оставь мне. {w}Может, что вспомню, может посмотрю в тетрадке. Сегодня вечером уже определимся."
    me "Спасибо большое, Мику."

    show mi pioneer smile with dspr

    mi "Не стоит."

    play sound sfx_dinner_horn_processed volume 0.6

    "Из приоткрытого окна донёсся звук горна."
    "Я отложил гитару, хлопнул себя по коленям, и встал."
    "Ну, игра игрой, а обед по расписанию! Идём?"
    mi "Да, идём!"
    "Она тоже встала с матрасов, и выйдя из клуба, мы направились в столовую."

    stop ambience fadeout 1.0

    show black with clocks_in

    play ambience ambience_camp_center_day fadein 1.0

    hide mi
    show bg ext_dining_hall_near_day
    show mi pioneer normal at left
    show sl pioneer smile at right
    hide black
    with clocks_out

    "На подходе к столовой мы пересеклись со Славей, которая шла с другой стороны."
    "Увидев друг друга мы со Славей обнялись, после чего она обратилась к Мику."

    sl "Привет, Мику!"
    sl "Как успехи в кружке?"

    show mi pioneer smile with dspr

    mi "Ой, ты знаешь, у Сёмы так отлично получается, я даже не видела никогда, чтобы кто-то так быстро учился играть!"
    mi "Он прямо быстро-быстро учится, сегодня вот мелодию полностью исполнил, которой я его учила. Сам!"
    
    show mi pioneer happy with dspr

    th "Сезонное, у неё это, что-ли?"
    "Кажется, Мику опять начала палить словами, как из пулемёта, и я боялся, что она сболтнёт лишнего, и выдаст мой сюрприз."

    stop ambience fadeout 1.0

    hide mi
    hide sl
    show bg int_dining_hall_people_day
    show mi pioneer smile at left
    show sl pioneer smile2 at right
    with dissolve

    play ambience ambience_dining_hall_full fadein 1.0

    "Мы зашли в столовую, а Мику всё продолжала меня «рекламировать»."
    "…"
    "Когда мы наконец сели за столик со своими подносами, Славя сказала."

    show sl pioneer smile2 with dspr

    sl "Сёма, да ты прямо будущий маэстро!"
    "Я смутился."
    me "Ну, до маэстро мне ещё как до Луны пешком."
    sl "Хи-хи!"

    show sl pioneer smile with dspr

    sl "Кстати… {w}Меня сегодня Женя просила помочь в библиотеке, а самим нам тяжело будет книги с верхних полок переставлять…"

    show sl pioneer shy with dspr

    "Славя немного смутилась."
    sl "Если ты не против, конечно. И Мику тоже."
    me "Славя, ты же знаешь. С тобой хоть на северный полюс."

    show mi pioneer grin with dspr

    mi "А я, как эксперт, ответственно заявляю, что в обучении нужно делать перерывы. Так материал изученный лучше усваивается."

    show sl pioneer happy with dspr

    "Славя растаяла в улыбке, и мы продолжили есть."

    stop ambience fadeout 1.0

    "..."

    stop music fadeout 2.0

    hide sl
    hide mi
    show bg ext_dining_hall_near_day
    show sl pioneer smile at right
    show mi pioneer normal at fleft
    with dissolve1

    play music music_list["she_is_kind"] fadein 2.0 volume 0.8

    "Мы вышли из столовой, и попрощались с Мику."

    show mi pioneer grin with dspr

    "Спускаясь по лестнице, девушка подмигнула нам."

    show mi pioneer smile
    show sl pioneer smile2
    with good_dspr

    "Славя, к счастью, не поняла, что это предназначалось мне, и помахала в ответ."
    th "Значит, она не забыла про наш уговор."

    hide mi
    show sl pioneer smile
    with good_dspr

    "Мы со Славей направились в библиотеку, заведя разговор о том о сём."

    show black with clocks_in

    hide sl
    show bg ext_library_day
    show sl pioneer normal at right
    hide black
    with clocks_out

    me "Подождёте меня пару минут? Я быстро."
    "Сказал я, когда мы стояли перед входом."

    show sl pioneer smile with dspr

    sl "Хорошо. {w}Заодно, проверю, чтобы Женя не спала. А то получится, как в прошлый раз."

    show sl pioneer laugh with dspr

    "Девушка посмеялась."
    me "Ха-ха, да. Отличная идея."

    show sl pioneer smile with dspr
    show sl pioneer smile at walk_away_right
    pause(0.5)
    hide sl with dspr

    "Славя зашла в библиотеку, а я, покурив за зданием, вернулся ко входу, и зашёл внутрь."

    stop ambience fadeout 1.0

    show bg int_library_day
    show sl pioneer smile at right
    show mz pioneer bukal glasses at left
    with dissolve

    play ambience ambience_library_day fadein 1.0

    mz "О, Семён, а вот и ты! Спасибо, что пришёл!"
    me "Привет, Женя."
    sl "Ну что, быстрее начнём, быстрее закончим?"

    hide sl
    hide mz
    with long_dspr

    call to_nvl_mode

    "Женя выдала нам экспозицию того, что нужно делать, и мы принялись за работу."
    "Оказалось, что книги нужно было правильно расставить в правильном порядке по первой букве названия книги на всех полках."
    "Поэтому, Женя взяла на себя низкие стеллажи, которые стояли по периметру, а мы со Славей те, что стояли посреди помещения, высокие."
    "Славя сверялась со списком, и говорила мне, какую книгу куда переставить."
    "Иногда было довольно высоко, так что даже мне приходилось время от времени вставать на стул, чтобы дотянуться до верхних полок."

    call to_adv_mode

    show sl pioneer normal at left
    with good_dspr

    sl "Так, теперь у нас Булгаков, «Мастер и Маргарита». Её опять на самый верх."
    me "Что же такие известные произведения, и не пользуются популярностью, что их надо наверх убирать?"

    show sl pioneer smile2 with dspr

    sl "Не знаю, может все их уже перечитали, хи-хи."
    "Я взял книгу, и встав на стул, начал тянуться к полке."

    hide sl
    show sl pioneer smile far at left
    with dspr

    "Она была уже довольно сильно заставлена, да и я не подвинул стул поближе, подумал, что дотянусь…"
    "Не дотянулся."
    "Слишком сильно отклонившись на одной стороне стула, вторая пара ножек оторвалась от пола, и я, не удержавшись, полетел вниз."

    stop music fadeout 1.5
    play sound sfx_fall_wood_floor volume 0.93

    hide sl
    show black
    with good_dspr

    stop ambience fadeout 1.0
    play music music_list["eat_some_trouble"] fadein 1.5 volume 0.8
    
    sl "А-а, ай!"

    hide black
    show cg d3_sl_library
    with dissolve

    "Я открыл глаза."
    "Подо мной лежала Славя, а книга отлетела на несколько метров."
    me "Я тебя не ушиб?"
    sl "Вроде нет."
    me "Тебе не кажется, что последнее время мы слишком часто вдвоём оказываемся на полу в горизонтальном положении?"
    "Девушка рассмеялась."
    sl "Аха-ха, что ты хочешь этим сказать?"
    me "Аккуратнее надо быть, вот что!"

    hide cg
    show sl pioneer smile2 at cright
    with dissolve

    stop music fadeout 2.0

    "Я поднялся, и подал Славе руку, чтобы она встала."

    play sound "<from 2.0>" + sfx_alisa_masha_enter fadein 1.0 fadeout 1.0 volume 0.5

    "Отряхиваясь, мы услышали, как подбегает Женя."

    show mz pioneer normal glasses at fleft
    with good_dspr

    mz "Что у вас тут случилось? {w}Я услышала такой грохот!"
    me "Ничего страшного! Небольшая неудача на рабочем месте."

    show mz pioneer smile glasses with dspr

    mz "Фух, ну слава Богу. Я уж думала, травмировался кто."

    show mz pioneer shy glasses with dspr

    mz "Вы поаккуратнее тут!"

    show sl pioneer shy with dspr

    sl "Мы постараемся."

    play music music_list["my_daily_life"] fadein 2.0 volume 0.75

    show mz pioneer shy glasses at walk_away_left
    pause(0.5)
    hide mz
    show sl pioneer smile
    with dspr

    "Я поднял книгу, стул, и поставив наконец бедных Мастера и Маргариту на их законное место, мы продолжили работу. {b}Аккуратно{/b}."

    play sound sfx_clocks fadein 0.5

    show black with clocks_in

    hide sl
    show bg ext_library_day
    show sl pioneer normal at right
    hide black
    with clocks_out

    play ambience ambience_camp_center_day fadein 1.0
    stop sound fadeout 0.5

    "Меньше чем через час, работа была выполнена."
    "Женя поблагодарила нас, заявив что теперь перед нами в долгу, мы попрощались, и вышли."
    
    show sl pioneer smile with dspr

    sl "Ты обратно в клуб?"
    me "Пожалуй, что да. Мику, меня, наверное, уже заждалась."
    sl "И то верно. Пройдём через домики? {w}У меня больше работы нет, так я, наверное, немножко отдохну."
    me "Конечно!"

    show sl pioneer smile2 with dspr

    "Я предложил Славе руку. {w}Она её взяла, и мы направились к её домику. Только что идти тут было от силы метров двести, а то и меньше."

    hide sl
    show bg ext_house_of_sl_day
    show sl pioneer shy at center
    with dissolve

    "Проводив девушку прямо до порога, я поцеловал её в щеку."
    "Это вызвало у меня лёгкую дрожь, и тех самых «бабочек в животе», а Славя немного смутилась и поцеловала меня в ответ."

    hide sl with good_dspr

    "Славя зашла в домик, а я проводил её взглядом, чувствуя подъём в душе."
    th "Надо же... {w}Как мало мне оказывается надо для счастья."
    th "А мало ли? {w}Мы со Славей, кажется, нравимся друг другу, и нам нравится проводить время вместе."
    th "Чем не счастье?"

    "Повертев ещё мысли в голове и приятное чувство внутри себя, в конечном итоге, я направился к клубу, предвкушая, подобрала ли Мику какую-нибудь песню."

    show black with clocks_in

    show bg ext_musclub_verandah_day
    hide black with clocks_out

    "Подходя к музыкальному клубу, я чувствовал мандраж предвкушения."
    "Не стучась, так как увидел Мику через стекло, сидящей на матрасах с гитарой в одной руке, и то ли тетрадкой, то ли книжкой в другой, я зашел."

    stop ambience fadeout 1.0

    show bg int_musclub_mattresses_day
    show mi pioneer normal at fright
    with dissolve

    play ambience ambience_music_club_day fadein 1.0

    mi "Сёма, ты как раз вовремя! У меня уже всё готово!"

    hide mi
    show mi pioneer normal at right
    with half_good_dspr

    "Я быстро подошёл, и сел рядом с ней."
    me "Ну, не тяни!"

    show mi pioneer smile with dspr

    mi "В общем, смотри, у меня два варианта."
    mi "Первый – песня, которую я исполняла на пляже. Ты её слышал."
    mi "А второй, вот, нашла табы в тетрадке. Только странно, что автор не указан."

    stop music fadeout 2.0

    mi "Сейчас я тебе её сыграю."

    hide mi
    show cg mi_guitar_yam
    with dissolve

    play music this_one_for_her volume 0.9 noloop

    "Мику, иногда поглядывая в тетрадь, начала исполнять очень красивую мелодию."
    $ renpy.pause(1.0, hard=True)
    "Она вызывала смешанные чувства."
    $ renpy.pause(1.0, hard=True)
    "С одной стороны, была немного меланхоличная, как и «Воспоминания», которую написала Мику."
    $ renpy.pause(1.0, hard=True)
    "Но с другой, звучала довольно романтично, и сразу начала ассоциироваться у меня со Славей. Такая же душевная, спокойная, приятная."
    $ renpy.pause(1.0, hard=True)
    "Она сразу запала мне в душу."

    call calc_music_how_much_play
    
    hide cg
    show mi pioneer smile at cright
    with dissolve

    mi "Ну что, какую выбираешь?"
    me "Песню, которую сочинила ты, я оставлю для тебя. Это твоя ценность."
    me "А мне очень понравилась вот эта. У неё есть название?"

    play music music_list["smooth_machine"] fadein 3.0 volume 0.77

    show mi pioneer normal with dspr
    pause(0.75)
    show mi pioneer smile with dspr

    mi "У меня написано «This One For Her». «Это для неё»…"

    show mi pioneer cry_smile with dspr

    mi "О-хоо-ё! Как красиво!"
    "Я согласился."
    me "Очень подходит. Я буду учить её!"

    hide mi
    show mi pioneer smile at center
    with dspr

    "Мику отложила гитару, вскочила с матрасов, и сказала."
    mi "Тогда, приступим незамедлительно! {w}Бери тетрадь, там табы. Начнём со вступления…"

    hide mi with dspr

    "..."
    "Мы с Мику начали разучивать композицию."
    "Начало шло бодро, и уже через полчаса я уверенно играл первые секунд пять из трека."

    show mi pioneer normal at left
    with dspr

    mi "Давай ненадолго прервёмся."
    "Я отложил гитару, потянулся, и сказал."
    me "Отличная идея! Пойду перекурю."

    show mi pioneer dontlike with dspr

    mi "Хо-о! {w}Курилка! {w}И как Славя ещё не заклеила тебе рот, чтобы ты эти палочки себе в рот не сувал?"
    me "Хе-хе-хе, сердце «маэстро» требует!"
    "Я посмеялся, а Мику пробормотала что-то невнятное на японском."

    stop ambience fadeout 1.0

    hide mi
    show bg ext_musclub_verandah_day
    with dissolve

    play ambience ambience_camp_center_day fadein 1.0

    call smoking_process(with_pause=1.0)

    "Я зашел за угол здания, и закурил сигарету."
    "В пачке, не считая той, что я только что взял, оставалось пять штук."
    th "Не густо. А ни одной машины, у водителей которых, можно что ни будь попросить, я так и не увидел."
    "Уже докуривая сигарету, я увидел, как в сторону клуба кто-то идёт."

    show bg ext_musclub_day with dissolve

    "Докурив сигарету, я вышел на тропинку перед входом, и пригляделся."

    show un pioneer normal far with long_dspr

    th "Лена!"
    th "А что она тут забыла? Ну ладно, подождём. Гостем будет."

    pause(1.0)

    hide un
    show un pioneer normal with good_dspr

    "Скоро Лена подошла и заговорила."
    un "Привет, Семён. Я тебя еще только подходя увидела."
    me "Я тоже, привет. Ты чего, в гости пришла?"

    show un pioneer shy with dspr

    un "Нет, я… Ну, как бы да, но…"
    un "Помнишь, мы разговаривали про общие увлечения, и я сказала, что играю на флейте?"
    "Я кивнул."

    show un pioneer smile with dspr

    un "Мне стало интересно, есть ли в музыкальном клубе флейта."
    me "Ох, а я и не знаю."
    me "Ну давай зайдём, Мику тебе всё покажет!"

    stop ambience fadeout 1.0

    hide un
    show bg int_musclub_mattresses_day
    show un pioneer normal at left
    show mi pioneer normal at right
    with dissolve1

    play ambience ambience_music_club_day fadein 1.0

    "Мы с Леной зашли внутрь."
    
    show mi pioneer smile with dspr

    mi "Леночка? Привет! А ты чего здесь?"

    show un pioneer shy with dspr

    "Лена смутилась, и ответила."
    un "Ну, уже наверное поздно, смена скоро закончится, но…"

    show un pioneer smile with dspr

    un "Я бы хотела побыть с вами. {w}Помнишь, я говорила, что играю на флейте?"

    show mi pioneer cry_smile with dspr

    "Мику расцвела."
    mi "Ни слова больше!"

    show mi pioneer smile at run_to_center

    "Вскочив с дивана, и немного споткнувшись…"

    show un pioneer shy
    show mi pioneer surprise
    with dspr

    mi "Ай!"
    me "Осторожнее!"

    show mi pioneer smile with dspr

    show mi pioneer smile at run_away_left
    pause(0.5)
    hide mi
    with good_dspr

    "Она побежала в подсобку, откуда вернулась с большой книгой, и положив её на стол, развернула, и обратилась к Лене."

    show un pioneer smile with dspr

    show mi pioneer smile at center
    with good_dspr

    mi "Ты хоть и ненадолго, но будешь членом клуба, тебя надо записать!"

    show un pioneer shy with dspr

    un "Хорошо…"
    "Когда Лена расписалась, Мику захлопнула книгу, и торжественно заявила."

    show un pioneer smile2
    show mi pioneer grin
    with dspr

    mi "Теперь нас трое!"
    "Мы с Леной тоже отметили этот приятный факт, после чего Мику отошла к инструментам, и наклонившись, в поисках, видимо, флейты, сказала."
    
    show un pioneer shy
    show mi pioneer happy
    with dspr

    mi "А вот…"

    show mi pioneer smile with dspr

    mi "Твой инструмент!"

    show un pioneer cry_smile with half_good_dspr

    "Лена взяла флейту, и с интересом, и некоторым восторгом, оглядела его."

    show un pioneer surprise with dspr

    un "Ого! У нас в школе были попроще, а своей у меня никогда и не было."
    "И правда, флейта выглядела довольно дорого, была инкрустирована вставками не то из меди, не то из бронзы, и имела резные элементы."

    show un pioneer cry_smile with dspr

    "Она ещё немного осмотрела её, пару раз приложившись губами, как будто «пробуя» её."

    show mi pioneer grin with dspr

    mi "А ты сможешь сейчас нам что-нибудь сыграть?"

    show un pioneer shy with dspr

    "Лена смутилась."
    un "Ну, кажется я помню пару композиций с музыкальной школы."
    me "Отлично, тогда давай послушаем!"
    "Вставил я."

    show mi pioneer smile with dspr

    mi "Присядем?"

    show un pioneer smile with dspr

    un "Нет, я стоя."
    "Мы с Мику сели на диван, и приготовились слушать."
    "Лена взяла флейту поудобнее, пару раз поправила рубашку на локте, и, закрыв глаза, начала играть…"

    stop music fadeout 2.0

    hide mi
    hide un
    show cg d4_un_flute
    with dissolve1

    pause(1.0)

    play music un_sinij_sinij_inij fadein 1.0 volume 0.35 noloop

    "Лена сразу погрузилась в процесс."
    "Она немного двигалась корпусом в такт мелодии, как будто сливаясь с ней воедино."
    "Мелодия звучала очень красиво."
    th "И почему она сразу не пошла в музыкальный клуб? Она же отлично играет."
    "Я взглянул на Мику. Глава клуба смотрела на неё завороженными глазами."
    "Кажется, она и сама жалела, что всё это время перед ней был такой алмаз."
    "А Лена, возможно, жалела, что из-за своей скромности и застенчивости, скрывала свои навыки от других."

    call calc_music_how_much_play

    stop music fadeout 1.0

    "Вскоре, Лена закончила играть."

    hide cg
    show mi pioneer cry_smile at right
    show un pioneer shy at left
    with dissolve

    "Она открыла глаза, и посмотрела на нас."

    play sound2 "<from 0.2>" + sfx_simon_applause fadein 0.5 volume 0.8 loop
    play sound3 "<from 0.5>" + sfx_simon_applause fadein 0.5 volume 0.55 loop

    "Одновременно с Мику мы начали аплодировать."

    stop sound2 fadeout 1.0

    hide mi
    show un pioneer smile2
    show mi pioneer cry_smile at center
    with good_dspr

    "Мику встала, подошла к Лене, и обняла её."

    stop sound3 fadeout 1.0

    mi "Лена! Ну почему же ты не пришла раньше?"
    un "Да я как-то… Стеснялась."

    show mi pioneer happy with dspr

    mi "И совершенно зря! Мы бы столько всего успели сыграть вместе."

    play music music_list["your_bright_side"] fadein 2.0 volume 0.8

    show un pioneer smile with dspr

    un "Ну, может ещё успеем?"

    show mi pioneer smile with dspr

    pause(1.0)

    "Мику на секунду задумалась, и начала говорить."
    mi "Ты знаешь, а ведь и…"

    hide un
    hide mi
    show un pioneer smile at fleft
    show mi pioneer normal at cleft
    with dspr

    play sound sfx_knock_door7_polite fadein 0.25 volume 0.5

    "Она остановилась, так как услышала стук в дверь, после чего она открылась, и из проёма выглянула… Славя?"

    show sl pioneer smile at fright
    with good_dspr

    "Я встал, и подойдя к ней, поцеловал в щеку, и спросил."

    hide sl
    show sl pioneer smile2 at right
    with dspr

    me "Славя, ты чего здесь? Я думал ты отдыхаешь!"
    sl "Ну, я хотела, но повалялась немного, да так и не смогла уснуть."
    sl "Решила к вам зайти…"

    show sl pioneer shy with dspr

    sl "Если я не помешаю."

    show mi pioneer smile with dspr

    mi "Конечно нет, Славечка! Гостям мы всегда рады, проходи пожалуйста."

    hide un
    hide mi
    hide sl
    show un pioneer smile at left
    show mi pioneer smile at center
    show sl pioneer smile at cright
    with good_dspr

    "Славя прошла дальше в помещение, и поздоровалась с Леной."

    show mi pioneer grin with dspr

    mi "Лена теперь тоже в клубе!"

    show sl pioneer surprise with dspr

    "Славя округлила глаза."
    sl "Что, правда? Ничего себе!"

    show un pioneer shy with dspr

    un "Да…"

    show sl pioneer smile with dspr

    sl "Ну точно, ты же говорила, что на флейте играешь!"
    th "Хорошо, хоть не на кожаной."
    "Автоматически вырвалась в голове тупая шутка."
    "Я глупо начал давиться смехом, благо никто не видел, так что я сразу успокоился."

    show un pioneer smile
    show mi pioneer happy
    with dspr

    mi "Ой, как здорово, что сегодня столько людей собралось! Я принесу всем чай!"

    hide mi
    show mi pioneer normal at cleft
    with good_dspr

    "Мику зашагала в подсобку."

    show sl pioneer smile2 with dspr

    sl "Стой, давай я тебе помогу!"
    mi "Нет-нет, я сама!"

    hide mi
    hide sl
    show sl pioneer smile at cright
    with dspr

    "Славя не стала настаивать, и села рядом со мной на диван."

    hide un
    hide sl
    show un pioneer smile at fright
    show sl pioneer smile at cright
    with dspr

    "Лена присела рядом, за Славей, и мы начали беседовать обо всяком."

    show black with clocks_in

    show mi pioneer normal at cleft
    hide black
    with clocks_out

    "Вскоре пришла Мику. На подносе у неё было четыре чашечки чая."
    "Я встал, и помог её раздать их, после чего сел обратно, а Мику облокотилась на пианино."
    "Славя отпила глоток, и сказала."
    sl "Слушайте, ребята, вы же какие-нибудь песни разучиваете?"
    sl "Не хотели бы организовать небольшой концерт, хотя бы тут, прямо перед зданием клуба?"

    show mi pioneer upset with dspr

    "Мику задумалась, поставив чашечку на поднос."
    mi "Идея конечно, отличная… {w}Но мы просто не успеем ничего подготовить, до конца смены несколько дней."
    mi "А из того, что есть? Никто нам не одобрит выступление с тремя композициями по тридцать секунд."
    mi "А если и одобрят, нас просто засмеют."

    show un pioneer normal
    show sl pioneer sad
    with dspr

    sl "Э-эх, этого я не учла. Жаль. Я бы помогла с организацией."

    show mi pioneer smile with dspr

    mi "Но нам ничего не мешает качественно выучить до конца одну, и исполнить для себя!"

    show un pioneer shy
    show sl pioneer surprise
    with dspr

    "Мы все многозначно посмотрели на Мику."
    mi "Сейчас…"

    hide mi
    show mi pioneer normal at left
    with dspr

    "Она взяла тетрадку с дивана, пролистнула несколько страниц, и развернув, показала нам."
    "Заголовок гласил:"
    "«{font=mods/simple_happiness_mod_efim/gui/fonts/NotoSansJP-Regular.ttf}最も暖かい夏{/font}» (Mottomo atatakai natsu)."
    "А левее уже на русском."
    "«Самое тёплое лето»."
    "Ниже был текст полностью на японском."
    mi "Семён, мелодия которую ты сейчас разучиваешь, это же я сама написала."
    mi "А недавно придумала название, и текст для песни."
    "Я понял, к чему она клонит."
    me "Ты хочешь, чтобы мы её исполнили?"

    show mi pioneer happy with dspr

    mi "Да… Я буду на вокале, у тебя гитара. А для Лены я напишу партию на флейте."

    show un pioneer smile2 with dspr

    un "Ой, как здорово! Мне нравится!"

    show sl pioneer smile with dspr

    sl "И можете исполнить её прямо здесь, в клубе! И придёт, кто захочет, афишировать не будем."
    "Мику засмеялась."

    show mi pioneer laugh with dspr

    mi "Славечка, может получиться так, что ты будешь нашим единственным слушателем."

    show un pioneer smile with dspr

    un "А мне и так хорошо будет."
    "Все согласились."

    show mi pioneer smile with dspr

    play sound sfx_dinner_horn_processed fadein 0.25 volume 0.4

    "Некоторое время мы обсуждали детали того, как всё это будет происходить, пока не услышали горн."
    "..."

    stop ambience fadeout 1.0

    hide mi
    hide un
    hide sl
    show bg ext_musclub_day
    show un pioneer smile at fleft
    show mi pioneer normal at cleft
    show sl pioneer smile at right
    with dissolve1

    play ambience ambience_camp_center_day fadein 1.0

    "Всей толпой мы направились в столовую…"

    show bg ext_houses_day with dissolve

    "По пути порешали на том, что мои репетиции на сегодня закончатся, а после ужина, Мику с Леной вдвоём пойдут в клуб."

    show bg ext_square_day with dissolve

    "Им надо будет написать партию для флейты, и начать учить."
    "А я в нотной грамоте всё равно понимал чуть больше, чем ничего."
    "К тому же, учить свою партию я начал ещё несколько дней назад, и у меня уже почти полностью получалось."

    call set_time("sunset")

    show bg ext_dining_hall_near_sunset with dissolve1

    "Пока мы шли, вечер уже активно вступал в права."
    "На пороге столовой никого не было."
    me "Вот чёрт, сейчас свободный столик не найдём."

    show sl pioneer smile2 with dspr

    sl "Может, кто-то скоро уже закончит есть."

    stop ambience fadeout 1.0

    hide sl
    hide un
    hide mi
    show bg int_dining_hall_people_sunset
    show un pioneer smile at fleft
    show mi pioneer normal at left
    show sl pioneer smile at center
    show mt pioneer normal at right
    with dissolve1

    play ambience "<from 5.0>" + ambience_dining_hall_full fadein 2.0

    "Мы зашли в столовую, и отметились у вожатой."
    "Надо сказать, она была сильно удивлена, когда узнала, что Лена, оказывается, играет на флейте, и теперь со мной и Мику, состоит в музыкальном кружке."
    "Пока мы разговаривали, первые пионеры уже заканчивали есть, и освобождали столики."
    "Мы дождались первого полностью свободного, и сели есть все вместе."

    show black with clocks_in

    stop ambience fadeout 1.0

    hide mi
    hide un
    hide sl
    hide mt
    show bg ext_dining_hall_near_sunset
    show sl pioneer normal at right
    hide black
    with clocks_out

    play ambience ambience_camp_center_evening fadein 1.0

    "Приятно, за тем исключением, что котлета была уже подостывшая, отужинав, мы со Славей попрощались с девочками, и остались вдвоём возле столовой."
    "Я вдохнул свежий, чистый воздух, и спросил."
    me "Вот и снова вечер. Есть идеи, чем заняться до отбоя?"
    sl "Хм-м, да как-то нету."

    show sl pioneer smile with dspr

    sl "Можно просто немножко прогуляться."
    me "С удовольствием!"

    hide sl
    show sl pioneer smile close at right
    with good_dspr

    "Взявшись за руки, мы пошли в произвольном направлении, беседуя по дороге."

    show bg ext_square_sunset with dissolve

    "Вышли на площадь."
    "Честно говоря, я даже не следил, куда мы идём."
    "Я просто держал за руку прекрасную девушку, и наслаждался её компанией."

    show bg ext_houses_sunset with dissolve

    stop music fadeout 2.0

    "Начав подходить к домикам пионеров, мы услышали какой-то звук."

    show sl pioneer surprise with dspr

    play music "<from 0.0 to 11.0>" + music_list["kostry"] fadein 3.0 volume 0.15

    "Кто-то играл на электрогитаре."
    "Мы переглянулись."
    me "Алиса?"
    sl "Возможно."

    show sl pioneer smile with dspr

    sl "Она, скорее всего на сцене, пойдём посмотрим."
    me "Пойдем."
    "Ускорив шаг, мы направились в сторону сцены."

    stop music fadeout 1.0

    show bg ext_stage_normal_sunset with dissolve1

    play music music_list["kostry"] fadein 1.0 volume 0.9 noloop

    "Выйдя к сцене, мы и правда увидели на ней Алису, которая играла на электрогитаре."
    "Звук был не очень качественный, зато мягкий, тёплый. Как будто пропущенный через очень старый ламповый усилитель."

    show cg d4_dv_guitar with dissolve

    "Алиса играла, поставив одну ногу на колонку, полностью отдавшись музыке."
    "Она качалась в такт своим же ударам медиатором по струнам, и не замечала ничего вокруг."
    "Мы подошли ближе."
    "Алиса, по всей видимости, уже заканчивала партию."

    call calc_music_how_much_play

    hide sl
    hide cg
    show bg ext_stage_normal_sunset
    show sl pioneer smile at right
    with dissolve

    "Когда Алиса закончила играть, то посмотрела на нас."
    me "Здорово у тебя получается!"
    "Крикнул я."
    "Алиса улыбнулась, и положив гитару на колонку, спустилась к нам."

    play music music_list["so_good_to_be_careless"] fadein 2.0 volume 0.8

    show dv pioneer2 normal at cleft
    with good_dspr

    dv "Что, правда понравилось?"

    show sl pioneer smile2 with dspr

    sl "Да! Очень энергично звучит."
    me "Мы тебя ещё чуть ли ни на площади услышали."

    show dv pioneer2 smile with dspr

    "Алиса ухмыльнулась."
    dv "Вот как? В таком случае, я надеюсь, ещё кто-нибудь заценил!"
    sl "Ха-ха, будь уверена!"

    show dv pioneer2 normal with dspr

    dv "Ну ладно. А вы чего здесь?"

    show sl pioneer smile with dspr

    me "Мы просто гуляли."

    show sl pioneer surprise with dspr

    sl "Кстати, как?.. {w}Как после утрешней ситуации?"
    dv "Ай, да всё отлично! С Ульянкой мы помирились."
    dv "Ты же и сама знаешь, я не могу на неё долго обижаться."

    show sl pioneer smile with dspr

    dv "А весь этот сыр-бор вроде как, всё-таки никто не видел."
    dv "Так что, можно сказать, обошлось."
    sl "Вот и славно!"

    show dv pioneer2 smile with dspr

    dv "Кстати, не видела вас на ужине. {w}Ни вас, ни Лены с Мику. Куда делись?"
    me "Да мы просто в музыкальном клубе задержались, пришли, наверное, минут на десять позже."
    dv "Во-от, как? И что вы там вчетвером делали?"

    show sl pioneer normal with dspr

    "Славя посмотрела на меня."

    show sl pioneer smile with dspr

    "Я кивнул, и она начала рассказывать Алисе про то, что Лена вступила в клуб, и про нашу «генеральную» репетицию."
    "Пока Славя рассказывала, я жестом поманил всех за сцену, достал по сигарете себе и Алисе."

    call smoking_process(with_pause=1.0)

    show sl pioneer smile2 with dspr

    sl "Во-от, как-то так."

    show dv pioneer2 grin with dspr

    dv "Слушайте, а здорово вы это придумали!"
    sv "И не концерт, но себя показать можно, и на других посмотреть…"

    show sl pioneer smile
    show dv pioneer2 laugh
    with half_good_dspr

    dv "Может мне тоже поучаствовать? Хоть с нормальным усилителем сыграю, а не этим доисторическим чудовищем."
    me "Думаю, Мику будет не против! Чем больше народу, тем веселее. Только предупредить её надо."

    show dv pioneer2 smile with dspr

    me "Она после ужина с Леной в клуб пошла, возможно, они ещё там."
    dv "Тогда я побежала! Даже если их там не найду, всё равно они же вместе живут, зайду к ним. {w}Спасибо!"

    show dv pioneer2 smile at run_away_right
    pause(0.5)
    hide dv with dspr

    "Алиса пулей залетела на сцену, отключила гитару, и взяв её за гриф, быстрым шагом направилась в сторону клуба."

    show sl pioneer smile2 with dspr

    "Славя улыбнулась, и сказала."
    sl "Мы так точно весь лагерь перед клубом соберём."
    me "Ха-ха-ха, не думаю. Вроде как никто больше ни на чём не играет."
    me "Только если не окажется, что Электроник у нас, мастер губной гармошки."

    show sl pioneer laugh with dspr

    "Славя рассмеялась, и взявшись за руки, мы направились в сторону домиков."
    "Начинало темнеть."

    window hide

    stop ambience fadeout 1.0
    stop music fadeout 2.0

    show black with clocks_in

    play ambience ambience_camp_center_night fadein 1.0
    play music music_list["forest_maiden"] fadein 2.0 volume 0.83

    hide sl

    call set_time("night")

    show bg ext_house_of_sl_night
    show sl pioneer smile2 close at center
    hide black
    with clocks_out

    pause(1.0)

    window show

    "Проводив Славю до домика, мы вновь обнялись, и поцеловались."
    "Но в этот раз, поцелуй был более уверенный. Но от этого, не менее приятный."
    "Прошло уже стеснение первых неловких прикосновений и объятий, так что я уже не скрывал ни своих чувств, ни реакции своего организма."
    "Славя, по всей видимости, брала с меня пример."
    "Невыполненным из списка любовных дел оставалось только словесное признание. {w}Я твердо намеревался решить это в ближайшее время."

    show sl pioneer shy with good_dspr

    "Закончив поцелуй, и продолжая стоять в обнимку, славя немного отвела взгляд, и сказала."
    sl "Сём, я… {w}Я понимаю, что, возможно, ты хочешь большего…"
    sl "Но… {w}Мне нужно немного времени. Это у меня впервые."
    th "Неужели у такой красавицы, как она, никогда не было парня?"
    me "Тебе не нужно за это извиняться. Всё хорошо. Напротив, это даже правильно."
    me "Продолжим, когда сама этого захочешь."

    show sl pioneer tender with good_dspr

    sl "Сёма…"
    "Она посмотрела на меня глазами, полными любви."
    "Моё сердце сжалось."

    show blink
    pause(1.0)
    hide blink
    show unblink

    "Она поцеловала меня ещё раз, и побыв ещё некоторое время вместе, мы попрощались."

    hide unblink

    hide sl
    show sl pioneer smile2 far at center
    with long_dspr

    "Заходя в дом, Славя послала мне воздушный поцелуй. Я поймал его."

    hide sl with dspr

    stop music fadeout 2.5

    "..."

    show black with clocks_in

    play music music_list["meet_me_there"] fadein 2.0 volume 0.6

    show bg ext_house_of_mt_night
    hide black
    with clocks_out

    call smoking_process

    "Я сидел на корточках, за деревом недалеко от нашего с вожатой домика."
    "У меня в пачке оставались две последние сигареты, но меня это не заботило."
    "Хотя я и понимал, что как только они закончатся, я начну по стенам лазить."
    th "Что-нибудь придумаем."
    "Отлично. {w}«Что-нибудь» это уже не «ничего». {w}Осталось понять, «что» конкретно."
    "Я докурил сигарету, и зашёл в дом."

    stop ambience fadeout 1.0

    show bg int_house_of_mt_night
    show mt nightdress normal at fright
    with dissolve

    play ambience ambience_int_cabin_night fadein 1.0

    "Вожатая ещё не спала, но уже сидела в ночнушке на постели вместе с книгой."
    mt "О, Семён!"
    me "Это я."
    mt "Дверку закрой на ключ."
    me "Точно!"
    "Я закрыл дверь, и начал готовиться ко сну."
    me "Как вы провели сегодня день?"

    show mt nightdress grin with dspr

    mt "Ты знаешь, очень неплохо! {w}А ты как, помимо деятельности в клубе."
    mt "Там я знаю, что у тебя всё хорошо."
    me "Я полон счастья, Ольга Дмитриевна! Даже не знаю, скоро расплёскивать начну."
    mt "Эх, молодая любовь!"

    show mt nightdress normal with dspr

    mt "Вот знаешь, Семён, почему я тебя не ругаю за то, что ты возвращаешься после отбоя?"
    me "Почему?"
    mt "Потому что ты со Славей. А ей я доверяю на сто процентов."
    mt "Только я тебя очень прошу."

    show mt nightdress sad with dspr

    mt "Вы молодые, гормоны бурлят."
    mt "Но не наделайте глупостей. Хотя бы, пока вы здесь."
    "Я немного покраснел."
    th "Очень откровенно с её стороны."
    me "Ну вы как обо мне думаете, Ольга Дмитриевна? Конечно нет."

    show mt nightdress normal with dspr

    "Вожатая покачала головой."
    mt "Не загадывай наперёд. Никогда не знаешь, что произойдёт завтра."
    "В этом она была права. Я сам убедился в этом на собственной шкуре."
    mt "В медпункте есть… {w}Всё, что нужно. Если надо будет, Виола даст."
    "Я вогнался в краску ещё больше, и ответил."
    me "Хорошо…"
    me "Спасибо, буду иметь в виду."
    "Я лег в постель, и накрылся простынью."

    play sound sfx_lamp_turn_on_off volume 0.9

    show bg int_house_of_mt_night2
    hide mt
    with dissolve

    "Я услышал, как вожатая положила на стол книгу, а затем встала и выключив свет, легла обратно."
    me "А что… Бывали уже случаи?"
    mt "Ты не представляешь сколько. И это за мою маленькую карьеру вожатой."
    th "А говорят сейчас молодёжь испорченная."
    me "Да уж…"

    stop music fadeout 3.0

    me "Спокойной ночи, Ольга Дмитриевна."
    mt "Спокойной ночи, Семён."
    "Я закрыл глаза, и начал погружаться в царство Морфея…"

    window hide

    $ renpy.pause(1.5, hard=True)

    jump simple_happiness_mod_day_none


# День ???
label simple_happiness_mod_day_none:
    $ renpy.block_rollback()

    call custom_day_screen(5, "Простое Счастье. День ???", "day_none")

    hide flickering_noise1
    hide flickering_noise2
    hide flickering_noise3
    show cg sleep_nothingness
    hide black
    with dissolve

    $ set_mode_adv()

    call set_time("night")

    play music music_list["drown"] fadein 3.0 volume 0.8

    $ renpy.pause(3.0, hard=True)

    window show

    "Я находился в некой пустоте."
    "Вокруг не было… Ничего? То есть, буквально. Даже меня там не было."
    "Я не чувствовал своей ориентации в пространстве, и даже не понимал, сижу я, лежу, или стою."
    "И даже зрение не спасало."
    "Совру, если скажу, что я ничего не видел. Это ощущалось иначе, как если бы я просто оказался в абсолютно тёмном помещении. Я {b}не{/b} видел."
    "Просто не мог. Потому-что было нечем."
    "Я просто ощущал своё присутствие {b}там{/b}."
    "Не было ни холодно ни жарко. Было никак."
    "Абсолютное {b}ничего{/b}, где {b}никто{/b} не находится."
    "..."
    "Мне стало грустно, если {b}здесь{/b} было уместно понятие {b}Я{/b}."
    th "И что, на этом всё закончится? Я не признаюсь Славе в любви, мы не сыграем с девочками у клуба все вместе?.."
    th "Вот так закончится моя история? Посреди ёбаного ничего?"
    th "Мне даже не нужны были ответы, вопросами от которых я старался задаваться первые дни."
    th "Не нужен был мой мир."
    th "Всё, чего я хотел, быть рядом с человеком, которого по-настоящему полюбил впервые за всю свою жизнь."

    play sound sfx_light_candle volume 0.7

    "Внезапно, я услышал, как кто-то чиркает зажигалкой."
    th "У меня уже галлюцинации?"
    "Моё сознание вырисовывало странную картину."

    play sound2 sfx_water_drops volume 0.35 loop

    "Я очень смутно наблюдал какое-то тёмное помещение. Рядом, кажется, капала вода."
    "Почти сразу я понял, что не умираю."
    "Ко мне, очень медленно, и как-то вязко, приходили чувства. Я начинал ощущать пространство вокруг, хотя всё ещё определить ориентацию было невозможно."
    "Через мутную пелену ко мне возвращалось зрение."

    hide cg
    show bg int_catacombs_living at blurring
    show prologue_dream
    with dissolve5

    "Я видел перед собой какое-то странное помещение, похожее на бомбоубежище."
    "Постепенно, я всё более явно начал понимать, что {u}нахожусь{/u} в этом помещении."
    "Ноги почувствовали одетую обувь и твердый пол под ней."
    "По коже пробежал холодок от сырого помещения."

    stop music fadeout 1.0
    play sound3 sfx_head_heartbeat fadein 0.5 volume 1.15 loop

    show bg int_catacombs_living at deblurring
    with dissolve

    "Как тут, меня качнуло, только, словно бы изнутри, и сознание вернулось ко мне в полной мере."
    "Я глубоко вдохнул, и мощно выдохнул."
    "Начало подташнивать, и я оперся руками на колени."
    th "Конечно, не каждый день приходится пребывать в астрале, а потом возвращаться в физический мир."
    "Полностью отдышавшись, я наконец выпрямился, и посмотрел перед собой."

    stop sound3 fadeout 2.0
    play music music_list["door_to_nightmare"] fadein 4.0 volume 0.9

    hide prologue_dream
    show pi normal far at center
    show uv guilty far at fright
    with dissolve

    "В другом конце комнаты стоял пионер."
    th "Так, ну по крайней мере можно с уверенностью говорить о том, что я всё ещё в Совёнке. Это радует."
    "А справа, на нижнем ярусе кровати сидела странная девочка."
    "Одета она была в какое-то разорванное платье, а на голове у неё были… Уши? То есть, кошачьи уши."
    "Я снова посмотрел вперёд."

    play sound3 sfx_smoking_cigaret volume 0.3

    "Пионер, стоящий передо мной, выдохнул дым сигареты, которую курил, и заговорил."
    pi "Ну и чё ты молчишь?"
    "Я несколько секунд помолчал."

    pause(1.0)

    stop sound2 fadeout 1.0
    play sound2 sfx_water_drops volume 0.15 loop

    me "Это ты мне?"
    pi "Конечно тебе."
    pi "Не вижу обоссаных штанов, и не слышу криков «А-а-а, кто вы?», «Где я?» «Что вам от меня нужно?»."
    "Он очень мерзко подражал высокому, испуганному голосу."
    "Кстати, его внешний вид мне кого-то напоминал… Я точно его уже где-то видел, но не мог разглядеть его глаз из-за чёлки и полумрака в комнате."
    me "Да я, знаешь, уже привык просыпаться непонятно где, и задавать эти вопросы. Надоело."

    show pi smile with dspr

    "Пионер расхохотался."
    pi "А-ха-ха! Ну ты молодец."
    "Он сплюнул, и подошёл ближе."

    hide pi
    show pi normal
    with half_good_dspr

    pi "Надоело ему. Как тебе могло это надоесть? Это твой первый виток."
    me "Что? Какой ещё виток?"

    show uv normal far with dspr

    uvp "Именно об этом мы и хотели поговорить."
    uvp "Милый, я потратила очень много сил, чтобы вытащить его сюда, и ты это знаешь. Не дай моим стараниям пропасть зря. Перемещения между лагерями очень нестабильны."
    th "Какого хера тут происходит?"
    pi "Ладно, ты права. Не будем терять времени."
    pi "Поздравляю, у тебя есть уникальная возможность задать несколько вопросов. Когда {b}Я{/b} посчитаю нужным, вопросы начну задавать {b}Я{/b}."
    "Зачем-то он два раза акцентировал внимание на слове «Я»."
    pi "Я жду."
    me "Задать вопросы? Может для начала объяснитесь, кто вы такие? {w}Я себе мирно заснул в домике вожатой, и оказался здесь."

    hide pi
    show pi normal at left
    with good_dspr

    "Пионер опять сплюнул, и прильнул к стене."
    pi "Я зачту это за первый вопрос."
    pi "Итак, кто мы такие? Я – Семён, а эта прекрасная девушка с кошачьими ушками и хвостом – Юля."

    show pi smile with dspr

    "Он оскалился."
    pi "М-м, ты даже не представляешь, как приятно под него пихать. Никогда не надоест."

    show uv grin far
    show pi normal
    with dspr
    pause(1.0)
    show uv normal far with dspr

    "Юля, кажется, повиляла хвостом."
    pi "Приятно познакомиться!"
    "Я застыл."
    "Так вот кого он мне напоминает! Это же вылитый я."
    "Только у него глаз не видно, да и веет от него... Недобрым. Как будто злодея из фильма вживую встретил."
    me "Подожди… {w}Это Я – Семён."
    pi "И тебя ничего не смущает?"
    me "Ты выглядишь как я…"
    "Этот тип, кем бы он ни был, наиграно воскликнул."
    pi "Браво, Холмс! Наконец-то до тебя начинает доходить."
    uv "Сёма, не заводись."
    me "То есть ты – это я? Или я это ты?"
    pi "Всё вместе."
    me "Хорошо… А кто тогда она? Я показал на девушку."
    pi "Об этом она лучше сама тебе расскажет. Юленька?"

    show uv smile far with dspr

    uv "Ну что за дурацкие вопросы? Я – это я. И всё тут."

    show pi smile with dspr

    pi "Ничего другого она тебе не скажет. Хорошо хоть не тупо следует алгоритму, как всё и все здесь."
    me "Какому ещё алгоритму?"

    show pi normal
    show uv normal far
    with dspr

    pi "Об этой загадке мы подумаем позже. Я жду ещё вопросы."
    "Он начинал меня бесить своим высокомерием."
    me "Ладно. Где мы?"
    pi "Сука, ну что за тупые вопросы? Поинтереснее ничего нет?"
    pi "Мы в пионерлагере Совёнок. Конкретно сейчас в заброшенном лагере. Но у себя в витке ты сюда не ходил."
    me "Я тебя не об этом спрашиваю! ГДЕ этот пионерлагерь??"
    pi "М-м-м, тебе ответ попроще? Отвечаю: он нигде, и везде одновременно."
    "Я начал натурально закипать."
    me "Блять, я тебя не о метафизике спрашиваю, и не о квантовых флуктуациях!"
    me "«Нигде и везде одновременно», как прикажешь это понимать!?"
    pi "Как хочешь, так и понимай."

    pause(1.0)

    stop sound2 fadeout 1.0

    "Он секунду помолчал, и продолжил."
    pi "Ты не единственный, кто попал сюда. {b}НАС{/b}, Семёнов, проснувшихся у ворот пионерлагеря Совёнок, много. Бесконечно много."
    pi "Но даже не думай попытаться отыскать их. Они в параллельных лагерях. Как параллельные миры."
    "Кажется, он наконец-то начал говорить что-то дельное, но всё ещё создавалось ощущение, что он несёт какую-то ахинею."
    me "Так, допустим. И что дальше?"

    call smoking_process

    "Пионер достал ещё одну сигарету из пачки, и закурил."
    pi "А дальше? Дальше неделя смены, и снова пробуждение в автобусе. И так до бесконечности."
    me "Как «день сурка»? Ты правда думаешь, что я реально поверю в этот фантастический бред?"
    pi "Откровенно говоря, мне похуй, поверишь ты, или нет. Для меня это всё равно не имеет никакого смысла."
    pi "Иногда смена будет заканчиваться хорошо. И может даже показаться, что этот кошмар кончился."
    pi "Но снова и снова ты будешь просыпаться в этом ебучем автобусе перед этим ебучим лагерем."
    pi "Будешь искать ответы, бороться. Дойдешь до безумства."
    pi "Одно время я только и делал, что резал всех без разбору, а потом выпиливался, чтобы повторить всё вновь."
    pi "Но и это бессмысленно."
    me "И что, отсюда никак не выбраться? Я, то есть мы, то е… {w}Короче ты понял."
    me "Обречены на бесконечное существование здесь? И никто не будет помнить наш прошлый раз?"
    pi "Долгое время ты и сам не будешь помнить предыдущие циклы."
    pi "Что уж говорить об этих тупых куклах, которые годятся только на то, чтобы воспользоваться ими, как грязной шлюхой, и порезать на кубики для супа."
    "Мне стало дурно."
    th "Господи, что за маньяк?"
    "Я полез по карманам в поисках оставшихся сигарет."
    pi "Не найдешь. На."
    "Он протянул мне пачку и зажигалку."

    call smoking_process

    "Я с опаской принял, но всё же достал сигарету, и закурил. Вернул ему."
    me "И долго ты этим занимаешься?"
    pi "Я не знаю. Во-первых, я не знаю, сколько витков прошло с момента, как я начал осознавать себя."
    pi "Во-вторых, когда по моим прикидкам, срок перевалил циклов за сто, я перестал считать. Бессмысленно."
    pi "Но больше тысячи, это точно."
    th "Охренеть просто. Кто-нибудь, разбудите меня."
    pi "Это продолжалось, пока я не встретил её."

    show uv smile far with dspr

    "Он показал на Юлю. Она всё так же сидела на кровати, и с интересом разглядывала свои ноги."
    pi "Она не такая, как остальные. Она всё и про всех помнит. И про меня."
    pi "После того, как я её впервые нашел, теперь всегда сразу иду искать её."

    show uv normal far with dspr

    me "Мне нужно подумать."
    pi "Да пожалуйста. Думай, сколько влезет, пока я курю."
    "Я сполз по стене, и сел на корточки."

    pause(1.0)

    "Что мы имеем? Если этот психопат прав, я нахожусь в некоторой временной аномалии. И его слова про кукол. Что он имеет в виду?"
    "Что все пионеры ненастоящие? Нет, я конечно замечал некоторые странности в их поведении. Но Славя…"
    "Всё было по-настоящему. Я по-настоящему испытывал чувства, нежность её прикосновений… Нет, этого не может быть."
    "Я знаю, что она настоящая. Что они ВСЕ настоящие. Этот тип просто крышей поехал."
    
    pause(1.0)

    "Я встал."
    me "И что, никому не удавалось отсюда выйти?"
    "Пионер сделал последнюю затяжку, и потушил окурок носком ботинка."
    pi "Я не знаю. Некоторых я уже долго не видел. Может им и правда удалось выйти, может, они также начали скрываться, как и я."
    pi "Единственное, что отложилось в памяти… Был тут один. Отходил десяток, или даже меньше витков. Я его навещал пару раз."
    pi "Так под конец он тут такое учудил. Я думал, что его виток сейчас просто схлопнется. С тех пор я его не видел."
    me "Почему ты не последовал его примеру?"
    pi "А я не знаю, что он сделал. {w}Я не могу долгое время находиться в других витках, меня начинает буквально выворачивать наизнанку."
    pi "Единственное, что могу сказать, он наверняка за все свои циклы перетрахал весь лагерь. {w}Ну да это не новость."
    th "У него явно какая-то фикция на всём, что связано с сексом."
    me "Ладно…"
    me "Это всё, конечно, очень интересно, но я вам зачем?"

    show pi smile with dspr

    pi "Динь-динь, бинго! Как удобно ты попал, я как раз собирался переходить к тебе. Время на вопросы вышло."

    stop music fadeout 2.0

    hide uv
    show uv normal at right
    show pi normal
    with good_dspr

    pause(1.0)

    play music music_list["orchid"] fadein 2.0

    "Юля, до этого не обращавшая внимания на наш диалог, встала и подошла к нам."
    uv "Мы позвали тебя для того, чтобы поговорить о твоём витке."
    pi "Видишь ли, Юля, судя по всему, находится во всех витках одновременно. Не спрашивай как, я сам не понимаю."
    pi "И в какой-то момент, она заметила что твой виток очень сильно отличается от остальных. У тебя всё идёт… {w}Не по сценарию."
    pi "Ровно с того момента, как с тобой начала везде таскаться эта твоя, златовласая."
    me "Её зовут Славя."
    "Пионер не обратил никакого внимания на моё замечание, и продолжил."
    pi "Даже раньше. Сразу, как ты проснулся в автобусе, и нашёл там сигареты. Этого уже {i}не должно было{/i} произойти."

    show uv smile with dspr

    uv "Но переломный момент произошёл, когда ты вступил в музыкальный кружок, но продолжил… М-м, как бы это…"
    pi "Продолжил мутить со Славей."
    pi "Судя по всему, это сломало весь твой виток. {w}И я не знаю, что произойдёт."
    pi "А поверь мне, у меня их было достаточно, чтобы наизусть выучить каждую возможную вариацию."
    "У меня голова шла кругом. Я уже с трудом соображал."
    me "И вы… Вытащили меня, чтобы сказать об этом?"
    pi "Вообще, это была её идея. Я хотел просто понаблюдать."
    th "Я просто хочу свалить отсюда."
    me "Что ж… Очень мило с вашей стороны, но с меня достаточно."

    show uv normal with dspr

    uv "Просто предупреждаю."
    uv "Неправильные витки обычно сразу исчезают, но твой кажется удивительно стабильным, но останется ли он таким, вопрос открытый."
    me "Спасибо за заботу."
    me "Можно уже наконец мне… {w}Я…"
    "Я почувствовал, что мир перед глазами начинает плыть."

    hide uv
    hide pi
    show bg int_catacombs_living at blurring
    with dissolve2

    "Я упал на колени, а мир передо мной начал рассыпаться на части."
    pi "Возможно ты тот, к кому лагерь оказался благосклонен. Цени это."

    stop music fadeout 3.0

    hide window

    show black with dissolve2

    "Я ничего не мог ответить. Перед глазами осталась только пустота…"

    window hide

    $ renpy.pause(1.5, hard=True)

    jump simple_happiness_mod_day5


# День 5
label simple_happiness_mod_day5:
    $ renpy.block_rollback()
    $ backdrop = "days"
    $ new_chapter(5, u"Простое Счастье. День 5")

    call set_time

    $ set_mode_adv()

    play ambience ambience_int_cabin_day fadein 3.0 volume 0.9
    play sound sfx_hell_alarm_clock fadein 1.0 volume 0.8
    play sound2 sfx_head_heartbeat fadein 1.0 loop

    window show

    "Я проснулся от ужасающей головной боли."
    "Кажется, я даже вскрикнул."
    "Голова вот-вот была готова взорваться."
    "Я схватился за голову, и только через несколько секунд понял, что это будильник."

    show bg int_house_of_mt_day
    show mt swim surprise at cright
    hide black
    show unblink

    "Я открыл глаза, и часто дышал."
    "Я весь был в холодном поту."
    mt "Семён! Ты чего кричишь? Семён!"
    "Вожатая потрясла меня за плечо."
    mt "Ты испугался, что-ли? Это всего лишь будильник!"

    stop sound2 fadeout 3.0

    "Постепенно я начал приходить в себя."
    me "Буб… {w}Что? {w}Откуда у нас будильник?"
    mt "Вчера на складе нашла, решила поставить. Так же удобнее, чтобы не проспать."
    me "Понятно…"
    "Я упал обратно на подушку."
    mt "А чего кричал-то? Я перепугалась."
    "Я попытался прокрутить в голове прошедшие события… Но там была какая-то каша."
    th "Кажется, я был… {w}Где-то. {w}И моя «злая» копия и кошко-девочка меня предупреждали об опасности моего «уникального цикла»."
    th "Ну и бред."
    me "Да так, кошмар приснился."
    "Я посмотрел на вожатую, и только сейчас понял, что она стоит в одном нижнем белье."

    show mt swim normal with dspr

    mt "Понятно. Фух, ну ты меня и напугал."
    mt "Я ж подскочила, сначала будильник, потом ты начал кричать. Перепугалась."
    me "Извините."
    mt "Да чего уж там… Бывает."

    play music music_list["confession_oboe"] fadein 2.5 volume 0.8

    hide mt
    show mt swim normal at fright
    with dspr

    "Хоть вожатая и завела будильник на довольно раннее время, я решил, что быстрее сброшу с себя всю произошедшую муть, если встану сразу."
    "..."
    "Я начал заправлять постель, одеваться, и готовиться пойти умыться."
    "Начав укладывать подушку, я заметил какой-то предмет, край которого торчал из-под матраса."
    
    show mt swim smile with dspr

    mt "Семён, не поворачивайся, я оденусь."
    me "Хорошо…"

    hide mt with good_dspr

    "Я достал находку. {w}Этим предметом оказалась пачка сигарет. Но не запечатанная. Там не было двух штук."
    th "Что за… {w}Так мне не приснилось? И что это, «привет» из другого мира?"
    "Я решил что некогда сейчас размышлять, и быстро убрав пачку в карман, продолжил застилась постель."

    show mt pioneer normal at right
    with good_dspr

    "Вожатая в это время оделась, и начала готовить кофе. Я не отказался от своей порции. Сейчас он был мне просто необходим."
    "Заправив кровать даже лучше обычного, я взял пакет с умывальными принадлежностями, и направился к умывальникам…"

    stop ambience fadeout 1.0

    show black with clocks_in

    play ambience ambience_camp_center_day fadein 1.0

    hide mt
    show bg ext_houses_day
    hide black
    with clocks_out

    "Я шел по тропинке, и вдыхал чудесный утренний букет ароматов."
    th "И тот злодей утверждал, что всё это иллюзия, фикция? {w}Не верю."
    "Думал я по дороге."
    th "Хотя, даже если так, я согласен. Оставляйте меня."
    "Промелькнуло в голове."
    "Я посмеялся собственной беззаботности, и продолжил идти в сторону умывальников."

    play sound sfx_open_water_sink
    play sound2 sfx_water_sink_stream fadein 1.0 loop

    show bg ext_washstand2_day with dissolve1

    "Сегодня холодная вода уже не обжигала, а наоборот, бодрила, и сразу придавала сил."
    "..."

    play sound sfx_close_water_sink
    stop sound2 fadeout 1.0

    "Закончив с умыванием, и чисткой зубов, я сложил всё в пакетик, и уже собирался уходить, как вдруг…"

    stop music fadeout 2.0

    show blink
    show black
    with dissolve

    "Мне закрыли глаза."

    play music music_list["she_is_kind"] fadein 2.0 volume 0.8

    "Я сразу понял, кто это, так как уже чувствовал эти руки у себя на лице."
    "Сердце моё, от счастья, чуть не упало на утреннюю траву, покрытую росой."
    me "Славя!"

    hide blink
    hide black
    show bg ext_washstand_day
    show unblink
    with dissolve

    show sl pioneer smile2 at cright
    with dspr

    "Глаза мои вновь увидели этот дивный мир, и перед собой я увидел Славю."

    hide unblink

    "Но сегодня она была не в спортивной форме, а в пионерской."

    hide sl
    show sl pioneer shy close at cright
    with half_good_dspr

    "Она кротко поцеловала меня в губы."

    hide sl
    show sl pioneer smile2 at cright
    with half_good_dspr

    sl "Доброе утро, Сёма! Сегодня опять пораньше?"
    me "Утречка, Славя! Да, вижу ты тоже умываться пришла?"
    sl "Да."
    me "Тогда давай я тебя подожду."

    hide sl
    show sl pioneer smile at right
    with good_dspr

    play sound sfx_open_water_sink volume 0.4
    play sound2 sfx_water_sink_stream fadein 1.0 volume 0.4 loop

    "Я стоял рядом со Славей, пока она умывалась, и мы, не торопясь, беседовали."
    "Не торопясь, ещё и потому, что ей было неудобно отвечать то с намыленным лицом, то с зубной щеткой во рту."
    "..."

    play sound sfx_close_water_sink volume 0.4
    stop sound2 fadeout 1.0

    "Когда она закончила гигиенические процедуры, мы пошли обратно к домикам…"

    show bg ext_houses_day with dissolve

    me "Знаешь, мне сегодня кошмар приснился."
    
    show sl pioneer surprise with dspr

    sl "Ой, правда? Я вот вообще, боюсь кошмаров, особенно когда сплю одна."
    me "Да я и сам в холодном поту проснулся."
    sl "Расскажешь?"
    me "Да."
    "Я вкратце описал всё, что происходило во сне, от пребывания нигде до разговора со злой копией себя и девочкой-кошкой."

    show sl pioneer sad with dspr

    sl "Да уж, звучит очень страшно. Я бы вообще, наверное, расплакалась, если бы мне такое приснилось."
    sl "Это же ужас!"

    show bg ext_house_of_sl_day with dissolve

    "Мы подошли к домику Слави."
    me "К счастью, это всего лишь сон."
    me "Я ни за что не собираюсь тебя терять."

    hide sl
    show sl pioneer tender at center
    with good_dspr

    sl "Сё-ема!"
    "Славя обняла меня, и поцеловала. Мы попрощались до завтрака."

    stop ambience fadeout 1.0

    hide sl
    show bg int_house_of_mt_day
    show mt pioneer normal at right
    with dissolve1

    play ambience ambience_int_cabin_day fadein 1.0
    
    "Вернувшись в домик, я сложил все умывальные принадлежности в ящик, и мы с вожатой сели пить кофе."
    "..."
    "После приятного, бодрящего напитка, мы отправились в столовую."

    stop ambience fadeout 1.0

    show black with clocks_in

    play ambience ambience_camp_center_day fadein 1.0

    hide mt
    show bg ext_dining_hall_near_day
    show mi pioneer normal at left
    show un pioneer normal at fleft
    show dv pioneer normal at fright
    show sl pioneer normal at cright
    hide black
    with clocks_out

    "На входе в столовую Ольга Дмитриевна отошла куда-то в сторону, её позвал вожатый из другого отряда."
    "А я на входе встретил Мику, Алису, Славю и Лену."

    show dv pioneer smile with dspr

    dv "Ну наконец-то! Пойдёмте скорее, пока столики свободные есть!"

    stop ambience fadeout 1.0

    show bg int_dining_hall_people_day with dissolve1

    play ambience ambience_dining_hall_full fadein 1.0

    "Зайдя внутрь, и получив свои порции, мы сели за столик у окна."

    show sl pioneer smile with dspr

    sl "Алиса, ну что, рассказывай. Нашла вчера Мику с Леной?"

    show un pioneer smile2
    show mi pioneer grin
    with good_dspr

    "Мику с Леной посмотрели друг на друга, и улыбнулись."
    dv "Ой, да-а. Такая беготня получилась, на самом деле."

    show un pioneer smile
    show mi pioneer smile
    with dspr

    dv "Сначала я пошла в клуб, там было закрыто. Я подумала, что девочки уже закончили."
    dv "Пошла к ним в домик. Но там тоже никого! Я уже разозлилась, но хорошо, под руку попался проходивший мимо Электрон."
    dv "Он сказал, что не видел их, но в клубе горит свет."
    dv "Уже вся взбешённая, я опять пошла в клуб, ну, и нашла их там. {w}Оказывается, они просто в туалет вдвоём ходили!"

    show mi pioneer happy with dspr

    mi "Хи-хи! Ну темно уже было, страшно. Ты же не обижаешься, Алисонька, за этот маленький конфуз?"
    dv "Конечно нет. Зато я теперь с вами, и буду исполнять свою композицию на вашей генералке."
    un "Слушайте, ребята, мне так нравится, что нас всё больше собирается. Так здорово!"

    show mi pioneer smile with dspr

    mi "Ага. Эх, по скорее бы завтра! Только надо будет обязательно всем ещё по паре раз отрепетировать."
    mi "У нас получается в программе: (Мику стала загибать пальцы)"
    mi "Мои «Воспоминания»."
    mi "Наше трио с «Самым теплым летом»."
    mi "И Алиса с… Хо-о, как ты говорила, называется?"

    show dv pioneer grin with dspr

    dv "«Костры»!"

    show dv pioneer smile
    show mi pioneer happy
    with dspr

    mi "И «Костры» Алисы это три. Неплохо!"
    "Все согласились."

    show sl pioneer surprise with dspr

    sl "А вы успеете за пол дня всё отрепетировать?"

    show un pioneer shy
    show mi pioneer shocked
    show dv pioneer surprise
    with half_good_dspr

    "Мы переглянулись."
    dv "Почему за пол дня?"

    show sl pioneer smile2 with dspr

    sl "Так сегодня же четверг. Пляж!"
    "Девочки разразились возгласами по типу «Бли-ин, точно!» и «Ё-моё, как мы забыли!»."
    "Я же этого не знал, так что и удивляться мне было нечему."
    me "А почему пляж именно в четверг?"

    show dv pioneer smile
    show sl pioneer laugh
    with dspr

    sl "Не знаю. Но кто-то шутит, что раз четверг – рыбный день, значит и нам надо поплавать. Ха-ха!"
    "Я посмеялся в ответ."

    show un pioneer smile
    show mi pioneer happy
    with dspr

    mi "А вечером же ещё и баня, получается?"
    me "О-о, вот баня — это хорошо! Давно пора."

    show sl pioneer smile
    show mi pioneer smile
    with dspr

    "Остаток трапезы мы продолжали обсуждать планы на ближайшие дни."
    "Например, Мику с Алисой решили дополнить её гитарную композицию ударными."
    "Мику, оказывается, умела играть и на барабанах."
    "..."

    stop ambience fadeout 1.0

    show black with clocks_in

    play ambience ambience_camp_center_day fadein 1.0

    show bg ext_square_day
    hide black
    with clocks_out

    "Выйдя из столовой, мы всем составом направились в сторону домиков чтобы взять с собой на пляж необходимые вещи."
    th "Вещи… {w}А плавать я в чём буду!?"

    stop music fadeout 2.0

    "Я озвучил эту мысль девочкам."

    show un pioneer shy with dspr
    show mi pioneer surprise with dspr

    mi "О-хоо-ё!"

    show dv pioneer grin with dspr

    dv "Да-а, засада."

    show sl pioneer smile2 with dspr

    sl "Без паники! Оставленные вещи должны храниться у вожатой, так?"
    sl "Я уверена, у неё найдутся плавки Семёну по размеру."
    "Я немного скривился."

    show sl pioneer laugh with dspr

    sl "А-ха-ха, да ты не переживай. Конечно, там всё стиранное."
    th "Это и правда успокаивает."

    show un pioneer smile
    show dv pioneer smile
    show mi pioneer smile
    show sl pioneer smile2
    with good_dspr

    me "Ну что же, тогда попытаем счастья…"

    play music music_list["she_is_kind"] fadein 2.0 volume 0.8

    hide un
    hide dv
    hide mi
    hide sl
    show bg ext_houses_day
    with dissolve1

    "Когда мы прошли площадь, откололась Алиса, а в нашем «районе», сначала Славя, а потом и Мику с Леной."
    "Я же пошёл к своему домику."

    show bg ext_house_of_mt_day
    show mt pioneer normal panama far at fright
    with dissolve

    "На подходе я заметил Ольгу Дмитриевну, которая уже собиралась уходить, держа в руке купальник и полотенце."
    me "Ольга Дмитриевна, постойте!"

    hide mt
    show mt pioneer normal panama at cright
    with half_good_dspr

    "Я быстро приблизился к ней."
    mt "Семён, что такое? Идешь на пляж?"
    me "Именно поэтому я так к вам спешил. Такое дело…"
    "Я объяснил всю ситуацию."

    show mt pioneer grin panama with dspr

    mt "У-у, напугал кота сметаной."
    mt "В шкафчике с моей стороны, на нижней полке забытые вещи пионеров с других смен. Там, думаю, точно найдешь."
    th "Значит, Славя не ошиблась."
    me "Спасибо!"

    show mt pioneer smile panama with dspr

    "Вожатая улыбнулась."
    mt "Всегда пожалуйста!"
    mt "Жду на пляже!"
    me "Всенепременно!"

    show mt pioneer smile panama at walk_away_right
    pause(1.0)
    hide mt with dspr

    "После этих слов она удалилась, но сразу заходить в дом я не стал."
    "Сначала дождался, пока вожатая скроется, покурил за домом, и только потом зашёл внутрь."

    stop ambience fadeout 1.0

    show bg int_house_of_mt_day with dissolve

    play ambience ambience_int_cabin_day fadein 1.0

    "Уже в домике, открыв нужный шкафчик, я покопался в вещах, там, где сказала вожатая, и довольно быстро действительно нашёл черные мужские плавки подходящего размера. Чистые."
    me "Отлично! Годится."
    "Заключил я, и взяв полотенце, перекинул его через плечо, и насвистывая какую-то знакомую мелодию, покинул дом, закрыв его своим ключом."

    stop ambience fadeout 1.0
    stop music fadeout 2.0

    play sound sfx_clocks fadein 0.5

    show black with clocks_in

    play ambience ambience_lake_shore_day fadein 1.0

    show bg ext_beach_day
    hide black with clocks_out

    stop sound fadeout 0.5
    play music music_list["my_daily_life"] fadein 2.0 volume 0.8

    "Через несколько минут я вышел к пляжу."
    "Там уже было довольно много пионеров разных возрастов, которые играли, купались, или просто лежали под Солнцем."
    "Я посмотрел на небо."
    th "А денёк сегодня обещает быть жарким."
    "Переодевшись в кабинке, я взял свои вещи под мышку, и направился ближе к песку, глазами выискивая знакомые лица."

    show mt swim normal at left
    with good_dspr

    "Первой встретилась вожатая. Она сидела на полотенце, и мазала руки кремом."

    show mt swim smile with dspr

    mt "Семён, вот и ты!"
    "Она посмотрела на меня сверху вниз."
    mt "Нашёл, да?"
    me "Да, спасибо!"
    mt "Не за что."

    hide mt with dspr

    "Я прошёл дальше."

    show us swim normal at fleft
    show dv swim normal at center
    with dspr

    "На глаза попались Алиса и, внезапно, Ульяна, которые лежали вдвоём."
    "Вокруг было довольно свободно, относительно других мест."
    me "Ну наконец-то хоть кто-то знакомый. Я к вам!"

    show dv swim smile with dspr

    "Алиса подняла на меня взгляд, и улыбнувшись, ответила."
    dv "Давай, падай! Мне уже надоело всех отгонять, а ещё, судя по всему, Лену с Мику и Славей ждать."
    "Я расстелил полотенце, и лёг рядом."

    hide us
    hide dv
    show cg d4_us_cancer
    with dissolve

    "Только сейчас я заметил, что Ульяна не просто лежит, а играется с речным раком."
    me "Ульяна, ты зачем бедное животное мучаешь?"
    dv "Бесполезно, я ей уже сколько раз говорила, и даже выкинула одного."
    dv "А она их всё ловит и ловит."
    us "Вот сейчас я ему клешни поотрываю, и попрошу поварих сварить на ужин!"

    hide cg with dissolve

    "Я ничего не ответил, и просто разлёгся, положив руки под голову, наслаждаясь приятным летним Солнцем."

    show blink

    "Если это не первый рак, которого она мучает, они точно скоро организуют восстание, и поднимут армию против огромного монстра в красном купальнике, который убивает их сородичей."
    th "Хы-хы, вот умора то будет."
    "..."
    dv "Семён, не хочешь искупаться?"
    me "Не-е, пока не хочу. Потом."
    "Судя по звуку, девочки встали, и направились к воде."
    mip "Вот он, давай скорее!"
    "Сзади послышался голос."

    hide blink
    show mi swim normal at cright
    show un swim normal at fright
    show unblink

    "Я открыл глаза, обернулся, и увидел подходящих Мику и Лену."

    hide unblink

    me "Что-то вы долго. А Славя где?"
    un "Мы вместе шли. Сейчас она подойдет."
    "Девочки подошли, и разложились рядом с местами Ульяны и Алисы."

    show mi swim happy with dspr

    mi "Ой, погода то какая хорошая. Уже жарко прям! Не плохо было бы и искупаться."
    slp "Я за!"

    show sl swim smile at left
    with dspr

    "Из-за моей спины вышла Славя, и улыбнулась мне."
    "Странно, что на других я как-то не обратил внимания, но её красоту в купальнике оценил сразу."
    me "У-у, ну теперь меня точно удар хватит. Рядом со мной же теперь два Солнца!"

    show un swim smile
    show mi swim smile
    show sl swim shy
    with dspr

    "Славя немного покраснела, и захихикала, а девочки, кажется, просто умилились."

    show sl swim smile2 with dspr

    "Славя разложила вещи рядом со мной, и обратилась ко всем нам."

    sl "Ну что, купаться идём?"
    "Мы все единогласно ответили «Да!», и направились к воде."
    "..."

    stop ambience fadeout 1.0
    stop music fadeout 2.0

    hide sl
    hide un
    hide mi
    show bg ext_water_day
    show sl swim smile at right
    show un swim smile at fleft
    show mi swim normal far at center
    with dissolve

    play ambience ambience_lake_shore_day fadein 1.0 volume 1.2

    "Вода была очень приятная."

    play music music_list["so_good_to_be_careless"] fadein 2.0 volume 0.85

    "Теплая, и чистая, так что купаться было одно удовольствие."
    "Мои навыки оставляли желать лучшего, так что я по большей части лишь ненадолго заплывал, делал короткий крюк и возвращался обратно на мелководье."
    "Славя плавала примерно также рядом со мной, а Лена вообще почти не заходила на глубину, и просто сидела по пояс в воде."
    "А вот Мику… Она сразу начала показывать класс."
    "Далеко и надолго заплывала, погружалась под воду и всплывала уже далеко в другом месте."
    th "Ну девочка-амфибия прям. И девочка-оркестр, по совместительству…"
    
    show sl swim smile2 with dspr

    sl "Мику! Ты где так плавать научилась?"

    hide mi
    show mi swim normal at center
    with good_dspr

    mi "А я не рассказывала?"
    
    show mi swim smile with dspr

    mi "Я же плаванием тоже занимаюсь. Даже несколько маленьких соревнований выигрывала."
    "Мы продолжили купаться ещё некоторое время."

    show dv swim smile at left
    with dspr

    "Под конец вообще подплыла Алиса, и начала брызгаться водой."

    show un swim smile2
    show dv swim grin
    show sl swim laugh
    with good_dspr

    "Но совместными усилиями меня, Слави и Лены, мы смогли её перебороть."
    "Смеявшись, мы выбрались из воды, и вернулись к своим местам."

    stop ambience fadeout 1.0

    hide un
    hide mi
    hide dv
    hide sl
    show bg ext_beach_day
    with dissolve

    play ambience ambience_lake_shore_day fadein 1.0 volume 0.88

    "Я немного постоял, обсыхая, и подумал."
    th "Фух, даже по меркам лагеря сегодня необычайно жарко."

    show sl swim smile2 close at fleft
    with dspr

    "Я полностью высох, и лёг обратно на своё полотенце."
    "Девочки обсуждали что-то связанное с одеждой, а я просто слушал, наслаждаясь компанией, и тем, что та, в которую я был влюблён, сидела рядом."
    "А её рука лежала на моей."

    hide sl
    show blink
    with dissolve

    "Я закрыл глаза, и наслаждался шумом воды, и разговорами девочек."

    stop music fadeout 4.0

    "..."

    play sound sfx_head_heartbeat fadein 2.0 volume 0.89 loop

    "В какой-то момент появилось странное чувство."
    "Как будто выпил, и лёг, ощущая те самые неприятные вертолётики."
    "К горлу подкатил ком."
    "Славя, до этого державшая свою руку на моей, вдруг убрала её, и положила мне на лоб."

    hide blink
    show sl swim sad at left
    with dissolve

    "Я открыл глаза."

    hide unblink

    "Передо мной была испуганная Славя."
    sl "Сём… Ты весь красный, и горячий."

    show sl swim scared with dspr

    sl "Как ты себя чувствуешь?"
    "Я сглотнул, и громко набрав в лёгкие побольше воздуха, медленно выдохнул ртом."
    me "Перегрелся наверное… Пойду ополоснуть в воде."

    show bg ext_beach_day at blurring
    hide sl
    with dissolve

    "Стоило мне подняться, и сделать первый шаг, как тут же перед глазами всё поплыло."

    stop sound fadeout 1.0
    play sound2 "<from 0.0 to 2.75>" + sfx_head_explode fadein 0.35 volume 0.93

    "Я уже почти ничего не понимал, и в какой-то момент просто почувствовал, что падаю."

    window hide

    show black with dissolve

    stop ambience fadeout 1.0
    play sound3 sfx_fall_wood_floor fadein 0.25 volume 0.85

    "..."

    $ renpy.pause(2.0, hard=True)

    stop sound2 fadeout 1.0
    stop sound3 fadeout 1.0

    $ renpy.pause(2.0, hard=True)

    play ambience ambience_medstation_inside_day fadein 3.0 volume 0.8
    play sound sfx_door_squeak_light volume 0.87

    window show

    "Открылась входная дверь."
    "Даже не знаю, почему я обратил на это внимания, ведь находился в полубессознательном состоянии."
    "Не сказать, что я чувствовал себя плохо, но всё тело немного ныло."
    mt "Виола, ну как он?"
    cs "Да всё хорошо будет, обычный тепловой удар."
    cs "Через полчаса уже полностью оклемается. Но до обеда пусть всё-таки лежит."

    show unblink
    show bg int_infirmary_day
    hide black
    with dissolve1

    "Я открыл глаза."

    show bg int_infirmary_day at deblurring
    hide unblink
    with None

    "Я лежал в палате, судя по всему в медпункте. Только в комнате, куда я не заходил."
    "Снаружи продолжали доноситься голоса."
    slp "А можно я с ним останусь?"
    th "Славя?"
    mt "Я то не против. Всё равно до обеда дел нет."
    cs "Хорошо. Как раз пусть тут кто-нибудь будет, на случай если меня станут искать."
    cs "Мы вернёмся на пляж, усилим, так сказать, контроль за состоянием пионеров. {w}День сегодня и правда жаркий."
    sl "Хорошо."

    play sound sfx_door_squeak_light volume 0.87

    "Судя по звукам, Виола и Ольга Дмитриевна вышли."
    "Я посмотрел на дверь в свою палату. И только сейчас понял, что был одет."
    th "И почему меня не раздели? Ну ладно…"

    show sl pioneer surprise far at fleft
    with good_dspr

    "Дверь в палату приоткрылась, и сюда заглянула Славя."

    show sl pioneer smile at cleft
    with good_dspr

    "Сразу поняв, что я не сплю, она забежала, и обняла меня."

    play music music_list["dance_of_fireflies"] fadein 2.0 volume 0.75

    show sl pioneer happy_cry with dspr

    sl "Сёма! Я так испугалась!"
    "Она прижалась лицом к моей груди."
    "Я обнял её одной рукой."
    me "Славя... Что вообще произошло?"
    sl "Ну, я почувствовала у тебя жар. Ты хотел умыться в воде, но стоило тебе встать, как ты тут же потерял сознание, и упал."
    sl "Я так испугалась. Мы с девочками сразу позвали вожатую, а пара ребят помогли донести тебя сюда."
    me "Вот оно что… Странно, раньше я никогда не падал в обморок."

    show sl pioneer shy with good_dspr

    "Девушка слегка улыбнулась."
    sl "Ну, может не привык к такой жаре?"
    me "Наверное…"

    show sl pioneer smile with good_dspr

    "Славя встала, и только сейчас я заметил, что в руке она держала какую-то одежду."
    me "Что это у тебя?"

    show sl pioneer smile2 with dspr

    sl "Да просто кофточка лёгкая."
    sl "Может слышал, я с девочками на пляже про одежду разговаривали."
    sl "Вот и про неё в том числе. Я же её с собой взяла, думала одену на обратном пути."
    sl "А по итогу просто всё похватала, и побежала сюда."
    "Я был очарован ей."
    "Тот факт, что она за меня испугалась, и на всех порах помчалась в медпункт, просто чтобы побыть со мной…"

    stop music fadeout 3.0

    me "Ну, я до обеда полежу наверное. Вроде чувствую себя неплохо, но надо отдохнуть."

    play music music_list["forest_maiden"] fadein 2.0 volume 0.85

    show sl pioneer smile with dspr

    sl "Я с тобой останусь!"
    me "Да что же ты со мной сидеть будешь в такой прекрасный день?"

    show sl pioneer sad with dspr

    sl "Без тебя он не прекрасный… {w}И я всё ещё переживаю за твоё состояние."

    show sl pioneer smile with dspr

    sl "Может… Просто полежим вместе?"
    "Я расплылся в улыбке."
    me "Это было бы замечательно."

    show sl pioneer shy with dspr

    sl "Хорошо, тогда я сейчас…"

    show sl skirt shy with long_dspr

    "Она сняла рубашку… {w}Прямо при мне."
    th "Она меня что, уже не стесняется?"
    th "Ну хотя, я же видел её в купальнике."
    th "Ну хотя, это немного другое."
    "Так или иначе, от этого вида я сразу приободрился."

    show sl skirt smile with dspr

    sl "Просто не хочу рубашку помять."
    "Она закрыла шторы, чтобы с улицы не бил солнечный свет, затем одела свою кофточку, и легла рядом со мной."

    hide sl
    show cg d5_sl_sleep_2
    with dissolve

    "Некоторое время мы лежали, и разговаривали."
    "Но вскоре, меня начало клонить в сон…"

    window hide

    stop music fadeout 2.0

    pause(1.0)

    show blink

    $ renpy.pause(2.5, hard=True)

    window show

    "..."
    sl "Семён! Семён, просыпайся!"
    "Славя трясла меня за плечо."

    hide blink
    hide cg
    show bg int_infirmary_day
    show sl pioneer smile at cleft
    show unblink
    with dissolve

    "Я открыл глаза."

    hide unblink

    play music music_list["get_to_know_me_better"] fadein 2.0 volume 0.81

    "По ощущениям, я проспал не больше полутора часов."
    sl "Скоро обед, нужно выходить."

    play sound sfx_stomach_growl volume 0.93

    "В животе заурчало."

    show sl pioneer laugh with dspr

    "Славя улыбнулась, и сказала."
    sl "Голодный, значит здоровый!"
    "Я посмеялся и ответил."
    me "Не могу не согласиться!"

    show sl pioneer smile2 with dspr

    "И правда, по ощущениям, если исключить голод, чувствовал я себя хорошо."
    "От солнечного удара не осталось и следа."
    "Я сел на кровати, обулся, и мы вышли в главный зал медпункта."

    hide sl
    show bg int_aidpost_day
    show sl pioneer smile at right
    with dissolve

    me "Никто не приходил?"

    show sl pioneer shy with dspr

    sl "Честно говоря, я сама уснула где-то на полчаса, но потом просто лежала с тобой. Никто не приходил."

    play sound sfx_medpunkt_door_open

    show sl pioneer smile
    show cs normal at left
    with good_dspr

    "Вошла медсестра."
    cs "Пионер… Как себя чувствуешь?"
    me "Отлично, спасибо! Как будто и не было ничего."
    cs "Не стоит… {w}Так, мне нужно ещё раз тебя проверить."

    show sl pioneer surprise with dspr

    cs "Славя, выйди пожалуйста, подожди на улице."

    show sl pioneer surprise at walk_away_right
    pause(1.0)
    hide sl with dspr

    stop music fadeout 3.0

    "Славя сильно удивилась, но всё же вышла."

    play music music_list["eternal_longing"] fadein 1.0 volume 0.9

    hide cs
    show cs shy at center
    with good_dspr

    "Медсестра подошла ближе."
    cs "Итак… {w}Пионер."
    cs "Ты настроен серьёзно?"
    me "Вы про что?"

    show cs smile with dspr

    cs "Я про Славю."
    th "И откуда она то знает?"
    "Ответ пришел в ту же секунду сам собой. {w}Вожатая."
    me "Ну-у, да. Но я не понимаю, к чему вы клоните?"

    show cs normal with dspr

    cs "Не прикидывайся."
    cs "Вообще, я бы не рекомендовала, но… Лучше с ним, чем без него."
    me "С кем с ним? Я не понимаю."
    "Я лукавил."

    show cs shy with dspr

    "Медсестра достала из кармана халата… Упаковку презерватива."
    "«Изделие из резины №3» - гласило название на упаковке."
    "Я немного покраснел."

    show cs normal with dspr

    cs "Ну, что смотришь? Как будто впервые в жизни презерватив видишь. {w}Бери."
    "Я машинально взял у неё из руки упаковку, и убрал в карман."

    show cs smile with dspr

    cs "Если нужна будет помощь... {w}Обращайся… {w}Пионер."
    "Я сглотнул."
    th "Да что с этой женщиной не так?"
    me "Спасибо. Я, пожалуй, пойду."
    cs "Иди уж."

    stop music fadeout 2.0
    stop ambience fadeout 1.0

    "Я быстро развернулся, и вышел на улицу."

    hide cs
    show bg ext_aidpost_day
    show sl pioneer normal at right
    with dissolve

    play ambience ambience_camp_center_day fadein 1.0

    "У лестницы меня ждала Славя."

    play music music_list["my_daily_life"] fadein 2.0 volume 0.8

    sl "Ну, что медсестра сказала?"
    me "Да так… Давление померяла. Здоров!"
    "Славя улыбнулась, и ответила."

    show sl pioneer smile with dspr

    sl "Вот и отлично, пойдём кушать?"
    me "Пойдем."
    "Мы направились в сторону столовой."

    show bg ext_dining_hall_away_day
    show mt pioneer normal at center
    with dissolve1

    "На подходе нас встретила вожатая, и поинтересовалась, как я себя чувствую."
    me "Всё отлично, спасибо!"

    show mt pioneer smile with dspr

    mt "Хорошо. Ну, идите кушать."
    dv "Славя, Семён!"
    "Со стороны площади нас окрикнула Алиса, и через полминуты подошла к нам."

    pause(0.5)

    hide mt
    show bg ext_dining_hall_near_day
    show dv pioneer normal at left
    with dissolve

    dv "Ну что, полегчало?"
    me "Да, обошлось, слава Богу."

    show dv pioneer smile with dspr

    dv "Ну и отлично, пойдёмте трапезничать."
    "..."

    stop ambience fadeout 1.0

    show bg int_dining_hall_people_day
    show mi pioneer normal at center
    with dissolve

    play ambience ambience_dining_hall_full fadein 1.0

    "Втроём мы сели за столик к Мику."

    show mi pioneer smile with dspr

    mi "Ой, Сёма, как я рада что с тобой всё в порядке! А то как бы мы играли."
    "Я картинно надул щёки, и ответил."
    me "Ах вот так да, я тебе только как инструмент нужен?"
    "Я скрестил руки на груди, и отвернулся в потолок."

    show mi pioneer cry_smile with dspr

    mi "Ой, ну что ты, что ты! Ещё как уборщик, и грузчик!"

    show dv pioneer laugh
    show sl pioneer smile2
    with dspr

    "Девочки засмеялись."
    me "Ой, да ну вас!"

    show dv pioneer smile
    show mi pioneer smile
    show sl pioneer smile
    with dspr

    "Мы продолжили есть, изредка перешучиваясь, но вскоре, разговор перешел в русло завтрашнего «мини-концерта», как мы его уже все окрестили."
    "..."

    stop ambience fadeout 1.0

    hide sl
    hide mi
    hide dv
    show bg ext_dining_hall_near_day
    show dv pioneer normal at left
    show mi pioneer normal at right
    show sl pioneer smile2 close at center
    with dissolve1

    play ambience ambience_camp_center_day fadein 1.0

    "Выйдя из столовой, я обнялся со Славей на прощание, и мы двинули в сторону музыкального клуба."

    hide sl
    show bg ext_dining_hall_away_day
    with dissolve
    
    "Недалеко отойдя от столовой, я внезапно понял, что кого-то не хватает, и спросил."
    me "А где Лена?"

    show mi pioneer sad with dspr

    mi "Ой, да она на обед просто не пошла, говорит у неё живот заболел."
    mi "Может тоже последствия долгого пребывания на Солнце, но сказала что подойдет к клубу, к тому времени, как мы с обеда вернёмся."

    show bg ext_square_day with dissolve

    "Мы вышли на площадь."
    me "И что же, она до вечера голодная будет?"

    show mi pioneer happy with dspr

    mi "Ну-у, у меня где-то должны были оставаться печеньки. Чай есть. Я думаю найдём, чем ей перекусить…"

    show mi pioneer grin with dspr

    "Внезапно, Мику ехидно улыбнулась, и продолжила."
    mi "Ну на краник, Алиса дверь в столовую взломает, и мы своруем для Лены что-нибудь."
    me "Что?"

    show dv pioneer smile with dspr

    dv "Аха-ха, Мику!"
    dv "Во-первых, «на крайняк»."
    dv "А во-вторых, замок у меня на прошлой неделе вскрыть так и не получилось."
    "Я опешил, но засмеялся."
    me "Ха-ха, Алиса. Ты пыталась вскрыть столовую?"
    "Алиса, кажется, гордая своей смелой, пусть и не удачной выходкой, ответила."
    dv "Ну да. Что-то булочек мне тогда захотелось. Не наелась я."
    me "Ну ты даёшь!"
    th "Эх, безбашенная молодость."
    me "Прям настоящий панк-рок."

    show dv pioneer grin with dspr

    dv "А то!"
    "..."

    hide mi
    hide dv
    show bg ext_musclub_day
    show dv pioneer smile at left
    show mi pioneer normal at right
    show un pioneer normal far at center
    with dissolve

    "Вскоре, мы пришли к зданию музыкального клуба."
    "Рядом с ним нас уже ждала Лена."

    hide un
    show bg ext_musclub_verandah_day
    show un pioneer smile at center
    with dissolve

    "Мы подошли ближе."
    un "А вот и вы наконец-то!"
    mi "Лена, как ты себя чувствуешь?"
    un "Хорошо, спасибо. Живот прошёл."
    mi "Ну тогда заходим!"

    play sound sfx_keys_rattle volume 0.7

    "Мику достала ключи из кармана."
    me "Вы пока заходите, а я пойду покурю."

    show mi pioneer dontlike with dspr

    mi "О-хоо! Бака!"

    show dv pioneer grin with dspr

    dv "Я с ним!"

    hide mi
    hide un
    with long_dspr

    "Мику с Леной направились ко входу, а мы с Алисой зашли за здание с торца."

    stop music fadeout 2.0

    call smoking_process(with_pause=1.0)

    "Я дал ей сигарету, достал себе, и мы закурили."

    play music music_list["reflection_on_water"] fadein 2.0 volume 0.84

    show dv pioneer normal with dspr

    "Внезапно, Алиса стала серьёзной в лице, и обратилась ко мне."
    dv "Семён…"
    "Я посмотрел на неё."
    me "Да?"
    dv "Насколько серьёзно у тебя всё со Славей?"
    th "Неожиданный вопрос."
    me "Ну… Не знаю ещё. Мы не торопимся в отношениях, и между нами пока не было признания… Но заметно, да, что мы друг другу нравимся?"

    show dv pioneer smile with dspr

    "Алиса улыбнулась."
    dv "Ты не представляешь, насколько."
    dv "Стоит тебе её увидеть, так ты сразу в такой дурацкой улыбке расплываешься…"
    dv "Если что, я не смеюсь, просто констатирую факт."
    me "Хм… А ты не знаешь, что Славя об этом думает?"

    show dv pioneer normal with dspr

    dv "Мало. Она живёт с Женей, а с ней я не общаюсь."
    dv "Но в любом случае, явно видно что она в тебя влюблена, и ты, я думаю, сам это знаешь."
    "Я кивнул."

    play sound sfx_smoking_cigaret

    "Алиса глубоко затянулась, и продолжила."
    dv "Может ты не знаешь, но мы с Леной подруги с детства. Мы выросли в одном дворе."
    th "Кажется, я что-то об этом слышал. {w}Или нет?"
    dv "Сейчас мы не так много общаемся, но лучше чем было ещё недавно… В общем, это другая история."
    me "Так… И к чему ты клонишь?"
    dv "К тому, что однажды Лену очень сильно обидел один парень, в которого она была влюблена."
    dv "Пришлось бить ему в нос. Намёк понял?"
    me "Понял. Но не понял я того, с чего ты вдруг решила, что я собираюсь обижать Славю?"
    dv "Я не решила, я просто предупреждаю."

    show dv pioneer smile with dspr

    "Она немного улыбнулась."
    dv "Мы со Славей конечно далеко не близкие подруги, и у нас были разногласия. Но я все равно за неё впрягусь, если придётся."
    me "Воинственная ты девушка, Алис!"
    
    show dv pioneer grin with dspr

    "Она потушила окурок, и сказала."
    dv "Уж какая есть! {w}Ладно, заходи пока в клуб, а я переоденусь и за тобой."
    me "Хорошо."

    "Я обогнул здание и вошел в музыкальный клуб..."

    stop ambience fadeout 1.0

    hide dv
    show bg int_musclub_mattresses_day
    show un pioneer normal at fleft
    show mi pioneer smile at center
    with dissolve

    play ambience ambience_music_club_day fadein 1.0

    mi "Вот и в-в... А. {w}А где Алиса?"
    "Я немного посмеялся."
    me "Сейчас зайдёт. Ты же знаешь её стиль."

    show dv pioneer2 smile at right
    with dspr

    dv "Не потеряли?"

    show mi pioneer happy with dspr

    stop music fadeout 2.0

    mi "О! Теперь точно приступаем!"

    hide un
    hide dv
    hide mi
    with dspr

    call to_nvl_mode

    play music music_list["so_good_to_be_careless"] fadein 2.0 volume 0.8

    "Мы начали заниматься."
    "Мику сразу взяла меня, и мы порепетировали композицию, которую я готовил для Слави. Так было проще, чем оставлять её на потом, ведь девочки в это время занялись своими делами."
    "Алиса сразу взяла свою гитару, и настроив звук, подключила её сначала в небольшой усилитель, а потом в наушники, чтобы не мешать остальным."
    "Лена же стояла перед пюпитром в другом конце помещения, и разучивала свою партию."
    "..."
    nvl clear
    "Примерно через час мы сделали перерыв."
    "Мой прогресс в разучивании композиции был налицо, я мог сыграть уже большую часть, хотя иногда и ошибался."
    "Лена, судя по всему, тоже делала успехи."
    "Поэтому, дав ей времени перекусить, мы прервались."
    "Пока Мику с Леной делали на всех чай, мы с Алисой вышли на улицу покурить."
    "..."
    nvl clear
    "Когда Лена утолила голод, чай был выпит а общие успехи подверглись обсуждению, мы продолжили."
    "В этот раз Мику оставила меня одного оттачивать свою партию для совместного «Самого Теплого Лета», и стала писать барабанную партию для «Костров» Алисы."
    "Лена продолжала заниматься флейтой, а Алиса, так как уже достаточно повторила композицию, которую, судя по всему, и так хорошо знала, просто наблюдала за нами."
    "..."

    call to_adv_mode

    show dv pioneer2 smile at fright
    show un pioneer normal at left
    show mi pioneer normal at center
    with good_dspr

    mi "Итак, Семён. Пришло время нам начинать репетировать всё вместе."
    "До ужина оставалась пара часов."

    show un pioneer smile with dspr

    un "Ну, я, в общем-то готова."
    me "Я тоже."

    show mi pioneer smile with dspr

    mi "Отлично, тогда за дело!"

    hide dv
    show dv pioneer2 smile at right
    with dspr

    "Алиса тоже подобралась поближе к нам, и начала слушать."
    "..."

    hide dv
    hide un
    hide mi
    with dspr

    call to_nvl_mode

    "Мы начали репетировать совместную игру."
    "Играть под вокал Мику оказалось несложно, у нас получилось почти идеально с первого раза."
    "Но вот при следующем прогоне, когда подключилась и Лена, стало сложнее."
    "Второй инструмент отвлекал, и я постоянно сбивался."

    call to_adv_mode

    show un pioneer smile at left
    show dv pioneer2 normal at right
    show mi pioneer normal at center
    with dspr

    me "Мхм, чёрт!"

    show mi pioneer smile with dspr

    mi "Семён, я поняла в чём ошибка!"
    "Я посмотрел на Мику."
    mi "Смотри, дело в том, что мы играем без ударных. Так бы конечно было легче."
    mi "Но также, это означает то, что линию и такт задаешь ты."
    mi "Ты ведущий инструмент. Так что тебе нужно просто играть, не обращая внимания на нас. А мы с Леной уже подстроимся."
    mi "Не нужно слушать флейту."
    mi "Ну то есть как, ты конечно должен её слышать, но не меняй свой ритм под неё, понял?"
    "Звучит логично."
    me "Вроде понял."

    show mi pioneer normal with dspr

    "..."
    "И правда, пошло легче."
    "Я просто играл, а Лена ложила сверху флейту. Мику дополняла вокалом."
    "Когда у нас впервые получилось более-менее ровно сыграть, я заулыбался от радости."

    show dv pioneer2 laugh with dspr

    dv "Звучит недурно, мне нравится!"
    "Решив, что успех надо закрепить, так как по словам Мику, мы «сыгрались», мы исполнили композицию ещё раз полностью. Последний раз на сегодня."
    "Получилось также хорошо."

    hide mi
    hide dv
    show dv pioneer2 smile at fright
    show mi pioneer happy at cright
    with dspr

    mi "Фух! Мы сегодня большие молодцы!"
    "Мику плюхнулась на матрасы."

    stop music fadeout 2.0

    show mi pioneer smile
    show dv pioneer2 smile
    with dspr

    mi "Особенно Семён. Он то вообще не музыкант, а вон как быстро схватывает!"

    play music music_list["she_is_kind"] fadein 2.0 volume 0.8

    "Я смутился."
    dv "А сколько ты на гитаре играешь?"
    me "Ну-у, если считать лагерь тоже… Две с половиной недели."

    show dv pioneer2 shocked with dspr

    "Алиса опешила."
    dv "Пол месяца, да, как я понимаю, с большими перерывами!? Да ты колдун!"
    dv "Не все «кузнечика» за это время могут сыграть, а ты уже вместе с другим инструментом играешь, и вокалом. Ну, силё-ён!"

    show dv pioneer2 laugh
    show un pioneer normal
    with dspr

    un "А мне кажется, это лагерь так действует."

    show mi pioneer shocked
    show dv pioneer2 normal
    with dspr

    "Все уставились на Лену."

    dv "Что?"
    me "Что?"

    show un pioneer shy with dspr

    un "Ну-у, знаете. Тут хорошо, атмосфера такая… Быстро и с интересом учишься новому."
    me "А-а-а, вот ты про что. Ну да, вполне может быть."

    show mi pioneer normal with dspr

    "Мику встала с дивана, и сказала."
    mi "А мне действительно кажется, что Лена права."
    mi "Это место меняет людей."
    th "Да что такое, они тут все решили загадками начать говорить?"
    th "Мне сейчас не по себе станет."

    show mi pioneer happy with dspr

    mi "Ну вот сам посуди. Не встретил бы ты тут Славю, не захотел бы ей сыграть. Мотивации учиться было бы меньше."
    "Я выдохнул, и у меня вырвался нервный смешок."
    me "А-а, вот ты о чём!"
    "Я тоже поднялся."
    me "А ведь и правда."
    me "Ну, тем и лучше, что я поп… {w}А-а-э, приехал в этот лагерь… А то мог бы и в другой. Вот."

    show mi pioneer cry_smile with dspr

    mi "И правда, так хорошо, что мы все тут познакомились и подружились!"

    play sound sfx_dinner_horn_processed volume 0.35

    "Мы услышали горн."

    show mi pioneer smile
    show dv pioneer2 smile
    with dspr

    "С дивана встали Лена и Алиса, и последняя заключила."
    dv "Во всяком случае… Мы все заслужили сегодня поесть!"
    "Радостно согласившись, мы всей компанией направились в столовую."

    show black with clocks_in

    stop ambience fadeout 1.0

    hide un
    hide mi
    hide dv
    show bg int_dining_hall_people_sunset
    show un pioneer normal at left
    hide black
    with clocks_out

    play ambience ambience_dining_hall_full fadein 1.0

    "Когда мы все зашли в столовую, Алису позвала за столик Ульяна, а Мику, на удивление, позвал Шурик."
    "После раздачи мы с Леной остались вдвоём, и искали, куда бы сесть, но я заметил Славю, которая махала нам."
    me "Пойдём!"

    hide un
    show un pioneer smile at fleft
    show sl pioneer smile at right
    with good_dspr

    "Подойдя к столику, я сел рядом со Славей, а Лена с противоположной стороны."
    "Мы пожелали друг другу приятного аппетита, и начали есть."
    me "Кстати, а ты чем сегодня после обеда занялась?"

    show sl pioneer smile2 with dspr

    sl "Ой, да почти ничем. Ольга Дмитриевна попросила клумбой на сцене заняться, уж не знаю зачем."
    sl "Да там клумба то, раза в два меньше чем на площади."

    show sl pioneer shy with dspr

    sl "Но без тебя было не так весело…"

    show sl pioneer smile2 with dspr

    sl "Через час уже закончила, и в домике сидела, книжку читала."
    sl "А у вас как успехи?"

    show sl pioneer smile with dspr

    "Я начал делиться нашим прогрессом, Лена тоже вскоре подключилась к обсуждению, и так мы провели ужин за приятной беседой."
    "К нам за столик больше никто не сел."
    "..."

    window hide

    call set_time("sunset")

    stop ambience fadeout 1.0
    stop music fadeout 2.0

    hide un
    hide sl
    show bg ext_dining_hall_near_sunset
    show sl pioneer smile at right
    with dissolve

    play ambience ambience_camp_center_evening fadein 1.0

    window show

    "Мы вышли из столовой."

    play music music_list["silhouette_in_sunset"] fadein 2.0 volume 0.85

    "Попрощались с Леной, и встали, перед входом, облокотившись на перилла перед столовой, наблюдая, как на лагерь опускается вечер."
    "Дневная жара уже спадала, и сейчас на улице стояло приятное вечернее тепло."
    me "Не хочешь прогуляться сегодня вечером? Погода на улице чудесная."

    show sl pioneer smile2 with dspr

    "Девушка улыбнулась."
    sl "Да я с тобой и в дождь, и в град, и в снег пошла бы куда угодно."
    "Я улыбнулся в ответ."
    "Внезапно я осознал, что между нами уже давно витает очень сильное напряжение, готовое разрядиться в любой момент."
    "Мы оба уже не могли молчать, чувства требовали выговорится."

    hide sl
    show sl pioneer smile2 at cright
    with dspr

    "Я повернулся к девушке, облокотившись на перилла одним локтем, и ответил."
    me "Тогда, после бани? Когда это примерно будет?"
    sl "Ну, вообще её сейчас, наверное, уже топят. Через полчаса где-то начнут заходить девочки, мальчики потом."
    sl "Но я последняя пойду. А ты постарайся попасть первым, так быстрее всего освободимся."
    me "Звучит разумно."
    me "Тогда пойдём к домикам?"

    show sl pioneer shy with dspr

    "Я протянул ей руку."
    sl "Пойдём."
    "Она взяла мою руку, и вместе мы направились к домикам."

    show black with clocks_in

    stop music fadeout 2.0

    hide sl
    show bg ext_house_of_mt_sunset
    hide black
    with clocks_out

    play music music_list["tried_to_bring_it_back"] fadein 2.0 volume 0.85

    "Разойдясь со Славей на повороте, я дошёл до нашего с вожатой домика, и уже покурил неподалёку."

    play sound sfx_knock_door7_polite volume 0.75

    "Я постучался."
    mt "Открыто!"

    stop ambience fadeout 1.0

    show bg int_house_of_mt_sunset
    show mt pioneer normal at right
    with dissolve

    play ambience ambience_int_cabin_evening fadein 1.0

    "Войдя в домик, я обнаружил вожатую, через плечо которой уже было перекинуто полотенце, а в руке она держала банные принадлежности."
    me "Готовитесь к баньке?"
    "Я улыбнулся, и налив себе в стакан воды из чайника, разом осушил его."

    show mt pioneer smile with dspr

    mt "Да, скоро уже запускать начнём."
    "Я сел на стул, уперевшись одним локтем на стол, и положив голову на кулак, посмотрел на вожатую."

    show mt pioneer grin with dspr

    mt "М-м-м, узнаю этот взгляд."
    mt "К отбою тебя опять не ждать?"
    me "Я постараюсь сильно не задерживаться."

    show mt pioneer smile with dspr

    mt "Ну ты уж постарайся. Ладно."
    mt "Сейчас в бане девочки купаются, потом мальчики. Ну, минут через 40 уже можешь быть там."
    me "Понял, хорошо."

    show mt pioneer smile at walk_away_right
    pause(1.0)
    hide mt with dspr

    "Вожатая вышла, а я проводил её взглядом."
    "Я откинулся на спинке стула, и подумал."
    th "П-ф-ф, и чем бы занять этот почти час?"
    "Взгляд упал на книги, которые лежали на настенной полке со стороны вожатой."
    th "Та-ак, посмотрим."
    "Я начал перебирать книги в поисках какой-нибудь, которую хотя бы знаю."
    "Наконец, в самом низу мне попалась такая."
    "«Л.Н. Толстой»"
    "«Война и Мир. Том I»"
    th "Ну как знаю. Имею представление."
    th "Читал конечно в старшей школе, но не полностью."
    th "Ай, ладно. Время убить пойдёт."
    "Я развалился с книжкой на кровати, и на всякий случай завел на телефоне таймер на полчаса."
    "Открыв книгу на случайной странице, я начал читать."

    stop music fadeout 2.0

    call to_nvl_mode

    "Французы успели сделать три картечные выстрела, прежде чем гусары вернулись к коноводам. Два залпа были сделаны неверно, и картечь всю перенесло, но зато последний выстрел попал в середину кучки гусар и повалил троих."
    "Ростов, озабоченный своими отношениями к Богданычу, остановился на мосту, не зная, что ему делать. Рубить (как он всегда воображал себе сражение) было некого, помогать в зажжении моста он тоже не мог, потому что не взял с собою, как другие солдаты, жгута соломы. Он стоял и оглядывался, как вдруг затрещало по мосту, будто рассыпанные орехи, и один из гусар, ближе всех бывший от него, со стоном упал на перилы. Ростов подбежал к нему вместе с другими. Опять закричал кто-то: «Носилки!» Гусара подхватили четыре человека и стали поднимать."
    "— Оооо!.. Бросьте, ради Христа, — закричал раненый; но его все-таки подняли и положили."
    "Николай Ростов отвернулся и, как будто отыскивая чего-то, стал смотреть на даль, на воду Дуная, на небо, на солнце! Как хорошо показалось небо, как голубо, спокойно и глубоко! Как ярко и торжественно опускающееся солнце! Как ласково-глянцевито блестела вода в далеком Дунае! И еще лучше были далекие, голубеющие за Дунаем горы, монастырь, таинственные ущелья, залитые до макуш туманом сосновые леса... там тихо, счастливо... «Ничего, ничего бы я не желал, ничего бы не желал, ежели бы я только был там, — думал Ростов. — Во мне одном и в этом солнце так много счастия, а тут... стоны, страдания, страх и эта неясность, эта поспешность... Вот опять кричат что-то, и опять все побежали куда-то назад, и я бегу с ними, и вот она, вот она, смерть, надо мной, вокруг меня... Мгновенье — и я никогда уже не увижу этого солнца, этой воды, этого ущелья...»"
    "В эту минуту солнце стало скрываться за тучами; впереди Ростова показались другие носилки. И страх смерти и носилок, и любовь к солнцу и жизни — все слилось в одно болезненно-тревожное впечатление."
    "«Господи Боже! Тот, кто там, в этом небе, спаси, прости и защити меня!» — прошептал про себя Ростов."
    "Гусары подбежали к коноводам, голоса стали громче и спокойнее, носилки скрылись из глаз."
    "— Что, бг'ат, понюхал пог'оху?.. — прокричал ему над ухом голос Васьки Денисова."

    call to_adv_mode

    th "Ну, это я помню. Ладно, продолжим."
    "Я продолжил читать, погружаясь в сюжет…"

    play sound sfx_clocks fadein 0.25

    show black with clocks_in
    pause(1.0)
    hide black with clocks_out

    play music music_list["everyday_theme"] fadein 2.5 volume 0.77
    stop sound fadeout 0.25

    "Из чтения меня вывел звук сработавшего таймера."
    th "А классика оказалась не такой скучной, как я помнил по школе!"
    "Сделав себе мысленную пометочку обязательно прочитать полностью это произведение, я убрал книгу обратно на полку."
    "После чего собрал банные принадлежности, и вышел на улицу."

    stop ambience fadeout 1.0

    show bg ext_house_of_mt_sunset with dissolve

    play ambience ambience_camp_center_evening fadein 1.0

    "Погода на улице стояла всё такая же замечательная."
    "Видимо, воздух за сегодня очень сильно нагрелся, и отдавал дневное тепло очень медленно."

    call smoking_process(with_pause=1.0)

    "Я быстро покурил за домиком, и направился в сторону бани."

    pause(1.0)

    show bg ext_houses_sunset with dissolve

    "На встречу мне то и дело попадались девочки разных возрастов."
    th "Интересно, а Славя уже была?"
    "..."
    "Я так и не пересекся с ней по пути."

    window hide

    call set_time("night")

    show bg ext_bathhouse_night
    show mt pioneer smile at right
    with dissolve

    window show

    "Когда я дошёл до бани, немного стемнело, а перед входом стояла Ольга Дмитриевна."
    mt "О, Семён, уже пришёл?"
    me "Да. Все девочки вышли?"
    mt "Вышли, я поэтому и стою, жду первого парня. Ну, значит это ты."
    mt "Передай первому, кого увидишь, что можно заходить."
    me "Хорошо."

    show mt pioneer smile at walk_away_right
    pause(1.0)
    hide mt with dspr

    "Ольга Дмитриевна ушла, а я посмотрел на здание."
    "Больше оно было похоже на избу, чем на баню."
    "Да и маленькая она какая-то. Учитывая предбанник, который там наверняка есть, мыться в ней может только человека три, не больше."
    th "И как тогда все девушки успели помыться за пол часа?"
    "Ну да неважно. Я поднялся по ступеням, и зашел внутрь."

    stop ambience fadeout 1.0

    show bg int_bath_ent with dissolve

    play ambience ambience_int_cabin_evening fadein 1.0

    "В предбаннике было довольно мало места."
    "Видимо, большую часть строения, всё-таки, решили выделить под саму баню."
    "Обо всём этом я думал, пока раздевался."
    th "Вот не люблю я всё-таки общественные банные места. Некомфортно себя чувствуешь в общественном месте, полностью раздеваясь."
    "Ну ладно, выбора всё равно нет."
    "Я полностью разделся, обмотал полотенце вокруг таза, схватил банные принадлежности, и широким шагом направился к двери в баню, которая была приоткрыта…"
    "Распахнув её, и успев сделать только один шаг внутрь, я застыл на пороге."

    stop music fadeout 1.0

    show cg d3_sl_bathhouse with dissolve

    play music music_list["sparkles"] fadein 1.0 volume 0.92

    "Передо мной стояла Славя. {w}Голая."

    play sound2 sfx_head_heartbeat fadein 1.0 volume 0.5 loop

    "Я обомлел, а вздох застрял где-то посреди горла…"
    "Она стояла спиной ко мне, и вытиралась полотенцем."
    "Я не мог пошевелиться, и сказать тоже ничего не мог."
    "Наконец, она обернулась, видимо, почувствовав свежий воздух с прохода."
    sl "Семён?"

    play sound3 sfx_close_door_clubs_nextroom
    stop music fadeout 0.5

    hide cg
    show bg int_bath_ent
    with long_dspr

    play music music_list["doomed_to_be_defeated"] fadein 0.5 volume 0.9

    "Я тут же закрыл дверь, и сделав шаг назад, упал на скамейку в предбаннике."
    th "А вожатая сказала, что там никого не осталось!"
    th "А если бы на моём месте оказался кто-то другой! Твою мать!"
    "Я посмотрел на противоположный конец предбанника."
    "Там, на вешалке в самом углу висела форма."
    th "Бля-ять…"
    "Всё, пиздец, приехали."
    th "И как я её не заметил??"
    th "Что она теперь обо мне подумает?"
    "Что я какой-то маньяк, или насильник, или ещё чего хуже?"

    stop sound2 fadeout 0.1
    play sound2 sfx_head_heartbeat fadein 0.1 volume 0.8 loop

    th "Сука, сука, сука!"
    "Я сидел на лавочке, и весь неимоверно трясся, обхватив руками голову."
    "Вот так просто, по тупой случайности подорвать доверие человека, в которого я влюблён!?"
    "Я начал бить себя кулаками по коленям."
    th "Дебил, придурок, идиот!"
    "Хотелось рвать на себе волосы. Славя должна была уже выйти, и эти секунды казались вечностью."

    stop music fadeout 1.0

    "Наконец, боковым зрением я увидел, что вышла Славя, обмотанная полотенцем."

    show sl towel normal at cright
    with good_dspr

    "Я тут же подскочил, и повернулся к ней."

    play music music_list["i_dont_blame_you"] fadein 1.5 volume 0.8

    me "Славя… Я…"
    me "Прости. Я правда, не знал, что внутри кто-то есть."
    sl "Сёма. Тебе не за что извиняться."
    me "Но, как же… {w}Я не хотел, чтобы вот так вот... получилось… {w}Прости меня."
    "Она подошла ближе, и придерживая полотенце, поцеловала меня, затем ответила, улыбнувшись."

    show sl towel smile with dspr

    sl "Я понимаю, что ты не специально. И никогда бы ничего подобного специально не сделал, я это знаю."
    "Я лишь опустил взгляд."
    "Я испытывал какое-то странное чувство: смесь стыда, и бесконечной любви к человеку, вперемешку с невероятным уважением."
    "Я снова посмотрел на Славю."
    me "Ты правда не обижаешься?"
    "У неё в глазах я прочитал абсолютное доверие."
    sl "Правда. Потому что я доверяю тебе, Сёма."

    show blink

    "Придерживая полотенце одной рукой, она прильнула ко мне, и обняла второй. {w}Я ответил на объятие, положив руки ей на спину и талию."

    stop sound2 fadeout 1.0

    "Всё моё напряжение как рукой сняло."
    "Я чувствовал прикосновения человека, который уже отдал мне своё сердце."

    hide blink
    show unblink

    sl "К тому же, было бы гораздо хуже, если бы на твоём месте оказался кто-то другой."

    hide unblink

    "Я улыбнулся."
    me "Это правда. Не знаю, даже, чтобы я потом с ним сделал!"
    "Ко мне начал возвращаться подъём духа."
    "Славя засмеялась, и ответила."

    stop music fadeout 2.0

    sl "Ха-ха, представляю!"

    play music music_list["she_is_kind"] fadein 2.0 volume 0.75

    sl "Ну ладно, иди уже купайся, а то там скоро очередь соберётся."
    me "Я мигом!"
    sl "Хорошо, тогда я подожду рядом с баней."
    "На том и порешили."
    
    show sl towel smile at walk_away_left
    pause(1.0)
    hide sl with dspr

    "Славя подошла к своей вешалке, и начала одеваться, а я зашёл-таки в банное помещение."

    show bg int_bathhouse with dissolve

    play sound sfx_water_sink_stream volume 0.1 loop

    "Внутри стоял настолько плотный пар, что сложно было даже что-то разглядеть в метре от себя."
    th "У-ух, вот это натопили."
    "Ну-с, ладно, приступим!"
    "..."
    "Я с большим удовольствием начал обтираться, поливать себя водой, и мыть все доступные части тела."
    "Всё-таки, сколько я не мылся? Почти неделю."
    th "Буэ, ужас просто."
    "И что, каждый раз, чтобы пионерам помыться, тут баню топят?"
    "Хотя я видел душевые… Может просто сломаны."
    "..."
    "Продолжая рассуждать обо всяком, я полностью помылся, и начал обтираться полотенцем. Все водные процедуры заняли у меня не больше пяти минут."
    th "Вот умора будет, если сейчас кто-нибудь зайдет…"
    "Как говорится: «где-то я уже это видел»."

    stop sound fadeout 1.0

    show bg int_bath_ent with dissolve

    "К счастью, ничего подобного не произошло, и я, спокойно вытеревшись, оделся, и взяв всё своё, вышел на улицу."

    stop music fadeout 2.0
    stop ambience fadeout 1.0

    show bg ext_bathhouse_night
    show el pioneer normal at cright
    show sh pioneer normal at fright
    show sl pioneer normal far at fleft
    with dissolve

    play ambience ambience_camp_center_night fadein 1.0

    "Там уже стояли Шурик с Электроником, а неподалеку ждала меня Славя."

    play music music_list["silhouette_in_sunset"] fadein 2.0 volume 0.75

    sh "Ну наконец-то, мы уж думали ты там утоп!"

    show el pioneer grin with dspr

    el "Да и пассия твоя, тебя уже кажется, заждалась."
    "Он подмигнул."
    me "Извините, парни. Давно в бане не был, пока всё вспомнил…"
    me "Приятно попариться!"

    hide el
    hide sh
    hide sl
    show sl pioneer smile at cright
    with good_dspr

    "Я спустился по ступенькам, и приблизился к Славе."
    th "Вдвоём, они, что ли, мыться будут?"
    "Промелькнуло в голове."

    show sl pioneer laugh with dspr

    sl "А ты и правда быстро! С лёгким паром!"
    me "Спасибо! Ну я же обещал!"

    hide sl
    show sl pioneer smile2 at right
    with dspr

    "Обернувшись, и убедившись что два светила науки зашли, я взял Славю за руку, и мы направились в сторону домиков, чтобы положить свои вещи."

    show black with clocks_in

    stop music fadeout 2.0

    show bg ext_houses_night
    show mi pioneer smile at left
    hide black
    with clocks_out

    play music music_list["eat_some_trouble"] fadein 2.0 volume 0.5

    "По пути Мы встретили Мику."
    "Она улыбнулась нам, и сказала."
    mi "Ой, ребята, вы гулять?"
    me "Да, прогуляемся немножко. А ты куда в такой час?"

    show mi pioneer shy with dspr

    "Кажется, она немного смутилась."
    mi "Я, н-ну… {w}А Шурик уже вышел из бани, не знаете?"
    "Я глупо улыбнулся."
    th "От оно што."
    me "Он заходил после меня, скоро выйдет наверное."

    show mi pioneer surprise with dspr

    mi "Хорошо, спасибо. Пока, Славя!"

    show sl pioneer smile2 with dspr

    sl "Пока, Микусь!"

    hide mi
    show mi pioneer shy far at fleft
    with half_good_dspr

    "Мику собиралась было уйти, но резко остановилась, и развернувшись на ходу, сказала."
    mi "Семён, до встречи завтра в клубе!"
    me "До встречи!"

    stop music fadeout 2.0

    show mi pioneer shy far at walk_away_left
    pause(0.5)
    hide mi
    show sl pioneer smile
    with dspr

    "Мы со Славей посмотрели друг на друга, улыбнулись, и продолжили идти дальше."

    play music music_list["silhouette_in_sunset"] fadein 2.0 volume 0.75

    sl "Они что, встречаются?"
    me "Не знаю. Но вроде как они сблизились после танцев, помнишь?"

    show sl pioneer smile2 with dspr

    sl "Точно, было дело."
    sl "Это же ты тогда подсобил, да?"
    "Я приятно ухмыльнулся, вспоминая, как подбил Шурика потанцевать с Мику, и ответил."
    me "Да, немного приложил к этому руку."

    hide sl
    show bg ext_house_of_sl_night
    show sl pioneer smile at cright
    with dissolve

    "Наконец, мы подошли к домику Слави."
    sl "Подожди меня несколько минут, я вещи сложу, и выйду, хорошо?"
    me "Конечно."

    hide sl with long_dspr

    "Славя зашла в домик, а я, решив не терять времени зря, зашел за угол её с Женей дома, и стал курить."

    call smoking_process(with_pause=1.0)

    "..."

    show sl pioneer normal far at fright
    with good_dspr

    "Славя вышла быстрее, чем я ожидал."

    show sl pioneer surprise with dspr

    "Кажется, она немного испугалась, потому что сразу выйдя из порога, и не увидев меня, стала озираться, и произнесла."
    sl "Семён! Ты где?"
    me "Тута я!"
    "Я выглянул из-за угла."

    show sl pioneer normal with dspr

    sl "А-а, фух."

    hide sl
    show sl pioneer smile at cright
    with good_dspr

    "Она подошла ближе."
    sl "Я уж думала ты сбежал."
    me "Я? От тебя? Да не в жизнь!"

    show sl pioneer shy with dspr

    sl "Извини."
    me "Ничего страшного."

    hide sl
    show sl pioneer smile at right
    with dspr

    "Я сделал последние затяжки, и мы направились к моему домику…"

    show bg ext_house_of_mt_night_without_light with dissolve

    me "Подождёшь меня? Я быстро."
    sl "Хорошо."
    me "Только не сбегай!"

    show sl pioneer laugh with dspr

    "Мы посмеялись, и я зашёл в домик."

    hide sl
    show bg int_house_of_mt_night2
    with dissolve

    th "Хм. Вожатой нет, и дверь открыта. Странно."
    th "Куда она опять ушла?"
    "Сложив все свои вещи, я вышел из домика, и закрыл его своим ключом."

    show bg ext_house_of_mt_night_without_light
    show sl pioneer smile at right
    with dissolve

    "Наконец-то, мы со Славей были свободны."

    stop music fadeout 2.0

    "Я подошёл к девушке."
    sl "Ну что, куда пойдём?"

    play music music_list["what_do_you_think_of_me"] fadein 2.0 volume 0.7

    me "Пойдём… Пойдём на лодочную станцию."
    "Я многозначно посмотрел на неё."
    me "Возможно, там сейчас также красиво, как и в тот день, когда мы танцевали."

    show sl pioneer shy with dspr

    "Славя, кажется, поняла намёк, и ответила."
    sl "Пойдём."

    hide sl
    show bg ext_houses_night
    show sl pioneer smile2 at right
    with dissolve

    "Мы шли, держась за руки, и изредка что-то говорили."
    "Кажется, мы оба понимали, что сейчас произойдёт."
    "Возможно, почувствовали мы это уже давно, но лишь недавно наши чувства настолько переполнились, что ждать уже было невозможно…"

    show bg ext_square_night with dissolve

    "По пути меня не отпускали бесконечные мысли о том, как лучше сделать, что сказать… {w}Я перебирал варианты как завести разговор, сказать, признаться."
    "Думал о том, что она может ответить… {w}И ответит ли взаимностью?"
    "Но идеальная схема всё не выстраивалась. Я начинал переживать, по телу побежал легкий мандраж, в горле пересохло."

    stop ambience fadeout 1.0

    show bg ext_boathouse_night with dissolve

    play ambience ambience_boat_station_night fadein 1.0

    "Наконец, мы вышли к лодочной станции."
    "На небе мерцали мириады звёзд, а лунный свет красиво отражался в воде, заливая всё пространство вокруг мягким синеватым оттенком."
    me "Давай спустимся немножко пониже."
    sl "Давай."
    "Мы спустились по насыпи, и прошли левее. Таким образом, оказавшись примерно между пляжем и станцией."
    "..."
    "Остановившись на берегу, мы смотрели на звёзды, на воду…"
    "Внезапно я понял."
    "Когда мы были здесь, и танцевали, когда впервые поцеловались, я не думал о том, как мне поступить."
    "Я делал так, как велит мне сердце…"

    hide sl
    show sl pioneer shy at center
    with good_dspr

    "Я обогнул Славю, встал лицом к ней, и взял её за руки."
    me "Разреши пригласить тебя на танец?"

    show sl pioneer tender with dspr

    stop music fadeout 3.0

    "Славя посмотрела на меня счастливыми глазами, и подала мне руку."

    pause(1.0)
    play music music_list["forest_maiden"] fadein 2.0 volume 0.9

    hide sl
    show cg d5_sl_dance
    with dissolve1

    "Мы закружились в танце. Сначала медленно, вспоминая движения."
    "Но уже скоро для нас вновь перестал существовать мир вокруг. Остались только мы вдвоём, в этом бесконечном мгновении единения."
    "Нам обоим было это нужно. Оторваться от мира вокруг, чтобы в полной мере сфокусироваться друг на друге."
    "Услышать, как наши сердца бьются в унисон, почувствовать взаимную энергию душ, и понять, кто же мы друг для друга."
    "Действительно понять, что сейчас произойдёт нечто, способное разделить наши судьбы на до и после."
    "И мы оба это понимали. Мы понимали, что обе наши судьбы уже слились воедино, и сплелись крепкими узлами. Мы оба уже не представляли себя друг без друга."

    pause(1.0)

    hide cg
    show sl pioneer shy at center
    with dissolve

    play sound sfx_head_heartbeat fadein 1.0 volume 0.7 loop

    "Вскоре, мы остановили движения, и замерли друг на против друга."
    "Я крепче взял руки девушки, и посмотрел прямо в её глаза."
    me "Славя…"
    me "Я люблю тебя."

    stop sound fadeout 0.5

    show sl pioneer tender with dspr

    pause(1.0)

    "Кажется, моё сердце пропустило пару ударов, стало тяжело дышать."
    "Мгновения ожидания ответа показались вечностью."
    "Но вот, из её глаз начали стекать слёзы."

    show sl pioneer happy_cry with good_dspr

    sl "Сёма… {w}Я до последнего надеялась, что ты это скажешь."
    sl "Я тоже тебя люблю."
    "Я не мог поверить своему счастью."
    "Мы стояли на берегу, держась за руки, и смотрели друг на друга влюблёнными глазами."
    "То облако эмоционального напряжения, которое витало между нами все эти дни, тут же разрядилось."
    "Мы больше не скрывали друг от друга своих чувств."
    "Я вновь посмотрел на Славю."

    hide sl
    show cg d5_sl_kiss
    with dissolve

    "Переведя одну руку ей на талию, я притянул её к себе, и поцеловал."
    "Она не сопротивлялась."
    "Напротив, Славя крепко прижалась ко мне, обняв за плечи, и мы слились в долгом, чувственном поцелуе."
    "..."

    pause(3.0)

    hide cg
    show sl pioneer happy_cry
    with dissolve

    "Через некоторое время мы прекратили поцелуй, но всё так же стояли, обнимаясь."

    hide sl
    show sl pioneer tender close at cright
    with good_dspr

    "Славя положила мне голову на грудь."
    sl "Сёма, я так счастлива!"
    sl "Так счастлива, что не давала себе повода усомниться в тебе…"
    sl "Как же хорошо, что ты появился в моей жизни."
    "Я положил одну руку ей на голову, и погладил её."
    me "Я тоже очень рад, что встретил тебя здесь."
    th "И что вообще оказался здесь."
    "..."
    "Девушка всхлипнула, утерла мокрые глаза, и ещё раз меня поцеловала."
    sl "Давай немножко посидим? Вон там, под деревьями."
    me "Конечно."
    "Продолжая держаться за руки, мы зашли под деревья."

    hide sl
    show cg d5_sl_love
    with dissolve

    "Я сел под одно из них, а Славя опустилась между моих ног, и облокотилась на меня спиной."
    "Мы долго сидели, и вспоминали всё, что успели пережить в лагере за эти дни вместе."
    "Прошло всего пять дней, а по ощущениям я был влюблён в эту девушку гораздо дольше."
    "Ещё мы детальнее успели поговорить про общие интересы, Славя несколько раз уже загадывала на будущее…"
    "Я поддерживал её, но мне было страшно."
    th "Что произойдёт, когда смена закончится? Уеду ли я с ней, и начну жизнь с чистого листа?"
    th "Или попаду обратно в свой мир?.. {w}Где снова будет холодно, одиноко и бессмысленно?"
    "Я откинул эти мысли, и лишь сильнее обнял Славю."
    "Ведь вот она, сидела рядом со мной."
    "Смотрела на меня глазами, полными любви."
    "Я чувствовал тепло её тела, её дыхание. Ощущал её прикосновения. Слышал её голос."
    "А это значит, что сейчас всё было по-настоящему. Сейчас, в этот момент."
    "И я им наслаждался."
    "А что произойдёт потом? Мне всё равно не суждено на это повлиять."
    "..."

    pause(2.0)

    stop music fadeout 3.0

    hide cg
    show sl pioneer smile2 at right
    with dissolve

    "Вскоре уже сильно стемнело, и мы решили отправляться по домам."

    play music music_list["raindrops"] fadein 2.0 volume 0.85

    "Славя взяла меня под руку, и мы пошли в сторону площади."

    stop ambience fadeout 1.0

    show bg ext_path2_night with dissolve

    play ambience ambience_camp_center_night fadein 1.0
    play sound sfx_owl_far volume 0.9

    "Когда мы проходили небольшой пролесок, вдалеке послышался крик совы."

    hide sl
    show sl pioneer scared close at cright
    with good_dspr

    sl "Ой, мамочки!"
    "Она ещё сильнее обняла мою руку."
    me "Ха, ну ты чего? Это же просто сова."

    show sl pioneer tender with dspr

    sl "Я всё равно боюсь, тут очень темно!"
    "Я погладил Славю по руке, и ответил."
    me "Сейчас уже придём."

    show bg ext_square_night with dissolve

    "Мы вышли к площади."

    hide sl
    show bg ext_house_of_sl_night
    show sl pioneer smile2 close at center
    with dissolve1

    "И пройдя по «жилому кварталу», пришли к домику Слави."
    "Мы обнялись, и снова заключили друг друга в долгий тёплый поцелуй."
    "..."
    me "До завтра?"
    sl "Я уже не могу дождаться, когда оно настанет!"

    hide sl
    show sl pioneer smile2 far at center
    with long_dspr

    "Славя поднялась на первые ступеньки, послала мне воздушный поцелуй, и зашла в домик."

    hide sl with good_dspr

    "А я, прижав пойманный поцелуйчик к сердцу, зашёл за дерево рядом с её домиком, и закурил."
    
    call smoking_process

    "Я долго курил, осмысляя всё, что со мной сейчас происходит…"
    "Думал о том, как же мне повезло встретить её здесь.."
    "Быть может, в этом и заключалась тайна моего попадания сюда? {w}Чтобы я нашёл своё {b}счастье{/b}?"
    "..."

    show black with clocks_in

    show bg ext_house_of_mt_night_without_light
    hide black with clocks_out

    "Пришёл к своему домику я только минут через десять."
    "Не знаю, сколько сейчас было, но по ощущениям, время приближалось к полуночи."

    stop ambience fadeout 1.0

    show bg int_house_of_mt_night2 with dissolve

    play ambience ambience_int_cabin_night fadein 1.0

    "Я аккуратно зашёл в домик. Вожатая спала."
    "Как можно тише закрыв дверь на ключ, я разделся и лёг в постель."
    "Засыпал я с таким простым, но далеко не каждому данным понять в полной мере чувством."
    "Я был счастлив."

    window hide

    stop ambience fadeout 1.0
    stop music fadeout 3.0

    show blink

    $ renpy.pause(3.5, hard=True)

    jump simple_happiness_mod_day6


# День 6
label simple_happiness_mod_day6:
    $ renpy.block_rollback()
    $ backdrop = "days"
    $ new_chapter(6, u"Простое Счастье. День 6")

    call set_time

    $ set_mode_adv()

    play ambience ambience_int_cabin_day fadein 3.0 volume 0.9
    play sound sfx_hell_alarm_clock fadein 1.5 volume 0.35 fadeout 1.5

    show bg int_house_of_mt_day
    hide blink
    show unblink

    window show

    "Я проснулся от будильника Ольги Дмитриевны."

    hide unblink

    "Но даже этот ужасный звук не мог испортить сегодняшнее утро."
    "Ведь вчера я решился на очень важный шаг. {w}Я признался Славе в любви. {w}И она ответила взаимностью."

    play music music_list["my_daily_life"] fadein 2.5 volume 0.7

    "Это было первое, о чём я подумал, когда проснулся."

    show mt pioneer grin at fright
    with long_dspr

    "Вожатая, по всей видимости, заметила у меня на лице глупую улыбку, и сказала."
    mt "Приём, Земля вызывает Семёна!"
    "Я посмотрел на неё, ещё шире улыбнувшись от шутки."
    mt "Доброе утро, любовничек. Что, не успел проснуться, а уже весь о ней?"
    me "Да… {w}Доброе утро, Ольга Дмитриевна."
    mt "Э-эх, молодость! Любовь, романтика!"

    show mt pioneer smile with dspr

    mt "Но это не отменяет того, что надо вставать, так что пошевеливайся."
    me "Ла-адно."
    "Так как вчера вечером я мылся в бане, сегодня утром решил не идти к умывальникам."
    "Я заправил постель, и просто почистил зубы и умылся, используя воду из чайника."

    show mt pioneer angry with dspr

    mt "Ну ты, крахобор! А кофе я как делать буду?"
    me "Да ладно вам, Ольга Дмитриевна, хватит нам воды кофе попить! Если надо будет, я принесу."

    show mt pioneer smile with dspr

    "Она улыбнулась."
    mt "Ну, ты сам это сказал."
    th "Вот блин."
    "Как оказалось, вода и правда была последняя, так что нам с вожатой хватило сделать меньше чем по половине чашки кофе."
    "Мы выпили их, и направились в столовую."

    stop ambience fadeout 1.0

    show black with clocks_in

    play ambience ambience_camp_center_day fadein 1.0

    hide mt
    show bg ext_dining_hall_near_day
    show mt pioneer normal at fleft
    show sl pioneer smile at right
    hide black
    with clocks_out

    "На входе мы пересеклись с подходящей Славей."

    hide sl
    show sl pioneer tender close at cright
    with dspr

    "Стоило ей меня увидеть, как она тут же подбежала, и обняла меня, чуть-ли не запрыгнув мне на руки."
    "Я тоже заулыбался, и радостно принял её в свои объятия, раскинув руки, и прижав к себе."

    show mt pioneer surprise with dspr

    mt "Славя! Ну ни… Ну т… Держите себя в руках, пожалуйста!"

    hide sl
    show sl pioneer shy at right
    with dspr

    "Мы прервали объятие, и Славя виновато посмотрела на вожатую."
    sl "Ольга Дмитриевна, извините… {w}Здравствуйте!"

    show mt pioneer smile with dspr

    mt "Да ладно, чего уж там. Я же всё понимаю."
    mt "Вы хорошие ребята, но всё-таки контролируйте себя."
    
    show sl pioneer smile2 with dspr

    "Мы со Славей активно закивали, и вместе с вожатой зашли в столовую."

    stop ambience fadeout 1.0

    hide mt
    hide sl
    show bg int_dining_hall_people_day
    show sl pioneer smile at center
    with dissolve1

    play ambience ambience_dining_hall_full fadein 1.0

    "..."
    "Получив свою пайку, мы заняли свободный столик, и пожелали друг другу приятного аппетита."
    me "В лагерном распорядке сегодня что-нибудь назначено, не знаешь?"
    sl "Даже не знаю… {w}М-м, ну в пятницу обычно какие-нибудь массово-развлекательные мероприятия. Кино там, или постановки."
    sl "Но никто ничего не ставил, так что даже не знаю. Вожатая на линейке, я думаю, скажет."
    "Мы продолжили есть, обсуждая разные вещи. Особенно меня заинтересовало кино."
    sl "Ну, отдельного кинотеатра тут нет, конечно. Под это дело обычно спортзал переделывают."
    me "Во-от как."
    sl "Да. Просто расставляют стулья из столовой и включают на проекторе."
    sl "Кстати, вы же уже сегодня клубом будете «мини-концертить»?"
    me "Да, после обеда."
    sl "Хорошо, я обязательно приду! Может ещё кого притащу, если получится. Женю например."
    "Я, зная какая Славя активистка, предупредил."
    me "Только пол лагеря не собирай."
    "Я улыбнулся."
    me "Девочки хотели локальное событие, да и переживать насчёт игры все будут."

    show sl pioneer smile2 with dspr

    "Славя улыбнулась в ответ."
    sl "Ну конечно, я же понимаю. Да кроме Жени я наверное, и не приведу никого больше."
    "Мы продолжили есть и разговаривать."
    "Странно, но к нам так никто и не подсел."
    "..."
    "По итогу, так и доев вдвоём, мы сдали подносы, и направились на линейку."

    stop ambience fadeout 1.0

    show black with clocks_in

    play ambience ambience_camp_center_day fadein 1.0

    hide sl
    show bg ext_square_day
    show sl pioneer smile at fleft
    hide black
    with clocks_out

    "Когда мы пришли на площадь, вожатой ещё не было."

    show dv pioneer normal at center
    show un pioneer smile at cright
    show mi pioneer normal at fright
    with good_dspr

    "Но мы увидели Алису, Лену и Мику, которые уже стояли в ряду, и подошли к ним."
    me "Всем привет!"
    sl "Привет, девочки."
    "Девочки поздоровались."
    me "Что-то мы вас в столовой не видели."

    show mi pioneer smile with dspr

    mi "Ой, а мы вас тоже. Ещё подумали, странно, где же вы."
    mi "А вы наверное за дальними столиками сидели, а мы просто опоздали, вот, я Лену ждала, а Алиса Ульяну."
    mi "Вот и пришлось нам за ближайший столик садиться."
    me "Вот оно что, понятно!"

    show dv pioneer smile with dspr

    dv "Ну что, сразу после обеда начинаем?"

    show mi pioneer happy with dspr

    mi "Я думаю, да. Уже все готовы, осталось последний раз прорепетировать, и аппаратуру подготовить."

    show mi pioneer smile with dspr

    "В этот момент подошла вожатая, и нам пришлось прервать разговор."
    mt "Стройсь!"
    "..."

    hide sl
    hide dv
    hide un
    hide mi
    show cg d2_lineup
    with dissolve

    "На линейке мы узнали, что после обеденного отдыха будет кино, Славя не прогадала."
    "А ещё отряды помладше назначили притащить из столовой стулья после обеда, а до этого времени в спортзале надо было убраться."
    "К счастью тоже не нам, но старшей вожатая назначила Славю."
    "А больше, в общем-то, новостей не было."
    "Так что {i}«Последняя линейка текущей смены торжественно объявляется закрытой!»{/i} - как провозгласила вожатая."

    hide cg with dissolve

    "Я уже было хотел попрощаться со Славей, и идти с девочками в клуб, как тут меня окрикнула вожатая."

    show mt pioneer normal far at left
    with dspr

    mt "Семён, ко мне!"

    hide mt
    show mt pioneer normal at cleft
    with dspr

    "Я подошёл."
    mt "Ты ничего не забыл?"
    "Я немного напрягся."
    th "Что я мог забыть?"
    me "Я-а-а… {w}М, ничего не забыл?"

    show mt pioneer grin with dspr

    mt "Хи, ответ неверный."
    mt "Да ладно, не напрягайся ты так."

    show mt pioneer smile with dspr

    mt "Принеси пожалуйста нам в домик бутылку воды из столовой. Ты обещал!"
    "И правда, обещал."
    th "Ну ладно, хорошо хоть не мешок сахара."
    "Я уже было хотел обернуться, и сказать девочкам, что задержусь, чтобы шли без меня, но подошла Мику."

    show mi pioneer normal at cright
    with dspr

    mi "Ольга Дмитриевна, я хотела с вами поговорить."

    show mt pioneer normal with dspr

    mt "Да, Мику, что такое?"

    show mi pioneer smile with dspr

    mi "Мы сегодня музыкальным кружком хотели бы провести что-то вроде генеральной, так сказать, показательной репетиции. И ещё Алиса."
    mi "После обеда, вот. Народ мы не собираем, но все желающие смогут прийти, играть будем на открытом воздухе возле клуба."
    mt "Хм-м. Показательная, да? А что, звучит неплохо."

    show mt pioneer smile with dspr

    mt "Добро, делайте."

    show mi pioneer happy with dspr

    mi "Спаси-и-ибочки, Ольга Дмитриевна."
    mt "Пожалуйста, Мику."
    "Вожатая повернулась на меня."

    show mt pioneer angry with dspr

    mt "Семён, ты ещё здесь!?"

    show mi pioneer surprise with dspr

    me "Ой, уже бегу!"

    show mt pioneer angry at walk_away_left
    show mi pioneer surprise at walk_away_left
    pause(0.5)
    hide mt
    hide mi
    with dspr

    "Я быстрым шагом направился в сторону столовой."

    window hide

    play sound sfx_clocks fadein 0.5 volume 0.8

    show black with clocks_in

    show bg ext_dining_hall_near_day
    hide black
    with clocks_out

    show black with clocks_in

    show bg ext_house_of_mt_day
    hide black
    with clocks_out

    stop sound fadeout 0.5

    window show

    "Донести пятилитровую бутылку с водой было не так уж и сложно, к тому же что в столовой она уже была наполнена."
    "Так что, расправившись с этим, я отправился в клуб."

    show black with clocks_in

    show bg ext_musclub_day
    show dv pioneer2 smile at right
    hide black
    with clocks_out

    "У входа меня ждала Алиса."
    me "Курить?"
    dv "А как же!"
    "..."
    "Покурив за углом, мы наконец зашли в здание."

    stop ambience fadeout 1.0

    show bg int_musclub_mattresses_day
    show un pioneer normal at left
    show mi pioneer normal at center
    with dissolve

    play ambience ambience_music_club_day fadein 1.0

    "Лена уже стояла перед пюпитром, и смотрела в ноты, а Мику настраивала гитару."
    "Когда она нас увидела, то встала, и заявила."

    show mi pioneer smile with dspr

    mi "Отлично, все в сборе. {w}Тогда начнём!"

    stop music fadeout 2.0

    hide un
    hide dv
    hide mi
    with long_dspr

    call to_nvl_mode

    play music music_list["so_good_to_be_careless"] fadein 2.0 volume 0.8

    "Мы начали репетировать."
    "Мику опять начала с меня, и моей предстоящей игры для Слави, пока Алиса повторяла свою композицию, а Лена доводила партию флейты до идеала."
    "Уже через полчаса я мог полностью сыграть мелодию, а через час делал это идеально."
    "Сыграв в последний раз, Мику заключила."
    mi_n "Отлично, Семён, ты большой молодец! Я уверена, Славе понравится!"
    me_n "Спасибо!"
    me_n "Ну что, перерывчик, и дальше?"
    mi_n "Да!"
    nvl clear
    "После перерыва мы усиленно принялись за «Самое тёплое лето»."
    "Всё-таки, это было самое сложное, что нам предстояло сыграть. А мне, как не-музыканту, приходилось напрягаться вдвойне, играя параллельно со флейтой и вокалом."
    "Но уже скоро мы дали идеальное исполнение."
    mi_n "Отлично! Вот, вот, так и надо!"
    un_n "Давайте ещё раз!"
    me_n "Вперёд!"
    "Мы отрепетировали ещё несколько раз, и закрепили успех."
    "Теперь мы были готовы выступить."
    mi_n "Алиса, давай прогоним твои «Костры» пару раз, а то так и не получалось же вместе сыграть!"
    dv_n "Ой, да я уверена, всё получится! Под ритм барабанов играть проще, а ты точно справишься."
    "Но всё же они несколько раз прогнали композицию."
    "Как и предполагала Алиса, получилось у них идеально даже с первого раза."

    call to_adv_mode

    show un pioneer smile at fleft
    show dv pioneer2 smile at fright
    show mi pioneer happy at center
    with good_dspr

    mi "Фух!"

    show mi pioneer smile with dspr

    mi "Так, небольшой перерыв, и у нас остаётся не больше полутора часов, чтобы подготовить на улицу всю необходимую аппаратуру."

    hide dv
    show dv pioneer2 laugh at right
    with dspr

    "Алиса вскочила с дивана и карикатурно козырнула."
    dv "Есть, так точно, мэм, грж-нин начальник! Разрешите перекур?"

    show mi pioneer laugh with dspr

    "Мику посмеялась."
    mi "Ахах, разрешаю!"
    "Мы с Алисой покурили, а затем все вместе начали подготавливать себе всё необходимое для выступления."

    stop ambience fadeout 1.0

    hide dv
    hide un
    hide mi
    show bg ext_musclub_day
    show un pioneer normal at fleft
    show dv pioneer2 smile at cleft
    show mi pioneer normal at right
    with dissolve

    play ambience ambience_camp_center_day fadein 1.0

    "Мы вынесли пюпитр с флейтой для Лены, и микрофон для Мику."
    "Затем пошли барабанная установка, благо она была разборная, гитары, моя акустическая, и электрическая Алисы."
    "Самым сложным оказалась колонка с усилителем, мы несли её втроём."
    "Я с одной стороны, а Мику и Алиса с другой, Лена держала дверь."
    "И вот, веранда уже преобразилась."

    show bg ext_musclub_concert_day with dissolve1

    "Но возникла другая проблема."

    show dv pioneer2 surprise with dspr

    dv "Мику-у! Удлинитель не дотягивается."

    show mi pioneer sad with dspr

    mi "О-хоо! Я не думала, что он такой короткий!"

    show un pioneer smile with dspr

    un "Может у кибернетиков есть?"

    show dv pioneer2 normal
    show mi pioneer grin
    with half_good_dspr

    mi "О, и правда. Мне Шурик даст!"
    mi "Я сейчас!"

    show mi pioneer grin at run_away_left
    pause(0.5)
    hide mi with good_dspr

    "Мику помчалась в клуб кибернетики, а мы продолжили оставшиеся приготовления."
    "..."

    stop music fadeout 2.0

    show black with clocks_in

    play music music_list["went_fishing_caught_a_girl"] fadein 2.0 volume 0.79

    show mi pioneer smile at right
    show dv pioneer2 smile
    show un pioneer normal
    hide black
    with clocks_out

    "Наконец, когда новый удлинитель был найден, всё было подключено и ждало своего часа, мы встали перед верандой, оценивая свою работу."
    me "Ну? Молодцы мы?"

    show mi pioneer happy with dspr

    mi "Хи-хи, ещё какие!"
    dv "Эх, вот было бы у нас времени побольше. Недели две! Мы бы тут такой концерт забабахали!"

    show un pioneer smile with dspr

    un "Ну, может в другой раз?"

    show mi pioneer smile with dspr

    mi "Ладно, скоро уже обед, давайте собираться."
    "Мы всё ещё раз проверили, Мику закрыла клуб, и мы направились в столовую."

    show bg ext_square_day with dissolve

    play sound sfx_dinner_horn_processed volume 0.9

    "Вышли мы как раз вовремя, ибо по пути заиграл горн."
    "Мы прибавили шагу."

    hide dv
    hide mi
    hide un
    show bg ext_dining_hall_away_day
    show sl pioneer smile at cright
    with dissolve1

    "На входе я подошёл к Славе, а девочки сразу пошли внутрь."
    "Славя оглянулась, видимо, чтобы не попасться вожатой, и быстренько меня обняла и поцеловала."

    show sl pioneer smile2 with dspr

    sl "Я успела соскучиться!"
    me "Я тоже!"
    "Я улыбнулся."

    hide sl
    show sl pioneer smile at right
    with dspr

    "Мы начали заходить в столовую и параллельно беседовать."

    show bg ext_dining_hall_near_day with dissolve

    me "Ну как там в импровизированном кинотеатре? Всё готово?"
    sl "Да, а у вас?"

    stop ambience fadeout 1.0

    show bg int_dining_hall_people_day with dissolve

    play ambience ambience_dining_hall_full fadein 1.0

    "Мы зашли в столовую."
    me "Да, у нас тоже всё готово."

    show sl pioneer smile2 with dspr

    sl "Отлично, тогда после обеда я сразу с вами!"
    sl "Женя тоже пойдёт, всё таки уговорила её."
    sl "Хоть раз за смену побудет не в библиотеке. А то две с половиной недели тут провела, а вся бледная."
    me "Здорово, чем больше народу тем веселее. Главное не через меру, хе-хе."
    "Мы взяли подносы, и нас позвала Мику с одного из ближайших столиков."
    mi "Ребята, давайте к нам!"

    show sl pioneer surprise with dspr

    sl "Ой, но там же всего одно место осталось."

    show sl pioneer smile with dspr

    me "Ничего страшного. Ты садись, а я рядом стул подставлю."

    hide sl
    show un pioneer smile at cleft
    show sl pioneer smile at fleft
    show dv pioneer normal at cright
    show mi pioneer smile at fright
    with good_dspr

    "Славя села рядом с Леной, а я подставил стул с другого столика, и сел с краю."
    "Мы начали кушать и обсуждать ближайшие планы."
    "..."

    stop ambience fadeout 1.0

    show bg ext_dining_hall_near_day with dissolve1

    play ambience ambience_camp_center_day fadein 1.0

    "Выйдя из столовой, мы всей компанией двинулись в сторону музыкального клуба."

    hide un
    hide dv
    hide mi
    hide sl
    show bg ext_square_day
    show un pioneer smile at fleft
    show dv pioneer smile at cleft
    show mi pioneer normal at cright
    show sl pioneer smile at fright
    with dissolve

    "По дороге мы весело обсуждали всякие забавные истории и ситуации, у кого какие были."

    hide un
    hide dv
    hide mi
    hide sl
    show un pioneer smile far at fleft
    show dv pioneer smile far at cleft
    show mi pioneer normal far at center
    show sl pioneer smile at right
    with dissolve

    "Остальные девочки шли впереди, а мы со Славей немного отстали, и я шепнул ей на ухо."
    me "{i}Была тут у меня недавно одна забавная ситуация…{/i}"

    show sl pioneer shy with dspr

    "Славя конечно же поняла о чём я, и немного смутившись, посмеялась."
    sl "{i}Аха-ха, Сёма блин, дурак!{/i}"
    "Я улыбнулся тому, что мы можем обсуждать такие вещи смехом."

    show sl pioneer smile
    show bg ext_musclub_concert_day
    with dissolve

    "Наконец, мы добрались до музыкального клуба."

    hide un
    hide dv
    hide mi
    show un pioneer smile at fleft
    show dv pioneer smile at cleft
    show mi pioneer normal at center
    with long_dspr

    "Вместе со Славей мы подошли к Мику, и остальным, и Славя спросила."
    sl "Когда начнёте?"
    mi "Хм-м, даже не знаю. Все музыканты уже тут. Осталось желающих дождаться. А... А кто, собственно, желающие?"

    show sl pioneer smile2 with dspr

    sl "Ну, я уже тут, хи-хи."

    show sl pioneer smile with dspr

    sl "Женя ещё подойдёт."
    mi "Ещё Шурик вроде обещал."
    "Повисла небольшая пауза."
    me "Ну, минут 20 наверное выжидаем, и хватит."

    show mi pioneer smile with dspr

    "Мику согласилась."
    
    show sl pioneer smile at walk_away_right
    pause(0.5)
    hide sl with dspr

    "Мы направились к инструментам, чтобы ещё раз всё проверить, а Славя села на скамейку рядом с крыльцом, и с интересом наблюдала за всеми нами."
    "..."

    show mz pioneer smile at right
    with good_dspr

    "Вскоре подошла Женя."
    mz "Ого, ничего себе у вас тут инструментов."
    mz "Может и не зря пришла!"
    sl "Женя, давай ко мне!"

    show mz pioneer smile at walk_away_right
    pause(0.5)
    hide mz with dspr

    "Женя села на скамейку рядом со Славей, а мы продолжили подготовку."
    "..."
    "На горизонте показалась вожатая."

    show dv pioneer surprise
    show mt pioneer normal at fright
    with good_dspr

    "Алиса посмотрела в её сторону."
    dv "Чего это она тут?"

    show mi pioneer normal with dspr

    mi "Не знаю, может сказать что-то хочет?"

    show dv pioneer normal with dspr

    "Вожатая подошла и заговорила."
    mt "Ну что, ребята, уже скоро начинаете?"
    mt "Я тоже послушаю."

    show mt pioneer smile with dspr

    mt "Не могу же я пропустить самодеятельность своих пионеров!"
    "Она по-доброму улыбнулась, и встала рядом с верандой, наблюдая за нами."

    show mt pioneer smile at walk_away_right
    pause(0.5)
    hide mt with dspr

    pause(1.0)
    
    show sh pioneer normal at right
    with dspr

    "Вскоре подошёл Шурик."

    show sh pioneer normal_smile with dspr

    sh "Представитель клуба кибернетиков на месте!"
    "Бодро заявил он."

    show mi pioneer smile with dspr

    "Мику увидела его, и помахала рукой."
    mt "А Электроник не пришёл?"
    "Послышался голос Ольги Дмитриевны неподалёку."

    show sh pioneer normal with dspr

    sh "Он с роботом возится. Да и ему не интересно, он сказал."
    "..."

    stop music fadeout 1.0

    hide mi
    hide dv
    hide un
    hide sh
    show un pioneer normal at fleft
    show dv pioneer smile at fright
    show mi pioneer normal at cleft
    with dissolve

    play music music_list["went_fishing_caught_a_girl"] fadein 1.0 volume 0.59

    "Мы все уже стояли на импровизированной сцене на веранде."
    "Лена стояла возле пюпитра и бегала глазами по нотам."
    "Алиса уже в который раз пробовала, как бы ей получше встать."
    "Я же просто стоял с гитарой у окна, и держал её за гриф. Так как сейчас с ней буду выступать не я."
    "А Мику, положив на барабан палочки, подошла ближе к выходу из веранды, взяла микрофон и начала говорить."

    hide mi
    show mi pioneer smile at center
    with good_dspr

    mi "Приветствую всех желающих поприсутствовать на генеральной репетиции музыкального клуба!"
    mi "Прошу всех встать поближе, но не мешать друг другу, начинаем уже через минуту!"

    show mi pioneer normal with dspr

    "Мику положила микрофон, и подойдя ко мне, взяла у меня гитару, и устроила её рядом со стулом перед выходом."
    "Когда она хотела было уже вновь взять микрофон, я увидел как к нам подходит какая-то пионерка, но не из нашего отряда."
    me "Мику, подожди."

    show mi pioneer smile with dspr

    "Она оглянулась на меня, а я кивнул головой в сторону дорожки."
    "Остальные участники, как и Мику, посмотрели в ту сторону."

    show dv pioneer normal
    show un pioneer normal
    with dspr

    dv "Кто это?"
    un "Не знаю, из другого отряда наверное."

    show un pioneer smile
    show mi pioneer happy
    with dspr

    "Наконец, девушка встала вместе с остальными, Мику взяла микрофон и произнесла."
    mi "Спасибо всем кто пришел на нашу генеральную репетицию."
    mi "Композиций не много, и они короткие, но надеемся, они вам понравятся."

    stop music fadeout 3.0

    pause(1.0)

    "Она выдержала небольшую паузу."
    mi "Первая композиция моего сочинения и исполнения для акустической гитары. «Воспоминания»."
    mi "Я написала её в память о своей родине, о Японии."

    show mi pioneer smile with dspr

    play sound sfx_simon_applause fadein 0.5 volume 0.6 loop
    play sound2 "<from 0.2>" + sfx_simon_applause fadein 0.5 volume 0.8 loop
    play sound3 "<from 0.5>" + sfx_simon_applause fadein 0.5 volume 0.55 loop

    "Мику отложила микрофон, а все слушатели, и мы, начали аплодировать."

    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    stop sound3 fadeout 1.0

    "Мику села на стул, устроилась, и начала играть…"

    stop ambience fadeout 1.0

    pause(1.0)

    play ambience ambience_camp_center_day fadein 1.0 volume 0.33

    show cg mi_guitar_yam with dissolve

    play music memories_guitar_only fadein 0.5 noloop

    "Когда Мику начала играть, всё пространство вокруг заполнилось магическим звуком."
    th "Всё-таки она великолепно играет."
    "Все слушатели, и это было даже внешне заметно, тут же обратились в слух."
    "Они стояли, словно зачарованные, и слушали красивейшие ноты, которые Мику извлекала из инструмента мастерскими движениями."
    "Больше всего, кажется, композиция понравилась Шурику."
    "Он подошёл чуть ближе, и встал, уперевшись плечом об веранду."

    call calc_music_how_much_play

    hide cg
    show mi pioneer happy
    show dv pioneer smile
    with dissolve

    "Мику закончила играть, и посмотрела на немногочисленных зрителей."

    pause(1.0)

    play sound "<from 0.0 to 7.0>" + sfx_concert_applause volume 0.7 fadeout 1.5

    "Спустя секундную паузу, все присутствующие начали с энтузиазмом аплодировать. {w}Аплодировали и мы, другие участники."

    show mi pioneer cry_smile with dspr

    "Я не видел лица Мику, но я был уверен, что она улыбается."

    show mi pioneer smile with dspr

    "Когда аплодисменты стихли, Мику встала со стула, и убрав его в сторону, передала мне гитару."
    "Затем она взяла микрофон, и сказала."
    mi "Спасибо вам всем большое за тёплую реакцию!"

    show mi pioneer happy

    mi "Следующая композиция посвящена Совёнку."
    mi "Её я написала под впечатлением от этой смены в лагере, и всех великолепных людях, которых встретила здесь!"

    hide dv
    hide mi
    hide un
    show un pioneer normal at cleft
    show sem normal at cright
    show mi pioneer normal at center
    with dissolve

    play sound sfx_simon_applause fadein 0.5 volume 0.6 loop
    play sound2 "<from 0.2>" + sfx_simon_applause fadein 0.5 volume 0.8 loop
    play sound3 "<from 0.5>" + sfx_simon_applause fadein 0.5 volume 0.55 loop

    "Пока нас встречали аплодисментами, мы с Леной подошли поближе, я перекинул гитару за ремень на плечо."

    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    stop sound3 fadeout 1.0
    
    "Лена встала возле пюпитра, а Мику, сделав громкость микрофона потише, сместилась немного в сторону."
    "Удивительно, но я даже не нервничал."
    "Конечно, был небольшой мандраж, но вызван он был скорее тем, что мне сейчас нужно сыграть идеально с первого раза, а не публикой."
    "Вдохнув, я посмотрел на Лену."

    show un pioneer smile with dspr

    "Она кивнула, и поднесла флейту к губам."
    "Я сложил пальцы в аккорде, занёс медиатор, и-и-и…"

    show cg d6_concert_me_un_mi with dissolve

    play music warmest_summer fadein 0.5 fadeout 0.5 noloop

    "Мы начали играть."
    "Также, как на репетициях. За тем исключением, что на нас сейчас смотрели пять пар глаз, четыре из которых я знал, а одну так и вовсе любил."

    call calc_music_how_much_play

    play sound "<from 0.0 to 8.0>" + sfx_concert_applause volume 0.75 fadeout 1.5

    hide cg with dissolve

    "Мику закончила петь, Лена выдула последний воздух во флейту, а я последний раз коснулся струны."
    "В этот раз слушатели проснулись быстрее, и начали хлопать почти сразу."
    "И, кажется, даже более активно."

    show mi pioneer smile with dspr

    mi "Спасибо вам!"
    mi "Нам очень приятно слышать ваши аплодисменты!"

    pause(1.0)

    hide un
    hide sem
    with long_dspr

    "Вскоре, хлопки утихли. Мы с Леной отошли назад, я поставил гитару, и облокотился на стену здания."

    show mi pioneer grin with dspr

    mi "А теперь, чтобы зарядить всех зарядом бодрости на оставшийся день – немного рока!"
    mi "Композиция «Костры»!"

    play sound "<from 0.0 to 7.0>" + sfx_concert_applause volume 0.35 fadeout 0.5

    "Зрители захлопали, а Шурик даже присвистнул."

    hide mi
    show mi pioneer normal at cleft
    with dspr

    "Мику запрыгнула на барабанную стойку."

    show dv pioneer laugh at cright
    with dspr

    "Алиса вышла к центру, показала козу, и выкрикнула."
    dv "Всем рок-н-ролл!"
    "Алиса отклонилась назад, и занесла руку с медиатором…"

    show cg d6_concert_mi_dv with dissolve

    play music kostry_concert fadein 0.5 fadeout 0.5 noloop

    "И начала играть мелодию."

    pause(3.0)

    "Мику отбила барабанами, и девочки выдали на полную."
    "Клубный усилитель был явно лучше, чем тот, что стоит на сцене, так что звук выходил потрясающий."
    "Я активно качался в такт музыке."
    "В зале, как я видел, Славя притопывает ногой, а вожатая, скрестив руки на груди, и улыбаясь, качает головой в такт."

    call calc_music_how_much_play

    play sound sfx_concert_applause volume 0.95 fadeout 1.0

    hide cg with dissolve

    "Когда девочки закончили играть, помимо, в этот раз явно громких аплодисментов, послышалось несколько растянутых «у-у-ху!»."

    hide mi
    hide dv
    show un pioneer smile at fleft
    show sem normal at cleft
    show mi pioneer normal at cright
    show dv pioneer smile at fright
    with dissolve

    "Я, Лена и Мику подошли к Алисе, и Мику, взяв микрофон, заговорила."

    show mi pioneer shy with dspr

    mi "Спасибо вам большое за то, что пришли!"

    show mi pioneer smile with dspr

    mi "Мы были очень рады услышать ваши аплодисменты, это лучшая награда для любого музыканта!"

    pause(1.0)

    "Все вместе мы поклонились, и на этом наш «мини-концерт» закончился."

    stop ambience fadeout 1.0

    hide mi
    hide dv
    hide un
    hide sem
    with dissolve1

    play ambience ambience_camp_center_day fadein 1.0

    "Продлился он всего несколько минут, но подарил эмоции всем присутствующим."
    "..."

    play music music_list["your_bright_side"] fadein 2.0 volume 0.7

    "После того, как мы закончили, немногочисленные зрители начали подходить к нам, и разговаривать."

    show mt pioneer smile far at fleft
    show sh pioneer normal far at cleft
    show mi pioneer smile far at left
    with good_dspr

    "К Мику подошли Ольга Дмитриевна и Шурик."

    show mt pioneer smile far at walk_away_left
    show sh pioneer normal far at walk_away_left
    show mi pioneer smile far at walk_away_left
    pause(0.5)
    hide mt
    hide sh
    hide mi
    with dspr

    pause(1.0)

    show un pioneer smile far at fright
    show dv pioneer smile far at cright
    show mz pioneer smile far at right
    with good_dspr

    "Женя подошла к Лене и Алисе, и они начали о чём-то беседовать."

    show un pioneer smile far at walk_away_right
    show dv pioneer smile far at walk_away_right
    show mz pioneer smile far at walk_away_right
    pause(0.5)
    hide un
    hide dv
    hide mz
    with dspr

    pause(1.0)

    show sl pioneer smile2 at cright
    with good_dspr

    "Ко мне подошла Славя, обняла меня, и сказала, что я отлично сыграл."
    me "Спасибо."
    me "Ну я поучаствовал то всего в одной композиции из трёх."
    "В отличии, кстати, от Мику, которая отыграла во всех трёх, так ещё и в разных ролях."

    show sl pioneer shy with dspr

    sl "Но мне всё равно больше всего твоя игра понравилась."

    show sl pioneer smile2 with dspr

    sl "Ну и Мику с Алисой. Здорово они конечно!"

    show sl pioneer laugh with dspr

    sl "Видимо, теперь я люблю рок."
    "Мы посмеялись, и к нам подошла та самая неизвестная пионерка."

    show kt normal at left
    show sl pioneer smile
    with good_dspr

    ktp "Хорошо играете."
    me "Спасибо. А ты, кстати, откуда? Я тебя не видел."
    ktp "Я из другого отряда. Сидела рядом с вашим столиком, услышала как вы обсуждаете «мини-концерт». Меня, кстати, Катя зовут."
    me "Приятно познакомиться, Катя. Ну что, не пожалела, что пришла?"
    kt "Ни в коем случае."

    show kt smile with dspr

    "Она улыбнулась."
    kt "Приятно было разбавить повседневные пионерские будни вашей музыкой."
    "Мы перебросились ещё парой фраз, после чего она подошла к Мику и остальным девочкам, и заговорила с ними."

    show kt smile at walk_away_left
    pause(0.5)
    hide kt with dspr

    "..."

    hide sl
    show sl pioneer smile at right
    with good_dspr

    "Мы отошли со Славей в сторону, и сели на лавочку. Она положила свою руку на мою."
    sl "Какие у вас сейчас планы?"
    me "А какие у нас планы? План максимум выполнен успешно!"
    me "Сейчас уберём всю аппаратуру, ну и-и… {w}Кино же сегодня, да?"

    show sl pioneer smile2 with dspr

    sl "Да. Тогда я тебя подожду, вместе пойдём. Может помогу чем."
    me "Спасибо. Думаю, девочки тоже оценят."

    stop music fadeout 2.0

    "..."

    hide sl with dspr

    call to_nvl_mode

    play music music_list["everyday_theme"] fadein 2.0 volume 0.8

    "Вскоре, вожатая, Женя и Шурик ушли."
    "Времени до кино было ещё порядком, так что мы все решили выпить чаю."
    "..."
    "Отпивая травяной напиток, я подумал."
    ths "А когда эта Катя ушла?"
    "Я спросил у остальных, и, как оказалось, никто не видел как она ушла."
    ths "Странно."
    "Впрочем, скоро наш разговор перешёл в совсем другое русло, а допив чай, мы начали убирать всю аппаратуру и инструменты."
    nvl clear
    "По инициативе Мику решено было начать с самого тяжелого и сложного: колонка, усилитель, барабанная установка и пюпитр."
    "Поднять усилитель в этот раз оказалось легче, ибо теперь мы с Алисой взялись спереди и сзади, а Мику и Лена поддерживали по краям. Славя держала дверь."
    "Затем, в ход пошла колонка, и барабанная установка."
    "Дело шло быстро."
    mi_n "Так, ну что, мелочь осталась."
    mi_n "До кино ещё где-то полчаса. Успеваем!"
    "Мы занесли оставшееся: гитары, флейту, пюпитр и стул, и аккуратно расставили всё внутри."

    stop ambience fadeout 1.0

    call to_adv_mode

    show bg int_musclub_mattresses_day
    show un pioneer normal at fleft
    show dv pioneer normal at cleft
    show mi pioneer smile at cright
    show sl pioneer smile at fright
    with dissolve1

    play ambience ambience_music_club_day fadein 1.0

    me "Дело сделано."
    mi "Отлично, тогда в кино!"

    show un pioneer smile with dspr

    un "Интересно, что сегодня будут показывать?"

    show dv pioneer grin with dspr

    dv "Да какая разница, главное поторопиться, а то Сёма наш со Славей не успеют места для парочек занять."

    show sl pioneer shy with dspr

    "Алиса ехидно улыбнулась, а мы со Славей смутились, но спорить не стали."

    stop ambience fadeout 1.0

    show bg ext_musclub_day
    show dv pioneer smile
    with dissolve

    play ambience ambience_camp_center_day fadein 1.0

    "Выйдя из клуба, Мику закрыла его на ключ, и мы направились в импровизированный кинотеатр, который располагался в здании спортзала."

    play sound sfx_clocks fadein 0.5 volume 0.5

    show black with clocks_in

    show bg ext_playground_day
    show dv pioneer smile
    show sl pioneer smile
    hide black
    with clocks_out

    stop sound fadeout 0.5

    "Мы подошли к зданию спортзала, которое располагалось рядом с площадками для волейбола и футбола."
    th "Хах, а я тут и не был ни разу."
    "Мысленно отметив у себя в голове, что даже {b}тут{/b} меня не тянуло к спорту, я обратил внимание на Мику, которая показывала на вход."

    show mi pioneer smile with dspr

    mi "Ой, смотрите, все уже заходят!"
    "Мы прибавили шаг, и зашли в здание спортзала."

    stop ambience fadeout 1.0

    show bg int_cinema_people with dissolve

    play ambience ambience_medium_crowd_indoors_1 fadein 1.0

    "Внутри уже было довольно много пионеров, так что мы начали искать, куда бы сесть."

    hide un
    hide dv
    hide mi
    hide sl
    show sl pioneer smile at right
    with good_dspr

    "Девочки пошли ближе к середине, а мы со Славей заприметили таки слева два свободных места в углу на последнем ряду, и сели туда."

    hide sl
    show sl pioneer normal at left
    with good_dspr

    me "А что тут обычно показывают?"
    "Поинтересовался я."

    show sl pioneer smile with dspr

    sl "Да по разному. Когда про войну, когда про пионерию. Может и просто какой-нибудь фильм."
    th "Понятно, «Терминатора» в пиратской озвучке мне не дождаться."
    "Потихоньку переговариваясь, через несколько минут мы услышали как закрывается входная дверь, а проектор начинает включаться."

    stop ambience fadeout 1.0
    stop music fadeout 3.0

    show bg int_cinema_movie with dissolve

    play ambience ambience_medium_crowd_indoors_1 fadein 1.0 volume 0.35

    hide sl
    show sl pioneer smile2 close at cleft
    with good_dspr

    "Зал стал затихать, я взял Славю за руку, а она положила голову мне на плечо."
    "Фильм начался."

    hide sl with dspr

    play music music_list["confession_oboe"] fadein 3.0 volume 0.6

    pause(1.0)

    call to_nvl_mode

    "Показывали «А зори здесь тихие»."
    "Конечно я смотрел этот фильм пару раз, но выбор его для пионерского лагеря мне показался весьма нетипичным. Хотя бы из-за пары откровенных сцен."
    ths "Хотя, раз цензура пропустила…"
    "Славя, как я понял, тоже уже видела этот фильм."
    "Неудивительно, учитывая скудность выбора у советских граждан."
    "..."
    "Примерно к середине фильма я настолько осмелел, что положил руку Славе на ногу."
    "Она была не против, а лишь взглянула на меня, и немного смутившись, положила свою руку поверх моей."
    "Так мы просидели до конца фильма."
    "..."

    stop music fadeout 2.0
    stop ambience fadeout 1.0

    call to_adv_mode

    show bg int_cinema_people
    show sl pioneer smile at left
    with dissolve

    play ambience ambience_medium_crowd_indoors_1 fadein 1.0 volume 0.85

    pause(1.0)

    "Наконец, фильм закончился, и пионеры начали потихоньку выходить."

    play music music_list["dance_of_fireflies"] fadein 2.0 volume 0.8

    "Славя потянулась, устав сидеть три часа подряд, и сказала."
    sl "Кажется они не учли, что хронометраж у фильма немаленький. Уже время ужина по идее."

    show mt pioneer normal far at fright
    with good_dspr

    "Не успела она это сказать, как в зал зашла ОД, заводя обратно пионеров, которые уже успели выйти, и сказала."
    mt "Так, ребята, внимание!"
    mt "Фильм затянулся, так что сейчас все сразу на ужин."
    mt "Все взяли себе по стулу, и шагом-арш в столовую!"
    "Нам повезло, что сидели мы близко к выходу, так что, взяв стулья, одни из первых вышли из здания."
    "На улице я взял у Слави её стул. Она, конечно, посопротивлялась, но я настоял."

    window hide

    stop ambience fadeout 1.0
    play sound sfx_clocks fadein 0.5 volume 0.8

    show black with clocks_in

    call set_time("sunset")

    play ambience ambience_dining_hall_full fadein 1.0

    hide sl
    hide mt
    show bg int_dining_hall_people_sunset
    show sl pioneer smile at center
    hide black
    with clocks_out

    stop sound fadeout 0.5

    window show

    "Вскоре, мы уже были в столовой, сидели за столом на принесённых нами стульях, и ужинали."
    me "Какие планы на вечер?"

    show sl pioneer smile2 with dspr

    "Славя немного посмеялась."
    sl "Очень хорошо, что ты спросил! {w}Потому что у меня {b}есть{/b} на тебя планы!"
    me "О-о, интересно, и какие же?"
    sl "Узнаешь, когда выйдем из столовой."
    "Я многозначно посмотрел на Славю."

    show sl pioneer shy with dspr

    "Та в ответ лишь игриво улыбнулась."
    me "Заинтриговала!"

    show sl pioneer smile with dspr

    "Мы продолжили есть и мило беседовать."
    "..."

    stop ambience fadeout 1.0

    hide sl
    show bg ext_dining_hall_near_sunset
    show sl pioneer normal at right
    with dissolve1

    play ambience ambience_camp_center_evening fadein 1.0

    "Выйдя из столовой, мы взялись за руки, и пошли в сторону домиков."
    me "Так что ты хотела предложить?"

    stop music fadeout 1.0

    show bg ext_dining_hall_away_sunset
    show sl pioneer smile
    with dissolve

    play music "<from 5.0>" + music_list["eternal_longing"] fadein 1.0 volume 0.8

    sl "Я хотела тебе предложить зайти ко мне сегодня вечером…"
    th "Что?"
    me "Что?"
    "Спросил я ещё раз, только уже вслух."
    "В голове тут же начался настоящий ворох. Я перебирал десятки вариантов того, как она продолжит."

    show bg ext_square_sunset
    show sl pioneer laugh
    with dissolve

    sl "… поиграть в карты!"
    th "Ах, вот оно что."
    th "А я тут себе уже начал фантазировать."
    th "Ну ладно, в эту игру могут играть двое."
    "У меня сразу же появилась идея, как можно «подогреть» этот вечер."
    th "Хотя… Чёрт, а с Женей что делать?"

    if card_game_d2_win == True:
        me "Что, хочешь взять реванш?"
        "Усмехнулся я, вспоминая свою победу, когда мы играли все вместе на пляже."
        show sl pioneer smile2 with dspr
        "Славя улыбнулась."
        sl "Можно и так сказать."
        sl "Но в этот раз ты так легко не отделаешься, зай!"
        show bg ext_houses_sunset with dissolve
        "Она хотела сказать «знай», или назвала меня «зай»?"
        me "Хорошо. Но ты тоже теперь поцелуем в щечку не отделаешься!"
    else:
        me "Отлично, я как раз хочу взять реванш!"
        "Сказал я, вспоминая как мы играли вместе с девочками на пляже."
        show bg ext_houses_sunset
        show sl pioneer smile2
        with dissolve
        sl "Хах, думаешь, в этот раз сможешь победить?"
        "Я улыбнулся."
        me "Не сомневайся! И я обязательно потребую приз."
    
    sl "Ха-ха, хорошо!"
    "Мы посмеялись, и продолжили идти."

    stop music fadeout 2.0

    "..."
    me "Кстати, ты же вместе с Женей живешь."

    play music music_list["everyday_theme"] fadein 2.0 volume 0.8

    me "Она с нами будет играть?"

    show sl pioneer smile with dspr

    sl "Хм-м, помнишь она говорила, что у неё перед нами должок."
    sl "Вот, пришло время возвращать."
    sl "Оставит нас вдвоём, посидит в библиотеке. Ей всё равно не привыкать."
    th "Отлично, она не станет помехой."

    show bg ext_house_of_sl_sunset with dissolve

    "Мы подошли к домику Слави."
    me "Ну что, когда мне быть?"
    sl "Через полчаса примерно подходи. Подожду, пока Женя вернётся с ужина, и поговорю с ней."
    me "Отлично, тогда не прощаемся!"
    "Мы поцеловались, и разошлись."

    hide sl with long_dspr

    "Я был в предвкушении сегодняшнего вечера."
    "..."

    show bg ext_house_of_mt_sunset with dissolve1

    pause(0.5)

    play sound sfx_knock_door7_polite volume 0.9

    "Покурив в пролеске, я подошёл к своему с вожатой домику и постучал."

    pause(1.0)

    th "Хм, не отвечает."
    me "Есть кто дома? Ольга Дмитриевна, это я!"

    pause(1.0)

    "Ответа не последовало."
    th "Ушла что ли?"
    "Я открыл дверь, и зашёл в домик."

    stop ambience fadeout 1.0

    show bg int_house_of_mt_sunset with dissolve

    play ambience ambience_int_cabin_evening fadein 1.0

    "И дверь не заперта. Странно."
    "Раскидывая мозгами о том, куда же вожатая так торопилась, что даже дверь не закрыла, я решил поменять нижнее бельё, благо, второй комплект носков и трусов у меня был."
    "..."
    "Переодевшись, я налил себе стакан воды, и сел на стул."
    th "Интересно, что там на мобиле?"
    "Я достал телефон из-под подушки."
    "Заряда оставалось всего 20%%, но меня привлекло другое."
    "Почему-то было открыто приложение заметок."

    stop music fadeout 1.0

    pause(1.0)

    play music music_list["just_think"] fadein 1.0 volume 0.8

    "Я разблокировал телефон, и открыл последнюю сохранённую заметку."
    "Когда я прочёл содержимое, то обомлел."
    "В заметке была всего одно предложение:"
    "{i}Ты здесь не просто так.{/i}"
    th "Что за?.."
    "Не мог же это я написать?"
    "Вожатая, или кто-то из пионеров?"
    th "Ну да, нашли неведомое устройство, и вместо того, чтобы разбираться, написали непонятное послание, и убрали обратно?"
    "Я задумался."
    "Кажется тот тип, похожий на меня, утверждал что может «перемещаться по лагерям»."
    "Так всё, что он говорил правда, и это его рук дело?"

    stop music fadeout 2.0

    "Посидев ещё пару минут, я понял, что все равно не смогу получить никакие ответы, поэтому, просто удалил заметку и убрал телефон обратно."

    play music music_list["take_me_beautifully"] fadein 2.0 volume 0.8

    th "Пора идти к Славе."
    
    show bg ext_house_of_mt_sunset with dissolve

    "С этими мыслями я вышел из домика, и закрыл его на ключ."
    "Я решил пару минут подождать, не появиться ли Ольга Дмитриевна."
    "..."
    "Но её всё не было."
    th "Ну и ладно. {w}Думаю она не обидится, если в этот раз я уйду без спроса."
    "..."
    "Я пошёл к домику Слави."

    show bg ext_house_of_sl_sunset with dissolve

    "Уже через две минуты я был на месте."

    play sound sfx_knock_door7_polite volume 0.7

    pause(1.0)

    show sl pioneer smile2 at center
    with good_dspr

    "Я постучал в дверь, и мне открыла Славя."
    sl "Сёма, заходи!"

    stop ambience fadeout 1.0

    hide sl
    show bg int_house_of_sl_sunset
    show sl pioneer shy close at cright
    with dissolve

    play ambience ambience_int_cabin_evening fadein 1.0

    "Я зашёл, и мы заключили друг друга в долгое объятие и поцелуи."
    "Я опустил одну руку чуть ниже талии, к бедрам девушки."
    "Славя не сопротивлялась, а лишь, кажется, томно улыбнулась, как я успел увидеть, немного отведя взгляд от её лица."

    hide sl
    show sl pioneer smile at cright
    with half_good_dspr

    "Наконец, мы закончили миловаться, Славя вернулась к двери, и повернула ключ, затем сказала."
    sl "Ну что, начнём игру? Карты у меня."
    me "Давай, а где играть будем? За столом, или?.."
    sl "Давай лучше на мою кровать сядем."
    me "Давай."

    hide sl
    show sl pioneer smile at center
    with good_dspr

    "Мы сели по обе стороны от кровати, Славя достала колоду, и начала тасовать карты."
    me "На что играем?"

    show sl pioneer smile2 with dspr

    "Девушка улыбнулась."
    sl "А ты хочешь играть на что-то конкретное?"
    "Я улыбнулся, прищурив взгляд и посмотрел на неё."
    me "У меня есть идея… {w}Но не знаю, как она тебе понравится."
    "Славя с интересом посмотрела на меня."

    stop music fadeout 2.0

    sl "Ну рассказывай! Кусаться не буду, честно!"

    pause(1.0)

    play music "<from 2.0>" + music_list["heather"] fadein 1.5 volume 0.8

    me "Сыграем… {w}На раздевание?"

    show sl pioneer surprise with dspr

    "Во мгновение у меня пересохло в горле."
    "Славя, кажется, удивилась, но я сразу понял по выражению лица, что она скорее заинтригована, а не злится."

    show sl pioneer laugh with dspr

    sl "Х-м-м, какой ты проказник!"
    sl "Ладно, я за!"

    show sl pioneer smile with dspr

    "В её глазах загорелся огонёк."
    "Я улыбнулся, и обсудив правила, мы приступили к игре."

    window hide

    jump simple_happiness_mod_d6_card_game_r1


# КАРТОЧНАЯ ИГРА ДЕНЬ 6
label simple_happiness_mod_d6_card_game_r1:
    python:
        difficulty = "normal"
        CARD_GAME_WITH_EXCHANGE = True

        dialogs = {
            (0, "win", "jump"): "d6_card_game_r1_me_win",
            (0, "fail", "jump"): "d6_card_game_r1_sl_win",
            (0, "draw", "jump"): "d6_card_game_r1_draw"
        }

        generate_cards("bg int_house_of_sl_sunset", dialogs)
        rival = CardGameRivalUn(sl_avatar_set, "Славя")
    
    $ game_starts_r1 = True

    call cards_gameloop

    return


label d6_card_game_r1_sl_win:
    show bg int_house_of_sl_sunset

    $ renpy.block_rollback()
    $ game_starts_r1 = False
    $ d6_r1_winner = "sl"

    window show

    "Славя меня уделала."

    show sl pioneer laugh with dspr

    sl "Д-а-а!"
    "Восторженно крикнула она, сбросив оставшиеся карты на кровать, и улыбнулась."

    show sl pioneer smile2 with dspr

    sl "Хи-хи, давай, выполняй уговор. С тебя рубашка!"
    me "Ну а как же!"

    show sl pioneer shy with dspr

    "Я снял рубашку, и повесил её на спинку кровати."
    "Славя, кажется, немного смутилась, но в её глазах уже очень рьяно горел азарт. У меня тоже."
    me "Продолжим?"

    show sl pioneer smile with dspr

    sl "Определённо! Раздавай!"
    "Заведённые и вошедшие в азарт после первого раунда, мы продолжили игру."

    hide sl with dspr

    window hide

    jump simple_happiness_mod_d6_card_game_r2


label d6_card_game_r1_me_win:
    show bg int_house_of_sl_sunset

    $ renpy.block_rollback()
    $ game_starts_r1 = False
    $ d6_r1_winner = "me"

    window show

    th "Да, победа!"
    "Я скинул оставшиеся карты, и посмотрел на Славю."

    show sl pioneer smile2 with dspr

    sl "Вот же! Так и знала, что надо было по-другому сыграть!"
    "Улыбнувшись, я ответил."
    me "Ну, может ещё отыграешься? А пока выполняй уговор."

    show sl pioneer shy with dspr

    "Славя немного смутилась, но всё же улыбнулась в ответ, и начала снимать рубашку."
    "А я с большим удовольствием наблюдал за этим."

    pause(1.0)

    show sl skirt shy with good_dspr

    "Теперь из верха на ней остался только лифчик."

    show sl skirt smile with dspr

    sl "Ну, в следующий раз ты со своей рубашкой попрощаешься! {w}Давай, раздавай!"
    "Кажется в Славе окончательно разгорелся азарт."
    me "Это мы ещё посмотрим!"
    "Мы посмеялись, и я начал раздавать карты."

    hide sl with dspr

    window hide

    jump simple_happiness_mod_d6_card_game_r2


label d6_card_game_r1_draw:
    show bg int_house_of_sl_sunset

    $ renpy.block_rollback()
    $ game_starts_r1 = False
    $ d6_r1_winner = "both"

    window show

    me "Вот те раз, с первого раунда и ничья!"
    sl "А может так даже и лучше! {w}Ну что, как договаривались?"
    me "Обижаешь!"

    pause(1.0)

    show sl skirt shy with good_dspr

    "Мы одновременно начали снимать свои рубашки."
    "Пока я расстегивал пуговицы, и снимал рукава, то постоянно смотрел на Славю."
    "Всё же у неё было интереснее."
    "Она, кажется, тоже поглядывала на меня."

    show sl skirt smile with dspr

    "Оба немного смущённые, но уже разгоряченные обстановкой и первым раундом игры, мы тут же решили продолжить играть дальше."
    "У нас обоих горел азарт в глазах в перемешку с возбуждением."
    "Я раздал карты, и начался второй раунд."

    hide sl with dspr

    window hide

    jump simple_happiness_mod_d6_card_game_r2


label simple_happiness_mod_d6_card_game_r2:
    python:
        difficulty = "normal"
        CARD_GAME_WITH_EXCHANGE = True

        dialogs = {
            (0, "win", "jump"): "d6_card_game_r2_me_win",
            (0, "fail", "jump"): "d6_card_game_r2_sl_win",
            (0, "draw", "jump"): "d6_card_game_r2_draw"
        }

        generate_cards("bg int_house_of_sl_sunset", dialogs)
        rival = CardGameRivalUn(sl_avatar_set, "Славя")
    
    $ game_starts_r2 = True

    call cards_gameloop

    return


label d6_card_game_r2_sl_win:
    show bg int_house_of_sl_sunset

    $ renpy.block_rollback()
    $ game_starts_r2 = False

    window show

    if d6_r1_winner == "sl":
        show sl pioneer laugh at center
        with good_dspr

        sl "Ура, снова победа!"
        th "Да как же так-то!?"
        "Не сказать, что я был зол, или раздосадован, просто не мог поверить в происходящее."
        "Славя выигрывает уже второй раз подряд!"

        show sl pioneer smile2 with dspr

        me "Вот ты блин! Ну, в следующем раунде тебе точно не поздоровится!"
        "Я начал снимать шорты."
        "Славя сначала смотрела на меня, а потом сказала."

        show sl pioneer smile with dspr

        sl "Знаешь, чтобы тебе было проще… {w}Так и быть."
        "Я сел обратно на кровать, раздетый уже до трусов, и увидел как Славя снимает рубашку."

        show sl skirt smile with dspr

        th "Так, а вот это плохо. На такой исход я не рассчитывал, а мой боец на посту может проснуться."
        "Славя сняла рубашку, и сказала."
        sl "Я думаю, тебе так спокойнее будет, верно?"
        "Она осмотрела меня."
        sl "И приятнее."
        "Мы оба посмеялись, и Славя собрала карты и начала их тасовать, сейчас был её черёд раздавать."
        "Я был очень приятно удивлён тому, что несмотря на небольшое стеснение и лёгкий мандраж, между нами не было неловкости даже в такой ситуации."
        "Наконец, мы начали играть третий раунд."
    
    elif d6_r1_winner == "me":
        show sl skirt smile at center
        with good_dspr

        "В этот раз выиграла Славя."
        sl "Ну что, теперь твой черёд, давай!"
        sl "Я уже не могу дождаться, когда эта рубашка слетит с тебя!"
        "Я посмеялся, и ответил."
        me "Конечно-конечно, сейчас!"
        "Я начал снимать рубашку, и подумал, что на мой взгляд последняя фраза Слави прозвучала очень эротично, если не сказать возбуждающе."
        "Что могло стать… Проблемой? Мой боец был готов вот-вот проснуться."
        "Я сняла рубашку полностью, и повесила её на спинку кровати."
        "А Славя, с большим интересом рассматривая меня, сказала."
        sl "Ну что, готов играть третий раунд?"
        me "Готов! И в этот раз я выиграю, будь уверена!"
        "Славя улыбнулась, и сказала."
        sl "Ну это мы ещё посмотрим!"
        "Славя раздала карты, и мы начали играть."
    
    elif d6_r1_winner == "both":
        show sl skirt smile at center
        with good_dspr

        "В этот раз победу одержала Славя."
        sl "Ура-а!"
        "Славя посмотрела на меня, и сказала."
        sl "А ну ка! Штаны на базу!"
        "Я встал, и начал расстёгивать ремень."
        me "Ничего себе, как смело!"

        show sl skirt shy with dspr

        "Славя в ответ лишь хихикнула."
        "Пока я стягивал штаны, я явно чувствовал напряжение ниже пояса."
        "Славя точно этого не могла не замечать, но не комментировала, а лишь осматривала меня."
        "Я заметил это, и спросил."

        show sl skirt smile with dspr

        me "Ну, как я выгляжу?"
        sl "Прекрасно! Как здорово, что ты достался мне."
        "Я умилился этим словам, сел обратно на кровать, и Славя начала тасовать карты."
        "Оставался третий раунд."

    window hide

    jump simple_happiness_mod_d6_after_card_game


label d6_card_game_r2_me_win:
    show bg int_house_of_sl_sunset

    $ renpy.block_rollback()
    $ game_starts_r2 = False

    window show

    if d6_r1_winner == "sl":
        show sl pioneer smile at center
        with good_dspr

        "В этот раз я выиграл."
        me "Ну что, теперь твой черёд, давай!"
        sl "Хи-хи, что не можешь дождаться, когда уже эта рубашка слетит с меня?"
        "Славя начала снимать рубашку, и я подумал что на мой взгляд последняя фраза прозвучала очень эротично, если не сказать возбуждающе."
        "Что могло стать… Проблемой? Мой боец был готов вот-вот проснуться."

        show sl skirt smile with dspr

        "Славя сняла рубашку полностью, и повесила её на спинку кровати."
        "А я, с большим интересом рассматривая её, сказал."
        me "Ну что, готова играть третий раунд?"
        "Славя улыбнулась, и сказала."
        sl "Готова! И в этот раз я выиграю, будь уверен!"
        me "Ну это мы ещё посмотрим!"
        "Славя раздала карты, и мы начали играть."
    
    elif d6_r1_winner == "me":
        show sl skirt smile at center
        with good_dspr

        th "Я опять выиграл! Да мне сегодня прёт!"
        "Славя, которая не могла не заметить мою радость в глазах, посмеялась, и спросила."
        sl "Хи-хи, Сёма, скажи честно, ты тренировался играть, да?"
        "После этих слов она встала с кровати, и начала снимать юбку."
        "Решив, что так дело не пойдет, я начал снимать рубашку, и ответил."
        me "Ни в коем случае! Выигрываю абсолютно честно!"

        show sl swim shy with dspr

        sl "Ой, Сём, ты зачем это?"
        "Славя увидела, как я вешаю рубашку на спинку кровати."
        "И непонятно, чем она была смущена больше, тем что осталась в одном нижнем белье, или тем, что я проявил инициативу."
        me "Мне кажется, так будет правильнее."
        "Я улыбнулся."

        show sl swim smile2 with dspr

        sl "Вполне… Мне все нравится!"
        "Она запрыгнула обратно на кровать, и начала тасовать карты для третьего раунда."
        "В это время я смотрел на неё."
        "Передо мной сидела, в одном нижнем белье, девушка, в которую я был влюблён."
        "Сердце было готово выскочить из груди, а мой боец уже начал просыпаться."
        "Наконец, Славя перемешала и раздала карты, и мы начали играть третий раунд."
    
    elif d6_r1_winner == "both":
        show sl skirt smile at center
        with good_dspr

        "В этот раз я победил."
        "Мы уже оба сидели без верха, но теперь черёд снимать следующий элемент одежды достался Славе."
        me "Во-от! Так мне больше нравится!"
        "Гордо заявил я, и откинулся на стену рядом с кроватью."
        sl "Хи-хи, нравится ему!"
        "Посмотрим, как тебе понравится следующий раунд!"
        "После этих слов она встала с кровати, и начала снимать юбку."
        "Я смотрел на неё, как завороженный."

        show sl swim smile2 with dspr

        "Славя обратила на это внимание, и полностью сняв юбку, спросила."
        sl "Сём… Ты так смотришь… Я правда такая красивая?"
        me "Конечно! И не смей сомневаться в обратном!"

        show sl swim shy with dspr

        "Славя явно смутилась от комплимента, и запрыгнув обратно на кровать, сказала."
        sl "Ну что, финальный раунд?"
        me "Раздавай!"
        "Славя перетасовала карты, раздала их, и мы начали играть."

    window hide

    jump simple_happiness_mod_d6_after_card_game


label d6_card_game_r2_draw:
    show bg int_house_of_sl_sunset

    $ renpy.block_rollback()
    $ game_starts_r2 = False

    window show

    if d6_r1_winner == "sl":
        show sl pioneer smile at center
        with dspr

        "В этот раз мы сыграли в ничью."
        me "Ну что, давай как договаривались?"
        sl "Ну конечно!"
        "Славя начала снимать рубашку, а я встал, и проделывал тоже самое с шортами."

        show sl skirt smile with dspr

        "Так как ей разобраться со своей одеждой было быстрее, она уже сидела в одном лифчике, и с интересом смотрела на меня."

        show sl skirt shy with dspr

        "Закончив, я остался в одних трусах, и поймал на себе интересующийся, но при этом слегка застенчивый взгляд Слави."
        "Я улыбнулся, посмотрев на неё, и сел обратно на кровать."
        me "Интересно, что будет в третьем раунде?"
        sl "Конечно, давай я раздам!"
        "Сейчас была очередь Слави, поэтому она собрала карты, перетасовала их, и мы начали играть третий раунд."

        jump simple_happiness_mod_d6_after_card_game
    
    elif d6_r1_winner == "me":
        show sl skirt smile at center
        with dspr

        "Второй раунд мы сыграли вничью."
        me "Вот те раз. Ну что, тогда как договаривались!"
        sl "Да, хорошо."

        show sl swim smile2 with dspr

        "Мне то было проще, я снял всего рубашку. А Славя осталась уже в одном нижнем белье."
        "Я смотрел на неё жадными глазами, а мой боец начал просыпаться."
        "Славя прыгнула обратно на кровать, и начала тасовать карты."
        sl "Ну что, играем третий раунд?"
        me "Конечно! Интересно же, как он закончится."

        show sl swim smile with dspr

        "Славя стрельнула глазками, и улыбнувшись, ответила."
        sl "А то!"
        "Она раздала карты, и мы начали играть третий раунд."
    
    elif d6_r1_winner == "both":
        show sl skirt smile at center
        with dspr

        "Вот так-так, а это уже интересно!"
        sl "Ого, второй раз подряд вничью вышли!"
        me "Ага…"
        "Я улыбнулся."
        me "Как специально, слушай!"
        sl "Как бы там ни было…"
        "Она встала с кровати."
        sl "Уговор есть уговор."
        "После этих слов она начала расстёгивать ремень, и снимать юбку."
        "Я последовал её примеру."

        show sl swim shy with dspr

        "Уже скоро мы оба стояли в одном лишь нижнем белье."
        "Мы оба были немного смущены, и я спросил."
        me "Ты когда-нибудь могла подумать, что в лагере с тобой произойдёт нечто подобное."

        show sl swim smile2 with dspr

        sl "Нет. Но я рада что произошло. И именно с тобой."

        hide sl
        show sl swim smile2 close at cright
        with good_dspr

        "Она сделала пару шагов ко мне."
        sl "Потому что я люблю тебя. И полностью тебе доверяю."
        "Я приобнял её за талию, и мы поцеловались."
        "Одна её рука была у меня на плече, а вторая водила по животу, следуя рельефу небольшого пресса, но ниже не опускалась."
        "..."

        hide sl
        show sl swim smile at center
        with good_dspr

        "Вскоре, мы вернулись обратно на кровать."
        "Славя взяла карты, и начала тасовать их. Нас ждал третий раунд."
    
    window hide

    jump simple_happiness_mod_d6_after_card_game


label simple_happiness_mod_d6_after_card_game:
    show bg int_house_of_sl_sunset

    $ renpy.block_rollback()
    $ renpy.pause(2.0, hard=True)

    stop music fadeout 3.0

    show black with clocks_in

    play music music_list["forest_maiden"] fadein 3.0 volume 0.93

    hide black with clocks_out

    "Примерно на половине игры, я понял что уже вообще не могу следить за картами."
    "Я весь пылал, и у меня тряслись руки."
    sl "Семён…"
    "Я обошел кровать сбоку, и сел рядом со Славей, положив руку ей на бедро."

    show blink

    "Уже через секунду мы слились в страстном поцелуе."

    hide sl

    "Я начал расстёгивать лифчик Слави, и через несколько секунд, он упал мне на колени."
    "Я отбросил его, и повалил девушку на кровать."

    show cg d6_sl_hentai_2
    hide blink
    show unblink

    "Мы лежали на кровати, и обменивались ласками."
    "Я нежно касался руками груди девушки, целуя её в шею, и покусывая за мочку уха."
    "..."
    "Она томно и горячо дышала, становясь всё смелее, опуская руку всё ниже и ниже."
    "..."
    "Я легонько провел пальцем по всему телу Слави, и коснулся пальцами её трусиков."
    "Она издала громкий вздох напополам со стоном, и немного поджала ноги."
    "..."
    "Мы оба пылали страстью."
    "Я уже забыл какого это, быть настолько близко с девушкой."
    "Голова кружилась, разум был готов вот-вот затуманиться, но я держал себя в руках, не позволяя лишнего."
    "..."
    "Вскоре, Славя шепнула мне на ушко."
    sl "{i}Сём… Сёма!{/i}"
    "Я с трудом отстранился от её объятий и прикосновений, облокотился на руку, и посмотрел на неё."

    window hide

    call set_time("night")

    hide cg
    show bg int_house_of_sl_night
    show sl naked tender close at cright
    with dissolve1

    window show

    sl "Сёма, если ты не против, то… давай не сегодня?"
    sl "Женя уже скоро должна прийти."
    "Я кивнул, и поцеловав её руку, ответил."
    me "Ну конечно. Я же говорил, когда ты будешь готова."
    "Славя улыбнулась мне, и мы ещё на несколько мгновений слились в поцелуе, после чего, настала пора нам собираться."
    "..."

    hide sl
    show sl pioneer smile at right
    with good_dspr

    stop music fadeout 5.0

    "Как не было бы грустно прерывать этот вечер, но мы оделись, собрали карты, которые разбросали по всему полу, пока валялись на кровати, после чего Славя сказала."

    play music music_list["what_do_you_think_of_me"] volume 0.8 fadein 2.0

    sl "Давай на улицу выйдем, там попрощаемся? Я хочу немного свежим воздухом подышать."
    me "Конечно!"

    show bg ext_house_of_sl_night with dissolve

    "Славя отперла дверь, и мы вышли на улицу."
    "Вечернее тепло уже спало, и вне стен домика было по-настоящему свежо."
    "А лунный свет вкупе с горящими лампой и светильником создавал поистине чудесную картинку."

    hide sl
    show sl pioneer tender close at center
    with good_dspr

    "Славя взяла меня за руки, посмотрела мне в глаза, и сказала."
    sl "Сёма, спасибо тебе большое за этот прекрасный вечер."
    sl "Я ещё никогда не чувствовала себя… {w}Так. Любимой, желанной. Страстной."

    show sl pioneer shy with dspr

    "Я улыбнулся, и ответил."
    me "Это тебе спасибо. Ты позвала, и сама организовала нам вечер вдвоём. Без твоей инициативы такой близости бы не было."
    "Я секунду подумал, и добавил."
    me "Я надеюсь, ты не обижаешься, что я был немного настойчив?"

    show sl pioneer smile2 with dspr

    sl "Нет, что ты, ни в коем случае."
    sl "Я бы и сама хотела большего. Смена скоро закончится, мы разъедемся…"

    show sl pioneer sad with good_dspr

    sl "Кто знает, увидимся ли мы ещё когда-нибудь?"

    hide sl
    show sl pioneer tender close at cright
    with long_dspr

    "Славя обняла меня и положила голову мне на плечо."
    "Я обнял её в ответ."
    th "Ох, как бы я сам хотел знать, что случится после смены…"
    me "Я надеюсь, у нас всё получится."
    "Славя ничего не ответила, а лишь крепче прижалась ко мне."

    pause(1.0)

    "..."

    show sl pioneer smile2 with dspr

    "Так, мы простояли ещё некоторое время, после чего подарили дуг другу последний на сегодня поцелуй."

    hide sl
    show sl pioneer smile2 far at center
    with long_dspr

    "Славя поднялась по ступенькам, и помахав друг другу на прощание, она зашла в домик..."

    hide sl with half_good_dspr

    "..."
    "А я простояв в улыбке с полминуты, пошел к нашему с вожатой домику."

    show bg ext_house_of_mt_night_without_light with dissolve1

    pause(1.0)

    call smoking_process(with_pause=1.5)

    "Я сидел за нашим с вожатой домиком, курил."
    "И не знал, что мне делать. Какая эмоция сейчас передо мной главенствующая?"
    "Воздушная, лёгкая, как пуховая подушка, любовь, в которую хотелось окунуться?"
    "Сладкая, терпкая, молодая, дерзкая и возбуждающая романтика?"
    "..."
    "Или страх? Холодный, пустой, странный… {w}Как и вся моя жизнь до того, как я встретил эту девушку, и вообще попал в этот лагерь?"
    "Страх пропасть отсюда, как будто бы меня тут и не было никогда? {w}Потерять весь этот лагерь навсегда?"
    "Потерять Славю?"
    "..."
    
    play sound sfx_smoking_cigaret

    "Я не знал, что случиться дальше. Но о последнем варианте даже думать не хотелось."
    "Я старался откинуть его как можно дальше. В любом случае от меня ничего не зависит."
    "Сейчас я мог только наслаждаться приятными чувствами, оставленными вечером, проведённым в компании девушки, которую я полюбил здесь."

    pause(1.0)

    show bg int_house_of_mt_night2 with dissolve

    "Докурив, я зашёл в домик, открыв дверь своим ключом, и не обнаружил вожатую."
    "Почему-то, я даже не удивился этому факту."
    "Поэтому, решив лишний раз не терзать себя вопросами, я разделся, и лёг в постель, и довольно быстро начал засыпать…"

    stop music fadeout 2.0

    "… засыпать, смакуя в голове, и прокручивая всё произошедшее за эти дни, и за сегодняшний вечер…"

    window hide

    stop ambience fadeout 1.0

    show blink

    $ renpy.pause(3.5, hard=True)

    jump simple_happiness_mod_day7


# День 7
label simple_happiness_mod_day7:
    $ renpy.block_rollback()
    $ backdrop = "days"
    $ new_chapter(7, u"Простое Счастье. День 7")

    call set_time

    $ set_mode_adv()

    play ambience ambience_int_cabin_day fadein 3.0 volume 0.9

    window show

    "Сон мой был, мягко говоря, откровенный."
    "Сказывалось всё произошедшее вчера."

    show bg int_house_of_mt_day
    hide blink
    show unblink

    play music music_list["dance_of_fireflies"] fadein 2.0 volume 0.7

    "Я открыл глаза, сладко потянулся, и подумал."

    hide unblink

    th "Надо же, ведь перед нами не было ни капли стеснения."
    mt "О чём мечтаешь?"

    show mt pioneer smile at right
    with dspr

    "От неожиданности я немного вздрогнул, и посмотрел на вожатую. Она уже была одета в пионерскую форму."
    me "Утро доброе, Ольга Дмитриевна! А я вас вчера вечером так и не дождался, вы где пропадали?"

    show mt pioneer grin with dspr

    mt "Ой, да прям ждал он, так и поверила."
    mt "Сам то небось уже в двенадцатом часу вернулся?"
    me "Ну-у…"

    show mt pioneer smile with dspr

    mt "Вот именно."
    mt "А я занята была немножко, у Ви… {w}Э, ну, пионеру плохо стало, вот."
    "Она немного замялась."
    mt "Виола его осматривала."
    th "С каждым разом всё интереснее и интереснее."
    me "Понятно. Ну, главное что всё хорошо."
    "После этих слов я поднялся с кровати, и начал готовиться к завтраку."
    "..."

    hide mt
    show mt pioneer normal at fright
    with good_dspr

    "Одевшись и умывшись, я спросил у вожатой."
    me "Ольга Дмитриевна, вы идёте?"

    show mt pioneer sad with dspr

    mt "Ты иди, я позже подойду. Всё равно линейки нет, а у меня живот крутит."
    me "Хорошо."

    stop ambience fadeout 1.0

    hide mt
    show bg ext_house_of_mt_day
    with dissolve

    play ambience ambience_camp_center_day fadein 1.0

    "Стоило мне выйти из домика, и закрыть дверь, как я увидел подходящую Славю."

    show sl pioneer smile2 at cright
    with half_good_dspr

    "Я быстро спустился по ступенькам, мы обнялись и поцеловались."
    sl "Сёма, сегодня после ужина… Нет, после обеда! Ты весь мой!"
    me "Ха-ха, Славя, в чём дело? Ты опять что-то придумала?"
    sl "Да. Тебе точно понравится! Пойдём завтракать, я тебе по дороге расскажу."
    me "Пойдём."

    hide sl
    show sl pioneer smile at right
    show bg ext_houses_day
    with dissolve

    "Пока мы шли, Славя рассказала мне, что вчера вечером, пока мы сидели у неё, Женя, от нечего делать, лазила в библиотеке по закоулкам."
    "И нашла в одном из таких походный спальник. Двухместный."

    stop music fadeout 2.0

    show bg ext_square_day with dissolve

    play music music_list["forest_maiden"] fadein 2.0 volume 0.95

    "Я уже понял, к чему она клонит."
    me "Ты хочешь, чтобы мы ушли с тобой подальше от всех?"
    sl "Да… {w}А переночевать я предлагаю прямо в лесу, в спальнике. Отъезд только днём, так что вернуться точно успеем."

    hide sl
    show sl pioneer smile2 close at cright
    with good_dspr

    "Идя по площади, мы свернули с протоптанной дорожки немного в сторону, к деревьям, и Славя продолжила."

    show sl pioneer shy close
    with dspr

    sl "Сём… {w}Я очень хочу провести там ночь. {w}С тобой…"
    "У меня перехватило дыхание. Ведь Славя говорила не просто о чувствах, не просто о вчерашних, хоть и эротических, но по большей части, играх."
    "Она была готова доверить мне… Себя."
    
    hide sl
    show sl pioneer shy close at center
    with dspr

    "Я взял девушку за руки."
    me "Славя."
    me "Я только за. Но я не хочу, чтобы ты чувствовала себя обязанной."
    sl "Всё хорошо."

    show sl pioneer smile2 close with dspr

    sl "Ведь ты сам говорил, что не будешь торопиться, пока я не буду готова."
    sl "Я готова. Вчера я это поняла."
    "Ну вот и всё, она окончательно овладела моим сердцем."
    "У меня пропали всякие сомнения. Теперь я точно её не отпущу."

    show sl pioneer tender close with dspr

    me "Я люблю тебя."
    sl "И я тебя."

    show sl pioneer smile2 close with dspr

    "Мы украдкой поцеловались, и пошли дальше в сторону столовой."

    stop music fadeout 3.0

    hide sl
    show bg ext_dining_hall_away_day
    show sl pioneer surprise at right
    with dissolve1

    pause(1.0)

    play music music_list["she_is_kind"] fadein 2.0 volume 0.83

    "Подойдя к столовой, мы поняли, что немного задержались, так как подходящих пионеров уже не было."
    "Ускорив шаг, мы почти забежали в столовую."

    stop ambience fadeout 1.0

    hide sl
    show bg int_dining_hall_people_day
    show sl pioneer smile at right
    with dissolve

    play ambience ambience_dining_hall_full fadein 1.0

    "Так и оказалось."
    "Внутри уже всё было забито, так что, получив завтрак, нам ничего не оставалось, кроме как приткнуться к единственному свободному столику, за которым сидела Ульяна, и ещё какая-то пионерка."

    stop music fadeout 2.0

    hide sl
    show us sport normal at center
    show sl pioneer smile at left
    with dissolve

    play music music_list["i_want_to_play"] fadein 1.5 volume 0.8

    "Сев, мы пожелали друг другу приятного аппетита, и я поздоровался с Ульяной."
    me "Здрав буди, мелочь!"

    show us sport calml with dspr

    us "Ещё один! Да не маленькая я!"
    me "Та я ж любя!"

    show kt normal at fright
    with good_dspr

    kt "Ой, кстати, ребята, привет!"
    "Я повернулся."
    "Пионеркой, которую я сначала не признал, оказалась Катя, которая слушала наше выступлении."

    show us sport normal
    show sl pioneer smile2
    with half_good_dspr

    sl "Привет."
    sl "Э-э-э, Катя, правильно?"
    kt "Правильно."
    
    show sl pioneer smile with dspr

    me "А я тебя и не признал сначала."

    show kt smile with dspr

    kt "Да ничего."
    "Мы немного поговорили, после чего Ульяна обратилась к Славе."

    show us sport smile
    show kt normal
    with dspr

    us "Кстати, Славя, а где ты всё пропадаешь?"
    us "Как хахаля своего нашла, так и не вижу тебя."

    show sl pioneer shy with dspr

    "Славя немного смутилась."
    sl "Да там же, где и всегда. Везде то есть."

    show sl pioneer smile2 with dspr

    sl "А вечерами мы с Семёном просто гуляем."
    "Мы со Славей переглянулись."

    show us sport surp1 with dspr

    us "Ой, а где гуляете? Скажите а, может я тоже туда кого приглашу!"

    show sl pioneer laugh with dspr

    "Мы со Славей немного рассмеялись."
    sl "Хах, Ульяна, ну нам же не нужно какое-то конкретное место. Где придётся, там и проводим время вместе."
    me "И вообще, будешь много знать, быстро состаришься."

    show us sport dontlike
    show sl pioneer smile2
    with dspr

    "Ульяна показала язык, и кажется, что-то пробормотала."
    kt "А вы... Встречаетесь?"
    sl "Да. Но мы тут познакомились, в лагере."
    "Я подтвердил."

    show kt smile with dspr

    kt "Ой, здорово!"
    kt "Знаете, я почему-то так и подумала, когда только вас вместе увидела."
    "Мы поговорили за остатками завтрака ещё немного."
    "Ульяна ещё пару раз пыталась что-то расспрашивать у Слави, но вскоре потеряла к нам интерес."

    stop ambience fadeout 1.0
    stop music fadeout 2.0

    hide us
    hide sl
    hide kt
    show bg ext_dining_hall_near_day
    show sl pioneer smile at right
    with dissolve1

    play ambience ambience_camp_center_day fadein 1.0

    "Выйдя из столовой, я спросил у Слави."

    play music music_list["so_good_to_be_careless"] fadein 2.0 volume 0.8

    me "Сегодня же, я так понимаю, хозяйственный день?"
    
    show sl pioneer smile2 with dspr

    sl "Да. Убираемся в домиках, в клубах… Ну обычно до обеда всё успеваем."
    
    show sl pioneer laugh with dspr

    sl "А мы с тобой должны успеть Сёма, обязаны!"
    "Я улыбнулся."
    me "Тогда не будем терять времени?"

    show sl pioneer smile2 with dspr

    sl "До встречи на обеде?"
    me "Жду с нетерпением!"
    "Мы попрощались, приобнявшись, но целоваться не стали. Слишком много было посторонних глаз вокруг."
    "..."

    hide sl
    show bg ext_dining_hall_away_day
    with dissolve

    "Воодушевлённый сегодняшним романтическим вечером, я направился к зданию музыкального клуба."
    "..."

    show bg ext_musclub_day
    show dv pioneer2 normal far at cleft
    with dissolve

    "Подходя к клубу, я пересёкся с Алисой."
    me "Привет!"

    hide dv
    show dv pioneer2 normal at cleft
    with long_dspr

    "Я подошёл ближе."
    me "А ты чего тут?"
    dv "Привет, да вот, убраться пришла помочь. Я всё-таки вместе с вами играла."
    dv "А мелкую одну в домике оставила убираться. Пусть будет ей в наказание за тот случай."
    me "Вот оно как, ну здорово, что пришла помочь. Вчетвером то мы тут за полчаса управимся."

    show dv pioneer2 smile with dspr

    dv "Да, только покурим для начала."
    me "Всенепременно!"
    "Мы раскурили с Алисой по сигарете, и зашли в клуб."

    stop ambience fadeout 1.0

    show cg d5_mi with dissolve

    play ambience ambience_music_club_day fadein 1.0

    mi "Ой, Семён, а вот и… {w}Алиса?"
    dv "Я тоже пришла! Я ж всё-таки у вас тут торчала, играла с вами. Нехорошо будет уборку на вас оставить."
    dv "Кстати, а где Лена?"

    hide cg
    show bg int_musclub_mattresses_day
    show mi pioneer smile at cright
    with dissolve

    un "Я тут!"

    show un pioneer smile at fleft
    with good_dspr

    "Лена вышла из подсобки с ведром с водой, и Мику весело огласила."

    show mi pioneer grin with dspr

    mi "Ну, берегись, клуб! Теперь ты будешь сиять!"

    hide mi
    hide un
    hide dv
    with good_dspr

    call to_nvl_mode

    "Мы принялись за уборку."
    "Сейчас дело шло конечно быстрее, чем в понедельник, когда мы убирались с Мику вдвоём."
    "Не представляю, как она это всё вообще в одного делала."
    me_n "А кстати, почему мы в понедельник то убирались, если хозяйственный день в субботу?"
    mi_n "Так я не успевала совсем, пока одна была, вот и приходилось часть в субботу делать, часть на понедельник оставлять."
    ths "И правда что."
    "..."
    "Уже через час всё здание музыкального клуба от потолка до пола сияло и пахло чистотой."

    call to_adv_mode

    pause(1.0)

    show un pioneer normal at left
    show dv pioneer2 smile at right
    show mi pioneer normal at center
    with long_dspr

    show dv pioneer2 smile with dspr

    dv "Ну что, может по чаю?"

    show mi pioneer smile with dspr

    mi "Конечно, можно! Мы заслужили."
    "Мы все единогласно на этом сошлись, и я с Мику отправились делать на всех чай."
    "..."

    hide un
    hide mi
    hide dv
    show un pioneer normal at left
    show dv pioneer2 smile at fright
    show mi pioneer normal at cright
    with long_dspr

    "Когда мы уже сидели на диване и наслаждались чаем, Мику вдруг спросила."

    show mi pioneer grin with dspr

    mi "Сём, а Сём! {w}Расскажи, как у тебя со Славей!"
    "Я немного округлил глаза."

    show dv pioneer2 laugh with dspr

    dv "Да чё ты, все свои."

    show un pioneer smile with dspr

    un "Да, всем было бы интересно послушать… {w}Но мы не настаиваем, конечно."
    me "Да что рассказывать…"

    show dv pioneer2 smile
    show mi pioneer happy
    with good_dspr

    "В конечном итоге я кратко рассказал девочкам всю историю наших со Славей отношений."
    "От первого моего дня, когда она мне помогала освоиться, до первого танца и поцелуя."
    "От вечерних прогулок, до вчерашней игры в карты."
    "Интимные подробности, я конечно, опускал."

    show un pioneer cry_smile with dspr

    un "Здорово…"
    "Мечтательно сказала Лена, когда я закончил рассказ."

    show dv pioneer2 laugh with dspr

    dv "Хм, знаешь, а ты мне сначала не понравился."
    "Поставила свой вердикт Алиса."

    show mi pioneer cry_smile with dspr

    mi "Сёма, да ты просто идеальный парень. Ещё и на гитаре ей хочешь сыграть. Кстати!"

    show un pioneer smile
    show dv pioneer2 smile
    with dspr

    me "Кстати да, блин, чуть не забыл!"
    
    show un pioneer shy with dspr

    un "Ой, заговорили мы тебя, кажется."

    show mi pioneer smile with dspr

    mi "Да вообще-то ничего, у Сёмы уже почти идеально получается. Только надо пару раз ещё прогнать."

    show un pioneer smile with dspr

    dv "Ну, наша помощь тут ни к чему."
    dv "Пойдём, Лена. Не будем им мешать."
    un "Да… {w}Мику, я в домике пока сама начну убираться тогда."
    
    show mi pioneer happy with dspr

    mi "Да, Леночка, хорошо-хорошо, ты сильно не торопись, успеем!"
    "Я встал с дивана, собрал все чашки, и перед тем как идти в подсобку, сказал."
    me "Пока, девочки!"

    show un pioneer smile at walk_away_left
    show dv pioneer2 smile at walk_away_left
    pause(1.0)
    hide un
    hide dv
    with dspr

    "Лена и Алиса попрощались, и вышли из здания."
    "А я отнес чашки, и вернувшись, взял гитару в руки, и сел рядом с Мику."

    hide mi
    show mi pioneer smile at right
    with good_dspr

    "Мы с Мику несколько раз повторили композицию, которую уже сегодня я буду играть Славе."
    mi "Отлично, Семён. Давай теперь последний раз полностью."
    "Я выдохнул, и начал играть."

    window hide

    pause(2.0)

    window show

    "Получилось идеально, и без ошибок."

    show mi pioneer cry_smile with dspr

    mi "Я горжусь тобой! Ты мой лучший ученик!"
    "Я улыбнулся."
    me "Легко быть лучшим, когда ты единственный."

    show mi pioneer happy with dspr

    mi "Неважно!"
    mi "Важно, что Славе понравится, я уверена."

    show mi pioneer smile with dspr

    mi "Так… {w}Ты гитару когда забираешь?"
    me "Ну-у, сегодня после обеда."
    mi "Хорошо, тогда я дверь закрывать не буду. Зайдешь, возьмёшь."
    mi "Только поаккуратнее с ней!"

    show mi pioneer grin with dspr

    mi "Ну, и со Славей тоже."
    "Мику интересно улыбнулась."
    me "Что, ха-ха, что ты имеешь в виду?"

    show mi pioneer smile with dspr

    mi "То самое."

    hide mi
    show mi pioneer smile at cright
    with dspr

    mi "А теперь пойдем, нам надо ещё в домиках до обеда убраться."
    me "Да. Меня вожатая, наверное, убьёт. Пойдём скорее."

    stop ambience fadeout 1.0
    stop music fadeout 2.0

    hide mi
    show bg ext_musclub_day
    show mi pioneer normal at left
    with dissolve

    play ambience ambience_camp_center_day fadein 1.0

    "Мы с Мику вышли из здания музыкального клуба, и поспешили в сторону домиков."

    play music music_list["everyday_theme"] fadein 2.0 volume 0.82

    show black with clocks_in

    hide mi
    show bg ext_houses_day
    hide black
    with clocks_out

    "Мы разошлись с ней на развилке, она пошла к Лене в их домик, а я к себе."

    show bg ext_house_of_mt_day
    show mt pioneer normal at center
    with dissolve

    "Когда я подошёл к домику, то увидел вожатую, которая выносила ведро с водой."
    mt "Семён, наконец-то. Убрались в клубе?"
    "Я ответил, утвердительно, и вожатая продолжила."
    mt "Отлично, тогда принимаемся за наше жилище. Я уже начала, так что до обеда управимся."
    mt "Сейчас самое сложное будет, надо всё двигать…"
    me "Всё сделаем, Ольг- Дмитр-на!"

    stop ambience fadeout 1.0

    hide mt
    show bg int_house_of_mt_day
    with dissolve

    play ambience ambience_int_cabin_day fadein 1.0

    "Мы с вожатой продолжили уборку вместе."
    "Отодвинули кровати, тумбочки, и даже шкаф."
    "Отовсюду всё вымели, вытерли, убрали грязные вещи, и навели на полках порядок."

    show bg int_house_of_mt_clean_day with dissolve1

    pause(2.0)

    "Вскоре, наш домик прямо-таки засиял чистотой."
    "Вожатая подошла ко мне, и сказала, также как и я осматривая плоды наших стараний."

    show mt pioneer smile at right
    with good_dspr

    mt "Ну вот, другое дело!"

    play sound sfx_dinner_horn_processed volume 0.5

    "Не успела закончить она, как прозвучал горн."
    mt "Ну вот, хорошо потрудились, теперь можно хорошо покушать!"
    "Я согласился, и мы направились в столовую."

    stop ambience fadeout 1.0

    show black with clocks_in

    play ambience ambience_camp_center_day fadein 1.0

    hide mt
    show bg ext_dining_hall_away_day
    show mt pioneer normal at left
    show sl pioneer normal far at cright
    hide black
    with clocks_out

    "Подходя к столовой, мы увидели Славю, которая ждала у крыльца."
    "Заприметив нас, она начала приближаться."

    hide sl
    show sl pioneer normal at right
    with good_dspr

    mt "Славя, привет ещё раз. Как в столовой?"

    show sl pioneer smile with dspr

    sl "Отлично, Ольга Дмитриевна, кухня сияет!"
    mt "Домик?"
    sl "Обижаете!"

    show mt pioneer smile with dspr

    mt "Ну хорошо. Идёмте есть?"

    hide mt
    show mt pioneer smile at cleft
    with dspr

    pause(0.33)

    hide sl
    show sl pioneer smile at cright
    with dspr

    "Вожатая уже было хотела сделать шаг, как Славя её прервала, сказав."
    sl "Стойте, Ольга Дмитриевна!"

    show mt pioneer surprise with dspr

    "Она посмотрела на Славю, и спросила."
    mt "Что такое?"
    sl "Давайте немножко отойдём."
    "Я понял, что она хочет сделать, а точнее спросить, поэтому посмотрел на Славю, и кивнул."

    hide mt
    hide sl
    show mt pioneer normal at cright
    show sl pioneer normal at fright
    with good_dspr

    "Вместе мы отошли в сторонку от тропинки."
    mt "Славя, что случилось?"

    show sl pioneer smile with dspr

    sl "Ольга Дмитриевна, …"
    "Славя рассказала вожатой про то, что мы хотим сегодня после обеда уйти, но предупредила, что фактически мы будем на территории лагеря."
    "Сказала она и про то, что под открытым небом мы не окажемся, у нас есть спальный мешок."

    show mt pioneer sad with half_good_dspr

    "Вожатая выслушала это всё, и покачав головой, ответила, потирая лоб."
    mt "Ох, дети…"
    mt "Конечно, это не по правилам. Поход должен быть под руководством хотя бы одного вожатого."
    mt "И странно вообще, что нам его не назначили на эту смену."
    mt "Но я знаю, что даже если не отпущу вас, вы всё равно сбежите, хоть я вас под ста замками закрою."

    show mt pioneer normal with dspr

    mt "Поэтому, я вас отпускаю. {w}А ещё потому, что вы честно всё сказали, а не пытались сбежать."

    show sl pioneer smile2 with dspr

    "Славя в миг повеселела, я тоже улыбнулся."
    mt "Но имейте в виду, что я это делаю под свою ответственность. Если с вами что-то случится, спрос будет с меня."
    mt "И хоть вы себя и показали, как пионеры ответственные, и взрослые, я обязана предупредить."
    mt "Глупостей не делать, за территорию лагеря не выходить."
    mt "При первых признаках недуга незамедлительно обратно в лагерь."

    hide sl
    show mt pioneer grin
    show sl pioneer laugh at right
    with dspr

    "Славя расплылась в «спасибо-спасибо-спасибо», и обняла вожатую."
    me "Спасибо за доверие, Ольга Дмитриевна."

    show mt pioneer smile with dspr

    mt "Да что уж там… Кстати, а что вы вечером то есть будете?"

    hide sl
    show sl pioneer smile2 at fright
    with dspr

    sl "Об этом не переживайте. Я пока помогала убираться в столовой, поговорила с поварихами."
    sl "Выделят нам остатки булочек и кефира с завтрака. Голодные не останемся."
    mt "Ну, хоть что-то."
    mt "Ладно, пойдёмте кушать."
    
    show sl pioneer laugh with dspr

    "Вожатая пошла впереди нас, а мы со Славей взялись за руку, и беззвучно засмеялись."
    "Теперь нам точно ничего не помешает, и ни от кого не прилетит."

    stop ambience fadeout 1.0

    hide mt
    hide sl
    show bg int_dining_hall_people_day
    show sl pioneer smile at right
    with dissolve

    play ambience ambience_dining_hall_full fadein 1.0

    "Столовая уже была полна пионеров, так что, взяв подносы, нам ничего не оставалось, кроме как сесть за единственные два оставшихся свободных места, с незнакомыми пионерами, и приступить к еде."
    "Так как мы сидели в битком набитой столовой, то не могли даже примерно перекинуться парой слов о нашем предстоящем «путешествии», так что разговор зашёл за отвлечённые темы…"

    stop music fadeout 2.0

    "..."

    play music music_list["dance_of_fireflies"] fadein 2.0 volume 0.8

    "Когда, наконец, пионеры начали рассасываться, а мы со Славей доели, то вышли на улицу, и заговорили о предстоящих планах."

    stop ambience fadeout 1.0

    show bg ext_dining_hall_near_day with dissolve

    play ambience ambience_camp_center_day fadein 1.0

    me "Когда выдвигаемся?"
    sl "Мне сейчас надо будет в столовой забрать нам еду, а для этого мне нужно в домик, у поварих пакетов нет."
    sl "Ну а потом к Жене в библиотеку, и можем отправляться."
    me "Хорошо, я тогда тоже кой-чего заберу. Встретимся тут же минут через десять?"

    show sl pioneer smile2 with dspr

    sl "Да, отлично."
    "Мы поцеловались и разошлись."

    hide sl
    show bg ext_dining_hall_away_day
    with dissolve

    "Славя направилась к домикам, а я пошёл в музыкальный клуб за гитарой."
    "..."

    show black with clocks_in

    show bg ext_musclub_verandah_day
    hide black
    with clocks_out

    "Уже через несколько минут я подошел к зданию клуба, и открыл дверь."
    "..."
    "Зайдя внутрь, и забрав гитару, я увидел что в замочной скважине изнутри торчит ключ."
    th "Вот Мику блин, во даёт."
    "Я вытащил ключ, закрыл дверь снаружи, и бросив ключ под коврик, зашёл за клуб."

    call smoking_process(with_pause=1.0)

    "Поставил гитару рядом, закурил сигарету, сел и задумался."
    th "А мне что-нибудь надо из домика взять?"
    th "..."
    th "Да вроде нет."
    "Повертев в голове варианты того, что я мог забыть, я так ничего и не вспомнил, и направился обратно к столовой."

    show black with clocks_in

    show bg ext_dining_hall_away_day
    show sl pioneer smile far at cright
    hide black
    with clocks_out

    "Ещё издалека я увидел Славю, которая стояла с немаленьким пакетом, в котором, судя по всему, было несколько булочек и несколько пакетов кефира."

    hide sl
    show sl pioneer surprise at right
    with long_dspr

    "Подойдя ближе, я так же заметил сильное изумление на её лице."
    sl "Сём, ты что… {w}играть будешь?"
    "Я улыбнулся."
    me "Да, ну-у… Сюрприз получился не полностью, я-то не думал, что мне с ней и с тобой одновременно идти придётся."
    me "Но да, Мику помогла мне выучить композицию."

    show sl pioneer tender with good_dspr

    "Славя расплылась в улыбке."
    sl "Сёма… {w}Ого!"
    sl "Так ты не только свою партию на выступление учил, но ещё и песню для меня?"
    sl "Бли-ин, это так мило!"

    hide sl
    show sl pioneer smile2 close at cright
    with good_dspr

    pause(1.0)

    hide sl
    show sl pioneer smile2 at right
    with good_dspr

    "Девушка подошла ближе, и положив мне руку на плечо, поцеловала меня."
    sl "Я притворюсь, что не вижу её, пока ты не решишь сыграть, хорошо?"
    "Мы посмеялись, и отправились к зданию библиотеки за спальником."

    show bg ext_library_day
    show sl pioneer smile
    with dissolve1

    "Подойдя, я оставил гитару у входа, и мы зашли внутрь."

    stop ambience fadeout 1.0

    show bg int_library_day with dissolve

    play ambience ambience_library_day fadein 1.0

    "Спальный мешок сложно было не заметить."
    "Он был свёрнут по всем походным канонам, и лежал прямо у входа."
    "Я поднял его."
    th "Не легкий, блин. Тёплый, наверное."
    "Благо сразу я обнаружил, что у него есть лямки, чтобы его можно было одеть как рюкзак."
    "Закинув мешок за спину, я подтянул регулировки, чтобы он не болтался, и утвердительно хмыкнул."

    show sl pioneer smile2 with dspr

    sl "Женя-я! Спасибо, что оставила спальник! Мы ушли!"
    "Из дальнего конца помещения послышалось."
    mz "Хорошо!"

    stop ambience fadeout 1.0

    show bg ext_library_day
    show sl pioneer smile
    with dissolve

    play ambience ambience_camp_center_day fadein 1.0

    "Мы вышли из библиотеки, я взял гитару в левую руку, а правую протянул Славе."

    stop music fadeout 2.0

    hide sl
    show sl pioneer smile close at right
    with good_dspr

    pause(1.0)

    play music music_list["everlasting_summer"] fadein 2.0 volume 0.7

    "Она взяла её, и мы медленно зашагали."
    th "Вот бы это {b}лето{/b} было {b}бесконечным{/b}."
    "Пронеслось в голове."
    "..."

    show bg ext_path_day with dissolve

    "Выйдя на лесную тропинку, мы обсуждали всякое, когда я спросил."
    me "Кстати, а куда конкретно мы идём?"
    sl "Да я сама толком не знаю. Но эта тропинка ведёт к месту, где у отрядов обычно конечная точка похода."
    "Так что идти должно быть недалеко, не больше сорока минут, может часа."

    show sl pioneer smile2 with half_good_dspr

    sl "А ещё, говорят, рядом есть чистое озеро."
    "Я улыбнулся."
    me "Я был бы не против искупаться."
    sl "Я тоже!"

    show sl pioneer smile with good_dspr

    "..."
    "Продолжая идти, мы мило беседовали, и наслаждались красотой вокруг."
    "Нас вела прекрасная лесная тропа, достаточно широкая чтобы по ней можно было спокойно идти вдвоём."

    stop ambience fadeout 1.0

    pause(1.5)

    play ambience ambience_forest_day fadein 1.0

    show bg ext_path2_day with dissolve

    "Постепенно, тропинка начала сужаться, а сама она становилась всё более заросшей."
    "Мы почувствовали, что уже не просто идём пионерской походной тропой, а заходим в самый настоящий лес."
    "И на удивление, не было комаров, да и в принципе я тут не встретил ни одного насекомого."
    "Чему, впрочем, я был скорее рад."
    "..."

    pause(1.0)

    "Совсем скоро идти рядом стало невозможно, кто-нибудь из нас постоянно сходил в траву, и путь тому преграждали кусты."

    show sl pioneer smile at walk_away_right
    pause(1.0)
    hide sl with good_dspr

    "Я решил идти первый, а Славя за мной."
    "Так мы прошли ещё метров двести, пока впереди не показалось большое пространство."
    me "Смотри, видимо пришли!"
    sl "Где?"

    pause(1.0)

    show sl pioneer smile2 at center
    with good_dspr

    "Она выглянула пару раз из-за моей спины, но толком ничего не разглядев, обогнала меня, и бодро зашагала впереди…"

    hide sl
    show bg ext_polyana_day
    show sl pioneer smile at fleft
    with dissolve1

    "И вот, мы вышли на залитую солнцем поляну, находившуюся в низине, в окружении деревьев, и сотен полевых цветов."

    show sl pioneer tender with dspr

    sl "О-ой, как красиво!"
    "Я тоже оценил красоту этого места."
    "По всей видимости, это была не та поляна, куда ходили пионеры. Она выглядела совершенно девственно чисто."

    hide sl
    show sl pioneer smile2 far at cleft
    with good_dspr

    pause(1.0)

    hide sl
    show sl pioneer smile far at cright
    with good_dspr

    pause(1.0)

    hide sl
    show sl pioneer tender far at fright
    with good_dspr

    pause(1.0)

    hide sl
    show sl pioneer smile at cright
    with good_dspr

    pause(1.0)

    hide sl
    show sl pioneer smile2 at center
    with long_dspr

    "Славя легонько оббежала поляну по кругу, сорвала один цветочек, и вдохнув его аромат, легла на траву."
    "Я впервые увидел её в самой естественной её среде, так как она выросла рядом с природой."

    play sound sfx_drop_alisa_bag volume 0.8

    "Я скинул спальник, и аккуратно поставил гитару рядом с одним из деревьев, и присоединился к Славе."

    hide sl
    show bg ext_polyana_nebo_day
    with dissolve1

    "Я лёг на траву рядом с ней, и посмотрел наверх."
    "Дневное небо было уже не таким ярким, но солнечные лучи красиво пробивались сквозь кроны деревьев."
    "..."

    stop music fadeout 2.0

    "Мы лежали, взявшись за руки, и смотрели на эту великолепную красоту."

    play music music_list["forest_maiden"] fadein 2.0 volume 1.0

    "Славя прикрыла глаза рукой, но по трясущимся губам я понял, что она собирается заплакать."
    me "Славечка, ты чего?"
    sl "Я… {w}Сёма, я так рада оказаться тут с тобой, вдвоём."

    show cg d7_polyana with dissolve

    "Я перевернулся на бок, и отложив руку девушки, нежно протёр ей выступившие слёзы."
    me "Но мы же оказались."
    me "Я считаю, что нам обоим повезло. И оказаться в этом лагере, и полюбить друг друга, и сейчас, лежать вдвоём здесь…"
    "Я понизил голос."
    me "На красивейшей поляне, а вокруг никого."
    "Славя лишь улыбнулась в ответ, и притянула меня за воротник рубашки к себе."
    "Я закрыл глаза, а наши губы соединились в поцелуе."

    show blink

    "Но это была не страсть. Не в этот момент."
    "Сейчас это была бесконечная благодарность друг другу за все моменты вместе, за взаимную любовь, уважение, доверие…"
    "За то, что мы нашли друг друга, а наши души слились воедино, и мы уже начинали понимать друг друга с полуслова."
    "..."

    hide blink
    hide cg
    show bg ext_polyana_day
    show unblink
    with dissolve1

    show sl pioneer smile at right
    with long_dspr

    "Полежав ещё некоторое время в тишине, державшись за руки, Славя сказала."

    hide unblink

    sl "Пойдём, поищем озеро, про которое я говорила?"
    me "Да, пойдём. Было бы правда здорово искупаться."
    "Мы встали, и выбрав произвольное направление, направились на поиски лесного озера."

    show bg ext_path2_day
    show sl pioneer smile2
    with dissolve

    "Пройдя немного по лесу, Славя вдруг вскинула руку, и указала куда-то."
    sl "Смотри, я вижу!"

    hide sl
    show sl pioneer smile at center
    with good_dspr

    "Она побежала вперёд."
    me "Стой, подожди!"

    hide sl with dspr

    "..."

    show cg d2_slavya_forest with dissolve

    "Нагнав её через несколько секунд, я уже наблюдал как она сбрасывает одежду у берега."
    "Я последовал её примеру."

    stop ambience fadeout 1.0

    show cg d6_sl_swim with dissolve

    play ambience ambience_lake_shore_day fadein 1.0

    "Славя разделась догола, и зашла в воду."
    "Уже совсем скоро мы с ней вдвоём плескались в слегка тёплой, но чистой и освежающей воде лесного озера."
    "Удивительно, но под ногами я даже не чувствовал ила, ноги касались мягкого песка."
    "..."
    "Вдоволь накупавшись, мы вышли из воды, и решили что пока не будем одевать нижнее белье, а просто накинем верхнюю одежду."

    stop music fadeout 2.0

    hide cg
    show sl pioneer_wet smile at right
    with dissolve

    pause(1.0)

    play music "<from 19.5>" + music_list["take_me_beautifully"] fadein 3.5 volume 0.75

    "Надо ли говорить, что от мокрого тела наши рубашки намокли, и стали полупрозрачные?"
    "И теперь, Славя хоть и была прикрыта рубашкой, но она вовсе ничего не закрывала, а лишь наоборот, подстёгивала воображение."
    "Так же и я уже не мог сдерживать свою природу, и всё было прекрасно видно, хоть я был и в шортах."
    "Мы это, конечно, оба заметили друг в друге."
    "Но лишь отметили этот приятный факт, многозначно друг на друга посмотрев, и отправились обратно к полянке."
    "..."

    stop ambience fadeout 1.0

    window hide

    hide sl
    show bg ext_polyana_sunset
    with dissolve

    call set_time("sunset")

    pause(1.0)

    show sl pioneer_wet smile at right
    with good_dspr

    play ambience ambience_forest_evening fadein 1.0

    window show

    "Пока мы шли обратно, день сменился вечером, и атмосфера на нашей полянке поменялась."

    play sound sfx_alisa_lighter volume 0.8
    queue sound sfx_forest_fireplace fadein 2.0 volume 0.7 loop

    "Разложив вещи, чтобы они успели просушиться, мы разожгли костёр, и сидели перед ним, уминая кефир с булочками."

    hide sl
    show sl pioneer_wet smile at left
    with dissolve

    "Посреди трапезы, Славя встала и подошла к нашим вещам."
    sl "Сём, да они уже высохли!"
    sl "Оденемся?"
    me "Да, конечно."
    "..."

    hide sl with good_dspr

    pause(1.0)

    show sl pioneer smile at left
    with good_dspr

    "Мы оделись, и вернулись к костру, продолжив наш небольшой ужин."

    hide sl
    show sl pioneer smile at right
    with good_dspr

    "..."

    show sl pioneer smile2 with dspr

    "Славя закончила есть первая, и достав из кармана платочек, вытерла рот."
    "Я заметил, что платок был не обычный, явно ручной работы."
    "Он был чуть большего размера, и украшен сложным вышитым рисунком из цветов в русском классическом стиле."
    me "Ого, красивый у тебя платок. Откуда у тебя такой?"
    sl "Я сама делала."
    "Я немного округлил взгляд."
    me "Ты и вышивать умеешь?"
    sl "А я разве не рассказывала? {w}Да, бабушка учила."

    stop music fadeout 2.0

    show sl pioneer shy with dspr

    pause(1.0)

    play music music_list["forest_maiden"] fadein 2.0 volume 1.0

    "Славя немного помяла платочек в руках, и сказала."
    sl "А знаешь, бери его себе."
    sl "Кто знает, когда мы в следующий раз встретимся, и встретимся ли вообще?"
    "На этих словах моё сердце сжалось."
    th "Уже завтра смена закончится. Что же будет дальше?"

    show sl pioneer happy_cry with good_dspr

    "Я запил остатки булочки, и подошёл к Славе. Она опять начала плакать."

    hide sl
    show cg d5_sl_love
    with dissolve

    "Я сел рядом с ней, и обнял её."
    me "Славя, давай не будем об этом думать сегодня."
    me "Обменяемся адресами, будем писать… Может, когда-нибудь, кто-нибудь из нас приедет к другому."
    "Я сам не верил в то, что говорил… Но мне хотелось утешить её, убедить, что всё будет хорошо…"
    "Хотя я сам не был уверен даже в своей судьбе."
    th "Что меня ждёт дальше?"
    "..."
    "Славя, кажется, немного успокоилась, и расслабилась, сидя у меня в объятиях."

    hide cg
    show sl pioneer smile2 at right
    with dissolve

    "Спустя некоторое время я поднялся, подбросил веток в костёр, и сказал Славе."
    me "Подожди меня немножко, я скоро вернусь."
    "Славя посмотрела на меня, и ответила."
    sl "Хорошо."
    "Я сразу расстелил спальник, чтобы не заниматься этим потом, и отошёл чуть дальше по окружности поляны, чтобы не дышать на Славю сигаретным дымом."

    hide sl
    show sl pioneer smile2 far at fright
    with long_dspr

    pause(1.0)

    call smoking_process

    "Отчего-то у меня тряслись руки, а сердце всё никак не хотело сбавлять темп."
    
    play sound2 sfx_smoking_cigaret

    "Я сделал затяжку, глубоко вдохнул, и задержав воздух на несколько секунд, выдохнул."
    "Славя сидела возле костра, поджав ноги, и обхватив их руками, и смотрела на красиво развивающиеся язычки пламени, иногда поглядывая в мою сторону."
    th "Ладно. С Богом."
    "Я бросил сигарету, потушил её носком, и зажевал последнюю оставшуюся жвачку."

    hide sl
    show sl pioneer smile2 at right
    with long_dspr

    "Взяв рядом стоящую гитару, я вернулся к костру, и сел рядом с девушкой."

    stop music fadeout 3.0

    "Славя взглянула на меня, и мило удивилась."

    show sl pioneer shy with dspr

    sl "Сёма... {w}Ты что, хочешь мне сыграть?"
    me "Да."
    "У меня дрожал голос."
    me "Эту мелодию я подготовил специально для тебя."

    hide sl
    show sl pioneer smile2 at cright
    with good_dspr

    "Славя подвинулась поближе, и посмотрела мне в глаза, полная ожидания."
    "Дав себе пару секунд на то, чтобы собраться с силами, я набрал воздух в грудь, и мои руки коснулись первых струн."

    stop sound fadeout 1.0
    stop ambience fadeout 1.0

    window hide

    hide sl
    show cg d7_polyana_guitar_playing
    with dissolve1

    play music this_one_for_her volume 1.05

    call set_time("night")

    window show

    "Я начал играть."
    "Я очень боялся, что от волнения, от того что мои руки трясутся, я забуду мелодию, начну промахиваться по струнам."
    "Но нет."
    "Музыка лилась сама собой."
    "Я немного качал в такт мелодии головой, медленно отводя её то в одну, то в другую сторону."
    "А Славя… Славя смотрела на меня, как завороженная."
    "Она приоткрыла рот в небольшом изумлении, да так и смотрела на меня всё время, пока я играл."
    "Этот момент был даже сильнее тех, когда мы танцевали вдвоём на лодочном причале, когда я впервые её поцеловал."
    "Тогда между нами всё ещё была недосказанность. А сейчас…"
    "Сейчас мы оба знаем, что любим друг друга. И от этого момент становился ещё ценнее."
    "Когда ты точно знаешь, что рядом с тобой сидит любимый тобою человек, а его взгляд, мысли и слух полностью обращены в твою сторону."
    "Я вновь ощутил это. {w}Вокруг нас перестало существовать всё вокруг. {w}Всё стало неважно."
    "Остались только мы в моменте душевного единения."

    $ renpy.pause(2.0, hard=True)

    hide cg
    show bg ext_polyana_night
    with dissolve1

    play ambience ambience_forest_night fadein 1.0
    stop music fadeout 3.0

    $ renpy.pause(2.0, hard=True)

    "Я закончил играть, и посмотрел на Славю."

    show sl pioneer tender at cright
    with dissolve

    "Она была невероятно счастлива."
    sl "Сёма..."

    show sl pioneer happy_cry with dspr

    sl "Спасибо тебе большое. {w}Это очень красиво."
    me "Я люблю тебя."

    play music music_list["forest_maiden"] fadein 2.0 volume 1.0

    hide sl
    show cg d7_polyana_night
    with dissolve1

    "Вместо ответа Славя притянула меня к себе, и начала целовать."
    "Я сразу поддался ей."
    
    pause(1.0)

    "Вскоре, мы опять лежали на траве, полностью отдавшись друг другу."
    "Вчерашний первый опыт смыл всяческие остатки смятения, неловкости…"
    "Продолжая поцелуи и ласки, мы начали раздевать друг друга."
    "Расстегнув Славину рубашку, я одной рукой снял с неё лифчик, и принялся за юбку."
    "Она делала то же самое."
    "Мы оба знали, что сейчас произойдёт."
    "Знали, и были к этому готовы."

    show cg d6_sl_hentai_2 with dissolve1

    "Вскоре, мы остались почти в неглиже."
    "Я опустился к груди девушки, а вторую руку опустил ниже."
    "Славя застонала."
    sl "Сёма, я..."
    "Она уже пылала."
    "А от отсутствия опыта так и вовсе, кажется, была в состоянии эйфории."
    sl "По о-… {w}Поосторожнее…"
    "Я вернулся к её лицу, поцеловал, и рукой нащупал рядом свои лежащие шорты, в кармане которых так удачно лежала одна упаковка изделия из резины №3."
    me "Конечно…"

    show cg d6_sl_hentai_1 with dissolve

    "И вот, это случилось."
    "И она, и я были полностью поглощены друг другом."
    "Я старался быть максимально нежен, но так и не понял, было ли ей больно."
    "Наверное, она сама не обратила на это внимания."
    "Славя полностью доверилась мне, и кажется, была готова потерять сознание от удовольствия."
    "Наши тела сплились в удивительном танце любви..."

    $ renpy.pause(2.0, hard=True)

    "Спустя… {w}некоторое время, я не знаю, сколько прошло."
    "Я почувствовал, что близок."
    "Прибавив темп, я заставил Славю стонать громче."
    "Она обвила меня руками, и…"

    window hide

    call flashing(dissolve_time=0.25)
    $ renpy.pause(1.0, hard=True)

    call flashing(dissolve_time=0.25)
    $ renpy.pause(1.0, hard=True)

    hide cg
    show bg ext_polyana_nebo_night
    with dissolve1

    pause(1.5)

    window show

    "Мы всё ещё лежали на траве."
    "Небо уже потемнело, но это создавало каку-то особенную, даже магическую атмосферу."
    "Я лежал, положив одну руку под голову, а Славя была наполовину на мне, обняв меня одной рукой, и закинув на меня одну ногу."
    "Своей второй рукой я обнимал её."
    sl "Так красиво…"
    sl "Вот бы это лето никогда не заканчивалось."
    th "Удивительно. Я помню, что подумал также буквально несколько часов назад."
    "Я погладил девушку по спине, а потом по волосам."
    me "Ты просто мои мысли читаешь. Я думал точно также."
    "Славя несколько секунд помолчала, а потом сказала."
    sl "А знаешь, почему? Потому-что мы уже чувствуем желания друг друга, даже если не произносим их вслух."
    "Я улыбнулся, и ещё долго мы лежали, разговаривали, и смотрели на то, как ночь вступает в права, и на проявляющиеся на небе звёзды."
    "..."

    stop music fadeout 2.0

    show bg ext_polyana_night
    show sl naked smile2 at right
    with dissolve1

    "Вскоре на улице стало прохладно, и совсем стемнело."

    play music music_list["dance_of_fireflies"] fadein 2.0 volume 0.62

    me "Будем ложиться спать?"
    sl "Да, завтра надо до завтрака… {w}хи-хи…"
    sl "Оказаться в лагере."
    "Я посмеялся с каламбура, и ответил."
    me "Ну, тогда спать."

    hide sl with good_dspr

    "Я принёс спальник, и мы нырнули в него вдвоём."
    "Одеваться не стали, так как он был и правда очень тёплый."
    "Славя глубоко вздохнула, и немного вздрогнула, поёжившись."
    sl "Знаешь, так странно... {w}Я себе и представить ничего подобного не могла, но..."
    sl "Всё ощущается... Правильно что-ли?"
    sl "Я не чувствую что мы допустили ошибку, поторопились, или ещё что-нибудь."
    sl "Почему-то я знаю, что у нас всё будет хорошо."
    "Славя взглянула мне в глаза, и сказала."
    sl "Потому-что я люблю тебя. {w}А это главное."
    "Я поцеловал девушку, и сказал."
    me "Я уверен, что всё так и будет."
    "Славя улыбнулась, источая полное спокойствие и умиротворение, и закрыла глаза, уперевшись мне в грудь."
    me "Спокойной ночи, Славя."
    sl "Спокойной ночи."
    "Я застегнул молнию на спальном мешке, и мы, обнявшись, начали засыпать…"

    window hide

    stop music fadeout 2.0
    stop ambience fadeout 1.0

    show blink

    $ renpy.pause(3.5, hard=True)

    jump simple_happiness_mod_day8


# День 8
label simple_happiness_mod_day8:
    $ renpy.block_rollback()
    $ backdrop = "days"
    $ new_chapter(8, u"Простое Счастье. День 8")

    call set_time

    $ set_mode_adv()

    play ambience ambience_forest_day fadein 3.0 volume 0.8
    play music music_list["everyday_theme"] fadein 3.0 volume 0.7

    window show

    "Я проснулся от того, что у меня затекла шея."
    th "Да, не привык я конечно к такому, считай что на земле спать."

    show cg d7_sl_morning
    hide blink
    show unblink
    with None

    "Я открыл глаза, огляделся вокруг, и немного расстегнув спальник, стал разминать затёкшую шею."

    hide unblink

    "Рядом со мной лежала Славя, и всё ещё мирно спала."
    "Я улыбнулся, вспомнив наш вчерашний поход, купание, игру на гитаре. {w}Ночь вдвоём…"
    "Я зевнул, и потянулся. Утро уже начало вступать в права."
    "Опять посмотрев на Славю, я наклонился к ней, и положив руку ей на плечо, поцеловал, и негромко сказал."
    me "{i}Сла-авя! {w}Надо просыпаться.{/i}"

    show cg d7_sl_morning_2 with dissolve1

    "Славя постепенно открыла глаза, и моргнув пару раз, улыбнулась мне."
    sl "Ах, это самое лучшее утро в моей жизни! {w}Доброе утро, Сёма!"
    "Её рука лежала у меня на животе, и она начала водить по нему кончиками пальцев."
    "Я улыбнулся."
    me "Доброе, Славя!"
    "Я сполз немного обратно, и заключил девушку в поцелуй..."

    pause(1.0)

    "Но немного погодя, мы встали и начали собираться."

    show black with clocks_in
    
    hide cg
    show bg ext_polyana_day
    hide black
    with clocks_out

    pause(1.0)

    show sl pioneer smile at right
    with good_dspr

    "Одевшись, мы скрутили спальник, и доели остатки того, что оставалось в пакетике."
    "А оставалось там всего по одной булочке и по одному пакету кефира."
    sl "Ну ничего, на завтрак наверное должны успеть."

    play sound sfx_stomach_growl volume 0.8

    "Хотя я и съел уже свою часть, живот заурчал, и я ответил."
    me "Хотелось бы! Лишь бы ещё вожатая нас не потеряла."
    "..."

    hide sl
    show sl pioneer smile at cright
    with good_dspr

    "Я распинал остатки вчерашнего костра, и прихватив гитару, мы со Славей взялись за руки, и направились обратно в лагерь."

    show bg ext_path_day with dissolve

    "Возвращались мы тем же путём, которым пришли сюда."
    "Странно, но обратная дорога казалась короче, так как уже скоро через деревья можно было увидеть мелькающие строения."

    show sl pioneer smile2 with half_good_dspr

    sl "Ого, почти пришли! Быстро мы."
    me "Точно. Мне казалось вчера мы дольше шли."

    stop ambience fadeout 1.0

    show bg ext_library_day
    show sl pioneer smile
    with dissolve

    play ambience ambience_camp_center_day fadein 1.0

    "Вышли мы обратно к зданию библиотеки."
    me "Слушай, а может сразу спальник скинем?"

    show sl pioneer surprise with good_dspr

    sl "Даже не знаю, библиотека наверное закрыта."

    hide sl
    show sl pioneer normal far at right
    with long_dspr

    "Славя подошла к двери, и подергала за ручку."
    sl "Закрыто."
    "Заключила она."

    show sl pioneer smile with dspr

    sl "Ну ладно, бросай здесь, Женя всё равно сюда ещё придёт. Я думаю не обидится."
    "Я согласился, и скинув мешок рядом с дверью, мы пошли к столовой, скоро должен был прозвучать горн."

    hide sl
    show bg ext_square_day
    show sl pioneer smile at right
    with dissolve

    "Идя по лагерю, я постоянно ловил себя на мысли, что всё тут начало казаться странным."
    "Было такое чувство, которое возникает только тогда, когда уезжаешь из какого-то места, где был не так долго, чтобы каждый уголок уже был знаком, но к которому успел прикипеть."
    "Всё кажется не то что, чужим, но… {i}Уже не своим{/i}, что ли?"
    "Хотя ты ещё не уехал, но уже понимаешь, что не принадлежишь этому месту."
    "Кажется, мою угрюмую морду заметила Славя."

    stop music fadeout 2.0

    show sl pioneer surprise with good_dspr

    sl "Сём, ты в порядке?"

    play music music_list["i_dont_blame_you"] fadein 2.0 volume 0.76

    me "Да-а, просто… Думаю обо всём. Уезжать не хочется."

    show sl pioneer sad with dspr

    sl "Мне тоже… Но ещё больше мне не хочется расставаться с тобой."
    sl "На райцентре надо будет обязательно обменяться адресами."
    me "Да, конечно. Я напишу тебе при первой же возможности."
    "Я опять врал."
    "Я не знал, и не мог знать что будет."
    "Но признаться, выдать всё как есть? Она бы не поверила. Да и было уже поздно."

    show bg ext_dining_hall_away_day
    show sl pioneer normal
    with dissolve

    "Мы начали подходить к столовой, и увидели стоящую рядом вожатую."

    show mt pioneer smile at left
    with good_dspr

    "Когда мы подошли ближе, она сказала."
    mt "Ну, вижу что я зря переживала!"
    mt "Нагулялись?"

    show sl pioneer smile with dspr

    "Мы со Славей почти одновременно поздоровались, после чего подтвердили, что с нами всё хорошо."
    mt "Вот и отлично!"
    mt "Ну, пойдёмте кушать. В обед уже автобус, а всем надо ещё собраться."
    "Мысль о скором отъезде всё больше давила на меня."

    stop ambience fadeout 1.0

    hide mt
    show bg int_dining_hall_people_day
    with dissolve

    play ambience ambience_dining_hall_full fadein 1.0

    "Мы зашли в столовую, взяли подносы в последний раз, и получив порцию, сели за столик, где сидели Мику и Алиса."

    show dv pioneer normal at fleft
    show mi pioneer normal at cleft
    with long_dspr

    "Гитару пришлось ставить рядом со столом."

    stop music fadeout 2.0

    show mi pioneer smile with dspr

    mi "Ой, ребята, привет!"
    "Мы поздоровались."

    play music music_list["so_good_to_be_careless"] fadein 2.0 volume 0.78

    show mi pioneer happy with dspr

    mi "Ребята, вы где вчера после обеда пропали? Ни тебя …"
    "Она обращалась к Славе."

    show mi pioneer smile with dspr

    mi "… ни Семёна не видела."
    "Мы со Славей переглянулись, и улыбнувшись, я сказал."
    me "Мы… Гуляли."
    dv "Весь день?"

    show sl pioneer smile2 with dspr

    sl "Мы далеко гуляли… {w}Чтоб нас никто не видел."

    pause(2.0)

    show dv pioneer surprise
    show mi pioneer surprise
    with half_good_dspr

    "Пару секунд девушкам взяло осознать сказанное Славей, после чего они переменились в лице."

    show mi pioneer grin with dspr

    mi "О-хоо! Вот это да!!"

    show dv pioneer laugh with dspr

    dv "Ну всё, Семён, теперь не отвертишься. Обязан жениться!"
    "Мы посмеялись, а я посмотрел на Славю, и правда понял, что уже не представляю своей жизни без неё."
    "Мы продолжили есть, и обсуждать отъезд, но благодаря девочкам атмосфера разрядилась, так что напряжение спало."
    "..."

    stop ambience fadeout 1.0

    hide dv
    hide mi
    show bg ext_dining_hall_near_day
    show sl pioneer smile
    with dissolve1

    play ambience ambience_camp_center_day fadein 1.0

    "Выйдя из столовой, мы на некоторое время попрощались с Алисой и Мику, им надо было что-то закончить в клубе."
    "Я передал Мику гитару, и поблагодарил её. Мы со Славей остались стоять на крыльце столовой."
    "Она облокотилась на перилла, и вздохнула."

    hide sl
    show sl pioneer smile close at cright
    with good_dspr

    "Я подошёл к ней."
    sl "Э-эх, как не хотелось бы растянуть пребывание тут ещё на подольше… Но надо собираться."
    sl "Пойдём, унесём свои вещи на склад?"
    "Я протянул девушке руку."

    show sl pioneer smile2 with dspr

    me "Пойдём."

    stop music fadeout 2.0

    hide sl
    show bg d8_nvl_back
    with dissolve

    call to_nvl_mode

    play music music_list["everyday_theme"] fadein 2.0 volume 0.7

    "Мы начали готовиться к отъезду."
    "Сперва, мы со Славей пошли в сторону домиков, и разделившись между нашими жилищами, отправились собирать постельное бельё, чтобы сдать его."
    "Также, я забрал свой телефон из подушки."
    "На нём оставалось 10%% заряда, а уведомление в шторке сигнализировало о том, что устройство почти разряжено."
    "Убрав телефон в карман, я продолжил собирать вещи."
    "..."
    "Закончив с постельным, я сложил всё в наволочку от подушки, и уже собирался уходить, но обернулся, и посмотрел на свою кровать."
    "Точнее, уже не на свою."
    "Она была пустой."
    "Я с грустью выдохнул, и вышел из домика."
    "..."
    "Мы вновь пересеклись со Славей, и отправились на склад, чтобы сдать постельное."
    "Отстояв небольшую очередь пионеров, которые уже успели выстроиться перед вожатой, мы сдали свои вещи и расписались."

    call to_adv_mode

    show bg ext_storage_day
    show sl pioneer smile at right
    with dissolve

    sl "Время ещё есть, а нам осталось только свои вещи собрать…"
    sl "Не хочешь немного прогуляться?"
    "Я улыбнулся, и ответил."

    show sl pioneer smile2 with good_dspr

    me "С удовольствием."
    me "Проводим лагерь перед отъездом."
    "Мы взялись за руки, и пошли в произвольном направлении."

    stop ambience fadeout 1.0

    show black with clocks_in

    play ambience ambience_boat_station_day fadein 1.0

    show bg ext_boathouse_day
    show sl pioneer smile
    hide black
    with clocks_out

    "Мы вышли на лодочную станцию."
    th "Символично."
    "Подумал я, и улыбнулся."
    "Днём она выглядела совсем иначе."
    "Она казалась манящей, завлекающей, зовущей на приключение."
    "Вот хоть сейчас бери лодочку, и плыви куда глаза глядят."
    "Хоть бы вон на тот остров, который виднеется с берега."
    "Отчего-то мне подумалось, что там наверняка растёт вкусная лесная ягода."
    sl "Пойдем вон туда сядем!"
    "Славя показала на место в небольшой тени деревьев."

    stop music fadeout 2.0

    hide sl
    show cg d8_sl_love
    with dissolve1

    pause(1.0)

    play music music_list["forest_maiden"] fadein 2.0 volume 0.85

    "Мы сели прямо как несколько дней назад, когда признались друг другу в любви."
    "Я обнимал свою любимую девушку, и думал, что это, возможно, последний раз, когда мы можем вот так вот спокойно сидеть, наслаждаться компанией друг друга и природой вокруг нас."
    "В груди всё больше давило от ощущения надвигающейся неизвестности."
    sl "Сём..."
    me "Да?"
    sl "Ты же меня не забудешь? Ты будешь мне писать?"
    "Я улыбнулся, но тут же мои губы задрожали."
    "Я начал глубоко и тяжело дышать."
    "Славя скорее всего это почувствовала, и крепче обняла мои руки."
    "С большим усилием подавив слёзы, и проглотив ком в горле, я ответил."
    me "Конечно, я… {w}Я постараюсь. {w}Я свяжусь с тобой при первой же возможности."
    "Славя откинула голову мне на грудь, и закрыла глаза."
    sl "Хорошо…"
    sl "Знаешь, а я почему-то уверена, что у нас всё получится."
    "Она немного засмеялась."
    sl "Даже не знаю, почему. Ведь мы живём в тысячах километров друг от друга."
    me "Наверное, это хорошее предчувствие."
    me "А такому надо верить, и надеяться на лучшее."

    show blink

    "Славя лишь вздохнула, а я покрепче обнял её, закрыв глаза."
    "У меня было странное, почти явственное желание. {w}Только одно."

    play sound sfx_head_heartbeat fadein 1.0 volume 0.65 loop

    "В голове гудело."
    "Она не болела, но было стойкое ощущение, как будто внутри работает ни то генератор, ни то большой вентилятор."
    "Я сосредоточился на главном. {w}На своём желании."
    "Мне было не важно где, в каком времени, и в какой стране."
    "Я просто хотел быть рядом с этой девушкой."
    "Ради этого я был готов отдать всё, и пойти на что угодно."
    "..."

    stop sound fadeout 1.0

    hide blink
    show unblink

    "Так мы просидели некоторое время, пока Славя не подняла на меня взгляд, и не поцеловала меня."
    sl "Нужно идти. А то опоздаем."
    me "Да…"
    "Я физически ощущал желание не покидать это место, остаться здесь…"

    hide unblink
    hide cg
    show sl pioneer smile2 at right
    with dissolve2

    "Но мы всё же поднялись, и пошли обратно к своим домикам."
    "..."
    "А по пути у нас завязался разговор про наши родные города, про то что есть интересного."
    "Делились мы и подробностями того, как мы живём."

    stop music fadeout 2.0
    stop ambience fadeout 1.0

    show black with clocks_in

    play ambience ambience_camp_center_day fadein 1.0
    play music music_list["farewell_to_the_past_full"] fadein 2.0 volume 0.65

    hide sl
    show bg ext_house_of_mt_day
    hide black
    with clocks_out

    "Проводив Славю до домика, и условившись встретиться на площади, чтобы уже оттуда пойти на остановку, мы разошлись."
    "А я, подошёл, уже по всей видимости в последний раз к домику вожатой, постучался."

    play sound sfx_knock_door7_polite volume 0.93

    pause(1.0)

    "Ответа не последовало."

    stop ambience fadeout 1.0

    show bg int_house_of_mt_clean_day with dissolve

    play ambience ambience_int_cabin_day fadein 1.0

    "Уже не гадая, где она может быть, я зашел в домик и задумался."
    th "А что мне, собственно, собирать?"
    "Из важных вещей у меня был с собой только телефон, но он уже лежал в кармане."
    "Тащить с собой свою зимнюю обувь не хотелось."
    "..."
    "Прикинув все за и против, я остановился на том, что заберу свою кофту и штаны, в которых приехал."
    "Достав их из шкафа, и аккуратно сложив на кровати, я сел на стул, и потёр лицо."

    stop music fadeout 2.0

    show blink

    pause(1.5)

    "Хотелось стереть с себя всю эту тяжесть."
    "Хотелось, чтобы всё само как-нибудь разрешилось, ведь впереди ждала только неизвестность."

    hide blink
    show pi normal at right
    show unblink

    play music music_list["door_to_nightmare"] fadein 1.5

    "Я открыл глаза и вздрогнул от неожиданности, подпрыгнув на стуле."
    "Передо мной стоял тот пионер из сна…"
    me "Ты… {w}это ты?"
    pi "Я? Не-ет, я это ты!"
    pi "Ну, в прочем, я тебе уже это объяснял."
    "В груди начала кипеть злость от его очередных игр в секреты, но я проигнорировал его слова."
    me "Так значит, это был не сон? Значит ты с той девушкой и правда забрали меня… Куда-то?"
    pi "А ты только сейчас это понял? Я думал ты посообразительнее."
    me "Я не намерен выслушивать твою пустую болтовню. Если тебе нет чего дельного сказать, уходи."
    pi "Да ладно, чего ты такой нерадостный?"
    pi "Больно будет, ну может первые раз пятьдесят…"

    show pi smile with dspr

    pi "Бесконечные эмоциональные качели, чтоб их, ха-ха-ха!"
    "Пионер мерзко рассмеялся."
    
    show pi normal with dspr

    pi "Я и сам через это проходил. Славя, Лена, Алиса, Мику, Славя, Лена, Мику, Алиса, Славя, Лена, чтоб её, Лена!"
    "Он сорвался на крик."
    pi "Я пытался полюбить каждую из них, но скоро понял, что это бессмысленно."
    pi "Потому-что всякий раз я оказывался в начальной точке."

    hide pi
    show pi normal at fright
    with long_dspr

    "Он присел на кровать вожатой."
    pi "Поэтому, просто начал получать удовольствие. {w}Сначала просто от изнасилования, потом от пыток."

    show pi smile with dspr

    pi "До сих пор вспоминаю. {w}М-м-м, ты даже не представляешь, как возбуждающе наша любимая вожатая кричит, молит о пощаде, когда раскалённая ложка проникает ей в живот."
    pi "А потом я совал в это отверстие, пх-пха-ха-ха!"
    "Он залился смехом, а я сидел на стуле, подперев голову кулаком, и смотрел в пол."
    me "Ты – долбанный психопат. Зачем ты {b}мне{/b} это всё рассказываешь?"
    pi "Делюсь опытом, друг! Разве тебе не интересно?"
    
    show pi normal with dspr

    pi "К чему романтические розовые сопли, когда можно от души оттянуться?"
    pi "Помню, я как то распял Славю в лесу, когда она в очередной раз купалась голая, как шлюха..."

    play sound sfx_head_heartbeat loop

    show white at pulsing_eyes

    "У меня закончился кислород."
    "Внутри всё сдавило, перед глазами пошла белая пелена. Я его уже не слышал."
    pi "… ну шлюха она и есть."

    show pi smile with dspr

    pi "А когда я закончил. М-м-м, я написал её кровью на её же теле красный крест. Как маэстро прям. Картина мас…"

    stop music fadeout 0.5

    show white at depulsing_eyes
    hide white
    with dissolve

    pause(0.5)

    show red at pulsing_eyes

    play music music_list["pile"] fadein 0.25 volume 0.95

    me "Заткнись, блять!!"

    play sound2 sfx_chair_fall volume 0.7
    queue sound2 sfx_blanket_off_stand
    queue sound2 sfx_body_bump volume 0.85

    hide pi
    show pi smile close at cright
    with long_dspr

    play sound2 sfx_bodyfall_1
    play sound3 sfx_bed_squeak1

    "Я вскочил со стула, и в одно мгновение повалил пионера, схватив его за воротник рубашки."
    pi "Ха-ха-ха!"
    "Он лишь заливался хохотом."
    "Я смотрел на него остервенелыми глазами, и тяжело дышал. Хотелось придушить его на месте."
    me "Я не знаю, кто ты, но лучше бы тебе убраться отсюда прямо сейчас, пока я тебя прямо тут не прикончил!!"
    "Мой голос срывался, а руки дрожали. Весь мир приобрёл красные оттенки."
    "Пионер продолжал заливаться гомерическим хохотом."
    pi "ХА-ХА-ХА!"
    pi "Ты всё равно мне ничего не сделаешь, ровно как и я тебе. Ведь {b}Я{/b}, ЭТО {b}ТЫ{/b}, СЕМЁН! А {b}ТЫ{/b}, ЭТО {b}Я{/b}!"
    me "Да как ты зае…!"

    play sound2 sfx_blanket_off_stand fadein 0.25 volume 0.75

    "Я занёс кулак для удара, и…"

    play sound2 sfx_bed_squeak1 fadein 0.25 volume 0.75

    hide pi with good_dspr

    "Он ударил по кровати, а я немного провалился."

    stop music fadeout 2.5

    "Пионера подо мной уже не было."
    "Я начал озираться по комнате, заглянул под кровати, и в шкафы."
    "Его не было."

    show red at depulsing_eyes
    hide red
    with dissolve

    "…"

    stop sound fadeout 2.0

    show blink

    "Всё ещё пытаясь отдышаться, я налил воды в кружку, поправил одежду, и сел на стул, закрыв глаза."
    "..."
    "Постепенно, я начал успокаиваться."

    play sound sfx_knock_door7_polite volume 0.6

    "Как вдруг услышал стук в дверь."

    hide blink
    show unblink

    me "Открыто!"

    hide unblink

    "Сказал я громче, чем хотел, и посмотрел в сторону входа."
    "Из-за двери сначала выглянула, а потом и зашла, Славя."

    play music music_list["i_dont_blame_you"] fadein 2.0 volume 0.9

    show sl pioneer surprise far at right
    with long_dspr

    sl "Семён?"

    hide sl
    show sl pioneer surprise close at cright
    with long_dspr

    "Я подбежал к ней, и обнял. Из глаз полились слёзы."
    me "Славя…"
    "Славя ответила на моё объятие, но всё ещё не понимала, что происходит."
    sl "Сёма, я тебя не дождалась на площади, зашла вот... Автобус уже скоро подьедет. {w}А ты чего красный весь?"
    "Я крепче вжался в неё, и смог выдавить лишь."
    me "Славя…"

    show sl pioneer sad with good_dspr

    "Мы сели на мою кровать, и Славя гладила меня по голове."
    sl "Сёма, что случилось?"
    "Я начал успокаиваться."
    "Утерев глаза, я потряс головой, чтобы выкинуть слова этого чокнутого, и ответил."
    me "Да так, что-то… Голова закружилась. Мне показалось…"
    
    show sl pioneer surprise with good_dspr

    "Славя приобняла меня за плечи, и спросила."
    sl "Что? Сёма, что показалось?"
    "Я лишь улыбнулся, взял её руку и выдохнул."
    me "Да так, ерунда всякая. От переживаний, наверное."

    show sl pioneer normal with long_dspr

    "Славя, кажется, тоже наконец расслабилась, и ответила."
    sl "А я уж и не знала, что и думать. Ну ты меня и напугал!"

    show sl pioneer smile with dspr

    "Славя улыбнулась."

    me "Да... Прости. Я сам испугался."
    sl "Ничего."

    "Славя опять обняла меня, и просидев ещё несколько минут, окончательно успокоившись, я сказал."
    me "Пойдём к остальным? А то без нас уедут."
    "Я хмыкнул, подумав, что это, в общем-то, не такая уж и плохая идея."

    show sl pioneer smile2 with dspr

    sl "Да… Пойдём."
    "…"
    "Я взял свои вещи, зажав их подмышкой, и поднял сумку Слави, которую она бросила на входе."

    stop ambience fadeout 1.0
    stop music fadeout 2.0

    hide sl
    show sl pioneer smile at right
    show bg ext_house_of_mt_day
    with dissolve1

    play ambience ambience_camp_center_day fadein 1.0
    play music music_list["confession_oboe"] fadein 2.0 volume 0.8

    "Мы вышли из домика вожатой, и взялись за руки…"

    show bg ext_houses_day with dissolve2

    "В последний раз прошлись вдоль домиков..."

    show bg ext_square_day with dissolve2

    "Прошли по площади…"

    show bg ext_clubs_day with dissolve2

    "Прошли мимо здания клубов..."

    stop ambience fadeout 1.0

    show bg ext_camp_entrance_day with dissolve1

    play ambience ambience_camp_entrance_day fadein 1.0

    "И вышли из ворот лагеря, где нас уже ждал автобус, а вокруг стояло много пионеров."
    "Мы подошли к нашему отряду."

    show mt pioneer normal at left
    with long_dspr

    "Там уже стояла Ольга Дмитриевна, и пересчитывала пионеров."
    "Увидев нас, она указала сначала на меня, потом на Славю, считая, и сказала."

    hide mt
    hide sl
    show cg d7_pioneers_leaving_without_us
    with dissolve

    mt "... девять."
    mt "Кого-то не хватает…"
    mt "Ульяна! Где Ульяна!?"
    "Мы все начали озираться, как тут из-за кольца пионеров пробилась девочка-ракета, и встала перед вожатой."

    show cg d7_pioneers_leaving with dissolve

    us "Ольга Дмитриевна, вот она я!"
    mt "Фух, ты где пропадаешь?"
    us "Извините…"
    mt "Ну ладно. Так, значит все в сборе."
    "..."
    "Вожатая начала инструктировать нас по поводу поведения в автобусе, а также касательно наших действий по прибытию в райцентр."
    "Чем дольше она говорила, тем больше дрожал её голос."

    stop music fadeout 2.0

    hide cg
    show us pioneer normal at fleft
    show mz pioneer normal at fright
    show un pioneer smile at left
    show dv pioneer normal at right
    show mi pioneer smile at cleft
    show sl pioneer smile at cright
    show mt pioneer scared at center
    with dissolve1

    pause(1.0)

    play music music_list["everlasting_summer"] fadein 2.0 volume 0.67

    "Наконец она не выдержала, и всхлипнула."
    mt "Дети… {w}Для многих из вас это была последняя смена в пионерском лагере."
    mt "Я надеюсь, она запомнится вам надолго…"
    "Вожатая окончательно заплакала, и к ней подошло несколько девочек, успокаивая."

    hide us
    hide mz
    hide un
    hide dv
    hide mi
    hide sl
    hide mt
    show bg ext_bus
    with dissolve1

    "Все остальные стояли рядом, разговаривая, а я отошел немного в сторону, и смотрел на автобус."
    "Не знаю, что в этот момент, говорил мой взгляд, но воспринимал я его не иначе как лотерейный билет."
    th "Ему велено решить мою судьбу. Куда он меня повезёт?"

    show sl pioneer smile2 at right
    with good_dspr

    "Славя, отойдя от вожатой, подошла ко мне, и обняв меня за руку, положила голову на плечо."

    play sound "<from 2.5 to 5.0>" + sfx_bus_stop fadein 1.0 volume 0.6 fadeout 1.0

    pause(1.0)

    "Но вот, мы услышали как открываются двери автобуса."
    "Вожатая отошла в сторонку, а пионеры начали загружаться в автобус."

    play sound sfx_ikarus_open_doors

    "Так же сделали и мы со Славей."

    stop ambience fadeout 1.0

    hide sl
    show bg int_bus
    show sl pioneer smile at cright
    with dissolve

    play ambience ambience_int_cabin_day fadein 0.5 volume 0.8

    "Мы прошли почти в самый конец, и заняли два места, чтобы к нам больше никто не мог сесть."

    show bg int_bus_people_day with dissolve

    "Вскоре, автобус был полностью заполнен пионерами."
    "Они разговаривали, смеялись, кто-то крутился."

    hide sl
    show sl pioneer smile close at cright
    with good_dspr

    "А Славя взяла мою руку, мы сцепили их на подлокотнике, и она положила голову мне на плечо и улыбнулась."
    "Только я сидел сжатый, тревожный. Впереди меня ждала неизвестность."
    "Я не знал, что со мной произойдёт уже через пару часов."

    show sl pioneer smile2 with good_dspr

    sl "Всё будет хорошо."
    "Произнесла Славя, и закрыла глаза."

    stop ambience fadeout 1.0
    play sound sfx_bus_interior_moving fadein 2.5 volume 0.7 loop

    "Автобус тронулся."
    "..."

    window hide

    show blink

    pause(1.5)

    hide sl
    hide blink
    show unblink
    
    pause(1.0)

    show sl pioneer smile2 close at cright
    with dspr

    pause(1.5)

    show blink

    pause(1.5)

    hide sl
    show bg int_bus_people_sunset

    call set_time("sunset")

    hide blink
    show unblink
    
    pause(1.0)

    show sl pioneer smile close at cright
    with good_dspr

    window show

    "Мы ехали уже довольно долго, пару часов."

    stop music fadeout 2.5

    "Всё это время Славя отвлекала меня разговорами, и надо сказать, довольно успешно."

    pause(1.0)

    play music "<from 40.0>" + music_list["into_the_unknown"] fadein 1.5 volume 0.8

    "Я почти перестал мандражировать."
    
    hide sl with long_dspr

    "Но вскоре она уснула, и я остался один на один со своими мыслями."
    "Я смотрел в окно, но дорога всё не заканчивалась, бесконечно петляя среди степей, которые перемежались лесами."
    "Не было ни намёка на хоть какой-то населённый пункт."
    "Я вспомнил записку, которую нашел на телефоне."
    th "Ты здесь не просто так."

    play sound2 sfx_head_heartbeat fadein 1.0 volume 0.77 loop

    "Эта фраза отчётливо долбила у меня в голове вновь и вновь, я повторял её про себя как мантру, пытаясь понять, может я что-то упустил?"
    "Недопонял, или не обратил на что-то внимания?"
    "..."

    stop sound2 fadeout 1.0

    "Но в слова чокнутого пионера я по-прежнему отказывался верить."
    "Лагерь, и все его обитатели точно были настоящими. {w}Живыми."
    "..."

    window hide

    call set_time("night")

    show bg int_bus_people_night with dissolve1

    window show

    "Вскоре начало темнеть, а мы всё ехали."
    "Начало клонить в сон."
    "Славя пару раз просыпалась, но перебросившись парой фраз, быстро засыпала снова."
    th "Наверное, тоже вымоталась со всеми этими переживаниями."
    "Я опёрся лбом о холодное стекло, и вглядывался вдаль, борясь со сном."
    "Я хотел своими глазами увидеть, что меня ждёт…"

    show blink

    pause(1.0)

    hide blink
    show unblink

    "Но организм был не согласен."
    "Всё чаще я кивал головой, но тут же вздрагивал, этого хватало ещё на пару минут."

    stop sound fadeout 3.0
    stop music fadeout 3.0

    "Пока в конце концов усталость не взяла своё, и я не заснул…"

    window hide

    show blink

    $ renpy.pause(2.5, hard=True)

    jump simple_happiness_mod_epilogue


# Эпилог
label simple_happiness_mod_epilogue:
    $ renpy.block_rollback()

    $ backdrop = "epilogue"
    $ new_chapter(9, u"Простое Счастье. Эпилог")

    call set_time("night")

    $ set_mode_adv()
    
    show bg ext_camp_entrance_night
    show prologue_dream
    hide blink
    show unblink
    with dissolve5

    play music music_list["sparkles"] volume 0.8 fadein 5.0

    hide unblink

    "Мне снился сон."
    "Я стоял перед воротами Совёнка, но вокруг была ночь."
    "Всё было как в тумане."
    "Разум медленно, словно старый процессор, обрабатывал информацию, порционно выдавая результаты того, что я вижу."
    "И я не мог пошевелиться."
    "Точнее, не мог понять, как пошевелиться. Я словно разучился управлять своим телом."
    "Но было спокойно."
    "Внезапно я понял, что ни мне, ни Славе ничего не угрожает."
    "Славя…"
    "Интересно, где она сейчас?"

    play sound sfx_head_heartbeat fadein 1.0
    queue sound "<from 0.0 to 3.0>" + sfx_head_explode

    "Славя…"
    "Что-то меня смущало…"
    th "{i}Ты здесь не просто так.{/i}"
    "Что же не так?"

    window hide

    stop music fadeout 2.0

    play sound sfx_hell_alarm_clock fadein 0.5

    hide prologue_dream
    show anim prolog_15
    with dissolve

    call set_time("prolog")

    call flashing(1.5)

    show anim prolog_14
    with dissolve2

    call flashing(1.5)

    $ renpy.pause(1.0, hard=True)

    stop sound fadeout 1.0

    window show

    "Я медленно открыл глаза."
    "Передо мной всё плыло, я не мог сфокусировать зрение."
    
    pause(1.0)

    me "Что за…"
    "Я сел на кровати, и начала потирать глаза."

    hide anim
    show bg semen_room
    with dissolve1

    "Постепенно, зрение вернулось ко мне, и я посмотрел на свою комнату."
    "Тут всё было как и раньше."
    th "Ну конечно, а что могло поменяться за одну ночь?"

    pause(1.0)

    me "За одну ночь…"

    play music music_list["just_think"] fadein 1.0 volume 0.5
    play sound sfx_head_heartbeat loop

    pause(1.5)

    th "СТОП!"
    "Сердце бешено заколотилось, а перед глазами начали мелькать картинки из лагеря…"
    "Я начал дергаться на кровати, поворачиваясь то в одну, то в другую сторону, пока не отвернулся к стене, и…"

    stop music fadeout 1.0

    show cg epilogue_uv_sl with dissolve1

    play music music_list["sparkles"] fadein 1.0

    "Увидел рядом с собой… {w}Славю."
    "Она лежала на кровати обнажённая, укрытая лишь одеялом."
    "Я долгое время просто смотрел на неё, и моргал."
    "Сразу я вспомнил всё…"
    "Как попал в Совёнок, все свои дни там, Славю… Любовь, музыкальный клуб, лес…"
    "Я смотрел и не мог пошевелиться, боялся спугнуть её, словно это было наваждение."
    "Наконец я сглотнул вязкую слюну, и пошевелил Славю за плечо."

    stop sound fadeout 1.0

    me "Сл… {w}Славя! {w}Славя, проснись!"
    th "Я вообще не понимаю, что происходит…"
    "Пронеслось в голове."
    "Девушка нежно потянулась на кровати, и открыв глаза, посмотрела на меня."

    pause(1.0)

    "Несколько секунд у неё ушло на то, чтобы спокойствие в её глазах сменилось непониманием, а потом страхом."

    stop music fadeout 1.0

    hide cg
    show sl naked scared close at right
    with dissolve1

    play music music_list["just_think"] fadein 1.0 volume 0.5

    sl "А-а!"
    sl "Ты кто!?"
    sl "Где я!?"

    hide sl
    show sl naked scared close at fright
    with good_dspr

    "Славя отползла к стене."
    "Мы оба смотрели друг на друга испуганными глазами."
    me "Славя, это.., {w}это я, Семён!"

    hide sl
    show sl naked scared close at cright
    with good_dspr

    "Я сел ровно перед ней, но приближаться не стал."

    pause(1.0)

    "Она смотрела на меня несколько секунд, после чего, видимо узнала меня, и переменилась в лице."

    show sl naked surprise close with long_dspr

    "Только сейчас я понял, что скорее всего, опять выгляжу на все свои двадцать пять."
    sl "С-семён? {w}Я тебя не узнала!"

    "Она подобралась ко мне, и обняла."

    show sl naked tender close with good_dspr

    "Я ответил на её объятие, и поцеловал её."

    show sl naked surprise close with good_dspr

    sl "Я так испугалась!"
    sl "Я помню, что заснула в автобусе, а потом…"
    sl "Провал. {w}И я просыпаюсь тут…"
    sl "А... А где мы?"

    stop music fadeout 2.0

    "Я выдохнул, поняв, что произошло, и что сейчас нас ждёт очень серьёзный разговор."
    me "Давай сначала найдем тебе какую-нибудь одежду, и нальём кофе."

    hide sl with good_dspr

    play music "<from 3.0>" + music_list["afterword"] fadein 2.0 volume 0.78

    call to_nvl_mode

    "Сидя на кухне, я рассказал Славе, всё как есть."
    "О том, что мне уже 25 лет, что я попал в Совёнок каким-то непонятным образом, и что мы с ней сейчас у меня в квартире в современной России, а не в Советском Союзе."
    "Славе, конечно, верилось с трудом во всё происходящее."
    "Но когда она выглянула в окно, и когда я показал ей приборы, которых в её время ещё не существовало, она во всём убедилась."
    "Конечно, она очень сильно испугалась. {w}В первую очередь, за своих родителей, ведь разрыв во времени получался не меньше тридцати лет, и могло статься так, что они уже умерли."
    "В какой-то момент она расплакалась у меня в объятиях от осознания происходящего."
    "Я как смог, успокоил Славю, сказав что не стоит загадывать наперёд, и что мы обязательно во всём разберёмся."
    nvl clear
    "А Славя, как я и предполагал, действительно родилась и выросла в Советском Союзе, и была в пионерлагере Совёнок, где и встретила меня."
    "Немаловажным было и то, что у кровати мы обнаружили сумку, с которой Славя уезжала из лагеря."
    "Помимо пионерской формы, все остальные вещи там были другие."
    "Среди кучи бумаг, в которых было свидетельство о рождении, ИНН, СНИЛС, аттестатах об окончании девятого и одиннадцатого классов, обнаружился и паспорт."
    "Судя по информации оттуда, Славяна Ясенева, а именно так была указана её фамилия, родилась уже в этом веке. {w}Начиная с пропечатанной даты рождения, получалось, что ей совсем недавно исполнилось восемнадцать лет."
    nvl clear
    "Мы оба были в недоумении касательно того, как всё это произошло, и что делать дальше."
    "Но, по крайней мере были счастливы в одном. Исполнилось то, чего мы в лагере желали больше всего. Мы были вместе."
    "Поэтому, оставалось решить лишь бытовые «мелочи» …"
    nvl clear

    nvl hide dissolve
    $ renpy.pause(1.0, hard=True)
    call to_nvl_mode

    "Прошёл месяц."
    "После похода по нескольким государственным инстанциям, мы убедились, что все её документы подлинные, но следов её родителей так и не нашли. Их как будто никогда и не существовало в нашем мире."
    "Ни в одном паспортном столе, ни в одном отделении МФЦ, ни где-либо ещё не было информации о людях с фамилиями, именами и отчествами, которые она называла."
    "\nМы много обсуждали, что же всё-таки могло произойти, и как так получилось."
    "Какие версии мы только не рассматривали. От параллельных миров, до путешествия во времени. От какого-то секретного эксперимента, до парных галлюцинаций."
    "Ответа, конечно, мы так и не нашли."
    "Но, по крайней мере Славя успокоила себя насчёт родителей."
    "Да и мы оба были уверены, что с ними всё хорошо, просто они остались там, в «мире Совёнка», как мы его называли."
    nvl clear
    "Также, одной из проблем стала адаптация Слави к современному миру."
    "Хотя говорила она без акцента, и быстро схватывала новые технологии, ей всё равно было тяжело, как человеку из двадцатого века."
    "А вот моей основной проблемой стал заработок денег. Ведь теперь мне приходилось кормить не только себя, но и Славю."
    "Поэтому, пришлось устраиваться на две подработки сразу. Славя, конечно, хотела помогать, но я настоял на том, что пока она полностью не освоится в нашем мире, ни о работе ни об учёбе ей думать не стоит."
    "Она не стала спорить, поэтому взяла на себя домашние обязанности, пока я был на работе."
    "Но это не значит, что она совсем не социализировалась."
    "Напротив, первые дни мы вместе выходили в магазины, а вскоре, разобравшись с пластиковыми картами и кассами самообслуживания, она стала ходить в них сама."
    "Также, мы часто старались выбраться куда-нибудь. Денег на развлечения у нас не было, так что устраивало и просто доехать на автобусе до центра, и погулять пешком."

    stop music fadeout 3.0

    call to_adv_mode

    window hide

    pause(2.0)

    call set_time("sunset")

    show bg int_semen_room_evening with dissolve1

    play music music_list["dance_of_fireflies"] fadein 2.0 volume 0.8

    window show

    "..."

    play sound sfx_open_door_1

    "И вот, вернувшись домой в один из дней, я зашёл в квартиру, и сказал."
    me "Славя, я дома!"

    show sl civil smile at left
    with half_good_dspr

    "Девушка подбежала ко мне, и обняв, поцеловала."
    sl "Ну наконец-то, я уже заждалась!"
    "Я виновато улыбнулся, и ответил."
    me "Автобус задержался."
    sl "Давай раздевайся, и я тебе такое покажу! В интернете сегодня нашла."
    "Я с интересом посмотрел на Славю."
    th "Что же она там такое нашла?"

    hide sl
    show sl civil normal at right
    with good_dspr

    "Я разулся, скинул куртку, и подошел к Славе, которая уже сидела за компьютером."
    sl "Смотри!"

    play sound sfx_computer_noise fadein 0.5 loop

    hide sl
    show cg ep_pc_mi
    with dissolve

    "Я посмотрел на экран, и увидел открытую вкладку видеохостинга, в видео на котором была…"
    me "Мику?"
    "Озвучил я вслух."
    "Славя сидела на стуле, поджав ноги, и ответила."
    sl "Значит, мне не показалось… {w}Это и правда она!"
    th "Подождите-ка, голос Мику мне сразу показался знакомым."
    th "Ну точно! Вот, кого он мне напоминал. Хатсуне Мику, певицу из Японии."
    "Я озвучил эту мысль Славе."

    stop sound
    queue sound sfx_computer_noise volume 0.5 loop

    hide cg
    show sl civil normal at right
    with dissolve

    sl "Ну и что ты думаешь? Это простое совпадение, или…"
    me "Ну, наверное… Скажем так, {b}она{/b}..."
    "Я показал пальцем на монитор."
    me "... точно не была в Совёнке."
    me "Ведь я знал про неё ещё до попадания туда..."
    me "Но, может она что-то знает?"
    sl "А откуда она тогда может знать?"
    "Решив, что проще всего будет не гадать, а спросить напрямую, мы вместе составили небольшое электронное письмо на английском языке."
    "После чего направили его на её личную почту, благо адрес ящика был известен в интернете."
    me "Ну вот, готово. Теперь остаётся только ждать."

    show sl civil smile with dspr

    sl "Ты пока не голодный? Ужин готов, но у меня есть идея, как можно скрасить ближайшие полчаса."

    hide sl
    show sl civil smile at cright
    with dspr

    "Славя развернулась на стуле, и взяв мою руку, потянула меня за собой на кровать."
    "Я улыбнулся, смотря ей в глаза, и ответил."
    me "Я с удовольствием потерплю."
    "Мы вдвоём упали на кровать, и сплелись в страстном поцелуе."

    stop music fadeout 2.0
    stop sound fadeout 1.0

    "..."

    hide sl with good_dspr

    call to_nvl_mode

    play music music_list["so_good_to_be_careless"] fadein 2.0 volume 0.8

    "Спустя примерно неделю, мы получили ответ от Мику…"
    "Это был обычный вечер, когда я сидел за ПК, и ни то просматривал хорошие вакансии, ни то просто серфил различные хостинги, а Славя лежала на кровати и читала книгу."

    play sound sfx_icq_msg volume 0.55

    "Внезапно, в правом нижнем углу высветилось уведомление от электронной почты."
    "Я хотел было по привычке нажать на крестик, но мой взгляд зацепился за поле Отправитель:"
    "{font=mods/simple_happiness_mod_efim/gui/fonts/NotoSansJP-Regular.ttf}初音ミク{/font} (Hatsune Miku)"
    "А рядом стояла галочка, подтверждающая, что аккаунт подлинный."
    "Я тут же крикнул Славю, сказав что Мику ответила."
    "Она подошла к монитору, и мы начали читать. На удивление, написано было на русском, но переводили явно машинным способом."
    nvl clear
    "«Друзья, Семён и Славя!"
    "Извините за такое долгое ожидание. Я не сразу заметила ваше письмо."
    "Я сама не знаю, как это получилось, но когда вы описали лагерь пионеров, и всё что там было, я сразу поверила. Потому что недавно я видела сон, в котором всё это было!"
    "Я надеюсь, у вас всё хорошо. Если вам нужна будет любая помощь, пожалуйста, пишите сюда."
    "Я не знаю, когда мне ждать ближайшего концерта в России, но когда он будет, мы обязательно встретимся. После сна я очень хочу попасть в ваши Столовая! Там было вкусно!"
    "Всегда Ваша, Хатсуне Мику."
    "\nP.S. Семён, я надеюсь ты не бросил игру на гитаре!?»"
    nvl clear
    "Мы прочитали письмо, и умилились."
    "Мы тут же написали ответ, с благодарностью за предложенную помощь, и ожиданием очной встречи. Принимать от Мику материальную помощь, или нет, мы решили ещё обсудить."
    "После того, как обратное письмо было отправлено, Славя откинулась на стуле, и сказала."

    call to_adv_mode

    show sl civil smile at right
    with good_dspr

    sl "А Мику права, Сёма!"
    sl "Я помню, что у тебя отлично получалось играть на гитаре."
    sl "Не хочешь продолжить?"
    me "Честно говоря, во всей этой суматохе я и забыл про неё."
    me "Но давай попробуем!"
    "..."
    "Мы сели на кровать, я взял инструмент, и мы провели остаток вечера, под гитару."
    "Я пробовал играть разные композиции, и убедился, что мне точно нужно продолжать заниматься."
    "Это будет отличным хобби, да и Славе очень нравится, когда я играю."

    stop music fadeout 2.0

    "..."

    hide sl with dspr

    call to_nvl_mode

    play music "<from 3.0>" + music_list["afterword"] fadein 2.0 volume 0.83

    "В конечном итоге, прошло ещё полгода."
    "Мы всё-таки решили принять помощь от Мику, но использовать её по уму."
    "Я остался только на одной подработке, чтобы у меня было больше времени, и часть денег, которые нам прислала Мику, мы пустили на моё обучение."
    "Я купил четырёхмесячный онлайн-курс по веб-разработке, и уже через три, брал первые офферы и получал с них деньги."
    "Пока что они были не великие, но я был безмерно рад, да и Славя тоже, что я теперь зарабатываю деньги, не хренача своё здоровье на подработках, а умственным трудом."
    "По окончанию курса, и получению диплома, я уволился и с первой подработки, посвящая всего себя Славе, и своей, теперь уже основной деятельности."
    "Так как у меня появилось больше свободного времени, мы со Славей стали больше гулять, и в целом, проводить времени вместе."
    "В современном мире она уже почти полностью освоилась, что ни могло не радовать."
    "А как только открылась приёмная комиссия в Петербургский Аграрный Университет, сразу подала все документы на поступление. Как и хотела, она поступила по направлению Агрономия. Уже этой осенью она начнёт учиться на первом курсе."
    "Гитару я тоже не бросил, активно осваивая инструмент, и даже прикупил электрогитару. Всё-таки душа моя лежала к рок музыке."
    nvl clear
    "А в начале лета в моей профессиональной карьере произошло очень важное событие."
    "В интернете я наткнулся на стартап, который активно набирал любых IT-специалистов."
    "Компания уже собрала немаленький капитал, и активно разрабатывала систему полива полей при помощи дронов."
    "Этим проектом уже заинтересовались несколько довольно крупных агрохолдингов. Так что, если дело выгорит, был огромный шанс не только продать патент подороже, но и стать постоянным подрядчиком для поддержки системы."
    "Я же в этой системе занял не очень заметное, но далеко не последнее место."
    "Следуя своей полученной специальности, я занял позицию младшего разработчика со стороны сервера. Наш отдел занимался поддержкой всей сетевой архитектуры проекта, а также сайта. А учитывая постоянно возрастающий интерес, систему приходилось постоянно расширять."
    "\nВ общем, можно было сказать, что жизнь наладилась, и била ключом."
    "Когда у меня появилось больше денег, мы со Славей даже смогли организовать небольшой ремонт в нашей квартире…"

    call to_adv_mode

    play sound sfx_computer_noise fadein 1.0

    show bg int_semen_room_evening_new
    show sl civil2 smile at fright
    with dissolve1

    pause(1.0)

    sl "Сё-ём, ну где ты там?"
    me "Сейчас-сейчас!"
    "Я сидел перед монитором, и закрывал все вкладки и окна, которые мне были нужны во время работы, потягивая электронную сигарету."
    "Была уже середина лета, которого мы так ждали со Славей."
    "Мы много гуляли, особенно любили вечерком выбраться в парк неподалёку."
    "А для меня это было особенно полезно, так как я много времени проводил перед монитором."

    hide sl
    show sl civil2 smile2 at right
    with long_dspr

    "Наконец, я выключил ПК, и подойдя ко входной двери, начал обуваться."

    stop music fadeout 2.0

    "На пороге меня ждала Славя."

    hide sl
    show cg ext_city_sunset
    with dissolve1

    play ambience ambience_ext_road_evening fadein 1.0
    play music music_list["forest_maiden"] fadein 2.0 volume 0.7

    "Мы вышли из дома, и взявшись за руки, пошли по городу."
    "Я мысленно усмехнулся."
    "В Совёнке мы бы постоянно ловили на себе взгляды, а здесь, в декорациях большого города, мы были никому не интересны. И в этом было своё счастье."
    "Мы были одной из многих влюблённых пар, гуляющих вечером по городу."
    "..."

    stop ambience fadeout 1.0

    show cg ep_me_sl_park with dissolve1

    play ambience ambience_camp_center_evening fadein 1.0

    "Наконец, мы зашли в парк."
    "Уже начинало темнеть, и двигаясь по довольно узкой тропинке, Славя обвила мою руку, и прижалась ко мне."
    "Мы были вместе уже полгода, но каждый раз это было как в первый."
    "Чувство лёгкости, когда мы вместе."
    "Безмятежности, и абсолютного счастья, сопряжённое с физическим влечением."
    "Это самый дурманящий опиум, который только можно себе представить."

    $ renpy.pause(1.0, hard=True)

    show cg ep_summer_walk with dissolve1

    "Наконец, зайдя глубже в парк, мы сели на траву, и стали обсуждать ближайшие планы."
    "Вспомнили, что Мику как раз должна приехать с концертом в конце лета."
    "Подумали о том, что было бы неплохо сходить в поход на пару дней, ведь мы оба любили природу."
    "У меня всплыло, что осенью я хочу взять отпуск, и отучиться на водительские права."
    "И наконец, мы просто понимали, что были счастливы друг с другом."
    "Я поцеловал Славю, и ещё по меньшей мере полчаса мы просто сидели рядом, чувствовали тепло и любовь друг друга."
    "И ощущение, что дальше всё будет только лучше."

    $ renpy.pause(2.0, hard=True)

    call to_nvl_mode

    stop music fadeout 5.0

    "Не у каждой истории есть свой конец."
    "Каким-то суждено повторяться раз за разом."
    "Каким-то, закончиться, не успев начаться."
    "А наша со Славей история на этом только начиналась."
    "Мы прошли первую главу, а впереди нас ждала ещё целая жизнь."
    "И мы были уверены, что на следующих страницах нашей книги нас ждёт только лучшее."
    "Ведь там мы были вдвоём."
    "А значит, что бы ни случилось..."
    "Мы будем счастливы."

    nvl hide dissolve1

    $ renpy.pause(2.0, hard=True)

    show black with dissolve

    stop ambience fadeout 1.5

    $ renpy.pause(2.0, hard=True)
    $ renpy.movie_cutscene("mods/simple_happiness_mod_efim/images/vid/simple_happiness_outro.webm")