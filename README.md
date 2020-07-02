    Cakethon 2.02
## Changelog
###### cake.py 1.28 - added `customFile` class;
###### cake.py 1.30 - added `exports` class;
###### cake.py 1.85 - deleted whole `ui` class;
###### cake.py 1.86 - deleted function `resize()` from `thisWindow` class;
###### cake.py 1.87 - added function `move()` to `thisWindow` class;
###### cake.py 1.91 - added `layout` class and supported `.json` files;
###### cake.py 1.97 - added function `removeItem()` to class `layout`;
###### cake.py 1.98 - added function `clearItems()`, also, to class `layout`;
###### cake.py 2.01 - added support for element `lister` (`layout` class);
###### cake.py 2.02 - added `dialog` class;

# Introduction

About six months ago I've decided to create an open source, light module to use in Python. This is, how it ended. I wanted to share my work - Cakethon.

# Topics

List of topics touched by me here (on the bottom):

1. License

2. Downloading the module

3. Helping me in Cakethon improvements

4. A guide to using module

5. Some comments about stuff

6. How to create JSON sprites and layouts

7. Summary

# License

This project is officially licensed under JFPU License 1.0. To see more info, read file "License.md".

# Downloading the module

After you, hopefully, understand how this project works, we can move on this thing and finally - download Cakethon. So, go ahead and do it!

# Helping me in Cakethon improvements

Also, as a part of Cakethon community, you can give me your own suggestions to improve official version of Cakethon.

# A guide to using module

Okay, that was the hardest part for me, because I had to make a complete list of things to cover in there, anyways, let's go.

## Before the guide

Since Cakethon uses different modules around, to actually make itself functional, I just wanted to say, that some of these modules are not automatically available for Python - you have to install them manually.

How to do this? Well, what you wanna do, is go to your CMD and execute following commands, to install all necessary modules:
```

pip install pywin32

pip install keyboard

pip install python-varname

pip install requests
```

Notice one more thing - I've built Cakethon on Python 3.8, so if you're using older versions of Python, these modules might not be available/work correctly for you.

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

] `move(title, X, Y, W, H)` - moves, and resizes, any window (depending on the title).

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

###### Exports (using functions from different modules)

`exports` (class)

] `call(module, variable, args)` - returns the value of given function from a module; args must be a list (later unpacked to single arguments).

] `retrive(module, variable)` - returns value of specified variable, which is in the module.

###### Layouts

`layout` (class)

] `addItem(item)` - adds item to the layout (use only if you make layout directly in your Python file).

] `text(self, x, y, text, color)` (class) - creates a new text element (use only if you make layout directly in your Python file).

] ] `setX(self, x)` - sets position on X axis.

] ] `setY(self, y)` - changes position on Y axis.

] ] `setText(self, text)` - makes the text of element change.

] ] `setColor(self, color)` - tells the element to use other color.

] `clickable(self, x, y, text, color)` (class) - generates a new so called "clickable" element (use only if you make layout directly in your Python file).

] ] `setX(self, x)` - sets position on X axis.

] ] `setY(self, y)` - changes position on Y axis.

] ] `setText(self, text)` - makes the text of element change.

] ] `setColor(self, color)` - tells the element to use other color.

] ] `setOnClick(method)` - changes the whole function, which will be called after the button's pressed (use always, even, if you are making layout via `.json` file).

] `lister(self, x, y, text, color)` (class) - makes a new element, which is a `list` and `dict` selector; use only if you make layout directly in your Python file.

] ] `setX(self, x)` - sets position on X axis.

] ] `setY(self, y)` - changes position on Y axis.

] ] `setText(self, text)` - makes the text of element change.

] ] `setColor(self, color)` - tells the element to use other color.

] ] `setOnClick(self, method)` - sets `onClick` definition for the `lister` element (use always, even, if you are making layout via `.json` file).

] ] `setList(self, list, defaultPos = 0)` - makes the `lister` element use given list (use always, even, if you are making layout via `.json` file).

] ] `setDict(self, dict, defaultKey)` - tells `lister` element to use given dict (use always, even, if you are making layout via `.json` file).

] `memo(self, text, x, y, color)` (class) - creates a new, memo type element; use only if you make layout directly in your Python file.

] ] `setX(self, x)` - sets the x position of `memo` element.

] ] `setY(self, Y)` - sets position on y axis of element.

] ] `setColor(self, color)` - changes color of `memo`.

] ] `setOnClick(self, method)` - makes the `onClick` method of `memo` element change.

] `inspectHitboxes()` - returns current mouse position; however, this mouse pos is devided by some numbers, so it's kinda relative to the Python window. Note, that even if this function returns kinda-relative mouse pos to the Python Window, you have to use function `move()` from `thisWindow` class. More in **Some comments about stuff**.

] `refresh()` - put in `while` loop

