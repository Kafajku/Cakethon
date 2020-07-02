# Cakethon
#Please notice, that I've built this module on Python 3.8!
#Copyright (c) since 2020 by Kazafka - All rights reserved.


##
## Important modules
##

import os
#If you see any errors due running your Python app, please, execute below commands via CMD:
# pip install pywin32
# pip install keyboard
# pip install python-varname
# pip install requests
import sys
import datetime
import win32gui
import win32api
import ctypes
import keyboard
import time
import msvcrt
import json
from varname import nameof
import getpass
import base64
import requests
import importlib


##
## JSON files
##

class jsonFile:
    def imp(path):
        if os.path.isfile(path):
            lines = ""
            file = open(path)
            for line in file:
                lines += line
            while "null" in lines:
                pos = lines.find("null")
                llist = list(lines)
                llist[pos:pos + len("null")] = "None"
                lines = "".join(llist)
            while "false" in lines:
                pos = lines.find("false")
                llist = list(lines)
                llist[pos:pos + len("false")] = "False"
                lines = "".join(llist)
            while "true" in lines:
                pos = lines.find("true")
                llist = list(lines)
                llist[pos:pos + len("true")] = "True"
                lines = "".join(llist)
            lines = eval(lines)
            return lines


    def exp(path, array):
        file = open(path, "w")
        jsonstr = json.dumps(array, indent = 4)
        file.write(jsonstr)
        file.close()



##
## Console cursor (moovement)
##

class cur:
    def setCoords(X, Y):
        POS = X * 2 + (Y << 16)
        handler = ctypes.windll.kernel32.GetStdHandle(ctypes.c_long(-11))
        ctypes.windll.kernel32.SetConsoleCursorPosition(handler, ctypes.c_ulong(POS))


##
## Window stuff
##

class thisWindow:
    def move(title, X, Y, W, H):
        hwnd = win32gui.FindWindow(None, title)
        win32gui.MoveWindow(hwnd, X, Y, W, H, True)


    def compactSize():
        if not os.path.isfile("npy_plugin-lc.cmd"):
            plugin = open("npy_plugin-lc.cmd", "w")
            plugin.write("@echo off\nsetlocal\n\nset \"lines=\"\nset \"cols=\"\nfor /F \"tokens=2 delims=:\" %%a in ('mode con') do for %%b in (%%a) do (\n   if not defined lines (\n      set \"lines=%%b\"\n   ) else if not defined cols (\n      set \"cols=%%b\"\n   )\n)\necho [%cols%, %lines%]>@results.txt\nexit")
            plugin.close()
        os.system("start npy_plugin-lc.cmd")
        time.sleep(0.5)
        results = open("@results.txt")
        lines = ""
        for line in results:
            lines += line
        results.close()
        os.system("del @results.txt")
        os.system("del npy_plugin-lc.cmd")
        lines = eval(lines)
        line = lines[1]
        col = lines[0]
        os.system("mode con: cols=" + str(col) + " lines=" + str(line))


    def close():
        sys.exit(0)


    def cls():
        os.system('cls')


    def title(title):
        os.system('title ' + title)


    def pause():
        return msvcrt.getch()


    def sleep(delay = 0):
        time.sleep(delay / 1000)


##
## Colors
##

Black = "\033[0;30;40m"
Gray = '\u001b[30;1m'
Red = '\u001b[31;1m'
Green = '\u001b[32;1m'
Yellow = '\u001b[33;1m'
Blue = '\u001b[34;1m'
Magenta = '\u001b[35;1m'
Cyan = '\u001b[36;1m'
White = '\u001b[37;1m'
Underline = '\u001b[4m'
Reverse = '\u001b[7m'
Def = '\u001b[0m'


##
## Mouse (position)
##

class mouse:
    def getCoords():
        POS = win32api.GetCursorPos()
        return POS[0], POS[1]


    def setCoords(X, Y):
        win32api.SetCursorPos((X, Y))


##
## Keys
##

class key:
    def listenFor(name):
        return keyboard.is_pressed(name)


    def press(name):
        keyboard.press_and_release(name)


    def hold(name):
        keyboard.press(name)


    def release(name):
        keyboard.release(name)


