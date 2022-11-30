from graphics import *
import time

def MoveAll(shapelist,dx,dy):
    for shape in shapelist:
        shape.move(dx,dy)

def MoveAllOnLine(shapelist,dx,dy,repetitions,delay):
    for i in range(repetitions):
        MoveAll(shapelist,dx,dy)
        time.sleep(delay)

def main():

    #main Circle

    win=GraphWin("Display",1000,500)
    p1=Point(500,250)
    cir=Circle(p1,100)
    cir.setFill("#ffcc33")
    cir.setOutline("#ffcc33")
    cir.draw(win)

    # Mouth of Emoji

    p2=Point(499.0, 266.0)
    cir1=Circle(p2,70)
    cir1.setWidth(2)
    cir1.setFill("#f5f8fa")
    cir1.move(2,-15)
    cir1.draw(win)

    p22=Point(499.0, 266.0)
    cir22=Circle(p22,72)
    cir22.setFill("#f5f8fa")
    # cir22.setWidth(5)
    cir22.setOutline("#f5f8fa")
    cir22.move(2,-25)
    cir22.draw(win)

    headMouth=[cir,cir1,cir22]

    # fill area

    pf = Point(429.0, 180.0)
    pff = Point(571.0, 246.0)
    recff = Rectangle(pf, pff)
    recff.setFill("#ffcc33")
    recff.setOutline("#ffcc33")
    recff.draw(win)

    pc=Point(534.0, 178.0)
    cpc=Circle(pc,2)
    cpc.setFill("#ffcc33")
    cpc.setOutline("#ffcc33")
    cpc.draw(win)

    pcc = Point(572.0, 232.0)
    cpcc = Circle(pcc, 12)
    cpcc.setFill("#ffcc33")
    cpcc.setOutline("#ffcc33")
    cpcc.draw(win)

    pccc = Point(572.0, 253.0)
    cpccc = Circle(pccc, 5)
    cpccc.setFill("#ffcc33")
    cpccc.setOutline("#ffcc33")
    cpccc.draw(win)

    pf1 = Point(466.0, 165.0)
    pff1 = Point(532.0, 184.0)
    recff1 = Rectangle(pf1, pff1)
    recff1.setFill("#ffcc33")
    recff1.setOutline("#ffcc33")
    recff1.draw(win)

    pf2 = Point(427.0, 240.0)
    pff2 = Point(574.0, 250.0)
    recff2 = Rectangle(pf2, pff2)
    recff2.setFill("#ffcc33")
    recff2.setOutline("#ffcc33")
    recff2.draw(win)

    pr1=Point(428.0, 244.0)
    pr4=Point(572.0, 272.0)
    rec=Rectangle(pr1,pr4)
    rec.setFill("#ffcc33")
    rec.setOutline("#ffcc33")
    rec.draw(win)

    pl=Point(434.0, 272.0)
    pll=Point(569.0, 272.0)
    lill=Line(pl,pll)
    lill.setWidth(2)
    lill.draw(win)

    pls = Point(444.0, 291.0)
    plls = Point(558.0, 291.0)
    lills = Line(pls, plls)
    lills.setWidth(1.5)
    lills.draw(win)

    prec1=Point(463.0, 177.0)
    prec2=Point(539.0, 183.0)
    rec1=Rectangle(prec1,prec2)
    rec1.setFill("#ffcc33")
    rec1.setOutline("#ffcc33")
    rec1.draw(win)

    fillArea = [recff,recff1,recff2,cpc,cpcc,cpccc,rec,lill,lills,rec1]

    # eyes

    pe=Point(459.0, 235.0)
    cirpe=Circle(pe,10)
    cirpe.setFill("#f5f8fa")
    cirpe.setWidth(7)
    cirpe.draw(win)

    pes = Point(459.0, 240.0)
    cirpes = Circle(pes, 12)
    cirpes.setFill("#ffcc33")
    cirpes.setOutline("#ffcc33")
    cirpes.draw(win)

    pe1=Point(540.0, 235.0)
    cirpe1=Circle(pe1,10)
    cirpe1.setFill("#f5f8fa")
    cirpe1.setWidth(7)
    cirpe1.draw(win)

    pe1s = Point(540.0, 240.0)
    cir1pes = Circle(pe1s, 12)
    cir1pes.setFill("#ffcc33")
    cir1pes.setOutline("#ffcc33")
    cir1pes.draw(win)

    eyes=[cirpe,cirpes,cirpe1,cir1pes]

    wholeApp = [cir, cir1, cir22,
                recff, recff1, recff2, cpc, cpcc, cpccc, rec, lill, lills,rec1,
                cirpe, cirpes, cirpe1,cir1pes]

    # >>>>>>>>> Default move <<<<<<<<<<<

    MoveAllOnLine(wholeApp, 1, 0, 400, 0)
    MoveAllOnLine(wholeApp, -1, 0, 800, 0)
    MoveAllOnLine(wholeApp, 1, 0, 400, 0)

    # >>>>>>>>> Automatic(infinite) move <<<<<<<<<

    # while True:
    #     MoveAllOnLine(wholeApp,1,0,400,0)
    #     MoveAllOnLine(wholeApp, -1, 0, 800, 0)
    #     MoveAllOnLine(wholeApp, 1, 0, 400, 0)

    # >>>>>>>>> Manual move <<<<<<<<<

    # while win.getKey()== "Right" or win.getKey()=="Left" :
    #
    #     # Press Right arrow --->
    #
    #     if win.getKey()== "Right":
    #         MoveAllOnLine(wholeApp,1,0,400,0)
    #
    #     # Press Left arrow <---
    #
    #     if win.getKey()== "Left":
    #         MoveAllOnLine(wholeApp, -1, 0, 400, 0)
    #
    #     # Press Esc (any key input) to finish loop


    win.getMouse()
    win.close()

main()