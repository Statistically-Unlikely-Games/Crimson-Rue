# In the following example, an encyclopaedia is created inside an "init python" block.
# This allows an encyclopaedia's content to be independent of the saved games. 
# ie: Whenever encyclopaedia content is unlocked, it's unlocked for all save games.
# If you want an encyclopaedia that is bound to a save game file, create the encyclopaedia in a "python" block inside the "start" label.
# Then, for the "locked" argument in each entry, don't use a persistent variable.    

init python:

    #Variables to hold the text.
    
    lorem1 = "Thistle. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. Sed non dapibus augue, quis hendrerit diam. Quisque bibendum turpis vitae orci iaculis volutpat. Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. Curabitur laoreet posuere orci eu eleifend. Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. Duis venenatis sem eu ipsum condimentum adipiscing. Ut vel augue ut velit bibendum varius pharetra nec ligula. Duis eu sollicitudin mauris. Praesent vestibulum ligula vel ligula condimentum dignissim. Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. Etiam posuere fringilla purus."
    lorem2 = "Crown Flower. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. Sed non dapibus augue, quis hendrerit diam. Quisque bibendum turpis vitae orci iaculis volutpat. Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. Curabitur laoreet posuere orci eu eleifend. Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. Duis venenatis sem eu ipsum condimentum adipiscing. Ut vel augue ut velit bibendum varius pharetra nec ligula. Duis eu sollicitudin mauris. Praesent vestibulum ligula vel ligula condimentum dignissim. Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. Etiam posuere fringilla purus."
#    lorem3 = "Black Rizeria. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. Sed non dapibus augue, quis hendrerit diam. Quisque bibendum turpis vitae orci iaculis volutpat. Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. Curabitur laoreet posuere orci eu eleifend. Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. Duis venenatis sem eu ipsum condimentum adipiscing. Ut vel augue ut velit bibendum varius pharetra nec ligula. Duis eu sollicitudin mauris. Praesent vestibulum ligula vel ligula condimentum dignissim. Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. Etiam posuere fringilla purus."
    lorem4 = "Dandelion. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. Sed non dapibus augue, quis hendrerit diam. Quisque bibendum turpis vitae orci iaculis volutpat. Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. Curabitur laoreet posuere orci eu eleifend. Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. Duis venenatis sem eu ipsum condimentum adipiscing. Ut vel augue ut velit bibendum varius pharetra nec ligula. Duis eu sollicitudin mauris. Praesent vestibulum ligula vel ligula condimentum dignissim. Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. Etiam posuere fringilla purus."
#    lorem5 = "Nanairoha. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. Sed non dapibus augue, quis hendrerit diam. Quisque bibendum turpis vitae orci iaculis volutpat. Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. Curabitur laoreet posuere orci eu eleifend. Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. Duis venenatis sem eu ipsum condimentum adipiscing. Ut vel augue ut velit bibendum varius pharetra nec ligula. Duis eu sollicitudin mauris. Praesent vestibulum ligula vel ligula condimentum dignissim. Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. Etiam posuere fringilla purus."
    lorem6 = "Marsh Marigold. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. Sed non dapibus augue, quis hendrerit diam. Quisque bibendum turpis vitae orci iaculis volutpat. Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. Curabitur laoreet posuere orci eu eleifend. Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. Duis venenatis sem eu ipsum condimentum adipiscing. Ut vel augue ut velit bibendum varius pharetra nec ligula. Duis eu sollicitudin mauris. Praesent vestibulum ligula vel ligula condimentum dignissim. Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. Etiam posuere fringilla purus."
