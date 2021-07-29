# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# NVL narrator
# define narrator = nvl_narrator

# // - check in the future.


define MH = Character("Main hero", image = "player")
# Main Hero Best Frider Pohui
define MHBFP = Character("Semyon", image = "semyon")
# Main Hero Best Frider Homophobe
define MHBFH = Character("Vladick", image = "vladick")

define CRUSH = Character("Sergey", image = "sergey")

define BULLY_MAIN = Character("Bully main")
define BULLY_TARGET1 = Character("Bully target 1")

define NERD_GIRL = Character("Angelina")
define TF = Character("Teacher friend")
define TEACHER_CHEMISTRY = Character("Chemistry teacher")

# The game starts here.

label start:
    # Variables:
    $ relationShipMHBFP = 0
    $ relationShipCRUSH = 0
    "Start of the game. Player name input. "
label sequence1:
    # at school
    scene bg street1

    show semyon neutral
    MHBFP "Hey, look."

    "[MHBFP] shoved me in the shoulder. The dim outline of the view from the window was replaced by the crunching sound of the opening class door."
    
    show semyon neutral at left 
    with move

    show sergey neutral

    "On the threshold of a chemistry class stands [CRUSH]. Weird. He looks like he was dragged along the rails for hours and then was kicked like hundreds of times."

    hide sergey neutral
    show semyon neutral at center
    with move
    
    MHBFP "What's that smell?"
    "[MHBFP] whispered, wrinkling his nose and turning away."

    MHBFP "That's fucking fume. Oh god..."

    """
    Indeed, as soon as [CRUSH] exhaled, a couple of people in the class coughed, and the chemistry teacher flew up to
    him and began to hiss something absolutely indistinct. 
    
    [CRUSH] knits his eyebrows and looks at her as if he doesn't understand what she's talking about.
    """

    "[MHBFH] stretched to us from the back of his desk."

    MHBFH "Did he really come drunk to school? He bet someone?"
    MHBFP "Douchebag."
    "[MHBFP] snorts and begins to concentrately roll the pencil in his hands. Is he nervous?"

    MHBFH "I can tell he lost his bet."
    "[MHBFH] chuckles and sits back down."

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

    """
    I turn around. [MHBFH] 's looking at us intently, apparently also feeling the tension. He purses his lips and looks down at the notebook too. 

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

    //sound of the bell

    [MHBFP] stands up fastly and starts to get his stuff. It's weird. He's usually very slow.
    """

    MH "Hey, um?.."

    MHBFP "I need to go to the bathroom, sorry. Feel bad. See you at biology, maybe."

    "Wowser. Maybe he's about to throw up, lol. At least [MHBFH] is here."

    MHBFH "[MHBFP] is not okay."

    "[MHBFH] chuckles and puts on his backpack. The green one. With a panda pendant. I bet his girlfriend bought that for him."

    MHBFH "I'm dying to eat something. Wanna visit Katya's class and steal her lunch? Of course you do..."

