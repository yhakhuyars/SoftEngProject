label chapter2:

    # Scene: Girl's announcement
    char_fmc "Your evaluation will take about three hours."

    char_mc "(When they first mentioned “selling lifespan”, what immediately came to mind was a morality lesson from elementary school.)"

    # Transition to flashback
    #window hide
    #scene bg classroom_day with fade
    #play music "audio/classroom_bgm.mp3"
    #window show

    # Teacher's dialogue
    char_t "You’ve all been told that it’s something that can’t be replaced,"
    char_t "And that it’s more valuable than anything."
    char_t "But if a human life were given a monetary value, how much do you think it would be worth?"

    # Himeno answers
    char_cmc "I know."
    char_cmc "A salaryman, over the course of their life, earns about 100 million to 300 million yen. That’s what I read in a book once."

    char_mc "(The class’s biggest smart-aleck answered.)"

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

    char_mc "(... said one girl with gloomy prospects.)"
    char_mc "(If we’re talking about the chance to live her life, yeah, I wouldn’t give that a value.)"

    # Classmate 4's joke
    char_cls4 "But if I were selling my life, you guys wouldn’t even pay 300 yen, would you?"

    "“Ha-ha-ha-ha-ha!”"

    char_mc "(The wise-cracking clown you get in every class, thought similarly to me, and had a self-deprecating laugh about it.)"

    char_mc "(As it happens, the teacher said that there was no right answer.)"
    char_mc "(But a right answer did sort of exist.)"

    # End flashback and return to the present
    #window hide
    #scene bg mysterious_building with fade
    #stop music fadeout 2.0
    #play music "audio/mysterious_bgm.mp3"
    #window show

    return


    return