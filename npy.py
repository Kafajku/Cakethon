# NativePython
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
#Notice, that this module was built on experimental (beta) version of Python.
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
    def resize(W, H):
        W = int(W / 16)
        H = int(H / 38)
        os.system('mode con: cols=' + str(W) + ' lines=' + str(H))
        W = int(W / 2)
        H = H - 1
        return int(W / 1.90), int(H / 2)


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
            localX = int(X * 1.5)
            cur.setCoords(localX, Y)
            print(text)
            cur.setCoords(0, 0)
            self.drawn.append(text)
            self.coords.append([X, Y])
        else:
            for key, value in enumerate(text):
                localX = int(X * 1.5)
                cur.setCoords(localX, Y + key)
                print(value)
                cur.setCoords(0, 0)
                self.drawn.append(value)
                self.coords.append([X, Y + key])


    def get(self, text, X, Y):
        X = int(X * 1.5)
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
## Menus
##

class ui:
    button = 0x33
    listsel = 0x34
    check = 0x35


    class createMenu:
        def __init__(self, filename, title, dsc):
            self.selected = None
            self.items = []
            self.style = {
                "accent": Def,
                "bordering": Def,
                "normal": Def,
                "title": title,
                "dsc": dsc,
                "margins": [
                    0,
                    0
                ]
            }
            menu = self
            lines = jsonFile.imp(filename)
            if not lines == None or not lines == {}:
                if lines["document_type"] == "NPYUI-Style":
                    styles = lines["document_body"]["style_body"]
                    menu.style["accent"] = eval(styles["theme"]["accent_color"])
                    menu.style["bordering"] = eval(styles["theme"]["bordering_style"])
                    menu.style["normal"] = eval(styles["theme"]["normal_style"])
                    menu.style["margins"] = [styles["margins"]["xpos"], styles["margins"]["ypos"]]


        def refresh(self):
            accent = self.style["accent"]
            border = self.style["bordering"]
            normal = self.style["normal"]
            title = self.style["title"]
            dsc = self.style["dsc"]
            xpos = self.style["margins"][0]
            ypos = self.style["margins"][1]
            caption.create(accent + title + normal, xpos, ypos)
            if dsc != "":
                ypos += 2
                caption.create(White + dsc + normal, xpos, ypos + 1)
            else:
                ypos += 1

            for key2, value in enumerate(self.items):
                if self.selected == key2:
                    caption.create(border, xpos + 1, ypos + key2)
                if value["id"] == ui.button:
                    caption.create(value["caption"] + normal, xpos + 1, ypos + key2)
                if value["id"] == ui.listsel:
                    pos = value["index"]
                    caption.create(value["caption"] + "     " + accent + "< " + value["list"][pos] + " >" + normal, xpos + 1, ypos + key2)
                if value["id"] == ui.check:
                    caption.create(value["caption"] + "     " + accent + "[" + str(value["bool"]) + "]" + normal, xpos + 1, ypos + key2)

            if not self.selected is None:
                value = self.items[self.selected]
                if key.listenFor("enter"):
                    if not value["handler"] is None and callable(value["handler"]):
                        func = value["handler"]
                        if value["id"] == ui.button:
                            func(*value["args"])
                        if value["id"] == ui.listsel:
                            func(value["list"], value["index"])
                        if value["id"] == ui.check:
                            value["bool"] = not value["bool"]
                            func(value["bool"])
                if key.listenFor("down"):
                    if self.selected < len(self.items) - 1:
                        self.selected += 1
                if key.listenFor("up"):
                    if self.selected > 0:
                        self.selected -= 1
                if value["id"] == ui.listsel:
                    if key.listenFor("left"):
                        if value["index"] > 0:
                            value["index"] -= 1
                    if key.listenFor("right"):
                        if value["index"] < len(value["list"]) - 1:
                            value["index"] += 1

                thisWindow.sleep(125)


    def createListSel(menu, caption, handler, llist, index):
        menu.items.append({
            "id": ui.listsel,
            "caption": caption,
            "handler": handler,
            "list": llist,
            "index": index
        })
        self = menu
        if self.selected is None:
            self.selected = 0


    def createButton(menu, caption, handler, args):
        menu.items.append({
            "id": ui.button,
            "caption": caption,
            "handler": handler,
            "args": args
        })
        self = menu
        if self.selected is None:
            self.selected = 0


    def createCheck(menu, caption, handler, boolean):
        menu.items.append({
            "id": ui.check,
            "caption": caption,
            "handler": handler,
            "bool": boolean
        })
        self = menu
        if self.selected is None:
            self.selected = 0


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
            path = replaceInStr(path, "%d", "C:/Users/" + thisUser.name() + "/Desktop/")
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
    def encode(path):
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

        image = string.encode("ascii")
        image = base64.b64decode(image)
        file = open(path, "wb")
        file.write(image)
        file.close()


    def getFromURL(url):
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