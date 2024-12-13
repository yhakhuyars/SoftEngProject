#characters
define char_mc = Character("[povname]", color="00A2FF", image='i_mc', callback=name_callback, cb_name='mc')
define char_fmc = Character('Miyagi', color="FFA680", image='i_fmc', callback=name_callback, cb_name='fmc')
define char_cmc = Character('Himeno', color="c8ffc8", image='i_cmc', callback=name_callback, cb_name='cmc')
define char_bk = Character('Bookstore Owner', color="9fe3da", image='i_bk', callback=name_callback, cb_name='bk')
define char_clerk = Character('Store Clerk', color="9fe3da", image='i_clerk', callback=name_callback, cb_name='clerk')
define char_t = Character('Teacher', color="9fe3da", image='i_t', callback=name_callback, cb_name='t')
define char_cls1 = Character('Classmate 1', color="9fe3da", image='i_cls1', callback=name_callback, cb_name='cls1')
define char_cls2 = Character('Classmate 2', color="9fe3da", image='i_cls2', callback=name_callback, cb_name='cls2')
define char_cls3 = Character('Classmate 3', color="9fe3da", image='i_cls3', callback=name_callback, cb_name='cls3')
define char_cls4 = Character('Classmate 4', color="9fe3da", image='i_cls4', callback=name_callback, cb_name='cls4')
define char_fclerk = Character('Girl', color="FFA680", image='i_fmc', callback=name_callback, cb_name='fmc')

#images

image i_mc old_normal = At('mc_old_neutral', sprite_highlight('mc'))
image i_mc old_disturbed = At('mc_old_disturbed', sprite_highlight('mc'))
image i_cmc normal = At('miyagi_normal', sprite_highlight('cmc'))
image i_cmc sad = At('miyagi_sad', sprite_highlight('cmc'))
image i_cmc annoy = At('miyagi_annoy', sprite_highlight('cmc'))
image i_cmc smile = At('miyagi_smile', sprite_highlight('cmc'))
image i_fmc office = At('miyagi_office', sprite_highlight('fmc'))
image i_bk normal = At('5_normal', sprite_highlight('bk'))
image i_bk thinking = At('5_thinking', sprite_highlight('bk'))
image i_bk mysterious = At('5_mysterious', sprite_highlight('bk'))

transform size_normal:
    ysize 1000
    fit "contain"

transform size_close:
    ysize 1400
    fit "contain"

transform size_far:
    ysize 800
    fit "contain"

init: 
    transform flip: 
        xzoom -1.0

image splash_anim_1:

    "gui/renpy-logo.png"
    xalign 0.5 yalign 0.5 alpha 0.0
    ease_quad 7.0 alpha 1.0 zoom 2.0

default persistent.firstlaunch = False

label splashscreen:
    
    scene black

    ## Here begins our splashscreen animation.
    show splash_anim_1
    #show text "{size=100}NOKOTECH {/s}":
        #xalign 0.5 yalign 0.8 alpha 0.0
        #pause 2.0
        #linear 1.0 alpha 1.0

    play sound "audio/nokotech.mp3"
    
    ## The first time the game is launched, players cannot skip the animation.
    if not persistent.seen_splash:
        
        ## No input will be detected for the set time stated.
        ## Set this to be a little longer than how long the animation takes.
        $ renpy.pause(5.5, hard=True)
 
        $ persistent.seen_splash = True
    
    ## Players can skip the animation in subsequent launches of the game.
    else:
 
        if renpy.pause(5.5):
 
            jump skip_splash

    scene black
    with fade
 
    label skip_splash:
 
        pass
    
    return

label start:

    #jump prologue
    jump prologue

    