#    lorem7 = "Herb 07. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. Sed non dapibus augue, quis hendrerit diam. Quisque bibendum turpis vitae orci iaculis volutpat. Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. Curabitur laoreet posuere orci eu eleifend. Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. Duis venenatis sem eu ipsum condimentum adipiscing. Ut vel augue ut velit bibendum varius pharetra nec ligula. Duis eu sollicitudin mauris. Praesent vestibulum ligula vel ligula condimentum dignissim. Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. Etiam posuere fringilla purus."
#    lorem8 = "Herb 08. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. Sed non dapibus augue, quis hendrerit diam. Quisque bibendum turpis vitae orci iaculis volutpat. Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. Curabitur laoreet posuere orci eu eleifend. Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. Duis venenatis sem eu ipsum condimentum adipiscing. Ut vel augue ut velit bibendum varius pharetra nec ligula. Duis eu sollicitudin mauris. Praesent vestibulum ligula vel ligula condimentum dignissim. Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. Etiam posuere fringilla purus."
#    lorem9 = "Herb 09. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. Sed non dapibus augue, quis hendrerit diam. Quisque bibendum turpis vitae orci iaculis volutpat. Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. Curabitur laoreet posuere orci eu eleifend. Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. Duis venenatis sem eu ipsum condimentum adipiscing. Ut vel augue ut velit bibendum varius pharetra nec ligula. Duis eu sollicitudin mauris. Praesent vestibulum ligula vel ligula condimentum dignissim. Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. Etiam posuere fringilla purus."
#    lorem10 = "Herb 10. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. Sed non dapibus augue, quis hendrerit diam. Quisque bibendum turpis vitae orci iaculis volutpat. Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. Curabitur laoreet posuere orci eu eleifend. Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. Duis venenatis sem eu ipsum condimentum adipiscing. Ut vel augue ut velit bibendum varius pharetra nec ligula. Duis eu sollicitudin mauris. Praesent vestibulum ligula vel ligula condimentum dignissim. Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. Etiam posuere fringilla purus."
    lorem11 = "Sage. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. Sed non dapibus augue, quis hendrerit diam. Quisque bibendum turpis vitae orci iaculis volutpat. Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. Curabitur laoreet posuere orci eu eleifend. Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. Duis venenatis sem eu ipsum condimentum adipiscing. Ut vel augue ut velit bibendum varius pharetra nec ligula. Duis eu sollicitudin mauris. Praesent vestibulum ligula vel ligula condimentum dignissim. Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. Etiam posuere fringilla purus."
    lorem12 = "Blackberry. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. Sed non dapibus augue, quis hendrerit diam. Quisque bibendum turpis vitae orci iaculis volutpat. Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. Curabitur laoreet posuere orci eu eleifend. Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. Duis venenatis sem eu ipsum condimentum adipiscing. Ut vel augue ut velit bibendum varius pharetra nec ligula. Duis eu sollicitudin mauris. Praesent vestibulum ligula vel ligula condimentum dignissim. Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. Etiam posuere fringilla purus."
    lorem13 = "Oak. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. Sed non dapibus augue, quis hendrerit diam. Quisque bibendum turpis vitae orci iaculis volutpat. Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. Curabitur laoreet posuere orci eu eleifend. Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. Duis venenatis sem eu ipsum condimentum adipiscing. Ut vel augue ut velit bibendum varius pharetra nec ligula. Duis eu sollicitudin mauris. Praesent vestibulum ligula vel ligula condimentum dignissim. Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. Etiam posuere fringilla purus."
    lorem14 = "Garlic. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. Sed non dapibus augue, quis hendrerit diam. Quisque bibendum turpis vitae orci iaculis volutpat. Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. Curabitur laoreet posuere orci eu eleifend. Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. Duis venenatis sem eu ipsum condimentum adipiscing. Ut vel augue ut velit bibendum varius pharetra nec ligula. Duis eu sollicitudin mauris. Praesent vestibulum ligula vel ligula condimentum dignissim. Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. Etiam posuere fringilla purus."
    lorem15 = "Laurel. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. Sed non dapibus augue, quis hendrerit diam. Quisque bibendum turpis vitae orci iaculis volutpat. Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. Curabitur laoreet posuere orci eu eleifend. Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. Duis venenatis sem eu ipsum condimentum adipiscing. Ut vel augue ut velit bibendum varius pharetra nec ligula. Duis eu sollicitudin mauris. Praesent vestibulum ligula vel ligula condimentum dignissim. Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. Etiam posuere fringilla purus."
    lorem16 = "Hyssop. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. Sed non dapibus augue, quis hendrerit diam. Quisque bibendum turpis vitae orci iaculis volutpat. Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. Curabitur laoreet posuere orci eu eleifend. Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. Duis venenatis sem eu ipsum condimentum adipiscing. Ut vel augue ut velit bibendum varius pharetra nec ligula. Duis eu sollicitudin mauris. Praesent vestibulum ligula vel ligula condimentum dignissim. Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. Etiam posuere fringilla purus."
    lorem17 = "Mint. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. Sed non dapibus augue, quis hendrerit diam. Quisque bibendum turpis vitae orci iaculis volutpat. Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. Curabitur laoreet posuere orci eu eleifend. Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. Duis venenatis sem eu ipsum condimentum adipiscing. Ut vel augue ut velit bibendum varius pharetra nec ligula. Duis eu sollicitudin mauris. Praesent vestibulum ligula vel ligula condimentum dignissim. Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. Etiam posuere fringilla purus."
    lorem18 = "Oregano. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. Sed non dapibus augue, quis hendrerit diam. Quisque bibendum turpis vitae orci iaculis volutpat. Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. Curabitur laoreet posuere orci eu eleifend. Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. Duis venenatis sem eu ipsum condimentum adipiscing. Ut vel augue ut velit bibendum varius pharetra nec ligula. Duis eu sollicitudin mauris. Praesent vestibulum ligula vel ligula condimentum dignissim. Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. Etiam posuere fringilla purus."
    lorem19 = "Parsley. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. Sed non dapibus augue, quis hendrerit diam. Quisque bibendum turpis vitae orci iaculis volutpat. Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. Curabitur laoreet posuere orci eu eleifend. Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. Duis venenatis sem eu ipsum condimentum adipiscing. Ut vel augue ut velit bibendum varius pharetra nec ligula. Duis eu sollicitudin mauris. Praesent vestibulum ligula vel ligula condimentum dignissim. Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. Etiam posuere fringilla purus."
    lorem20 = "Barage. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. Sed non dapibus augue, quis hendrerit diam. Quisque bibendum turpis vitae orci iaculis volutpat. Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. Curabitur laoreet posuere orci eu eleifend. Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. Duis venenatis sem eu ipsum condimentum adipiscing. Ut vel augue ut velit bibendum varius pharetra nec ligula. Duis eu sollicitudin mauris. Praesent vestibulum ligula vel ligula condimentum dignissim. Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. Etiam posuere fringilla purus."
     
    cras = "Cras pretium, tellus ac tristique dapibus, mauris eros convallis libero, nec porta urna leo sed mi. Quisque non metus ac lacus sodales blandit. Maecenas dapibus justo vitae hendrerit placerat. Phasellus mollis sem nunc, sed porta ligula ullamcorper sit amet. Vivamus posuere vestibulum velit, nec facilisis metus hendrerit sit amet. Vivamus vulputate cursus massa sit amet sagittis. Donec ullamcorper arcu sit amet nibh elementum posuere. Suspendisse lectus ligula, luctus sit amet placerat et, molestie vel diam. Donec suscipit ut urna pulvinar molestie. Suspendisse suscipit placerat ligula, ac mattis neque malesuada ut. Cras aliquet malesuada mauris eu venenatis. Sed dapibus quis leo at ultricies. Integer laoreet elit semper ante hendrerit hendrerit. Ut eget nisl justo. Duis sit amet dolor lectus. Aenean aliquet porttitor pellentesque."
    infeu = "In feugiat ut magna vitae tincidunt. Suspendisse mi odio, tincidunt a ante in, consectetur iaculis lacus. Aenean non mi vitae risus congue bibendum ut id magna. Sed ornare sit amet nulla eu tempor. Sed aliquam nisi nisl, in auctor mauris convallis non. Suspendisse nec lacus tristique erat sodales auctor quis sed est. Nullam vitae feugiat dui. Maecenas tempor, urna quis ullamcorper accumsan, ligula leo tincidunt justo, sagittis vulputate nulla dui quis tellus. Ut felis lacus, tempus eget bibendum id, feugiat sit amet dolor. Proin cursus at risus hendrerit scelerisque. Sed posuere lorem non lacus aliquam, nec faucibus quam tempus. Praesent eu velit in magna bibendum interdum."
    morbi = "Morbi lobortis ipsum felis, eget rutrum nulla rhoncus et. Ut et interdum lorem. Quisque sed mi vitae enim pulvinar ultricies id id tellus. Nunc non lectus nibh. Pellentesque id dui elementum, lacinia velit a, luctus urna. Donec tempus augue et diam pretium commodo. Phasellus bibendum leo ut augue hendrerit sollicitudin. Quisque et tellus at tortor fringilla pellentesque."
    mauris = "Mauris et risus at elit pharetra gravida. Nulla in est magna. Integer in pulvinar mauris. Etiam diam felis, sollicitudin vel nisi ac, rutrum bibendum quam. Sed mattis sodales est, in ultricies felis commodo et. Cras tempor tortor at viverra auctor. Suspendisse a imperdiet lacus, non auctor enim. Vivamus vel aliquam ligula. Duis viverra volutpat metus, quis scelerisque nibh dictum in. Fusce imperdiet posuere quam quis ultricies. In hac habitasse platea dictumst. Cras dignissim felis nibh, in consectetur dolor luctus eu. Quisque adipiscing turpis massa, ut ultricies dolor aliquam eu. Maecenas ac libero porttitor, bibendum libero ac, dapibus enim."
    wine = "Wine, so good."
    wine2 = "More Wine"
    wine3 = "More Wine 3x"
    
    #A list of strings being used instead of a single string. The default UI will show this as paragraphs.
    women = [
    "Who does not Love Wine Wife & Song will be a Fool for his Lifelong!",
    "Wine, women, and song is a hendiatris that endorses hedonistic lifestyles or behaviours. In modern times, it is usually seen in the form sex, drugs, and rock 'n' roll.",
    ]

    #Variables to hold the image paths.
    en1_image = "enc/Botanical_Thistle.png"
    en1_2_image = "enc/Botanical_Crown Flower.png"
