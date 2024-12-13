label chapter2:

    scene bg black with dissolve

    show text "Chapter 2" with Pause(1.5)

    scene bg office with dissolve

    show i_fmc office at size_normal, center
    with dissolve

    char_fclerk "Your evaluation will take about three hours."

    char_mc "(When they first mentioned “selling lifespan”, what immediately came to mind was a morality lesson from elementary school.)"

    stop music fadeout 1.0

    scene bg black with dissolve
    pause 1.0

    # Transition to flashback
    scene bg classroom with fade
    play music "audio/bgm_classroom.mp3"
    #window show

    # Teacher's dialogue
    char_t "You’ve all been told that it’s something that can’t be replaced,"
    char_t "And that it’s more valuable than anything."
    char_t "But if a human life were given a monetary value, how much do you think it would be worth?"

    # Himeno answers
    char_cmc "I know."
    char_cmc "A salaryman, over the course of their life, earns about 100 million to 300 million yen. That’s what I read in a book once."

    "The class’s biggest smart-aleck answered."

    # Teacher responds
    char_t "Even if you asked an adult, well…."
    char_t "You might get that same answer."
    char_t "But, for right now, I want you to get away from that line of thinking."
    char_t "So, say someone said this to you."
    char_t "“Hey. That life you’re gonna lead… Would ya let me have it all for myself?”"

    # Classmate 1's question
    char_cls1 "And what would happen if I did sell it?"

    char_t "You would die, surely."
    char_t "So of course, you’d want to refuse this offer."
    char_t "But it would keep hanging on."
    char_t "“Well, just half is fine. Wanna just sell me thirty years off the sixty you have left?”"

    # Kusonoki's thoughts
    char_mc "(I get it.)"
    char_mc "(If it went down like that, I really might feel like selling.)"

    # Teacher's follow-up
    char_t "Now, here’s the question."
    char_t "It would have to assign a per-year value to your lifespan, yes?"
    char_t "I’ll tell you in advance, but there’s no right answer. But I want to know how you came to your answer."

    # Classmate 2's response
    char_cls2 "Well, if a whole life is about 300 million yen…"

    char_mc "(If they’re 300 million… I could at least be 3 billion.)"

    # Classmate 3's reaction
    char_cls3 "You can’t assign a value to a person’s life!"

    "... said one girl with gloomy prospects."
    char_mc "(If we’re talking about the chance to live her life, yeah, I wouldn’t give that a value.)"

    # Classmate 4's joke
    char_cls4 "But if I were selling my life, you guys wouldn’t even pay 300 yen, would you?"

    "“Ha-ha-ha-ha-ha!”"

    char_mc "(The wise-cracking clown you get in every class, thought similarly to me, and had a self-deprecating laugh about it.)"

    char_mc "(As it happens, the teacher said that there was no right answer.)"
    char_mc "(But a right answer did sort of exist.)"

    scene bg black with dissolve
    pause 0.5

    stop music fadeout 2.0
    # End flashback and return to the present
    #window hide
    
    # Ten years later narration
    char_mc "(Ten years later, when I was twenty-one, I did in fact sell my lifespan and learn its value.)"

    char_mc "I hope it sells for a lot…"

    char_mc "(While waiting for the evaluation, I tried to make a low-ball estimate of how much my life was going to be.)"

    char_mc "(I was thinking, at minimum, maybe 300 million. Compared to my \"3 billion\" from when I was a kid, it was a rather modest estimate.)"

    char_mc "(However, I'd forgotten that thought I had.)"

    scene bg office with fade

    # Shop girl interaction

    play music "audio/bgm_think.mp3"

    char_fclerk "Mr. Kusonoki, your evaluation has been completed"

    show i_fmc office at size_normal, center
    with dissolve

    char_fclerk "..."

    char_mc "\"Mr. Kusonoki.\""

    char_mc "(I didn't recall ever giving them my name, or any form of identification.)"

    char_mc "(And yet, they knew it, some way or another. I guess that follows, since the business here goes beyond common sense.)"

    char_fclerk "3…"

    char_mc "(3 billion…!!!)"

    char_mc "(My childhood estimate was right on…!!!)"

    # Detailed evaluation scene
    char_fclerk "These are your results…"
    char_fclerk "What would you like to do?"

    char_mc "(300,000… per year…)"

    char_mc "(If I lived for eighty more years, that would be 24 million in all.)"

    char_mc "(24 million… 24 million…)"

    char_mc "*sigh*"

    char_mc "(Surely that's too cheap by any means?)"

    char_fclerk "…?"

    char_mc "(I guess I'll just have to take 24 million…)"

    # Harsh reality of the evaluation
    char_fclerk "Concerning your per-year value…"
    char_fclerk "You were given the bare minimum of 10,000 yen."
    char_fclerk "And as you have thirty years and three months remaining…"
    char_fclerk "You will be able to leave here with up to 300,000 yen."

    char_mc "*smirks*"
    char_mc "Hah…"

    char_mc "(There on the form were my results, many orders of magnitude below my expectations.)"

    char_mc "I want to know more about your standards."

    # Explanation of valuation
    char_fclerk "The detailed evaluations are carried out by a separate consulting body, so I don't know the specifics my self."

    char_fclerk "Happiness… Actualization… Contribution…"
    char_fclerk "The degree to which such factors are present can greatly affect the value."
    char_fclerk "Or so I hear."

    char_fclerk "In short, the value of your remaining years is…"
    char_fclerk "How happy a life it is, how it makes others happy,"
    
    char_mc "(If I won't be happy,)"
    
    char_fclerk "How many dreams are achieved,"
    
    char_mc "(Won't make anyone happy,)"
    
    char_fclerk "How much it contributes to society, so on and so forth… These things decide the value."

    scene bg black with dissolve

    char_mc "(Won't achieve any dreams,)"
    char_mc "(Won't contribute to society…)"
    char_mc "(Where can I look to for salvation…?)"

    # Final narration
    char_mc "(Ultimately, I sold off all thirty years, keeping only three months.)"

    stop music fadeout 1.0


    return