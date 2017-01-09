init python:
 
 #Variables to hold the text.
 lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. Sed non dapibus augue, quis hendrerit diam. Quisque bibendum turpis vitae orci iaculis volutpat. Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. Curabitur laoreet posuere orci eu eleifend. Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. Duis venenatis sem eu ipsum condimentum adipiscing. Ut vel augue ut velit bibendum varius pharetra nec ligula. Duis eu sollicitudin mauris. Praesent vestibulum ligula vel ligula condimentum dignissim. Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. Etiam posuere fringilla purus."
 cras = "Cras pretium, tellus ac tristique dapibus, mauris eros convallis libero, nec porta urna leo sed mi. Quisque non metus ac lacus sodales blandit. Maecenas dapibus justo vitae hendrerit placerat. Phasellus mollis sem nunc, sed porta ligula ullamcorper sit amet. Vivamus posuere vestibulum velit, nec facilisis metus hendrerit sit amet. Vivamus vulputate cursus massa sit amet sagittis. Donec ullamcorper arcu sit amet nibh elementum posuere. Suspendisse lectus ligula, luctus sit amet placerat et, molestie vel diam. Donec suscipit ut urna pulvinar molestie. Suspendisse suscipit placerat ligula, ac mattis neque malesuada ut. Cras aliquet malesuada mauris eu venenatis. Sed dapibus quis leo at ultricies. Integer laoreet elit semper ante hendrerit hendrerit. Ut eget nisl justo. Duis sit amet dolor lectus. Aenean aliquet porttitor pellentesque."
 infeu = "In feugiat ut magna vitae tincidunt. Suspendisse mi odio, tincidunt a ante in, consectetur iaculis lacus. Aenean non mi vitae risus congue bibendum ut id magna. Sed ornare sit amet nulla eu tempor. Sed aliquam nisi nisl, in auctor mauris convallis non. Suspendisse nec lacus tristique erat sodales auctor quis sed est. Nullam vitae feugiat dui. Maecenas tempor, urna quis ullamcorper accumsan, ligula leo tincidunt justo, sagittis vulputate nulla dui quis tellus. Ut felis lacus, tempus eget bibendum id, feugiat sit amet dolor. Proin cursus at risus hendrerit scelerisque. Sed posuere lorem non lacus aliquam, nec faucibus quam tempus. Praesent eu velit in magna bibendum interdum."
 morbi = "Morbi lobortis ipsum felis, eget rutrum nulla rhoncus et. Ut et interdum lorem. Quisque sed mi vitae enim pulvinar ultricies id id tellus. Nunc non lectus nibh. Pellentesque id dui elementum, lacinia velit a, luctus urna. Donec tempus augue et diam pretium commodo. Phasellus bibendum leo ut augue hendrerit sollicitudin. Quisque et tellus at tortor fringilla pellentesque."
 mauris = "Mauris et risus at elit pharetra gravida. Nulla in est magna. Integer in pulvinar mauris. Etiam diam felis, sollicitudin vel nisi ac, rutrum bibendum quam. Sed mattis sodales est, in ultricies felis commodo et. Cras tempor tortor at viverra auctor. Suspendisse a imperdiet lacus, non auctor enim. Vivamus vel aliquam ligula. Duis viverra volutpat metus, quis scelerisque nibh dictum in. Fusce imperdiet posuere quam quis ultricies. In hac habitasse platea dictumst. Cras dignissim felis nibh, in consectetur dolor luctus eu. Quisque adipiscing turpis massa, ut ultricies dolor aliquam eu. Maecenas ac libero porttitor, bibendum libero ac, dapibus enim."
 wine = "Wine, so good."
 wine2 = "More Wine"
 wine3 = "More Wine 3x"
 
 #Variables to hold the images.
 en1_image = "enc/1266537434812.png"
 en2_image = "enc/1381014062018.jpg"
 en3_image = "enc/Rtx-011.jpg"
 en4_image = "enc/Xord_concept.jpg"
 
 #Persistent data to hold the "New!" status for each entry
 try:
  persistent.enc00_new = persistent.new_dict["new_00"]
  persistent.enc01_new = persistent.new_dict["new_01"]
  persistent.enc02_new = persistent.new_dict["new_02"]
  persistent.enc03_new = persistent.new_dict["new_03"]
  persistent.enc04_new = persistent.new_dict["new_04"]
  persistent.enc05_new = persistent.new_dict["new_05"]
  persistent.enc06_new = persistent.new_dict["new_06"]
 except:
  pass
 
 persistent.new_dict = {
 "new_00" : persistent.enc00_new,
 "new_01" : persistent.enc01_new,
 "new_02" : persistent.enc02_new,
 "new_03" : persistent.enc03_new,
 "new_04" : persistent.enc04_new,
 "new_05" : persistent.enc05_new,
 "new_06" : persistent.enc06_new
 }

 #All the Encyclopaedia data must be created in an init python block
 encyclopaedia = Encyclopaedia(showLocked=True) #use showLocked=False to not display locked "???" entries on the list screen
 encyclopaedia.addSubjects("Lorem Ipsum", "Virtues")
 
 #Encyclopaedia Entries
 #number, name, text, subject, status, locked, image
 #status should always be from the persistent.new_dict or it won't save
 #if locked=False, entry will always be visible, even if new game hasn't been started
 en1 = EncEntry(1,"Lorem",lorem, "Lorem Ipsum", status=persistent.new_dict["new_00"], locked=False, image=en1_image)
 en2 = EncEntry(2,"Cras",cras, "Lorem Ipsum", status=persistent.new_dict["new_01"],  locked=False, image=en2_image)
 en3 = EncEntry(3,"In", infeu, "Lorem Ipsum", status=persistent.new_dict["new_02"], locked=False, image=en3_image)
 en4 = EncEntry(4,"Morbi", morbi, "Lorem Ipsum", status=persistent.new_dict["new_03"], locked=persistent.en4_locked, image=en4_image)
 en5 = EncEntry(5,"Mauris",mauris, "Lorem Ipsum", status=persistent.new_dict["new_04"], locked=False)
 en6 = EncEntry(6,"Wine",wine, "Virtues", status=persistent.new_dict["new_05"], locked=persistent.en6_locked)
 
 encyclopaedia.addEntries( [1,en1], [2,en2], [3,en3], [4,en4], [5,en5], [6,en6] ) #too clunky. Will change to something like: encyclopaedia.addEntries( en1,en2,en3,en4,en5,en6 ) 
 #addEntry uses [page_number, entry], and auto-sorts when adding.
 #en4 and en6 won't be viewed at the start because they're locked by persistent data.
 #After they're unlocked, they'll be added whenever the game loads. 

 en2_2 = EncEntry(2,"Cras 2","Cras 2","Virtues", locked=persistent.en2_2_locked)
 en2_3 = EncEntry(3,"Cras 3","Cras 3","Virtues", locked=persistent.en2_3_locked)
 
 en6_2 = EncEntry(2,"Wine 2",wine2,"Virtues", locked=persistent.en6_2_locked)
 en6_3 = EncEntry(3,"Wine 3",wine3,"Virtues", locked=persistent.en6_3_locked)

 #When adding sub-entries, the main entry is considered page 01
 en2.addSubEntries( [2,en2_2], [3,en2_3] )
 en6.addSubEntries( [2,en6_2], [3,en6_3] )
 
 #Placeholder text for the entries window if no entries are in the database
 entry_text = "No Data Available"
 
 current_position = 0 #Indicates the current entry open
 sub_current_position = 1 #1 because the main entry is the first page in the sub-entry list