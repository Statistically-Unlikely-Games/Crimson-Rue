# Copyright 2014 Joshua Fehler <jsfehler@gmail.com>
#
# This file is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.

init -1500 python:
 from operator import itemgetter
 
 class Encyclopaedia(object): 
  #The encyclopaedia object holds all the entries and manages them
  def __init__(self, sortingMode = "Number", showLocked=True):
   self.subjects= [] #List of all subjects
   self.unlocked_entries = [] #Only entries that are unlocked will be added
   self.all_entries = [] #List of all entries, regardless of if locked or not 
   self.size = 0  #For holding the length of self.unlocked_entries  
   self.size_all = 0 #For holding the length of self.all_entries  
   self.sortingMode = sortingMode #Default type of sorting for list screen. Defaults to "Number"
   self.showLocked = showLocked #If True, locked entries show "???" on the listing screen. Defaults to True
  
   self.index_page = 0
   self.index = 0
  
  def setEntryListSize(self):
   if self.showLocked:
    self.entry_list_size = self.size_all
   else:
    self.entry_list_size = self.size
  
  def getKey(self,item):
   return item[1].name
  
  def unlockEntry(self,entry_number, item, unlock_flag):
   item.locked = unlock_flag
   self.addEntry(entry_number,item)
  
  def addEntry(self, entry_number, item): 
   #Adds a new entry to the Encyclopaedia, but won't allow duplicates
   if not [entry_number,item] in self.all_entries:
    self.all_entries.append([entry_number,item])
    
   if not [entry_number,item] in self.unlocked_entries:
     if item.locked == False:
      self.unlocked_entries.append([entry_number,item])
    
   if self.sortingMode == "Number":
    self.unlocked_entries = sorted(self.unlocked_entries,key=itemgetter(0))
    self.all_entries = sorted(self.all_entries,key=itemgetter(0))
   else:
    self.unlocked_entries = sorted(self.unlocked_entries,key=self.getKey)
    self.all_entries = sorted(self.all_entries,key=self.getKey)
    
   self.size = len(self.unlocked_entries)
   self.size_all = len(self.all_entries)
   self.setEntryListSize()
 
  def addEntries(self,*new_entries):
   #Adds multiple new entries at once
   for item in new_entries:
    self.addEntry(item[0],item[1])
   
  def addSubject(self,new_subject):
   #Adds a new subject to the Encyclopaedia, but won't allow duplicates
   if not new_subject in self.subjects:
    self.subjects.append(new_subject)
  
  def addSubjects(self,*new_subjects):
   #Adds multiple new subjects at once
   for item in new_subjects:
    self.addSubject(item)
  
  def getEntryPage(self,entry_number):
   #Returns the page number of the specified entry_number
   if self.showLocked:
    return self.all_entries[entry_number][0]
   elif self.showLocked == False:
    return self.unlocked_entries[entry_number][0]
   
  def getEntry(self,entry_number):
   #Returns the entry of the specified entry_number
   if self.showLocked:
    return self.all_entries[entry_number][1]
   elif self.showLocked == False:
    return self.unlocked_entries[entry_number][1]
   
  def getUnlockedEntryPage(self,entry_number):
   #Returns the page number of the specified entry_number, from the unlocked_entries list
    return self.unlocked_entries[entry_number][0]
   
  def getUnlockedEntry(self,entry_number):
   #Returns the entry of the specified entry_number, from the unlocked_entries list
    return self.unlocked_entries[entry_number][1]
   
  def setEntryData(self, source, val):
   if source == "setEntry":
    self.index_page, self.index = self.getEntryPage(val), self.getEntry(val)
   elif source == "Prev_Next":
    self.index_page, self.index = self.getUnlockedEntryPage(val), self.getUnlockedEntry(val)
  
  def getEntryData(self):
   return self.index_page, self.index
   
 class EncEntry(object):
  def __init__(self, number=0, name="Entry Name", text="Entry Text", subject=None, status=None, locked=True, image=None):
   #Class for each individual entry
   #Every EncEntry has to be added to an Encyclopaedia or else it will do nothing
   #image is optional. If no image is specified, it's assumed the entry was meant to have no image
   self.number = number
   self.name = name
   self.text = text
   self.status = status
   self.subject = subject
   self.locked = locked
   self.pages = [] #holds an integer for the number of pages in the entry
  
   self.hasImage = False  
   if image != None:
    self.image = image
    self.hasImage = True  
  
   self.sub_entry_list = [[1,self]]
   self.hasSubEntry = False
  
  def __repr__(self):
   return str(self.name)
  
  def addSubEntry(self,sub_entry_page,sub_entry): 
   if not [sub_entry_page,sub_entry] in self.sub_entry_list:
    if not sub_entry in self.sub_entry_list:
     if sub_entry.locked == False:
      self.sub_entry_list.append([sub_entry_page,sub_entry])
      self.sub_entry_list = sorted(self.sub_entry_list,key=itemgetter(0))
      self.hasSubEntry = True
  
    self.pages = len(self.sub_entry_list)
  
  def addSubEntries(self, *new_sub_entries):
   #Adds multiple new sub-entries at once
   for item in new_sub_entries:
    self.addSubEntry(item[0],item[1])
  
  #returns array of pages an Entry has.
  def getSubEntryList(self):
   return self.sub_entry_list
 
  #accepts Integer. returns the text on given page 
  def getSubEntry(self,page):
   return self.sub_entry_list[page][1].text
  
  def unlockSubEntry(self,entry_number, item, unlock_flag):
   item.locked = unlock_flag
   self.addSubEntry(entry_number,item)
  
 #Action to call toggleStatus on an EncEntry
 class ChangeStatus(Action): 
  def __init__(self, position):
   self.position = position
  def __call__(self):
   encyclopaedia.all_entries[self.position][1].status = True
 
 class SaveStatus(Action):
  def __init__(self):
   pass
  def __call__(self):
   for x in range(encyclopaedia.size_all):
    persistent.new_dict["new_0" + str(x)] = encyclopaedia.all_entries[x][1].status
  
 #Action that places the selected encyclopaedia entry into the frame
 #Type controls if it's a main entry or a sub-entry
 class SetEntry(Action):
  def __init__(self, given_entry, given_pos):
   self.given_entry = given_entry
   self.given_pos = given_pos
   self.given_text = given_entry.text
   self.target_entry = given_pos
   
  def __call__(self):
   global entry_text
   global current_position
   global sub_current_position
   
   if encyclopaedia.showLocked:
    if [self.target_entry+1,self.given_entry] in encyclopaedia.unlocked_entries:
     self.target_entry = encyclopaedia.unlocked_entries.index([self.target_entry+1,self.given_entry])
   
   if encyclopaedia.sortingMode == "Number":
    self.target_entry = self.given_pos
   
   encyclopaedia.setEntryData("setEntry", self.target_entry)
   entry_text = self.given_text
   
   if encyclopaedia.sortingMode == "Z to A":
    current_position = encyclopaedia.unlocked_entries.index( [self.given_entry.number,self.given_entry] )
  
   else:
    current_position = self.target_entry 
   
  def get_sensitive(self):
   return True
 
 #Action that sorts the entries Alphabetically 
 class SortEncyclopaedia(Action):
  def __init__(self,enc, sorting_mode="Number"):
   #self.encyclopaedia = encyclopaedia
   self.unlocked_entries = encyclopaedia.unlocked_entries
   self.all_entries = encyclopaedia.all_entries
   self.reverse = False
   if sorting_mode == "Z to A":
    self.reverse = True
   self.sortingMode = sorting_mode

  def getKey(self,item):
   if self.sortingMode == "Number":
    return item[0]
   else:
    return item[1].name

  def __call__(self):
   encyclopaedia.unlocked_entries = sorted(self.unlocked_entries, reverse=self.reverse,key=self.getKey)
   encyclopaedia.all_entries = sorted(self.all_entries, reverse=self.reverse,key=self.getKey)
   encyclopaedia.sortingMode = self.sortingMode
   renpy.restart_interaction()
  
 #Base class to change the current entry being viewed. Should not be called on it's own. 
 class ChangeEntry(Action):
  def __init__(self, enc, block):  
   self.enc = enc
   self.block = block
   self.dir = 0
  
  def __call__(self):
   if self.block == False:
    global entry_text
    global current_position
    global sub_current_position
   
    encyclopaedia.setEntryData("Prev_Next", current_position+self.dir)
 
    entry_viewed = encyclopaedia.getUnlockedEntryPage(current_position+self.dir)

    encyclopaedia.unlocked_entries[current_position+self.dir][1].status = True   
    entry_text = self.enc.unlocked_entries[current_position + self.dir][1].text
    
    current_position += self.dir
     
    self.refresh()
      
    sub_current_position = 1
   else:
    pass
  
  def refresh(self): 
   renpy.show_screen("encyclopaedia_entry")
   renpy.restart_interaction()
  
  def get_sensitive(self):
   if self.block == False:
    return True
   else:
    return False
  
 #PreviousEntry and NextEntry inherit from ChangeEntry, but specify a direction.
 class PreviousEntry(ChangeEntry): 
  def __init__(self, enc, block):  
   self.enc = enc
   self.block = block
   self.dir = -1
 
 class NextEntry(ChangeEntry): 
  def __init__(self, enc, block):  
   self.enc = enc
   self.block = block
   self.dir = 1
 
 #Base class to change the current sub-entry being viewed. Should not be called on it's own. 
 class ChangePage(ChangeEntry):
  def __init__(self,block):
   self.block = block
   self.dir1 = 0
   self.dir2 = 0

  def __call__(self):
   if self.block == False:
    global sub_current_position  
    global entry_text

    entry_text = encyclopaedia.getUnlockedEntry(current_position).getSubEntry(sub_current_position + self.dir1)
    sub_current_position += self.dir2
    
    self.refresh()
 
 #PreviousPage and NextPage inherit from ChangeEntry, but specify a direction.
 class PreviousPage(ChangePage):
  def __init__(self,block):
   self.block = block
   self.dir1 = -2
   self.dir2 = -1
 
 class NextPage(ChangePage):
  def __init__(self,block):
   self.block = block
   self.dir1 = 0
   self.dir2 = 1
     
 #Check to make sure the entries and pages buttons can't go outside their list index
 def checkMin(check_value, min):
  if check_value <= min:
   return True
  else:
   return False
 
 def checkMax(check_value, max):
  if check_value >= max:
   return True
  else:
   return False
   
   
