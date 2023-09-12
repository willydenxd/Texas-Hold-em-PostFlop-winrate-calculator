import tkinter as tk
from PIL import ImageTk
from PIL import Image
from pokerface import *
from itertools import combinations


class Calculator(tk.Frame):
    global deck
    deck = StandardDeck()
    global btnctr
    btnctr = 0
    global leftHandStr
    leftHandStr = ''
    global rightHandStr
    rightHandStr = ''
    global boardStr
    boardStr = ''
    global leftWinRate
    leftWinRate = 0
    global rightWinRate
    rightWinRate = 0
    global TieRate
    TieRate = 0
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.createBoard()
        self.createHand()
        self.createAllCard()
        self.showWinRate()
    def createBoard(self):
        backSideImg = Image.open('C:\\Users\\xiuhu\\Downloads\\card back red.png')
        backSideImg_size = (144,100)
        backSideImg.thumbnail(backSideImg_size)
        self.backSide = ImageTk.PhotoImage(backSideImg)
        self.flop1 = tk.Label(self,image = self.backSide)
        self.flop1.grid(row = 0,column = 4)
        self.flop2 = tk.Label(self,image = self.backSide)
        self.flop2.grid(row = 0,column = 5)
        self.flop3 = tk.Label(self,image = self.backSide)
        self.flop3.grid(row = 0,column = 6)
        self.turn = tk.Label(self,image = self.backSide)
        self.turn.grid(row = 0,column = 7)
        self.river = tk.Label(self,image = self.backSide)
        self.river.grid(row = 0,column = 8)
    def createHand(self):
        self.leftHand1 = tk.Label(self,image = self.backSide)
        self.leftHand1.grid(row = 3,column = 1)
        self.leftHand2 = tk.Label(self,image = self.backSide)
        self.leftHand2.grid(row = 3,column = 2)
        self.rightHand1 = tk.Label(self,image = self.backSide)
        self.rightHand1.grid(row = 3,column = 10)
        self.rightHand2 = tk.Label(self,image = self.backSide)
        self.rightHand2.grid(row = 3,column = 11)
    def createAllCard(self):        
        spadeAImg = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\ace_of_spades2.png')
        spadeA_size = (144,100)
        spadeAImg.thumbnail(spadeA_size)
        self.spadeA = ImageTk.PhotoImage(spadeAImg)
        self.btnAs = tk.Button(self,image = self.spadeA,borderwidth = 0,command = self.clickAs)
        self.btnAs.grid(row = 4,column = 0)
        
        spade2Img = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\2_of_spades.png')
        spade2_size = (144,100)
        spade2Img.thumbnail(spade2_size)
        self.spade2 = ImageTk.PhotoImage(spade2Img)
        self.btn2s = tk.Button(self,image = self.spade2,borderwidth = 0,command = self.click2s)
        self.btn2s.grid(row = 4,column = 1)
        
        spade3Img = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\3_of_spades.png')
        spade3_size = (144,100)
        spade3Img.thumbnail(spade3_size)
        self.spade3 = ImageTk.PhotoImage(spade3Img)
        self.btn3s = tk.Button(self,image = self.spade3,borderwidth = 0,command = self.click3s)
        self.btn3s.grid(row = 4,column = 2)

        spade4Img = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\4_of_spades.png')
        spade4_size = (144,100)
        spade4Img.thumbnail(spade4_size)
        self.spade4 = ImageTk.PhotoImage(spade4Img)
        self.btn4s = tk.Button(self,image = self.spade4,borderwidth = 0,command = self.click4s)
        self.btn4s.grid(row = 4,column = 3)

        spade5Img = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\5_of_spades.png')
        spade5_size = (144,100)
        spade5Img.thumbnail(spade2_size)
        self.spade5 = ImageTk.PhotoImage(spade5Img)
        self.btn5s = tk.Button(self,image = self.spade5,borderwidth = 0,command = self.click5s)
        self.btn5s.grid(row = 4,column = 4)

        spade6Img = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\6_of_spades.png')
        spade6_size = (144,100)
        spade6Img.thumbnail(spade6_size)
        self.spade6 = ImageTk.PhotoImage(spade6Img)
        self.btn6s = tk.Button(self,image = self.spade6,borderwidth = 0,command = self.click6s)
        self.btn6s.grid(row = 4,column = 5)

        spade7Img = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\7_of_spades.png')
        spade7_size = (144,100)
        spade7Img.thumbnail(spade7_size)
        self.spade7 = ImageTk.PhotoImage(spade7Img)
        self.btn7s = tk.Button(self,image = self.spade7,borderwidth = 0,command = self.click7s)
        self.btn7s.grid(row = 4,column = 6)

        spade8Img = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\8_of_spades.png')
        spade8_size = (144,100)
        spade8Img.thumbnail(spade8_size)
        self.spade8 = ImageTk.PhotoImage(spade8Img)
        self.btn8s = tk.Button(self,image = self.spade8,borderwidth = 0,command = self.click8s)
        self.btn8s.grid(row = 4,column = 7)

        spade9Img = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\9_of_spades.png')
        spade9_size = (144,100)
        spade9Img.thumbnail(spade9_size)
        self.spade9 = ImageTk.PhotoImage(spade9Img)
        self.btn9s = tk.Button(self,image = self.spade9,borderwidth = 0,command = self.click9s)
        self.btn9s.grid(row = 4,column = 8)

        spade10Img = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\10_of_spades.png')
        spade10_size = (144,100)
        spade10Img.thumbnail(spade10_size)
        self.spade10 = ImageTk.PhotoImage(spade10Img)
        self.btnTs = tk.Button(self,image = self.spade10,borderwidth = 0,command = self.clickTs)
        self.btnTs.grid(row = 4,column = 9)

        spadeJImg = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\jack_of_spades2.png')
        spadeJ_size = (144,100)
        spadeJImg.thumbnail(spadeJ_size)
        self.spadeJ = ImageTk.PhotoImage(spadeJImg)
        self.btnJs = tk.Button(self,image = self.spadeJ,borderwidth = 0,command = self.clickJs)
        self.btnJs.grid(row = 4,column = 10)

        spadeQImg = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\queen_of_spades2.png')
        spadeQ_size = (144,100)
        spadeQImg.thumbnail(spadeQ_size)
        self.spadeQ = ImageTk.PhotoImage(spadeQImg)
        self.btnQs = tk.Button(self,image = self.spadeQ,borderwidth = 0,command = self.clickQs)
        self.btnQs.grid(row = 4,column = 11)

        spadeKImg = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\king_of_spades2.png')
        spadeK_size = (144,100)
        spadeKImg.thumbnail(spadeK_size)
        self.spadeK = ImageTk.PhotoImage(spadeKImg)
        self.btnKs = tk.Button(self,image = self.spadeK,borderwidth = 0,command = self.clickKs)
        self.btnKs.grid(row = 4,column = 12)


        heartAImg = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\ace_of_hearts.png')
        heartA_size = (144,100)
        heartAImg.thumbnail(heartA_size)
        self.heartA = ImageTk.PhotoImage(heartAImg)
        self.btnAh = tk.Button(self,image = self.heartA,borderwidth = 0,command = self.clickAh)
        self.btnAh.grid(row = 5,column = 0)
        
        heart2Img = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\2_of_hearts.png')
        heart2_size = (144,100)
        heart2Img.thumbnail(heart2_size)
        self.heart2 = ImageTk.PhotoImage(heart2Img)
        self.btn2h = tk.Button(self,image = self.heart2,borderwidth = 0,command = self.click2h)
        self.btn2h.grid(row = 5,column = 1)
        
        heart3Img = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\3_of_hearts.png')
        heart3_size = (144,100)
        heart3Img.thumbnail(heart3_size)
        self.heart3 = ImageTk.PhotoImage(heart3Img)
        self.btn3h = tk.Button(self,image = self.heart3,borderwidth = 0,command = self.click3h)
        self.btn3h.grid(row = 5,column = 2)

        heart4Img = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\4_of_hearts.png')
        heart4_size = (144,100)
        heart4Img.thumbnail(heart4_size)
        self.heart4 = ImageTk.PhotoImage(heart4Img)
        self.btn4h = tk.Button(self,image = self.heart4,borderwidth = 0,command = self.click4h)
        self.btn4h.grid(row = 5,column = 3)

        heart5Img = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\5_of_hearts.png')
        heart5_size = (144,100)
        heart5Img.thumbnail(heart2_size)
        self.heart5 = ImageTk.PhotoImage(heart5Img)
        self.btn5h = tk.Button(self,image = self.heart5,borderwidth = 0,command = self.click5h)
        self.btn5h.grid(row = 5,column = 4)

        heart6Img = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\6_of_hearts.png')
        heart6_size = (144,100)
        heart6Img.thumbnail(heart6_size)
        self.heart6 = ImageTk.PhotoImage(heart6Img)
        self.btn6h = tk.Button(self,image = self.heart6,borderwidth = 0,command = self.click6h)
        self.btn6h.grid(row = 5,column = 5)

        heart7Img = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\7_of_hearts.png')
        heart7_size = (144,100)
        heart7Img.thumbnail(heart7_size)
        self.heart7 = ImageTk.PhotoImage(heart7Img)
        self.btn7h = tk.Button(self,image = self.heart7,borderwidth = 0,command = self.click7h)
        self.btn7h.grid(row = 5,column = 6)

        heart8Img = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\8_of_hearts.png')
        heart8_size = (144,100)
        heart8Img.thumbnail(heart8_size)
        self.heart8 = ImageTk.PhotoImage(heart8Img)
        self.btn8h = tk.Button(self,image = self.heart8,borderwidth = 0,command = self.click8h)
        self.btn8h.grid(row = 5,column = 7)

        heart9Img = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\9_of_hearts.png')
        heart9_size = (144,100)
        heart9Img.thumbnail(heart9_size)
        self.heart9 = ImageTk.PhotoImage(heart9Img)
        self.btn9h = tk.Button(self,image = self.heart9,borderwidth = 0,command = self.click9h)
        self.btn9h.grid(row = 5,column = 8)

        heart10Img = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\10_of_hearts.png')
        heart10_size = (144,100)
        heart10Img.thumbnail(heart10_size)
        self.heart10 = ImageTk.PhotoImage(heart10Img)
        self.btnTh = tk.Button(self,image = self.heart10,borderwidth = 0,command = self.clickTh)
        self.btnTh.grid(row = 5,column = 9)

        heartJImg = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\jack_of_hearts2.png')
        heartJ_size = (144,100)
        heartJImg.thumbnail(heartJ_size)
        self.heartJ = ImageTk.PhotoImage(heartJImg)
        self.btnJh = tk.Button(self,image = self.heartJ,borderwidth = 0,command = self.clickJh)
        self.btnJh.grid(row = 5,column = 10)

        heartQImg = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\queen_of_hearts2.png')
        heartQ_size = (144,100)
        heartQImg.thumbnail(heartQ_size)
        self.heartQ = ImageTk.PhotoImage(heartQImg)
        self.btnQh = tk.Button(self,image = self.heartQ,borderwidth = 0,command = self.clickQh)
        self.btnQh.grid(row = 5,column = 11)

        heartKImg = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\king_of_hearts2.png')
        heartK_size = (144,100)
        heartKImg.thumbnail(heartK_size)
        self.heartK = ImageTk.PhotoImage(heartKImg)
        self.btnKh = tk.Button(self,image = self.heartK,borderwidth = 0,command = self.clickKh)
        self.btnKh.grid(row = 5,column = 12)

        diamondAImg = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\ace_of_diamonds.png')
        diamondA_size = (144,100)
        diamondAImg.thumbnail(diamondA_size)
        self.diamondA = ImageTk.PhotoImage(diamondAImg)
        self.btnAd = tk.Button(self,image = self.diamondA,borderwidth = 0,command = self.clickAd)
        self.btnAd.grid(row = 6,column = 0)
        
        diamond2Img = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\2_of_diamonds.png')
        diamond2_size = (144,100)
        diamond2Img.thumbnail(diamond2_size)
        self.diamond2 = ImageTk.PhotoImage(diamond2Img)
        self.btn2d = tk.Button(self,image = self.diamond2,borderwidth = 0,command = self.click2d)
        self.btn2d.grid(row = 6,column = 1)
        
        diamond3Img = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\3_of_diamonds.png')
        diamond3_size = (144,100)
        diamond3Img.thumbnail(diamond3_size)
        self.diamond3 = ImageTk.PhotoImage(diamond3Img)
        self.btn3d = tk.Button(self,image = self.diamond3,borderwidth = 0,command = self.click3d)
        self.btn3d.grid(row = 6,column = 2)

        diamond4Img = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\4_of_diamonds.png')
        diamond4_size = (144,100)
        diamond4Img.thumbnail(diamond4_size)
        self.diamond4 = ImageTk.PhotoImage(diamond4Img)
        self.btn4d = tk.Button(self,image = self.diamond4,borderwidth = 0,command = self.click4d)
        self.btn4d.grid(row = 6,column = 3)

        diamond5Img = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\5_of_diamonds.png')
        diamond5_size = (144,100)
        diamond5Img.thumbnail(diamond2_size)
        self.diamond5 = ImageTk.PhotoImage(diamond5Img)
        self.btn5d = tk.Button(self,image = self.diamond5,borderwidth = 0,command = self.click5d)
        self.btn5d.grid(row = 6,column = 4)

        diamond6Img = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\6_of_diamonds.png')
        diamond6_size = (144,100)
        diamond6Img.thumbnail(diamond6_size)
        self.diamond6 = ImageTk.PhotoImage(diamond6Img)
        self.btn6d = tk.Button(self,image = self.diamond6,borderwidth = 0,command = self.click6d)
        self.btn6d.grid(row = 6,column = 5)

        diamond7Img = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\7_of_diamonds.png')
        diamond7_size = (144,100)
        diamond7Img.thumbnail(diamond7_size)
        self.diamond7 = ImageTk.PhotoImage(diamond7Img)
        self.btn7d = tk.Button(self,image = self.diamond7,borderwidth = 0,command = self.click7d)
        self.btn7d.grid(row = 6,column = 6)

        diamond8Img = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\8_of_diamonds.png')
        diamond8_size = (144,100)
        diamond8Img.thumbnail(diamond8_size)
        self.diamond8 = ImageTk.PhotoImage(diamond8Img)
        self.btn8d = tk.Button(self,image = self.diamond8,borderwidth = 0,command = self.click8d)
        self.btn8d.grid(row = 6,column = 7)

        diamond9Img = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\9_of_diamonds.png')
        diamond9_size = (144,100)
        diamond9Img.thumbnail(diamond9_size)
        self.diamond9 = ImageTk.PhotoImage(diamond9Img)
        self.btn9d = tk.Button(self,image = self.diamond9,borderwidth = 0,command = self.click9d)
        self.btn9d.grid(row = 6,column = 8)

        diamondTImg = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\10_of_diamonds.png')
        diamondT_size = (144,100)
        diamondTImg.thumbnail(diamondT_size)
        self.diamondT = ImageTk.PhotoImage(diamondTImg)
        self.btnTd = tk.Button(self,image = self.diamondT,borderwidth = 0,command = self.clickTd)
        self.btnTd.grid(row = 6,column = 9)

        diamondJImg = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\jack_of_diamonds2.png')
        diamondJ_size = (144,100)
        diamondJImg.thumbnail(diamondJ_size)
        self.diamondJ = ImageTk.PhotoImage(diamondJImg)
        self.btnJd = tk.Button(self,image = self.diamondJ,borderwidth = 0,command = self.clickJd)
        self.btnJd.grid(row = 6,column = 10)

        diamondQImg = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\queen_of_diamonds2.png')
        diamondQ_size = (144,100)
        diamondQImg.thumbnail(diamondQ_size)
        self.diamondQ = ImageTk.PhotoImage(diamondQImg)
        self.btnQd = tk.Button(self,image = self.diamondQ,borderwidth = 0,command = self.clickQd)
        self.btnQd.grid(row = 6,column = 11)

        diamondKImg = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\king_of_diamonds2.png')
        diamondK_size = (144,100)
        diamondKImg.thumbnail(diamondK_size)
        self.diamondK = ImageTk.PhotoImage(diamondKImg)
        self.btnKd = tk.Button(self,image = self.diamondK,borderwidth = 0,command = self.clickKd)
        self.btnKd.grid(row = 6,column = 12)    


        clubAImg = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\ace_of_clubs.png')
        clubA_size = (144,100)
        clubAImg.thumbnail(clubA_size)
        self.clubA = ImageTk.PhotoImage(clubAImg)
        self.btnAc = tk.Button(self,image = self.clubA,borderwidth = 0,command = self.clickAc)
        self.btnAc.grid(row = 7,column = 0)
        
        club2Img = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\2_of_clubs.png')
        club2_size = (144,100)
        club2Img.thumbnail(club2_size)
        self.club2 = ImageTk.PhotoImage(club2Img)
        self.btn2c = tk.Button(self,image = self.club2,borderwidth = 0,command = self.click2c)
        self.btn2c.grid(row = 7,column = 1)
        
        club3Img = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\3_of_clubs.png')
        club3_size = (144,100)
        club3Img.thumbnail(club3_size)
        self.club3 = ImageTk.PhotoImage(club3Img)
        self.btn3c = tk.Button(self,image = self.club3,borderwidth = 0,command = self.click3c)
        self.btn3c.grid(row = 7,column = 2)

        club4Img = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\4_of_clubs.png')
        club4_size = (144,100)
        club4Img.thumbnail(club4_size)
        self.club4 = ImageTk.PhotoImage(club4Img)
        self.btn4c = tk.Button(self,image = self.club4,borderwidth = 0,command = self.click4c)
        self.btn4c.grid(row = 7,column = 3)

        club5Img = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\5_of_clubs.png')
        club5_size = (144,100)
        club5Img.thumbnail(club2_size)
        self.club5 = ImageTk.PhotoImage(club5Img)
        self.btn5c = tk.Button(self,image = self.club5,borderwidth = 0,command = self.click5c)
        self.btn5c.grid(row = 7,column = 4)

        club6Img = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\6_of_clubs.png')
        club6_size = (144,100)
        club6Img.thumbnail(club6_size)
        self.club6 = ImageTk.PhotoImage(club6Img)
        self.btn6c = tk.Button(self,image = self.club6,borderwidth = 0,command = self.click6c)
        self.btn6c.grid(row = 7,column = 5)

        club7Img = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\7_of_clubs.png')
        club7_size = (144,100)
        club7Img.thumbnail(club7_size)
        self.club7 = ImageTk.PhotoImage(club7Img)
        self.btn7c = tk.Button(self,image = self.club7,borderwidth = 0,command = self.click7c)
        self.btn7c.grid(row = 7,column = 6)

        club8Img = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\8_of_clubs.png')
        club8_size = (144,100)
        club8Img.thumbnail(club8_size)
        self.club8 = ImageTk.PhotoImage(club8Img)
        self.btn8c = tk.Button(self,image = self.club8,borderwidth = 0,command = self.click8c)
        self.btn8c.grid(row = 7,column = 7)

        club9Img = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\9_of_clubs.png')
        club9_size = (144,100)
        club9Img.thumbnail(club9_size)
        self.club9 = ImageTk.PhotoImage(club9Img)
        self.btn9c = tk.Button(self,image = self.club9,borderwidth = 0,command = self.click9c)
        self.btn9c.grid(row = 7,column = 8)

        clubTImg = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\10_of_clubs.png')
        clubT_size = (144,100)
        clubTImg.thumbnail(clubT_size)
        self.clubT = ImageTk.PhotoImage(clubTImg)
        self.btnTc = tk.Button(self,image = self.clubT,borderwidth = 0,command = self.clickTc)
        self.btnTc.grid(row = 7,column = 9)

        clubJImg = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\jack_of_clubs2.png')
        clubJ_size = (144,100)
        clubJImg.thumbnail(clubJ_size)
        self.clubJ = ImageTk.PhotoImage(clubJImg)
        self.btnJc = tk.Button(self,image = self.clubJ,borderwidth = 0,command = self.clickJc)
        self.btnJc.grid(row = 7,column = 10)

        clubQImg = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\queen_of_clubs2.png')
        clubQ_size = (144,100)
        clubQImg.thumbnail(clubQ_size)
        self.clubQ = ImageTk.PhotoImage(clubQImg)
        self.btnQc = tk.Button(self,image = self.clubQ,borderwidth = 0,command = self.clickQc)
        self.btnQc.grid(row = 7,column = 11)

        clubKImg = Image.open('C:\\Users\\xiuhu\\Downloads\\PNG-cards-1.3\\PNG-cards-1.3\\king_of_clubs2.png')
        clubK_size = (144,100)
        clubKImg.thumbnail(clubK_size)
        self.clubK = ImageTk.PhotoImage(clubKImg)
        self.btnKc = tk.Button(self,image = self.clubK,borderwidth = 0,command = self.clickKc)
        self.btnKc.grid(row = 7,column = 12)
        
        self.resetButton = tk.Button(self, text = 'reset', command = self.clickReset)
        self.resetButton.grid(row = 3, column = 6)
    def clickReset(self):
        global btnctr
        global leftWinRate
        global TieRate
        global rightWinRate
        global deck
        deck = StandardDeck()
        global leftHandStr
        leftHandStr = ''
        global rightHandStr
        rightHandStr = ''
        global boardStr
        boardStr = ''
        global leftWinRate
        leftWinRate = 0
        global rightWinRate
        rightWinRate = 0
        global TieRate
        TieRate = 0
        btnctr = 0
        TieRate = 0
        leftWinRate = 0
        rightWinRate = 0
        self.btnAs = tk.Button(self,image = self.spadeA,borderwidth = 0,command = self.clickAs)
        self.btnAs.grid(row = 4,column = 0)
        self.btn2s = tk.Button(self,image = self.spade2,borderwidth = 0,command = self.click2s)
        self.btn2s.grid(row = 4,column = 1)
        self.btn3s = tk.Button(self,image = self.spade3,borderwidth = 0,command = self.click3s)
        self.btn3s.grid(row = 4,column = 2)
        self.btn3s = tk.Button(self,image = self.spade3,borderwidth = 0,command = self.click3s)
        self.btn3s.grid(row = 4,column = 2)
        self.btn4s = tk.Button(self,image = self.spade4,borderwidth = 0,command = self.click4s)
        self.btn4s.grid(row = 4,column = 3)
        self.btn5s = tk.Button(self,image = self.spade5,borderwidth = 0,command = self.click5s)
        self.btn5s.grid(row = 4,column = 4)
        self.btn6s = tk.Button(self,image = self.spade6,borderwidth = 0,command = self.click6s)
        self.btn6s.grid(row = 4,column = 5)
        self.btn7s = tk.Button(self,image = self.spade7,borderwidth = 0,command = self.click7s)
        self.btn7s.grid(row = 4,column = 6)
        self.btn8s = tk.Button(self,image = self.spade8,borderwidth = 0,command = self.click8s)
        self.btn8s.grid(row = 4,column = 7)
        self.btn9s = tk.Button(self,image = self.spade9,borderwidth = 0,command = self.click9s)
        self.btn9s.grid(row = 4,column = 8)
        self.btnTs = tk.Button(self,image = self.spade10,borderwidth = 0,command = self.clickTs)
        self.btnTs.grid(row = 4,column = 9)
        self.btnJs = tk.Button(self,image = self.spadeJ,borderwidth = 0,command = self.clickJs)
        self.btnJs.grid(row = 4,column = 10)
        self.btnQs = tk.Button(self,image = self.spadeQ,borderwidth = 0,command = self.clickQs)
        self.btnQs.grid(row = 4,column = 11)
        self.btnKs = tk.Button(self,image = self.spadeK,borderwidth = 0,command = self.clickKs)
        self.btnKs.grid(row = 4,column = 12)
        self.btnAh = tk.Button(self,image = self.heartA,borderwidth = 0,command = self.clickAh)
        self.btnAh.grid(row = 5,column = 0)
        self.btn2h = tk.Button(self,image = self.heart2,borderwidth = 0,command = self.click2h)
        self.btn2h.grid(row = 5,column = 1)
        self.btn3h = tk.Button(self,image = self.heart3,borderwidth = 0,command = self.click3h)
        self.btn3h.grid(row = 5,column = 2)
        self.btn4h = tk.Button(self,image = self.heart4,borderwidth = 0,command = self.click4h)
        self.btn4h.grid(row = 5,column = 3)
        self.btn5h = tk.Button(self,image = self.heart5,borderwidth = 0,command = self.click5h)
        self.btn5h.grid(row = 5,column = 4)
        self.btn6h = tk.Button(self,image = self.heart6,borderwidth = 0,command = self.click6h)
        self.btn6h.grid(row = 5,column = 5)
        self.btn7h = tk.Button(self,image = self.heart7,borderwidth = 0,command = self.click7h)
        self.btn7h.grid(row = 5,column = 6)
        self.btn8h = tk.Button(self,image = self.heart8,borderwidth = 0,command = self.click8h)
        self.btn8h.grid(row = 5,column = 7)
        self.btn9h = tk.Button(self,image = self.heart9,borderwidth = 0,command = self.click9h)
        self.btn9h.grid(row = 5,column = 8)
        self.btnTh = tk.Button(self,image = self.heart10,borderwidth = 0,command = self.clickTh)
        self.btnTh.grid(row = 5,column = 9)
        self.btnJh = tk.Button(self,image = self.heartJ,borderwidth = 0,command = self.clickJh)
        self.btnJh.grid(row = 5,column = 10)
        self.btnQh = tk.Button(self,image = self.heartQ,borderwidth = 0,command = self.clickQh)
        self.btnQh.grid(row = 5,column = 11)
        self.btnKh = tk.Button(self,image = self.heartK,borderwidth = 0,command = self.clickKh)
        self.btnKh.grid(row = 5,column = 12)
        self.btnAd = tk.Button(self,image = self.diamondA,borderwidth = 0,command = self.clickAd)
        self.btnAd.grid(row = 6,column = 0)
        self.btn2d = tk.Button(self,image = self.diamond2,borderwidth = 0,command = self.click2d)
        self.btn2d.grid(row = 6,column = 1)
        self.btn3d = tk.Button(self,image = self.diamond3,borderwidth = 0,command = self.click3d)
        self.btn3d.grid(row = 6,column = 2)
        self.btn4d = tk.Button(self,image = self.diamond4,borderwidth = 0,command = self.click4d)
        self.btn4d.grid(row = 6,column = 3)
        self.btn5d = tk.Button(self,image = self.diamond5,borderwidth = 0,command = self.click5d)
        self.btn5d.grid(row = 6,column = 4)
        self.btn6d = tk.Button(self,image = self.diamond6,borderwidth = 0,command = self.click6d)
        self.btn6d.grid(row = 6,column = 5)
        self.btn7d = tk.Button(self,image = self.diamond7,borderwidth = 0,command = self.click7d)
        self.btn7d.grid(row = 6,column = 6)
        self.btn8d = tk.Button(self,image = self.diamond8,borderwidth = 0,command = self.click8d)
        self.btn8d.grid(row = 6,column = 7)
        self.btn9d = tk.Button(self,image = self.diamond9,borderwidth = 0,command = self.click9d)
        self.btn9d.grid(row = 6,column = 8)
        self.btnTd = tk.Button(self,image = self.diamondT,borderwidth = 0,command = self.clickTd)
        self.btnTd.grid(row = 6,column = 9)
        self.btnJd = tk.Button(self,image = self.diamondJ,borderwidth = 0,command = self.clickJd)
        self.btnJd.grid(row = 6,column = 10)
        self.btnQd = tk.Button(self,image = self.diamondQ,borderwidth = 0,command = self.clickQd)
        self.btnQd.grid(row = 6,column = 11)
        self.btnKd = tk.Button(self,image = self.diamondK,borderwidth = 0,command = self.clickKd)
        self.btnKd.grid(row = 6,column = 12)
        self.btnAc = tk.Button(self,image = self.clubA,borderwidth = 0,command = self.clickAc)
        self.btnAc.grid(row = 7,column = 0)
        self.btn2c = tk.Button(self,image = self.club2,borderwidth = 0,command = self.click2c)
        self.btn2c.grid(row = 7,column = 1)
        self.btn3c = tk.Button(self,image = self.club3,borderwidth = 0,command = self.click3c)
        self.btn3c.grid(row = 7,column = 2)
        self.btn4c = tk.Button(self,image = self.club4,borderwidth = 0,command = self.click4c)
        self.btn4c.grid(row = 7,column = 3)
        self.btn5c = tk.Button(self,image = self.club5,borderwidth = 0,command = self.click5c)
        self.btn5c.grid(row = 7,column = 4)
        self.btn6c = tk.Button(self,image = self.club6,borderwidth = 0,command = self.click6c)
        self.btn6c.grid(row = 7,column = 5)
        self.btn7c = tk.Button(self,image = self.club7,borderwidth = 0,command = self.click7c)
        self.btn7c.grid(row = 7,column = 6)
        self.btn8c = tk.Button(self,image = self.club8,borderwidth = 0,command = self.click8c)
        self.btn8c.grid(row = 7,column = 7)
        self.btn9c = tk.Button(self,image = self.club9,borderwidth = 0,command = self.click9c)
        self.btn9c.grid(row = 7,column = 8)
        self.btnTc = tk.Button(self,image = self.clubT,borderwidth = 0,command = self.clickTc)
        self.btnTc.grid(row = 7,column = 9)
        self.btnJc = tk.Button(self,image = self.clubJ,borderwidth = 0,command = self.clickJc)
        self.btnJc.grid(row = 7,column = 10)
        self.btnQc = tk.Button(self,image = self.clubQ,borderwidth = 0,command = self.clickQc)
        self.btnQc.grid(row = 7,column = 11)
        self.btnKc = tk.Button(self,image = self.clubK,borderwidth = 0,command = self.clickKc)
        self.btnKc.grid(row = 7,column = 12)
        self.leftHand1 = tk.Label(self,image = self.backSide)
        self.leftHand1.grid(row = 3,column = 1)
        self.leftHand2 = tk.Label(self,image = self.backSide)
        self.leftHand2.grid(row = 3,column = 2)
        self.rightHand1 = tk.Label(self,image = self.backSide)
        self.rightHand1.grid(row = 3,column = 10)
        self.rightHand2 = tk.Label(self,image = self.backSide)
        self.rightHand2.grid(row = 3,column = 11)
        self.flop1 = tk.Label(self,image = self.backSide)
        self.flop1.grid(row = 0,column = 4)
        self.flop2 = tk.Label(self,image = self.backSide)
        self.flop2.grid(row = 0,column = 5)
        self.flop3 = tk.Label(self,image = self.backSide)
        self.flop3.grid(row = 0,column = 6)
        self.turn = tk.Label(self,image = self.backSide)
        self.turn.grid(row = 0,column = 7)
        self.river = tk.Label(self,image = self.backSide)
        self.river.grid(row = 0,column = 8)
        self.showWinRate()
        
    def showWinRate(self):
        global leftWinRate
        global TieRate
        global rightWinRate
        self.lblLeftWinRate = tk.Label(self,text = 'Winrate:'+'%7.2f' %(leftWinRate)+'%')
        self.lblLeftWinRate.grid(row = 1,column = 1)
        self.lblLeftTieRate = tk.Label(self,text = 'Tierate:'+'%7.2f' %(TieRate)+'%')
        self.lblLeftTieRate.grid(row = 2,column = 1)
        self.lblRightWinRate = tk.Label(self,text = 'Winrate:'+'%7.2f' %(rightWinRate)+'%')
        self.lblRightWinRate.grid(row = 1,column = 10)
        self.lblRightTieRate = tk.Label(self,text = 'Tierate:'+'%7.2f' %(TieRate)+'%')
        self.lblRightTieRate.grid(row = 2,column = 10)
    def checkClickTime(self):
        evaluator = StandardEvaluator()
        assumeBoard = ''
        leftWinNumerator = 0
        rightWinNumerator = 0
        TieNumerator = 0
        global btnctr
        global leftWinRate
        global rightWinRate
        global TieRate
        '''if btnctr == 4:
            for i in list(combinations(deck,5)):
                assumeBoard = str(i[0]) + str(i[1]) + str(i[2]) + str(i[3]) + str(i[4])
                x = evaluator.evaluate_hand(parse_cards(leftHandStr),parse_cards(assumeBoard),)
                y = evaluator.evaluate_hand(parse_cards(rightHandStr),parse_cards(assumeBoard),)
                if x > y:
                    leftWinNumerator += 1
                elif x == y:
                    TieNumerator += 1
                elif x < y:
                    rightWinNumerator += 1
            leftWinRate = 100*leftWinNumerator/1712304
            rightWinRate = 100*rightWinNumerator/1712304
            TieRate = 100*TieNumerator/1712304
        self.showWinRate()'''  
        #上述部分為翻牌前計算勝率，因為組合數過多，計算時間太久(大約要跑10-15分鐘)，所以在最後決定移除這項功能
        if btnctr == 7:
            for i in list(combinations(deck,2)):
                assumeBoard = str(i[0]) + str(i[1])
                assumeBoard += boardStr
                x = evaluator.evaluate_hand(parse_cards(leftHandStr),parse_cards(assumeBoard),)
                y = evaluator.evaluate_hand(parse_cards(rightHandStr),parse_cards(assumeBoard),)
                if x > y:
                    leftWinNumerator += 1
                elif x == y:
                    TieNumerator += 1
                elif x < y:
                    rightWinNumerator += 1
            leftWinRate = 100*leftWinNumerator/990
            rightWinRate = 100*rightWinNumerator/990
            TieRate = 100*TieNumerator/990
        self.showWinRate()
        if btnctr == 8:
            for i in list(combinations(deck,1)):
                assumeBoard = str(i[0])
                assumeBoard += boardStr
                x = evaluator.evaluate_hand(parse_cards(leftHandStr),parse_cards(assumeBoard),)
                y = evaluator.evaluate_hand(parse_cards(rightHandStr),parse_cards(assumeBoard),)
                if x > y:
                    leftWinNumerator += 1
                elif x == y:
                    TieNumerator += 1
                elif x < y:
                    rightWinNumerator += 1
            leftWinRate = 100*leftWinNumerator/44
            rightWinRate = 100*rightWinNumerator/44
            TieRate = 100*TieNumerator/44
        self.showWinRate()
        if btnctr == 9:
            x = evaluator.evaluate_hand(parse_cards(leftHandStr),parse_cards(boardStr),)
            y = evaluator.evaluate_hand(parse_cards(rightHandStr),parse_cards(boardStr),)
            if x > y:
                leftWinRate = 100
                TieRate = 0
                rightWinRate = 0
            elif x < y:
                rightWinRate = 100
                TieRate = 0
                leftWinRate = 0
            elif x == y:
                TieRate = 100
                leftWinRate = 0
                rightWinRate = 0
        self.showWinRate()
    
    def clickAs(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.spadeA)
            self.leftHand1.grid(row = 3,column = 1)
            self.btnAs = tk.Label(self,image = self.backSide)
            self.btnAs.grid(row = 4,column = 0)
            deck.draw(parse_cards('As'))
            leftHandStr += 'As'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.spadeA)
            self.leftHand2.grid(row = 3,column = 2)
            self.btnAs = tk.Label(self,image = self.backSide)
            self.btnAs.grid(row = 4,column = 0)
            deck.draw(parse_cards('As'))
            leftHandStr += 'As'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.spadeA)
            self.rightHand1.grid(row = 3,column = 10)
            self.btnAs = tk.Label(self,image = self.backSide)
            self.btnAs.grid(row = 4,column = 0)
            deck.draw(parse_cards('As'))
            rightHandStr += 'As'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.spadeA)
            self.rightHand2.grid(row = 3,column = 11)
            self.btnAs = tk.Label(self,image = self.backSide)
            self.btnAs.grid(row = 4,column = 0)
            deck.draw(parse_cards('As'))
            rightHandStr += 'As'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.spadeA)
            self.flop1.grid(row = 0,column = 4)
            self.btnAs = tk.Label(self,image = self.backSide)
            self.btnAs.grid(row = 4,column = 0)
            deck.draw(parse_cards('As'))
            boardStr += 'As'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.spadeA)
            self.flop2.grid(row = 0,column = 5)
            self.btnAs = tk.Label(self,image = self.backSide)
            self.btnAs.grid(row = 4,column = 0)
            deck.draw(parse_cards('As'))
            boardStr += 'As'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.spadeA)
            self.flop3.grid(row = 0,column = 6)
            self.btnAs = tk.Label(self,image = self.backSide)
            self.btnAs.grid(row = 4,column = 0)
            deck.draw(parse_cards('As'))
            boardStr += 'As'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.spadeA)
            self.turn.grid(row = 0,column = 7)
            self.btnAs = tk.Label(self,image = self.backSide)
            self.btnAs.grid(row = 4,column = 0)
            deck.draw(parse_cards('As'))
            boardStr += 'As'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.spadeA)
            self.river.grid(row = 0,column = 8)
            self.btnAs = tk.Label(self,image = self.backSide)
            self.btnAs.grid(row = 4,column = 0)
            deck.draw(parse_cards('As'))
            boardStr += 'As'
            btnctr += 1
        self.checkClickTime()
    def click2s(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.spade2)
            self.leftHand1.grid(row = 3,column = 1)
            self.btn2s = tk.Label(self,image = self.backSide)
            self.btn2s.grid(row = 4,column = 1)
            deck.draw(parse_cards('2s'))
            leftHandStr += '2s'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.spade2)
            self.leftHand2.grid(row = 3,column = 2)
            self.btn2s = tk.Label(self,image = self.backSide)
            self.btn2s.grid(row = 4,column = 1)
            deck.draw(parse_cards('2s'))
            leftHandStr += '2s'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.spade2)
            self.rightHand1.grid(row = 3,column = 10)
            self.btn2s = tk.Label(self,image = self.backSide)
            self.btn2s.grid(row = 4,column = 1)
            deck.draw(parse_cards('2s'))
            rightHandStr += '2s'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.spade2)
            self.rightHand2.grid(row = 3,column = 11)
            self.btn2s = tk.Label(self,image = self.backSide)
            self.btn2s.grid(row = 4,column = 1)
            deck.draw(parse_cards('2s'))
            rightHandStr += '2s'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.spade2)
            self.flop1.grid(row = 0,column = 4)
            self.btn2s = tk.Label(self,image = self.backSide)
            self.btn2s.grid(row = 4,column = 1)
            deck.draw(parse_cards('2s'))
            boardStr += '2s'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.spade2)
            self.flop2.grid(row = 0,column = 5)
            self.btn2s = tk.Label(self,image = self.backSide)
            self.btn2s.grid(row = 4,column = 1)
            deck.draw(parse_cards('2s'))
            boardStr += '2s'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.spade2)
            self.flop3.grid(row = 0,column = 6)
            self.btn2s = tk.Label(self,image = self.backSide)
            self.btn2s.grid(row = 4,column = 1)
            deck.draw(parse_cards('2s'))
            boardStr += '2s'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.spade2)
            self.turn.grid(row = 0,column = 7)
            self.btn2s = tk.Label(self,image = self.backSide)
            self.btn2s.grid(row = 4,column = 1)
            deck.draw(parse_cards('2s'))
            boardStr += '2s'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.spade2)
            self.river.grid(row = 0,column = 8)
            self.btn2s = tk.Label(self,image = self.backSide)
            self.btn2s.grid(row = 4,column = 1)
            deck.draw(parse_cards('2s'))
            boardStr += '2s'
            btnctr += 1
        self.checkClickTime()
    def click3s(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.spade3)
            self.leftHand1.grid(row = 3,column = 1)
            self.btn3s = tk.Label(self,image = self.backSide)
            self.btn3s.grid(row = 4,column = 2)
            deck.draw(parse_cards('3s'))
            leftHandStr += '3s'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.spade3)
            self.leftHand2.grid(row = 3,column = 2)
            self.btn3s = tk.Label(self,image = self.backSide)
            self.btn3s.grid(row = 4,column = 2)
            deck.draw(parse_cards('3s'))
            leftHandStr += '3s'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.spade3)
            self.rightHand1.grid(row = 3,column = 10)
            self.btn3s = tk.Label(self,image = self.backSide)
            self.btn3s.grid(row = 4,column = 2)
            deck.draw(parse_cards('3s'))
            rightHandStr += '3s'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.spade3)
            self.rightHand2.grid(row = 3,column = 11)
            self.btn3s = tk.Label(self,image = self.backSide)
            self.btn3s.grid(row = 4,column = 2)
            deck.draw(parse_cards('3s'))
            rightHandStr += '3s'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.spade3)
            self.flop1.grid(row = 0,column = 4)
            self.btn3s = tk.Label(self,image = self.backSide)
            self.btn3s.grid(row = 4,column = 2)
            deck.draw(parse_cards('3s'))
            boardStr += '3s'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.spade3)
            self.flop2.grid(row = 0,column = 5)
            self.btn3s = tk.Label(self,image = self.backSide)
            self.btn3s.grid(row = 4,column = 2)
            deck.draw(parse_cards('3s'))
            boardStr += '3s'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.spade3)
            self.flop3.grid(row = 0,column = 6)
            self.btn3s = tk.Label(self,image = self.backSide)
            self.btn3s.grid(row = 4,column = 2)
            deck.draw(parse_cards('3s'))
            boardStr += '3s'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.spade3)
            self.turn.grid(row = 0,column = 7)
            self.btn3s = tk.Label(self,image = self.backSide)
            self.btn3s.grid(row = 4,column = 2)
            deck.draw(parse_cards('3s'))
            boardStr += '3s'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.spade3)
            self.river.grid(row = 0,column = 8)
            self.btn3s = tk.Label(self,image = self.backSide)
            self.btn3s.grid(row = 4,column = 2)
            deck.draw(parse_cards('3s'))
            boardStr += '3s'
            btnctr += 1
        self.checkClickTime()
    def click4s(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.spade4)
            self.leftHand1.grid(row = 3,column = 1)
            self.btn4s = tk.Label(self,image = self.backSide)
            self.btn4s.grid(row = 4,column = 3)
            deck.draw(parse_cards('4s'))
            leftHandStr += '4s'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.spade4)
            self.leftHand2.grid(row = 3,column = 2)
            self.btn4s = tk.Label(self,image = self.backSide)
            self.btn4s.grid(row = 4,column = 3)
            deck.draw(parse_cards('4s'))
            leftHandStr += '4s'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.spade4)
            self.rightHand1.grid(row = 3,column = 10)
            self.btn4s = tk.Label(self,image = self.backSide)
            self.btn4s.grid(row = 4,column = 3)
            deck.draw(parse_cards('4s'))
            rightHandStr += '4s'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.spade4)
            self.rightHand2.grid(row = 3,column = 11)
            self.btn4s = tk.Label(self,image = self.backSide)
            self.btn4s.grid(row = 4,column = 3)
            deck.draw(parse_cards('4s'))
            rightHandStr += '4s'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.spade4)
            self.flop1.grid(row = 0,column = 4)
            self.btn4s = tk.Label(self,image = self.backSide)
            self.btn4s.grid(row = 4,column = 3)
            deck.draw(parse_cards('4s'))
            boardStr += '4s'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.spade4)
            self.flop2.grid(row = 0,column = 5)
            self.btn4s = tk.Label(self,image = self.backSide)
            self.btn4s.grid(row = 4,column = 3)
            deck.draw(parse_cards('4s'))
            boardStr += '4s'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.spade4)
            self.flop3.grid(row = 0,column = 6)
            self.btn4s = tk.Label(self,image = self.backSide)
            self.btn4s.grid(row = 4,column = 3)
            deck.draw(parse_cards('4s'))
            boardStr += '4s'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.spade4)
            self.turn.grid(row = 0,column = 7)
            self.btn4s = tk.Label(self,image = self.backSide)
            self.btn4s.grid(row = 4,column = 3)
            deck.draw(parse_cards('4s'))
            boardStr += '4s'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.spade4)
            self.river.grid(row = 0,column = 8)
            self.btn4s = tk.Label(self,image = self.backSide)
            self.btn4s.grid(row = 4,column = 3)
            deck.draw(parse_cards('4s'))
            boardStr += '4s'
            btnctr += 1
        self.checkClickTime()
    def click5s(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.spade5)
            self.leftHand1.grid(row = 3,column = 1)
            self.btn5s = tk.Label(self,image = self.backSide)
            self.btn5s.grid(row = 4,column = 4)
            deck.draw(parse_cards('5s'))
            leftHandStr += '5s'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.spade5)
            self.leftHand2.grid(row = 3,column = 2)
            self.btn5s = tk.Label(self,image = self.backSide)
            self.btn5s.grid(row = 4,column = 4)
            deck.draw(parse_cards('5s'))
            leftHandStr += '5s'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.spade5)
            self.rightHand1.grid(row = 3,column = 10)
            self.btn5s = tk.Label(self,image = self.backSide)
            self.btn5s.grid(row = 4,column = 4)
            deck.draw(parse_cards('5s'))
            rightHandStr += '5s'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.spade5)
            self.rightHand2.grid(row = 3,column = 11)
            self.btn5s = tk.Label(self,image = self.backSide)
            self.btn5s.grid(row = 4,column = 4)
            deck.draw(parse_cards('5s'))
            rightHandStr += '5s'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.spade5)
            self.flop1.grid(row = 0,column = 4)
            self.btn5s = tk.Label(self,image = self.backSide)
            self.btn5s.grid(row = 4,column = 4)
            deck.draw(parse_cards('5s'))
            boardStr += '5s'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.spade5)
            self.flop2.grid(row = 0,column = 5)
            self.btn5s = tk.Label(self,image = self.backSide)
            self.btn5s.grid(row = 4,column = 4)
            deck.draw(parse_cards('5s'))
            boardStr += '5s'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.spade5)
            self.flop3.grid(row = 0,column = 6)
            self.btn5s = tk.Label(self,image = self.backSide)
            self.btn5s.grid(row = 4,column = 4)
            deck.draw(parse_cards('5s'))
            boardStr += '5s'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.spade5)
            self.turn.grid(row = 0,column = 7)
            self.btn5s = tk.Label(self,image = self.backSide)
            self.btn5s.grid(row = 4,column = 4)
            deck.draw(parse_cards('5s'))
            boardStr += '5s'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.spade5)
            self.river.grid(row = 0,column = 8)
            self.btn5s = tk.Label(self,image = self.backSide)
            self.btn5s.grid(row = 4,column = 4)
            deck.draw(parse_cards('5s'))
            boardStr += '5s'
            btnctr += 1
        self.checkClickTime()
    def click6s(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.spade6)
            self.leftHand1.grid(row = 3,column = 1)
            self.btn6s = tk.Label(self,image = self.backSide)
            self.btn6s.grid(row = 4,column = 5)
            deck.draw(parse_cards('6s'))
            leftHandStr += '6s'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.spade6)
            self.leftHand2.grid(row = 3,column = 2)
            self.btn6s = tk.Label(self,image = self.backSide)
            self.btn6s.grid(row = 4,column = 5)
            deck.draw(parse_cards('6s'))
            leftHandStr += '6s'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.spade6)
            self.rightHand1.grid(row = 3,column = 10)
            self.btn6s = tk.Label(self,image = self.backSide)
            self.btn6s.grid(row = 4,column = 5)
            deck.draw(parse_cards('6s'))
            rightHandStr += '6s'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.spade6)
            self.rightHand2.grid(row = 3,column = 11)
            self.btn6s = tk.Label(self,image = self.backSide)
            self.btn6s.grid(row = 4,column = 5)
            deck.draw(parse_cards('6s'))
            rightHandStr += '6s'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.spade6)
            self.flop1.grid(row = 0,column = 4)
            self.btn6s = tk.Label(self,image = self.backSide)
            self.btn6s.grid(row = 4,column = 5)
            deck.draw(parse_cards('6s'))
            boardStr += '6s'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.spade6)
            self.flop2.grid(row = 0,column = 5)
            self.btn6s = tk.Label(self,image = self.backSide)
            self.btn6s.grid(row = 4,column = 5)
            deck.draw(parse_cards('6s'))
            boardStr += '6s'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.spade6)
            self.flop3.grid(row = 0,column = 6)
            self.btn6s = tk.Label(self,image = self.backSide)
            self.btn6s.grid(row = 4,column = 5)
            deck.draw(parse_cards('6s'))
            boardStr += '6s'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.spade6)
            self.turn.grid(row = 0,column = 7)
            self.btn6s = tk.Label(self,image = self.backSide)
            self.btn6s.grid(row = 4,column = 5)
            deck.draw(parse_cards('6s'))
            boardStr += '6s'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.spade6)
            self.river.grid(row = 0,column = 8)
            self.btn6s = tk.Label(self,image = self.backSide)
            self.btn6s.grid(row = 4,column = 5)
            deck.draw(parse_cards('6s'))
            boardStr += '6s'
            btnctr += 1
        self.checkClickTime()
    def click7s(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.spade7)
            self.leftHand1.grid(row = 3,column = 1)
            self.btn7s = tk.Label(self,image = self.backSide)
            self.btn7s.grid(row = 4,column = 6)
            deck.draw(parse_cards('7s'))
            leftHandStr += '7s'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.spade7)
            self.leftHand2.grid(row = 3,column = 2)
            self.btn7s = tk.Label(self,image = self.backSide)
            self.btn7s.grid(row = 4,column = 6)
            deck.draw(parse_cards('7s'))
            leftHandStr += '7s'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.spade7)
            self.rightHand1.grid(row = 3,column = 10)
            self.btn7s = tk.Label(self,image = self.backSide)
            self.btn7s.grid(row = 4,column = 6)
            deck.draw(parse_cards('7s'))
            rightHandStr += '7s'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.spade7)
            self.rightHand2.grid(row = 3,column = 11)
            self.btn7s = tk.Label(self,image = self.backSide)
            self.btn7s.grid(row = 4,column = 6)
            deck.draw(parse_cards('7s'))
            rightHandStr += '7s'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.spade7)
            self.flop1.grid(row = 0,column = 4)
            self.btn7s = tk.Label(self,image = self.backSide)
            self.btn7s.grid(row = 4,column = 6)
            deck.draw(parse_cards('7s'))
            boardStr += '7s'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.spade7)
            self.flop2.grid(row = 0,column = 5)
            self.btn7s = tk.Label(self,image = self.backSide)
            self.btn7s.grid(row = 4,column = 6)
            deck.draw(parse_cards('7s'))
            boardStr += '7s'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.spade7)
            self.flop3.grid(row = 0,column = 6)
            self.btn7s = tk.Label(self,image = self.backSide)
            self.btn7s.grid(row = 4,column = 6)
            deck.draw(parse_cards('7s'))
            boardStr += '7s'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.spade7)
            self.turn.grid(row = 0,column = 7)
            self.btn7s = tk.Label(self,image = self.backSide)
            self.btn7s.grid(row = 4,column = 6)
            deck.draw(parse_cards('7s'))
            boardStr += '7s'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.spade7)
            self.river.grid(row = 0,column = 8)
            self.btn7s = tk.Label(self,image = self.backSide)
            self.btn7s.grid(row = 4,column = 6)
            deck.draw(parse_cards('7s'))
            boardStr += '7s'
            btnctr += 1
        self.checkClickTime()
    def click8s(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.spade8)
            self.leftHand1.grid(row = 3,column = 1)
            self.btn8s = tk.Label(self,image = self.backSide)
            self.btn8s.grid(row = 4,column = 7)
            deck.draw(parse_cards('8s'))
            leftHandStr += '8s'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.spade8)
            self.leftHand2.grid(row = 3,column = 2)
            self.btn8s = tk.Label(self,image = self.backSide)
            self.btn8s.grid(row = 4,column = 7)
            deck.draw(parse_cards('8s'))
            leftHandStr += '8s'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.spade8)
            self.rightHand1.grid(row = 3,column = 10)
            self.btn8s = tk.Label(self,image = self.backSide)
            self.btn8s.grid(row = 4,column = 7)
            deck.draw(parse_cards('8s'))
            rightHandStr += '8s'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.spade8)
            self.rightHand2.grid(row = 3,column = 11)
            self.btn8s = tk.Label(self,image = self.backSide)
            self.btn8s.grid(row = 4,column = 7)
            deck.draw(parse_cards('8s'))
            rightHandStr += '8s'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.spade8)
            self.flop1.grid(row = 0,column = 4)
            self.btn8s = tk.Label(self,image = self.backSide)
            self.btn8s.grid(row = 4,column = 7)
            deck.draw(parse_cards('8s'))
            boardStr += '8s'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.spade8)
            self.flop2.grid(row = 0,column = 5)
            self.btn8s = tk.Label(self,image = self.backSide)
            self.btn8s.grid(row = 4,column = 7)
            deck.draw(parse_cards('8s'))
            boardStr += '8s'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.spade8)
            self.flop3.grid(row = 0,column = 6)
            self.btn8s = tk.Label(self,image = self.backSide)
            self.btn8s.grid(row = 4,column = 7)
            deck.draw(parse_cards('8s'))
            boardStr += '8s'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.spade8)
            self.turn.grid(row = 0,column = 7)
            self.btn8s = tk.Label(self,image = self.backSide)
            self.btn8s.grid(row = 4,column = 7)
            deck.draw(parse_cards('8s'))
            boardStr += '8s'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.spade8)
            self.river.grid(row = 0,column = 8)
            self.btn8s = tk.Label(self,image = self.backSide)
            self.btn8s.grid(row = 4,column = 7)
            deck.draw(parse_cards('8s'))
            boardStr += '8s'
            btnctr += 1
        self.checkClickTime()
    def click9s(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.spade9)
            self.leftHand1.grid(row = 3,column = 1)
            self.btn9s = tk.Label(self,image = self.backSide)
            self.btn9s.grid(row = 4,column = 8)
            deck.draw(parse_cards('9s'))
            leftHandStr += '9s'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.spade9)
            self.leftHand2.grid(row = 3,column = 2)
            self.btn9s = tk.Label(self,image = self.backSide)
            self.btn9s.grid(row = 4,column = 8)
            deck.draw(parse_cards('9s'))
            leftHandStr += '9s'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.spade9)
            self.rightHand1.grid(row = 3,column = 10)
            self.btn9s = tk.Label(self,image = self.backSide)
            self.btn9s.grid(row = 4,column = 8)
            deck.draw(parse_cards('9s'))
            rightHandStr += '9s'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.spade9)
            self.rightHand2.grid(row = 3,column = 11)
            self.btn9s = tk.Label(self,image = self.backSide)
            self.btn9s.grid(row = 4,column = 8)
            deck.draw(parse_cards('9s'))
            rightHandStr += '9s'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.spade9)
            self.flop1.grid(row = 0,column = 4)
            self.btn9s = tk.Label(self,image = self.backSide)
            self.btn9s.grid(row = 4,column = 8)
            deck.draw(parse_cards('9s'))
            boardStr += '9s'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.spade9)
            self.flop2.grid(row = 0,column = 5)
            self.btn9s = tk.Label(self,image = self.backSide)
            self.btn9s.grid(row = 4,column = 8)
            deck.draw(parse_cards('9s'))
            boardStr += '9s'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.spade9)
            self.flop3.grid(row = 0,column = 6)
            self.btn9s = tk.Label(self,image = self.backSide)
            self.btn9s.grid(row = 4,column = 8)
            deck.draw(parse_cards('9s'))
            boardStr += '9s'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.spade9)
            self.turn.grid(row = 0,column = 7)
            self.btn9s = tk.Label(self,image = self.backSide)
            self.btn9s.grid(row = 4,column = 8)
            deck.draw(parse_cards('9s'))
            boardStr += '9s'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.spade9)
            self.river.grid(row = 0,column = 8)
            self.btn9s = tk.Label(self,image = self.backSide)
            self.btn9s.grid(row = 4,column = 8)
            deck.draw(parse_cards('9s'))
            boardStr += '9s'
            btnctr += 1
        self.checkClickTime()
    def clickTs(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.spade10)
            self.leftHand1.grid(row = 3,column = 1)
            self.btnTs = tk.Label(self,image = self.backSide)
            self.btnTs.grid(row = 4,column = 9)
            deck.draw(parse_cards('Ts'))
            leftHandStr += 'Ts'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.spade10)
            self.leftHand2.grid(row = 3,column = 2)
            self.btnTs = tk.Label(self,image = self.backSide)
            self.btnTs.grid(row = 4,column = 9)
            deck.draw(parse_cards('Ts'))
            leftHandStr += 'Ts'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.spade10)
            self.rightHand1.grid(row = 3,column = 10)
            self.btnTs = tk.Label(self,image = self.backSide)
            self.btnTs.grid(row = 4,column = 9)
            deck.draw(parse_cards('Ts'))
            rightHandStr += 'Ts'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.spade10)
            self.rightHand2.grid(row = 3,column = 11)
            self.btnTs = tk.Label(self,image = self.backSide)
            self.btnTs.grid(row = 4,column = 9)
            deck.draw(parse_cards('Ts'))
            rightHandStr += 'Ts'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.spade10)
            self.flop1.grid(row = 0,column = 4)
            self.btnTs = tk.Label(self,image = self.backSide)
            self.btnTs.grid(row = 4,column = 9)
            deck.draw(parse_cards('Ts'))
            boardStr += 'Ts'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.spade10)
            self.flop2.grid(row = 0,column = 5)
            self.btnTs = tk.Label(self,image = self.backSide)
            self.btnTs.grid(row = 4,column = 9)
            deck.draw(parse_cards('Ts'))
            boardStr += 'Ts'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.spade10)
            self.flop3.grid(row = 0,column = 6)
            self.btnTs = tk.Label(self,image = self.backSide)
            self.btnTs.grid(row = 4,column = 9)
            deck.draw(parse_cards('Ts'))
            boardStr += 'Ts'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.spade10)
            self.turn.grid(row = 0,column = 7)
            self.btnTs = tk.Label(self,image = self.backSide)
            self.btnTs.grid(row = 4,column = 9)
            deck.draw(parse_cards('Ts'))
            boardStr += 'Ts'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.spade10)
            self.river.grid(row = 0,column = 8)
            self.btnTs = tk.Label(self,image = self.backSide)
            self.btnTs.grid(row = 4,column = 9)
            deck.draw(parse_cards('Ts'))
            boardStr += 'Ts'
            btnctr += 1
        self.checkClickTime()
    def clickJs(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.spadeJ)
            self.leftHand1.grid(row = 3,column = 1)
            self.btnJs = tk.Label(self,image = self.backSide)
            self.btnJs.grid(row = 4,column = 10)
            deck.draw(parse_cards('Js'))
            leftHandStr += 'Js'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.spadeJ)
            self.leftHand2.grid(row = 3,column = 2)
            self.btnJs = tk.Label(self,image = self.backSide)
            self.btnJs.grid(row = 4,column = 10)
            deck.draw(parse_cards('Js'))
            leftHandStr += 'Js'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.spadeJ)
            self.rightHand1.grid(row = 3,column = 10)
            self.btnJs = tk.Label(self,image = self.backSide)
            self.btnJs.grid(row = 4,column = 10)
            deck.draw(parse_cards('Js'))
            rightHandStr += 'Js'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.spadeJ)
            self.rightHand2.grid(row = 3,column = 11)
            self.btnJs = tk.Label(self,image = self.backSide)
            self.btnJs.grid(row = 4,column = 10)
            deck.draw(parse_cards('Js'))
            rightHandStr += 'Js'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.spadeJ)
            self.flop1.grid(row = 0,column = 4)
            self.btnJs = tk.Label(self,image = self.backSide)
            self.btnJs.grid(row = 4,column = 10)
            deck.draw(parse_cards('Js'))
            boardStr += 'Js'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.spadeJ)
            self.flop2.grid(row = 0,column = 5)
            self.btnJs = tk.Label(self,image = self.backSide)
            self.btnJs.grid(row = 4,column = 10)
            deck.draw(parse_cards('Js'))
            boardStr += 'Js'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.spadeJ)
            self.flop3.grid(row = 0,column = 6)
            self.btnJs = tk.Label(self,image = self.backSide)
            self.btnJs.grid(row = 4,column = 10)
            deck.draw(parse_cards('Js'))
            boardStr += 'Js'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.spadeJ)
            self.turn.grid(row = 0,column = 7)
            self.btnJs = tk.Label(self,image = self.backSide)
            self.btnJs.grid(row = 4,column = 10)
            deck.draw(parse_cards('Js'))
            boardStr += 'Js'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.spadeJ)
            self.river.grid(row = 0,column = 8)
            self.btnJs = tk.Label(self,image = self.backSide)
            self.btnJs.grid(row = 4,column = 10)
            deck.draw(parse_cards('Js'))
            boardStr += 'Js'
            btnctr += 1
        self.checkClickTime()
    def clickQs(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.spadeQ)
            self.leftHand1.grid(row = 3,column = 1)
            self.btnQs = tk.Label(self,image = self.backSide)
            self.btnQs.grid(row = 4,column = 11)
            deck.draw(parse_cards('Qs'))
            leftHandStr += 'Qs'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.spadeQ)
            self.leftHand2.grid(row = 3,column = 2)
            self.btnQs = tk.Label(self,image = self.backSide)
            self.btnQs.grid(row = 4,column = 11)
            deck.draw(parse_cards('Qs'))
            leftHandStr += 'Qs'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.spadeQ)
            self.rightHand1.grid(row = 3,column = 11)
            self.btnQs = tk.Label(self,image = self.backSide)
            self.btnQs.grid(row = 4,column = 11)
            deck.draw(parse_cards('Qs'))
            rightHandStr += 'Qs'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.spadeQ)
            self.rightHand2.grid(row = 3,column = 11)
            self.btnQs = tk.Label(self,image = self.backSide)
            self.btnQs.grid(row = 4,column = 11)
            deck.draw(parse_cards('Qs'))
            rightHandStr += 'Qs'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.spadeQ)
            self.flop1.grid(row = 0,column = 4)
            self.btnQs = tk.Label(self,image = self.backSide)
            self.btnQs.grid(row = 4,column = 11)
            deck.draw(parse_cards('Qs'))
            boardStr += 'Qs'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.spadeQ)
            self.flop2.grid(row = 0,column = 5)
            self.btnQs = tk.Label(self,image = self.backSide)
            self.btnQs.grid(row = 4,column = 11)
            deck.draw(parse_cards('Qs'))
            boardStr += 'Qs'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.spadeQ)
            self.flop3.grid(row = 0,column = 6)
            self.btnQs = tk.Label(self,image = self.backSide)
            self.btnQs.grid(row = 4,column = 11)
            deck.draw(parse_cards('Qs'))
            boardStr += 'Qs'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.spadeQ)
            self.turn.grid(row = 0,column = 7)
            self.btnQs = tk.Label(self,image = self.backSide)
            self.btnQs.grid(row = 4,column = 11)
            deck.draw(parse_cards('Qs'))
            boardStr += 'Qs'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.spadeQ)
            self.river.grid(row = 0,column = 8)
            self.btnQs = tk.Label(self,image = self.backSide)
            self.btnQs.grid(row = 4,column = 11)
            deck.draw(parse_cards('Qs'))
            boardStr += 'Qs'
            btnctr += 1
        self.checkClickTime()
    def clickKs(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.spadeK)
            self.leftHand1.grid(row = 3,column = 1)
            self.btnKs = tk.Label(self,image = self.backSide)
            self.btnKs.grid(row = 4,column = 12)
            deck.draw(parse_cards('Ks'))
            leftHandStr += 'Ks'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.spadeK)
            self.leftHand2.grid(row = 3,column = 2)
            self.btnKs = tk.Label(self,image = self.backSide)
            self.btnKs.grid(row = 4,column = 12)
            deck.draw(parse_cards('Ks'))
            leftHandStr += 'Ks'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.spadeK)
            self.rightHand1.grid(row = 3,column = 12)
            self.btnKs = tk.Label(self,image = self.backSide)
            self.btnKs.grid(row = 4,column = 12)
            deck.draw(parse_cards('Ks'))
            rightHandStr += 'Ks'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.spadeK)
            self.rightHand2.grid(row = 3,column = 11)
            self.btnKs = tk.Label(self,image = self.backSide)
            self.btnKs.grid(row = 4,column = 12)
            deck.draw(parse_cards('Ks'))
            rightHandStr += 'Ks'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.spadeK)
            self.flop1.grid(row = 0,column = 4)
            self.btnKs = tk.Label(self,image = self.backSide)
            self.btnKs.grid(row = 4,column = 12)
            deck.draw(parse_cards('Ks'))
            boardStr += 'Ks'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.spadeK)
            self.flop2.grid(row = 0,column = 5)
            self.btnKs = tk.Label(self,image = self.backSide)
            self.btnKs.grid(row = 4,column = 12)
            deck.draw(parse_cards('Ks'))
            boardStr += 'Ks'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.spadeK)
            self.flop3.grid(row = 0,column = 6)
            self.btnKs = tk.Label(self,image = self.backSide)
            self.btnKs.grid(row = 4,column = 12)
            deck.draw(parse_cards('Ks'))
            boardStr += 'Ks'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.spadeK)
            self.turn.grid(row = 0,column = 7)
            self.btnKs = tk.Label(self,image = self.backSide)
            self.btnKs.grid(row = 4,column = 12)
            deck.draw(parse_cards('Ks'))
            boardStr += 'Ks'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.spadeK)
            self.river.grid(row = 0,column = 8)
            self.btnKs = tk.Label(self,image = self.backSide)
            self.btnKs.grid(row = 4,column = 12)
            deck.draw(parse_cards('Ks'))
            boardStr += 'Ks'
            btnctr += 1
        self.checkClickTime()   
    def clickAh(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.heartA)
            self.leftHand1.grid(row = 3,column = 1)
            self.btnAh = tk.Label(self,image = self.backSide)
            self.btnAh.grid(row = 5,column = 0)
            deck.draw(parse_cards('Ah'))
            leftHandStr += 'Ah'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.heartA)
            self.leftHand2.grid(row = 3,column = 2)
            self.btnAh = tk.Label(self,image = self.backSide)
            self.btnAh.grid(row = 5,column = 0)
            deck.draw(parse_cards('Ah'))
            leftHandStr += 'Ah'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.heartA)
            self.rightHand1.grid(row = 3,column = 10)
            self.btnAh = tk.Label(self,image = self.backSide)
            self.btnAh.grid(row = 5,column = 0)
            deck.draw(parse_cards('Ah'))
            rightHandStr += 'Ah'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.heartA)
            self.rightHand2.grid(row = 3,column = 11)
            self.btnAh = tk.Label(self,image = self.backSide)
            self.btnAh.grid(row = 5,column = 0)
            deck.draw(parse_cards('Ah'))
            rightHandStr += 'Ah'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.heartA)
            self.flop1.grid(row = 0,column = 4)
            self.btnAh = tk.Label(self,image = self.backSide)
            self.btnAh.grid(row = 5,column = 0)
            deck.draw(parse_cards('Ah'))
            boardStr += 'Ah'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.heartA)
            self.flop2.grid(row = 0,column = 5)
            self.btnAh = tk.Label(self,image = self.backSide)
            self.btnAh.grid(row = 5,column = 0)
            deck.draw(parse_cards('Ah'))
            boardStr += 'Ah'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.heartA)
            self.flop3.grid(row = 0,column = 6)
            self.btnAh = tk.Label(self,image = self.backSide)
            self.btnAh.grid(row = 5,column = 0)
            deck.draw(parse_cards('Ah'))
            boardStr += 'Ah'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.heartA)
            self.turn.grid(row = 0,column = 7)
            self.btnAh = tk.Label(self,image = self.backSide)
            self.btnAh.grid(row = 5,column = 0)
            deck.draw(parse_cards('Ah'))
            boardStr += 'Ah'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.heartA)
            self.river.grid(row = 0,column = 8)
            self.btnAh = tk.Label(self,image = self.backSide)
            self.btnAh.grid(row = 5,column = 0)
            deck.draw(parse_cards('Ah'))
            boardStr += 'Ah'
            btnctr += 1
        self.checkClickTime()
    def click2h(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.heart2)
            self.leftHand1.grid(row = 3,column = 1)
            self.btn2h = tk.Label(self,image = self.backSide)
            self.btn2h.grid(row = 5,column = 1)
            deck.draw(parse_cards('2h'))
            leftHandStr += '2h'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.heart2)
            self.leftHand2.grid(row = 3,column = 2)
            self.btn2h = tk.Label(self,image = self.backSide)
            self.btn2h.grid(row = 5,column = 1)
            deck.draw(parse_cards('2h'))
            leftHandStr += '2h'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.heart2)
            self.rightHand1.grid(row = 3,column = 10)
            self.btn2h = tk.Label(self,image = self.backSide)
            self.btn2h.grid(row = 5,column = 1)
            deck.draw(parse_cards('2h'))
            rightHandStr += '2h'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.heart2)
            self.rightHand2.grid(row = 3,column = 11)
            self.btn2h = tk.Label(self,image = self.backSide)
            self.btn2h.grid(row = 5,column = 1)
            deck.draw(parse_cards('2h'))
            rightHandStr += '2h'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.heart2)
            self.flop1.grid(row = 0,column = 4)
            self.btn2h = tk.Label(self,image = self.backSide)
            self.btn2h.grid(row = 5,column = 1)
            deck.draw(parse_cards('2h'))
            boardStr += '2h'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.heart2)
            self.flop2.grid(row = 0,column = 5)
            self.btn2h = tk.Label(self,image = self.backSide)
            self.btn2h.grid(row = 5,column = 1)
            deck.draw(parse_cards('2h'))
            boardStr += '2h'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.heart2)
            self.flop3.grid(row = 0,column = 6)
            self.btn2h = tk.Label(self,image = self.backSide)
            self.btn2h.grid(row = 5,column = 1)
            deck.draw(parse_cards('2h'))
            boardStr += '2h'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.heart2)
            self.turn.grid(row = 0,column = 7)
            self.btn2h = tk.Label(self,image = self.backSide)
            self.btn2h.grid(row = 5,column = 1)
            deck.draw(parse_cards('2h'))
            boardStr += '2h'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.heart2)
            self.river.grid(row = 0,column = 8)
            self.btn2h = tk.Label(self,image = self.backSide)
            self.btn2h.grid(row = 5,column = 1)
            deck.draw(parse_cards('2h'))
            boardStr += '2h'
            btnctr += 1
        self.checkClickTime()
    def click3h(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.heart3)
            self.leftHand1.grid(row = 3,column = 1)
            self.btn3h = tk.Label(self,image = self.backSide)
            self.btn3h.grid(row = 5,column = 2)
            deck.draw(parse_cards('3h'))
            leftHandStr += '3h'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.heart3)
            self.leftHand2.grid(row = 3,column = 2)
            self.btn3h = tk.Label(self,image = self.backSide)
            self.btn3h.grid(row = 5,column = 2)
            deck.draw(parse_cards('3h'))
            leftHandStr += '3h'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.heart3)
            self.rightHand1.grid(row = 3,column = 10)
            self.btn3h = tk.Label(self,image = self.backSide)
            self.btn3h.grid(row = 5,column = 2)
            deck.draw(parse_cards('3h'))
            rightHandStr += '3h'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.heart3)
            self.rightHand2.grid(row = 3,column = 11)
            self.btn3h = tk.Label(self,image = self.backSide)
            self.btn3h.grid(row = 5,column = 2)
            deck.draw(parse_cards('3h'))
            rightHandStr += '3h'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.heart3)
            self.flop1.grid(row = 0,column = 4)
            self.btn3h = tk.Label(self,image = self.backSide)
            self.btn3h.grid(row = 5,column = 2)
            deck.draw(parse_cards('3h'))
            boardStr += '3h'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.heart3)
            self.flop2.grid(row = 0,column = 5)
            self.btn3h = tk.Label(self,image = self.backSide)
            self.btn3h.grid(row = 5,column = 2)
            deck.draw(parse_cards('3h'))
            boardStr += '3h'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.heart3)
            self.flop3.grid(row = 0,column = 6)
            self.btn3h = tk.Label(self,image = self.backSide)
            self.btn3h.grid(row = 5,column = 2)
            deck.draw(parse_cards('3h'))
            boardStr += '3h'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.heart3)
            self.turn.grid(row = 0,column = 7)
            self.btn3h = tk.Label(self,image = self.backSide)
            self.btn3h.grid(row = 5,column = 2)
            deck.draw(parse_cards('3h'))
            boardStr += '3h'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.heart3)
            self.river.grid(row = 0,column = 8)
            self.btn3h = tk.Label(self,image = self.backSide)
            self.btn3h.grid(row = 5,column = 2)
            deck.draw(parse_cards('3h'))
            boardStr += '3h'
            btnctr += 1
        self.checkClickTime()
    def click4h(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.heart4)
            self.leftHand1.grid(row = 3,column = 1)
            self.btn4h = tk.Label(self,image = self.backSide)
            self.btn4h.grid(row = 5,column = 3)
            deck.draw(parse_cards('4h'))
            leftHandStr += '4h'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.heart4)
            self.leftHand2.grid(row = 3,column = 2)
            self.btn4h = tk.Label(self,image = self.backSide)
            self.btn4h.grid(row = 5,column = 3)
            deck.draw(parse_cards('4h'))
            leftHandStr += '4h'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.heart4)
            self.rightHand1.grid(row = 3,column = 10)
            self.btn4h = tk.Label(self,image = self.backSide)
            self.btn4h.grid(row = 5,column = 3)
            deck.draw(parse_cards('4h'))
            rightHandStr += '4h'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.heart4)
            self.rightHand2.grid(row = 3,column = 11)
            self.btn4h = tk.Label(self,image = self.backSide)
            self.btn4h.grid(row = 5,column = 3)
            deck.draw(parse_cards('4h'))
            rightHandStr += '4h'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.heart4)
            self.flop1.grid(row = 0,column = 4)
            self.btn4h = tk.Label(self,image = self.backSide)
            self.btn4h.grid(row = 5,column = 3)
            deck.draw(parse_cards('4h'))
            boardStr += '4h'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.heart4)
            self.flop2.grid(row = 0,column = 5)
            self.btn4h = tk.Label(self,image = self.backSide)
            self.btn4h.grid(row = 5,column = 3)
            deck.draw(parse_cards('4h'))
            boardStr += '4h'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.heart4)
            self.flop3.grid(row = 0,column = 6)
            self.btn4h = tk.Label(self,image = self.backSide)
            self.btn4h.grid(row = 5,column = 3)
            deck.draw(parse_cards('4h'))
            boardStr += '4h'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.heart4)
            self.turn.grid(row = 0,column = 7)
            self.btn4h = tk.Label(self,image = self.backSide)
            self.btn4h.grid(row = 5,column = 3)
            deck.draw(parse_cards('4h'))
            boardStr += '4h'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.heart4)
            self.river.grid(row = 0,column = 8)
            self.btn4h = tk.Label(self,image = self.backSide)
            self.btn4h.grid(row = 5,column = 3)
            deck.draw(parse_cards('4h'))
            boardStr += '4h'
            btnctr += 1
        self.checkClickTime()
    def click5h(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.heart5)
            self.leftHand1.grid(row = 3,column = 1)
            self.btn5h = tk.Label(self,image = self.backSide)
            self.btn5h.grid(row = 5,column = 4)
            deck.draw(parse_cards('5h'))
            leftHandStr += '5h'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.heart5)
            self.leftHand2.grid(row = 3,column = 2)
            self.btn5h = tk.Label(self,image = self.backSide)
            self.btn5h.grid(row = 5,column = 4)
            deck.draw(parse_cards('5h'))
            leftHandStr += '5h'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.heart5)
            self.rightHand1.grid(row = 3,column = 10)
            self.btn5h = tk.Label(self,image = self.backSide)
            self.btn5h.grid(row = 5,column = 4)
            deck.draw(parse_cards('5h'))
            rightHandStr += '5h'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.heart5)
            self.rightHand2.grid(row = 3,column = 11)
            self.btn5h = tk.Label(self,image = self.backSide)
            self.btn5h.grid(row = 5,column = 4)
            deck.draw(parse_cards('5h'))
            rightHandStr += '5h'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.heart5)
            self.flop1.grid(row = 0,column = 4)
            self.btn5h = tk.Label(self,image = self.backSide)
            self.btn5h.grid(row = 5,column = 4)
            deck.draw(parse_cards('5h'))
            boardStr += '5h'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.heart5)
            self.flop2.grid(row = 0,column = 5)
            self.btn5h = tk.Label(self,image = self.backSide)
            self.btn5h.grid(row = 5,column = 4)
            deck.draw(parse_cards('5h'))
            boardStr += '5h'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.heart5)
            self.flop3.grid(row = 0,column = 6)
            self.btn5h = tk.Label(self,image = self.backSide)
            self.btn5h.grid(row = 5,column = 4)
            deck.draw(parse_cards('5h'))
            boardStr += '5h'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.heart5)
            self.turn.grid(row = 0,column = 7)
            self.btn5h = tk.Label(self,image = self.backSide)
            self.btn5h.grid(row = 5,column = 4)
            deck.draw(parse_cards('5h'))
            boardStr += '5h'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.heart5)
            self.river.grid(row = 0,column = 8)
            self.btn5h = tk.Label(self,image = self.backSide)
            self.btn5h.grid(row = 5,column = 4)
            deck.draw(parse_cards('5h'))
            boardStr += '5h'
            btnctr += 1
        self.checkClickTime()
    def click6h(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.heart6)
            self.leftHand1.grid(row = 3,column = 1)
            self.btn6h = tk.Label(self,image = self.backSide)
            self.btn6h.grid(row = 5,column = 5)
            deck.draw(parse_cards('6h'))
            leftHandStr += '6h'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.heart6)
            self.leftHand2.grid(row = 3,column = 2)
            self.btn6h = tk.Label(self,image = self.backSide)
            self.btn6h.grid(row = 5,column = 5)
            deck.draw(parse_cards('6h'))
            leftHandStr += '6h'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.heart6)
            self.rightHand1.grid(row = 3,column = 10)
            self.btn6h = tk.Label(self,image = self.backSide)
            self.btn6h.grid(row = 5,column = 5)
            deck.draw(parse_cards('6h'))
            rightHandStr += '6h'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.heart6)
            self.rightHand2.grid(row = 3,column = 11)
            self.btn6h = tk.Label(self,image = self.backSide)
            self.btn6h.grid(row = 5,column = 5)
            deck.draw(parse_cards('6h'))
            rightHandStr += '6h'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.heart6)
            self.flop1.grid(row = 0,column = 4)
            self.btn6h = tk.Label(self,image = self.backSide)
            self.btn6h.grid(row = 5,column = 5)
            deck.draw(parse_cards('6h'))
            boardStr += '6h'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.heart6)
            self.flop2.grid(row = 0,column = 5)
            self.btn6h = tk.Label(self,image = self.backSide)
            self.btn6h.grid(row = 5,column = 5)
            deck.draw(parse_cards('6h'))
            boardStr += '6h'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.heart6)
            self.flop3.grid(row = 0,column = 6)
            self.btn6h = tk.Label(self,image = self.backSide)
            self.btn6h.grid(row = 5,column = 5)
            deck.draw(parse_cards('6h'))
            boardStr += '6h'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.heart6)
            self.turn.grid(row = 0,column = 7)
            self.btn6h = tk.Label(self,image = self.backSide)
            self.btn6h.grid(row = 5,column = 5)
            deck.draw(parse_cards('6h'))
            boardStr += '6h'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.heart6)
            self.river.grid(row = 0,column = 8)
            self.btn6h = tk.Label(self,image = self.backSide)
            self.btn6h.grid(row = 5,column = 5)
            deck.draw(parse_cards('6h'))
            boardStr += '6h'
            btnctr += 1
        self.checkClickTime() 
    def click7h(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.heart7)
            self.leftHand1.grid(row = 3,column = 1)
            self.btn7h = tk.Label(self,image = self.backSide)
            self.btn7h.grid(row = 5,column = 6)
            deck.draw(parse_cards('7h'))
            leftHandStr += '7h'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.heart7)
            self.leftHand2.grid(row = 3,column = 2)
            self.btn7h = tk.Label(self,image = self.backSide)
            self.btn7h.grid(row = 5,column = 6)
            deck.draw(parse_cards('7h'))
            leftHandStr += '7h'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.heart7)
            self.rightHand1.grid(row = 3,column = 10)
            self.btn7h = tk.Label(self,image = self.backSide)
            self.btn7h.grid(row = 5,column = 6)
            deck.draw(parse_cards('7h'))
            rightHandStr += '7h'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.heart7)
            self.rightHand2.grid(row = 3,column = 11)
            self.btn7h = tk.Label(self,image = self.backSide)
            self.btn7h.grid(row = 5,column = 6)
            deck.draw(parse_cards('7h'))
            rightHandStr += '7h'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.heart7)
            self.flop1.grid(row = 0,column = 4)
            self.btn7h = tk.Label(self,image = self.backSide)
            self.btn7h.grid(row = 5,column = 6)
            deck.draw(parse_cards('7h'))
            boardStr += '7h'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.heart7)
            self.flop2.grid(row = 0,column = 5)
            self.btn7h = tk.Label(self,image = self.backSide)
            self.btn7h.grid(row = 5,column = 6)
            deck.draw(parse_cards('7h'))
            boardStr += '7h'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.heart7)
            self.flop3.grid(row = 0,column = 6)
            self.btn7h = tk.Label(self,image = self.backSide)
            self.btn7h.grid(row = 5,column = 6)
            deck.draw(parse_cards('7h'))
            boardStr += '7h'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.heart7)
            self.turn.grid(row = 0,column = 7)
            self.btn7h = tk.Label(self,image = self.backSide)
            self.btn7h.grid(row = 5,column = 6)
            deck.draw(parse_cards('7h'))
            boardStr += '7h'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.heart7)
            self.river.grid(row = 0,column = 8)
            self.btn7h = tk.Label(self,image = self.backSide)
            self.btn7h.grid(row = 5,column = 6)
            deck.draw(parse_cards('7h'))
            boardStr += '7h'
            btnctr += 1
        self.checkClickTime()
    def click8h(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.heart8)
            self.leftHand1.grid(row = 3,column = 1)
            self.btn8h = tk.Label(self,image = self.backSide)
            self.btn8h.grid(row = 5,column = 7)
            deck.draw(parse_cards('8h'))
            leftHandStr += '8h'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.heart8)
            self.leftHand2.grid(row = 3,column = 2)
            self.btn8h = tk.Label(self,image = self.backSide)
            self.btn8h.grid(row = 5,column = 7)
            deck.draw(parse_cards('8h'))
            leftHandStr += '8h'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.heart8)
            self.rightHand1.grid(row = 3,column = 10)
            self.btn8h = tk.Label(self,image = self.backSide)
            self.btn8h.grid(row = 5,column = 7)
            deck.draw(parse_cards('8h'))
            rightHandStr += '8h'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.heart8)
            self.rightHand2.grid(row = 3,column = 11)
            self.btn8h = tk.Label(self,image = self.backSide)
            self.btn8h.grid(row = 5,column = 7)
            deck.draw(parse_cards('8h'))
            rightHandStr += '8h'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.heart8)
            self.flop1.grid(row = 0,column = 4)
            self.btn8h = tk.Label(self,image = self.backSide)
            self.btn8h.grid(row = 5,column = 7)
            deck.draw(parse_cards('8h'))
            boardStr += '8h'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.heart8)
            self.flop2.grid(row = 0,column = 5)
            self.btn8h = tk.Label(self,image = self.backSide)
            self.btn8h.grid(row = 5,column = 7)
            deck.draw(parse_cards('8h'))
            boardStr += '8h'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.heart8)
            self.flop3.grid(row = 0,column = 6)
            self.btn8h = tk.Label(self,image = self.backSide)
            self.btn8h.grid(row = 5,column = 7)
            deck.draw(parse_cards('8h'))
            boardStr += '8h'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.heart8)
            self.turn.grid(row = 0,column = 7)
            self.btn8h = tk.Label(self,image = self.backSide)
            self.btn8h.grid(row = 5,column = 7)
            deck.draw(parse_cards('8h'))
            boardStr += '8h'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.heart8)
            self.river.grid(row = 0,column = 8)
            self.btn8h = tk.Label(self,image = self.backSide)
            self.btn8h.grid(row = 5,column = 7)
            deck.draw(parse_cards('8h'))
            boardStr += '8h'
            btnctr += 1
        self.checkClickTime()
    def click9h(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.heart9)
            self.leftHand1.grid(row = 3,column = 1)
            self.btn9h = tk.Label(self,image = self.backSide)
            self.btn9h.grid(row = 5,column = 8)
            deck.draw(parse_cards('9h'))
            leftHandStr += '9h'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.heart9)
            self.leftHand2.grid(row = 3,column = 2)
            self.btn9h = tk.Label(self,image = self.backSide)
            self.btn9h.grid(row = 5,column = 8)
            deck.draw(parse_cards('9h'))
            leftHandStr += '9h'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.heart9)
            self.rightHand1.grid(row = 3,column = 10)
            self.btn9h = tk.Label(self,image = self.backSide)
            self.btn9h.grid(row = 5,column = 8)
            deck.draw(parse_cards('9h'))
            rightHandStr += '9h'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.heart9)
            self.rightHand2.grid(row = 3,column = 11)
            self.btn9h = tk.Label(self,image = self.backSide)
            self.btn9h.grid(row = 5,column = 8)
            deck.draw(parse_cards('9h'))
            rightHandStr += '9h'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.heart9)
            self.flop1.grid(row = 0,column = 4)
            self.btn9h = tk.Label(self,image = self.backSide)
            self.btn9h.grid(row = 5,column = 8)
            deck.draw(parse_cards('9h'))
            boardStr += '9h'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.heart9)
            self.flop2.grid(row = 0,column = 5)
            self.btn9h = tk.Label(self,image = self.backSide)
            self.btn9h.grid(row = 5,column = 8)
            deck.draw(parse_cards('9h'))
            boardStr += '9h'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.heart9)
            self.flop3.grid(row = 0,column = 6)
            self.btn9h = tk.Label(self,image = self.backSide)
            self.btn9h.grid(row = 5,column = 8)
            deck.draw(parse_cards('9h'))
            boardStr += '9h'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.heart9)
            self.turn.grid(row = 0,column = 7)
            self.btn9h = tk.Label(self,image = self.backSide)
            self.btn9h.grid(row = 5,column = 8)
            deck.draw(parse_cards('9h'))
            boardStr += '9h'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.heart9)
            self.river.grid(row = 0,column = 8)
            self.btn9h = tk.Label(self,image = self.backSide)
            self.btn9h.grid(row = 5,column = 8)
            deck.draw(parse_cards('9h'))
            boardStr += '9h'
            btnctr += 1
        self.checkClickTime()
    def clickTh(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.heart10)
            self.leftHand1.grid(row = 3,column = 1)
            self.btnTh = tk.Label(self,image = self.backSide)
            self.btnTh.grid(row = 5,column = 9)
            deck.draw(parse_cards('Th'))
            leftHandStr += 'Th'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.heart10)
            self.leftHand2.grid(row = 3,column = 2)
            self.btnTh = tk.Label(self,image = self.backSide)
            self.btnTh.grid(row = 5,column = 9)
            deck.draw(parse_cards('Th'))
            leftHandStr += 'Th'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.heart10)
            self.rightHand1.grid(row = 3,column = 10)
            self.btnTh = tk.Label(self,image = self.backSide)
            self.btnTh.grid(row = 5,column = 9)
            deck.draw(parse_cards('Th'))
            rightHandStr += 'Th'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.heart10)
            self.rightHand2.grid(row = 3,column = 11)
            self.btnTh = tk.Label(self,image = self.backSide)
            self.btnTh.grid(row = 5,column = 9)
            deck.draw(parse_cards('Th'))
            rightHandStr += 'Th'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.heart10)
            self.flop1.grid(row = 0,column = 4)
            self.btnTh = tk.Label(self,image = self.backSide)
            self.btnTh.grid(row = 5,column = 9)
            deck.draw(parse_cards('Th'))
            boardStr += 'Th'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.heart10)
            self.flop2.grid(row = 0,column = 5)
            self.btnTh = tk.Label(self,image = self.backSide)
            self.btnTh.grid(row = 5,column = 9)
            deck.draw(parse_cards('Th'))
            boardStr += 'Th'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.heart10)
            self.flop3.grid(row = 0,column = 6)
            self.btnTh = tk.Label(self,image = self.backSide)
            self.btnTh.grid(row = 5,column = 9)
            deck.draw(parse_cards('Th'))
            boardStr += 'Th'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.heart10)
            self.turn.grid(row = 0,column = 7)
            self.btnTh = tk.Label(self,image = self.backSide)
            self.btnTh.grid(row = 5,column = 9)
            deck.draw(parse_cards('Th'))
            boardStr += 'Th'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.heart10)
            self.river.grid(row = 0,column = 8)
            self.btnTh = tk.Label(self,image = self.backSide)
            self.btnTh.grid(row = 5,column = 9)
            deck.draw(parse_cards('Th'))
            boardStr += 'Th'
            btnctr += 1
        self.checkClickTime()
    def clickJh(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.heartJ)
            self.leftHand1.grid(row = 3,column = 1)
            self.btnJh = tk.Label(self,image = self.backSide)
            self.btnJh.grid(row = 5,column = 10)
            deck.draw(parse_cards('Jh'))
            leftHandStr += 'Jh'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.heartJ)
            self.leftHand2.grid(row = 3,column = 2)
            self.btnJh = tk.Label(self,image = self.backSide)
            self.btnJh.grid(row = 5,column = 10)
            deck.draw(parse_cards('Jh'))
            leftHandStr += 'Jh'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.heartJ)
            self.rightHand1.grid(row = 3,column = 10)
            self.btnJh = tk.Label(self,image = self.backSide)
            self.btnJh.grid(row = 5,column = 10)
            deck.draw(parse_cards('Jh'))
            rightHandStr += 'Jh'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.heartJ)
            self.rightHand2.grid(row = 3,column = 11)
            self.btnJh = tk.Label(self,image = self.backSide)
            self.btnJh.grid(row = 5,column = 10)
            deck.draw(parse_cards('Jh'))
            rightHandStr += 'Jh'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.heartJ)
            self.flop1.grid(row = 0,column = 4)
            self.btnJh = tk.Label(self,image = self.backSide)
            self.btnJh.grid(row = 5,column = 10)
            deck.draw(parse_cards('Jh'))
            boardStr += 'Jh'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.heartJ)
            self.flop2.grid(row = 0,column = 5)
            self.btnJh = tk.Label(self,image = self.backSide)
            self.btnJh.grid(row = 5,column = 10)
            deck.draw(parse_cards('Jh'))
            boardStr += 'Jh'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.heartJ)
            self.flop3.grid(row = 0,column = 6)
            self.btnJh = tk.Label(self,image = self.backSide)
            self.btnJh.grid(row = 5,column = 10)
            deck.draw(parse_cards('Jh'))
            boardStr += 'Jh'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.heartJ)
            self.turn.grid(row = 0,column = 7)
            self.btnJh = tk.Label(self,image = self.backSide)
            self.btnJh.grid(row = 5,column = 10)
            deck.draw(parse_cards('Jh'))
            boardStr += 'Jh'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.heartJ)
            self.river.grid(row = 0,column = 8)
            self.btnJh = tk.Label(self,image = self.backSide)
            self.btnJh.grid(row = 5,column = 10)
            deck.draw(parse_cards('Jh'))
            boardStr += 'Jh'
            btnctr += 1
        self.checkClickTime()
    def clickQh(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.heartQ)
            self.leftHand1.grid(row = 3,column = 1)
            self.btnQh = tk.Label(self,image = self.backSide)
            self.btnQh.grid(row = 5,column = 11)
            deck.draw(parse_cards('Qh'))
            leftHandStr += 'Qh'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.heartQ)
            self.leftHand2.grid(row = 3,column = 2)
            self.btnQh = tk.Label(self,image = self.backSide)
            self.btnQh.grid(row = 5,column = 11)
            deck.draw(parse_cards('Qh'))
            leftHandStr += 'Qh'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.heartQ)
            self.rightHand1.grid(row = 3,column = 10)
            self.btnQh = tk.Label(self,image = self.backSide)
            self.btnQh.grid(row = 5,column = 11)
            deck.draw(parse_cards('Qh'))
            rightHandStr += 'Qh'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.heartQ)
            self.rightHand2.grid(row = 3,column = 11)
            self.btnQh = tk.Label(self,image = self.backSide)
            self.btnQh.grid(row = 5,column = 11)
            deck.draw(parse_cards('Qh'))
            rightHandStr += 'Qh'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.heartQ)
            self.flop1.grid(row = 0,column = 4)
            self.btnQh = tk.Label(self,image = self.backSide)
            self.btnQh.grid(row = 5,column = 11)
            deck.draw(parse_cards('Qh'))
            boardStr += 'Qh'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.heartQ)
            self.flop2.grid(row = 0,column = 5)
            self.btnQh = tk.Label(self,image = self.backSide)
            self.btnQh.grid(row = 5,column = 11)
            deck.draw(parse_cards('Qh'))
            boardStr += 'Qh'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.heartQ)
            self.flop3.grid(row = 0,column = 6)
            self.btnQh = tk.Label(self,image = self.backSide)
            self.btnQh.grid(row = 5,column = 11)
            deck.draw(parse_cards('Qh'))
            boardStr += 'Qh'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.heartQ)
            self.turn.grid(row = 0,column = 7)
            self.btnQh = tk.Label(self,image = self.backSide)
            self.btnQh.grid(row = 5,column = 11)
            deck.draw(parse_cards('Qh'))
            boardStr += 'Qh'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.heartQ)
            self.river.grid(row = 0,column = 8)
            self.btnQh = tk.Label(self,image = self.backSide)
            self.btnQh.grid(row = 5,column = 11)
            deck.draw(parse_cards('Qh'))
            boardStr += 'Qh'
            btnctr += 1
        self.checkClickTime()
    def clickKh(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.heartK)
            self.leftHand1.grid(row = 3,column = 1)
            self.btnKh = tk.Label(self,image = self.backSide)
            self.btnKh.grid(row = 5,column = 12)
            deck.draw(parse_cards('Kh'))
            leftHandStr += 'Kh'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.heartK)
            self.leftHand2.grid(row = 3,column = 2)
            self.btnKh = tk.Label(self,image = self.backSide)
            self.btnKh.grid(row = 5,column = 12)
            deck.draw(parse_cards('Kh'))
            leftHandStr += 'Kh'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.heartK)
            self.rightHand1.grid(row = 3,column = 10)
            self.btnKh = tk.Label(self,image = self.backSide)
            self.btnKh.grid(row = 5,column = 12)
            deck.draw(parse_cards('Kh'))
            rightHandStr += 'Kh'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.heartK)
            self.rightHand2.grid(row = 3,column = 11)
            self.btnKh = tk.Label(self,image = self.backSide)
            self.btnKh.grid(row = 5,column = 12)
            deck.draw(parse_cards('Kh'))
            rightHandStr += 'Kh'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.heartK)
            self.flop1.grid(row = 0,column = 4)
            self.btnKh = tk.Label(self,image = self.backSide)
            self.btnKh.grid(row = 5,column = 12)
            deck.draw(parse_cards('Kh'))
            boardStr += 'Kh'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.heartK)
            self.flop2.grid(row = 0,column = 5)
            self.btnKh = tk.Label(self,image = self.backSide)
            self.btnKh.grid(row = 5,column = 12)
            deck.draw(parse_cards('Kh'))
            boardStr += 'Kh'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.heartK)
            self.flop3.grid(row = 0,column = 6)
            self.btnKh = tk.Label(self,image = self.backSide)
            self.btnKh.grid(row = 5,column = 12)
            deck.draw(parse_cards('Kh'))
            boardStr += 'Kh'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.heartK)
            self.turn.grid(row = 0,column = 7)
            self.btnKh = tk.Label(self,image = self.backSide)
            self.btnKh.grid(row = 5,column = 12)
            deck.draw(parse_cards('Kh'))
            boardStr += 'Kh'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.heartK)
            self.river.grid(row = 0,column = 8)
            self.btnKh = tk.Label(self,image = self.backSide)
            self.btnKh.grid(row = 5,column = 12)
            deck.draw(parse_cards('Kh'))
            boardStr += 'Kh'
            btnctr += 1
        self.checkClickTime()
    def clickAd(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.diamondA)
            self.leftHand1.grid(row = 3,column = 1)
            self.btnAd = tk.Label(self,image = self.backSide)
            self.btnAd.grid(row = 6,column = 0)
            deck.draw(parse_cards('Ad'))
            leftHandStr += 'Ad'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.diamondA)
            self.leftHand2.grid(row = 3,column = 2)
            self.btnAd = tk.Label(self,image = self.backSide)
            self.btnAd.grid(row = 6,column = 0)
            deck.draw(parse_cards('Ad'))
            leftHandStr += 'Ad'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.diamondA)
            self.rightHand1.grid(row = 3,column = 10)
            self.btnAd = tk.Label(self,image = self.backSide)
            self.btnAd.grid(row = 6,column = 0)
            deck.draw(parse_cards('Ad'))
            rightHandStr += 'Ad'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.diamondA)
            self.rightHand2.grid(row = 3,column = 11)
            self.btnAd = tk.Label(self,image = self.backSide)
            self.btnAd.grid(row = 6,column = 0)
            deck.draw(parse_cards('Ad'))
            rightHandStr += 'Ad'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.diamondA)
            self.flop1.grid(row = 0,column = 4)
            self.btnAd = tk.Label(self,image = self.backSide)
            self.btnAd.grid(row = 6,column = 0)
            deck.draw(parse_cards('Ad'))
            boardStr += 'Ad'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.diamondA)
            self.flop2.grid(row = 0,column = 5)
            self.btnAd = tk.Label(self,image = self.backSide)
            self.btnAd.grid(row = 6,column = 0)
            deck.draw(parse_cards('Ad'))
            boardStr += 'Ad'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.diamondA)
            self.flop3.grid(row = 0,column = 6)
            self.btnAd = tk.Label(self,image = self.backSide)
            self.btnAd.grid(row = 6,column = 0)
            deck.draw(parse_cards('Ad'))
            boardStr += 'Ad'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.diamondA)
            self.turn.grid(row = 0,column = 7)
            self.btnAd = tk.Label(self,image = self.backSide)
            self.btnAd.grid(row = 6,column = 0)
            deck.draw(parse_cards('Ad'))
            boardStr += 'Ad'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.diamondA)
            self.river.grid(row = 0,column = 8)
            self.btnAd = tk.Label(self,image = self.backSide)
            self.btnAd.grid(row = 6,column = 0)
            deck.draw(parse_cards('Ad'))
            boardStr += 'Ad'
            btnctr += 1
        self.checkClickTime() 
    def click2d(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.diamond2)
            self.leftHand1.grid(row = 3,column = 1)
            self.btn2d = tk.Label(self,image = self.backSide)
            self.btn2d.grid(row  = 6,column = 1)
            deck.draw(parse_cards('2d'))
            leftHandStr += '2d'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.diamond2)
            self.leftHand2.grid(row = 3,column = 2)
            self.btn2d = tk.Label(self,image = self.backSide)
            self.btn2d.grid(row  = 6,column = 1)
            deck.draw(parse_cards('2d'))
            leftHandStr += '2d'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.diamond2)
            self.rightHand1.grid(row = 3,column = 10)
            self.btn2d = tk.Label(self,image = self.backSide)
            self.btn2d.grid(row  = 6,column = 1)
            deck.draw(parse_cards('2d'))
            rightHandStr += '2d'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.diamond2)
            self.rightHand2.grid(row = 3,column = 11)
            self.btn2d = tk.Label(self,image = self.backSide)
            self.btn2d.grid(row  = 6,column = 1)
            deck.draw(parse_cards('2d'))
            rightHandStr += '2d'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.diamond2)
            self.flop1.grid(row = 0,column = 4)
            self.btn2d = tk.Label(self,image = self.backSide)
            self.btn2d.grid(row  = 6,column = 1)
            deck.draw(parse_cards('2d'))
            boardStr += '2d'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.diamond2)
            self.flop2.grid(row = 0,column = 5)
            self.btn2d = tk.Label(self,image = self.backSide)
            self.btn2d.grid(row  = 6,column = 1)
            deck.draw(parse_cards('2d'))
            boardStr += '2d'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.diamond2)
            self.flop3.grid(row = 0,column = 6)
            self.btn2d = tk.Label(self,image = self.backSide)
            self.btn2d.grid(row  = 6,column = 1)
            deck.draw(parse_cards('2d'))
            boardStr += '2d'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.diamond2)
            self.turn.grid(row = 0,column = 7)
            self.btn2d = tk.Label(self,image = self.backSide)
            self.btn2d.grid(row  = 6,column = 1)
            deck.draw(parse_cards('2d'))
            boardStr += '2d'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.diamond2)
            self.river.grid(row = 0,column = 8)
            self.btn2d = tk.Label(self,image = self.backSide)
            self.btn2d.grid(row  = 6,column = 1)
            deck.draw(parse_cards('2d'))
            boardStr += '2d'
            btnctr += 1
        self.checkClickTime()      
    def click3d(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.diamond3)
            self.leftHand1.grid(row = 3,column = 1)
            self.btn3d = tk.Label(self,image = self.backSide)
            self.btn3d.grid(row  = 6,column = 2)
            deck.draw(parse_cards('3d'))
            leftHandStr += '3d'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.diamond3)
            self.leftHand2.grid(row = 3,column = 2)
            self.btn3d = tk.Label(self,image = self.backSide)
            self.btn3d.grid(row  = 6,column = 2)
            deck.draw(parse_cards('3d'))
            leftHandStr += '3d'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.diamond3)
            self.rightHand1.grid(row = 3,column = 10)
            self.btn3d = tk.Label(self,image = self.backSide)
            self.btn3d.grid(row  = 6,column = 2)
            deck.draw(parse_cards('3d'))
            rightHandStr += '3d'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.diamond3)
            self.rightHand2.grid(row = 3,column = 11)
            self.btn3d = tk.Label(self,image = self.backSide)
            self.btn3d.grid(row  = 6,column = 2)
            deck.draw(parse_cards('3d'))
            rightHandStr += '3d'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.diamond3)
            self.flop1.grid(row = 0,column = 4)
            self.btn3d = tk.Label(self,image = self.backSide)
            self.btn3d.grid(row  = 6,column = 2)
            deck.draw(parse_cards('3d'))
            boardStr += '3d'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.diamond3)
            self.flop2.grid(row = 0,column = 5)
            self.btn3d = tk.Label(self,image = self.backSide)
            self.btn3d.grid(row  = 6,column = 2)
            deck.draw(parse_cards('3d'))
            boardStr += '3d'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.diamond3)
            self.flop3.grid(row = 0,column = 6)
            self.btn3d = tk.Label(self,image = self.backSide)
            self.btn3d.grid(row  = 6,column = 2)
            deck.draw(parse_cards('3d'))
            boardStr += '3d'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.diamond3)
            self.turn.grid(row = 0,column = 7)
            self.btn3d = tk.Label(self,image = self.backSide)
            self.btn3d.grid(row  = 6,column = 2)
            deck.draw(parse_cards('3d'))
            boardStr += '3d'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.diamond3)
            self.river.grid(row = 0,column = 8)
            self.btn3d = tk.Label(self,image = self.backSide)
            self.btn3d.grid(row  = 6,column = 2)
            deck.draw(parse_cards('3d'))
            boardStr += '3d'
            btnctr += 1
        self.checkClickTime()
    def click4d(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.diamond4)
            self.leftHand1.grid(row = 3,column = 1)
            self.btn4d = tk.Label(self,image = self.backSide)
            self.btn4d.grid(row = 6,column = 3)
            deck.draw(parse_cards('4d'))
            leftHandStr += '4d'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.diamond4)
            self.leftHand2.grid(row = 3,column = 2)
            self.btn4d = tk.Label(self,image = self.backSide)
            self.btn4d.grid(row = 6,column = 3)
            deck.draw(parse_cards('4d'))
            leftHandStr += '4d'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.diamond4)
            self.rightHand1.grid(row = 3,column = 10)
            self.btn4d = tk.Label(self,image = self.backSide)
            self.btn4d.grid(row = 6,column = 3)
            deck.draw(parse_cards('4d'))
            rightHandStr += '4d'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.diamond4)
            self.rightHand2.grid(row = 3,column = 11)
            self.btn4d = tk.Label(self,image = self.backSide)
            self.btn4d.grid(row = 6,column = 3)
            deck.draw(parse_cards('4d'))
            rightHandStr += '4d'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.diamond4)
            self.flop1.grid(row = 0,column = 4)
            self.btn4d = tk.Label(self,image = self.backSide)
            self.btn4d.grid(row = 6,column = 3)
            deck.draw(parse_cards('4d'))
            boardStr += '4d'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.diamond4)
            self.flop2.grid(row = 0,column = 5)
            self.btn4d = tk.Label(self,image = self.backSide)
            self.btn4d.grid(row = 6,column = 3)
            deck.draw(parse_cards('4d'))
            boardStr += '4d'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.diamond4)
            self.flop3.grid(row = 0,column = 6)
            self.btn4d = tk.Label(self,image = self.backSide)
            self.btn4d.grid(row = 6,column = 3)
            deck.draw(parse_cards('4d'))
            boardStr += '4d'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.diamond4)
            self.turn.grid(row = 0,column = 7)
            self.btn4d = tk.Label(self,image = self.backSide)
            self.btn4d.grid(row = 6,column = 3)
            deck.draw(parse_cards('4d'))
            boardStr += '4d'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.diamond4)
            self.river.grid(row = 0,column = 8)
            self.btn4d = tk.Label(self,image = self.backSide)
            self.btn4d.grid(row = 6,column = 3)
            deck.draw(parse_cards('4d'))
            boardStr += '4d'
            btnctr += 1
        self.checkClickTime()
    def click5d(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.diamond5)
            self.leftHand1.grid(row = 3,column = 1)
            self.btn5d = tk.Label(self,image = self.backSide)
            self.btn5d.grid(row = 6,column = 4)
            deck.draw(parse_cards('5d'))
            leftHandStr += '5d'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.diamond5)
            self.leftHand2.grid(row = 3,column = 2)
            self.btn5d = tk.Label(self,image = self.backSide)
            self.btn5d.grid(row = 6,column = 4)
            deck.draw(parse_cards('5d'))
            leftHandStr += '5d'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.diamond5)
            self.rightHand1.grid(row = 3,column = 10)
            self.btn5d = tk.Label(self,image = self.backSide)
            self.btn5d.grid(row = 6,column = 4)
            deck.draw(parse_cards('5d'))
            rightHandStr += '5d'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.diamond5)
            self.rightHand2.grid(row = 3,column = 11)
            self.btn5d = tk.Label(self,image = self.backSide)
            self.btn5d.grid(row = 6,column = 4)
            deck.draw(parse_cards('5d'))
            rightHandStr += '5d'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.diamond5)
            self.flop1.grid(row = 0,column = 4)
            self.btn5d = tk.Label(self,image = self.backSide)
            self.btn5d.grid(row = 6,column = 4)
            deck.draw(parse_cards('5d'))
            boardStr += '5d'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.diamond5)
            self.flop2.grid(row = 0,column = 5)
            self.btn5d = tk.Label(self,image = self.backSide)
            self.btn5d.grid(row = 6,column = 4)
            deck.draw(parse_cards('5d'))
            boardStr += '5d'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.diamond5)
            self.flop3.grid(row = 0,column = 6)
            self.btn5d = tk.Label(self,image = self.backSide)
            self.btn5d.grid(row = 6,column = 4)
            deck.draw(parse_cards('5d'))
            boardStr += '5d'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.diamond5)
            self.turn.grid(row = 0,column = 7)
            self.btn5d = tk.Label(self,image = self.backSide)
            self.btn5d.grid(row = 6,column = 4)
            deck.draw(parse_cards('5d'))
            boardStr += '5d'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.diamond5)
            self.river.grid(row = 0,column = 8)
            self.btn5d = tk.Label(self,image = self.backSide)
            self.btn5d.grid(row = 6,column = 4)
            deck.draw(parse_cards('5d'))
            boardStr += '5d'
            btnctr += 1
        self.checkClickTime()    
    def click6d(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.diamond6)
            self.leftHand1.grid(row = 3,column = 1)
            self.btn6d = tk.Label(self,image = self.backSide)
            self.btn6d.grid(row = 6,column = 5)
            deck.draw(parse_cards('6d'))
            leftHandStr += '6d'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.diamond6)
            self.leftHand2.grid(row = 3,column = 2)
            self.btn6d = tk.Label(self,image = self.backSide)
            self.btn6d.grid(row = 6,column = 5)
            deck.draw(parse_cards('6d'))
            leftHandStr += '6d'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.diamond6)
            self.rightHand1.grid(row = 3,column = 10)
            self.btn6d = tk.Label(self,image = self.backSide)
            self.btn6d.grid(row = 6,column = 5)
            deck.draw(parse_cards('6d'))
            rightHandStr += '6d'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.diamond6)
            self.rightHand2.grid(row = 3,column = 11)
            self.btn6d = tk.Label(self,image = self.backSide)
            self.btn6d.grid(row = 6,column = 5)
            deck.draw(parse_cards('6d'))
            rightHandStr += '6d'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.diamond6)
            self.flop1.grid(row = 0,column = 4)
            self.btn6d = tk.Label(self,image = self.backSide)
            self.btn6d.grid(row = 6,column = 5)
            deck.draw(parse_cards('6d'))
            boardStr += '6d'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.diamond6)
            self.flop2.grid(row = 0,column = 5)
            self.btn6d = tk.Label(self,image = self.backSide)
            self.btn6d.grid(row = 6,column = 5)
            deck.draw(parse_cards('6d'))
            boardStr += '6d'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.diamond6)
            self.flop3.grid(row = 0,column = 6)
            self.btn6d = tk.Label(self,image = self.backSide)
            self.btn6d.grid(row = 6,column = 5)
            deck.draw(parse_cards('6d'))
            boardStr += '6d'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.diamond6)
            self.turn.grid(row = 0,column = 7)
            self.btn6d = tk.Label(self,image = self.backSide)
            self.btn6d.grid(row = 6,column = 5)
            deck.draw(parse_cards('6d'))
            boardStr += '6d'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.diamond6)
            self.river.grid(row = 0,column = 8)
            self.btn6d = tk.Label(self,image = self.backSide)
            self.btn6d.grid(row = 6,column = 5)
            deck.draw(parse_cards('6d'))
            boardStr += '6d'
            btnctr += 1
        self.checkClickTime()   
    def click7d(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.diamond7)
            self.leftHand1.grid(row = 3,column = 1)
            self.btn7d = tk.Label(self,image = self.backSide)
            self.btn7d.grid(row = 6,column = 6)
            deck.draw(parse_cards('7d'))
            leftHandStr += '7d'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.diamond7)
            self.leftHand2.grid(row = 3,column = 2)
            self.btn7d = tk.Label(self,image = self.backSide)
            self.btn7d.grid(row = 6,column = 6)
            deck.draw(parse_cards('7d'))
            leftHandStr += '7d'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.diamond7)
            self.rightHand1.grid(row = 3,column = 10)
            self.btn7d = tk.Label(self,image = self.backSide)
            self.btn7d.grid(row = 6,column = 6)
            deck.draw(parse_cards('7d'))
            rightHandStr += '7d'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.diamond7)
            self.rightHand2.grid(row = 3,column = 11)
            self.btn7d = tk.Label(self,image = self.backSide)
            self.btn7d.grid(row = 6,column = 6)
            deck.draw(parse_cards('7d'))
            rightHandStr += '7d'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.diamond7)
            self.flop1.grid(row = 0,column = 4)
            self.btn7d = tk.Label(self,image = self.backSide)
            self.btn7d.grid(row = 6,column = 6)
            deck.draw(parse_cards('7d'))
            boardStr += '7d'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.diamond7)
            self.flop2.grid(row = 0,column = 5)
            self.btn7d = tk.Label(self,image = self.backSide)
            self.btn7d.grid(row = 6,column = 6)
            deck.draw(parse_cards('7d'))
            boardStr += '7d'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.diamond7)
            self.flop3.grid(row = 0,column = 6)
            self.btn7d = tk.Label(self,image = self.backSide)
            self.btn7d.grid(row = 6,column = 6)
            deck.draw(parse_cards('7d'))
            boardStr += '7d'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.diamond7)
            self.turn.grid(row = 0,column = 7)
            self.btn7d = tk.Label(self,image = self.backSide)
            self.btn7d.grid(row = 6,column = 6)
            deck.draw(parse_cards('7d'))
            boardStr += '7d'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.diamond7)
            self.river.grid(row = 0,column = 8)
            self.btn7d = tk.Label(self,image = self.backSide)
            self.btn7d.grid(row = 6,column = 6)
            deck.draw(parse_cards('7d'))
            boardStr += '7d'
            btnctr += 1
        self.checkClickTime() 
    def click8d(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.diamond8)
            self.leftHand1.grid(row = 3,column = 1)
            self.btn8d = tk.Label(self,image = self.backSide)
            self.btn8d.grid(row = 6,column = 7)
            deck.draw(parse_cards('8d'))
            leftHandStr += '8d'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.diamond8)
            self.leftHand2.grid(row = 3,column = 2)
            self.btn8d = tk.Label(self,image = self.backSide)
            self.btn8d.grid(row = 6,column = 7)
            deck.draw(parse_cards('8d'))
            leftHandStr += '8d'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.diamond8)
            self.rightHand1.grid(row = 3,column = 10)
            self.btn8d = tk.Label(self,image = self.backSide)
            self.btn8d.grid(row = 6,column = 7)
            deck.draw(parse_cards('8d'))
            rightHandStr += '8d'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.diamond8)
            self.rightHand2.grid(row = 3,column = 11)
            self.btn8d = tk.Label(self,image = self.backSide)
            self.btn8d.grid(row = 6,column = 7)
            deck.draw(parse_cards('8d'))
            rightHandStr += '8d'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.diamond8)
            self.flop1.grid(row = 0,column = 4)
            self.btn8d = tk.Label(self,image = self.backSide)
            self.btn8d.grid(row = 6,column = 7)
            deck.draw(parse_cards('8d'))
            boardStr += '8d'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.diamond8)
            self.flop2.grid(row = 0,column = 5)
            self.btn8d = tk.Label(self,image = self.backSide)
            self.btn8d.grid(row = 6,column = 7)
            deck.draw(parse_cards('8d'))
            boardStr += '8d'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.diamond8)
            self.flop3.grid(row = 0,column = 6)
            self.btn8d = tk.Label(self,image = self.backSide)
            self.btn8d.grid(row = 6,column = 7)
            deck.draw(parse_cards('8d'))
            boardStr += '8d'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.diamond8)
            self.turn.grid(row = 0,column = 7)
            self.btn8d = tk.Label(self,image = self.backSide)
            self.btn8d.grid(row = 6,column = 7)
            deck.draw(parse_cards('8d'))
            boardStr += '8d'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.diamond8)
            self.river.grid(row = 0,column = 8)
            self.btn8d = tk.Label(self,image = self.backSide)
            self.btn8d.grid(row = 6,column = 7)
            deck.draw(parse_cards('8d'))
            boardStr += '8d'
            btnctr += 1
        self.checkClickTime()           
    def click9d(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.diamond9)
            self.leftHand1.grid(row = 3,column = 1)
            self.btn9d = tk.Label(self,image = self.backSide)
            self.btn9d.grid(row = 6,column = 8)
            deck.draw(parse_cards('9d'))
            leftHandStr += '9d'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.diamond9)
            self.leftHand2.grid(row = 3,column = 2)
            self.btn9d = tk.Label(self,image = self.backSide)
            self.btn9d.grid(row = 6,column = 8)
            deck.draw(parse_cards('9d'))
            leftHandStr += '9d'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.diamond9)
            self.rightHand1.grid(row = 3,column = 10)
            self.btn9d = tk.Label(self,image = self.backSide)
            self.btn9d.grid(row = 6,column = 8)
            deck.draw(parse_cards('9d'))
            rightHandStr += '9d'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.diamond9)
            self.rightHand2.grid(row = 3,column = 11)
            self.btn9d = tk.Label(self,image = self.backSide)
            self.btn9d.grid(row = 6,column = 8)
            deck.draw(parse_cards('9d'))
            rightHandStr += '9d'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.diamond9)
            self.flop1.grid(row = 0,column = 4)
            self.btn9d = tk.Label(self,image = self.backSide)
            self.btn9d.grid(row = 6,column = 8)
            deck.draw(parse_cards('9d'))
            boardStr += '9d'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.diamond9)
            self.flop2.grid(row = 0,column = 5)
            self.btn9d = tk.Label(self,image = self.backSide)
            self.btn9d.grid(row = 6,column = 8)
            deck.draw(parse_cards('9d'))
            boardStr += '9d'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.diamond9)
            self.flop3.grid(row = 0,column = 6)
            self.btn9d = tk.Label(self,image = self.backSide)
            self.btn9d.grid(row = 6,column = 8)
            deck.draw(parse_cards('9d'))
            boardStr += '9d'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.diamond9)
            self.turn.grid(row = 0,column = 7)
            self.btn9d = tk.Label(self,image = self.backSide)
            self.btn9d.grid(row = 6,column = 8)
            deck.draw(parse_cards('9d'))
            boardStr += '9d'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.diamond9)
            self.river.grid(row = 0,column = 8)
            self.btn9d = tk.Label(self,image = self.backSide)
            self.btn9d.grid(row = 6,column = 8)
            deck.draw(parse_cards('9d'))
            boardStr += '9d'
            btnctr += 1
        self.checkClickTime()
    def clickTd(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.diamondT)
            self.leftHand1.grid(row = 3,column = 1)
            self.btnTd = tk.Label(self,image = self.backSide)
            self.btnTd.grid(row = 6,column = 9)
            deck.draw(parse_cards('Td'))
            leftHandStr += 'Td'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.diamondT)
            self.leftHand2.grid(row = 3,column = 2)
            self.btnTd = tk.Label(self,image = self.backSide)
            self.btnTd.grid(row = 6,column = 9)
            deck.draw(parse_cards('Td'))
            leftHandStr += 'Td'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.diamondT)
            self.rightHand1.grid(row = 3,column = 10)
            self.btnTd = tk.Label(self,image = self.backSide)
            self.btnTd.grid(row = 6,column = 9)
            deck.draw(parse_cards('Td'))
            rightHandStr += 'Td'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.diamondT)
            self.rightHand2.grid(row = 3,column = 11)
            self.btnTd = tk.Label(self,image = self.backSide)
            self.btnTd.grid(row = 6,column = 9)
            deck.draw(parse_cards('Td'))
            rightHandStr += 'Td'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.diamondT)
            self.flop1.grid(row = 0,column = 4)
            self.btnTd = tk.Label(self,image = self.backSide)
            self.btnTd.grid(row = 6,column = 9)
            deck.draw(parse_cards('Td'))
            boardStr += 'Td'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.diamondT)
            self.flop2.grid(row = 0,column = 5)
            self.btnTd = tk.Label(self,image = self.backSide)
            self.btnTd.grid(row = 6,column = 9)
            deck.draw(parse_cards('Td'))
            boardStr += 'Td'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.diamondT)
            self.flop3.grid(row = 0,column = 6)
            self.btnTd = tk.Label(self,image = self.backSide)
            self.btnTd.grid(row = 6,column = 9)
            deck.draw(parse_cards('Td'))
            boardStr += 'Td'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.diamondT)
            self.turn.grid(row = 0,column = 7)
            self.btnTd = tk.Label(self,image = self.backSide)
            self.btnTd.grid(row = 6,column = 9)
            deck.draw(parse_cards('Td'))
            boardStr += 'Td'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.diamondT)
            self.river.grid(row = 0,column = 8)
            self.btnTd = tk.Label(self,image = self.backSide)
            self.btnTd.grid(row = 6,column = 9)
            deck.draw(parse_cards('Td'))
            boardStr += 'Td'
            btnctr += 1
        self.checkClickTime()
    def clickJd(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.diamondJ)
            self.leftHand1.grid(row = 3,column = 1)
            self.btnJd = tk.Label(self,image = self.backSide)
            self.btnJd.grid(row = 6,column = 10)
            deck.draw(parse_cards('Jd'))
            leftHandStr += 'Jd'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.diamondJ)
            self.leftHand2.grid(row = 3,column = 2)
            self.btnJd = tk.Label(self,image = self.backSide)
            self.btnJd.grid(row = 6,column = 10)
            deck.draw(parse_cards('Jd'))
            leftHandStr += 'Jd'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.diamondJ)
            self.rightHand1.grid(row = 3,column = 10)
            self.btnJd = tk.Label(self,image = self.backSide)
            self.btnJd.grid(row = 6,column = 10)
            deck.draw(parse_cards('Jd'))
            rightHandStr += 'Jd'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.diamondJ)
            self.rightHand2.grid(row = 3,column = 11)
            self.btnJd = tk.Label(self,image = self.backSide)
            self.btnJd.grid(row = 6,column = 10)
            deck.draw(parse_cards('Jd'))
            rightHandStr += 'Jd'         
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.diamondJ)
            self.flop1.grid(row = 0,column = 4)
            self.btnJd = tk.Label(self,image = self.backSide)
            self.btnJd.grid(row = 6,column = 10)
            deck.draw(parse_cards('Jd'))
            boardStr += 'Jd'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.diamondJ)
            self.flop2.grid(row = 0,column = 5)
            self.btnJd = tk.Label(self,image = self.backSide)
            self.btnJd.grid(row = 6,column = 10)
            deck.draw(parse_cards('Jd'))
            boardStr += 'Jd'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.diamondJ)
            self.flop3.grid(row = 0,column = 6)
            self.btnJd = tk.Label(self,image = self.backSide)
            self.btnJd.grid(row = 6,column = 10)
            deck.draw(parse_cards('Jd'))
            boardStr += 'Jd'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.diamondJ)
            self.turn.grid(row = 0,column = 7)
            self.btnJd = tk.Label(self,image = self.backSide)
            self.btnJd.grid(row = 6,column = 10)
            deck.draw(parse_cards('Jd'))
            boardStr += 'Jd'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.diamondJ)
            self.river.grid(row = 0,column = 8)
            self.btnJd = tk.Label(self,image = self.backSide)
            self.btnJd.grid(row = 6,column = 10)
            deck.draw(parse_cards('Jd'))
            boardStr += 'Jd'
            btnctr += 1
        self.checkClickTime()
    def clickQd(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.diamondQ)
            self.leftHand1.grid(row = 3,column = 1)
            self.btnQd = tk.Label(self,image = self.backSide)
            self.btnQd.grid(row = 6,column = 11)
            deck.draw(parse_cards('Qd'))
            leftHandStr += 'Qd'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.diamondQ)
            self.leftHand2.grid(row = 3,column = 2)
            self.btnQd = tk.Label(self,image = self.backSide)
            self.btnQd.grid(row = 6,column = 11)
            deck.draw(parse_cards('Qd'))
            leftHandStr += 'Qd'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.diamondQ)
            self.rightHand1.grid(row = 3,column = 10)
            self.btnQd = tk.Label(self,image = self.backSide)
            self.btnQd.grid(row = 6,column = 11)
            deck.draw(parse_cards('Qd'))
            rightHandStr += 'Qd'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.diamondQ)
            self.rightHand2.grid(row = 3,column = 11)
            self.btnQd = tk.Label(self,image = self.backSide)
            self.btnQd.grid(row = 6,column = 11)
            deck.draw(parse_cards('Qd'))
            rightHandStr += 'Qd'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.diamondQ)
            self.flop1.grid(row = 0,column = 4)
            self.btnQd = tk.Label(self,image = self.backSide)
            self.btnQd.grid(row = 6,column = 11)
            deck.draw(parse_cards('Qd'))
            boardStr += 'Qd'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.diamondQ)
            self.flop2.grid(row = 0,column = 5)
            self.btnQd = tk.Label(self,image = self.backSide)
            self.btnQd.grid(row = 6,column = 11)
            deck.draw(parse_cards('Qd'))
            boardStr += 'Qd'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.diamondQ)
            self.flop3.grid(row = 0,column = 6)
            self.btnQd = tk.Label(self,image = self.backSide)
            self.btnQd.grid(row = 6,column = 11)
            deck.draw(parse_cards('Qd'))
            boardStr += 'Qd'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.diamondQ)
            self.turn.grid(row = 0,column = 7)
            self.btnQd = tk.Label(self,image = self.backSide)
            self.btnQd.grid(row = 6,column = 11)
            deck.draw(parse_cards('Qd'))
            boardStr += 'Qd'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.diamondQ)
            self.river.grid(row = 0,column = 8)
            self.btnQd = tk.Label(self,image = self.backSide)
            self.btnQd.grid(row = 6,column = 11)
            deck.draw(parse_cards('Qd'))
            boardStr += 'Qd'
            btnctr += 1
        self.checkClickTime()
    def clickKd(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.diamondK)
            self.leftHand1.grid(row = 3,column = 1)
            self.btnKd = tk.Label(self,image = self.backSide)
            self.btnKd.grid(row = 6,column = 12)
            deck.draw(parse_cards('Kd'))
            leftHandStr += 'Kd'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.diamondK)
            self.leftHand2.grid(row = 3,column = 2)
            self.btnKd = tk.Label(self,image = self.backSide)
            self.btnKd.grid(row = 6,column = 12)
            deck.draw(parse_cards('Kd'))
            leftHandStr += 'Kd'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.diamondK)
            self.rightHand1.grid(row = 3,column = 10)
            self.btnKd = tk.Label(self,image = self.backSide)
            self.btnKd.grid(row = 6,column = 12)
            deck.draw(parse_cards('Kd'))
            rightHandStr += 'Kd'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.diamondK)
            self.rightHand2.grid(row = 3,column = 11)
            self.btnKd = tk.Label(self,image = self.backSide)
            self.btnKd.grid(row = 6,column = 12)
            deck.draw(parse_cards('Kd'))
            rightHandStr += 'Kd'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.diamondK)
            self.flop1.grid(row = 0,column = 4)
            self.btnKd = tk.Label(self,image = self.backSide)
            self.btnKd.grid(row = 6,column = 12)
            deck.draw(parse_cards('Kd'))
            boardStr += 'Kd'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.diamondK)
            self.flop2.grid(row = 0,column = 5)
            self.btnKd = tk.Label(self,image = self.backSide)
            self.btnKd.grid(row = 6,column = 12)
            deck.draw(parse_cards('Kd'))
            boardStr += 'Kd'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.diamondK)
            self.flop3.grid(row = 0,column = 6)
            self.btnKd = tk.Label(self,image = self.backSide)
            self.btnKd.grid(row = 6,column = 12)
            deck.draw(parse_cards('Kd'))
            boardStr += 'Kd'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.diamondK)
            self.turn.grid(row = 0,column = 7)
            self.btnKd = tk.Label(self,image = self.backSide)
            self.btnKd.grid(row = 6,column = 12)
            deck.draw(parse_cards('Kd'))
            boardStr += 'Kd'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.diamondK)
            self.river.grid(row = 0,column = 8)
            self.btnKd = tk.Label(self,image = self.backSide)
            self.btnKd.grid(row = 6,column = 12)
            deck.draw(parse_cards('Kd'))
            boardStr += 'Kd'
            btnctr += 1
        self.checkClickTime()
    def clickAc(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.clubA)
            self.leftHand1.grid(row = 3,column = 1)
            self.btnAc = tk.Label(self,image = self.backSide)
            self.btnAc.grid(row = 7,column = 0)
            deck.draw(parse_cards('Ac'))
            leftHandStr += 'Ac'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.clubA)
            self.leftHand2.grid(row = 3,column = 2)
            self.btnAc = tk.Label(self,image = self.backSide)
            self.btnAc.grid(row = 7,column = 0)
            deck.draw(parse_cards('Ac'))
            leftHandStr += 'Ac'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.clubA)
            self.rightHand1.grid(row = 3,column = 10)
            self.btnAc = tk.Label(self,image = self.backSide)
            self.btnAc.grid(row = 7,column = 0)
            deck.draw(parse_cards('Ac'))
            rightHandStr += 'Ac'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.clubA)
            self.rightHand2.grid(row = 3,column = 11)
            self.btnAc = tk.Label(self,image = self.backSide)
            self.btnAc.grid(row = 7,column = 0)
            deck.draw(parse_cards('Ac'))
            rightHandStr += 'Ac'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.clubA)
            self.flop1.grid(row = 0,column = 4)
            self.btnAc = tk.Label(self,image = self.backSide)
            self.btnAc.grid(row = 7,column = 0)
            deck.draw(parse_cards('Ac'))
            boardStr += 'Ac'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.clubA)
            self.flop2.grid(row = 0,column = 5)
            self.btnAc = tk.Label(self,image = self.backSide)
            self.btnAc.grid(row = 7,column = 0)
            deck.draw(parse_cards('Ac'))
            boardStr += 'Ac'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.clubA)
            self.flop3.grid(row = 0,column = 6)
            self.btnAc = tk.Label(self,image = self.backSide)
            self.btnAc.grid(row = 7,column = 0)
            deck.draw(parse_cards('Ac'))
            boardStr += 'Ac'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.clubA)
            self.turn.grid(row = 0,column = 7)
            self.btnAc = tk.Label(self,image = self.backSide)
            self.btnAc.grid(row = 7,column = 0)
            deck.draw(parse_cards('Ac'))
            boardStr += 'Ac'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.clubA)
            self.river.grid(row = 0,column = 8)
            self.btnAc = tk.Label(self,image = self.backSide)
            self.btnAc.grid(row = 7,column = 0)
            deck.draw(parse_cards('Ac'))
            boardStr += 'Ac'
            btnctr += 1
        self.checkClickTime()
    def click2c(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.club2)
            self.leftHand1.grid(row = 3,column = 1)
            self.btn2c = tk.Label(self,image = self.backSide)
            self.btn2c.grid(row = 7,column = 1)
            deck.draw(parse_cards('2c'))
            leftHandStr += '2c'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.club2)
            self.leftHand2.grid(row = 3,column = 2)
            self.btn2c = tk.Label(self,image = self.backSide)
            self.btn2c.grid(row = 7,column = 1)
            deck.draw(parse_cards('2c'))
            leftHandStr += '2c'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.club2)
            self.rightHand1.grid(row = 3,column = 10)
            self.btn2c = tk.Label(self,image = self.backSide)
            self.btn2c.grid(row = 7,column = 1)
            deck.draw(parse_cards('2c'))
            rightHandStr += '2c'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.club2)
            self.rightHand2.grid(row = 3,column = 11)
            self.btn2c = tk.Label(self,image = self.backSide)
            self.btn2c.grid(row = 7,column = 1)
            deck.draw(parse_cards('2c'))
            rightHandStr += '2c'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.club2)
            self.flop1.grid(row = 0,column = 4)
            self.btn2c = tk.Label(self,image = self.backSide)
            self.btn2c.grid(row = 7,column = 1)
            deck.draw(parse_cards('2c'))
            boardStr += '2c'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.club2)
            self.flop2.grid(row = 0,column = 5)
            self.btn2c = tk.Label(self,image = self.backSide)
            self.btn2c.grid(row = 7,column = 1)
            deck.draw(parse_cards('2c'))
            boardStr += '2c'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.club2)
            self.flop3.grid(row = 0,column = 6)
            self.btn2c = tk.Label(self,image = self.backSide)
            self.btn2c.grid(row = 7,column = 1)
            deck.draw(parse_cards('2c'))
            boardStr += '2c'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.club2)
            self.turn.grid(row = 0,column = 7)
            self.btn2c = tk.Label(self,image = self.backSide)
            self.btn2c.grid(row = 7,column = 1)
            deck.draw(parse_cards('2c'))
            boardStr += '2c'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.club2)
            self.river.grid(row = 0,column = 8)
            self.btn2c = tk.Label(self,image = self.backSide)
            self.btn2c.grid(row = 7,column = 1)
            deck.draw(parse_cards('2c'))
            boardStr += '2c'
            btnctr += 1
        self.checkClickTime()
    def click3c(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.club3)
            self.leftHand1.grid(row = 3,column = 1)
            self.btn3c = tk.Label(self,image = self.backSide)
            self.btn3c.grid(row = 7,column = 2)
            deck.draw(parse_cards('3c'))
            leftHandStr += '3c'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.club3)
            self.leftHand2.grid(row = 3,column = 2)
            self.btn3c = tk.Label(self,image = self.backSide)
            self.btn3c.grid(row = 7,column = 2)
            deck.draw(parse_cards('3c'))
            leftHandStr += '3c'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.club3)
            self.rightHand1.grid(row = 3,column = 10)
            self.btn3c = tk.Label(self,image = self.backSide)
            self.btn3c.grid(row = 7,column = 2)
            deck.draw(parse_cards('3c'))
            rightHandStr += '3c'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.club3)
            self.rightHand2.grid(row = 3,column = 11)
            self.btn3c = tk.Label(self,image = self.backSide)
            self.btn3c.grid(row = 7,column = 2)
            deck.draw(parse_cards('3c'))
            rightHandStr += '3c'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.club3)
            self.flop1.grid(row = 0,column = 4)
            self.btn3c = tk.Label(self,image = self.backSide)
            self.btn3c.grid(row = 7,column = 2)
            deck.draw(parse_cards('3c'))
            boardStr += '3c'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.club3)
            self.flop2.grid(row = 0,column = 5)
            self.btn3c = tk.Label(self,image = self.backSide)
            self.btn3c.grid(row = 7,column = 2)
            deck.draw(parse_cards('3c'))
            boardStr += '3c'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.club3)
            self.flop3.grid(row = 0,column = 6)
            self.btn3c = tk.Label(self,image = self.backSide)
            self.btn3c.grid(row = 7,column = 2)
            deck.draw(parse_cards('3c'))
            boardStr += '3c'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.club3)
            self.turn.grid(row = 0,column = 7)
            self.btn3c = tk.Label(self,image = self.backSide)
            self.btn3c.grid(row = 7,column = 2)
            deck.draw(parse_cards('3c'))
            boardStr += '3c'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.club3)
            self.river.grid(row = 0,column = 8)
            self.btn3c = tk.Label(self,image = self.backSide)
            self.btn3c.grid(row = 7,column = 2)
            deck.draw(parse_cards('3c'))
            boardStr += '3c'
            btnctr += 1
        self.checkClickTime()
    def click4c(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.club4)
            self.leftHand1.grid(row = 3,column = 1)
            self.btn4c = tk.Label(self,image = self.backSide)
            self.btn4c.grid(row = 7,column = 3)
            deck.draw(parse_cards('4c'))
            leftHandStr += '4c'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.club4)
            self.leftHand2.grid(row = 3,column = 2)
            self.btn4c = tk.Label(self,image = self.backSide)
            self.btn4c.grid(row = 7,column = 3)
            deck.draw(parse_cards('4c'))
            leftHandStr += '4c'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.club4)
            self.rightHand1.grid(row = 3,column = 10)
            self.btn4c = tk.Label(self,image = self.backSide)
            self.btn4c.grid(row = 7,column = 3)
            deck.draw(parse_cards('4c'))
            rightHandStr += '4c'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.club4)
            self.rightHand2.grid(row = 3,column = 11)
            self.btn4c = tk.Label(self,image = self.backSide)
            self.btn4c.grid(row = 7,column = 3)
            deck.draw(parse_cards('4c'))
            rightHandStr += '4c'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.club4)
            self.flop1.grid(row = 0,column = 4)
            self.btn4c = tk.Label(self,image = self.backSide)
            self.btn4c.grid(row = 7,column = 3)
            deck.draw(parse_cards('4c'))
            boardStr += '4c'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.club4)
            self.flop2.grid(row = 0,column = 5)
            self.btn4c = tk.Label(self,image = self.backSide)
            self.btn4c.grid(row = 7,column = 3)
            deck.draw(parse_cards('4c'))
            boardStr += '4c'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.club4)
            self.flop3.grid(row = 0,column = 6)
            self.btn4c = tk.Label(self,image = self.backSide)
            self.btn4c.grid(row = 7,column = 3)
            deck.draw(parse_cards('4c'))
            boardStr += '4c'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.club4)
            self.turn.grid(row = 0,column = 7)
            self.btn4c = tk.Label(self,image = self.backSide)
            self.btn4c.grid(row = 7,column = 3)
            deck.draw(parse_cards('4c'))
            boardStr += '4c'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.club4)
            self.river.grid(row = 0,column = 8)
            self.btn4c = tk.Label(self,image = self.backSide)
            self.btn4c.grid(row = 7,column = 3)
            deck.draw(parse_cards('4c'))
            boardStr += '4c'
            btnctr += 1
        self.checkClickTime()
    def click5c(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.club5)
            self.leftHand1.grid(row = 3,column = 1)
            self.btn5c = tk.Label(self,image = self.backSide)
            self.btn5c.grid(row = 7,column = 4)
            deck.draw(parse_cards('5c'))
            leftHandStr += '5c'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.club5)
            self.leftHand2.grid(row = 3,column = 2)
            self.btn5c = tk.Label(self,image = self.backSide)
            self.btn5c.grid(row = 7,column = 4)
            deck.draw(parse_cards('5c'))
            leftHandStr += '5c'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.club5)
            self.rightHand1.grid(row = 3,column = 10)
            self.btn5c = tk.Label(self,image = self.backSide)
            self.btn5c.grid(row = 7,column = 4)
            deck.draw(parse_cards('5c'))
            rightHandStr += '5c'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.club5)
            self.rightHand2.grid(row = 3,column = 11)
            self.btn5c = tk.Label(self,image = self.backSide)
            self.btn5c.grid(row = 7,column = 4)
            deck.draw(parse_cards('5c'))
            rightHandStr += '5c'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.club5)
            self.flop1.grid(row = 0,column = 4)
            self.btn5c = tk.Label(self,image = self.backSide)
            self.btn5c.grid(row = 7,column = 4)
            deck.draw(parse_cards('5c'))
            boardStr += '5c'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.club5)
            self.flop2.grid(row = 0,column = 5)
            self.btn5c = tk.Label(self,image = self.backSide)
            self.btn5c.grid(row = 7,column = 4)
            deck.draw(parse_cards('5c'))
            boardStr += '5c'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.club5)
            self.flop3.grid(row = 0,column = 6)
            self.btn5c = tk.Label(self,image = self.backSide)
            self.btn5c.grid(row = 7,column = 4)
            deck.draw(parse_cards('5c'))
            boardStr += '5c'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.club5)
            self.turn.grid(row = 0,column = 7)
            self.btn5c = tk.Label(self,image = self.backSide)
            self.btn5c.grid(row = 7,column = 4)
            deck.draw(parse_cards('5c'))
            boardStr += '5c'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.club5)
            self.river.grid(row = 0,column = 8)
            self.btn5c = tk.Label(self,image = self.backSide)
            self.btn5c.grid(row = 7,column = 4)
            deck.draw(parse_cards('5c'))
            boardStr += '5c'
            btnctr += 1
        self.checkClickTime()
    def click6c(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.club6)
            self.leftHand1.grid(row = 3,column = 1)
            self.btn6c = tk.Label(self,image = self.backSide)
            self.btn6c.grid(row = 7,column = 5)
            deck.draw(parse_cards('6c'))
            leftHandStr += '6c'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.club6)
            self.leftHand2.grid(row = 3,column = 2)
            self.btn6c = tk.Label(self,image = self.backSide)
            self.btn6c.grid(row = 7,column = 5)
            deck.draw(parse_cards('6c'))
            leftHandStr += '6c'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.club6)
            self.rightHand1.grid(row = 3,column = 10)
            self.btn6c = tk.Label(self,image = self.backSide)
            self.btn6c.grid(row = 7,column = 5)
            deck.draw(parse_cards('6c'))
            rightHandStr += '6c'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.club6)
            self.rightHand2.grid(row = 3,column = 11)
            self.btn6c = tk.Label(self,image = self.backSide)
            self.btn6c.grid(row = 7,column = 5)
            deck.draw(parse_cards('6c'))
            rightHandStr += '6c'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.club6)
            self.flop1.grid(row = 0,column = 4)
            self.btn6c = tk.Label(self,image = self.backSide)
            self.btn6c.grid(row = 7,column = 5)
            deck.draw(parse_cards('6c'))
            boardStr += '6c'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.club6)
            self.flop2.grid(row = 0,column = 5)
            self.btn6c = tk.Label(self,image = self.backSide)
            self.btn6c.grid(row = 7,column = 5)
            deck.draw(parse_cards('6c'))
            boardStr += '6c'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.club6)
            self.flop3.grid(row = 0,column = 6)
            self.btn6c = tk.Label(self,image = self.backSide)
            self.btn6c.grid(row = 7,column = 5)
            deck.draw(parse_cards('6c'))
            boardStr += '6c'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.club6)
            self.turn.grid(row = 0,column = 7)
            self.btn6c = tk.Label(self,image = self.backSide)
            self.btn6c.grid(row = 7,column = 5)
            deck.draw(parse_cards('6c'))
            boardStr += '6c'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.club6)
            self.river.grid(row = 0,column = 8)
            self.btn6c = tk.Label(self,image = self.backSide)
            self.btn6c.grid(row = 7,column = 5)
            deck.draw(parse_cards('6c'))
            boardStr += '6c'
            btnctr += 1
        self.checkClickTime()
    def click7c(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.club7)
            self.leftHand1.grid(row = 3,column = 1)
            self.btn7c = tk.Label(self,image = self.backSide)
            self.btn7c.grid(row = 7,column = 6)
            deck.draw(parse_cards('7c'))
            leftHandStr += '7c'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.club7)
            self.leftHand2.grid(row = 3,column = 2)
            self.btn7c = tk.Label(self,image = self.backSide)
            self.btn7c.grid(row = 7,column = 6)
            deck.draw(parse_cards('7c'))
            leftHandStr += '7c'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.club7)
            self.rightHand1.grid(row = 3,column = 10)
            self.btn7c = tk.Label(self,image = self.backSide)
            self.btn7c.grid(row = 7,column = 6)
            deck.draw(parse_cards('7c'))
            rightHandStr += '7c'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.club7)
            self.rightHand2.grid(row = 3,column = 11)
            self.btn7c = tk.Label(self,image = self.backSide)
            self.btn7c.grid(row = 7,column = 6)
            deck.draw(parse_cards('7c'))
            rightHandStr += '7c'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.club7)
            self.flop1.grid(row = 0,column = 4)
            self.btn7c = tk.Label(self,image = self.backSide)
            self.btn7c.grid(row = 7,column = 6)
            deck.draw(parse_cards('7c'))
            boardStr += '7c'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.club7)
            self.flop2.grid(row = 0,column = 5)
            self.btn7c = tk.Label(self,image = self.backSide)
            self.btn7c.grid(row = 7,column = 6)
            deck.draw(parse_cards('7c'))
            boardStr += '7c'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.club7)
            self.flop3.grid(row = 0,column = 6)
            self.btn7c = tk.Label(self,image = self.backSide)
            self.btn7c.grid(row = 7,column = 6)
            deck.draw(parse_cards('7c'))
            boardStr += '7c'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.club7)
            self.turn.grid(row = 0,column = 7)
            self.btn7c = tk.Label(self,image = self.backSide)
            self.btn7c.grid(row = 7,column = 6)
            deck.draw(parse_cards('7c'))
            boardStr += '7c'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.club7)
            self.river.grid(row = 0,column = 8)
            self.btn7c = tk.Label(self,image = self.backSide)
            self.btn7c.grid(row = 7,column = 6)
            deck.draw(parse_cards('7c'))
            boardStr += '7c'
            btnctr += 1
        self.checkClickTime()
    def click8c(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.club8)
            self.leftHand1.grid(row = 3,column = 1)
            self.btn8c = tk.Label(self,image = self.backSide)
            self.btn8c.grid(row = 7,column = 7)
            deck.draw(parse_cards('8c'))
            leftHandStr += '8c'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.club8)
            self.leftHand2.grid(row = 3,column = 2)
            self.btn8c = tk.Label(self,image = self.backSide)
            self.btn8c.grid(row = 7,column = 7)
            deck.draw(parse_cards('8c'))
            leftHandStr += '8c'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.club8)
            self.rightHand1.grid(row = 3,column = 10)
            self.btn8c = tk.Label(self,image = self.backSide)
            self.btn8c.grid(row = 7,column = 7)
            deck.draw(parse_cards('8c'))
            rightHandStr += '8c'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.club8)
            self.rightHand2.grid(row = 3,column = 11)
            self.btn8c = tk.Label(self,image = self.backSide)
            self.btn8c.grid(row = 7,column = 7)
            deck.draw(parse_cards('8c'))
            rightHandStr += '8c'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.club8)
            self.flop1.grid(row = 0,column = 4)
            self.btn8c = tk.Label(self,image = self.backSide)
            self.btn8c.grid(row = 7,column = 7)
            deck.draw(parse_cards('8c'))
            boardStr += '8c'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.club8)
            self.flop2.grid(row = 0,column = 5)
            self.btn8c = tk.Label(self,image = self.backSide)
            self.btn8c.grid(row = 7,column = 7)
            deck.draw(parse_cards('8c'))
            boardStr += '8c'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.club8)
            self.flop3.grid(row = 0,column = 6)
            self.btn8c = tk.Label(self,image = self.backSide)
            self.btn8c.grid(row = 7,column = 7)
            deck.draw(parse_cards('8c'))
            boardStr += '8c'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.club8)
            self.turn.grid(row = 0,column = 7)
            self.btn8c = tk.Label(self,image = self.backSide)
            self.btn8c.grid(row = 7,column = 7)
            deck.draw(parse_cards('8c'))
            boardStr += '8c'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.club8)
            self.river.grid(row = 0,column = 8)
            self.btn8c = tk.Label(self,image = self.backSide)
            self.btn8c.grid(row = 7,column = 7)
            deck.draw(parse_cards('8c'))
            boardStr += '8c'
            btnctr += 1
        self.checkClickTime()
    def click9c(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.club9)
            self.leftHand1.grid(row = 3,column = 1)
            self.btn9c = tk.Label(self,image = self.backSide)
            self.btn9c.grid(row = 7,column = 8)
            deck.draw(parse_cards('9c'))
            leftHandStr += '9c'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.club9)
            self.leftHand2.grid(row = 3,column = 2)
            self.btn9c = tk.Label(self,image = self.backSide)
            self.btn9c.grid(row = 7,column = 8)
            deck.draw(parse_cards('9c'))
            leftHandStr += '9c'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.club9)
            self.rightHand1.grid(row = 3,column = 10)
            self.btn9c = tk.Label(self,image = self.backSide)
            self.btn9c.grid(row = 7,column = 8)
            deck.draw(parse_cards('9c'))
            rightHandStr += '9c'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.club9)
            self.rightHand2.grid(row = 3,column = 11)
            self.btn9c = tk.Label(self,image = self.backSide)
            self.btn9c.grid(row = 7,column = 8)
            deck.draw(parse_cards('9c'))
            rightHandStr += '9c'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.club9)
            self.flop1.grid(row = 0,column = 4)
            self.btn9c = tk.Label(self,image = self.backSide)
            self.btn9c.grid(row = 7,column = 8)
            deck.draw(parse_cards('9c'))
            boardStr += '9c'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.club9)
            self.flop2.grid(row = 0,column = 5)
            self.btn9c = tk.Label(self,image = self.backSide)
            self.btn9c.grid(row = 7,column = 8)
            deck.draw(parse_cards('9c'))
            boardStr += '9c'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.club9)
            self.flop3.grid(row = 0,column = 6)
            self.btn9c = tk.Label(self,image = self.backSide)
            self.btn9c.grid(row = 7,column = 8)
            deck.draw(parse_cards('9c'))
            boardStr += '9c'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.club9)
            self.turn.grid(row = 0,column = 7)
            self.btn9c = tk.Label(self,image = self.backSide)
            self.btn9c.grid(row = 7,column = 8)
            deck.draw(parse_cards('9c'))
            boardStr += '9c'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.club9)
            self.river.grid(row = 0,column = 8)
            self.btn9c = tk.Label(self,image = self.backSide)
            self.btn9c.grid(row = 7,column = 8)
            deck.draw(parse_cards('9c'))
            boardStr += '9c'
            btnctr += 1
        self.checkClickTime()
    def clickTc(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.clubT)
            self.leftHand1.grid(row = 3,column = 1)
            self.btnTc = tk.Label(self,image = self.backSide)
            self.btnTc.grid(row = 7,column = 9)
            deck.draw(parse_cards('Tc'))
            leftHandStr += 'Tc'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.clubT)
            self.leftHand2.grid(row = 3,column = 2)
            self.btnTc = tk.Label(self,image = self.backSide)
            self.btnTc.grid(row = 7,column = 9)
            deck.draw(parse_cards('Tc'))
            leftHandStr += 'Tc'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.clubT)
            self.rightHand1.grid(row = 3,column = 10)
            self.btnTc = tk.Label(self,image = self.backSide)
            self.btnTc.grid(row = 7,column = 9)
            deck.draw(parse_cards('Tc'))
            rightHandStr += 'Tc'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.clubT)
            self.rightHand2.grid(row = 3,column = 11)
            self.btnTc = tk.Label(self,image = self.backSide)
            self.btnTc.grid(row = 7,column = 9)
            deck.draw(parse_cards('Tc'))
            rightHandStr += 'Tc'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.clubT)
            self.flop1.grid(row = 0,column = 4)
            self.btnTc = tk.Label(self,image = self.backSide)
            self.btnTc.grid(row = 7,column = 9)
            deck.draw(parse_cards('Tc'))
            boardStr += 'Tc'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.clubT)
            self.flop2.grid(row = 0,column = 5)
            self.btnTc = tk.Label(self,image = self.backSide)
            self.btnTc.grid(row = 7,column = 9)
            deck.draw(parse_cards('Tc'))
            boardStr += 'Tc'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.clubT)
            self.flop3.grid(row = 0,column = 6)
            self.btnTc = tk.Label(self,image = self.backSide)
            self.btnTc.grid(row = 7,column = 9)
            deck.draw(parse_cards('Tc'))
            boardStr += 'Tc'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.clubT)
            self.turn.grid(row = 0,column = 7)
            self.btnTc = tk.Label(self,image = self.backSide)
            self.btnTc.grid(row = 7,column = 9)
            deck.draw(parse_cards('Tc'))
            boardStr += 'Tc'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.clubT)
            self.river.grid(row = 0,column = 8)
            self.btnTc = tk.Label(self,image = self.backSide)
            self.btnTc.grid(row = 7,column = 9)
            deck.draw(parse_cards('Tc'))
            boardStr += 'Tc'
            btnctr += 1
        self.checkClickTime()
    def clickJc(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.clubJ)
            self.leftHand1.grid(row = 3,column = 1)
            self.btnJc = tk.Label(self,image = self.backSide)
            self.btnJc.grid(row = 7,column = 10)
            deck.draw(parse_cards('Jc'))
            leftHandStr += 'Jc'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.clubJ)
            self.leftHand2.grid(row = 3,column = 2)
            self.btnJc = tk.Label(self,image = self.backSide)
            self.btnJc.grid(row = 7,column = 10)
            deck.draw(parse_cards('Jc'))
            leftHandStr += 'Jc'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.clubJ)
            self.rightHand1.grid(row = 3,column = 10)
            self.btnJc = tk.Label(self,image = self.backSide)
            self.btnJc.grid(row = 7,column = 10)
            deck.draw(parse_cards('Jc'))
            rightHandStr += 'Jc'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.clubJ)
            self.rightHand2.grid(row = 3,column = 11)
            self.btnJc = tk.Label(self,image = self.backSide)
            self.btnJc.grid(row = 7,column = 10)
            deck.draw(parse_cards('Jc'))
            rightHandStr += 'Jc'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.clubJ)
            self.flop1.grid(row = 0,column = 4)
            self.btnJc = tk.Label(self,image = self.backSide)
            self.btnJc.grid(row = 7,column = 10)
            deck.draw(parse_cards('Jc'))
            boardStr += 'Jc'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.clubJ)
            self.flop2.grid(row = 0,column = 5)
            self.btnJc = tk.Label(self,image = self.backSide)
            self.btnJc.grid(row = 7,column = 10)
            deck.draw(parse_cards('Jc'))
            boardStr += 'Jc'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.clubJ)
            self.flop3.grid(row = 0,column = 6)
            self.btnJc = tk.Label(self,image = self.backSide)
            self.btnJc.grid(row = 7,column = 10)
            deck.draw(parse_cards('Jc'))
            boardStr += 'Jc'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.clubJ)
            self.turn.grid(row = 0,column = 7)
            self.btnJc = tk.Label(self,image = self.backSide)
            self.btnJc.grid(row = 7,column = 10)
            deck.draw(parse_cards('Jc'))
            boardStr += 'Jc'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.clubJ)
            self.river.grid(row = 0,column = 8)
            self.btnJc = tk.Label(self,image = self.backSide)
            self.btnJc.grid(row = 7,column = 10)
            deck.draw(parse_cards('Jc'))
            boardStr += 'Jc'
            btnctr += 1
        self.checkClickTime()
    def clickQc(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.clubQ)
            self.leftHand1.grid(row = 3,column = 1)
            self.btnQc = tk.Label(self,image = self.backSide)
            self.btnQc.grid(row = 7,column = 11)
            deck.draw(parse_cards('Qc'))
            leftHandStr += 'Qc'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.clubQ)
            self.leftHand2.grid(row = 3,column = 2)
            self.btnQc = tk.Label(self,image = self.backSide)
            self.btnQc.grid(row = 7,column = 11)
            deck.draw(parse_cards('Qc'))
            leftHandStr += 'Qc'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.clubQ)
            self.rightHand1.grid(row = 3,column = 10)
            self.btnQc = tk.Label(self,image = self.backSide)
            self.btnQc.grid(row = 7,column = 11)
            deck.draw(parse_cards('Qc'))
            rightHandStr += 'Qc'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.clubQ)
            self.rightHand2.grid(row = 3,column = 11)
            self.btnQc = tk.Label(self,image = self.backSide)
            self.btnQc.grid(row = 7,column = 11)
            deck.draw(parse_cards('Qc'))
            rightHandStr += 'Qc'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.clubQ)
            self.flop1.grid(row = 0,column = 4)
            self.btnQc = tk.Label(self,image = self.backSide)
            self.btnQc.grid(row = 7,column = 11)
            deck.draw(parse_cards('Qc'))
            boardStr += 'Qc'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.clubQ)
            self.flop2.grid(row = 0,column = 5)
            self.btnQc = tk.Label(self,image = self.backSide)
            self.btnQc.grid(row = 7,column = 11)
            deck.draw(parse_cards('Qc'))
            boardStr += 'Qc'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.clubQ)
            self.flop3.grid(row = 0,column = 6)
            self.btnQc = tk.Label(self,image = self.backSide)
            self.btnQc.grid(row = 7,column = 11)
            deck.draw(parse_cards('Qc'))
            boardStr += 'Qc'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.clubQ)
            self.turn.grid(row = 0,column = 7)
            self.btnQc = tk.Label(self,image = self.backSide)
            self.btnQc.grid(row = 7,column = 11)
            deck.draw(parse_cards('Qc'))
            boardStr += 'Qc'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.clubQ)
            self.river.grid(row = 0,column = 8)
            self.btnQc = tk.Label(self,image = self.backSide)
            self.btnQc.grid(row = 7,column = 11)
            deck.draw(parse_cards('Qc'))
            boardStr += 'Qc'
            btnctr += 1
        self.checkClickTime()
    def clickKc(self):
        global btnctr
        global deck
        global leftHandStr
        global rightHandStr
        global boardStr
        if btnctr == 0:
            self.leftHand1 = tk.Label(self,image = self.clubK)
            self.leftHand1.grid(row = 3,column = 1)
            self.btnKc = tk.Label(self,image = self.backSide)
            self.btnKc.grid(row = 7,column = 12)
            deck.draw(parse_cards('Kc'))
            leftHandStr += 'Kc'
            btnctr += 1
        elif btnctr == 1:
            self.leftHand2 = tk.Label(self,image = self.clubK)
            self.leftHand2.grid(row = 3,column = 2)
            self.btnKc = tk.Label(self,image = self.backSide)
            self.btnKc.grid(row = 7,column = 12)
            deck.draw(parse_cards('Kc'))
            leftHandStr += 'Kc'
            btnctr += 1
        elif btnctr == 2:
            self.rightHand1 = tk.Label(self,image = self.clubK)
            self.rightHand1.grid(row = 3,column = 10)
            self.btnKc = tk.Label(self,image = self.backSide)
            self.btnKc.grid(row = 7,column = 12)
            deck.draw(parse_cards('Kc'))
            rightHandStr += 'Kc'
            btnctr += 1
        elif btnctr == 3:
            self.rightHand2 = tk.Label(self,image = self.clubK)
            self.rightHand2.grid(row = 3,column = 11)
            self.btnKc = tk.Label(self,image = self.backSide)
            self.btnKc.grid(row = 7,column = 12)
            deck.draw(parse_cards('Kc'))
            rightHandStr += 'Kc'
            btnctr += 1
        elif btnctr == 4:
            self.flop1 = tk.Label(self,image = self.clubK)
            self.flop1.grid(row = 0,column = 4)
            self.btnKc = tk.Label(self,image = self.backSide)
            self.btnKc.grid(row = 7,column = 12)
            deck.draw(parse_cards('Kc'))
            boardStr += 'Kc'
            btnctr += 1
        elif btnctr == 5:
            self.flop2 = tk.Label(self,image = self.clubK)
            self.flop2.grid(row = 0,column = 5)
            self.btnKc = tk.Label(self,image = self.backSide)
            self.btnKc.grid(row = 7,column = 12)
            deck.draw(parse_cards('Kc'))
            boardStr += 'Kc'
            btnctr += 1
        elif btnctr == 6:
            self.flop3 = tk.Label(self,image = self.clubK)
            self.flop3.grid(row = 0,column = 6)
            self.btnKc = tk.Label(self,image = self.backSide)
            self.btnKc.grid(row = 7,column = 12)
            deck.draw(parse_cards('Kc'))
            boardStr += 'Kc'
            btnctr += 1
        elif btnctr == 7:
            self.turn = tk.Label(self,image = self.clubK)
            self.turn.grid(row = 0,column = 7)
            self.btnKc = tk.Label(self,image = self.backSide)
            self.btnKc.grid(row = 7,column = 12)
            deck.draw(parse_cards('Kc'))
            boardStr += 'Kc'
            btnctr += 1
        elif btnctr == 8:
            self.river = tk.Label(self,image = self.clubK)
            self.river.grid(row = 0,column = 8)
            self.btnKc = tk.Label(self,image = self.backSide)
            self.btnKc.grid(row = 7,column = 12)
            deck.draw(parse_cards('Kc'))
            boardStr += 'Kc'
            btnctr += 1
        self.checkClickTime()
        #checkClickTime(=4算preflop,=7算flop,=8算turn,=10算river)

cal = Calculator()
cal.master.title("Texas Hold'em Calculator")
cal.mainloop()
