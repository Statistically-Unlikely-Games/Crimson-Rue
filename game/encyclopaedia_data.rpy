# In the following example, an encyclopaedia is created inside an "init python" block.
# This allows an encyclopaedia's content to be independent of the saved games. 
# ie: Whenever encyclopaedia content is unlocked, it's unlocked for all save games.
# If you want an encyclopaedia that is bound to a save game file, create the encyclopaedia in a "python" block inside the "start" label.
# Then, for the "locked" argument in each entry, don't use a persistent variable.    

init python:


    # Variables to hold the image paths. The path is relative to your game/ directory.
    image_getting_started = "enc/getting_started.png"
    image_translations = "enc/translations.png"
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
    
    en2_image = "enc/Botanical_Thistle.png"
    en2_2_image = "enc/Botanical_Crown Flower.png"
#    en2_3_image = "enc/Botanical_Black Rizeria.png"
    en2_4_image = "enc/Botanical_Dandelion.png"
#    en2_5_image = "enc/Botanical_Nanairoha.png"
    en2_6_image = "enc/Botanical_Marsh Marigold.png"
#    en2_7_image = "enc/Botanical_Thistle.png"
#    en2_8_image = "enc/Botanical_Thistle.png"
#    en2_9_image = "enc/Botanical_Thistle.png"
#    en2_10_image = "enc/Botanical_Thistle.png"
    en2_11_image = "enc/Botanical_Sage.png"
    en2_12_image = "enc/Botanical_Blackberry.png"
    en2_13_image = "enc/Botanical_Oak.png"
    en2_14_image = "enc/Botanical_Garlic.png"
    en2_15_image = "enc/Botanical_Laurel.png"
    en2_16_image = "enc/Botanical_Hyssop.png"
    en2_17_image = "enc/Botanical_Mint.png"
    en2_18_image = "enc/Botanical_Oregano.png"
    en2_19_image = "enc/Botanical_Parsley.png"
    en2_20_image = "enc/Botanical_Borage.png"
    
    en3_image = "enc/Botanical_Thistle.png"
    en3_2_image = "enc/Botanical_Crown Flower.png"
#    en3_3_image = "enc/Botanical_Black Rizeria.png"
    en3_4_image = "enc/Botanical_Dandelion.png"
#    en3_5_image = "enc/Botanical_Nanairoha.png"
    en3_6_image = "enc/Botanical_Marsh Marigold.png"
