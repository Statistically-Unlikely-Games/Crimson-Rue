##Ren'Py Inventory System v. 1.5 provided under public domain by saguaro

init python: 
    import renpy.store as store    
    
    class Item(store.object):
        def __init__(self, name, desc, icon=False, value=0, act=Show("inventory_popup", message="Nothing happened!"), type="item", recipe=False, containers=False):
            global cookbook
            self.name = name
            self.desc = desc
            self.icon = icon
            self.value = value
            self.act = act # screen action
            self.type = type # type of item
            self.recipe = recipe # nested list of [ingredient, qty]  
            self.containers = containers
            
            if recipe:
                cookbook.append(self)
                cookbook.sort(key=lambda i: i.name) #alpha order

        def change(self, name, desc=False, icon=False, value=False, act=False, recipe=False, containers=False): 
            self.name = name
            if desc:
                self.desc = desc
            if icon:
                self.icon = icon
            if value:
                self.value = value   
            if act:
                self.act = act
            if recipe:
                self.recipe = recipe  
            if containers:
                self.containers = containers
            
    class Inventory(store.object):
        def __init__(self, name, money=0, barter=100):
            self.name = name
            self.money = money
            self.barter = barter #percentage of value paid for items            
            self.inv = []  # items stored in nested list [item object, qty]
            self.sort_by = self.sort_name
            self.sort_order = True #ascending, descending
            self.grid_view = True
            
        def buy(self, item, price):            
            self.deposit(price)            
            self.take(item[0]) #Why is the zero there? Adding a popup doesn't work, maybe because of the zero. Says the object has no name.
#            message = "Purchased %s!" % (item.name)
#            renpy.show_screen("inventory_popup", message=message,item=item.name)

        def check(self, item):
            if self.qty(item):
                for i in self.inv:
                    if i[0] == item:        
                        return self.inv.index(i) # returns item index (location)            
            
        def check_recipe(self, item): # verify all ingredients are in inv
            checklist = list()
            for i in item.recipe:
                if self.qty(i[0]) >= i[1]:
                    checklist.append(True)
            if len(checklist) == len(item.recipe):
                return True
            else:
                return False        
                
        def craft(self, item):
            for line in item.recipe:
                self.drop(line[0], line[1])
            for line in item.containers:
                self.take(line[0], line[1])

            self.take(item)
            #if new item bottles is not 0, take empty bottles equal to the number of bottles -1
            message = "Crafted %s!" % (item.name)
            renpy.show_screen("inventory_popup2", message=message,item=item.name)  
            
                            
        def deposit(self, amount):
            self.money -= amount   
                            
        def drop(self, item, qty=1):
            if self.qty(item):
                item_location = self.check(item)
                if self.inv[item_location][1] > qty:
                    self.inv[item_location][1] -= qty
                else:
                    del self.inv[item_location]                      
                            
        def qty(self, item):
            for i in self.inv:
                if i[0] == item:   
                    return i[1] # returns quantity   
                    
        def sell(self, item, price):
            self.withdraw(price)
            self.drop(item[0])
            
        def sort_name(self):
            self.inv.sort(key=lambda i: i[0].name, reverse=self.sort_order)
            
        def sort_qty(self):
            self.inv.sort(key=lambda i: i[1], reverse=self.sort_order)
                      
        def sort_value(self):
            self.inv.sort(key=lambda i: i[0].value, reverse=self.sort_order)
           
        def take(self, item, qty=1):
            if self.qty(item):
                item_location = self.check(item)            
                self.inv[item_location][1] += qty                  
            else:
                self.inv.append([item,qty])  

        def withdraw(self, amount):
            self.money += amount
            
    def calculate_price(item, buyer):
        if buyer:
            price = item[0].value * (buyer.barter * 0.01)
            return int(price)
        
    def money_transfer(depositor, withdrawer, amount):
        if depositor.money >= amount:
            depositor.deposit(amount)
            withdrawer.withdraw(amount) 
        else:
            message = "Sorry, %s doesn't have %d!" % (buyer.name, amount) 
            renpy.show_screen("inventory_popup", message=message) 

    def trade(seller, buyer, item):
        seller.drop(item[0])
        buyer.take(item[0])              
        
    def transaction(seller, buyer, item):
        price = calculate_price(item, buyer)
        if buyer.money >= price:   
            seller.sell(item, price)
            buyer.buy(item, price)
        else:
            message = "Sorry, %s doesn't have enough money!" % (buyer.name)
            renpy.show_screen("inventory_popup", message=message)

    transfer_amount = 0
                
