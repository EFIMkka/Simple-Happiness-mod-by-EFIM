default card_game_d2_win = False # Сохранение результатов карточной игры во втором дне

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
    image flickering noise1 = "mods/simple_happiness_mod_efim/images/anim/simple_happiness_flickering1.png"
    image flickering noise2 = "mods/simple_happiness_mod_efim/images/anim/simple_happiness_flickering2.png"
    image flickering noise3 = "mods/simple_happiness_mod_efim/images/anim/simple_happiness_flickering3.png"
    image fullscreen_flickering noise1 = "mods/simple_happiness_mod_efim/images/anim/simple_happiness_fullscreen_flickering_1.png"
    image fullscreen_flickering noise2 = "mods/simple_happiness_mod_efim/images/anim/simple_happiness_fullscreen_flickering_2.png"
    image fullscreen_flickering noise3 = "mods/simple_happiness_mod_efim/images/anim/simple_happiness_fullscreen_flickering_3.png"

    image bg prologue_backdrop = "mods/simple_happiness_mod_efim/images/backdrop/simple_happiness_prologue_backdrop.png"
    image bg prologue_monitor_cactus = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_prologue_monitor_cactus.png"
    image bg prologue_bus = "mods/simple_happiness_mod_efim/images/anim/simple_happiness_prologue_bus.jpg"
    image bg prologue_bus_ent = "mods/simple_happiness_mod_efim/images/anim/simple_happiness_prologue_bus_ent.jpg"
    image bg prologue_bus_ent2 = "mods/simple_happiness_mod_efim/images/anim/simple_happiness_prologue_bus_ent2.jpg"

    image bg ext_storage_day = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_ext_storage_day.png"
    image bg ext_storage_sunset = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_ext_storage_sunset.png"
    image bg ext_musclub_verandah_day = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_ext_music_club_verandah_day.jpg"
    image bg ext_beach_blur_sunset = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_d2_dizz.png"
    image bg ext_houses_night = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_ext_houses_night.png"
    image bg ext_house_of_sl_night = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_ext_house_of_sl_night.png"

    image bg int_warehouse_day = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_int_warehouse_day.png"
    image bg int_dining_hall_people_sunset = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_int_dining_hall_people_sunset.png"
    image bg int_musclub_mattresses_day = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_int_music_club_mattresses_day.jpg"

    image bg d1_rena_sleep = "mods/simple_happiness_mod_efim/images/bg/simple_happiness_d1_rena.jpg"

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

    image sl veryfar = "mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_1_pioneer_veryfar_normal.png"
    image sl naked smile = "mods/simple_happiness_mod_efim/images/sp/sl/simple_happiness_sl_1_naked_smile.png"

    image mt nightdress normal = "mods/simple_happiness_mod_efim/images/sp/mt/simple_happiness_mt_1_nightdress_normal.png"
    image mt nightdress sad = "mods/simple_happiness_mod_efim/images/sp/mt/simple_happiness_mt_1_nightdress_sad.png"
    image mt nightdress grin = "mods/simple_happiness_mod_efim/images/sp/mt/simple_happiness_mt_3_nightdress_grin.png"

    image dv skirt sad = "mods/simple_happiness_mod_efim/images/sp/dv/simple_happiness_dv_3_skirt_sad.png"
    image dv skirt shy = "mods/simple_happiness_mod_efim/images/sp/dv/simple_happiness_dv_3_skirt_shy.png"

    image obhod none = "mods/simple_happiness_mod_efim/images/sp/obhod/simple_happiness_obhod_0.png"
    image obhod one = "mods/simple_happiness_mod_efim/images/sp/obhod/simple_happiness_obhod_1.png"
    image obhod two = "mods/simple_happiness_mod_efim/images/sp/obhod/simple_happiness_obhod_2.png"
    image obhod three = "mods/simple_happiness_mod_efim/images/sp/obhod/simple_happiness_obhod_3.png"
    image obhod full = "mods/simple_happiness_mod_efim/images/sp/obhod/simple_happiness_obhod_full.png"

    # Инициализация звуков
    $ sfx_smoking_cigaret = "mods/simple_happiness_mod_efim/sounds/sfx/smoking_cigaret.mp3"
    $ sfx_clocks = "mods/simple_happiness_mod_efim/sounds/sfx/clocks.mp3"
    $ sfx_bicycle_falls = "mods/simple_happiness_mod_efim/sounds/sfx/bicycle_fall.mp3"
    $ sfx_bicycle_ring = "mods/simple_happiness_mod_efim/sounds/sfx/bicycle_ring.mp3"
    $ sfx_bicycle_wheels = "mods/simple_happiness_mod_efim/sounds/sfx/bicycle_wheels.mp3"
    $ sfx_mic_noise = "mods/simple_happiness_mod_efim/sounds/sfx/mic_noise.mp3"

    $ miku_song_mi_learn1 = "mods/simple_happiness_mod_efim/sounds/music/miku_song_miku_learn1.ogg"
    $ miku_song_bad_learn = "mods/simple_happiness_mod_efim/sounds/music/miku_song_bad_learn.ogg"
    $ memories_guitar_only = "mods/simple_happiness_mod_efim/sounds/music/memories_guitar_only.mp3"

    # Персонажи
    define pis = Character(name=u"Пионеры", color="#ffffff", what_color="#f1d076") # Для случаев, когда много пионеров говорят разом
    define ths = Character(name=u" ", color="#000000", what_color="#f1d076", kind=nvl, what_prefix="~ ", what_suffix=" ~") # Мысли Семёна в режиме nvl
    define me_n = Character(name=u"Семён", color="#b1ffb1", what_color="#f1d076", kind=nvl) # Семён для режима nlv
    define sl_n = Character(name=u"Славя", color="#ffd200", what_color="#f1d076", kind=nvl) # Славя для режима nlv

    # Анимация "часов"
    define clocks_in = ImageDissolve(image="mods/simple_happiness_mod_efim/images/anim/simple_happiness_clock_anim_mask.png", time=2.5, ramplen=8)
    define clocks_out = ImageDissolve(image="mods/simple_happiness_mod_efim/images/anim/simple_happiness_clock_anim_mask_back.png", time=2.5, ramplen=8, reverse=True)


