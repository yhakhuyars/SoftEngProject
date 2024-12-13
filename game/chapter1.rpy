


label chapter1:

    stop music

    scene black with dissolve

    show text "Chapter 1" at truecenter with dissolve
    pause 1.0
   
    scene black with dissolve

    "A part-time job in blazing heat."

    "After deeply bowing my head with the eleventh 'I’m really sorry of the day' it seems I had a dizzy spell and fell unconscious."

    play sound "audio/sfx/Interior-Door_Close.mp3"

    scene bg room_day

    char_mc "(The manager sent me a text telling me to rest, but I don’t think I’ll be hearing back from him tomorrow.)"

    char_mc "(and I don't have anything to eat for tonight.)"

    char_mc "..."

    char_mc "(My wallet is empty as well.)"

    char_mc "I guess I don't have a choice."

    char_mc "Like it or not, I need money for food."

    char_mc "(Parting with my CDs and books made my heart ache.)"

    char_mc "(They were all second-hand, purchases I’d made with careful considerations.)"

    char_mc "(But my room lacked even a computer or a TV. By now, my CDs and books seemed the only things left that could get me any money.)"

    char_mc "(With a heavy heart, I packed it up in a bag and went outside in the scorching heat.)"

    play sound "audio/sfx/footsteps.mp3"

    scene black with dissolve
    pause 3.0

    scene bg library

    play sound "audio/sfx/Interior-Door_Close.mp3"

    play music "audio/bgm_library.mp3"

    char_bk "Good afternoon. Your name is [povname] right? "

    show i_bk normal at size_normal, right
    with dissolve

    char_bk "Anything I can help you with?"

    show i_mc old_normal at left, flip, size_normal
    with dissolve

    char_mc "Hello, I'm here to sell some books"

    char_bk "…."

    char_bk "Are you moving or something?"

    show i_mc old_disturbed

    char_mc "No. Nothing like that."

    char_bk "Well then, why do something so wasteful?"

    show i_mc old_normal

    char_mc "Well, paper doesn’t make for a good meal. Not much nutritional value."

    show i_bk thinking

    char_bk "Short on cash, eh… it’ll take a few minutes to evaluate your books."

    char_mc "Thanks, I'll wait here."

    char_mc "(With that, I meandered around the store browsing the shelves)"

    hide i_bk
    with dissolve
    hide i_mc
    with dissolve

    "The shelves are fully stacked with rows and rows of books."

    "You recognize a few of the titles such as the classic  \"How to kill a Mockingbird\" "

    "While looking through the shelves, you heard the bookkeeper call your name."

    show i_bk normal at size_normal, right
    with dissolve

    char_bk "Here you go."

    show i_mc old_normal at left, flip, size_normal
    with dissolve

    char_mc "(He handed me the cash for my books, )which I figured should last me days at most.)"

    char_bk "Hey."

    show i_bk mysterious

    char_bk "I’ve got something to tell you about."

    menu:
        "Ignore":
            char_mc "…"
        "What is it?":
            char_mc "What is it?"

    char_bk "You’re strapped for cash right?"

    show i_mc old_normal

    char_mc "…"

    char_mc "It’s not like it’s anything recent."

    show i_bk normal

    char_bk "Well, I don’t care how poor you are, or why things got that way. That’s not my interest."

    char_bk "I just wanna ask you one thing."

    show i_bk mysterious

    char_bk "You wanna sell some of your lifespan?"

    char_mc "…"

    show i_mc old_disturbed

    char_mc "What."

    show i_bk normal

    char_bk "Yeah, lifespan. Oh, but, it’s not like I’m the one buying it."

    char_bk "I know it sells for a lot though."

    char_mc "…"

    char_bk "Can’t blame you if you think I’m joking. Or thinking that this old coot’s gone senile."

    char_bk "But if you want to entertain my nonsense, go take a look, I’ll tell you where. You’ll see I’m not lying."

    stop music fadeout 0.5

    scene black with dissolve

    play music "audio/bgm_think.mp3"
    
    # Kusonoki's thoughts
    char_mc "(In short, this is what he told me.)"
    char_mc "(On the fourth floor of a nearby building, is a shop that buys lifespan.)"
    char_mc "(It differs from person to person.)"
    char_mc "(“How rich would the life you would have lived been?”)"
    char_mc "(By that metric, the value can fluctuate a lot.)"

    # Flashback with the Bookstore Owner

    scene bg library with fade

    show i_bk normal at size_normal, center
    with dissolve

    char_bk "I don’t really know much at all, but you don’t look like a bad guy and you’ve got a decent taste in books. Your life must have some value right?"

    char_bk "Besides lifespan, apparently they’ll buy 'time' and 'health' too."

    menu:
        "What's the difference?":
            char_mc "What’s the difference between lifespan and time?"

        "That's crazy talk.":
            char_mc "What are you saying man."
    show i_bk thinking

    char_bk "Couldn’t tell you any details. It’s not like I’ve ever sold any of it."

    scene black with fade

    char_mc "(A shop dealing in lifespan… It could only be the fantasy of an old man nearing his death.)"
    char_mc "(Because, I mean… wouldn’t that just be too good to be true?)"

    stop music

    scene bg shop
    play sound "audio/sfx/Interior-Door_Close.mp3"
    play music "audio/bgm_neutral.mp3"

    # Dialogue with the CD store clerk
    char_clerk "Hello."

    char_mc "These."

    "I say as I place a dozen CDs on the counter"

    char_clerk "…"

    char_clerk "What kinda turn of events is this?"

    # Kusonoki's inner thoughts
    char_clerk "I don’t know who you are, but why let go of so many CDs?)"
    char_mc "(Its the same reaction as the old bookstore owner.)"
    menu:
        "Explain":
            char_mc "(Just like before, I explained why I had no choice but to sell them.)"
            char_clerk "In that case, I’ve got somethin’ good for you."
        "It's a long story":
            char_mc "It's a long story"
            char_clerk "Nah I think I understand."
            char_clerk "Actually, I think I can help with that!"

    char_clerk "See, the truth is, bro, I’m pretty into your taste in music!"

    char_clerk "I really shouldn’t be telling you this… But just between us, a’ight?"

    char_clerk "Here in town, there’s a shop where they’ll buy your lifespan!"

    char_clerk "In fact I sold some of mine!"

    # Kusonoki's inner thoughts
    char_mc "(Was it the trend to make fun of poor people?)"

    char_mc "So, uh… How much did it go for?"

    char_clerk "Can’t really tell you that. But tell you what, I'll tell you where it is"

    char_clerk "Here ya go."

    scene black with dissolve

    "He hands me a paper with a crude drawing of a map marking the supposed shop that buys lifespan."
    # Kusonoki's reflection
    "Needless to say, his directions perfectly matched the old man’s."

    stop music fadeout 1.0
    play sound "audio/sfx/footsteps.mp3"
    # Kusonoki's inner thoughts
    "In the end, I found myself standing in front of that building."
    

    scene bg street_night

    char_mc "(It’s not like I believed their story, I thought of it like this.)"
    char_mc "(“Circumstances kept them from saying it directly, but there was some lucrative job offered there that was at the risk of shortening your lifespan.”)"
    char_mc "(And that’s what they really wanted to share with me.)"

    scene black with dissolve

    char_mc "…."
    play sound "audio/sfx/Interior-Door_Close.mp3"
    char_fclerk "Welcome."

    scene bg office
    play music bgm_think

    char_fclerk "Your time?"

    pause 0.5

    show i_fmc office at size_normal, center
    with dissolve

    char_fclerk "Your health?"

    pause 0.5

    char_fclerk "Or your lifespan?"

    pause 0.5
#BRANCH FLAG
    char_mc ". . ."

    char_mc "… Lifespan."

    jump chapter2