screen tooltip(item=False,seller=false):      
    if item:
        hbox:
            xalign 0.5 yalign 1.0
            if seller:
                text ("[item[0].name]: [item[0].desc] (Value: " + str(calculate_price(item, seller)) + ")")
            else:
                text "[item[0].name]: [item[0].desc] (Value: [item[0].value])" 

screen inventory_screen(first_inventory, second_inventory=False, trade_mode=False, bank_mode=False):
    default crafting_screen = False
    tag menu
    modal True       
    frame:
        style_group "invstyle"          
        hbox:
            spacing 25
            vbox:
                label first_inventory.name                   
                if second_inventory:
                    use money(first_inventory, second_inventory, bank_mode) 
                use inventory_view(first_inventory, second_inventory, trade_mode)                          
                use view_nav(first_inventory)
                use sort_nav(first_inventory)
                if not second_inventory:
                    textbutton "Crafting Mode" action ToggleScreenVariable("crafting_screen")
                textbutton "Close" action Hide("inventory_screen")
            if second_inventory:
                vbox:
                    label second_inventory.name  
                    use money(second_inventory, first_inventory, bank_mode)                       
                    use inventory_view(second_inventory, first_inventory, trade_mode)
                    use view_nav(second_inventory)
                    use sort_nav(second_inventory)
            if crafting_screen:
                use crafting(first_inventory)
                
screen inventory_craftbalm(first_inventory, second_inventory=False, trade_mode=False, bank_mode=False):
    default crafting_screen = True
    tag menu
    modal True 
    
    frame:
        style_group "invstyle"
        hbox:
            spacing 25
            vbox:
                label first_inventory.name                   
                use money(first_inventory, second_inventory, bank_mode) 
                use craftinv_view(first_inventory, second_inventory, trade_mode)                          
                use view_nav(first_inventory)
                use sort_nav(first_inventory)
                use craft_nav(first_inventory)
                textbutton "Close" action Hide("inventory_craftbalm")
            use crafting_balms(first_inventory)
            
screen inventory_craftcream(first_inventory, second_inventory=False, trade_mode=False, bank_mode=False):
    default crafting_screen = True
    tag menu
    modal True 
    
    frame:
        style_group "invstyle"
        hbox:
            spacing 25
            vbox:
                label first_inventory.name                   
                use money(first_inventory, second_inventory, bank_mode) 
                use craftinv_view(first_inventory, second_inventory, trade_mode)                          
                use view_nav(first_inventory)
                use sort_nav(first_inventory)
                use craft_nav(first_inventory)
                textbutton "Close" action Hide("inventory_craftcream")
            use crafting_creams(first_inventory)
            
screen inventory_craftextract(first_inventory, second_inventory=False, trade_mode=False, bank_mode=False):
    default crafting_screen = True
    tag menu
    modal True 
    
    frame:
        style_group "invstyle"
        hbox:
            spacing 25
            vbox:
                label first_inventory.name                   
                use money(first_inventory, second_inventory, bank_mode) 
                use craftinv_view(first_inventory, second_inventory, trade_mode)                          
                use view_nav(first_inventory)
                use sort_nav(first_inventory)
                use craft_nav(first_inventory)
                textbutton "Close" action Hide("inventory_craftextract")
            use crafting_extracts(first_inventory)
            
screen inventory_craftherboil(first_inventory, second_inventory=False, trade_mode=False, bank_mode=False):
    default crafting_screen = True
    tag menu
    modal True 
    
    frame:
        style_group "invstyle"
        hbox:
            spacing 25
            vbox:
                label first_inventory.name                   
                use money(first_inventory, second_inventory, bank_mode) 
                use craftinv_view(first_inventory, second_inventory, trade_mode)                          
                use view_nav(first_inventory)
                use sort_nav(first_inventory)
                use craft_nav(first_inventory)
                textbutton "Close" action Hide("inventory_craftherboil")
            use crafting_herboil(first_inventory)
            
