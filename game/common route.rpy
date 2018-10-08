label day001:

    $ day001_evt = True

#    show aeth neu at left
#    show elaine neu at right
#    show child neu at center

#    "This is a dialogue test."

    scene bg overworld01

    "Skip Intro?"

    menu:

        "Yes":
            jump apothecary_shop

        "No":
            aeth "..."

    #Need town from hill BG

    "The air is cold, carrying the strong smell of pine, which I've always associated with home."

#    "This is a test. I need to see how the game deals with very long dialogue and narration. Currently, I have dialogue centered and it should be shorter than the narration, which is unlimited. But unless I know exactly where it will make the cut for dialogue, I can't make a dialogue box. Thus, I need to know how it deals with long text like this."

#    aeth "This is a test. I need to see how the game deals with very long dialogue and narration. Currently, I have dialogue centered and it should be shorter than the narration, which is unlimited. But unless I know exactly where it will make the cut for dialogue, I can't make a dialogue box. Thus, I need to know how it deals with long text like this."

    #Maybe caravan in woods BG?

    scene bg forest001 with slow_dissolve

    show aethl up cloak hood at ease(offscreenleft, left, 2.0)

    "I step out into the crisp snow, pulling my hood down to get a better view."

    show aethl -hood

    "It has been so long since I last saw this familiar landscape, smelled this familiar forest."

    aeth_int slack mouth_smile "(I'm glad we were able to make it before the roads snowed in.)"

    show aethl mouth_neu

    "A member of the caravan I have been traveling with jogs up to me."

    "Trader" "Aeth! Will you be joining us in town?"

    aeth "No. I'd like to greet my mother first, so I'll be taking a shortcut through the forest."

    "The trader smiles at me, but it seems somewhat strained."

    "Trader" "I guess this is where we part ways then."

    "Trader" "You've been of such great help these past few years. I want you to know you're always welcome back if... things change."

    show aethl mouth_smile brows_sad

    "That isn't possible, but I appreciate the gesture. I have been worried the caravan members resented me."

    aeth "Thank you for your generosity. I hope your trip back to Harvest City goes safely."

    "Trader" "Aye. And you, too. I hope you're able to settle back in quickly."

    hide aethl
    with fast_dissolve

    "I make my rounds one last time, checking in on a few sick and injured travelers and saying a short farewell."

#    "(There shouldn't be anyone I know along this path.)"
#    "I still haven't decided how I will explain my early homecoming."
#    "(I wonder if I can get away with not saying anything...)"
#    "Most people are conditioned to go with the flow, so if you act like something is natural, "
#    "they will often accept unusual behavior without questioning it."
#    "I stop for a few minutes, thinking hard before I reach my decision."
#    "(Right. I'll just go with that then.)"
#    "(If anyone corners me I'll just be infuriatingly vague until they give up.)"

## I feel like this scene is a little heavy-handed? I want to drop a few mentions that Aeth is
## leaving the caravan with baggage, but don't want to hit them repeatedly over the head with it.

    #Kayen's house exterior BG

    "The sun is barely creeping out from behind the horizon when I reach my mother's house."

    "I heave open the heavy oak door and announce myself."

    scene bg kitchen #Replace with Kayen's house interior BG
    show aethl cloak at left with slow_dissolve

    aeth "Mother, I'm home. Are you there?"

    "The room is dimly lit, and I hear a shuffling sound coming from the back."

    "My mother scrambles forward, looking disheveled."

    $ kayen_pose = 'hand_hair'
    show kayen neu at ease(offscreenright, center, 2.0)

    kayen "Aeth-- What are you doing back this time of year?"

    show aethl mouth_frown eyes_wide brows_up

    $ kayen_pose = 'arms_down'
    "I think I see the shadow of another person back there..."

    aeth_int "(Oops. I must have interrupted. Sorry, Mom.)"

    aeth mouth_neu eyes_neu mouth_neu "I started missing home, so I came back early."

    aeth crossed brows_sad "Would it be okay for me to stay over for a bit?"

    aeth brows_neu "I plan on seeing Master Elaine tomorrow to see if she needs help around the shop."

    "She stares at me, a bit too hard, before replying."

    $ kayen_pose = 'arm_up'

    kayen "Of course! You're always welcome."

    show aethl mouth_smile

    kayen "You've been traveling for so long, it will be good to have you around again."

    $ kayen_pose = 'arm_down'

    show aethl slack

    "A wry grin spreads across her face."

    kayen "Master Elaine has been so busy since Mikael started his own shop, I'm sure she'll work you to the bone."

    show aethl mouth_neu

    kayen "Alright, don't just stand in the doorway, bring your things in! You must be exhausted."

    scene bg cellar #Replace with Kayen's house bedroom BG
    with slow_dissolve

    "I dump my bag onto the floor and start preparing for dinner."

    scene bg black
    with slow_dissolve

    #Insert dinner scene with Kayen and Sherylle

    black_screen "I lay down as sleep takes me, exhausted from my long journey."

    $ day_cnt += 1
    $ calendar.next()


