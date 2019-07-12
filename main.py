import trans as t

print("The Translator")
input("press enter...")
while True:
    print("options:\n1. translate\n2. present a file\n3. quit")
    usr = int(input())
    if usr == 1:
        source = input("The source language .... (ISO lang code)\n")
        target = input("which language would you want to translate to? (ISO lang code)\n")
        string = input("what is it you want to translate?\n")
        string = t.Translate(target=target,string=string,source=source)
        res = string.getOutput()
        print(res)
    elif usr == 2:
        doc = input("please name the file and format(.txt)\n")
        source = input("The source language .... (ISO lang code)\n")
        target = input("which language would you want to translate to? (ISO lang code)\n")
        name = input("target name file?\n")
        ffile = t.File(doc=doc,target=target,source=source,targetF=name)
        ffile.create()
    elif usr == 3:
        print("thanks")
        break
    print("continue? [y/n]")
    usr = input()
    if usr == "y":
        pass
    elif usr == "n":
        break
