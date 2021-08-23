from cmu_112_graphics import *
import math
import ast
from new import getAnalysis

# from http://www.cs.cmu.edu/~112/notes/notes-strings.html
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

finalData = readFile('FinalData.txt')
valueDictionary = ast.literal_eval(finalData)

def categorize(currList, valueDictionary):
    minDistance=1000
    minGenre=""
    for genre in valueDictionary:
        valueList = valueDictionary[genre]
        currDistance=0
        for index in range(len(valueList)):
            entry=(currList[index]-valueList[index])**2
            currDistance+=entry
        currDistance=math.sqrt(currDistance)
        if currDistance<minDistance:
            minDistance=currDistance
            minGenre = genre
    return minGenre


def appStarted(app):
    app.currString=input("Please enter your excerpt to analyze here: ")
    currList = getAnalysis(app.currString)
    app.genre = categorize(currList, valueDictionary)
    getCover(app) #gets the image associated with genre
    genreToColor={'Adventure':"goldenrod2",
    "African American Literature":"SpringGreen2",
    "Art":"peach puff", "Banned Books":"RoyalBlue2",
    "Business":"lightgoldenrod", "Canadian Literature":"Linen",
    "Classic":"cyan2", "Computers":"Green", 'Cooking':"LightCyan3",
    "Correspondence":"lightgoldenrod", "Creative Commons":"red3",
    "Criticism":"papaya whip", "Drama":"skyblue2","Espionage":"springgreen",
    "Essays":"chocolate1","Etiquette":"bisque2","Fantasy":"tomato",
    "Fiction and Literature":"light coral","Games":"sandybrown",
    "Gay/Lesbian":"khaki4","Ghost Stories":"forestgreen", "Gothic":"goldenrod1",
    "Government Publication":'palegoldenrod',"Harvard Classics":"gray87", 
    "Health":"lemon chiffon","History":"green3", "Horror":"gray77",
    "Humor":"lightgoldenrod1", "Instructional":"blanched almond",
    "Language":"light salmon","Music":"coral","Mystery/Detective":"tomato",
    "Myth":"maroon1","Nature":"royalblue4","Nautical":"steelblue4", 
    "Non-fiction": "lightgoldenrod", "Occult":"darkgoldenrod1",
    "Periodical": "gray97","Philosophy":"gray78","Pirate Tales":"orange",
    "Poetry":"palegreen2", "Politics":"orange3","Post-1930":"lightgoldenrod",
    "Psychology":"lightsalmon", "Pulp":"Palegreen4", 
    "Random Selection":"khaki", "Reference":"SteelBlue4",
    "Religion":"lightyellow","Romance":"Red","Satire":"gray96",
    'Science':"lightgoldenrod","Science Fiction":"Light Blue2", 
    "Sexuality":"snow2", "Short Story":"misty rose",
    "Short Story Collection":"lightgoldenrod yellow",
    "Thriller":"skyblue2", "Travel":"darkolivegreen1", "War":"firebrick1",
    "Western":"gold", "Women's Studies":"bisque",
    "Young Readers":"palevioletred1"}
    app.color=genreToColor.get(app.genre,"white") #gets background color of UX