screen inventory_craftinfusion(first_inventory, second_inventory=False, trade_mode=False, bank_mode=False):
    default crafting_screen = True
    tag menu
    modal True 
    
    frame:
        style_group "invstyle"
        hbox:
            spacing 25
            vbox:
                label first_inventory.name                   
                use money(first_inventory, second_inventory, bank_mode) 
                use craftinv_view(first_inventory, second_inventory, trade_mode)                          
                use view_nav(first_inventory)
                use sort_nav(first_inventory)
                use craft_nav(first_inventory)
                textbutton "Close" action Hide("inventory_craftinfusion")
            use crafting_infusions(first_inventory)
            
screen inventory_craftsalve(first_inventory, second_inventory=False, trade_mode=False, bank_mode=False):
    default crafting_screen = True
    tag menu
    modal True 
    
    frame:
        style_group "invstyle"
        hbox:
            spacing 25
            vbox:
                label first_inventory.name                   
                use money(first_inventory, second_inventory, bank_mode) 
                use craftinv_view(first_inventory, second_inventory, trade_mode)                          
                use view_nav(first_inventory)
                use sort_nav(first_inventory)
                use craft_nav(first_inventory)
                textbutton "Close" action Hide("inventory_craftsalve")
            use crafting_salves(first_inventory)
            
screen inventory_crafttincture(first_inventory, second_inventory=False, trade_mode=False, bank_mode=False):
    default crafting_screen = True
    tag menu
    modal True 
    
    frame:
        style_group "invstyle"
        hbox:
            spacing 25
            vbox:
                label first_inventory.name                   
                use money(first_inventory, second_inventory, bank_mode) 
                use craftinv_view(first_inventory, second_inventory, trade_mode)                          
                use view_nav(first_inventory)
                use sort_nav(first_inventory)
                use craft_nav(first_inventory)
                textbutton "Close" action Hide("inventory_crafttincture")
            use crafting_tinctures(first_inventory)

screen inventory_kitchen(first_inventory, second_inventory=False, trade_mode=False, bank_mode=False):
    default crafting_screen = True
    tag menu
    modal True 
    
    frame:
        style_group "invstyle"
        hbox:
            spacing 25
            vbox:
                label first_inventory.name                   
                use money(first_inventory, second_inventory, bank_mode) 
                use craftinv_view(first_inventory, second_inventory, trade_mode)                          
                use view_nav(first_inventory)
                use sort_nav(first_inventory)
                textbutton "Close" action Hide("inventory_kitchen")
            use crafting_kitchen(first_inventory)
                
screen inventory_view(inventory, second_inventory=False, trade_mode=False):     
    side "c r":
        style_group "invstyle"
        area (0, 0, 350, 400) 
        vpgrid id ("vp"+inventory.name):
            draggable True   
            mousewheel True
            xsize 350 ysize 400
            if inventory.grid_view:
                cols 3 spacing 10
            else:
                cols 1 spacing 25
            for item in inventory.inv:
                $ name = item[0].name
                $ desc = item[0].desc
                $ value = item[0].value
                $ qty = str(item[1])
                hbox:
                    if item[0].icon:
                        $ icon = item[0].icon
                        $ hover_icon = im.Sepia(icon)                              
                        imagebutton:
                            idle LiveComposite((100,100), (0,0), icon, (0,0), Text(qty))
                            hover LiveComposite((100,100), (0,0), hover_icon, (0,0), Text(qty))
                            action (If(not second_inventory, item[0].act, (If(trade_mode, Function(trade,inventory, second_inventory, item), Function(transaction,inventory, second_inventory, item)))))
                            hovered Show("tooltip",item=item,seller=second_inventory)
                            unhovered Hide("tooltip")
                        if not inventory.grid_view:
                            vbox:
                                text name
                                if not trade_mode:
                                    text "List Value: [value]"                                        
                                    if second_inventory:                                            
                                        text ("Sell Value: " + str(calculate_price(item, second_inventory)) + ")")
                    
                    else:                               
                        textbutton "[name] ([qty])" action (If(not second_inventory, item[0].act,(If(trade_mode, Function(trade,inventory, second_inventory, item), Function(transaction,inventory, second_inventory, item))))) hovered Show("tooltip",item=item,seller=second_inventory) unhovered Hide("tooltip")
                        if not inventory.grid_view:
                            vbox:                        
                                text "List Value: [value]"
                                if not trade_mode and second_inventory:
                                    text "Sell Value: " + str(calculate_price(item, second_inventory)) + ")"
            
            ## maintains spacing in empty inventories.
            if len(inventory.inv) == 0:
                add Null(height=100,width=100)
                                    
        vbar value YScrollValue("vp"+inventory.name)
        

