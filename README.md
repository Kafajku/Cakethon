# Introduction

About six months ago I've decided to create an open source, light module to use in Python. This is, how it ended. I wanted to share my work - NativePython.

# Topics

List of topics touched by me here (on the bottom):

1. Policy of mine

2. Downloading the module

3. Helping me in NativePython improvements

4. A guide to using module

5. How to create JSON sprites and menu styles

6. Summary

# Policy of mine

Since it is on open source, you can edit it and share your own modified version of NativePython with users. But I wanted to strict out one thing.
g
Now, you might be a bit confused, because I have told you, that i share my work on open source license, which means exactly, that you can modify my project and publish your own, modified version. But I wanted to make sure, you do respect my work, so please, include me as a part of credits.

# Downloading the module

After you, hopefully, understand my policy, we can move on this thing and finally - download NativePython. So, go ahead and do it!

# Helping me in NativePython improvements

Also, as a part of NativePython community, you can give me your own suggestions to improve official version of NativePython.

# A guide to using module

Okay, that was the hardest part for me, because I had to make a complete list of things to cover in there, anyways, let's go.

## Before the guide

Since NativePython uses different modules around, to actually make itself functional, I just wanted to say, that some of these modules are not automatically available for Python - you have to install them manually.

How to do this? Well, what you wanna do, is go to your CMD and execute following commands, to install all necessary modules:
```

pip install pywin32

pip install keyboard

pip install python-varname

pip install requests
```

Notice one more thing - I've built NativePython on Python 3.8, so if you're using older versions of Python, these modules might not be available/work correctly for you.

## The right guide

###### JSON Files

JSON (JavaScript Object Notation) files are type of documents, that are storing JSON objects, which are same as Python dicts.

To use functions for JSON files, you want to also use `jsonFile` class.

Functions of following class:

] `imp(path)` - reads JSON file from given path and returing it's object (Python's dict).

] `exp(path, array)` - takes given path and dict (array) and saves it into JSON file.

Console cursor (moovement)

Console cursor is a blinking rectangle, which is indicating where next character will be placed.

Class: `cur`

Functions:

] `setCoords(X, Y)` - sets x and y position of the console cursor.

###### Window stuff

Well, what can I say, I have added some functions, that modifies window.

Class name: `thisWindow`

Functions of this class:

] `resize(W, H)` - resizes your window.

] `compactSize()` - sets your window's size to compact, making it scorllable.

] `close()` - closes your window/exists from your Python app.

] `cls()` - clears your whole window (text).

] `title(title)` - sets your window's title to given one.

] `pause()` - pauses the Python script.

] `sleep(delay)` - your Python app is sleeping for given amount of time in ms.

###### Colors

There is nothing much to say about colors - I will just place here list of all colors (as variables):
```

Black

Gray

Red

Green

Yellow

Blue

Magenta

Cyan

White

Underline

Reverse

Def
```

###### Mouse (position)

Functions from this class (`mouse`) are setting/getting the current position of mouse cursor.

All functions:

] `getCoords()` - returns x and y position of mouse cursor, notice, that it is retriving mouse postition relative to Python's app window, which means, that it is not always accurate.

] `setCoords(X, Y)` - sets the x and y position of mouse cursor.

###### Keys

*Since I've got many, many more things to cover in this post, let me just to put classes' names and their functions - of course, I will put functions descriptions but - not classes descriptions.*

`key` (class)

] `listenFor(name)` - listens for a selected key press, remember, to put this function into if statement.

] `press(name)` - (not physically) presses selected key.

] `hold(name)` - holds selected key.

] `release(name)` - releases (always, not only if key is held) selected key.

###### Timers

`createTimer(self, delay)` (class) - makes a new timer.

] `attach(self, name)` - attaches a function to given timer.

] `detach(self, name)` - detaches a function (only if it's is attached)

] `attached(self, name)` - checks, if function is already attached to given timer.

] `refresh(self, args = [])` - (put into while loop) refreshes timer, runs all attached functions, with given arguments (args).

###### Text

`caption` (class)

] `create(self, text, X, Y)` - creates a text at given pos (x, y).

] `get(self, text, X, Y)` - creates an input on x and y coords.

] `delete(self, X, Y)` - deletes a caption at selected x, y.

] `cls(self)` - deletes all the captions created with caption class.

###### Menus

`ui` (class)

] `ui.button`

] `ui.listsel`

] `ui.check`

] `createMenu(self, filename, title, dsc)` (class) - creates a menu from a filename, which is JSON file style path.

]] `refresh(self)` - refreshes menu (put within while loop).

] `createButton(menu, caption, handler, args)` - creates a button with given caption, sets it's handler, also, arguments.

] `createCheck(menu, caption, handler, boolean)` - makes a list checkbox, with caption, handler and default boolean.

] `createListSel(menu, caption, handler, llist, index)` - this function is creating a list selector, with set caption, handler, base list and default index.

###### JSON models (sprites)

`jsonModel(self, path)` (class) - generates a model with given JSON file (path).

] `show(self)` - shows generated sprite.

###### Current user

`thisUser` (class)

] `name()` - returns name of current user.

###### A file exporer

`fileExplorer` (class)

] `title` = "File explorer"

] `select` = "Type file/folder index to select: "

] `path` = "Type " + Green + "$ " + Def + "to select current path"

] `default` = "Type " + Green + "% " + Def + "to go back to default dir"

] `explore(path)` - explores given directory.

###### (Custom) files

`customFile` (class)

] `encode(path)` - reads and ecodes file from given path; returns two values - name of the file, that has been selected and it's encoded value.

] `decode(path)` - decodes file from given path; useful when getting files from URL and exactly decoding encoded files.

] `getFromURL(url)` - requesting reading files from given url; also, returns two values - name of the requested file and automatically encoded value of it.

# How to create JSON sprites and menu styles

Well, this one might be a bit tricky, because from my last updates, a structure of such a JSON file has been changed. So, let's go right into it!

Structure of a menu style JSON file is presented in "menu1.json"

And structure of a JSON sprite is presented in "sprite1.json"
Now, this structure has a simple feature - type. There are two types - "file" and "text".
"file" type is for *.txt* files and other text documents.
"text" type is for lists and strings, like this: `["Multi", "lined", "sprite"]` or: `"Single lined text"`. Also, you can use lists in `caption.create()` function, because `text` argument can also be a list, not only a string.

# Summary

Thank you for reading this whole document, I hope. I also hope, that you will enjoy using NativePython. I'm really happy, to finally share my work after 6 months of making it. Well, welcome to the community of NativePython!