#    en1_3_image = "enc/Botanical_Black Rizeria.png"
    en1_4_image = "enc/Botanical_Dandelion.png"
#    en1_5_image = "enc/Botanical_Nanairoha.png"
    en1_6_image = "enc/Botanical_Marsh Marigold.png"
#    en1_7_image = "enc/Botanical_Thistle.png"
#    en1_8_image = "enc/Botanical_Thistle.png"
#    en1_9_image = "enc/Botanical_Thistle.png"
#    en1_10_image = "enc/Botanical_Thistle.png"
    en1_11_image = "enc/Botanical_Sage.png"
    en1_12_image = "enc/Botanical_Blackberry.png"
    en1_13_image = "enc/Botanical_Oak.png"
    en1_14_image = "enc/Botanical_Garlic.png"
    en1_15_image = "enc/Botanical_Laurel.png"
    en1_16_image = "enc/Botanical_Hyssop.png"
    en1_17_image = "enc/Botanical_Mint.png"
    en1_18_image = "enc/Botanical_Oregano.png"
    en1_19_image = "enc/Botanical_Parsley.png"
    en1_20_image = "enc/Botanical_Borage.png"
    
    en2_image = "enc/1381014062018.jpg"
    en3_image = "enc/Rtx-011.jpg"
    en4_image = "enc/Xord_concept.jpg"
    en7_image = "enc/Thanatos_sprite.png"

    #Define an encyclopaedia object.
    #showLockedButtons=False will not display locked "???" entries on the list screen.
    #showLockedEntry=False will prevent the player from viewing the locked entry.
    encyclopaedia = Encyclopaedia(showLockedButtons=True, showLockedEntry=True) 
    
    #If the encyclopaedia is save game independent, run this function to generate the persistent status variables. 
    #If the encyclopaedia is unique for each save game, comment out or delete this.
    #entries_total is the total number of EncEntries the Encyclopaedia will hold.
    #master_key and name are what determines the name of the status variables and the name of each key.
    #only change master_key and name if you need multiple encyclopaedias in a game.
    encyclopaedia.setPersistentStatus(entries_total=7, master_key="new", name="new")
    
    #Add all the subjects the Encyclopaedia will have.
    encyclopaedia.addSubjects("Herb Identification", "Medical Journals")

    #Here we define each Encyclopaedia Entry
    #The arguments are: number, name, text, subject, status, locked, image
    #status should always be from the persistent.new_dict or it won't save
    #if locked=False, entry will always be visible, even if new game hasn't been started
    en1 = EncEntry(1,"Lorem",lorem1, "Herb Identification", status=persistent.new_dict["new_00"], locked=False, image=en1_image)
    en2 = EncEntry(2,"Cras",cras, "Herb Identification", status=persistent.new_dict["new_01"],  locked=False, image=en2_image)
    en3 = EncEntry(3,"In", infeu, "Herb Identification", status=persistent.new_dict["new_02"], locked=False, image=en3_image)
    en4 = EncEntry(4,"Morbi", morbi, "Herb Identification", status=persistent.new_dict["new_03"], locked=persistent.en4_locked, image=en4_image, locked_image=None)
    en5 = EncEntry(5,"Mauris",mauris, "Medical Journals", status=persistent.new_dict["new_04"], locked=False)
    en6 = EncEntry(6,"Wine",wine, "Medical Journals", status=persistent.new_dict["new_05"], locked=persistent.en6_locked)
    en7 = EncEntry(7,"Women",women, "Medical Journals", status=persistent.new_dict["new_06"], locked=persistent.en7_locked, image=en7_image, locked_image=None)
  
    #Add all entries and sub-entries in an init block.
    encyclopaedia.addEntries(en1,en2,en3,en4,en5,en6,en7) 
    #addEntry auto-sorts when adding.
    #en4 and en6 won't be viewed at the start because they're locked by persistent data.
    #After they're unlocked, they'll be available whenever the game loads. 

    #When creating sub-entries, the main entry is considered page 1, always start at 2
    en1_2 = EncEntry(2,"Crown Flower",lorem2,"Herb Identification", locked=False, image=en1_2_image)