###### Dialog boxes

`dialog` (class)

] `info(title, message)` - generates a dialog box with ***OK*** button and ***Information*** icon.

] `error(title, message)` - creates simple dialog box, which is including ***OK*** button and, of course, ***Error*** icon.

# Some comments about stuff

## Classes

Actually, there are some things I've gotta tell about classes and functions inside Cakethon module. For first, let's tell, that classes like `createTimer` (classes with `create` keyword) are used to make instances, unlike classes such as `caption`, also, in case of class `caption`, it has it's own, default instance, others, are just classes to normal use.

Also, after the update **1.91**, I should tell something, if you are using `layout` class. Since it is using mouse position, you got to make it somehow even more relative, to the Python window, so I deleted the `resize()` function and replaced it with `move()` function (`thisWindow` class, I recommend reading **changelog** also), which will let you to move any window and resize it at once. Within it, you don't want to change your Python window's title, otherwise, `move()` function will be probably useless. You want to always move the Python window to position `0, 0`, `width` and `height` can be set as you want, and the `title` must be the Python window's title.

## Functions

I guess, that the only function, that I've got to describe is `create()` from class `caption`. Why? Hmmm... in this function, you can also use lists to place multi lined text. It looks like this:

###### Syntax:

```
caption.create("Single lined text", 5, 5) #Single lined
caption.create("", 5, 6) #A simple space between texts
caption.create(["Multi", "lined", "text"], 5, 7) #Multi lined
```

###### Output:

```
Single lined text

Multi
lined
text
```

## Arguments

Another thing, which I forgot to mention in this section, that probably all `args` arguments of functions, must be `lists`. Those lists, will be later unpacked, to the actual arguments of a function.

###### Example:

```
def exampleFunction(arg1, arg2):
  print(arg1 + ", " + arg2)
  
newmenu = cake.ui.createMenu("example.json", "Example menu", "")
ui.createButton(newmenu, "Example button", exampleFunction, ["value1", "value2"])
```

## Some elements of layouts

In layouts we have some elements that we can click and do other stuff with them. Since I've made all of this, I wanted to let you know *here* how to click on particular elements, choose item from `listers` or edit `memos`.

###### General

Press **`spacebar`** to click on item (`text` element not supported).

###### Clickables

*Like, well, there's nothing special about it; just press the **click** key.*

###### Listers

Press **`A`** to select previous item from `lister`.

Press **`D`** to select next item in `lister`.

Press **click** key to select current item (in funtion, it returns the `list` of `lister` and `position` of `lister`'s `list`).

###### Memos

Press **`E`** to edit the `memo`.

Press **`enter`** to end editing the memo.

Press **click** key to select current `text` of `memo`.

# How to create JSON sprites and layouts

Well, this one might be a bit tricky, because from my last updates, a structure of such a JSON file has been changed. So, let's go right into it!

Structure of a layout JSON file is presented in "layout1.json"

And structure of a JSON sprite is presented in "sprite1.json"

Now, this structure has a simple feature - type. There are two types - "file" and "text".

"file" type is for *.txt* files and other text documents.

"text" type is for lists and strings, like this: `["Multi", "lined", "sprite"]` or: `"Single lined text"`.

# Summary

Thank you for reading this whole document, I hope. I also hope, that you will enjoy using Cakethon. I'm really happy, to finally share my work after 6 months of making it. Well, welcome to the community of Cakethon!

###### Copyright © Cakethon since 2020 by Kafajku - All rights reserved.