#    en3_7_image = "enc/Botanical_Thistle.png"
#    en3_8_image = "enc/Botanical_Thistle.png"
#    en3_9_image = "enc/Botanical_Thistle.png"
#    en3_10_image = "enc/Botanical_Thistle.png"
    en3_11_image = "enc/Botanical_Sage.png"
    en3_12_image = "enc/Botanical_Blackberry.png"
    en3_13_image = "enc/Botanical_Oak.png"
    en3_14_image = "enc/Botanical_Garlic.png"
    en3_15_image = "enc/Botanical_Laurel.png"
    en3_16_image = "enc/Botanical_Hyssop.png"
    en3_17_image = "enc/Botanical_Mint.png"
    en3_18_image = "enc/Botanical_Oregano.png"
    en3_19_image = "enc/Botanical_Parsley.png"
    en3_20_image = "enc/Botanical_Borage.png"

    en4_image = "enc/Xord_concept.jpg"
    en7_image = "enc/Thanatos_sprite.png"

    # Define an encyclopaedia object.
    encyclopaedia = Encyclopaedia(
        sorting_mode = Encyclopaedia.SORT_NUMBER,
        show_locked_buttons=True,
        show_locked_entry=True,
        entry_screen="encyclopaedia_entry"
    )

    # If the encyclopaedia is save game independent, run this function to generate the persistent status variables. 
    # If the encyclopaedia is unique for each save game, comment out or delete this.
    
    # entries_total is the total number of EncEntries the Encyclopaedia will hold.
    # master_key and name are what determines the name of the status variables and the name of each key.
    # only change master_key and name if you need multiple encyclopaedias in a game.
    persistent_status_flags(
        total=8,
        master_key="new",
        status_name="new_status"
    )

    ################
    # Documentation
    ################

    # Herb Identification vol. 1
    en1 = EncEntry(
        encyclopaedia,
        1,
        "Herb Identification vol. 1",
        [
            "Thistle. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=persistent.new_status["new_01"],
        locked=False,
        image=en1_image,
    )

    en1_2 = EncEntry(
        en1,
        2,
        "Herb Identification vol. 1",
        [
            "Crown Flower. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=False,
        image=en1_2_image,
    )

    en1_3 = EncEntry(
        en1,
        3,
        "Herb Identification vol. 1",
        [
            "Black Rizeria. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=False,
    )
    
    en1_4 = EncEntry(
        en1,
        4,
        "Herb Identification vol. 1",
        [
            "Dandelion. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=False,
        image=en1_4_image,
    )
    
    en1_5 = EncEntry(
        en1,
        5,
        "Herb Identification vol. 1",
        [
            "Nanairoha. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=False,
    )
    
    en1_6 = EncEntry(
        en1,
        6,
        "Herb Identification vol. 1",
        [
            "Marsh Marigold. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=False,
        image=en1_6_image,
    )
    
    en1_7 = EncEntry(
        en1,
        7,
        "Herb Identification vol. 1",
        [
            "Herb 7. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=False,
    )
    
    en1_8 = EncEntry(
        en1,
        8,
        "Herb Identification vol. 1",
        [
            "Herb 8. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=False,
    )
    
    en1_9 = EncEntry(
        en1,
        9,
        "Herb Identification vol. 1",
        [
            "Herb 9. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=False,
    )
    
    en1_10 = EncEntry(
        en1,
        10,
        "Herb Identification vol. 1",
        [
            "Herb 10. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=False,
    )
    
    en1_11 = EncEntry(
        en1,
        11,
        "Herb Identification vol. 1",
        [
            "Sage. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=False,
        image=en1_11_image,
    )
    
    en1_12 = EncEntry(
        en1,
        12,
        "Herb Identification vol. 1",
        [
            "Blackberry. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=False,
        image=en1_12_image,
    )
    
    en1_13 = EncEntry(
        en1,
        13,
        "Herb Identification vol. 1",
        [
            "Oak. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=False,
        image=en1_13_image,
    )
    
    en1_14 = EncEntry(
        en1,
        14,
        "Herb Identification vol. 1",
        [
            "Garlic. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=False,
        image=en1_14_image,
    )
    
    en1_15 = EncEntry(
        en1,
        15,
        "Herb Identification vol. 1",
        [
            "Laurel. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=False,
        image=en1_15_image,
    )
    
    en1_16 = EncEntry(
        en1,
        16,
        "Herb Identification vol. 1",
        [
            "Hyssop. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=False,
        image=en1_16_image,
    )
    
    en1_17 = EncEntry(
        en1,
        17,
        "Herb Identification vol. 1",
        [
            "Mint. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=False,
        image=en1_17_image,
    )
    
    en1_18 = EncEntry(
        en1,
        18,
        "Herb Identification vol. 1",
        [
            "Oregano. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=False,
        image=en1_18_image,
    )
    
    en1_19 = EncEntry(
        en1,
        19,
        "Herb Identification vol. 1",
        [
            "Parsley. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=False,
        image=en1_19_image,
    )
    
    en1_20 = EncEntry(
        en1,
        20,
        "Herb Identification vol. 1",
        [
            "Borage. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=False,
        image=en1_20_image,
    )

    en2 = EncEntry(
        encyclopaedia,
        2,
        "Herb Identification vol. 2",
        [
            "Thistle. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=persistent.new_status["new_01"],
        locked=True,
        image=en2_image,
    )

    en2_2 = EncEntry(
        en2,
        2,
        "Herb Identification vol. 2",
        [
            "Crown Flower. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=True,
        image=en2_2_image,
    )

    en2_3 = EncEntry(
        en2,
        3,
        "Herb Identification vol. 2",
        [
            "Black Rizeria. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=True,
    )
    
    en2_4 = EncEntry(
        en2,
        4,
        "Herb Identification vol. 2",
        [
            "Dandelion. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=True,
        image=en2_4_image,
    )
    
    en2_5 = EncEntry(
        en2,
        5,
        "Herb Identification vol. 2",
        [
            "Nanairoha. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=True,
    )
    
    en2_6 = EncEntry(
        en2,
        6,
        "Herb Identification vol. 2",
        [
            "Marsh Marigold. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=True,
        image=en2_6_image,
    )
    
    en2_7 = EncEntry(
        en2,
        7,
        "Herb Identification vol. 2",
        [
            "Herb 7. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=True,
    )
    
    en2_8 = EncEntry(
        en2,
        8,
        "Herb Identification vol. 2",
        [
            "Herb 8. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=True,
    )
    
    en2_9 = EncEntry(
        en2,
        9,
        "Herb Identification vol. 2",
        [
            "Herb 9. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=True,
    )
    
    en2_10 = EncEntry(
        en2,
        10,
        "Herb Identification vol. 2",
        [
            "Herb 10. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=True,
    )
    
    en2_11 = EncEntry(
        en2,
        11,
        "Herb Identification vol. 2",
        [
            "Sage. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=True,
        image=en2_11_image,
    )
    
    en2_12 = EncEntry(
        en2,
        12,
        "Herb Identification vol. 2",
        [
            "Blackberry. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=True,
        image=en2_12_image,
    )
    
    en2_13 = EncEntry(
        en2,
        13,
        "Herb Identification vol. 2",
        [
            "Oak. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=True,
        image=en2_13_image,
    )
    
    en2_14 = EncEntry(
        en2,
        14,
        "Herb Identification vol. 2",
        [
            "Garlic. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=True,
        image=en2_14_image,
    )
    
    en2_15 = EncEntry(
        en2,
        15,
        "Herb Identification vol. 2",
        [
            "Laurel. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=True,
        image=en2_15_image,
    )
    
    en2_16 = EncEntry(
        en2,
        16,
        "Herb Identification vol. 2",
        [
            "Hyssop. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=True,
        image=en2_16_image,
    )
    
    en2_17 = EncEntry(
        en2,
        17,
        "Herb Identification vol. 2",
        [
            "Mint. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=True,
        image=en2_17_image,
    )
    
    en2_18 = EncEntry(
        en2,
        18,
        "Herb Identification vol. 2",
        [
            "Oregano. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=True,
        image=en2_18_image,
    )
    
    en2_19 = EncEntry(
        en2,
        19,
        "Herb Identification vol. 2",
        [
            "Parsley. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=True,
        image=en2_19_image,
    )
    
    en2_20 = EncEntry(
        en2,
        20,
        "Herb Identification vol. 2",
        [
            "Borage. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=True,
        image=en2_20_image,
    )

    en3 = EncEntry(
        encyclopaedia,
        3,
        "Herb Identification vol. 3",
        [
            "Thistle. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=persistent.new_status["new_01"],
        locked=True,
        image=en3_image,
    )

    en3_2 = EncEntry(
        en3,
        2,
        "Herb Identification vol. 3",
        [
            "Crown Flower. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=True,
        image=en3_2_image,
    )

    en3_3 = EncEntry(
        en3,
        3,
        "Herb Identification vol. 3",
        [
            "Black Rizeria. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=True,
    )
    
    en3_4 = EncEntry(
        en3,
        4,
        "Herb Identification vol. 3",
        [
            "Dandelion. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=True,
        image=en3_4_image,
    )
    
    en3_5 = EncEntry(
        en3,
        5,
        "Herb Identification vol. 3",
        [
            "Nanairoha. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=True,
    )
    
    en3_6 = EncEntry(
        en3,
        6,
        "Herb Identification vol. 3",
        [
            "Marsh Marigold. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=True,
        image=en3_6_image,
    )
    
    en3_7 = EncEntry(
        en3,
        7,
        "Herb Identification vol. 3",
        [
            "Herb 7. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=True,
    )
    
    en3_8 = EncEntry(
        en3,
        8,
        "Herb Identification vol. 3",
        [
            "Herb 8. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=True,
    )
    
    en3_9 = EncEntry(
        en3,
        9,
        "Herb Identification vol. 3",
        [
            "Herb 9. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=True,
    )
    
    en3_10 = EncEntry(
        en3,
        10,
        "Herb Identification vol. 3",
        [
            "Herb 10. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=True,
    )
    
    en3_11 = EncEntry(
        en3,
        11,
        "Herb Identification vol. 3",
        [
            "Sage. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=True,
        image=en3_11_image,
    )
    
    en3_12 = EncEntry(
        en3,
        12,
        "Herb Identification vol. 3",
        [
            "Blackberry. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=True,
        image=en3_12_image,
    )
    
    en3_13 = EncEntry(
        en3,
        13,
        "Herb Identification vol. 3",
        [
            "Oak. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=True,
        image=en3_13_image,
    )
    
    en3_14 = EncEntry(
        en3,
        14,
        "Herb Identification vol. 3",
        [
            "Garlic. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=True,
        image=en3_14_image,
    )
    
    en3_15 = EncEntry(
        en3,
        15,
        "Herb Identification vol. 3",
        [
            "Laurel. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=True,
        image=en3_15_image,
    )
    
    en3_16 = EncEntry(
        en3,
        16,
        "Herb Identification vol. 3",
        [
            "Hyssop. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=True,
        image=en3_16_image,
    )
    
    en3_17 = EncEntry(
        en3,
        17,
        "Herb Identification vol. 3",
        [
            "Mint. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=True,
        image=en3_17_image,
    )
    
    en3_18 = EncEntry(
        en3,
        18,
        "Herb Identification vol. 3",
        [
            "Oregano. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=True,
        image=en3_18_image,
    )
    
    en3_19 = EncEntry(
        en3,
        19,
        "Herb Identification vol. 3",
        [
            "Parsley. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=True,
        image=en3_19_image,
    )
    
    en3_20 = EncEntry(
        en3,
        20,
        "Herb Identification vol. 3",
        [
            "Borage. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "Vivamus in nisl magna. Fusce nec bibendum magna, sed venenatis erat. ",
            "Sed non dapibus augue, quis hendrerit diam. ",
            "Quisque bibendum turpis vitae orci iaculis volutpat. ",
            "Proin venenatis, nunc quis tempus convallis, lectus eros ultrices sem, eu condimentum tellus nisi sed magna. ",
            "Curabitur laoreet posuere orci eu eleifend. ",
            "Vivamus sed dui dignissim, egestas lorem eu, lobortis arcu. ",
            "Duis venenatis sem eu ipsum condimentum adipiscing. ",
            "Ut vel augue ut velit bibendum varius pharetra nec ligula. ",
            "Duis eu sollicitudin mauris. ",
            "Praesent vestibulum ligula vel ligula condimentum dignissim. ",
            "Ut risus velit, laoreet sed pellentesque sed, suscipit in massa. ",
            "Etiam posuere fringilla purus.",
        ],
        "Herb Identification",
        viewed=False,
        locked=True,
        image=en3_20_image,
    )

    placeholders = EncEntry(
        encyclopaedia,
        4,
        "Placeholders",
        [""],
        "Basic Usage"
    )

    # In-Depth
    # Encyclopaedia
    # EncEntry
    # Actions

    encyclopaedia_options = EncEntry(
        encyclopaedia,
        5,
        "Encyclopaedia",
        [
            "Encyclopaedias can take four optional arguments when being created:"
            " \n 1 - The default sorting mode. If not set, will be by number."
            " \n 2 - If locked buttons should be displayed or not. Default is False. Locked buttons will use placeholder values."
            " \n 3 - If locked entries should be displayed or not. Default is False. Locked entries will use placeholder values."
            " \n 4 - The screen to display individual entries on. Default is 'encyclopaedia_entry'."
        ],
        "In-Depth",
        viewed=False,
        locked=False
    )

    customizing_screens = EncEntry(
        encyclopaedia,
        6,
        "Customizing Screens",
        [""],
        "In-Depth",
    )

    translations = EncEntry(
        encyclopaedia,
        7,
        "Translations",
        [
            "Translating the labels used by an Encyclopaedia can be done through the LabelController object.",
            "Every Encyclopaedia is created with a default one that can be replaced.",
        ],
        "In-Depth",
        image=image_translations
    )

    # Sorting
    # Filtering

    # Stress testing
    #for x in range(25, 30):
    #    e = EncEntry(
    #        encyclopaedia,
    #        x,
    #        "Test Entry: " + str(x),
    #        "Test Entry",
    #        "Test Entries",
    #    )


    # When creating sub-entries, the main entry is considered page 1,
    # so always start at 2.

#    locking_unlocking_entries_3 = EncEntry(
#        locking_unlocking_entries,
#        3,
#        "Locking and Unlocking Entries",
#        [
#            "This entry was unlocked while playing."
#        ],
#        "Basic Usage",
#        locked = persistent.lock_unlock_3
#    )
