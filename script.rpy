# The script of the game goes in this file.

# Declare characters used by this game.

define q = Character(
    name="Qin-Qin",
    color="#CCCCCC",
    image="qinqin",
    what_color="#000",
    window_background=Frame("gui/textbox_frame.png",25,25),
    window_xmimimum=300,
    window_xmaximum=700,
    window_xpos=0.35,
    window_ypos=0.45,
    window_xpadding=30,
    what_xpos=0.0
    )

define q0 = Character(
    name="???",
    color="#CCCCCC",
    what_color="#000",
    window_background=Frame("gui/textbox_frame.png",25,25),
    window_xmimimum=300,
    window_xmaximum=700,
    window_xpos=0.35,
    window_ypos=0.45,
    window_xpadding=30,
    what_xpos=0.0
    )

# Declare music
define audio.atmosphere = "audio/music/castletrivia_theme.opus"

define persistent.ending = "default"

# The game starts here.

label start:

    # Load the questions from questions.rpy
    call questions from _call_questions

    # Initialize player scores
    $ playerPass = 0
    $ playerFail = 0

    # Initialize required points to pass and fail
    $ passingScore = 3
    $ failingScore = 3

    scene bg room
    image darkerScreen = "#000000AA"

    play music atmosphere fadein 1.0

    "I wake up and find myself on the floor, soaking in a pool of blood."
    "Most of it is not mine."
    "My weapons, broken. My armor, shattered."
    "Beside me is a lifeless two-headed wolf, as tall as two gladiators."
    "One of this ugly beast's heads still had its fangs cutting deep into my leg."
    "It was a battle I could have avoided if I paid better attention to my surroundings."
    "But, what a glorious story it will be to tell."
    "If I can survive my wounds, that is."
    "I fight to stay concious but my memory and thoughts are muddled."
    "The first clear thought I have is my name."

    $ player_name = renpy.input("My name is:")
    $ player_name = player_name.strip().upper()

    # Declare default player name
    if(not player_name):
        $ player_name = "Amadeus"

    define player = Character("[player_name]", color="#CCCCCC",
        what_color="#000",
        window_background=Frame("gui/textbox_frame.png",25,25),
        window_xmimimum=300,
        window_xmaximum=700,
        window_xpos=0.30,
        window_ypos=0.85,
        window_xpadding=30,
        what_xpos=0.0
    )

    "Between labored breaths, I try to rouse myself with the usual senseless salutation I use when I meet would-be enemies, allies or patrons."
    player "Good day! I am {b}[player_name]{/b}, the Foolhardy Fortune Hunter!"
    "It is a trite greeting, I've been told."
    "But it has been tied to my reputation since my youth."
    "I never really outgrew it, in any case."

    "On the other side of the corridor, I see my bag of treasure."
    "I spent most of the night fighting this castle's beasties for those shinies."
    "There are enough trinkets there to keep my belly full and have a roof over my head for a year."
    "Before I can drag myself to my loot, I hear footsteps echoing on the marble floor."
    "Another wayward adventurer?"
    "Or another beastie come to finish me off?"
    "I yell with strained effort."
    player "Hello? Is someone there?"

    "A figure steps out from the shadows."

    show qinqin at right with Dissolve(0.5)

    "My sanity must have fractured."
    "How could this lovely vision be possible in a place like this?"
    # jump ending02

    "The figure looks like a human female."
    "Or maybe an elf female, judging by her stature."
    "She has long, silver hair that is only slightly lighter than her skin."
    "She wears a style of clothing I am not familiar with. An eccentric magic user, maybe?"

    "Her wide, piercing eyes betray that she is equally surprised to see me."

    q0 "What are you doing here?"

    "Her voice is soft and soothing like the choir of the local town's church."

    "If these are my final moments, at least my last vision will be pleasant."

    "I speak to her through broken breaths."

    player "Good day! I am [player_name], the Fool--"
    "A bout of coughs interrupt me."
    "I realize how ridiculous I must sound as soon as the words leave my bleeding mouth."
    "I muster all my friendliness and charm in the most sincere appeal of my life."
    player "I wonder if you may have a healing potion to spare?"

    "She reaches into her satchel but then hesitates."

    q0 "I... I'm sorry, but this is a dangerous place and I don't know who you are."
    q0 "The last \"person\" I tried to help turned out to be a shapeshifter who nearly slit my throat."

    "Smart lady. Smarter than me, no doubt."
    "She keeps her distance, but hasn't abandoned me yet."
    "I recognize a hint of sadness in her eyes as she looks at the mess I am."

    player "I'm just a humble and foolish adventurer, my lady."
    player "As you can see from my broken armor and bones, I may not live to see the dawn."

    "Truthfully, I am feeling colder."

    q "Did you slay the beast beside you?"

    "Qin-Qin is staring at the wolf's head still clamped on my leg."
    "It must be a grim sight to witness."

    player "Ah, this monstrous mongrel? Of course!"
    player "It was a terrible battle, but in the end, it was no match for my skill."

    "I pour on the bravado to assure her that she is safe."
    "She doesn't need to know how much luck favored into my triumph."

    "Another round of coughs revisit me."

    player "If I may be so bold, may I ask for your name?"
    player "If I do not survive, it will make my final hours less lonely."

    "She considers my pathetic state.\nThe grip on her satchel seemingly loosens."

    q0 "M-my name is {b}Qin-Qin{/b}."

    "Qin-Qin. What a strange and lovely name."

    player "Lady Qin-Qin, I know you have no reason to trust me, but you must leave this place if you can."
    player "Learn from my folly and live to see another day."

    "I take a glance at my treasure bag."
    "I might as well be generous."

    player "If you wish, you can take my loot. I will no longer need it."

    "Qin-Qin does not move. Her eyes dart everywhere around us."
    "Is she looking for something?"

    q "I can help you [player_name], but I need to make sure you are not dangerous."

    q "I will ask you a few questions, and your answers will determine our fate."
    q "Answer {b}all three questions{/b} correctly, and I will restore your health."
    q "But if you fail three times, then... I am afraid I cannot risk my own life to save yours."

    "Her expression softens, as if to reassure a child learning how to swim for the first time."
    q "Do not worry, it will be a simple test."

    player "A test?!"

    "I laugh and cough blood in turns."
    "I am about to die and the only one who can help me wants to test my wit."
    "Bards sing of my skill with swords, whips, and other weapons. My wit? Not so much."
    "Oh, I am certainly doomed."
    "..."
    "Ha! Why not? A test is far from the most foolish thing I've ever done."
    "Besides, I would be lying if I said I wanted to be alone right now."

    player "I understand your wariness, Lady Qin-Qin."
    player "Goddess knows a little more caution would've kept me healthier."
    player "I accept your gracious challenge."

    player "What subject shall we trade wits about, then?"

    q "Vampires."

    player "Vampires!?"

    q "Yes. If you believe the rumors, the lord of this castle is a powerful vampire."
    q "True vampire hunters should know who they are dealing with. And prepare meticulously."
    q "If you can prove your worth, then maybe you are not one of the dark one's minions as I suspect you are."

    "I cannot blame her reasoning."

    "And yet in my pathetic condition I cannot help but lament at my situation."
    "Such a horrible night to have a test."

    player "As you wish, Lady Qin-Qin. Please ask your questions."

    "Her face lights up. A small, sweet smile briefly paints her face."
    "I swear I saw her hop and skip a little closer."

    "She then looks at me with serious intent and asks her questions."

    jump askQuestion