# == РАБОЧИЕ ЛЕЙБЛЫ ==

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
label custom_day_screen(day_num, title):
    $ full_title = u"Простое Счастье. " + title
    show bg prologue_backdrop
    show flickering noise1 at screen_flickering
    show flickering noise2 at screen_flickering
    show flickering noise3 at screen_flickering
    with dissolve5
    $ new_chapter(day_num, full_title)
    return


# Расчет конца проигрываемого трека
label calc_music_how_much_play:
    $ track_len = renpy.music.get_duration()
    $ track_played = renpy.music.get_pos()
    $ track_left = (track_len - track_played) + 1

    return track_left


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


# Плавное размытие
transform blurring:
    blur 0.0
    linear 1.5 blur 15.0

# Плавное деразмытие
transform deblurring:
    blur 15.0
    linear 1.5 blur 0.0

# == ПОВЕСТВОВАНИЕ ==

# Стартовый лейбл. Пролог
label simple_happiness_mod_prologue:
    $ renpy.block_rollback()
    call custom_day_screen(0, "Пролог")

    $ prolog_time()
    $ set_mode_adv()

    play music music_list["farewell_to_the_past_full"] volume 0.7 fadein 5.0

    hide flickering noise1
    hide flickering noise2
    hide flickering noise3
    show bg prologue_monitor_cactus
    with dissolve3

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

    pause(1.5)

    $ renpy.movie_cutscene("mods/simple_happiness_mod_efim/images/vid/simple_happiness_intro.webm")

    jump simple_happiness_mod_day1