#    en1_3 = EncEntry(2,"Black Rizeria",lorem3,"Herb Identification", locked=False, image=en1_3_image)
    en1_4 = EncEntry(2,"Dandelion",lorem4,"Herb Identification", locked=False, image=en1_4_image)
#    en1_5 = EncEntry(2,"Nanairoha",lorem5,"Herb Identification", locked=False, image=en1_5_image)
    en1_6 = EncEntry(2,"Marsh Marigold",lorem6,"Herb Identification", locked=False, image=en1_6_image)
#    en1_7 = EncEntry(2,"Herb 7",lorem7,"Herb Identification", locked=False, image=en1_7_image)
#    en1_8 = EncEntry(2,"Herb 8",lorem8,"Herb Identification", locked=False, image=en1_8_image)
#    en1_9 = EncEntry(2,"Herb 9",lorem9,"Herb Identification", locked=False, image=en1_9_image)
#    en1_10 = EncEntry(2,"Herb 10",lorem10,"Herb Identification", locked=False, image=en1_10_image)
    en1_11 = EncEntry(2,"Sage",lorem11,"Herb Identification", locked=False, image=en1_11_image)
    en1_12 = EncEntry(2,"Blackberry",lorem12,"Herb Identification", locked=False, image=en1_12_image)
    en1_13 = EncEntry(2,"Oak",lorem13,"Herb Identification", locked=False, image=en1_13_image)
    en1_14 = EncEntry(2,"Garlic",lorem14,"Herb Identification", locked=False, image=en1_14_image)
    en1_15 = EncEntry(2,"Laurel",lorem15,"Herb Identification", locked=False, image=en1_15_image)
    en1_16 = EncEntry(2,"Hyssop",lorem16,"Herb Identification", locked=False, image=en1_16_image)
    en1_17 = EncEntry(2,"Mint",lorem17,"Herb Identification", locked=False, image=en1_17_image)
    en1_18 = EncEntry(2,"Oregano",lorem18,"Herb Identification", locked=False, image=en1_18_image)
    en1_19 = EncEntry(2,"Parsley",lorem19,"Herb Identification", locked=False, image=en1_19_image)
    en1_20 = EncEntry(2,"Borage",lorem20,"Herb Identification", locked=False, image=en1_20_image)
    
    en2_2 = EncEntry(2,"Cras 2","Cras 2","Herb Identification", locked=False)
    en2_3 = EncEntry(3,"Cras 3","Cras 3","Herb Identification", locked=persistent.en2_3_locked)

    en6_2 = EncEntry(2,"Wine 2",wine2,"Medical Journals", locked=persistent.en6_2_locked)
    en6_3 = EncEntry(3,"Wine 3",wine3,"Medical Journals", locked=persistent.en6_3_locked)

    en1.addSubEntries(en1_2,en1_4,en1_6,en1_11,en1_12,en1_13,en1_14,en1_15,en1_16,en1_17,en1_18,en1_19,en1_20)
    en2.addSubEntries(en2_2,en2_3)
    en6.addSubEntries(en6_2,en6_3)