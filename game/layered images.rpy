##############################################################################
# Layered Images
#
# Controls all Dynamic Characters

layeredimage aethl:
#Eyebrows > Eyes > Mouth > Hood > Bangs > Ears > Cloak > Arms > Base
    group base auto:
        attribute vest default

    group arms if_any "nude" auto variant "nude":
        attribute slack default
    group arms if_not "nude" auto variant "vest":
        attribute slack default

    group ears auto prefix "ears":
        attribute down default

    group bangs auto:
        attribute bangs default

    attribute cloak null
    group cloak if_all ["cloak", "up"] auto variant "open":
        attribute plain default
    group cloak if_any "cloak" if_not "up" auto variant "closed":
        attribute plain default

    group mouth auto prefix "mouth":
        attribute neu default

    group eyes auto prefix "eyes":
        attribute neu default

    group brows auto prefix "brows":
        attribute neu default

layeredimage aethr:
#Eyebrows > Eyes > Mouth > Hood > Bangs > Ears > Cloak > Arms > Base
    group base auto:
        attribute vest default

    group arms if_any "nude" auto variant "nude":
        attribute slack default
    group arms if_not "nude" auto variant "vest":
        attribute slack default

    group ears auto prefix "ears":
        attribute down default

    group bangs auto:
        attribute bangs default

    attribute cloak null
    group cloak if_all ["cloak", "up"] auto variant "open":
        attribute plain default
    group cloak if_any "cloak" if_not "up" auto variant "closed":
        attribute plain default

    group mouth auto prefix "mouth":
        attribute neu default

    group eyes auto prefix "eyes":
        attribute neu default

    group brows auto prefix "brows":
        attribute neu default
