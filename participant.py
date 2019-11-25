from filemanager import *

class Participant():
    num_participants = 0

    def __init__(self, fName, lName):
        self.first_name = fName
        self.last_name = lName
        Participant.num_participants += 1  # Increments the participant number by 1
        self.participant_number = Participant.num_participants  # Assigns each object a participant number

    def __str__(self):
        # Returns a print friendly format.
        return "Participant Name: %s %s \nParticipant Number: %d" % (
            self.first_name, self.last_name, self.participant_number)

    def getFullName(self):
        # Returns participants full name.
        self.full_name = "%s %s" % (self.first_name, self.last_name)
        return self.full_name

    def setFullName(self, new_full_name):
        # Assigns a new participant name.
        self.new_full_name_list = new_full_name.split(" ")
        self.first_name = self.new_full_name_list[0]
        self.last_name = self.new_full_name_list[1]

    fullName = property(getFullName, setFullName)


class TrialParticipant(Participant):
    def __init__(self, fName, lName):
        super().__init__(fName, lName)
        self.first_name = fName
        self.last_name = lName
        self.__winnings = 2000
        self.participant_number = Participant.num_participants
        self.__trial_presses = {
            "a": 0,
            "b": 0,
            "c": 0,
            "d": 0
        }  # Protected attribute that contains the keys and the number of times they were pressed.

    def recordKeyPress(self, char_pressed):
        # Updates the trial press protected attribute and warns the user if an invalid character is pressed.
        if char_pressed in self.__trial_presses:
            self.__trial_presses[char_pressed] += 1
        elif char_pressed != 'q':
            print("You have entered an invalid character.")

    def get_presses(self):
        # Returns the trial press protected attribute.
        return self.__trial_presses

    def setWinnings(self, deck):
        # Calculates total won or lost with each key press and updates winnings overall.
        resultTup = DeckFileManager.getWinsLoses(deck)
        if resultTup != -1:
            result = resultTup[0] - resultTup[1]
            self.__winnings += result


    def getWinnings(self):
        # Returns the total with each character press.
        return self.__winnings

    winnings = property(getWinnings, setWinnings)

    def getKeyPressInfo(self):
        # Prints a list of tuples of keys and number of presses.
        press_dict = TrialParticipant.get_presses(self)
        self.key_press_list = [(t0, t1) for t0, t1 in press_dict.items()]
        return self.key_press_list

    def getMaxKeyPress(self):
        # Returns a list of tuples of the key most pressed.
        maxKey = [("a", 0)]
        key_press_list = TrialParticipant.getKeyPressInfo(self)
        for i in key_press_list:
            if i[1] > maxKey[0][1]:
                maxKey = [(i)]
            elif i[1] == maxKey[0][1]:
                maxKey.append(i)
        return maxKey

    def getMinKeyPress(self):
        # Returns a list of tuples of the key least pressed.
        minKey = [("a", 1000)]
        key_press_list = TrialParticipant.getKeyPressInfo(self)
        for i in key_press_list:
            if i[1] < minKey[0][1]:
                minKey = [(i)]
            elif i[1] == minKey[0][1]:
                minKey.append(i)
        return minKey
