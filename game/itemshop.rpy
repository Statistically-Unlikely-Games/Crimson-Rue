##############################################################################
# Item Shop
#
# Sell and buy.


label it_looping: 
    $ renpy.pause()
    call timecount_nomsg
    call time_img
    jump aplooping


label item_shop:
    
    $ current_loc = "itemshop"
    
#    $ in_overworld01 = False
#    $ in_overworld02 = False
#    $ in_apothecary = False
#    $ in_kitchen = False
#    $ in_cellar = False
#    $ in_itemshop = True
#    $ in_forest001 = False
#    $ in_forest002 = False
#    $ in_forest003 = False
#    $ in_forest004 = False
#    $ in_forest005 = False
#    $ in_forest006 = False
#    $ in_forest007 = False
#    $ in_forest008 = False
#    $ in_forest009 = False
    
    scene bg itemshop
    show screen itemshop
    show screen basic_overlay
    
#    "I can sell my wares and buy new supplies here."

    hide screen itemshop
    call check_events
    show screen itemshop

    jump it_looping

screen itemshop:
    tag menu2
        
    imagebutton: 
        auto "gui/button.itemshop.desk_%s.png" 
        focus_mask True 
        action Show("store_screen", player=player_bag, seller=seller_bag)
        xpos 655 ypos 420 
        xanchor 0 yanchor 0
    
label leave_itemshop:
    show screen basic_overlay
    show screen overworld
    $ current_loc = "none"
    $ time_cnt += 1
    hide screen itemshop
    if time_cnt > 5:
        call timecount_msg
        jump return_home
    
    jump overworld01