screen craftinv_view(inventory, second_inventory=False, trade_mode=False):     
    side "c r":
        style_group "invstyle"
        area (0, 0, 450, 530) 
        vpgrid id ("vp"+inventory.name):
            draggable True   
            mousewheel True
            xsize 450 ysize 530
            if inventory.grid_view:
                cols 4 spacing 10
            else:
                cols 1 spacing 25
            for item in inventory.inv:
                $ name = item[0].name
                $ desc = item[0].desc
                $ value = item[0].value
                $ qty = str(item[1])
                hbox:
                    if item[0].icon:
                        $ icon = item[0].icon
                        $ hover_icon = im.Sepia(icon)                              
                        imagebutton:
                            idle LiveComposite((100,100), (0,0), icon, (0,0), Text(qty))
                            hover LiveComposite((100,100), (0,0), hover_icon, (0,0), Text(qty))
                            action (If(not second_inventory, item[0].act, (If(trade_mode, Function(trade,inventory, second_inventory, item), Function(transaction,inventory, second_inventory, item)))))
                            hovered Show("tooltip",item=item,seller=second_inventory)
                            unhovered Hide("tooltip")
                        if not inventory.grid_view:
                            vbox:
                                text name
                                if not trade_mode:
                                    text "List Value: [value]"                                        
                                    if second_inventory:                                            
                                        text ("Sell Value: " + str(calculate_price(item, second_inventory)) + ")")
                    
                    else:                               
                        textbutton "[name] ([qty])" action (If(not second_inventory, item[0].act,(If(trade_mode, Function(trade,inventory, second_inventory, item), Function(transaction,inventory, second_inventory, item))))) hovered Show("tooltip",item=item,seller=second_inventory) unhovered Hide("tooltip")
                        if not inventory.grid_view:
                            vbox:                        
                                text "List Value: [value]"
                                if not trade_mode and second_inventory:
                                    text "Sell Value: " + str(calculate_price(item, second_inventory)) + ")"
            
            ## maintains spacing in empty inventories.
            if len(inventory.inv) == 0:
                add Null(height=100,width=100)
                                    
        vbar value YScrollValue("vp"+inventory.name)

    
screen money(inventory, second_inventory, bank_mode=False):    
    hbox:
        style_group "invstyle"
        text "Money: [inventory.money]"
        if bank_mode and inventory.money:
            textbutton "Transfer" action Show("banking", depositor=inventory, withdrawer=second_inventory)
    
screen banking(depositor, withdrawer):    
    modal True
    frame:
        style_group "invstyle"        
        vbox:
            label "Money Transfer"
            text "Amount: [transfer_amount]"
            bar value VariableValue("transfer_amount", depositor.money, max_is_zero=False, style='scrollbar', offset=0, step=0.1) xmaximum 200
            
            hbox: #examples of the types of controls you can set up                
                for amount in [50,100,250,depositor.money]:
                    if depositor.money>=amount:
                        textbutton str(amount) action SetVariable("transfer_amount", amount)              
            hbox:
                textbutton "Transfer" action [Function(money_transfer, depositor, withdrawer, transfer_amount), SetVariable("transfer_amount", 0), Hide("banking")]
                textbutton "Cancel" action Hide("banking")

