import re 

import os
from urllib import parse 
import time
import clean
""""
VTODO : REPLACE CUSTOM COMMANDS WITH THEIR DEFINITION AT LOCATION
    LINKS NOT WORKING CORRECTLY ANYMORE no idea why

"""
def parseTheorems(text):
    theorems = {}
    for line in text : 
        if line.startswith(r"\begin{document}"):
            break 
        elif line.startswith(r"\newtheorem"):
            res = re.search("{(.*)}",line)
            res = res.group(1).split("}{")
            theorems[res[0]] = [res[1],1]
    return theorems
#needs work to implement arguments
def parseCommands(text):
    commands = {}
    for line in text : 
        if line.startswith(r"\begin{document}"):
            break 
        elif line.startswith(r"\newcommand"):
            l = line.split("\\")  
            name = l[2][:-1]
            command = re.search("{(.*)}",line).group(1)
            commands[name] = command
    return commands
def generateDefaultContent(title):
    return f'---\n title: "{title}"\n mathjax : true\n---\n'

def linkToToc(title,pathToFile):
    with open(f"content/_index.md","a") as f :
        f.write(f"[{title}]({pathToFile}.md)  \n")

def writeLink(title,section):
    with open(f"content/{section}/{section}.md","a") as f :
        f.write(f'[{title}]({section}/{title}.md)  \n')
def writeLinkByPath(title,path):

    linkPath = path.split("/")[1:]
    linkPath[-1] = title
    with open(f"{path}.md","a") as f :
        f.write(f'[{title}]({"/".join(linkPath)}.md)  \n')
def sectionLinks(i,line,section,index=0):
    #when we find a section we extract the section name , create a folder for the section 
    # and create a Markdownfile that links to the subsections
    if line.startswith("\\section"):
        section = re.search("{(.*)}",line).group(1)
        section = cleanName(section)
        if not os.path.exists(f"~/AnimationenUni/texParser/content/{section}"):
            os.mkdir(rf"content/{section}")
        with open(f"content/{section}/{section}.md","a") as f :
            f.write(generateDefaultContent(section))
        linkToToc(section,pathToFile=f"{section}/{section}")
        index +=1
    return section , index
def subsectionLinks(i,line,between,section,prevTitle,start,sectionIndex,theorems):
    #when we find a subsection , we check if we re at the end or start and depending on that 
    # we create a .tex file contatinign the subsection content , convert that tex file to .md using pandoc 
    # and link to the section .md file
    link = None
    if line.startswith("\\subsection"):
        title = re.search("{(.*)}",line).group(1)
        title = cleanName(title)
        # print(title)
        if between:
            content =  text[start+1:i]
            path = f"content/{section}/{prevTitle}"
            with open(f"{path}.tex","a") as f:
                # print(path)
                f.write(clean.clean("\n".join(content),theorems,sectionIndex))

            with open(f"{path}.md","a") as f:
                f.write(generateDefaultContent(prevTitle))
            os.system(f"pandoc -f latex -t markdown {path}.tex >> {path}.md")
            link = (prevTitle,f"content/{section}/{section}")
            between=False
            # writeLink(prevTitle,section)
        else: 
            start = i 
            prevTitle = title
            between = True
    return between,prevTitle,start,link
def cleanName(name):
    illegalCharacters = ["$","\\"," ","/","'","."]
    for c in illegalCharacters : 
        if c in name:
            name = name.replace(c,"_")
    return name 
def theoremLinks(i,line,section,subsection,name,start,theorems,sectionIndex):
    link = None
    if line.startswith(r"\end"): 
        # print(name)
        name = cleanName(name) 
        theoremName = re.search("{(.*)}",line).group(1)
        if theoremName in theorems :  
            content = text[start+1:i]
            path = f"content/{section}/{name}" 
            with open(f"{path}.tex","a") as f :
                f.write(clean.clean("\n".join(content),theorems,sectionIndex))
            with open(f"{path}.md","a") as f:
                f.write(generateDefaultContent(name))
            os.system(f"pandoc -f latex -t markdown {path}.tex >> {path}.md")
            #if we write links , the links will appear at the top of the subsection, ISSUE
            # We save the name and link to write to and return it and write all the links after the first pass through
            #should also do that with sections and subsections
            link = (name,f"content/{section}/{subsection}")
            # writeLinkByPath(name,f"content/{section}/{subsection}")
    if line.startswith(r"\begin"):
        theoremName = re.search("{(.*)}",line).group(1)
        if theoremName in theorems:
            try:
                name = re.search("\[(.*)\]",line).group(1)
            except AttributeError:
                name = theorems[theoremName][0] + f"{sectionIndex}.{theorems[theoremName][1]}"
                theorems[theoremName][1] +=1  
            start = i 
    return start,name,theorems,link

#READ IN SOURCE TEX FILE
with open("Markovketten-Skript.tex","r") as f :
    text = f.read().splitlines()

# INITIALIZE DEFAULTS

#CREATE _index.md 
with open("content/_index.md","a") as f :
    f.write(generateDefaultContent("ToC"))
#LOOP OVER text [type list] 
commands = parseCommands(text)
theorems = parseTheorems(text)
theorems["proof"]= ["Beweis",1]
# print(commands)
# print(theorems)

def links(text,theorems):
    order = ["subsection","theorems"]
    linksToWrite = {"subsection":[],
                    "theorems":[]}
    between = False
    prevTitle = ""
    start = 0
    start2 = 0
    name = ""
    section=""
    sectionIndex=0
    for i,line in enumerate(text) : 
        section,sectionIndex = sectionLinks(i,line,section,sectionIndex) 
        between,prevTitle,start,subsectionLink = subsectionLinks(i,line,between,section,prevTitle,start,sectionIndex,theorems)
        start2,name,theorems,theoremLink = theoremLinks(i,line,section,prevTitle,name,start2,theorems,sectionIndex)
        if subsectionLink :
            linksToWrite["subsection"].append(subsectionLink)
        if theoremLink:
            linksToWrite["theorems"].append(theoremLink)
    for k in order: 
        for link in linksToWrite[k]:
            writeLinkByPath(link[0],link[1])

links(text,theorems) 
       
     

