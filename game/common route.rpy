label intro: 
    
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
            
    "The air is cold, carrying the strong smell of pine, which I've always associated with home."
    
    "This is a test. I need to see how the game deals with very long dialogue and narration. Currently, I have dialogue centered and it should be shorter than the narration, which is unlimited. But unless I know exactly where it will make the cut for dialogue, I can't make a dialogue box. Thus, I need to know how it deals with long text like this."
    
    aeth "This is a test. I need to see how the game deals with very long dialogue and narration. Currently, I have dialogue centered and it should be shorter than the narration, which is unlimited. But unless I know exactly where it will make the cut for dialogue, I can't make a dialogue box. Thus, I need to know how it deals with long text like this."
    
    scene bg forest001 with slow_dissolve
    show aeth neu at easein_left
    
    "I step out into the crisp snow, removing my hood to get a better look."
    
    "It has been so long since I last saw this familiar landscape, smelled this familiar forest."
    
    aeth_int "(I'm glad we were able to make it before the roads snowed in.)"
    
    "A member of the caravan I have been traveling with jogs up to me."
    
    "Trader" "Aeth! Will you be joining us in town?"
    
    aeth "No. I'd like to greet my mother first, so I'll be taking a shortcut through the forest."
    
    "The trader smiles at me, but it seems somewhat strained."
    
    "Trader" "I guess this is where we part ways then."
    
    "Trader" "You've been of such great help these past few years. I want you to know you're always welcome back if... things change."
    
    "That isn't possible, but I appreciate the gesture. I have been worried the caravan members resented me."
    
    aeth "Thank you for your generosity. I hope your trip back to Harvest City goes safely."
    
    "Trader" "Aye. And you, too. I hope you're able to settle back in quickly."
    
    hide aeth
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

    "The sun is barely creeping out from behind the horizon when I reach my mother's house."
    
    "I heave open the heavy oak door and announce myself."
    
    scene bg kitchen
    show aeth neu at left
    with slow_dissolve
    
    aeth "Mother, I'm home. Are you there?"
    
    "The room is dimly lit, and I hear a shuffling sound coming from the back."
    
    "My mother scrambles forward, looking disheveled."
    
    show kayen neu at easein_rightctr
    
    kayen "Aeth-- What are you doing back this time of year?"
    
    "I think I see the shadow of another person back there..."
    
    aeth_int "(Oops. I must have interrupted. Sorry, Mom.)"
    
    aeth "I started missing home, so I came back early."
    
    aeth "Would it be okay for me to stay over for a bit?"
    
    aeth "I plan on seeing Master Elaine tomorrow to see if she needs help around the shop."
    
    "She stares at me, a bit too hard, before replying."
    
    kayen "Of course! You're always welcome."
    
    kayen "You've been traveling for so long, it will be good to have you around again."
    
    "A wry grin spreads across her face."
    
    kayen "Master Elaine has been so busy since Mikael started his own shop, I'm sure she'll work you to the bone."
    
    kayen "Alright, don't just stand in the doorway, bring your things in! You must be exhausted."
    
    scene bg cellar
    with slow_dissolve
    
    "I dump my bag onto the floor and start preparing for dinner."
    
    scene bg black
    with slow_dissolve
    
    "I lay down as sleep takes me, exhausted from my long journey."
    
    scene bg forest002
    with slow_dissolve
    
    "The next day, I decide to head into town."
    
    show aeth neu at left
    with moveinleft
    
    "As I approach my master's shop, I see a small child hiding around the corner."
    
    show lufte neu right at right
    with dissolve
    
    "Child" "..."
    
    show aeth neu at center
    with ease
    
    aeth "Do you need any help?"
    
    show lufte neu at surprised_left
    
    "The child seems surprised to hear a voice behind them and jumps slightly. I stare blankly at them, waiting for a response."
    
    "Instead of responding, they back away slowly and then run around a corner."
    
    hide lufte
    
    "I stare after them for a moment, considering if I need to go after them. But it doesn't look like they were hurting anything, so I go about my business."
    
    scene bg apothecary
    with slow_dissolve
    
    "When I enter the shop, Master Elaine is busily preparing the morning's medication."
    
    show elaine neu at right
    
    elaine "Aeth! My dear, you are certainly home early, aren't you? Well, I'm sure there's a long explanation for that, but we simply don't have the time."
    
    "She hurriedly shoves an assortment of bottles and tools on the counter, and pushes them in my direction."
    
    elaine "I'll need you to prepare some dried X, a Y tincture, and get the Z started."
    
    scene bg forest002
    with slow_dissolve
    
    "Faster than I can register, the morning is over. Elaine sent me out to pick up supplies and deliver medications in town."
    
    "I started with deliveries, figuring that I'd then only have to carry supplies on the way home."
    
    "I approach a small house on the outskirts of town."
    
    show aeth neu at left
    
    aeth "Hm, this seems to be the right place."
    
    "Supposedly a young man lives here named Orthrus, and I am supposed to deliver medication for his younger sister."
    
    "As I approached the door, a voice stops me."
    
    show orthrus neu right at left behind aeth
    
    "Young Man" "You have business with me?"
    
    "He leans over me from behind, inches away from my ear. I did't hear him approach, and the sudden closeness causes me to instinctively tense up."
    
    aeth "Master Elaine sent me to deliver medicine to Orthrus."
    
    show orthrus neu at center
    with ease
    
    "He steps back, and I'm able to relax my muscles."
    
    orthrus "Ah, that'll be for me. Thanks for dropping them by, we'd just about run out."
    
    "A wide grin spreads across his face as he reaches out and takes the bag."
    
    orthrus "You're Aeth, yeah? Kayen's kid? We met a few times when we were younger, dunno if you remember me?"
    
    "I remember that Orthrus's family ran a merchant caravan, and he and his sister often traveled with them away from town."
    
    "By the time they disappeared, I had already left on your journey, and because of this I haven't had much interaction with either sibling."
    
    "It was possible we'd seen each other in passing, but I would have a hard time picking his face out of a crowd."
    
    "I've learned that being so direct was considered rude by most, though, and remain silent unsure of what to say in response."
    
    orthrus "Er, it was a long time ago in any case. If you're helping out at Elaine's shop I'm sure we'll see more of each other from now on."
    
    orthrus "We'll just call this our first meeting then-- thanks in advanced for your hard work! These meds make life a lot easier."
    
    "I tip my head towards Orthrus in a greeting and reply"
    
    aeth "Thank you for your patronage."
    
    "As I turned to leave, Orthrus waves me off cheekily."
    
    hide orthrus
    hide aeth
    
    "That ended up being a bit more stressful than I'd anticipated, but I figure it worked out okay."
    
    "The next stop on my agenda is the general store. I need to pick up some more glass bottles, as well as a few other essentials."
    
    scene bg itemshop
    with slow_dissolve
    
    "I walk in and am greeted by the shopkeeper, Harte."
    
    show harte neu at right
    
    harte "Aeth! I heard you were back in town early. Elaine got you running errands already?"
    
    "I give a small smile."
    
    show aeth neu at left
    
    aeth "You know Master Elaine. She goes at her own pace, and anyone around will get dragged right along."
    
    harte "Haha, you got that right! So, she send you for the regular refills?"
    
    aeth "The regular, plus an extra case of containers and wax."
    
    harte "I'm on it!"
    
    "Harte disappears into the back room for a moment, then comes out with a large, heavy box. She places it on the counter, then adds a few extra items from the supply shelf."
    
    harte "This should get you set up. You okay to carry all that?"
    
    aeth "I'll be fine, thanks."
    
    harte "They put you to work on the caravan, eh? Haha, good to see you back again in any case. Feel free to drop by anytime you need something!"
    
    aeth "I will-- have a good day."
    
    scene bg forest002
    with slow_dissolve
    
    "I leave the shop and make my way toward the last errand."
    
    "I take the main street through the center of town and end up in front of a shop with a sign that wasn't there last time I was here."
    
    "It shows the Healer's crest, just like my master's shop. I step in and take a look around."
    
    scene bg apothecary
    with slow_dissolve
    
    "The front of the shop has a more clinical feel than Master Elaine's-- it is missing the racks of dried herbs and general clutter."
    
    show mikael neu at center
    
    "Instead, there are more seats, and a curtain near the back of the room. Not long after the door shut behind me a familiar figure steps out from behind the counter."
    
    show aeth neu at left
    
    aeth "Mikael?"
    
    mikael "Aeth, it's good to see you. Sorry for the delay, I was just wiping down the examination table."
    
    aeth "No, it's fine. Is this your shop?"
    
    mikael "Ah, right-- you were gone quite a while this time. I opened shop near the beginning of last year, with Master Elaine's blessings of course."
    
    mikael "She had been looking to step back from Guild work, so I've been taking on more of the administrative tasks. I've not quite taken over as representative, but..."
    
    mikael "Master Elaine has been wanting to tell the Healer's in Harvest City to get off her back for a while, haha."
    
    "His face emanates warmth, and I can't help but smile at the image of Master Elaine chasing the powerful guild members out of her shop."
    
    mikael "Ahem, in any case, I'm guessing Master Elaine has you running her errands?"
    
    aeth "Yes, I'm here to pick up some distilled alcohol, and a few other specialty items."
    
    "Mikael looks down and sees the fairly large and heavy box Aeth is carrying."
    
    mikael "Well, I was just planning on closing the shop for a lunch break, why don't I help you take these back? That box looks pretty heavy."
    
    aeth "I've got this covered. But I wouldn't mind the company on the way back. It's been a while, it would be good to catch up."
    
    mikael "Alright, just give me a moment to pack up those supplies."
    
    jump apothecary_shop