# День 1
label simple_happiness_mod_day1:
    $ renpy.block_rollback()
    $ backdrop = "days"
    $ new_chapter(1, u"Простое Счастье. День 1")

    $ day_time()
    $ set_mode_adv()
    $ persistent.sprite_time = "day"

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
    "Её красоту я не мог не отметить, даже трясясь от напряжения."
    "Длинные, до самых бёдер золотого цвета толстые косы, голубые, большие глаза, словно самое чистое море, в которых хотелось утонуть."
    "И фигурой её природа не то, что не обделила, даже перестаралась."
    "Не самая длинная даже по современным меркам юбка дразнящим образом открывала ноги на добрые пятнадцать сантиметров выше колена, а заправленная в неё рубашка эффектно подчеркивала прекрасного размера грудь."
    me "При-привет… Да я вот… Да."
    "Всё ещё находясь в шоке от происходящего, я не мог из себя выдавить более осмысленный ответ."
    "Девочка (девушка?) улыбнулась, и ответила."
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
    show dv pioneer2 grin
    pause(1.0)
    show dv pioneer2 grin at walk_away_left
    pause(2.0)
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

    show bg int_house_of_mt_day with dissolve1

    "Минуя внутреннее убранство домика, мой взор сразу же зацепился за девушку, сидящую за столом возле окна."

    show sl pioneer smile far at left
    show mt pioneer normal far at cright
    with good_dspr

    "Она неторопливо что-то записывала то ли в тетрадь, то ли в какой-то документ."
    slp "Ещё раз здравствуйте, Ольга Дмитриевна, я вот новенького привела, как раз ведь сегодня должен был приехать."
    mt "Да, я знаю. Ну что, {i}Семён{/i}…"
    th "Она знает, как меня зовут!??"

    show mt pioneer smile close with good_dspr

    "Девушка встала из-за стола, и выпрямившись, сделала пару шагов мне навстречу, улыбнулась, и продолжила."
    mt "Добро пожаловать! Жалко конечно, что ты задержался, но я уверена, что оставшееся время, которое ты проведешь здесь, принесёт исключительно положительные эмоции!"
    "Говорила она, как мне казалось, как типичный представитель убеждённых социалистов того времени."
    "Громкие фразы и полная уверенность в светлом будущем. {w}Хотя меня, как раз, будущее ждало очень даже туманное."
    me "Да, замечательно… {w}Только я хотел бы узнать, а где это {i}здесь{/i} находится?"
    me "А то, я, понимаете, родителям хотел написать, и-и…"

    show mt pioneer surprise
    show sl pioneer normal far at fleft
    with good_dspr

    "Вожатая непонимающе уставилась на меня."
    mt "Как это, где… {w}Ты в пионерлагере «Совёнок». Забыл, куда ехал, что ли?"

    show mt pioneer laugh with half_good_dspr
    pause(1.25)
    show mt pioneer normal far
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

    show sl pioneer smile far with good_dspr

    "В паре рядов столов от меня стояла пионерка рядом с пустым столом и махала рукой."
    th "Чёрт, как же я проглядел?"
    "С немного виноватым видом я подошёл к златовласой пионерке, и, запомнив место, мы вместе отправились получать свою пайку..."

    stop music fadeout 2.0
    play music music_list["so_good_to_be_careless"]

    show sl pioneer smile with long_dspr
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
    play music music_list["i_want_to_play"] fadein 0.75

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
    play music music_list["goodbye_home_shores"] fadein 2.0

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
    play music music_list["silhouette_in_sunset"] volume 0.7 fadein 2.0

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

    call smoking_process(with_pause=0.5)

    "Погружаясь в водоворот мыслей, я достал из кармана сигареты, и закурил."

    stop music fadeout 2.0
    play music music_list["reflection_on_water"] volume 0.5

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

    stop ambience fadeout 3.0
    play music music_list["my_daily_life"] fadein 3.0

    show bg ext_dining_hall_away_day with dissolve2

    play ambience ambience_camp_center_day fadein 3.0

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

    play music music_list["tried_to_bring_it_back"] fadein 1.5

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
    play music music_list["so_good_to_be_careless"] fadein 3.0

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
    play music music_list["reminiscences"] fadein 3.0 volume 0.4

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
    show fullscreen_flickering noise1 at screen_flickering
    show fullscreen_flickering noise2 at screen_flickering
    show fullscreen_flickering noise3 at screen_flickering
    show bg ext_bus_night
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

    hide fullscreen_flickering noise1
    hide fullscreen_flickering noise2
    hide fullscreen_flickering noise3
    show cg sleep_nothingness
    with dissolve

    "Пустоту."
    "Всеобъемлющую, всепоглощающую."
    "И такую тягучую, плотную, неприятную, от которой никак не получается освободиться…"

    stop music fadeout 5.0

    sl "Семён! {w}Семён! {w}Сёма, блин, проснись!"
    th "Что?"

    $ sunset_time()
    $ persistent.sprite_time = "sunset"

    play ambience ambience_camp_center_evening fadein 5.0 volume 0.75

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

    play music music_list["dance_of_fireflies"] fadein 3.0 volume 0.75

    "Пока мы шли, прозвучал горн, а на подходе к столовой, помимо меньшей толпы пионеров, я заметил, что начало вечереть."

    show mt pioneer normal panama with dspr

    mt "Вы пока заходите, получайте пайку, я вас отмечу. А мне надо поговорить с вожатыми других отрядов."
    sl "Хорошо."

    show mt pioneer normal panama at walk_away_left
    pause(0.75)
    hide mt with dspr

    stop ambience fadeout 2.0

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
    stop ambience fadeout 3.0

    show bg ext_dining_hall_near_sunset
    show un pioneer normal
    show sl pioneer smile
    with dissolve2

    "Мы вышли из столовой."

    play ambience ambience_camp_center_evening fadein 2.0 volume 0.75
    play music music_list["raindrops"] fadein 3.0 volume 0.7

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

    play music music_list["get_to_know_me_better"] fadein 3.0 volume 0.8

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

    stop ambience fadeout 2.0

    pause(0.5)

    show bg ext_storage_sunset
    show dv pioneer normal
    with dissolve2

    "Мы пришли к складу, в котором я днем получал одежду, и зашли немного за угол."

    play ambience ambience_forest_evening fadein 3.0

    dv "Ну, не тяни кота за одно место! {w}Доставай!"
    me "Эка ты, какая нетерпеливая! Сейчас, подожди."
    "Я достал из кармана пачку сигарет, и зажигалку. Достал одну себе и одну Алисе."

    show dv pioneer surprise with dspr

    dv "Ого! Кэмэл? {w}Ты где их достал, это ж заграничные!"
    me "Секрет фирмы, о как!"
    "Я вставил сигарету в зубы."

    show dv pioneer smile with dspr

    me "Давай я тебе подкурю."

    call smoking_process

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

    stop ambience fadeout 3.0

    hide dv
    show dv pioneer normal at right
    with long_dspr

    show bg ext_dining_hall_away_sunset with dissolve2

    "На обратном пути я переваривал информацию, которую только что узнал."

    play ambience ambience_camp_center_evening fadein 3.0

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

    stop music fadeout 1.0

    mip "Ой, привет! А я тебя раньше не видела!"
    "Я опустил взгляд."

    show mi pioneer normal far with long_dspr

    th "Так. А это что ещё за импортный пионер?"

    play music music_list["so_good_to_be_careless"] fadein 1.0 volume 0.9

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

    mi "{font=mods/simple_happiness_mod_efim/gui/fonts/NotoSansJP-Regular.ttf}私たちの音楽クラブへようこそ!{/font} (watashitachi no ongaku kurabu he yokoso!)."

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
    stop ambience fadeout 3.0

    th "Да, девочка ураган прямо. Только словесный."

    $ night_time()

    show bg ext_square_night with dissolve

    $ persistent.sprite_time = "night"

    pause(2.0)

    play ambience ambience_camp_center_night fadein 2.0 volume 0.9
    play music music_list["trapped_in_dreams"] fadein 3.0 volume 0.75

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
    stop ambience fadeout 5.0

    th "Ох, не простая вы, Ольга Дмитриевна, ох не простая."
    "..."
    "Повертев ещё пару минут в голове всякое, я начал проваливаться в сон…"

    show blink

    window hide

    pause(1.0)

    jump simple_happiness_mod_day2


