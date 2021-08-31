# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# NVL narrator
# define narrator = nvl_narrator

# // - check in the future.


define MH = Character("[main_hero_name]", image = "mainhero", color = "#4a86e8")
# Main Hero Best Frider Pohui
define MHBFP = Character("Semyon", image = "semyon", color = "#019401")
# Main Hero Best Frider Homophobe
define MHBFH = Character("Vladick", image = "vladick", color = "#c53333")

define CRUSH = Character("Sergey", image = "sergey", color = "#9900ff")

define BULLY_MAIN = Character("Ilya")
define BULLY_SECOND = Character("Nikita")
define BULLY_TARGET1 = Character("Arkadiy")

define NERD_GIRL = Character("Angelina", image = "angelina", color = "#45818e")
define TF = Character("Anastasiya Sergeevna", image = "teacherfriend", color = "#93a1c4")
define TEACHER_CHEMISTRY = Character("Lyudmila Alexandrovna", image = "chemistryteacher", color = "#c39e29")

# The game starts here.

label start:
    # Global variables:
    $ relationShipMHBFP = 0
    $ relationShipCRUSH = 0

    queue music ["audio/background_music1.mp3", "audio/background_music2.mp3"]

    # player input name
    python:
        main_hero_name = renpy.input("Choose a name for your character", length=32)
        main_hero_name = main_hero_name.strip()

        if not main_hero_name:
            main_hero_name = "Alexander"
label sequence1:
    scene empty
    "Week 1." 
    "Wednesday. "

    # at school
    scene classroom chemistry 1 with dissolve

    show semyon smirk
    MHBFP "Hey, look."

    "[MHBFP] shoved me in the shoulder. The dim outline of the view from the window was replaced by the crunching sound of the opening class door."

    show semyon normal at left with move

    show sergey normal at center

    "On the threshold of a chemistry class stands [CRUSH]. Weird. He looks like he was dragged along the rails for hours and then was kicked like hundreds of times."
    
    hide sergey with dissolve
    show semyon angry 1 at center with move

    MHBFP "What's that smell?"
    "[MHBFP] whispered, wrinkling his nose and turning away."

    MHBFP "That's fucking fume. Oh god..."

    """
    Indeed, as soon as [CRUSH] exhaled, a couple of people in the class coughed, and the chemistry teacher flew up to
    him and began to hiss something absolutely indistinct. 
    
    [CRUSH] knits his eyebrows and looks at her as if he doesn't understand what she's talking about.
    """

    show semyon at left with move
    show vladick normal at center with dissolve

    "[MHBFH] stretched to us from the back of his desk."

    MHBFH "Did he really come drunk to school? He bet someone?"
    MHBFP "Douchebag."
    "[MHBFP] snorts and begins to concentrately roll the pencil in his hands. Is he nervous?"

    MHBFH "I can tell he lost his bet."
    "[MHBFH] chuckles and sits back down."

    hide vladick with dissolve
    show semyon at center with move

    """
    [MHBFP] looks tense for some reason. He keeps rolling the pencil in his hands, dabbing at the varnish with his fingers and leaving marks from the nails. Is it because of [CRUSH] appearance? 

    They don't know each other. Although, to be honest, [MHBFP] cannot stand [CRUSH] at all. I mean, at all. 

    As soon as he appears in the corridor or in a common photo with [MHBFP] friends, he immediately becomes hysterical and starts to curse [CRUSH] in all possible ways. 

    That's all because of the old rumor. Someone once told [MHBFP] that [CRUSH] had raped a seventh grader and she had done nothing, because she was afraid to tell about him even to her parents, so no police or headmaster were involved. 

    No one knows if this rumor's true or not. Well, except for [CRUSH]. No one could either confirm it or disprove it, so I probably don't care. But [MHBFP] ... 

    He was angry and hella believed it. Perhaps because he has a sister and he unconsciously imagines her in the place of that seventh-grader. 

    Well it may just be all my guesswork, but [MHBFP] really hates [CRUSH], and it is a fact. 

    I decided to talk to him.
    """

    MH "Are you okay?"

    "[MHBFP] doesn't even look up, but answers in a low voice."

    MHBFP "All right."

    show vladick normal at right with dissolve

    """
    I turn around. [MHBFH] 's looking at us intently, apparently also feeling the tension. He purses his lips and looks down at the notebook too. 
    """

    hide vladick with dissolve
    hide semyon with dissolve

    """
    I even forgot that we're in class. 

    The teacher has already kicked [CRUSH] out and returned to her unshakable hypostasis of the great master. Bruh. I hate chemistry. 

    And of course I'm not listening. All the formulas in the notebook are merging into one abyss of blue ink stripes. 

    [CRUSH]. How fucking strange he is. He doesn't care at all. Even though he will be expelled tomorrow for this trick, he will find it out only after a week, maybe, and he won't give a fuck. 

    It's weird to think like this, but I'm a bit envious. 

    No, I am really ENVIOUS. 

    The only extraordinary thing I can do here is to play hooky or not to return the book to the library. Well, I do this. And I definitely think [CRUSH] feels different when he does come to school drunk or makes teachers mad. 

    I think he feels freedom. 

    I want to feel the same. I've never felt I'm free from all of this stupid shit. Like, everything is so dumb. Maybe I should find myself a girlfriend? 

    Like... [MHBFH] changed when he started dating. Even now. He is chatting with his girl. She is dumb, i must say, but still. He's smiling like she texted him she made a vaccine for AIDS. But I know, they talk about some shit. I doubt she knows the word AIDS. 

    Does [MHBFP] have a girlfriend? He definitely needs some calming ingredient in his life. And he never tells us about his private life. I know, private means private, but... 

    On the other hand [MHBFH] tells us about everything. He never feels ashamed to talk about what he does with his... um... Katya? Can't believe I forgot her name. 

    It should be Katya, right. So, he tells us even what we don't wanna hear, huh. 

    I want something like this too, but I'm too scared and lazy for some actions. Maybe I can fight myself?... 
    """

    play sound "audio/bell.mp3"

    show semyon angry 1 with dissolve

    "[MHBFP] stands up fastly and starts to get his stuff. It's weird. He's usually very slow."

    MH "Hey, um?.."

    MHBFP "I need to go to the bathroom, sorry. Feel bad. See you at biology, maybe."

    hide semyon with dissolve

    "Wowser. Maybe he's about to throw up, lol. At least [MHBFH] is here."

    show vladick normal with dissolve

    MHBFH "[MHBFP] is not okay."

    show vladick smile 2

    "[MHBFH] chuckles and puts on his backpack. The green one. With a panda pendant. I bet his girlfriend bought that for him."

    show vladick normal

    MHBFH "I'm dying to eat something. Wanna visit Katya's class and steal her lunch? Of course you do..."

label sequence2:
    scene empty with dissolve
    "Wednesday. Evening."

    # chat should be here.
    scene chatting 1 with dissolve
    "Chatroom"

    MHBFP "you guys decided that not showing up in class without me is a great idea." 


    MHBFP "hate y'all. i sat here alone & hungry" 


    MH "sorry we thought you were sick..." 


    MHBFH "and Katya made us run away from her for like 15 minutes so we were too tired to sit at the biology" 


    MH "Did we miss something interesting?" 


    MHBFP "not at all, but i am still pissed off bout [CRUSH]. he's fucking bastard "


    MHBFH " do NOT start this again" 


    MH "calm down, he were always like this "


    MHBFP "I know but he always does shit that triggers me. And it's not appropriate. He cut our lesson. I have the right to hate him."  


    MHBFH "i'm so fucking tired of all this shit guys. Let's hang out this friday." 


    MH "uhh..? okay. i'm free" 


    MHBFH "[MHBFP]?" 


    MHBFP "you gotta be kidding. you've forgotten i have a violin exam on Saturday morning?" 


    MHBFH "oh" 


    MHBFH "now i remember" 


    MHBFP "i hate you so much "


    MHBFH " but i love you ♡" 


    MH "i send this to your girlfriend "


    MHBFH "you fucking go. she knows i hate this gay shit" 


    MHBFH "did you guys see how [BULLY_MAIN] punched that [BULLY_TARGET1] from the other class? that fag deserved it. I saw his instagram. He literally freely kisses man. I almost threw up." 


    MHBFP "[BULLY_MAIN]?" 


    MHBFH "yep." 


    MHBFP "..." 


    MH "jeez. This jerk is much worse. Can't believe you support him." 


    MHBFH "I do not support him, okay? I just support what he had done. it's normal that this cunt gets a reaction like this. I bet he wanted it." 


    MH "what's about friday?" 


    MHBFH "I'll figure it out but in general just beer and girls. my bro from the other school will bring some." 


    MH "fine" 


    MHBFH "that's your chance, little virgin :) "


    MH "lmao fuck off"

