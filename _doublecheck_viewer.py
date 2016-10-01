import os, shutil

htmlTop = """

<!DOCTYPE html>
<html>

<head>
  <title>fileName</title>

  <meta charset="UTF-8">
  <meta name="description" content="Reviewing OCR Training/Testing Data">
  <meta name="keywords" content="HTML">
  <meta name="author" content="Open ITI Corpus Team">

  <link href='http://fonts.googleapis.com/earlyaccess/amiri.css' rel='stylesheet' type='text/css'>
  
    <style>
      body {background-color: white;}
      p {color: red; direction: rtl; font-size: 22pt; font-weight: bold; text-align: center; font-family: "Courier New", "Geeza Pro",  "Amiri"}
      h1 {color: darkgreen; font-size: 20pt; text-align: left; font-family: "Baskerville",  "Garamond"}
      img {height: 50pt; text-align: center}
      #download_button {
      position: fixed;
      padding: 0;
      text-align: left;
      width: 15%;
      bottom: 10px;
      right: 20px;
      font-size: 16pt;
      color: #8B0000;
      font-weight: bold;
      }
      
    </style>

</head>

<body>

<table style="width:100%" align="center">
"""

htmlBot = """

</table>

<a id="download_button">To Save: `Ctrl+s`, make sure to choose `Webpage, complete`!</a>

</body>

</html>


"""

def getText(fileName):
    with open(fileName[:-4]+'.gt.txt', "r", encoding="utf8") as f1:
        text = f1.read()
        text = text.replace('"', "«»")
        #print(text)
        #text = list(text)
        #print(text)
        #text.reverse()
        #print(text)
        #text = "".join(text)
        #print(text)
        #input()
        return(text)

import math
def roundup(x, par):
    newX = int(math.ceil(int(x) / float(par)) * par)
    return(newX)

def createHTMLs(folder, pref, lines):
    files = os.listdir(folder)

    relFolder = folder.split("/")
    relFolder = "./"+"/".join(relFolder[-2:])+"/"
    #input(relFolder)

    counter = 0
    table = []

    for f in files:
        if f.endswith(".png"):
            # <a href="file://C:/path/to/file/file.html">Link Anchor</a>
            href = '<h1>File: %s (if the image is defective, simply delete all Arabic text and the line will be excluded)</h1>'
            head = href % (f[:-4]+'.gt.txt')
            tags = head + '<p><img src="%s"></p>' % (relFolder+"/"+f)
            text = tags+"<p contenteditable=\"true\" fileNameId=\"%s\">%s</p>" % ((f[:-4]+'.gt.txt'), getText(folder+"/"+f))
            table.append('<tr align="center">%s</tr><hr>' % text)
            counter += 1
            if counter % lines == 0:
                fileName = "%s%06d.html" % (pref, counter)
                corr = fileName[:-5]+"_corrected.html"
                newHTML = htmlTop.replace(">fileName<", ">"+fileName[:-5]+"_corrected.html<")
                with open("./ara/"+fileName, "w", encoding="utf8") as f9:
                    f9.write(newHTML + "\n\n".join(table) + htmlBot)
                table = []
                print("%s%06d.html" % (pref, counter))
                #input("Check!")

    newCount = roundup(counter, lines)
    fileName = "%s%06d.html" % (pref, newCount)
    corr = fileName[:-5]+"_corrected.html"
    newHTML = htmlTop.replace(">fileName<", ">"+fileName[:-5]+"_corrected.html<")
    with open("./ara/"+fileName, "w", encoding="utf8") as f9:
        f9.write(newHTML + "\n\n".join(table) + htmlBot)


def processAll():
    sub = "./ara/"
    lofol = os.listdir(sub)
    suf = "/7_final/"

    for fol in lofol:
        if fol.startswith(("book_", "lq_")):
            print(fol+suf)
            folder = sub+fol+suf
            pref = (os.path.abspath(folder)).split("/")[-2].replace(".","_")
            pref = "dc_"+pref+"_"
            print(pref)
            createHTMLs(os.path.abspath(folder), pref, 50)    

processAll()       
        
