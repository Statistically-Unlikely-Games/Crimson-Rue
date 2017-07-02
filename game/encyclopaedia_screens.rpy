init python:

    class Shelf():

        def __init__(self, name, limit):
            self.name = name
            self.limit = limit

            self.filtering = ""
            self.sorting = "default"
            self.completion = 0

            self.store = []
            self.available_filters = set()

        def add_book(self, book):
            if len(self.store) >= self.limit:
                return

            self.store.append(book)
            self.available_filters.add(book.kind)

        def filter(self, key):
            self.filtering = key

        def sort(self, method="asc"):
            if method == "asc":
                self.store.sort(key=lambda book: book.name)
            elif method == "dsc":
                self.store.sort(key=lambda book: book.name, reverse=True)

        def get_completion(self):
            return len(self.store) / float(self.limit) * 100

        def list_books(self):
            return [book for book in self.store if not self.filtering or book.kind == self.filtering]

    class Book():

        def __init__(self, name, kind, author, year):
            self.name = name
            self.kind = kind
            self.year = year
            self.author = author

            self.pages = 0
            self.last_opened_page = 0

            self.store = []

        def add_page(self, title, image, icon, text, stats, page_no=0, unlocked=False):
            self.pages += 1

            if not page_no:
                page_no = self.pages

            entry = Page(title, image, icon, text, stats, page_no, unlocked)
            self.store.insert(page_no, entry)

        def remove_page(self, page_no):
            page_no -= 1

            # Remove the page from the book
            self.store[page_no].rip()

        def restore_page(self, page_no):
            page_no -= 1

            # Add the page from the book
            self.store[page_no].restore()

        def unlock_page(self, page_no):
            page_no -=  1

            self.store[page_no].unlock()

        def unlock_range(self, type, start=0, number=0):
            """
            type: String. Can be "next", "previous", "all"
            """

            if type == "next":
                first = start
                last = start + number
            elif type == "previous":
                first = start + number
                last = start
            elif type == "all":
                for page in self.store:
                    page.unlock()
                return

            page_range = [i for i in range(first, last)]

            for i in page_range:
                self.unlock_page(i)

        def get_toc(self):
            return self.store

        def get_page(self, page=0, move=""):
            """
            move: String. Can be next, previous
            """

            if page:
                self.last_opened_page = page - 1
                print self.last_opened_page

            if move == "next":
                self.last_opened_page += 1
            elif move == "previous":
                self.last_opened_page -= 1

            return self.store[self.last_opened_page]

        def next_page(self):
            if self.last_opened_page < len(self.store) - 1:
                return True
            return False

        def previous_page(self):
            if self.last_opened_page > 0:
                return True
            return False

    class Page():

        def __init__(self, title, image, icon, text, stats, page_no, unlocked):
            self.icon = icon
            self.text = text
            self.title = title
            self.image = image
            self.stats = stats
            self.page_no = page_no
            self.unlocked = unlocked

            self.original = {
                "icon": self.icon,
                "text": self.text,
                "title": self.title,
                "image": self.image,
                "stats": self.stats
            }

        def unlock(self):
            self.unlocked = True

        def lock(self):
            self.unlocked = False

        def reorder(self, new_no):
            self.page_no = new_no

        def update_text(self, new):
            self.text = new

        def update_stats(self, new):
            self.stats = new

        def rip(self):
            self.icon = "Ripped"
            self.text = "Ripped"
            self.title = "Ripped"
            self.image = Null()
            self.stats = "Ripped"

        def restore(self):
            self.icon = self.original["icon"]
            self.text = self.original["text"]
            self.title = self.original["title"]
            self.image = self.original["image"]
            self.stats = self.original["stats"]

    class NextPage(Action):

        def __init__(self, book):
            self.book = book

        def __call__(self):
            cs = renpy.current_screen()

            cs.scope["page"] = self.book.get_page(move="next")
            renpy.restart_interaction()

        def get_sensitive(self):
            return self.book.next_page()

    class PreviousPage(Action):

        def __init__(self, book):
            self.book = book

        def __call__(self):
            cs = renpy.current_screen()

            cs.scope["page"] = self.book.get_page(move="previous")
            renpy.restart_interaction()

        def get_sensitive(self):
            return self.book.previous_page()

    class ShowPage(Action):

        def __init__(self, book, page_no):
            self.book = book
            self.page_no = page_no

        def __call__(self):
            cs = renpy.current_screen()

            cs.scope["page"] = self.book.get_page(page=self.page_no)
            renpy.restart_interaction()

    class AddBook(Action):

        def __init__(self, book):
            self.book = book

        def __call__(self):
            shelf.add_book(self.book)