label sequence3:
    scene living room 2 with dissolve

    """
    This day was so surreal. I don't know why, but everything feels like a total mess. we got [MHBFP] furious about [CRUSH] and [MHBFH]... as always.

    The sun's constantly falling asleep on the other side of the window. I don't remember the last time I washed it, but it has such a quirky vibe I love. The mess has the same vibe, that's why it's always here. 

    [CRUSH] was the same. He loved mess and always fought with his parents to keep the clothes lying on his bed and floor.

    Sometimes I forget we were best friends back in the days. I can't even accept it at some point. 

    We were just 13, and he was normal. Totally like everyone, nothing more, nothing less. We were classmates and spent so much time together before he left the city with his parents. I still don't know why. 

    I become sad while thinking of this. He was the first to betray me, but now I don't feel like I'm still offended or abandoned. I just feel nothing. 

    Sometimes I think about him and the obscure wishes just pop in my head. Maybe I could talk with [CRUSH] at least once. Just to remember the past and the warmness of these memories, that connect me with myself. 

    Then I understand I don't want to. We are different now and he scares me. I mean it's scary to think what he has become. Like somebody totally different, but it's okay, right? 

    We all do change, [CRUSH] does too. I just need to concentrate on my own life and stop thinking about him or anyone else. 

    Should I do my homework now then?
    """
label sequence4:
    scene empty with dissolve
    "Thursday."

    scene school hall 1 with dissolve

    show vladick normal with dissolve

    MHBFH "Have you seen [MHBFP] yet? He wasn't at school and he wasn't replying to my messages."

    MH "Seems like he's sick. We gotta visit him if he's not replying, but not now. "

    show vladick smirk

    MHBFH "Too busy with getting ready for the chemistry test, huh? I've never thought you're a nerd. "

    MH "I just don't want to be expelled, and I recommend you to at least find out what we're studying right now. "


    MHBFH "Some stupid shit? I already know everything 'bout this. Anyway, teachers say they gonna mix the classes so we won't cheat on this fucking test. I only hope to be in the one room with some nerd like you. "


    MH "How can this stop us from cheating? "


    MHBFH "You think I know? Maybe they think we don't know people from other classes. "


    MH "We should tell [MHBFP] about it. "


    MHBFH "At least you can have a chance to meet some pretty babe at the test, you know? Make her steal your sheet with answers and perhaps ask her out then. Sounds like an amazing plan. "


    MH "Jeez, there's only one thing on your mind. Calm down. "


    MHBFH "Don't say like you won't do what I just said. I see it in your eyes. You are interested. "


    MH "Oh god, [MHBFH]... You better revise anything. The test starts in an hour... "


    MHBFH "...And [MHBFP] is still not there. "


    MH "He's gotta be dead to skip a chemistry test. I mean, the principal and Miss Shark will eat him alive. "


    MHBFH "So he'll be dead anyway. Sorry, I must see Katya now. She's so nervous before every single test... "


    MH "Okay, good luck then. Say her hello for me. "

    hide vladick with dissolve

    "[MHBFH] fastly went away. It seems like the only two things he cares about are Katya and his phone. Also, maybe, being annoying. Can't imagine being that concentrated on somebody else. It must be so utterly exhausting and..."


    MHBFP "Hey! [MH]! You're here! "
    # TODO Should be out of breath and with bags under the eyes
    show semyon laugh

    "He looked so out of breath and red. Oh god."

    show semyon normal

    MHBFP "I hurried here as fast as I could. Uh. I need a minute... "


    MH "Wh-where have you been? "

    show semyon smile 3

    MHBFP "You'll be surprised, but I just overslept. I only woke up twenty minutes ago and almost ran like the wind. "

    menu:
        "I can tell. His hoodie is so wrinkled and his face... I guess he didn't sleep. But why? Should I ask?"

        "Ask.":
            $ relationShipMHBFP += 1

            MH "[MHBFP], did you even sleep yesterday? You look tired. Did anything happen?"

            show semyon smile 1

            MHBFP "Uh... That's tough. I will tell you later, okay? I need to concentrate on the test now."

            MH "Please, tell me now, is everything alright?"

            show semyon smile 2

            MHBFP "Y-y-yeah. Yep. Just fine. Really, don't think about this."

            MH "You also didn't answer [MHBFH] 's messages. We were worried."

            show semyon smile 1

            MHBFP "Oh, sorry... I didn't check my phone. God, I hate this day."

            MH "If you tell [MHBFH] about this as you just did to me he won't be angry, I think."

            MHBFP "I hope. Thanks, anyway."

            MH "For what?"

            MHBFP "..."

            show semyon smile 3

            MHBFP "Nothing. Sorry, uh, I need to read."

            MH "Okay."

            hide semyon with dissolve

            "Now think about chemistry. There's only half an hour left. "
        "Do not ask.":
            "No, it's none of my business. I need to let him get ready for the test and all the extra stuff will be figured out soon. Now think about chemistry. There's only half an hour left. "
            hide semyon with dissolve

    """
    It seemed like I didn't realize the time. Holy shit, there's still so much to revise left... Hope I can get through this hell soon. 

    At least, it's the last year. After it there won't be any stupid chemistry or anything as stupid as this. 

    I still don't know what university or profession I'll enroll in after exams, but I know the only thing — no chemistry. At all. 

    Anyway, but now there's only it. Fine, just breathe. 
    """

    scene classroom chemistry 1

    """
    Nothing will confuse you, [MH]. Breathe in, breathe out. You are calm. 

    What? 

    There's [CRUSH] with his friends in our classroom. Seems like [MHBFH] didn't lie and I totally forgot to tell [MHBFP] about this stupid mixed party. 

    Oh no. I just hope he'll be in the other classroom. If [CRUSH] is placed here, [MHBFP] can be also placed somewhere else... 

    Should I call him to report about this? It can be dangerous if teacher's see my phone here. 

    Like... [MHBFP] hates [CRUSH]. I don't know why but it seems like betrayal that I didn't tell him about that. 

    Happily, there's some vacant desks at the very end of the classroom. I guess if I sit here, I can at least text [MHBFP]. 

    Maybe to cheat also. I haven't said this. 

    Okay, now I can write to [MHBFP]. So... 
    """

    show chemistryteacher angry with dissolve

    TEACHER_CHEMISTRY "[MH], please, pass me your phone and sit somewhere closer... Here. "

    "Oh shit, shit, shit. Fuck. She pointed her finger at the desk near the window. Oh my fucking god. It's [CRUSH] at it." 

    MH "I must sit here? With [CRUSH]? "

    "The teacher's blankly staring at me like she doesn't understand. Stupid bitch." 

    TEACHER_CHEMISTRY "Yes, you must sit here. Pass me your phone. "

    """
    God, I didn't even text a single letter. Ok, take it, Miss Shark. 
    """

    hide chemistryteacher with dissolve

    """
    There's a much bigger problem. [CRUSH]. 
    """
    
    show sergey normal with dissolve

    """
    He only looked at me for a second when I took a seat. Like I'm not even there. Okay. I'm just a good decent boy. Just need to greet him. 
    """

    MH "Hey, um... "

    CRUSH "Hello. "

    "He sounds calm. No aggression or annoyance." 


    MH "This is weird, huh? Mixing classes, I mean. All this stupid shit. "


    CRUSH "Yeah. They want us not to cheat, but we anyway will. "


    MH "How? They took away our phones. You have the second one? "

    show sergey smile 1

    "[CRUSH] mildly smiled. "


    CRUSH "Look back. "

    show angelina smile at right with dissolve

    "There's some girl sitting at the desk behind ours." 

    hide angelina with dissolve

    MH "So? "


    CRUSH "She's the best student in our class. [NERD_GIRL]. She knows chemistry better than the witch. I promised to ask her out if she helps me to pass this test. "


    MH "Really? Huh, that's smart. And who's the witch? "


    CRUSH "Don't you know? We call the chemistry teacher like this. I thought everyone knew this alias. "


    MH "We call her Miss Shark. "


    CRUSH "Hah, that's nice too. "

    show chemistryteacher angry at left with dissolve

    TEACHER_CHEMISTRY "Keep silent, [MH], [CRUSH]. And take your test papers. "

    hide chemistryteacher with dissolve

    """
    When I took it, it seemed like the end of the world. Ten tasks and I can solve only two or three. I'm not sure even about these two or three. 


    I sat like a dumbass doing nothing for twenty minutes. At the same time [CRUSH] was doing nothing, just drawing some doodles on the margin of paper. 


    I decided to talk with him just a bit. Maybe he can help..? Or whatever... 

    """
    menu:
        "His doodles are pretty, by the way. Looks like he practised a lot. Should I comment on it? Won't it be too over the top?"
        "Why don't you write anything?":
            MH "Why don't you write anything? "

            show sergey normal

            "[CRUSH] glanced at me for a couple of seconds and snorted. "


            CRUSH "I said, my test will be done by [NERD_GIRL]. Why don't YOU write anything then? "


            MH "I suck at chemistry. Barely did the first two tasks. "


            CRUSH "You need help? "


            "I smiled a bit. He tries to make his voice sound like he doesn't care, but in fact he does. I know this. His old habit. "


            MH "That would be pretty cool. "

            """
            [CRUSH] took my test and turned back to the girl. I looked around to see if teachers notice [CRUSH] 's behaviour, but happily no one gave a shit. 
            """

            show angelina smile at right with dissolve

            """
            It seems she doesn't fit in [CRUSH] 's preferences in girls. 
            """

            CRUSH "Fine. She'll solve yours too. "

            hide angelina with dissolve

            MH "Thank you so much... Really. I couldn't do without you. "


            CRUSH "Oh stop. She just asked to go on a date with you too. "


            MH "What? "


            CRUSH "Oh my god, I'm joking. "


            MH "Thanks anyway. "

            """
            We didn't talk after it. Then [NERD_GIRL] passed [CRUSH] his answers and he calmly continued to sit and draw. 


            In ten minutes something was poked in my back. I turned back and saw [NERD_GIRL] trying to pass me my paper back. Oh god... She really solved all the tasks. 


            Amazing. I don't know how to thank [CRUSH]. 


            Suddenly I noticed something written by a pencil on the margin of the list. 


            \"Thank me later. 55-XXX-XXX <3\" 


            Wow. 


            I don't think I need to show it to [CRUSH]. I'll think about this later, I suppose. Or I won't.
            """

        "You have a talent for drawing.":
            $ relationShipCRUSH += 1

            MH "You have a talent for drawing. "

            show sergey smile 2

            CRUSH "Um... That's just stupid doodles, but thank you. I like drawing. Also... why don't you do your test? "

            show sergey normal

            MH "I suck at chemistry, to be honest. Barely did the first two tasks. "

            CRUSH "You need help? "

            "I smiled a bit. His voice is so caring, like something bad happened to me, even though it's just a test. "


            MH "That would be pretty cool. "

            """
            [CRUSH] took my test and turned back to the girl. I looked around to see if teachers notice [CRUSH] 's behaviour, but happily no one gave a shit. 
            """

            show angelina smile at right with dissolve

            """
            It seems she doesn't fit in [CRUSH] 's preferences in girls. 
            """

            CRUSH "Fine. She'll solve yours too. "

            hide angelina with dissolve

            MH "Thank you so much... Really. I couldn't do without you. "

            CRUSH "Oh stop. She just asked to go on a date with you too. "

            MH "What? "

            CRUSH "Oh my god, I'm joking. "

            MH "Thanks anyway. "

            """
            We didn't talk after it. Then [NERD_GIRL] passed [CRUSH] his answers and he calmly continued to sit and draw. 

            In ten minutes something was poked in my back. I turned back and saw [NERD_GIRL] trying to pass me my paper back. Oh god... She really solved all the tasks. 

            Amazing. I don't know how to thank [CRUSH]. 

            Suddenly I noticed something written by a pencil on the margin of the list. 

            \"Thank me later. 55-XXX-XXX <3\" 

            Wow. 

            I don't think I need to show it to [CRUSH]. I'll think about this later, I suppose. Or I won't.
            """
