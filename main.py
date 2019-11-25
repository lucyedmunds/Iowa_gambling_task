from psychopy.visual import *
import psychopy.visual
from psychopy import event, core
from filemanager import *
from participant import *


display = Window(
    units="pix",
    size=[1440, 900],  # 1366,768
    color="#222222"
)

any_press = TextStim(
        win=display,
        pos=(0,0),
        height=55,
        text="Press any key to begin",
        color="#AFAFAF",
        font="HelveticaNeue.ttc",
        wrapWidth=1800
    )

instruction_text = "Instructions \n\nIn this task you play a “gambling” game. \n\nYou need to choose 1 of 4 keys " \
           "(A,B,C or D) on the keyboard.\nEach time you can win some money but you may sometimes \nalso " \
           "have to pay a fee. After each trial, your total money will be \nadjusted.\n\nYou start with a loan of " \
           "€2000.\n\nGo on until it stops and see how much money you can make!\n\nPress any key to continue " \
           "and good luck!\n"

instruction = TextStim(
        win=display,
        pos=(0, 0),
        height=45,
        text=instruction_text,
        color="#AFAFAF",
        font="HelveticaNeue.ttc",
        wrapWidth=1800
    )

Q = TextStim(
        win=display,
        pos=(0,0),
        height=55,
        text="You have chosen to quit, Thanks for Participating!",
        color="#AFAFAF",
        font="HelveticaNeue.ttc",
        wrapWidth=1800
    )

finish = TextStim(
        win=display,
        pos=(0,0),
        height=55,
        text="You have completed the Iowa Gambling Task, Thanks for Participating!",
        color="#AFAFAF",
        font="HelveticaNeue.ttc",
        wrapWidth=1200
    )

A = TextStim(
            win=display,
            pos=(-427.5, -16.5),
            height=159,
            text="A",
            color="#581845",
            font="HelveticaNeue.ttc"
        )


B = TextStim(
            win=display,
            pos=(-156.5, -16.5),
            height=159,
            text="B",
            color="#900C3F",
            font="HelveticaNeue.ttc"
        )

C = TextStim(
            win=display,
            pos=(117.5, -16.5),
            height=159,
            text="C",
            color="#C70039",
            font="HelveticaNeue.ttc"
        )

D = TextStim(
            win=display,
            pos=(396.5,-16.5),
            height=159,
            text="D",
            color="#FF5733",
            font="HelveticaNeue.ttc"
        )


moneyDisplay = TextStim(
            win=display,
            pos=(-396.5, 335),
            height=60,
            text="Your Money: €2000",
            color="#AFAFAF",
            font="HelveticaNeue.ttc",
            wrapWidth=1800
        )

choose = TextStim(
            win=display,
            pos=(17, -153.5),
            height=55,
            text="Choose one of the options",
            color="#AFAFAF",
            font="HelveticaNeue.ttc",
            wrapWidth=1800
    )


win_box = psychopy.visual.Rect(
            win=display,
            pos=(-217,145),
            width=250,
            height=114,
            fillColor="#C70039"
        )

win_text = TextStim(
            win=display,
            pos=(-217,145),
            height=25,
            text="You won: €",
            color="white",
            font="HelveticaNeue.ttc",
            wrapWidth= 200
        )

lose_box = psychopy.visual.Rect(
            win=display,
            pos=(217, 145),
            width=250,
            height=114,
            fillColor="#00A3A1"
        )

lose_text = TextStim(
            win=display,
            pos=(217, 145),
            height=25,
            text="You lost: €",
            color="white",
            font="HelveticaNeue.ttc",
            wrapWidth=200
)