screen book_shelf():
    tag encyclopedia
    add Solid("#000000") alpha 0.75

    frame:
        xsize 200
        ysize 40

        background Solid("#d3d3d3")

        text shelf.name size 32 xalign 0.5 yalign 0.5
        xalign 0.5
        ypos -1
        
    frame:
        xsize 100
        xalign 1.0
        ypos 60
        background Solid("#d3d3d3")

        button:
            xfill True

            idle_background Solid("#d3d3d3")
            hover_background Solid( Color("#d3d3d3").tint(0.5) )
            selected_background Solid( Color("#d3d3d3").shade(0.5) )

            text "X" color "#000000" align (0.5, 0.5)

            action [Hide("book_shelf"), Jump("apothecary_shop")]

    vbox:
        ypos 150
        spacing 15

        for book in shelf.list_books():
            button:
                xfill True

                idle_background Solid("#d3d3d3")
                hover_background Solid( Color("#d3d3d3").tint(0.5) )
                selected_background Solid( Color("#d3d3d3").shade(0.5) )

                text book.name xalign 0.5 yalign 0.5

                action Show("open_book", book=book)

    hbox:
        spacing 10
        xalign 1.0
        yalign 1.0

        textbutton _("Sort") action Function(callable=shelf.sort, method="dsc")
        textbutton _("R Sort") action Function(callable=shelf.sort)

    hbox:
        spacing 10
        xalign 0.0
        yalign 1.0

        for i in shelf.available_filters:
            textbutton _(i) action Function(callable=shelf.filter, key=i)

        textbutton _("None") action Function(callable=shelf.filter, key="")

screen open_book(book):
    tag encyclopedia

    default page = book.get_page()
    default toc = False
    default hide_text = False

    frame:
        xfill True
        background Solid("#d3d3d3")

        text book.name xalign 0.5 yalign 0.5

    frame:
        xsize 500
        xalign 0.5
        ypos 60
        background Solid("#d3d3d3")

        text page.title xalign 0.5 yalign 0.5

    frame:
        xsize 100
        xalign 1.0
        ypos 60
        background Solid("#d3d3d3")

        button:
            xfill True

            idle_background Solid("#d3d3d3")
            hover_background Solid( Color("#d3d3d3").tint(0.5) )
            selected_background Solid( Color("#d3d3d3").shade(0.5) )

            text "X" color "#000000" align (0.5, 0.5)

            action Show("book_shelf")

    hbox:
        ysize 40
        spacing 12
        yalign 0.98

        button:
            xsize config.screen_width / 3 - 6

            idle_background Solid("#d3d3d3")
            hover_background Solid( Color("#d3d3d3").tint(0.5) )
            selected_background Solid( Color("#d3d3d3").shade(0.5) )
            insensitive_background Solid( Color("#d3d3d3").tint(1.0) )

            text "<<" color "#000000" align (0.5, 0.5)

            action PreviousPage(book)

        button:
            xsize config.screen_width / 3 - 6

            idle_background Solid("#d3d3d3")
            hover_background Solid( Color("#d3d3d3").tint(0.5) )
            selected_background Solid( Color("#d3d3d3").shade(0.5) )

            text "Table of Content" color "#000000" align (0.5, 0.5)

            action SetScreenVariable("toc", True)

        button:
            xsize config.screen_width / 3 - 6

            idle_background Solid("#d3d3d3")
            hover_background Solid( Color("#d3d3d3").tint(0.5) )
            selected_background Solid( Color("#d3d3d3").shade(0.5) )
            insensitive_background Solid( Color("#d3d3d3").tint(0.95) )

            text ">>" color "#000000" align (0.5, 0.5)

            action NextPage(book)

    frame:
        xfill True
        ysize 520

        yalign 0.64

        if page.image:
            background page.image
        else:
            background Solid("#000000")

        button:
            xsize config.screen_width - 280
            ysize 520

            background Solid("#00000000")

            action ToggleScreenVariable("hide_text", true_value=True, false_value=False)

        if not hide_text:
            frame:
                xsize 350
                ysize 520
                xalign 1.0
                xoffset 4
                ypos -5

                background Solid("#00000050")

                viewport:
                    draggable True
                    mousewheel True

                    area (0, 0, 350, 515)

                    text page.text color "#ffffff"

    if toc:
        frame:
            xsize 500
            ysize 650

            xalign 0.5
            yalign 0.5

            background Solid("#000000")

            text "Table of Contents" xalign 0.5 ypos 10
            button:
                xysize(35, 35)
                align (1.0, 0.012)

                text "X" xalign 0.5 yalign 0.5

                action SetScreenVariable("toc", False)

            viewport:
                draggable True
                mousewheel True

                area (0, 50, 500, 600)

                vbox:
                    for i in book.get_toc():
                        button:
                            xfill True
                            ysize 50

                            idle_background Solid("#d3d3d3")
                            hover_background Solid( Color("#d3d3d3").tint(0.5) )
                            selected_background Solid( Color("#d3d3d3").shade(0.5) )

                            text i.title xmaximum 380 xalign 0.1 yalign 0.5
                            text str(i.page_no) xalign 0.95 yalign 0.5

                            selected (i.page_no == page.page_no)
                            action ShowPage(book, i.page_no)