label sequence5:
    scene school hall 1 with dissolve

    """
    I went out of the class, tightly gripping the backpack.

    Huh. 

    [CRUSH]. I talked to him like we were complete strangers. 

    This is so... weird. I mean it made us escape awkward moments of discussing the past but it was still a bit painful. Even after all these years. 

    Memories of it came upon me rather suddenly and I leaned on the wall, trying to calm down my heavy breathing. 

    I do remember many things but they changed. When we were 13, he always wore colourful classy T-shirts and cared about all homeless kittens. 

    Now he only wears black hoodies. Like... everything black. Punk ass. 

    I wear the same but for me it's more bout not caring. I don't care what I wear. Maybe that's why I'm single lol. 

    Fuck. What time is it now? I need to find [MHBFP] and [MHBFH]. 
    """

    show teacherfriend smile with dissolve

    TF "Oh, [MH], you here! Finally I've found you! "


    "That's [TF]! Hope she came to talk not about how I skipped the whole previous week. "


    TF "See, in two weeks we're having a poem contest. I want you to participate, it's a great chance to show your talent, [MH]. "


    MH "Uh... To be honest I don't think I'm able to write anything decent. I've never tried to. "

    show teacherfriend smile 2

    TF "That's the thing! You just need to try. At least to try. You've participated in many contests in literature, you can write well, you're nice at reading poems out loud. Just give yourself a chance. "


    MH "But... "

    show teacherfriend smile

    TF "Pretty please, [MH], just try, I will help you. "


    "Nice. Another challenge out of nothing. How can I say no to [TF]? "


    MH "Okay. Fine. "

    show teacherfriend smile 2

    TF "Oh, thank you. Come after the break, I'll show you the requirements. Don't forget! "

    hide teacherfriend with dissolve

    """
    Aha. After the last class. Like I had nothing else to do. 


    At least it's [TF]. I like her so much, she's a great teacher even if she's only 25. She feels me and other students like she's one of us. 


    That's why I love literature. Only cause [TF] teaches it. 


    Yeah, it sounds bad. Literature is cool. 
    """

    MHBFH "Hey, [MH], why are you standing there? "
    
    "I shuddered. [MHBFH] 's voice is always so sonorous. Oh, he's with [MHBFP]! "

    show vladick normal zorder 1 with dissolve
    show semyon normal at right zorder 0 with dissolve 

    MH "Just went out of the classroom. "

    show semyon smile 1

    MHBFP "With [TF]? Good try. We saw you "

    MH "Again. You little punk... "

    MHBFH "Jeez, guys. [MH], better tell us how was the test? I only did one task and copied from [MHBFP] 's sheet. He only did five tasks, unfortunately. "

    show semyon normal

    MHBFP "And where's my thank you, ungrateful bitch? "

    MH "I cheated too. "


    MHBFH "Really? They told us teachers in your class took away your phones. Or you copied some pretty girl's work? "


    MH "Um... yeah, exactly. Not so pretty but anyway. "

    show vladick smile 2

    MHBFH "Whooa! Finally! "


    MHBFP "You know her? How did you do it? Teacher's wasn't looking? "

    show vladick smile 1

    MHBFH "Wait, now you should ask her out! "


    MH "Oh please... My head hurts because of your screams. "


    MH "I got helped actually. Teachers made me sit with [CRUSH] and he knew that girl. She helped me and him. I just passed her my test and she returned to me the ready one. "


    MHBFP "[CRUSH]? "


    MH "I couldn't do anything. They made me sit with him. "


    MHBFH "That's cool! She did you the whole test! "


    MH "Yeah... And she left me her number on the sheet. "

    show vladick surprised

    MHBFH "OH GOD. "

    show vladick smile 1

    MHBFH "You have to go. I will die but I'll manage to make you go on a date with her. Even if she's not as pretty as you wish. You are given a chance to touch a girl, bro. "


    MH "I don't think I can... "


    "[MHBFP] mumbled. "


    MHBFP "What's stopping you? "

    "If they only knew that it's [CRUSH] who will go out with her for helping him with the test. It's just... dirty I think. "

    menu:
        "Do I need to tell them about it? I can't lie to [MHBFP], but if I tell the truth [MHBFH] won't lag behind and will make me go. 
        And I realised I really don't want to. If only I made up some weird story so they would be pleased..."

        "Tell the truth.":
            $ relationShipMHBFP += 1

            MH "She helped us only because [CRUSH] promised to go on a date with her. I don't wanna participate in that shit. "

            MHBFP "Oh... "


            MHBFH "You know what it sounds like... An easy target! "


            MHBFP "It's a girl, not an object. "


            MHBFH "Yeah, yeah, again. "


            MHBFP "That's so weird that girls are ready to do [CRUSH] 's test just to go on a date with him. He's not even THAT handsome. "

            show vladick smile 2

            MHBFH "Don't lie, he is THAT handsome. You're just envious. "


            MHBFP "I'm not. He looks like an insane squirrel. "

            show vladick smile 1

            MH "Gosh, guys. I need to go. [TF] is waiting for me. "


            MHBFP "Me too. Violin classes. "


            MHBFH "Can't wait for Friday night. We'll live it up! "


            MHBFP "Thanks, without me. Bye. "


            MHBFH "Is he angry again? "


            MH "I don't think so. Maybe he's just tired of you."
        "Lie.":
            MH "There's another girl I wanna go out with. So no [NERD_GIRL]."


            MHBFP "Really?.."

            show vladick surprised

            MHBFH "Why haven't you told?! That's amazing news! Who's she? Does she study with us? "


            MH "Not now, [MHBFH]. I still haven't figured everything out. "

            show vladick smile 1 with dissolve

            "[MHBFP] looks upset. That's because he knows I'm lying? How?"


            MH "I need to go. [TF] is waiting for me. "


            MHBFP "Me too. Violin classes. "


            MHBFH "Can't wait for Friday night. We'll live it up! "


            MHBFP "Thanks, without me. Bye. "

            hide vladick with dissolve
            hide semyon with dissolve

            """
            He freaks me out.

            How can he be like that? I don't know what's happening around and with [MHBFP] and that's fucking stupid. I need to chill.

            Hope [TF] won't overload me with information today.
            """
