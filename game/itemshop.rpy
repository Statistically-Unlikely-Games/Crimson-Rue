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
    
    $ in_itemshop = True
    
    scene bg itemshop
    show screen itemshop
    show screen basic_overlay
    
#    "I can sell my wares and buy new supplies here."
    jump it_looping

screen itemshop:
    tag menu2
        
    imagebutton: 
        auto "gui/button.itemshop.desk_%s.png" 
        focus_mask True 
        action Show("inventory_screen", first_inventory=pc_inv, second_inventory=shop_inv)
        xpos 655 ypos 420 
        xanchor 0 yanchor 0
    
label leave_itemshop:
    show screen basic_overlay
    show screen overworld
    $ in_itemshop = False
    $ time_cnt += 1
    hide screen itemshop
    if time_cnt > 5:
        call timecount_msg
        jump return_home
    
    jump overworld01