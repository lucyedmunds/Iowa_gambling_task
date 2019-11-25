import csv

class FileManager:
  def __init__(self, file_path):
    self.__path = file_path
    self.__file_object = None

  def readRow(self, r):
    row_num = 0
    with open(self.__path) as csv_file:
      reader = csv.reader(csv_file)
      for row in reader:
        if row_num == r:
          return row
        row_num += 1
      return None # this means None will return, and will only happen if the row number is not in range.

  def countRow(self):
    row_total = -2 # to account for blank line and counting from 0
    with open(self.__path) as csv_file:
      reader = csv.reader(csv_file)
      for row in reader:
        row_total+=1
    return row_total


class DeckFileManager(FileManager):
  totalObjects = 0 # this variable counts the number of instances of the class created.

  def __init__(self,file_path, deck):
    # increments the totalDecks counter
    DeckFileManager.totalObjects +=1
    # inherits the init method from file manager
    super().__init__(file_path)

    self.deckNum = DeckFileManager.totalObjects
    self.rowNumToRead = 1
    self.deck = deck
    self.winLoseTup = None
  
  def __str__(self):
    return "Deck: %s \nDeck number: %d \nTotal Decks: %d " %(self.deck,self.deckNum,DeckFileManager.totalObjects)
  
  def getWinsLoses(self):
    # Checks if in range and returns a tuple of the win and lose amount for that deck at the current row. If out of range it returns -1.
        if self.rowNumToRead <= FileManager.countRow(self):
          rowList = FileManager.readRow(self, self.rowNumToRead)
          for i in rowList:
            if self.deck == "a":
              a = 0
              b = 1
            elif self.deck == "b":
              a = 2
              b = 3
            elif self.deck == "c":
              a = 4
              b = 5
            elif self.deck == "d":
              a = 6
              b = 7
          self.winLoseTup = (int(rowList[a]),int(rowList[b]))
          return self.winLoseTup
        else:
          return -1
      
  
  def getWins(self):
    winLose = DeckFileManager.getWinsLoses(self)
    if winLose == -1:
        return -1
    else:
      self.win = winLose[0]
      return self.win

  def getLoses(self):
    # This function returns the Loses as long as it is withing range
    winLose = DeckFileManager.getWinsLoses(self)
    if winLose == -1:
        return "Deck Finished"
    else:
      self.lose = winLose[1]
      return self.lose

    
  def getDeckNumber(self):
    return self.deckNum

  def getRowNumber(self):
    if self.rowNumToRead <= FileManager.countRow(self):
      return self.rowNumToRead
    else:
        return "Out of range"

  def setRowNumber(self, new_row_num):
    if new_row_num > 1 and new_row_num <= FileManager.countRow(self):
      if self.rowNumToRead < FileManager.countRow(self):
          self.rowNumToRead = new_row_num
    else:
        return "Out of range"
    