label sequence6:
    scene classroom literature 1 with dissolve

    """
    The classroom was empty. Only the golden touches of afternoon light were on the blue wall. Posters, posters, photos... [TF] really likes this place. 

    The poster of Literature Evening... It takes place every season. We come here with tea & pastry and read poems and cite our favourite books. 

    It was [TF] 's idea to have it here. She likes cozy events like this. 

    Maybe because she's so sweet tempered and open-minded? That's true obviously. 

    Also another photo in a white frame. A class of kids in yellow caps and [TF]. I guess it's something like summer activities that are held here. 

    She looks so happy. Even in this stupid cap. Does she really enjoy this or... 
    """

    show teacherfriend smile with dissolve

    TF "Oh, you're already here! I was at the headmaster. C'mon, take a seat. "


    """
    I sat on my favourite chair. Not right in front of her but a bit at the left. I sometimes feel too... I don't know. Just... 


    It's too scary to see her eyes all the time. Like I feel I'm about to overshare. 


    She searches for something in her bag and I sit quietly thinking. 
    """


    TF "No one wants to participate in things connected with art now. It was really hard to find even one person. I also went to the 10th grade and some girls wanted to attend the contest. "

    show teacherfriend smile 2
    TF "I don't know if they still want to do it but... Let's just do what we can, right? "
    show teacherfriend smile

    """
    She finally found what she wanted and it appeared to be her notebook. A real legend. She uses paper for notes, not apps for phone or anything like that. 


    I would go nuts if I did it. Plus my handwriting is mindblowingly awful. 
    """


    TF "Okay, so... The contest is planned to be in two weeks. You need to write a poem from 3 to 10 verses of four lines. No rules for lines. "

    TF "That's it. We will have a contest in our school, you'll need to read it out loud. After your performance, Jury members will take your poem and read it by themselves. That's all. "

    MH "Will there be places or winners? "

    show teacherfriend smile 2
    TF "No. You'll anyway get the certificate of participation. Still we need to do our best, you know? "
    show teacherfriend smile

    MH "Yeah, got it. "

    TF "You always know you can contact me if you need some help, right? "

    MH "Aha. "

    "She keeps silence for half a second. I felt a bit strange."

    TF "You act uptied these days, [MH]. Is everything fine? "

    TF "I know you may be busy. You're in the last year of studying, you have exams, but this contest is really important. I don't know whom to ask but you. "

    MH "No, I know, no problem about the contest. It's... I don't know. "

    TF "Is something bothering you? "

    MH "I feel like... something wrong is happening. With me. I always dive into my memories. "

    TF "Do you regret doing something or you just want to go back? "

    MH "Neither. "

    MH "I just... remember. Then I feel like I've lost something in the past and that I'll never find it anymore. "

    TF "Hmm. "

    "She stood up and went to the cabinet. Then a kettle and two pink mugs appeared on the table." 

    show teacherfriend smile 2
    TF "A little cup of tea is always a nice decision, right? "
    show teacherfriend smile


    """
    I nodded. After some noise of the old kettle I felt the smell of tea leaves. 

    [TF] always makes tea when we sit here talking about everything starting with school subjects and finishing with philosophy. 

    [TF] took her mug and sat, holding her palms round the hot surface. 
    """


    TF "It happens. Sometimes you think about the past as something from a different life and want to go back to those innocent times. You just don't remember pain. "

    TF "There was pain and bad feelings. We all tend to forget about it. Our brain just pushes it away from our consciousness so we won't be traumatized. "

    TF "The thing is that our past is still us. That's the part of us that forms our character. Sometimes we should let it go. "

    TF "Everything changes. The faster you get this the better. Let it go. Concentrate on your present-self. That's the only thing you're in charge of. "


    """
    I sat looking into the depth of the mug. Gosh, she really wants to support me. As always does. 

    This softens me. May I just stay here for eternity? 
    """

    MH "Yeah... I need to understand that things have changed and they won't go back. Even if that's painful. "

    show teacherfriend smile 2
    TF "Right! "
    show teacherfriend smile

    TF "Pain will go away one day but you'll stay here. As they say, easy come easy go. Cookies? "

    MH "Yes please. "

    """
    I really feel much better. The first thing is that I've told somebody about my feelings and finally let them out of my chest. 

    The second thing is that I understood I need to think about [CRUSH] as somebody new. 

    Not as about my old friend from teenagerhood, but as a 18 years old guy with his new life. 

    It sometimes amazes me how [TF] can help with literally everything and to give nice advice. To be honest I hate advice from everyone but not from her. 

    Maybe I just overthink?..
    """

