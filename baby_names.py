#Ajay Katoch
#CSC 110
from drawingpanel import *
def main():
    x = 1890-10
    name, gender = nameAndGender(x)
    info = fileInfo(name,gender)
    line = meanings(name,gender)
    p=draw(name,gender,line)
    dates(x,p,info)
    boxes(p,info)
    



def nameAndGender(x):
    print("This program allows you to search through the")
    print("data from the Social Security Administration")
    print("to see how popular a particular name has been")
    print("since "+ str(x)+".")
    print()
    name = input("Name: ")
    gender = input("Gender: ")
    return name, gender
    
    

def fileInfo(name, gender):
    file = open("names.txt")
    fileTwo = open("names2.txt")
    lines = file.readlines()
    linesTwo = fileTwo.readlines()
    for line in lines:
        if(name.lower() in line.lower()):
            numbers = line.strip()
            print(numbers)
            return numbers
    print("Name:", name)
    print("Gender:",gender)
    print(name ,"not found.")
            
            

def meanings(name,gender):
    file = open("meanings.txt")
    lines = file.readlines()
    for line in lines:
        if(name.lower() in line.lower()):
            print(line.strip())
            return line
    print(name, gender,"(no meaning found)")

def draw(name,gender,line):
    p = DrawingPanel(780,560, background="white")
    p.canvas.create_rectangle(0, 560, 780, 530, fill ="light gray", width=1)
    p.canvas.create_rectangle(0, 0, 780, 30 , fill = "light gray" ,width=1)
    p.canvas.create_line(0, 780, 0, 30 , fill="black", width=0)
    p.canvas.create_line(0, 530, 780, 530 , fill="black", width=0)
    p.canvas.create_text(390,16,text= line,fill="black")
    return p

def boxes(p,info):
    wide = 30
    height = 530
    count = 0 
    y = info.split()
    if(y[1]=="m"):
        color = "green"
    else:
        color = "yellow"

    for lines in y:
        eq = (count- 2) * 60
        count +=1
        if(lines is "0"):
            p.canvas.create_line(eq, height, eq+wide, height, fill = color, width=0)
            p.canvas.create_text(eq, height,text= lines,fill="black")
        elif(count>2):
            p.canvas.create_rectangle(eq, height, eq+wide, wide+(int(lines)/2), fill = color, width=0)
            p.canvas.create_text(eq, wide+(int(lines)/2),text= lines,fill="black")

def dates(x,p,info):
    y = info.split()
    count = 0
    for lines in y:
        count +=1
        if(count>2):
            x += 10
            axis=(count-3)*60+15
            p.canvas.create_text(axis, 552, text=x ,fill="black")
        

main()    
    
    
    
    
    
    
    