##
## Timers
##

class createTimer:
    def __init__(self, delay = 0):
        self.attached = []
        self.currTime = time.time()
        self.delay = delay / 1000


    def attach(self, name):
        if not name is None:
            self.attached.append(name)


    def detach(self, name):
        if name in self.attached:
            self.attached.remove(name)


    def attached(self, name):
        if name in self.attached:
            return True
        return False


    def refresh(self, args = []):
        if time.time() - self.delay > self.currTime:
            self.currTime = time.time()
            for key, value in enumerate(self.attached):
                value(*args)


##
## Text
##

class caption:
    def __init__(self):
        self.drawn = []
        self.coords = []


    def create(self, text, X, Y):    
        if not isinstance(text, list):
            localX = X
            cur.setCoords(localX, Y)
            print(text)
            cur.setCoords(0, 0)
            self.drawn.append(text)
            self.coords.append([X, Y])
        else:
            for key, value in enumerate(text):
                localX = X
                cur.setCoords(localX, Y + key)
                print(value)
                cur.setCoords(0, 0)
                self.drawn.append(value)
                self.coords.append([X, Y + key])


    def get(self, text, X, Y):
        cur.setCoords(X, Y)
        got = input(text)
        cur.setCoords(0, 0)
        self.drawn.append(text)
        self.coords.append(Y)
        return got


    def delete(self, X, Y):
        if [X, Y] in self.coords:
            i = self.coords.index([X, Y])
            text = self.drawn[i]
            llen = len(str(text))
            spaces = ""
            for _ in range(llen):
                spaces += "#"
            localX = int(X * 1.5)
            cur.setCoords(localX, Y)
            print(Black + spaces + Def)
            cur.setCoords(0, 0)
            self.coords.pop(i)
            self.drawn.pop(i)


    def cls(self):
        for key, value in enumerate(self.coords):
            cur.setCoords(value[0], value[1])
            text = self.drawn[key]
            __ = ""
            for _ in range(len(str(text))):
                __ += " "
            print(__)
            cur.setCoords(0, 0)
            self.coords.pop(key)
            self.drawn.pop(key)
caption = caption()


##
## JSON models (sprites)
##

class jsonSprite:
    def __init__(self, path):
        self.array = jsonFile.imp(path)


    def show(self):
        array = self.array
        if array["manifest"] == "sprite":
            folder = array["model"]["namespace"]
            layers = array["model"]["layers"]
            X = array["model"]["margins"][0]
            Y = array["model"]["margins"][1]
            for layer in layers:
                if layer["type"] == "file":
                    path = folder + layer["source"]
                    color = eval(layer["color"])
                    file = open(path)
                    lines = []
                    for line in file:
                        lines.append(line)
                    file.close()
                    caption.create(color, X, Y)
                    caption.create(lines, X, Y)
                elif layer["type"] == "text":
                    texts = layer["source"]
                    color = eval(layer["color"])
                    caption.create(color, X, Y)
                    caption.create(texts, X, Y)


##
## Current user
##

class thisUser:
    def name():
        return getpass.getuser()


##
## A file explorer
##

class fileExplorer:
    title = "File explorer"
    select = "Type file/folder index to select: "
    path = "Type " + Green + "$ " + Def + "to select current path"
    default = "Type " + Green + "% " + Def + "to go back to default dir"


    def explore(path = "%c"):
        def replaceInStr(b, o, n):
            i = b.find(o)
            l = list(b)
            l[i:i + len(o)] = n
            return "".join(l)

        if "%u" in path:
            path = replaceInStr(path, "%u", thisUser.name())
        if "%c" in path:
            path = replaceInStr(path, "%c", "C:")
        if "%d" in path:
            path = replaceInStr(path, "%d", "C:/Users/" + thisUser.name() + "/Desktop")
        if "%g" in path:
            path = replaceInStr(path, "%g", os.getcwd() + "")
        old = path

        def isStrConvToInt(s):
            try:
                int(s)
                return True
            except ValueError:
                return False

        def getExtensionOf(s):
            if "." in s:
                i = s.find(".")
                l = list(s)
                e = "".join(l[i:i + (len(s) - 1)])
                return e
            else:
                return -1

        while not os.path.isfile(path):
            if fileExplorer.title == "%p":
                fileExplorer.title = path
            thisWindow.cls()
            print(fileExplorer.title)
            print("")
            found = os.listdir(path)
            for key2, value in enumerate(found):
                if os.path.exists(path + value + "/"):
                    found[key2] = value + "/"
                print(Green + "[" + str(key2) + "] " + Def + found[key2])
            print("")
            print(fileExplorer.path)
            print(fileExplorer.default)
            goto = input(fileExplorer.select)
            check = isStrConvToInt(goto)
            if check:
                selection = int(goto)
                if selection <= (len(found) - 1) and selection >= 0:
                    item = found[int(goto)]
                    item = path + item
                    path = item
            elif goto == "$":
                return path
            elif goto == "%":
                path = old
        return path