label sequence7:
    scene empty with dissolve
    "Thursday. Evening."

    scene living room 2 with dissolve

    """
    I spent the whole evening thinking about my poem for the contest. And I haven't written a single line. 

    My brain hurts. 

    Maybe it's just too hard for me but who am I without hardship? 

    Calm me. 

    Okay, don't think about the bad side. It's only a small contest, [MH]. Only. A. Small. Contest. 

    I may open the window. I guess it's all because there's no fresh air in the room. 
    """


    MH "Fuck!"

    """
    When I tried to reach for the window handle I accidentally stepped on my backpack and all my notebooks scattered on the floor. Fuck. 

    What's here? My maths exercise book... 

    I guess it's the messiest one. Pencil marks on the cover, ripped pages and meaningless doodles. Maths is boring, huh. 

    A school diary... Another messy thing. I don't give a fuck why does this stuff exists. 

    Huh, the draft of my chemistry test answers. 

    It was today but feels like a week ago. And [CRUSH]. 

    Oh. [NERD_GIRL]. 

    Her phone on the margin. 

    A sociable girl, I may say. 

    Ah, [MH], don't be like that. Maybe she really liked you. Couldn't she? She could. 

    At least you need to thank her. That would be polite. She helped you. 

    Or was that [CRUSH] who did? 

    It doesn't matter for now. 

    I should text her and then decide what I'll do next. 

    My fingers make proud taps on the keyboard of the phone. 

    I text her \"Hey, it's [MH] from chemistry\" 

    Now wait. 

    A poem. That's fucking hilarious. I hate myself for agreeing but I would do the same if I said no. So easy and so stupid. 

    I just need to write something. Even some nonsense. 

    \"Beep\" 

    Uh, the phone. My savior. 
    """


    NERD_GIRL " \"Hi\" "

    NERD_GIRL " \"Yes, I remember you :)\" "
    
    "And what should I answer? "

    "Firstly, I wanted to thank her. "

    MH " \"Thanks for your help. You hella saved my life\" "

    NERD_GIRL " \"Haha I'm glad to help\" "

    "Then what? I forgot how to chat with strangers." 

    "She texts something. "

    NERD_GIRL " \"Listen, I'm with [CRUSH] now. He wanted to talk to you but he didn't have your number\" "

    NERD_GIRL " \"I wanted to ask you if you allow to share your number\" "

    "[CRUSH]? What does he want from me? "

    MH " \"Um.. ok\" "

    NERD_GIRL " \"Nice :3\" "

    NERD_GIRL " \"Hope to see you at school ASAP!\" "

    "Oh. She is a sociable girl but I still have questions for [CRUSH]. "

    "I guess he'll answer when he texts me. Now I should do something more valuable. "

    "Like trying to know what's wrong with [MHBFP]. "

    "I put on my favourite sneakers and a phone with headphones. The best way to make him happy is to make a surprise."

    if relationShipMHBFP >= 2:
        """
        I should take a cake with me! [MHBFP] likes them so much and it'll definitely make him pleased as hell. 

        Happily my mom always has at least one cake in the fridge in case somebody comes or whatever. I must say it helps from time to time. 

        He likes strawberry shortcakes and vanilla cupcakes. I know, that's not classy but... 

        Kinda cute, right? 

        Even if I don't know what's happening with him there are certain things I always do to cheer him up. 

        And I am worried.
        """

    scene bg street 1 with dissolve

    """
    The weather isn't that nice, to be honest. Only low greyish cumulus and fresh cool wind that runs around my ankles. 

    Rain, pretty please, I beg you, do not start. My thin hoodie won't survive. 

    Thankfully we're neighbours with [MHBFP] so it only takes like ten minutes to reach for his flat building. 

    I remember the times we were young and played here together. Rode on that old swing with cracked handrails, run everywhere playing hide-and-seek. 

    Once he fell when running away from me and hurt his knee. There was much blood all around his leg and he was crying so loud. 

    We're the same age but I acted like a real adult. I took him and we went to his mom to disinfect the wound. 

    I didn't remember that but his mum told me I tried to calm [MHBFP] down by telling him jokes and fairy tales about dwarfs. 
    """

    scene entrance 1 with dissolve

    """
    I'm here. Two knocks and I hear the sound of the door being opened. 
    """

    show semyon sad with dissolve

    """
    He's in a stretched T-shirt with stains and his face looks like... he cried. 
    """

    MH "[MHBFP], I- "

    MHBFP "What happened? "

    MH "I just came to cheer you up, dude."

    if relationShipMHBFP >= 2:
        MH "I have something for you. "

        "I hold out a box of cake. "

        MHBFP "Oh... "

        """
        He takes it and I feel the warmth of his thin hands. 

        Even if it's cold outside and it's the middle of the winter, even if it's the coolest fall, even if it's snowing like hell. 

        His hands are warm. 

        He smiles a bit. 
        """

        MHBFP "Thank you... Come in. I'll put the kettle on. "

        scene living room 1

        """
        It always smells like this here. Like... old newspapers, aloe, pastry. And something undetectable but in general it feels cozy and warm. 

        Like his hands. 

        Okay, calm down. 
        """

        show semyon normal with dissolve

        MH "[TF] made me participate in a new contest. Of poetry. "

        MHBFP "Really? I didn't know you write poems. "

        MH "Yeah, the same. And now I do. "

        MHBFP "You do so much for her. "

        "I come to the kitchen. [MHBFP] takes out two big mugs and tea bags from the cabinet. "

        MH "She told me nobody wants to do this now. What's connected with literature, I mean. "

        MHBFP "And you want to? "

        MH "I don't know, really. I messed up but for now I need to do what I need. "

        MH "Now you. "

        MH "You overslept today. "

        MHBFP "So what? "

        MH "Don't act like this! You NEVER oversleep. You literally have fifteen alarms. For every day. "

        "He chuckles and sits back. Now I see how fucking tired he is." 

        MHBFP "I... You don't have to worry, okay? It's fine. Trust me. Just regular problems. I need to solve them by myself. "

        MH "You know, you can always ask me if you need help. "

        MHBFP "Yes. "

        "It doesn't seem well. He doesn't seem well but he asked to trust him. How can I do this if he's like a walking dead?" 

        menu:
            "Should I insist?"

            "Insist.":
                $ relationShipMHBFP -= 1
                MH "You can tell me. Please, do, [MHBFP]. It's not okay. I will help. You must tell me what's happening. "

                "His face tensed and [MHBFP] pursed his lips. "

                show semyon angry 1

                MHBFP "Stop this. For God's sake. "

                MH "But... "

                MHBFP "Do not make me do what I'll regret later. I’ve already said everything you need. I will solve everything. "

                MH "Okay, jeez, okay. You got this. Let's better change the topic. "

                MHBFP "I'm dying to eat the cake. Shut up for a second, let me enjoy. "

                MH "Haha, fine. I will. After I tell you about the show I spent the whole night watching. So... "

                MHBFP "Oh no."

            "Do not insist.":
                $ relationShipMHBFP += 2
                MH "Fine. I trust you. "

                show semyon smile 1

                "He tilted his head down but I still noticed the little smile. "

                MH "Now better try the cake. It's a blessing it was in the fridge. "

                MHBFP "Uh, your mum is so prudent. A real hero. "

                MH "And I can't even calculate how long my chewing gum will last. "

                MHBFP "That's cute. "

                MH "Oh really? It's clumsy, don't try to calm me down. "

                MHBFP "I will. C'mon, you're a teen. It'll change. "

                MH "I'll always be like this. Some things don't change. "

                MHBFP "Why are you so sure? Everything changes. People change when they get older. "

                MH "I just feel that it's me. I mean... "

                MHBFP "What? "

                MH "That's a part of my character. To be clumsy. Also lonely, pathetic, et cétéra. "

                show semyon smile 3

                "[MHBFP] giggled for a second and I felt... strange. "

                MH "Why do you laugh? "

                show semyon smile 1

                MHBFP "You're so lost. Don't be tricked by the stigma they give you. "

                MHBFP "You aren't clumsy, lonely, pathetic or whatever. You're more than all this stuff. "

                MHBFP "Ah, that's weird. And awkward... I only hope you got this. "

                "I lowered my eyes to the floor, to my fancy socks with frogs. Oh god, we never talked like this before. "

                MH "Yeah. Right. "

                MH "Thank you. "

                "He didn't answer. Just noticed the sound of boiling water and spilled it into mugs."

    if relationShipMHBFP < 2:
        MHBFP "Huh. Nice. "

        MH "I'm not a dumbass, [MHBFP]. I have eyes. And the brain. Something is happening with you and you must tell me everything. "

        MHBFP "Yeah, of course, I must. "

        show semyon angry 1

        MHBFP "I do not owe you anything. Do you even hear yourself? You never cared. And now you come here and say I must do something. "

        MH "Okay, I'm sorry. I'm really sorry. I just want to help. That's why I'm here. "

        MHBFP "You want to help? Amazing. I don't need your help. Go away. "

        MH "[MHBFP], please... "

        MHBFP "I need to stay by myself. Go home. "

        MH "I won't. I'm just... you act weird. You've never acted like this before. I'm worried. I want to make sure you're alright. Only this. "

        MHBFP "I'm fine, okay? Go home. I need to go. Goodbye. "

        "He closes the door right in front of me. "

        "He's right. I need to go home before I break this fucking door to hell."

label sequence8:
    scene empty
    "Friday. "

    scene school hall 1 with dissolve

    """
    On the next day [MHBFP] didn't show up at school. I've decided not to bother him. 

    I really had much to think about like... [CRUSH]. He asked Angelina for my number. 

    But for what? 

    There's so many people around me. This hall is always so crowded like they don't have another place to stay around. 

    However, for now I can't leave. The physics classroom is here and I just want to come into it as soon as possible. 

    I take out my diary. 

    At least I have some time to work on my poem. Maybe this noise will somehow inspire me. 

    Even if I can't hear my own thoughts. 

    I don't like to deepen into my mind. It's too overwhelming and it just feels wrong. 

    If you don't concentrate on your feelings it's way easier to overcome them. 

    Especially if these feelings aren't important. 

    And I still have no idea how to write this fucking poem. 

    Pathetic. 
    """

    "Unknown" "Hey, [CRUSH]!" 

    """
    I shuddered. Wait, that's not my name. But he's there. 

    I notice his dark hair among the crowd and look down. Huh. 

    His appearance here seems kind of embarrassing. For me, of course. 

    The voice that called [CRUSH] didn't sound again. 

    [CRUSH] came to school one more time? He does it so rarely it feels like a blessing for our poor headmaster. 

    She wanted to deduct him for three times but something stopped her. Maybe it's 'cause he acted like a normal student for a week when there were signs they wanted to deduct him. 

    Maybe it's 'cause of his parents. We don't know who they are but it seems this type of a son is always brought up by a special type of parents. 

    Even though we were friends… many years ago… I still didn't know a thing about his parents.

    Of course, this is none of our business but it could explain a lot about him. 

    He acts like he doesn't care and the thing is that.. maybe he really doesn't care? 

    Kids that were brought up by \"basic\" people don't do this. They may act but in fact they care. 

    And- 
    """

    show sergey smile 1 with dissolve

    CRUSH "Howdy. What're you writing? "

    """
    Oh. 

    The sudden discharge embraced my whole body and I dropped my diary. Fuck. 

    I just leaned down to take it and accidentally felt that he had leaned down too. 

    We collide with our hands for a couple of seconds and I automatically pull back mine. 
    """

    show sergey smile 2

    CRUSH "You're so easy to scare. Um, sorry, by the way. "

    MH "Oh no, it's not your fault. Thanks. "

    show sergey smile 1

    CRUSH "I hope [NERD_GIRL] didn't startle you with me asking for your number. "

    MH "Uh, no, but it's still bizarre. "

    CRUSH "I just wanted to... We'll have a small party with my friends next week, Sunday, to be precise. So I wanted you to come too. "

    CRUSH "Like you know, we were friends for so many years before. Why not? "

    "I felt my eyebrows raise even if I tried to act like there's nothing strange in his behaviour. "

    MH "Okay... Let it be. "

    CRUSH "Alright then. Later. "

    hide sergey with dissolve

    """
    He disappeared as fast as came into sight. Oh. 

    That's pretty... strange. His offer. 

    [MHBFP] could be mad, huh.
    """

    if relationShipMHBFP >= 4:
        """
        I should tell him. 

        Even if [CRUSH] seems to be fine and that stuff it's still not okay. [MHBFP] has a right to know. 

        Maybe it'll make him sad but what can I do? 

        Still there's something bothering me. I can't say I refuse to go. 

        I know it sounds bad but I just can't sleep on that feeling. 
        """
        menu:
            "Should I go to that party?"

            "Yes.":
                $ relationShipMHBFP -= 4
            "No.":
                "..."

    """
    However, that's not what I should worry about. 

    The noise quited down after the bell rang. I thought I needed to go to physics class. 

    [CRUSH] washed away my thoughts about the poem contest and physics and... 

    He just did. 

    I need to go.
    """