def runningTrial():
    A.draw()
    B.draw()
    C.draw()
    D.draw()
    moneyDisplay.draw()
    choose.draw()
    display.flip()

    char_pressed = []
    while "q" not in char_pressed:
        char_pressed = event.waitKeys()
        char_pressed = char_pressed[0]
        if char_pressed == "a":
            A.color = "#581845"
            B.color = "#900C3F"
            C.color = "#C70039"
            D.color = "#FF5733"

            A.color = "#000000"  # Feedback to the participant

            winningAmount = Deck_A.getWins()
            if winningAmount >= 0:
                win_text.text = "You won: €%d" %winningAmount
                losingAmount = Deck_A.getLoses()
                lose_text.text = "You lose: €%d"%losingAmount
                win_box.draw()
                win_text.draw()
                lose_box.draw()
                lose_text.draw()
            else:
                maxKey = P1.getMaxKeyPress()
                minKey = P1.getMinKeyPress()
                print(maxKey)
                print(minKey)

                finish.draw()
                display.flip()
                core.wait(3)
                display.close()

            P1.setWinnings(Deck_A)
            total = P1.getWinnings()
            moneyDisplay.text = "Your Money: €%d" % total

            P1.recordKeyPress("a")

            Deck_A.rowNumToRead += 1
        elif char_pressed == "b":
            A.color = "#581845"
            B.color = "#900C3F"
            C.color = "#C70039"
            D.color = "#FF5733"

            B.color = "#000000"  # Feedback to the participant

            winningAmount = Deck_B.getWins()
            if winningAmount >= 0:
                win_text.text = "You won: €%d" % winningAmount
                losingAmount = Deck_B.getLoses()
                lose_text.text = "You lose: €%d" % losingAmount
                win_box.draw()
                win_text.draw()
                lose_box.draw()
                lose_text.draw()
            else:
                maxKey = P1.getMaxKeyPress()
                minKey = P1.getMinKeyPress()
                print(maxKey)
                print(minKey)

                finish.draw()
                display.flip()
                core.wait(3)
                display.close()


            P1.setWinnings(Deck_B)
            total = P1.getWinnings()
            moneyDisplay.text = "Your Money: €%d" % total

            P1.recordKeyPress("b")

            Deck_B.rowNumToRead += 1

        elif char_pressed == "c":
            A.color = "#581845"
            B.color = "#900C3F"
            C.color = "#C70039"
            D.color = "#FF5733"

            C.color = "#000000"  # Feedback to the participant

            winningAmount = Deck_C.getWins()
            if winningAmount >= 0:
                win_text.text = "You won: €%d" % winningAmount
                losingAmount = Deck_C.getLoses()
                lose_text.text = "You lose: €%d" % losingAmount
                win_box.draw()
                win_text.draw()
                lose_box.draw()
                lose_text.draw()
            else:
                maxKey = P1.getMaxKeyPress()
                minKey = P1.getMinKeyPress()
                print(maxKey)
                print(minKey)

                finish.draw()
                display.flip()
                core.wait(3)
                display.close()

            P1.setWinnings(Deck_C)
            total = P1.getWinnings()
            moneyDisplay.text = "Your Money: €%d" % total

            P1.recordKeyPress("c")

            Deck_C.rowNumToRead += 1

        elif char_pressed == "d":
            A.color = "#581845"
            B.color = "#900C3F"
            C.color = "#C70039"
            D.color = "#FF5733"

            D.color = "#000000"  # Feedback to the participant

            winningAmount = Deck_D.getWins()
            if winningAmount >= 0:
                win_text.text = "You won: €%d" % winningAmount
                losingAmount = Deck_D.getLoses()
                lose_text.text = "You lose: €%d" % losingAmount
                win_box.draw()
                win_text.draw()
                lose_box.draw()
                lose_text.draw()
            else:
                maxKey = P1.getMaxKeyPress()
                minKey = P1.getMinKeyPress()
                print(maxKey)
                print(minKey)

                finish.draw()
                display.flip()
                core.wait(3)
                display.close()

            P1.setWinnings(Deck_D)
            total = P1.getWinnings()
            moneyDisplay.text = "Your Money: €%d" % total

            P1.recordKeyPress("d")

            Deck_D.rowNumToRead += 1

        A.draw()
        B.draw()
        C.draw()
        D.draw()
        moneyDisplay.draw()
        choose.draw()
        display.flip()

    Q.draw()
    display.flip()
    core.wait(3)
    display.close()


any_press.draw()
display.flip()
event.waitKeys()

instruction.draw()
display.flip()
event.waitKeys()


Deck_A = DeckFileManager("Decks.csv", "a")
Deck_B = DeckFileManager("Decks.csv", "b")
Deck_C = DeckFileManager("Decks.csv", "c")
Deck_D = DeckFileManager("Decks.csv", "d")

P1 = TrialParticipant("Lucy", "Edmunds")

runningTrial()

maxKey = P1.getMaxKeyPress()
minKey = P1.getMinKeyPress()
print("Maximum Key Presses:", maxKey)
print("Minimum Key Presses:", minKey)