label askQuestion:

    # Get a question from the list using a random number
    $ question_random = renpy.random.randint(0,(len(question_list)-1))
    $ renpy.random.shuffle(question_list)

    $ (questionNow_question, questionNow_options, questionNow_answer) = question_list[question_random]

    # Remove the question from the list of available questions
    $ question_list.pop(question_random)

    # Ask the question, before showing the choices, so the player can think about it
    q "[questionNow_question]"

    menu:
        q "[questionNow_question]"

        "[questionNow_options[0]]":
            $ playerAnswer = int(0)
            call checkAnswer(questionNow_answer,playerAnswer) from _call_checkAnswer

        "[questionNow_options[1]]":
            $ playerAnswer = int(1)
            call checkAnswer(questionNow_answer,playerAnswer) from _call_checkAnswer_1

        "[questionNow_options[2]]":
            $ playerAnswer = int(2)
            call checkAnswer(questionNow_answer,playerAnswer) from _call_checkAnswer_2

    # Display the current score
    call showScore from _call_showScore

    # Evaluate the player's status
    if(playerPass >= passingScore):
        jump ending01
    elif(playerFail >= failingScore):
        jump ending02
    else:
        jump askQuestion


    return


label showScore:
    q "You have answered [playerPass] questions correctly and [playerFail] questions incorrectly."
    if(playerFail==2 and playerPass<=2):
        q "Be careful, [player]. You have only have one mistake left to make."
    return


label checkAnswer(correctAnswer,playerAnswer):
    $ playerAnswerStr = str(questionNow_options[playerAnswer])
    $ correctAnswerStr = str(questionNow_options[correctAnswer])

    if(correctAnswer==playerAnswer):
        $ playerPass +=1
    else:
        $ playerFail +=1

    q "The correct answer is {b}[correctAnswerStr]{/b}.{p=2}Your answer is {b}[playerAnswerStr]{/b}."

    return