label sequence9:
    scene empty
    "Friday. Evening."

    scene bg street 2 with dissolve
    
    """
    It seemed too cold when I went outside wearing only some skinny jeans but [MHBFH] was already here. I got no chance to change and at the same time I was too tired to do that. 
    """

    show vladick smile 1 with dissolve

    """
    He was smiling and the warm orange light from the street lamp was making his blonde hair look like a tangerine. 

    Some tiny snowflakes are falling on my nose. 

    Huh. 
    """

    MHBFH "Five minutes late. "

    """
    I said nothing but it didn't feel like I needed to answer. 

    [MHBFH] doesn't really nag even if it feels that he might be. Just... he takes everything easy. 

    We're on the way to the party [MHBFH] talked about. 

    And [MHBFP] isn't with us. 

    Would he go if he was free? I don't think so. 

    He's not that guy. 

    He doesn't even like alcohol and I ain't got an idea why he can get up with [MHBFH]. 

    Who's definitely a humanisation of A Party. 

    Like... that much. He can't live without all that hustle and bustle. 

    He talks bout some shit but I can't concentrate on listening. Moreover, he doesn't really need me to comment on what he's talking bout. 

    I look on the snowy pavement. 

    These days were over the top. 

    Maybe it's a blessing? 

    I got so much to feel, to discover, to know. 

    Even though it's overwhelming as fuck. 

    Time just gets away when you overthink. 

    We finally came to the big tower block building. Wet grey walls of it seemed so pathetic to be real. 

    I can't say I hate all that stuff that surrounds me. It's somehow inspiring from time to time. All those greyish buildings, halls with dark green walls peeling off. 

    Bumpy roads. 

    Stray dogs. 

    We climb the stairs to the fifth level. I accidentally step on a thin spider slowly running through my way. 

    [MHBFH], anyway, acts too happy for this surrounding. With his bright hair he looks like a sun beam. 

    And I look like a moon. 

    Huh. Drama queen. 

    I look like a drug addict, to be honest. 

    [MHBFH] doesn't hear my depressive thoughts and opens the dark scarlet door. 

    It's not closed? Seems like they're fearless. 
    """

    scene party 1 with dissolve

    """
    The first things I notice are amber light and cigarette smoke. Everywhere. And five of like six persons. 

    [MHBFH] goes deeper into the flat but I stay to explore it a bit. 

    It's actually quite a big room with two doors. One of them leads to the kitchen, another is closed. Maybe it's a WC but why is it closed then? 

    I don't know who designed this flat but they certainly did an awful job. 

    Like... who thought olive walls would go well with pinkish kitchen cabinets or a red couch? 

    I notice only stranger's faces here, they seem to be my age. And... drinking. 

    I suddenly step on a small puddle on the linoleum. 

    Oh god, please, let it be beer... 
    """

    "Somebody" "[MH]?" 

    "I fastly straightened up from examining my poor sneakers and it appeared that the voice was [NERD_GIRL]."

    show angelina smile with dissolve

    NERD_GIRL "Oh, you're here! "

    MH "Um, yes... "

    NERD_GIRL "I've never seen you there! "

    
    "So, she often goes there. Not an excellent student anymore. "

    "But who am I to judge? "


    MH "Yeah, I'm new there. I came with [MHBFH], actually. "


    NERD_GIRL "I see. [MHBFH] is... that blonde guy? With a red tie? "


    MH "Yeah. He loves it. His father's gift. "

    show angelina smug

    NERD_GIRL "Jeez. "


    MH "Uh? "


    NERD_GIRL "I thought no one wears ties now. Especially red ones. "


    MH "He just does what he likes. "


    NERD_GIRL "Yep, right. Sorry. "

    show angelina smile

    "I only shrug my shoulders in answer. "


    NERD_GIRL "So, let me treat you with this cider. "

    """
    She gave me a little transparent plastic glass with an ocher drink in it. 

    It's too sweet but I didn't pay for it. I have no right to criticize. 

    [NERD_GIRL] drank a glass too. It didn't seem like she tried something before I had come. Acted like a fully sober girl. 
    """

    MH "You know somebody there? "

    "[NERD_GIRL] looked around and nodded. "

    NERD_GIRL "Sure. And it seems like you do not know. "

    "I chuckled. "

    MH "Right. I only know [MHBFH]. "

    NERD_GIRL "So these two guys near the window are [BULLY_MAIN] and [BULLY_SECOND]. They are from the \"B\" foam. "

    NERD_GIRL "I don't talk with them much, we... have nothing in common, frankly saying. "

    NERD_GIRL "These three girls are from my foam. You'll anyway forget their names, so... "

    NERD_GIRL "Kids in the kitchen are from the 10th form, I don't really know them. But the guy in the red jacket is a son of [TEACHER_CHEMISTRY]. "

    MH "Really? I didn't know she had a son. "

    NERD_GIRL "He's quite a bizarre person. Too... spoiled, I should say. "

    MH "No wonder. "

    NERD_GIRL "Oh, the couch is free. C'mon, let's sit, my legs hurt. "

    NERD_GIRL "I spent the whole afternoon running around with books at the library. [TF] asked me to help her with arranging her bookcase. "

    MH "[TF]? "

    NERD_GIRL "Yes... Our literature teacher. You know her? "

    show angelina smile 2

    MH "Surely. "

    MH "Yeah, she was my teacher for many years. "

    NERD_GIRL "She's amazing. "

    MH "For sure... "

    show angelina smile

    "She frowned for a second. "


    NERD_GIRL "Huh, are you okay? You sound weird. "


    MH "No, no, I'm fine. Just... Nothing. "


    """
    I take a new glass with cider and let myself chill a bit. 

    She talks to me about some stuff like these three girls whose names I still don't know or that son of the chemistry teacher. 

    The alcohol starts to affect. 

    Oh god, I didn't eat anything before drinking. 

    My mistake. I'll pay for it. 

    But [NERD_GIRL] looks as fresh as a daisy. Like she drank only pure water. 

    Fuck, I hate it. 

    The lights begin to mess but just a bit. [NERD_GIRL] sits closer and closer while I recline on the couch trying to go back to this world. 

    I only feel her warmness and the smell of cider and her perfume. 

    It's too sweet and... smells like flowers. 

    Doesn't match her character. 

    She's kinda spicy. 

    I feel that when she leans closer and closer to my cheek. 
    """

    show angelina smug

    """
    Holy shit. 

    She wants to kiss me. 

    I realise that three seconds before she does that. I move away heavily breathing. 
    """

    show angelina smile

    """
    Her face doesn't reflect anything. Like she doesn't feel disappointment or shame because of her failed attempt. 

    I would. 

    I scarcely stand up and she doesn't even move for a bit to help me. I don't need that, actually, but it seems like [NERD_GIRL] wouldn't even care if I fall right here. 

    Wait. 

    Hold on. 

    Breathe in. 

    Breathe out. 

    [MH], you need to calm down. 

    Let's clear my mind. There was a balcony in the kitchen. 

    My steps are hesitant but I don't stop. 

    Please, [NERD_GIRL], go out of my head. It hurts like hell. 

    I don't notice anyone around... There's just a whole mess in my mind. 
    """

    scene party balcony with dissolve

    "I noticed somebody on the balcony for too late. And I hold my breath. "

    MH "[CRUSH]? "

    show sergey normal with dissolve

    "He turns his head to me for a second. "

    "I never noticed how good black hair looks in the light of the moon and stars. Like a miracle. "


    CRUSH "What in a world. "

    """
    And then I see a whitish line of smoke for a cigarette between his fingers. 

    Don't wanna sound dramatic but it looks like a painting. 

    Him in a moonlight, under the starry sky, with a thin cigarette. 
    """

    MH "I didn't know you're there. "


    CRUSH "Same. "


    CRUSH "I never left this balcony. No wonder. "


    MH "Why? "


    "I come closer to see his face and lean on the cold railing. "


    CRUSH "It's better there. Fresh air, all that stuff. "


    MH "But you smoke... "


    CRUSH "Thank you, Captain Hindsight. "


    MH "It's still illogical. "


    CRUSH "And you like to find logic everywhere, even where you're not asked to? "


    "I humed something but [CRUSH] was right. "


    MH "Just wanna understand you. "


    CRUSH "By asking stupid questions? Oh no. "


    MH "Don't act like you don't get what I am talking about. "


    MH "We both know it's strange. "


    MH "To talk after all these years. We didn't even say hello to each other. "


    MH "We acted like complete strangers. You didn't care if I felt lonely or left, I did the same. "


    MH "I still don't know why and for what. "


    MH "And let me tell you, you started that many years ago. "


    MH "But now you start to talk, you search for my number, you ask me to go to the night with your friends. "


    MH "Why? "


    """
    I felt devastated after saying that. Like I let all the thoughts out. All the thoughts that bothered me, that interrupted my calm life and my ability to do everyday tasks. 

    And he keeps silent. After all that. 

    Fuck, I only want him to understand what I feel. What I felt for these years. 

    Even if that subsided for the last years I spent with [MHBFH] and [MHBFP]. 

    We were so close. And we separated as fast as we had found each other. 
    """


    CRUSH "Little did I know what I would do now when I was younger. "


    CRUSH "I'm sorry. "


    CRUSH "I don't have a right to say thay, I know, but... I feel so sorry we splitted up. "


    CRUSH "Then I felt I needed to do that to become somebody cooler. To find cool friends. "


    CRUSH "To become... I don't know whom. "


    CRUSH "It felt like I needed to change what surrounds me to change myself. "


    CRUSH "It worked. You see it did. "


    CRUSH "But... Am I pleased with what I have done? Am I fine? "


    CRUSH "That's why I am sorry. "


    """
    I was so astonished I couldn't even say a word. 

    [CRUSH] was watching the dark street under the balcony. 

    It's cold here. 

    Not freezing but it gave me goosebumps. 

    [CRUSH] seemed to be okay with this temperature. He standed like a statue, only his hand moved so he could take a hit off. 
    """


    CRUSH "She's sometimes too clingy. "

    "I raised my eyebrows. "

    MH "Who? "

    CRUSH "[NERD_GIRL]. I saw you and her. "

    "It seemed I needed to be shocked or just surprised but I only felt some unknown urge to laugh. "

    MH "You're right though. "

    MH "I didn't know she's like... this. I thought she is like a straight-A student that has nothing to do with parties or cider. "

    CRUSH "You condemn her? "

    MH "No, of course. I'm just... surprised. "

    CRUSH "Not all people are like there's nothing behind them. Even if you think so. "

    MH "And you think you know her? "

    CRUSH "No. We just went out one time. It was her wish for helping me with chemistry. "

    CRUSH "Happily she haven't done the same with you "

    MH "Because I'm just weird. "

    CRUSH "She still tried to kiss you. "

    MH "She's drunk. "

    CRUSH "Jeez, you better stop. Don't act stupid. "

    MH "And you just don't know what's on my mind! Maybe... maybe I have wanted her to ask me out. "

    show sergey smile 1

    "[CRUSH] chuckled. "

    CRUSH "For real? "

    MH "It doesn't matter. "

    CRUSH "It does. "

    CRUSH "There are much better girls than [NERD_GIRL]. If you haven't fallen in love with her already, of course. "

    show sergey normal

    "I winced unconsciously."

    MH "No... Obviously no. "

    CRUSH "Then what's the point? "

    CRUSH "If you love somebody, act like this. If you don't — do not show this pathetic performance. "

    MH "I don't. "


    """
    [CRUSH] took a pause to drag on. 

    I feel that the air is purging my soul. The alcohol effect is certainly reducing and I can clearly see and think. 

    Time flies there. 

    It's so cold yet I stand close to [CRUSH] and feel his warmth. He doesn't look cozy at all but it feels like everything is like it has to be. 

    That's what you feel at home. 

    The memories of our past are pouring back so fast that my feet almost gave way under me. 

    Summers with shiny cola bottles with glittery water drops on it, old creaking bikes, dirty sneaks. 

    Falls under the sad sun trying to get into the classroom where we play tic-tac-toe on the last desk. 

    Winters, wet mittens, wet backpacks, that we left on the ground when playing catch up. 

    Springs. Fresh smell of acacia trees. And him, standing on the sandy riverbank, looking at the glossy water surface. 

    Feels like a different life. 

    I look at him to find at least something connecting the old [CRUSH] to his newer... version. 

    His face is sharper. Maybe just because he's way older. 

    He's a bit taller than me but back in the days I was in his position. 

    He was always so envious of my height and thought he would never get taller. 

    If only he knew after years things would change and he'll look much more masculine than me. 

    There are scratches on his knuckles. Tiny, but there are many of them. 

    It gives an impression they are fully scarlet and cyan at the same time. 

    Even bruises on him look nice. 

    And a cigarette between the fingers. He holds it firmly, and the white surface of it begins to fill with little dents. 
    """


    MH "Can I... Can I take a drag on? "


    CRUSH "You smoke? "


    MH "No but I want it now. "


    CRUSH "Huh, good attempt. I strongly do not recommend it."

    menu:
        "To insist.":
            $ relationShipCRUSH += 1

            MH "I insist. If you don't give me I'll ask for a cigarette from these people inside. "

            show sergey smile 1

            CRUSH "Wow, what a spirit. "

            CRUSH "Okay, you persuaded me. "

            """
            He gave me his cigarette tenderly touching my fingers for a second. 

            Huh. It wasn't hard to talk him into that. 

            I finally took a drag on. 
            """

            show sergey smile 3

            """
            [CRUSH] laughs when I cough like hell. 

            It's... bad. 

            He looked so ethereal doing this even if in my own mouth it feels like somebody pissed here. 

            I gave the cigarette away as fast as I took it. 
            """

            show sergey smile 2
            CRUSH "I appreciate your try. But still don't do this anymore. "
            show sergey smile 1

            MH "It's so gross in my mouth I cannot bicker. Okay, I got you. "

            CRUSH "Good boy. "

            """
            There was nothing special in what he had said but I felt that my cheeks flushed. 

            Hell, this is awkward. But... 

            Cool.
            """

        "To agree.":
            MH "Fine. I got you. "

            "[CRUSH] didn't answer. He only quietly snorted but I ain't got an idea why."

    CRUSH "Let's get back to the inside. I wanna have a drink. "

    scene party 1 with dissolve

    """
    I silently follow him. 

    When we appear in the kitchen I suddenly feel like the hot air is burning my skin. We spent too much time outside and now I just want to stay here. With him. 

    He searches for a glass while I walk around looking for [MHBFH]. 

    Just to check on him, of course. 

    We never split up when we go anywhere with him and [MHBFP]. Especially with [MHBFP]. 

    Today is an exception, though. 

    The reality kinda strikes me. 

    He's snogging with [NERD_GIRL] on a couch where I was sitting before. 

    But... What about his girlfriend? 
    """

    show sergey normal with dissolve

    CRUSH "You see, don't worry. She will always find somebody else. "

    MH "I know but... "

    CRUSH "But what? "

    MH "Nothing, man, I was just thinking. "

    "He shrugged his shoulders."

    CRUSH "I told the guys in the kitchen to get lost and now we have a chance to sit in a warm place. "

    MH "You're a bully. "

    CRUSH "I just said and they left, it's not my fault. "

    MH "Of course. Anyway, thanks. "

    CRUSH "It's for us both. "

    """
    We come and [CRUSH] sits down at the table. 

    I stay standing, leaning on the wall. We keep silent for a couple of seconds and [CRUSH] starts: 
    """

    CRUSH "If you don't like Angelina we can find you somebody else. I don't get why you're so sad if you've told you don't care bout her. "

    """
    I don't even think for a second and say okay. 

    Like... Even though I don't want to find anyone. 

    I'm not sad. 

    I just... I don't know. 

    Maybe the truth about his reason to leave me and end our friendship is too overwhelming. 

    But I agree to find somebody new. 

    Will it fill me from inside? Will it heal me?
    """