label day002:

    $ day002_evt = True

    scene bg forest002 #Replace with town back street BG
    with slow_dissolve

    "The next day, I decide to head into town."

    show aethl -cloak at ease(offscreenleft, left, 2.0)

    #Apothecary shop exterior BG

    "As I approach my master's shop, I see a small child hiding around the corner."

    show aethl ears_half brows_up

    $ lufte_facing = 'right'
    show lufte neu at right
    with dissolve

    "Child" "..."

    show aethl ears_down brows_neu at ease(left, center, 3.0)

    aeth "Do you need any help?"

    show lufte neu at surprised(right)
    $ lufte_facing = 'left'

    "The child seems surprised to hear a voice behind them and jumps slightly. I stare blankly at them, waiting for a response."

    show lufte neu at linear(right, offscreenright, 4.0)

    "Instead of responding, they back away slowly and then run around a corner."

    hide lufte

    show aethl mouth_frown brows_up

    "I stare after them for a moment, considering if I need to go after them. But it doesn't look like they were hurting anything, so I go about my business."

    scene bg apothecary
    show elaine neu at right
    with slow_dissolve

    "When I enter the shop, Master Elaine is busily preparing the morning's medication."

    elaine "Aeth! My dear, you are certainly home early, aren't you? Well, I'm sure there's a long explanation for that, but we simply don't have the time."

    elaine "I expect you've been practicing while you're on the road?"

    "She doesn't wait for an answer before hurriedly shoving an assortment of bottles and tools at me."

    elaine "Then this should be easy for you. I'll need you to prepare some dried X, a Y tincture, and get the Z started."

    hide elaine

    "CRAFTING TUTORIAL YAAAAAY"

    #Good place for a tutorial on crafting. Add needed herbs to Aeth's inventory

    "Master Elaine keeps me busy all morning, and I'm at my wits end trying to keep up with her."

    "They are all very simple recipes that I've been using during my travels, but I usually don't make so many at once."

    "It's nice to have all the tools I need on hand-- I couldn't afford to travel with them all-- but the shop is so cluttered that it's difficult to find what I need."

    "Master Elaine somehow seems to know exactly where everything is, so there must be a method to her madness, but I can't make any sense of it."

    "Maybe she's just been living in filfth for so long she's developed a sixth sense."

    "As I'm finishing up the latest order, I hear the entrance bell ring."

    "Elaine is shuffling around in the back, so I will have to deal with the customer by myself."

    show aethr slack mouth_neu brows_neu at right

    aeth "I'll be right with you!"

    "Hastily bottling the brew, I make sure nothing is liable to get knocked off the table and turn towards the shop front."

    show mikael neu at left
    $ mikael_pose = 'hand_ear'
    $ mikael_facing = 'right'

    "Rather than a customer, I see a familiar face-- Mikael, who apprenticed under Master Elaine at the same time I did."

    mikael "Aeth! I didn't realize you were back in town."

    aeth "I just got in yesterday. How have you been, Mikael?"

    mikael "I've been doing quite well-- I opened my own shop last year. I'm actually here today to put in an order with Master Elaine."

    mikael "There have been a lot more infections this month, and I ran out of stock earlier than expected."

    show aethr mouth_smile

    aeth "Congratulations, I'll have to stop by soon. Master Elaine is in the back, but I can take your order down and make sure she sees it."

    mikael "That would be a big help, thank you."

    "He pulls a piece of parchment out from his vest pocket and hands it to me."

    mikael "I've got to get back to the shop, but you need to come by for dinner."

    "He reaches down and ruffles my hair, just like he did when we were kids."

    mikael "You've grown so much! I can catch you up on what you've missed, and I know I'd love to hear stories from your journey."

    show aethr mouth_neu

    aeth "Of course. I'll probably be busy for a few days helping Master Elaine with back-orders, but I'll come over soon."

    "He waves and disappears out the front door."

    #More tutorial!

    scene bg black
    with slow_dissolve

    black_screen "I spend the rest of the day filling orders for Master Elaine, and collapse as soon as I get home."

    $ day_cnt += 1
    $ calendar.next()