label ending01:
    "Qin-Qin smiles as I answered the last question correctly."
    q "You have answered all my questions correctly, [player_name]."
    "She reaches into her satchel and takes out a small bottle with crimson liquid."
    "She helps me sit upright to drink."
    "The bitterness and warmth of the potion is most welcome."
    "I feel the pain in my body slowly ebb away."
    q "This is all I can give you."
    q "But it shall be enough to restore your strength so you can leave this castle."
    "She retrives my treasure bag and places it beside me."
    "Her hand pats my head, as if to give me assurance."
    "It is refreshingly cool."
    "With my recovery, we will have a better chance of escaping this castle."
    player "Thank you, Qin-Qin. I vow to protect you as we escape this nightmarish place."
    "Qin-Qin steps back. She shakes her head. Her sweet smile slowly fades."
    q "I still have much work to do here."
    "Did I hear her right?"
    "My head swirls from the memory of the savage beasties I fought earlier."
    "I cannot possibly abandon Qin-Qin if her own quest is not yet done."
    player "Well then, I shall join you. I must repay you for saving my life."
    "Qin-Qin steps away further. She clutches her satchel in front of her."
    q "No. If you wish to repay your debt, please, do not return to this castle. Ever again."
    "She walks towards a branching corridor."
    "Her gaze darts around the room once more."
    "She seems particularly focused on the high ceiling where I see nothing but shadows."
    "Her strange gesture reminds me of a cornered animal looking for traps."
    "Finally, she looks at me with a sad smile."

    window hide
    q "Goodbye, [player_name]. {p}Please try to be more careful in your next adventure."

    hide qinqin with Dissolve(2)
    with Pause(1.5)

    "What?"
    "No, this can't be right."
    "I struggle to get up, but my mending legs ignore my will."
    "I call out to where the shadows embraced her."
    player "Lady Qin-Qin! Wait for me! Qin-Qin!"
    "She is gone. As quickly as she had appeared."
    "I struggle to get up again, but the medicine has made my head heavy."
    "I need to rest and let the medicine work."
    "The sun will be rising soon. I will follow Qin-Qin as soon as I can."

    scene black with Dissolve(1)
    scene bg room dawn  with Dissolve(1)

    "After the longest hour of my life, warm sunlight breaks through the windows."
    "I feel the potion has restored enough of my strength."
    "I gather my weapons and limp towards the corridor that Qin-Qin took."
    "But... {w}the corridor is short and ends in a wall."
    "There is no other doorway here."
    "I look for other paths, but find none."
    "I hesitate and weigh my options."
    "..."
    "I don't understand it. The sun is rising, there is no breeze... but I am starting to feel cold again."
    "Perhaps...{w} Qin-Qin is right and I should leave this place while I can."
    "I take my bag of treasure and walk as briskly as I can towards the castle exit."

    scene black with Dissolve(2)

    "I feel I will meet Qin-Qin again someday."
    "But for now, I will honor her counsel and strive to be more cautious."

    $ persistent.ending = "Ending 1"

    jump ending03

label ending02:

    q "You have failed, [player]."
    "My mind is tired from the test."
    "The loss of blood, the fatigue, I--"
    q "I find it inconceivable that you chose to trespass into a vampire's home without knowing enough about them."
    "Qin-Qin's expression has changed, as if the color has left her face."
    "I wanted to say that her trivial questions would probably not help in a fight with a vampire."
    "But... I--{w} I can no longer move my jaw to speak."
    q "I was truly afraid that you would be a threat..."
    "I sense no breeze...{w} and yet a biting chill scratches my arms."
    q "...as you seem to have disposed of the master's minions with considerable skill."
    "My eyes...{w} so tired and heavy."
    "I will...{w} just...{w} rest for..."

    window hide
    show darkerScreen with Dissolve(2)
    show qinqin dhampir with Dissolve(0.5)

    q "Perhaps your prowess as a fighter will serve you better as our soldier."
    q "Goodbye for now, [player_name]. I look forward to your rebir..."

    hide qinqin with Dissolve(2)
    scene black with Dissolve(0.5)
    "Qin-Qin is still speaking, but I no longer hear or understand her."
    "As I lose conciousness, I feel something sharp pierce my neck."
    "It feels like a wolf's bite, but stronger and, strangely, more gentle."
    "..."
    "Several hours later, I would wake up, once again soaking in a pool of blood."
    "Most of it is not mine..."

    $ persistent.ending = "Ending 2"

    jump ending03

label ending03:

    scene black
    with Pause(1)
    stop music fadeout 1.0
    centered "THE END{w=1}\n\nYou answered [playerPass] questions correctly and [playerFail] questions incorrectly.{w=1}\n\nThank you for playing!"

    return