label sequence10:
    scene empty with dissolve
    "Week 2."
    "Monday."

    scene classroom chemistry 1 with dissolve

    """
    This Monday is rainy. 

    The thin layer of snow disappeared as fast as it happened to show up. 

    I still felt a bit of fatique from Friday but I tried to get distracted and watched some stupid series yesterday. 

    Like, these TV-shows with shitty actors and shitty scenarios where you just enjoy the madness happening on the screen. 

    It really helps to take your mind off. 

    Today I cannot do the same. 

    I've already skipped many lessons in previous weeks so now I have to at least show up at school more. 

    I come to the math class ten minutes before the lesson. 

    Almost nobody there. 

    Just some girls I don't really talk to. 

    [MHBFH] will definitely be late but it's too strange for [MHBFP] not to come with me. 

    There's much weird things he does now. Like... His behaviour is strange. 

    Gradually the classroom begins to be filled with students. 

    [CRUSH] doesn't come. 

    As always, right? 

    It's strange to think I thought he would come. 

    Why? Because we talked drunk at the party on Friday? 

    Jeez, I go nuts. 

    [MHBFH] comes right before the bell. He shines like a dumbass and runs to me with a wide smile like he had won a million dollars a minute ago. 

    Like I haven't seen him with [NERD_GIRL]. 
    """

    show vladick smile 2 with dissolve

    MHBFH "Whatsup man! Heck, I'm hungry. I overslept and didn't have breakfast. You have something? "

    MH "Um... A gum? "

    show vladick smile 1

    MHBFH "It will do. At least something. "

    """
    He takes a pink candy and the teacher enters. 

    I try to listen to him about some integrals or whatever but I can't really understand. Or just to concentrate. 

    [MHBFH] doesn't even try to and just starts playing games on his phone. 
    """

    hide vladick with dissolve

    """
    I draw some tiny doodles on the margin of the maths notebook. 

    Like [CRUSH] does. 

    Our doodles became similar. The same strokes, the same figures. 

    I find it inspiring to think about this. 

    We're different but we are still somehow connected effortlessly. 

    It may sound too dramatic or... Nevermind. 

    It's weird. We're just friends from the past. 

    We got a chance to become friends one more time. 

    I barely not sleep in the class just because. 

    Just because I don't wanna sleep but it's too boring I can't think of anything else. 

    This torture ends rapidly. When the bell rings I fastly pack up and decide to wash my face in the bathroom. 
    """

    play sound "audio/bell.mp3"    

    scene school hall 1 with dissolve

    """
    [MHBFH] didn't react so I got no dumb questions. 

    When I was 12 I thought I'll be super cool when I become an eleventh-grader. 

    But now if I see middle-schoolers in halls I understand I'm not the coolest one here. 

    I scarcely put on my old hoodie in the mornings but they all dress up like there will be at least a national parade right now. 

    Why are my thoughts so pathetic? Why do I think I'm worse if I do not dress up perfectly every day? 

    When I come up the stairs I suddenly hear a strange sound. 

    Like... A voice. 
    """

    show semyon sad with dissolve

    MHBFP "[MH], wait! "

    """
    It's [MHBFP]! 

    I turn around and see him. 

    It looked like he had been crying. 

    A lot. 

    I'm unusually happy to see him, really. 

    But... 

    He is so tired and his red eyes look deep into mine. 
    """

    MH "Where have you been? What happened? "

    MHBFP "I'm so... I'm so sorry. "

    MHBFP "Please we gotta talk. "

    MH "Okay, sure... "

    """
    I was confused and my voice sounded too disoriented but [MHBFP] only took my hand and pulled me after him. 

    We went down to the lonely place under the stairs. 

    Usually students who wanted to skip the classes spent their time here but then the headmaster knew about this place. 

    And it was forgotten. 

    But now it seemed to be needed. 
    """

    MH "So? "

    """
    [MHBFP] quietly sobbed. It was so heartbreaking but I literally couldn't move. 

    My whole body freezed. I didn't know how to calm, how to comfort him. 

    And I didn't even know if these things could help. 
    """

    MHBFP "I'm sorry... I wanted to say this earlier but... I couldn't... I thought it'll be over... "

    MHBFP "This guy... [BULLY_MAIN]... He... He... "

    """
    [BULLY_MAIN]. It sounds so familiar. 

    Oh gosh. [MHBFH] told us about him. 

    That guy bullied a boy. Because? 

    Shit. 

    Because he was gay. 
    """

    MH "[MHBFP], tell me now. "

    "I wanted to sound strict but [MHBFP] only sobbed more. "

    MHBFP "He... He had seen me with a guy. We were in one chat room. And we went for a walk and... "

    MH "And what? "

    MHBFP "We kissed. [BULLY_MAIN] saw that. It was in the evening at the park and I thought there was nobody around... But... "

    "Oh god. "

    "I felt my eyes got round. "

    MH "You... You kissed a guy? "

    "[MHBFP] fastly looked away. "

    MHBFP "Yes. So what? You gonna hit me too? "

    MH "[BULLY_MAIN] hit you?! "

    MHBFP "Yes. On the next day all this happened. He took me behind the school and said he had seen everything. And he... Kicked me in the stomach. "

    """
    He raised his shirt. 

    Like a big galaxy, there was a round blue and yellow and green hematoma above the belly button. 

    It looked so painful I almostly felt burning at the same place on my own body. 
    """

    MH "Oh my god... But when did it happen? "

    MHBFP "Before the day of the chemistry test. "

    MHBFP "After classes. "

    MHBFP "I barely came home... Took some painkillers and fell asleep for 16 hours. "

    MHBFP "Mum's on a business trip so nobody noticed. "

    MHBFP "[BULLY_MAIN] said people like me don't deserve to live. "

    MHBFP "And I thought... I... I thought he'll back off after that. "

    MHBFP "And I came to school like nothing happened so nobody here will notice either. "

    MHBFP "But after we dispersed with you and [MHBFH] I got a text... "

    """
    He gradually stopped crying and only gave me a phone with chat with [BULLY_MAIN]. 

    I opened the picture he sent and saw a blurry photo of two people kissing almost in the dark. 

    Nevertheless the face of [MHBFP] was seen clearly. 

    And it was obvious the second person was a guy too because of his manly built. 

    Under the message with this photo there was a text: 

    \"You send me $100 or I send this to [CRUSH]\" 
    """

    MH "What? [CRUSH]? "

    MHBFP "Yes. "

    MH "What does he have to do with this? "

    MHBFP "You don't know but... [CRUSH] also... He also bullies us. "

    MHBFP "It's a secret. Only we know that. "

    MH "\"We\"? "

    MHBFP "Gays. There're not many of us but... Still. Like a couple of people in our school. "

    MH "What a community. "

    MH "Sorry. I mean... It's okay. "

    MH "I won't say anything about what gender you love. "

    MH "It's none of my business. "

    MH "But I'm... I'm stunned about [CRUSH]. "

    MH "I never knew that. "

    MHBFP "And you couldn't... "

    MHBFP "I- "

    """
    He starts crying again. 

    Mostly when people cry I feel irritated. Like... Even if it's somebody who is close to me. 

    But with [MHBFP] crying I feel awkward and... Useless. 
    """

    MH "I could talk with him. "

    MH "To protect you. "

    MH "So he won't touch you. "

    MH "Do not send anything to [BULLY_MAIN]. Block him now. "

    MHBFP "But... If I go to school? He'll easily find me here. "

    MH "Stay at home, okay? Say you're ill, just make up some sort of story. I'll confirm it to teachers. "

    MH "We'll do something. "

    """
    It felt like sadness just exploded in his big swollen red eyes. 

    And it was replaced with something... Unusual. 

    He never looked at me like that. 

    It wasn't gratitude or appreciation. 

    It wasn't positive but at the same time there was nothing negative. 

    It was a fully new emotion coming into existence in his dark pupils. 
    """

    MHBFP "I'm sorry I did this all to you. Sorry for not sharing. I felt so lonely. "

    MHBFP "Like everyone left me in a moment. "

    """
    I stood still, blankly staring into his face. 

    But he moved. 

    It was as fast as the flight of a butterfly. 

    He leaned on me and clumsily kissed my lips. 
    """
    
    hide semyon with dissolve

    """
    I only felt a warmness, some diluted salt from hot tears and a velvety sense. 

    It wasn't a real kiss. 

    More like an embarrassing touch of a lost teen. 

    He ran away and didn't look back.
    """
label end:
    scene empty with dissolve
    "TO BE CONTINUED..."
    return


# ENDINGS:
label endingGoodMHBFP:
    "GOOD ENDING MHBFP"
    return