label simple_happiness_mod_day2:
    $ backdrop = "days"
    $ new_chapter(2, u"Простое Счастье. День 2")

    $ day_time()
    $ set_mode_adv()
    $ persistent.sprite_time = "day"

    play music music_list["everyday_theme"] fadein 6.0 volume 0.5

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
    show mt pioneer normal panama far at fright
    with dissolve1

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
    th "~ Интересно, как я выгляжу в пионерской форме?"
    th "Наверное, просто верх идиотизма."

    stop music fadeout 2.0

    "Я подошел к зеркалу, и…"

    play music music_list["doomed_to_be_defeated"]

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

    play music music_list["confession_oboe"] fadein 3.5 volume 0.9

    "С другой стороны, так даже лучше. Будет меньше проблем, чем если бы я выглядел на свои 25."
    "..."
    th "Ладно, пора в столовую."

    show bg ext_house_of_mt_day with dissolve

    play ambience ambience_camp_center_day fadein 2.0
    play sound sfx_dinner_horn_processed

    "Выйдя из домика, я закрыл его, и тут прозвучал горн."
    th "Черт, надо поторапливаться."
    "Я быстрым шагом направился в столовую, никого не встретив по дороге."

    show bg ext_dining_hall_near_day with dissolve1

    "У входа, как обычно, толпились пионеры, заходя в помещение, но никого из знакомых я не увидел, так что, просто зашел внутрь."

    stop ambience fadeout 2.0

    show bg int_dining_hall_people_day
    show mt pioneer normal at fright
    with dissolve

    "На входе уже стояла Ольга Дмитриевна, и отмечала пионеров."

    play ambience ambience_dining_hall_full fadein 1.5

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

    stop ambience fadeout 2.0

    show sl pioneer normal at right
    with good_dspr

    show bg ext_dining_hall_near_day with dissolve

    "Закончив приём пищи, мы вышли на крыльцо, и я спросил."
    me "Ну что, есть у нас сегодня какие-нибудь планы?"
    "Не знаю от чего, но жутко хотелось себя чем-нибудь занять."

    play ambience ambience_camp_center_day fadein 2.0 volume 0.8

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

    play music music_list["sweet_darkness"] fadein 2.0

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

    hide sl
    show bg ext_clubs_day
    show sl pioneer normal at right
    with dissolve

    "Мы стояли перед зданием клубов."

    play music music_list["tried_to_bring_it_back"] fadein 3.0 volume 0.75

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

    stop ambience fadeout 2.0

    hide sl
    show bg int_clubs_male_day
    show sl pioneer normal at fright
    with dissolve

    "Мы зашли в помещение, и оказались в месте, которое принято называть «мужыцкой» берлогой."

    play ambience ambience_clubs_inside_day fadein 2.0 volume 0.95

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

    stop music fadeout 1.0

    el "Конечно подпишем! После того, как к нам в клуб вступишь!"

    show el pioneer grin
    show sh pioneer normal_smile
    with good_dspr

    play music music_list["heather"] fadein 1.0

    "Вот чёрт, кажется, эти двое настроены решительно…"
    "Но вступать в их «gachi club boy next door» совершенно не хотелось."
    "Мне кажется, они тут и без меня нормально справляются."

    sh "Конечно, нам всегда нужны молодые, сильные, мужские руки вроде твоих!"
    sh "Тебе найдется чем заняться, вот увидишь!"

    stop music fadeout 0.5

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

    stop ambience fadeout 2.0
    stop music fadeout 3.0

    hide el
    hide sh
    show bg ext_clubs_day
    show sl pioneer normal at cright
    with dissolve1

    pause(1.0)

    play sound sfx_paper_bag volume 0.8

    "Мы вышли на улицу, и Славя передала мне листок."

    show sl pioneer smile with dspr

    "Я заметил, что её сейчас как будто разорвёт от желания засмеяться."
    me "Славь, ты чего?"

    play music music_list["gentle_predator"] fadein 3.0

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

    play ambience ambience_camp_center_day fadein 2.0

    "Давно я так хорошо не смеялся, и себя не чувствовал тоже."
    "С этой девушкой не пропадёшь, однозначно."

    play music music_list["my_daily_life"] fadein 3.0 volume 0.9

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

    stop ambience fadeout 2.0

    hide sl
    show bg int_musclub_mattresses_day
    show sl pioneer normal at cleft
    with dissolve

    play ambience ambience_music_club_day fadein 3.0

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

    play music music_list["so_good_to_be_careless"]

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
    mi "{font=mods/simple_happiness_mod_efim/gui/fonts/NotoSansJP-Regular.ttf}私たちの音楽クラブへようこそ!{/font} (watashitachi no ongaku kurabu he yokoso!)."

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

    stop ambience fadeout 2.0
    stop music fadeout 3.0

    hide mi
    hide sl
    show bg ext_musclub_verandah_day
    show sl pioneer smile at right
    with dissolve1

    pause(1.5)

    show bg ext_musclub_day with dissolve

    play ambience ambience_camp_center_day fadein 2.0 volume 0.7

    "Сделав пару шагов от клуба, Славя заговорила."

    play music "<from 12>" + music_list["farewell_to_the_past_edit"] fadein 2.0 volume 0.8

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

    play ambience ambience_medstation_inside_day fadein 2.0

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

    stop music fadeout 4.0

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

    stop music fadeout 5.0

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

    stop ambience fadeout 2.0

    hide sl
    hide cs
    show bg ext_aidpost_day
    show sl pioneer normal at right
    with dissolve

    play ambience ambience_camp_center_day fadein 2.0 volume 0.75
    play music music_list["dance_of_fireflies"] fadein 2.5

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

    stop ambience fadeout 2.0
    stop music fadeout 3.0

    hide sl
    show bg int_library_day
    show sl pioneer normal at cright
    with dissolve

    'Нас встретила…'

    play ambience ambience_library_day fadein 1.5

    "А что нас должно было встретить? Библиотека, она и в Африке библиотека."

    play music music_list["your_bright_side"] fadein 3.0 volume 0.9

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

    stop ambience fadeout 2.0
    stop music fadeout 2.0

    hide sl
    show bg ext_library_day
    show sl pioneer smile at cright
    with dissolve

    me "Чем же она по ночам занимается, что днём спит."

    play ambience ambience_camp_center_day fadein 2.0 volume 0.9

    sl "Даже не знаю. Наверное, книжки читает. Мы хоть и общаемся, но не очень много."
    me "Да, девочка-загадка прям."
    sl "И не говори… {w}Ну что."

    play sound sfx_paper_bag

    "Она развернула обходной, и передала мне."

    show obhod full with dspr

    "Я взял лист, и проверил. Все поля заполнены."
    me "Фух, ну наконец-то. Спасибо большое, без тебя бы до вечера бродил!"

    play music music_list["forest_maiden"] fadein 3.0 volume 0.7

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

    stop ambience fadeout 2.0
    stop music fadeout 3.0

    play sound sfx_clocks fadein 0.5 volume 0.55

    show black with clocks_in

    show bg ext_square_day
    hide black with clocks_out

    show black with clocks_in

    show bg int_dining_hall_people_day
    hide mt
    hide black with clocks_out
    show black with clocks_in

    stop sound fadeout 2.5
    play ambience ambience_camp_center_day fadein 3.0 volume 0.8
    play music music_list["my_daily_life"] fadein 3.0 volume 0.8

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

    play music music_list["your_bright_side"] fadein 3.0
    show bg ext_houses_day with dissolve1

    "По пути я понял, что хочется курить."
    th "А ведь уже половина дня прошла, а ещё не курил. В {i}моём{/i} мире это была бы уже катастрофа."
    "Но здесь, находясь в прекрасном месте…"
    th "И в окружении прекрасных дам, да?"
    th "Что?"
    th "Это я сейчас подумал? {w}Ладно…"

    stop ambience fadeout 2.0

    "В общем да, в прекрасном месте, и вместе со Славей. Она успокаивала не хуже любой сигареты."

    show bg ext_path_day with dissolve

    play ambience ambience_forest_day fadein 3.0 volume 0.95

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

    stop ambience fadeout 2.0

    "..."

    show bg ext_house_of_mt_day with dissolve2

    stop music fadeout 3.0

    "Подходя к порогу домика, я, всё ещё погруженный в свои мысли, просто дернул за ручку и вошёл внутрь."

    play ambience ambience_int_cabin_day fadein 3.0
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

    "Я вылетел из домика."

    play ambience ambience_camp_center_day fadein 2.0

    th "Откровенно говоря, конечно, зрелище пришлось мне по нраву."
    th "Но, в любом случае, это было некрасиво."

    show mt pioneer normal at center
    with good_dspr

    "Вышла вожатая."
    mt "Семён, ну ты даёшь. {w}Всегда же стучался."
    me "Извините, я что-то… Задумался."

    show mt pioneer smile with dspr

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

    play ambience ambience_int_cabin_day fadein 2.0
    play music music_list["everyday_theme"] fadein 2.0 volume 0.72

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
    hide black with clocks_out

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

    stop ambience fadeout 2.0

    hide mt
    show bg ext_house_of_mt_day
    with dissolve

    th "Покурить бы не помешало."
    "Я задумался."
    "Судя из того, что я успел понять касательно расположения объектов в лагере, если я сейчас обогну крайний ряд домов, и пойду примерно на юго-запад, то как раз выйду к музыкальному клубу."
    "А в лесу мне никто не помешает посмолить. {w}Отлично."

    show bg ext_path_day with dissolve1

    play sound sfx_smoking_cigaret

    "Так я и сделал, и курил, идя по лесной тропинке."
    "Докурив сигарету, я потушил её и отправил окурок подальше в лес, закинул в рот жвачку, и начал прикидывать, когда поворачивать."
    "..."
    th "Ну, наверное сейчас. В любом случае не заблужусь."

    show bg ext_musclub_verandah_day with dissolve1

    "Интуиция меня не подвела."
    "Через пару минут я оказался перед зданием музклуба, только с другой стороны."
    "Обойдя его, я уже было хотел открыть дверь, но одернулся, вспомнив, как Мику меня со Славей встречала утром, и как я вломился в наш с вожатой домик."

    play sound sfx_knock_door7_polite

    "Поэтому, я, как можно более громко, но аккуратно, постучал."
    mi "Да-да, заходите!"

    show cg d5_mi with dissolve1

    stop ambience fadeout 2.0
    stop music fadeout 2.0

    "Я открыл дверь, и меня встретила Мику, которая вытирала тряпкой рояль."
    mi "Сёма! Наконец-то ты пришел."

    hide cg
    show bg int_musclub_mattresses_day
    with dissolve

    play ambience ambience_music_club_day fadein 2.0
    
    "Она оставила тряпку, и подошла ко мне."

    play music music_list["so_good_to_be_careless"] fadeout 3.0 volume 0.85

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

    stop music fadeout 1.5

    me "Я тоже рад, Мику. Ну что, начнём?"

    play music music_list["went_fishing_caught_a_girl"]

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

    pause(10.5)

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

    pause(13.0)

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
    "Честно говоря, я был довольно смущён."

    play music music_list["so_good_to_be_careless"] fadein 2.0 volume 0.95

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

    stop ambience fadeout 2.0
    stop music fadeout 2.0

    show black with clocks_in

    hide mi
    show bg ext_houses_day
    hide black
    with clocks_out

    show black with clocks_in

    $ sunset_time()
    $ persistent.sprite_time = "sunset"

    stop sound fadeout 3.0

    show bg ext_dining_hall_near_sunset
    show mi pioneer normal at cleft
    hide black
    with clocks_out

    play music music_list["dance_of_fireflies"] fadein 3.0 volume 0.85
    play ambience ambience_dining_hall_full fadein 3.0

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

    stop ambience fadeout 2.0

    hide sl
    hide mi
    hide un
    show bg ext_dining_hall_near_sunset
    show sl pioneer normal at right
    show un pioneer smile at center
    show mi pioneer normal at left
    with dissolve1

    "Мы вышли из столовой."

    show mi pioneer shocked with dspr

    mi "Ой, я же клуб не закрыла!"
    mi "Ладно, я постараюсь успеть!"

    show mi pioneer normal with dspr

    play ambience ambience_camp_center_evening fadein 3.0

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

    play music music_list["she_is_kind"] fadein 3.0 volume 0.9

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

    stop ambience fadeout 2.0

    show bg int_house_of_mt_sunset
    show mt pioneer normal at center
    with dissolve

    "Я зашёл."
    "Не зная, как начать разговор, я мялся, и начал говорить что-то не вполне внятное."
    me "Ольг Дмитрив, а я, а мы тут, это…"

    play ambience ambience_int_cabin_evening fadein 2.0

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
    pause(1.0)
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

    stop ambience fadeout 2.0
    stop music fadeout 2.0

    show bg ext_house_of_mt_sunset with dissolve

    "Я выключил свет, вышел из домика, закрыл его, и направился в сторону пляжа."
    "..."

    show bg ext_square_sunset with dissolve

    play ambience ambience_camp_center_evening fadein 2.0
    play music music_list["everyday_theme"] fadein 3.0 volume 0.7

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

    stop ambience fadeout 2.0

    show black with clocks_in

    hide mi
    hide un
    show mi pioneer normal at fright
    show un pioneer smile at cright
    show bg ext_beach_sunset
    hide black
    with clocks_out

    "И вскоре оказались на пляже."

    play ambience ambience_lake_shore_evening fadein 2.0

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
    show un pioneer normal at right
    show mi pioneer far normal at center
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

    stop music fadeout 3.0

    "Никто не возражал."
    "Секунд десять Мику потратила на то, чтобы сесть поудобнее и настроиться играть."
    "Пару раз она дернула несколько струн, после чего, приготовившись, начала играть."

    play music memories_guitar_only noloop

    pause(5.0)

    "Она играла какую-то очень красивую, но, как мне казалось, немного грустную мелодию…"

    pause(1.0)

    hide sl
    show sl pioneer tender close at left
    with dspr

    "Славя положила голову мне на плечо…"

    pause(1.0)

    hide un
    show un pioneer cry_smile at right
    with dspr

    "У Лены, кажется, намокли глаза…"

    pause(1.0)

    "Что-то очень теплое и душевное навевает эта композиция…"

    pause(1.0)

    show cg mi_guitar_yam with dissolve

    "Я посмотрел на Мику. {w}Она играла с закрытыми глазами, полностью сосредоточившись на музыке."

    window hide

    call calc_music_how_much_play

    pause(_return)

    stop music fadeout 1.0

    hide cg with dissolve

    window show

    hide mi
    show mi pioneer smile at center
    with good_dspr

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

    un "Мику, очень красиво! А она как-нибудь называется?"
    mi "Да. Я назвала её «Воспоминания». Это воспоминания о моей родине."
    sl "Ты её ещё и сама сочинила? Очень здорово!"
    "Ещё обменявшись любезностями, и порасспрашивав Мику о песне, мы переключились на другую тему."

    play music music_list["sweet_darkness"] fadein 2.5 volume 0.85

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

    show bg ext_beach_sunset with dissolve1

    show un pioneer smile at deblurring
    hide un
    show sl pioneer smile at left
    show mi pioneer normal at right
    show un pioneer smile at center
    with long_dspr

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
    $ game_starts_r1 = False

    window show

    show bg ext_beach_sunset with None
    show un pioneer normal at right
    with dspr

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
    $ game_starts_r1 = False

    window show

    show bg ext_beach_sunset with None
    show un pioneer normal at right
    with dspr

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
    window show

    show bg ext_beach_sunset with None
    show un pioneer normal at center
    with dspr

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
    $ game_starts_r2 = False
    $ card_game_d2_win = True

    window show

    show cg d2_cards_scheme_r2_me_win
    with dissolve

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
    pause(1.0)

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
    $ game_starts_r2 = False

    window show

    show cg d2_cards_scheme_r2_sl_win
    with dissolve

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
    window show

    show bg ext_beach_sunset with None
    show sl pioneer smile at center
    with dspr

    me "Как это? Ничья?"
    sl "Переигрываем!"
    me "Полностью поддерживаю!"
    mi "Конечно. Время ещё есть, а мы должны определить победителя сегодняшней встречи!"

    call simple_happiness_mod_d2_card_game_r2