##############################################################################
# Encyclopaedia List
#
# Screen that's used to display the list of entries 
screen encyclopaedia_list:
 tag menu
 
 window:
  style "gm_root"

  vbox:
   spacing 10
  
   frame:
    style_group "mm_root"
    xfill True
    xmargin 10
    top_margin 10
    text "Welcome to the Demo Encyclopaedia"
    
   frame:
    style_group "mm_root"
    xfill True
    xmargin 10
    
    hbox:
     xfill True
     text ""

   frame:
    style_group "mm_root"  
    xmargin 10
    yfill True
    xmaximum 400 #This controlls the width of the entry list. 
    bottom_margin 10
   
    viewport:
     scrollbars "vertical"
     mousewheel True
     draggable True
     
     vbox: 
      text encyclopaedia.sortingMode xalign 0.5 
     
      python:
      #Creates the buttons for each entry. 
       def generateEntryButtons(x):  
        ui.hbox()
        if encyclopaedia.showLocked:
         if encyclopaedia.all_entries[x][1].locked == False:
          ui.textbutton(encyclopaedia.all_entries[x][1].name, clicked= [ ChangeStatus(x), SetEntry(encyclopaedia.getEntry(x), x), Show("encyclopaedia_entry")] )
          if encyclopaedia.all_entries[x][1].status == None or encyclopaedia.all_entries[x][1].status == False:
           ui.textbutton ("New!")
          
         else:
          ui.textbutton("???")
    
        if encyclopaedia.showLocked == False:
         ui.textbutton(encyclopaedia.unlocked_entries[x][1].name, clicked= [ ChangeStatus(x), SetEntry(encyclopaedia.getUnlockedEntry(x), x), Show("encyclopaedia_entry")] )
         if encyclopaedia.unlocked_entries[x][1].status == None or encyclopaedia.unlocked_entries[x][1].status == False:  
          ui.textbutton ("New!")
        ui.close()
      
       #If sorting by subject, display the subject heading and add an entry under it if it's the same subject
       if encyclopaedia.sortingMode == "Subject":
        for x in range(len(encyclopaedia.subjects) ):
         ui.text(encyclopaedia.subjects[x])
         for y in range(encyclopaedia.entry_list_size):  
          if encyclopaedia.all_entries[y][1].subject == encyclopaedia.subjects[x]:
           generateEntryButtons(y)   
       
       #If sorting by number, add the number next to the entry
       elif encyclopaedia.sortingMode == "Number":    
        for x in range(encyclopaedia.entry_list_size):
         ui.hbox()
         ui.textbutton (str(encyclopaedia.getEntryPage(x) ) )
         generateEntryButtons(x)   
         ui.close()
      
       #If sorting Alphabetically or Reverse-Alphabetically, don't add anything before the entry
       else:
        for x in range(encyclopaedia.entry_list_size):
         generateEntryButtons(x) 
    
 frame:
  xalign .98
  yalign .98
  vbox:
   textbutton "Sort by Number" action [SortEncyclopaedia(encyclopaedia,sorting_mode="Number")]
   textbutton "Sort A to Z" action [SortEncyclopaedia(encyclopaedia,sorting_mode="A to Z")]
   textbutton "Sort Z to A" action [SortEncyclopaedia(encyclopaedia,sorting_mode="Z to A")]
   textbutton "Sort by Subject" action [SortEncyclopaedia(encyclopaedia,sorting_mode="Subject")]
   
   textbutton "Return"  action [SortEncyclopaedia(encyclopaedia,sorting_mode="Number"), SaveStatus(), Return()]
  
  