screen crafting(inventory):
    vbox:            
        label "Recipes"
        hbox:
            xmaximum 600 xminimum 600 xfill True         
            text "Name" xalign 0.5   
            text "Ingredients" xalign 0.5   
        side "c r":
            area (0,0,600,400)
            viewport id "cookbook":           
                draggable True
                mousewheel True
                vbox:
                    for item in cookbook:
                        hbox:                            
                            first_spacing 25 spacing 10
                            hbox:
                                xmaximum 250 xminimum 250 xfill True box_wrap True
                                if item.icon:
                                    add im.FactorScale(item.icon, 0.33)
                                if inventory.check_recipe(item):
                                    textbutton item.name action Function(inventory.craft,item)
                                else:                                                                   
                                    text item.name
                            for i in item.recipe: 
                                if i[0].icon:
                                    add im.FactorScale(i[0].icon, 0.33)
                                else:
                                    text i[0].name
                                if inventory.qty(i[0]) >= i[1]:
                                    text "x" + str(i[1]) bold True
                                else:
                                    text "x" + str(i[1])             
            vbar value YScrollValue("cookbook") 
        textbutton "Hide" action ToggleScreenVariable("crafting_screen") xalign 0.5
        
screen crafting_balms(inventory):
    vbox:            
        label "Recipes"
        hbox:
            xmaximum 800 xminimum 800 xfill True         
            text "Name" xalign 0.6
            text "Ingredients" xalign 0.2
        side "c r":
            area (0,0,1280,530)
            viewport id "balmslist":           
                draggable True
                mousewheel True
                vbox:
                    for item in balmslist:
                        hbox:                            
                            first_spacing 25 spacing 10
                            hbox:
                                xmaximum 400 xminimum 400 xfill True box_wrap True
                                if item.icon:
                                    add im.FactorScale(item.icon, 0.33)
                                if inventory.check_recipe(item):
                                    textbutton item.name action Function(inventory.craft,item)
                                else:                                                                   
                                    text item.name
                            for i in item.recipe: 
                                if i[0].icon:
                                    add im.FactorScale(i[0].icon, 0.33)
                                else:
                                    text i[0].name
                                if inventory.qty(i[0]) >= i[1]:
                                    text "x" + str(i[1]) bold True
                                else:
                                    text "x" + str(i[1])             
            vbar value YScrollValue("balmslist") 
        
screen crafting_creams(inventory):
    vbox:            
        label "Recipes"
        hbox:
            xmaximum 800 xminimum 800 xfill True         
            text "Name" xalign 0.6
            text "Ingredients" xalign 0.2  
        side "c r":
            area (0,0,1280,530)
            viewport id "creamslist":           
                draggable True
                mousewheel True
                vbox:
                    for item in creamslist:
                        hbox:                            
                            first_spacing 25 spacing 10
                            hbox:
                                xmaximum 400 xminimum 400 xfill True box_wrap True
                                if item.icon:
                                    add im.FactorScale(item.icon, 0.33)
                                if inventory.check_recipe(item):
                                    textbutton item.name action Function(inventory.craft,item)
                                else:                                                                   
                                    text item.name
                            for i in item.recipe: 
                                if i[0].icon:
                                    add im.FactorScale(i[0].icon, 0.33)
                                else:
                                    text i[0].name
                                if inventory.qty(i[0]) >= i[1]:
                                    text "x" + str(i[1]) bold True
                                else:
                                    text "x" + str(i[1])             
            vbar value YScrollValue("creamslist") 
        
screen crafting_extracts(inventory):
    vbox:            
        label "Recipes"
        hbox:
            xmaximum 800 xminimum 800 xfill True         
            text "Name" xalign 0.6
            text "Ingredients" xalign 0.2  
        side "c r":
            area (0,0,1280,530)
            viewport id "extractslist":           
                draggable True
                mousewheel True
                vbox:
                    for item in extractslist:
                        hbox:                            
                            first_spacing 25 spacing 10
                            hbox:
                                xmaximum 400 xminimum 400 xfill True box_wrap True
                                if item.icon:
                                    add im.FactorScale(item.icon, 0.33)
                                if inventory.check_recipe(item):
                                    textbutton item.name action Function(inventory.craft,item)
                                else:                                                                   
                                    text item.name
                            for i in item.recipe: 
                                if i[0].icon:
                                    add im.FactorScale(i[0].icon, 0.33)
                                else:
                                    text i[0].name
                                if inventory.qty(i[0]) >= i[1]:
                                    text "x" + str(i[1]) bold True
                                else:
                                    text "x" + str(i[1])             
            vbar value YScrollValue("extractslist") 
            
