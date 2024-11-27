


label chapter1:

    stop music

    scene black with dissolve

    show text "Chapter 1" at truecenter with dissolve
    pause 1.0
   
    scene black with dissolve

    char_mc "(A part-time job in blazing heat.)"

    char_mc "(After deeply bowing my head with the eleventh 'I’m really sorry of the day' it seems I had a dizzy spell and fell unconscious.)"

    play sound "audio/sfx/Interior-Door_Close.mp3"

    scene bg room_day

    char_mc "(The manager sent me a text telling me to rest, but I don’t think I’ll be hearing back from him tomorrow.)"

    char_mc "(and I don't have anything to eat for tonight.)"

    char_mc "..."

    char_mc "(My wallet is empty as well.)"

    char_mc "I guess I don't have a choice."

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

    char_mc "Hello. I’m here to sell some books."

    char_bk "…."

    char_bk "Are you moving or something?"

    char_mc "No. Nothing like that."

    char_bk "Well then, why do something so wasteful?"

    char_mc "Well, paper doesn’t make for a good meal. Not much nutritional value."

    char_bk "Short on cash, eh… it’ll take about thirty minutes to evaluate your books."

    char_mc "(With that, I meandered around the store browsing until the owner called me over.)"

    char_mc "(He handed me the cash for my books, which I figured should last me days at most.)"

    char_bk "Hey."

    char_bk "I’ve got something to tell you about."

    char_mc "…"

    char_mc "What is it?"

    char_bk "You’re strapped for cash right?"

    char_mc "…"

    char_mc "It’s not like it’s anything recent."

    char_bk "Well, I don’t care how poor you are, or why things got that way. That’s not my interest."

    char_bk "I just wanna ask you one thing."

    char_bk "You wanna sell some of your lifespan?"

    char_mc "…"

    char_mc "What."

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

    char_bk "I don’t really know much at all, but you don’t look like a bad guy and you’ve got a decent taste in books. Your life must have some value right?"

    char_bk "Besides lifespan, apparently they’ll buy 'time' and 'health' too."

    char_mc "What’s the difference between lifespan and time?"

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

    char_clerk "…"

    char_clerk "What kinda turn of events is this?"

    # Kusonoki's inner thoughts
    char_clerk "I don’t know who you are, but why let go of so many CDs?)"
    char_mc "(Its the same reaction as the old bookstore owner.)"
    char_mc "(Just like before, I explained why I had no choice but to sell them.)"

    char_clerk "In that case, I’ve got somethin’ good for you."

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
    # Kusonoki's reflection
    char_mc "(Needless to say, his directions perfectly matched the old man’s.)"

    stop music fadeout 1.0
    play sound "audio/sfx/footsteps.mp3"
    # Kusonoki's inner thoughts
    char_mc "(In the end, I found myself standing in front of that building.)"
    

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

    char_fclerk "Your health?"

    char_fclerk "Or your lifespan?"

    pause 0.5
#BRANCH FLAG
    char_mc "… Lifespan."

    jump chapter2