##############################################################################
# Encyclopaedia Entry
#
# Screen that's used to display each entry 
screen encyclopaedia_entry:
 tag menu
 
 python: 
  #checkMin and checkMax return Boolean to see if we're at the first or last entry in the encyclopaedia
  cmin = checkMin(current_position, 0)
  cmax = checkMax(current_position, encyclopaedia.size-1)
  sub_cmin = checkMin(sub_current_position, 1)
  sub_cmax = checkMax(sub_current_position, encyclopaedia.getEntry(current_position).pages)

 window:
  style "gm_root"  
  maximum (config.screen_width ,config.screen_height)

  xfill True
  yfill True
   
  vbox:
   spacing 10
  
   frame:
    style_group "mm_root"
    xfill True
    xmargin 10
    top_margin 10
    $page_indicator= "0" + str(encyclopaedia.getEntryData()[0]) + ": " + str(encyclopaedia.getEntryData()[1].name)
    text page_indicator
  
   frame:
    id "entry_nav"
    style_group "mm_root"
    xfill True
    xmargin 10
      
    hbox:
     xfill True
     if encyclopaedia.getEntryData()[1].hasSubEntry:  
      textbutton "Previous Page" xalign .02 action PreviousPage(sub_cmin)
      python:
        ui.text("Page " + str(sub_current_position) + " / " + str(encyclopaedia.getEntryData()[1].pages) ) 
      textbutton "Next Page" xalign .98 action NextPage(sub_cmax) 
     else: 
      text("") 
       
   hbox:
    $ddd = config.screen_width
    $dd = config.screen_width/1.4
    $pp = config.screen_height/1.321
    $pp2 = config.screen_height/2
    
    if encyclopaedia.getEntryData()[1].hasImage:   
     frame:
      xmargin 10
      yfill True
      xfill True                 
      
      xmaximum dd
      ymaximum pp  

      $current_image = encyclopaedia.getEntryData()[1].image
      add current_image crop (0,10,dd-33,pp-13)
     
    python:     
     ui.window(id="entry_window",xmargin=10,xfill=True,yfill=True,xalign=.5,xmaximum=ddd,ymaximum=pp2)
     ui.viewport(scrollbars="vertical",mousewheel=True,draggable=True,edgescroll=(0,0),xfill=True,yfill=True)
     ui.text(entry_text)
     
    hbox:

     xfill True  
  
     if encyclopaedia.getEntryData()[1].hasSubEntry:      
      textbutton "Previous Page" xalign .02 action PreviousPage(sub_cmin)
      python:
       ui.text("Page " + str(sub_current_position) + " / " + str(encyclopaedia.getEntryData()[1].pages) ) 
      textbutton "Next Page" xalign .98 action NextPage(sub_cmax)  
 
     else:
      text("")
 
  frame:
   xfill True
   xmargin 10

   yalign .98
   hbox:
    xfill True
    $sorting_mode_display = "Sorting Mode: " + encyclopaedia.sortingMode 
    text sorting_mode_display
    textbutton "Close Entry" id "close_entry_button" xalign .98 clicked [ SetVariable("sub_current_position",1), Show("encyclopaedia_list")] 

  textbutton "Previous Entry" xpos 910 ypos 13 action PreviousEntry(encyclopaedia,cmin)
  textbutton "Next Entry" xpos 1110 ypos 13 action NextEntry(encyclopaedia,cmax)