label sequence2:
    # chat should be here.

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
    MHBFH "Have you seen [MHBFP] yet? He wasn't at school and he wasn't replying to my messages."

    MH "Seems like he's sick. We gotta visit him if he's not replying, but not now. "

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


    "[MHBFH] fastly went away. It seems like the only two things he cares about are Katya and his phone. Also, maybe, being annoying. Can't imagine being that concentrated on somebody else. It must be so utterly exhausting and..."


    MHBFP "Hey! [MH]! You're here! "


    "He looked so out of breath and red. Oh god."


    MHBFP "I hurried here as fast as I could. Uh. I need a minute... "


    MH "Wh-where have you been? "


    MHBFP "You'll be surprised, but I just overslept. I only woke up twenty minutes ago and almost ran like the wind. "

    menu:
        "I can tell. His hoodie is so wrinkled and his face... I guess he didn't sleep. But why? Should I ask?"

        "Ask.":
            $ relationShipMHBFP += 1

            MH "[MHBFP], did you even sleep yesterday? You look tired. Did anything happen?"

            MHBFP "Uh... That's tough. I will tell you later, okay? I need to concentrate on the test now."

            MH "Please, tell me now, is everything alright?"

            MHBFP "Y-y-yeah. Yep. Just fine. Really, don't think about this."

            MH "You also didn't answer [MHBFH] 's messages. We were worried."

            MHBFP "Oh, sorry... I didn't check my phone. God, I hate this day."

            MH "If you tell [MHBFH] about this as you just did to me he won't be angry, I think."

            MHBFP "I hope. Thanks, anyway."

            MH "For what?"

            MHBFP "..."

            MHBFP "Nothing. Sorry, uh, I need to read."

            MH "Okay."

            "Now think about chemistry. There's only half an hour left. "
        "Do not ask.":
            "No, it's none of my business. I need to let him get ready for the test and all the extra stuff will be figured out soon. Now think about chemistry. There's only half an hour left. "

    """
    It seemed like I didn't realize the time. Holy shit, there's still so much to revise left... Hope I can get through this hell soon. 

    At least, it's the last year. After it there won't be any stupid chemistry or anything as stupid as this. 

    I still don't know what university or profession I'll enroll in after exams, but I know the only thing — no chemistry. At all. 

    Anyway, but now there's only it. Fine, just breathe. 

    Nothing will confuse you, [MH]. Breathe in, breathe out. You are calm. 

    What? 

    There's [CRUSH] with his friends in our classroom. Seems like [MHBFH] didn't lie and I totally forgot to tell [MHBFP] about this stupid mixed party. 

    Oh no. I just hope he'll be in the other classroom. If [CRUSH] is placed here, [MHBFP] can be also placed somewhere else... 

    Should I call him to report about this? It can be dangerous if teacher's see my phone here. 

    Like... [MHBFP] hates [CRUSH]. I don't know why but it seems like betrayal that I didn't tell him about that. 


    Happily, there's some vacant desks at the very end of the classroom. I guess if I sit here, I can at least text [MHBFP]. 


    Maybe to cheat also. I haven't said this. 


    //*some sitting sound lol?? idk he takes place*


    Okay, now I can write to [MHBFP]. So... 
    """

    TEACHER_CHEMISTRY "[MH], please, pass me your phone and sit somewhere closer... Here. "


    "Oh shit, shit, shit. Fuck. She pointed her finger at the desk near the window. Oh my fucking god. It's [CRUSH] at it." 


    MH "I must sit here? With [CRUSH]? "


    "The teacher's blankly staring at me like she doesn't understand. Stupid bitch." 


    TEACHER_CHEMISTRY "Yes, you must sit here. Pass me your phone. "


    """
    God, I didn't even text a single letter. Ok, take it, Miss Shark. 

    There's a much bigger problem. [CRUSH]. 

    He only looked at me for a second when I took a seat. Like I'm not even there. Okay. I'm just a good decent boy. Just need to greet him. 
    """

    MH "Hey, um... "

    CRUSH "Hello. "

    "He sounds calm. No aggression or annoyance." 


    MH "This is weird, huh? Mixing classes, I mean. All this stupid shit. "


    CRUSH "Yeah. They want us not to cheat, but we anyway will. "


    MH "How? They took away our phones. You have the second one? "


    "[CRUSH] mildly smiled. "


    CRUSH "Look back. "


    "There's some girl sitting at the desk behind ours." 


    MH "So? "


    CRUSH "She's the best student in our class. [NERD_GIRL]. She knows chemistry better than the witch. I promised to ask her out if she helps me to pass this test. "


    MH "Really? Huh, that's smart. And who's the witch? "


    CRUSH "Don't you know? We call the chemistry teacher like this. I thought everyone knew this alias. "


    MH "We call her Miss Shark. "


    CRUSH "Hah, that's nice too. "


    TEACHER_CHEMISTRY "Keep silent, [MH], [CRUSH]. And take your test papers. "

    """
    When I took it, it seemed like the end of the world. Ten tasks and I can solve only two or three. I'm not sure even about these two or three. 


    I sat like a dumbass doing nothing for twenty minutes. At the same time [CRUSH] was doing nothing, just drawing some doodles on the margin of paper. 


    I decided to talk with him just a bit. Maybe he can help..? Or whatever... 

    """
    menu:
        "His doodles are pretty, by the way. Looks like he practised a lot. Should I comment on it? Won't it be too over the top?"
        "Why don't you write anything?":
            MH "Why don't you write anything? "


            "[CRUSH] glanced at me for a couple of seconds and snorted. "


            CRUSH "I said, my test will be done by [NERD_GIRL]. Why don't YOU write anything then? "


            MH "I suck at chemistry. Barely did the first two tasks. "


            CRUSH "You need help? "


            "I smiled a bit. He tries to make his voice sound like he doesn't care, but in fact he does. I know this. His old habit. "


            MH "That would be pretty cool. "

            """
            [CRUSH] took my test and turned back to the girl. I looked around to see if teachers notice [CRUSH] 's behaviour, but happily no one gave a shit. 

            [NERD_GIRL] is really pretty... Even though she seems to be a nerd. There's something strange in some details about her, like... Her earrings are like they were chosen by some insane kids. Or her pink shirt with mushrooms. Sounds weird. 
            
            It seems she doesn't fit in [CRUSH] 's preferences in girls. 
            """

            CRUSH "Fine. She'll solve yours too. "


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

        "You have a talent for drawing":
            $ relationShipCRUSH += 1

            MH "You have a talent for drawing. "

            CRUSH "Um... That's just stupid doodles, but thank you. I like drawing. Also... why don't you do your test? "

            MH "I suck at chemistry, to be honest. Barely did the first two tasks. "

            CRUSH "You need help? "

            "I smiled a bit. His voice is so caring, like something bad happened to me, even though it's just a test. "


            MH "That would be pretty cool. "

            """
            [CRUSH] took my test and turned back to the girl. I looked around to see if teachers notice [CRUSH] 's behaviour, but happily no one gave a shit. 


            [NERD_GIRL] is really pretty... Even though she seems to be a nerd. There's something strange in some details about her, like... Her earrings are like they were chosen by some insane kids. Or her pink shirt with mushrooms. Sounds weird. 
            
            It seems she doesn't fit in [CRUSH] 's preferences in girls.
            """

            CRUSH "Fine. She'll solve yours too. "

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

    TF "Oh, [MH], you here! Finally I've found you! "


    "That's [TF]! Hope she came to talk not about how I skipped the whole previous week. "


    TF "See, in two weeks we're having a poem contest. I want you to participate, it's a great chance to show your talent, [MH]. "


    MH "Uh... To be honest I don't think I'm able to write anything decent. I've never tried to. "


    TF "That's the thing! You just need to try. At least to try. You've participated in many contests in literature, you can write well, you're nice at reading poems out loud. Just give yourself a chance. "


    MH "But... "


    TF "Pretty please, [MH], just try, I will help you. "


    "Nice. Another challenge out of nothing. How can I say no to [TF]? "


    MH "Okay. Fine. "


    TF "Oh, thank you. Come after the break, I'll show you the requirements. Don't forget! "

    """
    Aha. After the last class. Like I had nothing else to do. 


    At least it's [TF]. I like her so much, she's a great teacher even if she's only 25. She feels me and other students like she's one of us. 


    That's why I love literature. Only cause [TF] teaches it. 


    Yeah, it sounds bad. Literature is cool. 
    """

    MHBFH "Hey, [MH], why are you standing there? "

    
    "I shuddered. [MHBFH] 's voice is always so sonorous. Oh, he's with [MHBFP]! "


    MH "Just went out of the classroom. "


    MHBFP "With [TF]? Good try. We saw you "


    MH "Again. You little punk... "


    MHBFH "Jeez, guys. [MH], better tell us how was the test? I only did one task and copied from [MHBFP] 's sheet. He only did five tasks, unfortunately. "

    MHBFP "And where's my thank you, ungrateful bitch? "


    MH "I cheated too. "


    MHBFH "Really? They told us teachers in your class took away your phones. Or you copied some pretty girl's work? "


    MH "Um... yeah, exactly. Not so pretty but anyway. "


    MHBFH "Whooa! Finally! "


    MHBFP "You know her? How did you do it? Teacher's wasn't looking? "


    MHBFH "Wait, now you should ask her out! "


    MH "Oh please... My head hurts because of your screams. "


    MH "I got helped actually. Teachers made me sit with [CRUSH] and he knew that girl. She helped me and him. I just passed her my test and she returned to me the ready one. "


    MHBFP "[CRUSH]? "


    MH "I couldn't do anything. They made me sit with him. "


    MHBFH "That's cool! She did you the whole test! "


    MH "Yeah... And she left me her number on the sheet. "


    MHBFH "OH GOD. "


    MHBFH "You have to go. I will die but I'll manage to make you go on a date with her. Even if she's not as pretty as you wish. You are given a chance to touch a girl, bro. "


    MH "I don't think I can... "


    "[MHBFP] mumbled. "


    MHBFP "What's stopping you? "

    "If they only knew that it's [CRUSH] who will go out with her for helping him with the test. It's just... dirty I think. "

    menu:
        "Do I need to tell them about it? I can't lie to [MHBFP], but if I tell the truth [MHBFH] won't lag behind and will make me go. 
        And I realised I really don't want to. If only I made up some weird story so they would be pleased..."

        "Tell the truth":
            $ relationShipMHBFP += 1

            MH "She helped us only because [CRUSH] promised to go on a date with her. I don't wanna participate in that shit. "

            MHBFP "Oh... "


            MHBFH "You know what it sounds like... An easy target! "


            MHBFP "It's a girl, not an object. "


            MHBFH "Yeah, yeah, again. "


            MHBFP "That's so weird that girls are ready to do [CRUSH] 's test just to go on a date with him. He's not even THAT handsome. "


            MHBFH "Don't lie, he is THAT handsome. You're just envious. "


            MHBFP "I'm not. He looks like an insane squirrel. "


            MH "Gosh, guys. I need to go. [TF] is waiting for me. "


            MHBFP "Me too. Violin classes. "


            MHBFH "Can't wait for Friday night. We'll live it up! "


            MHBFP "Thanks, without me. Bye. "


            MHBFH "Is he angry again? "


            MH "I don't think so. Maybe he's just tired of you."
        "Lie":
            MH "There's another girl I wanna go out with. So no [NERD_GIRL]."


            MHBFP "Really?.."


            MHBFH "Why haven't you told?! That's amazing news! Who's she? Does she study with us? "


            MH "Not now, [MHBFH]. I still haven't figured everything out. "


            "[MHBFP] looks upset. That's because he knows I'm lying? How?"


            MH "I need to go. [TF] is waiting for me. "


            MHBFP "Me too. Violin classes. "


            MHBFH "Can't wait for Friday night. We'll live it up! "


            MHBFP "Thanks, without me. Bye. "

            """
            He freaks me out.

            How can he be like that? I don't know what's happening around and with [MHBFP] and that's fucking stupid. I need to chill.

            Hope [TF] won't overload me with information today.
            """

    return