label simple_happiness_mod_day2_continue:
    $ renpy.block_rollback()
    stop music fadeout 2.5

    hide cg
    hide sl
    hide mi
    hide un
    show bg ext_beach_sunset
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

    $ night_time()
    $ persistent.sprite_time = "night"

    hide sl
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

    stop ambience fadeout 3.0

    show black with clocks_in
    hide mi
    hide sl
    hide un
    show bg ext_houses_night
    show un pioneer normal at fleft
    show mi pioneer normal at cleft
    show sl pioneer normal at right
    hide black
    with clocks_out

    play ambience ambience_camp_center_night fadein 3.0

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

    stop music fadeout 3.0

    show black with clocks_in
    show bg ext_house_of_mt_night_without_light
    hide black
    with clocks_out

    play music music_list["goodbye_home_shores"] fadein 2.0 volume 0.75

    stop ambience fadeout 1.0

    "Сделав несколько поворотов, я оказался перед нашим с вожатой домиком."
    "Свет был выключен."

    show bg int_house_of_mt_night2 with dissolve

    play ambience ambience_int_cabin_night fadein 1.0 volume 0.8

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

    stop music fadeout 5.0
    stop ambience fadeout 3.0

    nvl clear
    "Постепенно я начал засыпать."
    "А мысли так и продолжили крутиться вокруг девушки с золотыми волосами и глазами голубого цвета, как самое чистое на свете море. {w}В которых хотелось утонуть."

    jump simple_happiness_mod_day3


label simple_happiness_mod_day3:
    $ renpy.block_rollback()
    $ backdrop = "days"
    $ new_chapter(3, u"Простое Счастье. День 3")

    $ day_time()
    $ set_mode_adv()
    $ persistent.sprite_time = "day"

    play ambience ambience_int_cabin_day fadein 3.0 volume 0.9

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

    play ambience ambience_dining_hall_full fadein 1.5

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

    $ sunset_time()
    $ persistent.sprite_time = "sunset"

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

    $ night_time()
    $ persistent.sprite_time = "night"

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

    pause(1.0)

    jump simple_happiness_mod_day4


label simple_happiness_mod_day4:
    $ renpy.block_rollback()
    $ backdrop = "days"
    $ new_chapter(4, u"Простое Счастье. День 4")

    $ day_time()
    $ set_mode_adv()
    $ persistent.sprite_time = "day"

    play ambience ambience_int_cabin_day fadein 3.0 volume 0.9
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

    show bg ext_dining_hall_near_day with dspr

    "{i}Сегодня на улице Ленина ничего не произошло.{/i}"

    play ambience ambience_camp_center_day fadein 1.0

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