##
## (Custom) files
##

class customFile:
    def __checkForShorts__(path):
        def replaceInStr(b, o, n):
            i = b.find(o)
            l = list(b)
            l[i:i + len(o)] = n
            return "".join(l)

        if "%u" in path:
            path = replaceInStr(path, "%u", thisUser.name())
        if "%c" in path:
            path = replaceInStr(path, "%c", "C:")
        if "%d" in path:
            path = replaceInStr(path, "%d", "C:/Users/" + thisUser.name() + "/Desktop")
        if "%g" in path:
            path = replaceInStr(path, "%g", os.getcwd() + "")

        return path


    def encode(path):
        path = customFile.__checkForShorts__(path)

        if os.path.isfile(path):
            def getFileName(s):
                i = s.rfind("/")
                l = list(s)
                return "".join(l[i + 1:len(l)])

            name = getFileName(path)
            file = open(path, "rb")
            string = file.read()
            string = base64.b64encode(string)
            file.close()
            return name, string.decode("ascii")


    def decode(path, string):
        path = customFile.__checkForShorts__(path)

        image = string.encode("ascii")
        image = base64.b64decode(image)
        file = open(path, "wb")
        file.write(image)
        file.close()


    def importFromURL(url):
        def getFileName(s):
            i = s.rfind("/")
            l = list(s)
            return "".join(l[i + 1:len(l)])

        name = getFileName(url)
        path = os.getcwd() + "/"
        image = requests.get(url, allow_redirects = True).content
        file = open(path + name, "wb")
        file.write(image)
        file.close()
        name, image = customFile.encode(path + name)
        os.remove(path + name)
        return name, image


    def exportToURL(path, url):
        def getFileName(s):
            i = s.rfind("/")
            l = list(s)
            return "".join(l[i + 1:len(l)])

        path = customFile.__checkForShorts__(path)
        name = getFileName(path)

        file = {
            "file": open(path, "rb")
        }
        requests.post(url, files = file)

        return name


##
## Exports (using functions from different modules)
##

class exports:
    def call(module, variable, args):
        name = module
        module = importlib.import_module(name)
        val = getattr(module, variable)(*args)
        del module
        return val


    def get(module, variable):
        name = module
        module = importlib.import_module(name)
        val = getattr(module, variable)
        del module
        return val


##
## Layouts
##