label day003:

    $ day003_evt = True

    scene bg kitchen #Replace with Kayen's house kitchen BG
    with slow_dissolve

    "I get up early the next day and start making breakfast."

    show aethr at center

    "I've always been an early riser, and often made breakfast for my mother before I left."

    "Every time I visited one of her partners would mention that she'd not been taking care of herself, and was spending the night at their place to mooch."

    "She's gotten better about it over the years, but I still end up cooking for her out of habit."

    #Food porn!

    "When I'm done, I lay the food out on the table and start eating. Who knows when she'll be up, and I need to get to the shop before it opens."

    kayen "FOOD"


    scene bg forest002 #Replace with town backstreet BG
    with slow_dissolve

    "Faster than I can register, the morning is over. Elaine sent me out to pick up supplies and deliver medications in town."

    "I started with deliveries, figuring that I'd then only have to carry supplies on the way home."

    #Orthrus' house exterior BG

    "I approach a small house on the outskirts of town."

    show aethl mouth_frown brows_up at ease(offscreenleft, left, 2.0)

    aeth "Hm, this seems to be the right place."

    show aethl mouth_neu brows_neu

    "Apparently a young man lives here named Orthrus, and I am supposed to deliver medication for his younger sister."

    "As I approach the door, a voice stops me."

    show aethl ears_half eyes_wide brows_angry

    #Orthrus introduction CG

    $ orthrus_pose = 'arms_up'
    $ orthrus_facing = 'right'
    show orthrus wary at left behind aethl
    with dissolve

    "Young Man" "You have business with me?"

    show aethl ears_down mouth_frown eyes_half

    "He leans over me from behind, inches away from my ear. I did't hear him approach, and the sudden closeness causes me to instinctively tense up."

    aeth "I'm here to deliver medicine. Master Elaine sent me."

    $ orthrus_facing = 'left'
    $ orthrus_pose = 'arms_crossed'
    show orthrus smile at ease(left, center, 2.0)

    show aethl mouth_neu

    "He steps back, and I'm able to relax."

    orthrus "Ah, that'll be for me. Thanks for dropping them by, we'd just about run out."

    show aethl mouth_neu eyes_neu

    show orthrus grin
    $ orthrus_pose = 'hands_hips'

    "A wide grin spreads across his face as he reaches out and takes the bag."

    orthrus "You're Aeth, yeah? Kayen's kid? We met a few times when we were younger, dunno if you remember me?"

    show aethl brows_neu

    "I remember that Orthrus's family ran a merchant caravan, and he and his sister often traveled with them away from town."

    show orthrus smile

    "By the time they disappeared, I had already left on my journey, and because of that I haven't had much interaction with either sibling."

    "It was possible we'd seen each other in passing, but I would have a hard time picking his face out of a crowd."

    "I've learned that being so direct was considered rude by most, though, and remain silent unsure of what to say in response."

    show orthrus sad
    $ orthrus_pose = 'arms_crossed'

    orthrus "Er, it was a long time ago in any case. If you're helping out at Elaine's shop I'm sure we'll see more of each other from now on."

    show orthrus grin
    $ orthrus_pose = 'hands_hips'

    orthrus "We'll just call this our first meeting then-- thanks in advanced for your hard work! These meds make life a lot easier."

    "I tip my head towards Orthrus in a greeting and reply"

    aeth "Thank you for your patronage."

    "As I turned to leave, Orthrus waves me off cheekily."

    hide orthrus
    hide aeth

    #Town back street BG

    "That ended up being a bit more stressful than I'd anticipated, but I figure it worked out okay."

    #Item shop exterior BG

    "The next stop on my agenda is the general store. I need to pick up some more glass bottles, as well as a few other essentials."

    scene bg itemshop
    with slow_dissolve

    "I walk in and am greeted by the shopkeeper, Harte."

    #need to remove Harte from image, possibly livecomp

    show harte neu at right

    harte "Aeth! I heard you were back in town early. Elaine got you running errands already?"

    show aethl crossed mouth_smile at left

    "I give a small smile."

    aeth "You know Master Elaine. She goes at her own pace, and anyone around will get dragged right along."

    $ harte_pose = 'pages'

    harte "Haha, you got that right! So, she send you for the regular refills?"

    aeth slack mouth_neu "The regular, plus an extra case of containers and wax."

    $ harte_pose = 'book'

    harte "I'm on it!"

    hide harte
    with dissolve

    "Harte disappears into the back room for a moment, then comes out with a large, heavy box. She places it on the counter, then adds a few extra items from the supply shelf."

    show harte neu at right

    harte "This should get you set up. You okay to carry all that?"

    aeth "I'll be fine, thanks."

    $ harte_pose = 'leaning'

    show aethl mouth_smile

    harte "They put you to work on the caravan, eh? Haha, good to see you back again in any case. Feel free to drop by anytime you need something!"

    aeth "I will-- have a good day."

    scene bg forest002 #Replace with town back street BG
    with slow_dissolve

    "I leave the shop and make my way toward the last errand."

    #Town main street BG

    "I take the main street through the center of town and end up in front of a shop with a sign that wasn't there last time I was here."

    #Mikael's shop exterior BG

    "It shows the Healer's crest, just like my master's shop. I step in and take a look around."

    scene bg apothecary #Replace with Mikael's shop interior BG
    with slow_dissolve

    "The front of the shop has a more clinical feel than Master Elaine's-- it is missing the racks of dried herbs and general clutter."

    $ mikael_pose = 'arms_crossed'
    show mikael neu at center

    "Instead, there are more seats, and a curtain near the back of the room. Not long after the door shut behind me a familiar figure steps out from behind the counter."

    show aethl mouth_smile at left

    aeth "Mikael?"

    $ mikael_pose = 'arms_down'

    mikael "Aeth, it's good to see you back in town. Sorry for the delay, I was just wiping down the examination table."

    show aethl ears_half brows_up

    aeth "No, it's fine. I hear this place is yours? It's nice."

    show aethl ears_down brows_neu

    mikael "Ah, right-- you were gone quite a while this time. I opened shop near the beginning of last year, with Master Elaine's blessings of course."

    mikael "She had been looking to step back from Guild work, so I've been taking on more of the administrative tasks. I've not quite taken over as representative, but..."

    $ mikael_pose = 'hand_ear'

    mikael "Master Elaine has been wanting to tell the Healer's in Harvest City to get off her back for a while, haha."

    "His face emanates warmth, and I can't help but smile at the image of Master Elaine chasing the powerful guild members out of her shop."

    $ mikael_pose = 'arms_down'

    mikael "Ahem, in any case, I'm guessing Master Elaine has you running her errands?"

    aeth "Yes, I'm here to pick up some distilled alcohol, and a few other specialty items."

    "Mikael looks down and sees the fairly large and heavy box Aeth is carrying."

    mikael "Well, I was just planning on closing the shop for a lunch break, why don't I help you take these back? That box looks pretty heavy."

    aeth "I've got this covered. But I wouldn't mind the company on the way back. It's been a while, it would be good to catch up."

    mikael "Alright, just give me a moment to pack up those supplies."

    scene bg black
    with dissolve
    with Pause (0.5)

    scene bg forest002
    with dissolve

    "As we walk back together, Mikael catches me up on what I've missed while I've been gone."

    "When we get to the shop we part ways."

    scene bg apothecary

    show aethl mouth_neu at left

    aeth "Master Elaine, I've finished the deliveries and brought the supplies"

    show elaine neu at right

    elaine "Ah, good! Put them over there and help me with this-- NAME will be coming by any moment to pick it up."

    "The shop is a disaster, but I try to clear some space for the new supplies."

    aeth_int "I'm amazed Master Elaine can find anything in here, but she must have some kind of system because she keeps filling orders."

    aeth_int "I should clean when I get the chance though. Even if she can figure out where everything goes, working in this clutter will stress me out."

    #Tutorial maybe?

    "I spend the rest of the day laboring under Master Elaine's tutilage, refreshing my memory on various medicines I didn't have the resources to make on the road."

    jump apothecary_shop


label day002_itemshop:

    $ day002_itemshop_evt = True

    scene bg itemshop

    "It is the second day of the game."

    show harte neu at right

    harte "You should only see this on your second day of the game."

    harte "You should only see this if you are in the item shop."

    hide harte

    "You should only see this event one time."

    jump item_shop
