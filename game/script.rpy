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

# The game starts here.

label start:
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

label a_chatroom:
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


    return