screen crafting_herboil(inventory):
    vbox:            
        label "Recipes"
        hbox:
            xmaximum 800 xminimum 800 xfill True         
            text "Name" xalign 0.6
            text "Ingredients" xalign 0.2 
        side "c r":
            area (0,0,1280,530)
            viewport id "herboilslist":           
                draggable True
                mousewheel True
                vbox:
                    for item in herboilslist:
                        hbox:                            
                            first_spacing 25 spacing 10
                            hbox:
                                xmaximum 400 xminimum 400 xfill True box_wrap True
                                if item.icon:
                                    add im.FactorScale(item.icon, 0.33)
                                if inventory.check_recipe(item):
                                    textbutton item.name action Function(inventory.craft,item)
                                else:                                                                   
                                    text item.name
                            for i in item.recipe: 
                                if i[0].icon:
                                    add im.FactorScale(i[0].icon, 0.33)
                                else:
                                    text i[0].name
                                if inventory.qty(i[0]) >= i[1]:
                                    text "x" + str(i[1]) bold True
                                else:
                                    text "x" + str(i[1])             
            vbar value YScrollValue("herboilslist") 
            
screen crafting_infusions(inventory):
    vbox:            
        label "Recipes"
        hbox:
            xmaximum 800 xminimum 800 xfill True         
            text "Name" xalign 0.6
            text "Ingredients" xalign 0.2 
        side "c r":
            area (0,0,1280,530)
            viewport id "infusionslist":           
                draggable True
                mousewheel True
                vbox:
                    for item in infusionslist:
                        hbox:                            
                            first_spacing 25 spacing 10
                            hbox:
                                xmaximum 400 xminimum 400 xfill True box_wrap True
                                if item.icon:
                                    add im.FactorScale(item.icon, 0.33)
                                if inventory.check_recipe(item):
                                    textbutton item.name action Function(inventory.craft,item)
                                else:                                                                   
                                    text item.name
                            for i in item.recipe: 
                                if i[0].icon:
                                    add im.FactorScale(i[0].icon, 0.33)
                                else:
                                    text i[0].name
                                if inventory.qty(i[0]) >= i[1]:
                                    text "x" + str(i[1]) bold True
                                else:
                                    text "x" + str(i[1])             
            vbar value YScrollValue("infusionslist") 
            
screen crafting_salves(inventory):
    vbox:            
        label "Recipes"
        hbox:
            xmaximum 800 xminimum 800 xfill True         
            text "Name" xalign 0.6
            text "Ingredients" xalign 0.2
        side "c r":
            area (0,0,1280,530)
            viewport id "salveslist":           
                draggable True
                mousewheel True
                vbox:
                    for item in salveslist:
                        hbox:                            
                            first_spacing 25 spacing 10
                            hbox:
                                xmaximum 400 xminimum 400 xfill True box_wrap True
                                if item.icon:
                                    add im.FactorScale(item.icon, 0.33)
                                if inventory.check_recipe(item):
                                    textbutton item.name action Function(inventory.craft,item)
                                else:                                                                   
                                    text item.name
                            for i in item.recipe: 
                                if i[0].icon:
                                    add im.FactorScale(i[0].icon, 0.33)
                                else:
                                    text i[0].name
                                if inventory.qty(i[0]) >= i[1]:
                                    text "x" + str(i[1]) bold True
                                else:
                                    text "x" + str(i[1])             
            vbar value YScrollValue("salveslist") 
            
screen crafting_tinctures(inventory):
    vbox:            
        label "Recipes"
        hbox:
            xmaximum 800 xminimum 800 xfill True         
            text "Name" xalign 0.6
            text "Ingredients" xalign 0.2
        side "c r":
            area (0,0,1280,530)
            viewport id "tinctureslist":           
                draggable True
                mousewheel True
                vbox:
                    for item in tinctureslist:
                        hbox:                            
                            first_spacing 25 spacing 10
                            hbox:
                                xmaximum 400 xminimum 400 xfill True box_wrap True
                                if item.icon:
                                    add im.FactorScale(item.icon, 0.33)
                                if inventory.check_recipe(item):
                                    textbutton item.name action Function(inventory.craft,item)
                                else:                                                                   
                                    text item.name
                            for i in item.recipe: 
                                if i[0].icon:
                                    add im.FactorScale(i[0].icon, 0.33)
                                else:
                                    text i[0].name
                                if inventory.qty(i[0]) >= i[1]:
                                    text "x" + str(i[1]) bold True
                                else:
                                    text "x" + str(i[1])             
            vbar value YScrollValue("tinctureslist") 