class layout:
    items = []


    def addItem(item):
        layout.items.append(item)


    def removeItem(item):
        layout.items.remove(item)


    def clearItems():
        layout.items = []


    class text:
        def __init__(self, x, y, text, color):
            self.type = "text"
            self.x = x
            self.y = y
            self.text = text
            self.color = color
            layout.addItem(self)


        def setX(self, x):
            self.x = x


        def setY(self, y):
            self.y = y


        def setText(self, text):
            self.text = text


        def setColor(self, color):
            self.color = color


    class clickable:
        def __init__(self, x, y, text, color):
            self.type = "clickable"
            self.x = x
            self.y = y
            self.text = text
            self.color = color
            self.endX = (x + int(len(text) / 2)) + 1
            layout.addItem(self)


        def setX(self, x):
            self.x = x


        def setY(self, y):
            self.y = y


        def setText(self, text):
            self.text = text


        def setOnClick(self, method):
            self.onClick = method


        def setColor(self, color):
            self.color = color


    class lister:
        def __init__(self, x, y, text, color):
            self.type = "lister"
            self.x = x
            self.y = y
            self.text = text
            self.color = color
            self.endX = (x + int(len(text) / 2)) + 1
            layout.addItem(self)


        def setX(self, x):
            self.x = x


        def setY(self, y):
            self.y = y


        def setText(self, text):
            self.text = text


        def setList(self, llist, defaultPos = 0):
            self.dict = None
            self.list = llist
            self.defpos = defaultPos


        def setDict(self, ddict, defaultKey):
            self.list = None
            self.dict = ddict

            def getDictKeys(theDict):
                theList = []
                for key in theDict.keys():
                    theList.append(key)
                return theList

            self.helpList = getDictKeys(self.dict)
            self.defkey = defaultKey
            self.defhelppos = self.helpList.index(self.defkey)


        def setOnClick(self, method):
            self.onClick = method


        def setColor(self, color):
            self.color = color


    def inspectHitboxes():
        x, y = mouse.getCoords()
        x, y = int(x / 18), int(y / 24)
        return x, y


    def refresh():
        for item in layout.items:
            if item.type == "text" or item.type == "clickable":
                caption.create(item.color + item.text + Def, item.x, item.y)
            else:
                if not item.list is None:
                    caption.create(item.color + item.text + "     <" + item.list[item.defpos] + ">" + Def, item.x, item.y)
                else:
                    caption.create(item.color + item.text + "     <" + item.dict[item.defkey] + ">" + Def, item.x, item.y)

            if item.type == "clickable":
                var = item.endX - item.x
                for xPos in range(var):
                    x, y = layout.inspectHitboxes()
                    if x == item.x + xPos and y == item.y:
                        if key.listenFor("space"):
                            item.onClick()
                            thisWindow.sleep(125)

            if item.type == "lister":
                var = item.endX - item.x
                for xPos in range(var):
                    x, y = layout.inspectHitboxes()
                    if x == item.x + xPos and y == item.y:
                        if key.listenFor("space"):
                            if not item.list is None:
                                item.onClick(item.list, item.defpos)
                                thisWindow.sleep(125)
                            else:
                                item.onClick(item.dict, item.defkey)
                                thisWindow.sleep(125)

                        if key.listenFor("d"):
                            if not item.list is None:
                                if item.defpos < len(item.list) - 1:
                                    item.defpos += 1
                                    thisWindow.sleep(125)
                            else:
                                if item.defhelppos < len(item.helpList) - 1:
                                    item.defhelppos += 1
                                    item.defkey = item.helpList[item.defhelppos]
                                    thisWindow.sleep(125)

                        if key.listenFor("a"):
                            if not item.list is None:
                                if item.defpos > 0:
                                    item.defpos -= 1
                                    thisWindow.sleep(125)
                            else:
                                if item.defhelppos > 0:
                                    item.defhelppos -= 1
                                    item.defkey = item.helpList[item.defhelppos]
                                    thisWindow.sleep(125)


    def imp(path):
        layout.clearItems()
        
        path = customFile.__checkForShorts__(path)

        array = jsonFile.imp(path)
        __manifest = array["manifest"]
        __body = array["body"]
        for item in __body:
            pos = item.find("@")
            pos2 = item.find(".")

            typeof = item[pos + 1:pos2]
            name = item[pos2 + 1:len(item)]

            __x = __body[item]["x"]
            __y = __body[item]["y"]
            __text = __body[item]["text"]
            __color = __body[item]["color"]

            globals()[name] = eval("layout." + typeof)(__x, __y, __text, __color)


class dialog:
    def error(title, message):
        text = "x = msgbox(\"" + message + "\",0+16,\"" + title + "\")"
        file = open("msgbox.vbs", "w")
        file.write(text)
        file.close()
        os.system("start msgbox.vbs")


    def info(title, message):
        text = "x = msgbox(\"" + message + "\",0+64,\"" + title + "\")"
        file = open("msgbox.vbs", "w")
        file.write(text)
        file.close()
        os.system("start msgbox.vbs")
