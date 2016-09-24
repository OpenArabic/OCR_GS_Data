import os, shutil

folder = "./ara/book_IbnFaqihHamadhani.Buldan/5_goldStandard/"

htmlTop = """

<!DOCTYPE html>
<html>

<head>
  <title>Creating GoldStandard</title>

  <meta charset="UTF-8">
  <meta name="description" content="Reviewing OCR Training/Testing Data">
  <meta name="keywords" content="HTML">
  <meta name="author" content="Open ITI Corpus Team">

  <link href='http://fonts.googleapis.com/earlyaccess/amiri.css' rel='stylesheet' type='text/css'>
  
    <style>
      body {background-color: white;}
      p {color: red; direction: rtl; font-size: 38pt; text-align: center; font-family: "Geeza Pro",  "Amiri"}
      h1 {color: blue; font-size: 28pt; text-align: left}
      img {height: 50pt; text-align: center}
    </style>

</head>

<body>

<table style="width:100%" align="center">
"""

htmlBot = """

</table>

</body>

</html>


"""

def getText(fileName):
    with open(fileName[:-4]+'.gt.txt', "r", encoding="utf8") as f1:
        text = f1.read()
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

def createHTMLs(lines):
    files = os.listdir(folder)

    counter = 0
    table = []

    for f in files:
        if f.endswith(".png"):
            # <a href="file://C:/path/to/file/file.html">Link Anchor</a>
            href = '<h1><a href="%s">%s</a></h1>'
            head = href % ((folder+f[:-4]+'.gt.txt'), (f[:-4]+'.gt.txt'))
            tags = head + '<p><img src="%s"><br>' % (folder+f)
            text = tags+"%s</p>" % getText(folder+f)
            table.append('<tr align="center">%s</tr><hr>' % text)
            counter += 1
            if counter % lines == 0:
                with open("%s%06d.html" % (pref, counter), "w", encoding="utf8") as f9:
                    f9.write(htmlTop + "\n\n".join(table) + htmlBot)
                table = []
                print("%s%06d.html" % (pref, counter))
                #input("Check!")

    newCount = roundup(counter, lines)
    with open("%s%06d.html" % (pref, newCount), "w", encoding="utf8") as f9:
        f9.write(htmlTop + "\n\n".join(table) + htmlBot)
        print("%s%06d.html" % (pref, newCount))
        

folder = "./5_goldStandard_b/"
pref   = "gs_IbnFaqihBuldan_b_"
#folder = os.path.abspath(folder)+"/"
createHTMLs(100)    

        
        