screen crafting_kitchen(inventory):
    vbox:            
        label "Recipes"
        hbox:
            xmaximum 800 xminimum 800 xfill True         
            text "Name" xalign 0.6
            text "Ingredients" xalign 0.2
        side "c r":
            area (0,0,1280,530)
            viewport id "cooklist":           
                draggable True
                mousewheel True
                vbox:
                    for item in cooklist:
                        hbox:                            
                            first_spacing 25 spacing 10
                            hbox:
                                xmaximum 400 xminimum 400 xfill True box_wrap True
                                if item.icon:
                                    add im.FactorScale(item.icon, 0.33)
                                if inventory.check_recipe(item):
                                    textbutton item.name action Function(inventory.craft,item)
                                else:                                                                   
                                    text item.name
                            for i in item.recipe: 
                                if i[0].icon:
                                    add im.FactorScale(i[0].icon, 0.33)
                                else:
                                    text i[0].name
                                if inventory.qty(i[0]) >= i[1]:
                                    text "x" + str(i[1]) bold True
                                else:
                                    text "x" + str(i[1])             
            vbar value YScrollValue("cooklist") 

                
screen view_nav(inventory):
    hbox:
        text "View: "
        textbutton "Grid" action SetField(inventory, "grid_view", True)        
        textbutton "List" action SetField(inventory, "grid_view", False)     
                
screen sort_nav(inventory):
    hbox:
        text "Sort: "         
        textbutton "Name" action [ToggleField(inventory, "sort_by", inventory.sort_name), inventory.sort_name]
        textbutton "Qty" action [ToggleField(inventory, "sort_by", inventory.sort_qty), inventory.sort_qty]
        textbutton "Val" action [ToggleField(inventory, "sort_by", inventory.sort_value), inventory.sort_value]
        if inventory.sort_order:
            textbutton "asc." action [ToggleField(inventory, "sort_order"), inventory.sort_by]
        else:
            textbutton "des." action [ToggleField(inventory, "sort_order"), inventory.sort_by]            
            
screen craft_nav(inventory):
    hbox:
        xalign 1.53
        xmaximum 250 xminimum 250 xfill True
        textbutton "Balms" action Show("inventory_craftbalm", first_inventory=pc_inv)       
        textbutton "Creams" action Show("inventory_craftcream", first_inventory=pc_inv) 
        textbutton "Extracts" action Show("inventory_craftextract", first_inventory=pc_inv)
        textbutton "Oils" action Show("inventory_craftherboil", first_inventory=pc_inv)
        textbutton "Infusions" action Show("inventory_craftinfusion", first_inventory=pc_inv)
        textbutton "Salves" action Show("inventory_craftsalve", first_inventory=pc_inv)
        textbutton "Tinctures" action Show("inventory_crafttincture", first_inventory=pc_inv)

screen inventory_popup(message):
    zorder 100
    frame:
        style_group "invstyle"
        vbox:
            text message
    timer 0.8 action Hide("inventory_popup")
    
screen inventory_popup2(message,item):
    zorder 100
    imagebutton idle "gui/"+item+"_notification.png" xalign 0.5 yalign 0.35
    frame:
        style_group "msgstyle"
        vbox:
            text message
    timer 0.8 action Hide("inventory_popup2")
    
    
init -2: 

    ## STYLES ##
    style invstyle_frame:
        xalign 0.5
        yalign 0.5
        
    style invstyle_label_text:
        size 30
        
    style invstyle_label:
        xalign 0.5 
        
    style msgstyle_frame:
        xalign 0.5
        yalign 0.61
        
    style msgstyle_label_text:
        size 30
        
    style msgstyle_label:
        xalign 0.5 