def getCover(app):
    #gets the image associated with the genre
    if app.genre=="Adventure":
        url='https://s23078.pcdn.co/wp-content/uploads/Screen-shot-2012-04-15-at-11.28.44-PM.png'
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 0.7)
    elif app.genre=="African American Literature":
        url='https://i.pinimg.com/originals/06/d5/13/06d51314d02ef1eca4915242a9bdb5a6.jpg'
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 0.7)
    elif app.genre=="Art":
        url='https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-auto-16832.jpg?itok=CklCg3cN'
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Banned Books":
        url="https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-orig-7032.jpg?itok=SzLOTSG-"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Business":
        url="https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-auto-23743.jpg?itok=mwyqOHds"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Canadian Literature":
        url="https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-orig-4504.jpg?itok=7GUogtiG"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Classic":
        url="https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-cust-1621.jpg?itok=ch16gxqH"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Computers":
        url="https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-cust-6617.jpg?itok=X5lOvFJR"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Cooking":
        url='https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQDxT6n5ntrRCZfdvZymjPP9yGJ4zTGi7Yh0e1lR3hZ0XFM2aJFEINFtjtXIF-44Pla4A2eET4o&usqp=CAc'
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.7)
    elif app.genre=="Correspondence":
        url="https://manybooks.net/titles/darwinchetext99adrwn10.html"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Creative Commons":
        url="https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-orig-29439.jpg?itok=UL3V2FNr"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Criticism":
        url="https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-cust-4062.jpg?itok=uULeONJk"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Drama":
        url="https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-cust-6331.jpg?itok=KRtl4Ol8"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Espionage":
        url="https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-orig-1285.jpg?itok=cnPObJht"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Essays":
        url='https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-cust-6908.jpg?itok=QZOjk3nG'
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Etiquette":
        url='https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-auto-3009.jpg?itok=qg4tTaDA'
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Fantasy":
        url="https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-orig-14299.jpg?itok=wPpEKSe6"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Fiction and Literature":
        url="https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-orig-1371.jpg?itok=AT7JJfHh"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Games":
        url='https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-cust-4256.jpg?itok=AGh8UYoW'
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Gay/Lesbian":
        url="https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-orig-15971.jpg?itok=HZkHZUy1"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Ghost Stories":
        url='https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-orig-13007.jpg?itok=_sl7pDVk'
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Gothic":
        url="https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-orig-6694.jpg?itok=1NNJXYUa"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Government Publication":
        url='https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-auto-22730.jpg?itok=LgpwuZ51'
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Harvard Classics":
        url="https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-cust-4852.jpg?itok=ebI82sLE"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Health":
        url="https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-cust-9634.jpg?itok=A0hiI-Uc"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="History":
        url="https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-cust-2356.jpg?itok=NsH-dAJf"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Horror":
        url='https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-cust-13095.jpg?itok=H0c1QL8Y'
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Humor":
        url='https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-orig-7033.jpg?itok=9yw2Lq07'
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Instructional":
        url="https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-orig-15945.jpg?itok=O28u0iBP"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Language":
        url="https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-orig-13195.jpg?itok=IQKS3uA8"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Music":
        url="https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-orig-29991.jpg?itok=CDdjJQGl"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Mystery/Detective":
        url="https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-orig-1704.jpg?itok=5GwsfdUd"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Myth":
        url='https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-orig-18335.jpg?itok=MBzkd61O'
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Nature":
        url="https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-orig-9536.jpg?itok=RPQNiNlZ"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Nautical":
        url="https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-cust-7150.jpg?itok=efUU_jRw"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Non-fiction":
        url="https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-orig-7949.jpg?itok=VkRqXU-8"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Occult":
        url="https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-orig-29513.jpg?itok=M2T72Mn-"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Romance":
        url='https://bookriot.com/wp-content/uploads/2019/02/By-Love-Undone-Suzanne-Enoch-cover.jpg'
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 0.5)
    elif app.genre=="Periodical":
        url='https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-orig-21468.jpg?itok=E7Hk0u9y'
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Philosophy":
        url="https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-cust-9609.jpg?itok=h3yR_sUK"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Pirate Tales":
        url='https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-orig-6054.jpg?itok=bhvnDS0c'
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Poetry":
        url='https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-cust-5719.jpg?itok=td4M8RUi'
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Politics":
        url="https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-cust-6908.jpg?itok=QZOjk3nG"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Post-1930":
        url="https://image.slidesharecdn.com/year1931cars-130725064644-phpapp02/95/year-1931-cars-1-638.jpg?cb=1374735189"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 0.7)
    elif app.genre=="Psychology":
        url="https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-orig-6031.jpg?itok=zk5X8XY0"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Pulp":
        url="https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-orig-21936.jpg?itok=VAx4AGPs"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=='Random Selection':
        url="https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-auto-30870.jpg?itok=2rL-x2Zv"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Reference":
        url='https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-orig-12105.jpg?itok=iaUQ5wwm'
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Religion":
        url="https://kbimages1-a.akamaihd.net/13f7c85f-2fa3-4556-af07-28f855b3c4d4/1200/1200/False/bible-king-james-version-authorized-kjv-1611-best-bible-for-kobo.jpg"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 0.28)
    elif app.genre=="Satire":
        url="https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-orig-3986.jpg?itok=njDXJM9j"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Science":
        url="https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-cust-2037.jpg?itok=7jEn9lV5"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Science Fiction":
        url="https://images.penguinrandomhouse.com/cover/9781400052929"
        app.bookCover=app.loadImage(url)
    elif app.genre=="Sexuality":
        url="https://manybooks.net/sites/default/files/styles/220x330sc/public/2018-11/41147717.jpg?itok=DP5V29Vt"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Short Story":
        url='https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-auto-21306.jpg?itok=KCnMGGHj'
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Short Story Collection":
        url="https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-orig-2305.jpg?itok=fKkqXRnW"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Thriller":
        url="https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-orig-5924.jpg?itok=w66aryr_"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Travel":
        url="https://images-na.ssl-images-amazon.com/images/I/51dHKuQkRPL._SX331_BO1,204,203,200_.jpg"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 0.95)
    elif app.genre=="War":
        url="https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-cust-7354.jpg?itok=3aKaEL4D"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Western":
        url="https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-cust-8177.jpg?itok=793uWgY9"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Women's Studies":
        url="https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-orig-2860.jpg?itok=OjET8Fln"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    elif app.genre=="Young Readers":
        url="https://manybooks.net/sites/default/files/styles/220x330sc/public/old-covers/cover-orig-498.jpg?itok=zY7xCyMC"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 1.3)
    else:
        #error if genre not in categories
        url="https://thumbs.dreamstime.com/z/binary-code-error-11333859.jpg"
        preBookCover=app.loadImage(url)
        app.bookCover=app.scaleImage(preBookCover, 0.44)

def keyPressed(app, event):
    if event.key=="e":
        #allows user to exit app by pressing e
        app.quit()

def redrawAll(app, canvas):
    #draw function for the app
    canvas.create_rectangle(0,0,app.width,app.height,fill=app.color)
    #draws the background color
    canvas.create_text(app.width//2,app.height//10,text=app.genre,
    font="Arial 32 bold") #writes the genre of text excerpt
    canvas.create_image(app.width//2,app.height*0.55,
    image=ImageTk.PhotoImage(app.bookCover))
    #creates the image associated with the genre


runApp(width=600, height=600)