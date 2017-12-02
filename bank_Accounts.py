class Bank_accounts:

	def __init__(self,ID, name, acountBallance = 0):
		self._IDcode = ID
		self._Name = name
		self.setBallance(acountBallance)

	def getID(self):
		return self._IDcode

	def getName(self):
		return self._Name

	def getBallance(self):
		return self._ballance

	def setBallance(self, acountBallance):
		self._ballance = acountBallance

class Node:

	def __init__(self, data):
		self._data =data
		self.setNext(None)
		self.setPrev(None)

	def getData(self):
		return self._data

	def getNext (self):
		return self._next

	def getPrev(self):
		return self._prev

	def setNext(self, n):
		self._next = n

	def setPrev(self, p):
		self._prev = p

class LinkedList:

	def __init__(self):
		self._head = None


	def add(self, account):
		newnode = Node(account)
		if self._head == None:
			self._head =  newnode
		else:
			newnode.setNext(self._head)
			self._head.setPrev(newnode)
			self._head = newnode

	def displayAll(self):
		iterator =self._head
		while iterator != None:
			print("Client ID: ", iterator.getData().getID())
			print("Clinet Name: ", iterator.getData().getName())
			print("Account balance: ", iterator.getData().getBallance())
			print("----------------------------------------------------")

			iterator = iterator.getNext()

	def delteAccount(self,IDcode):
		iterator = self._head
		while iterator != None:
			if iterator.getData().getID() == IDcode:
				if iterator.getPrev() != None:
					iterator.getPrev().setNext(iterator.getNext())
				if iterator.getNext() != None:
					iterator.getNext().setPrev(iterator.getPrev())
				if iterator == self._head:
					self._head = iterator.getNext()
			iterator = iterator.getNext()


	def deposit(self,IDcode, amount):
		iterator = self._head
		while iterator != None:
			if iterator.getData().getID() == IDcode:
				if amount < 0:
					print("Ivalid deposit amount")
				else:
					iterator.getData().setBallance(iterator.getData().getBallance() + amount)
					print("Deposit succesfull")
					print("Account balance: ", iterator.getData().getBallance())
			else:
				print("Wrong ID. Not Found.")
				break
			iterator = iterator.getNext()
			


	def withdraw(self, IDcode, amount):
		iterator = self._head
		while iterator != None:
			if iterator.getData().getID() == IDcode:
				if iterator.getData().getBallance() == 0:
					print("You do not have any deposit money to withdraw.")
				elif iterator.getData().getBallance() - amount < 0:
					print("The ammount to withdraw is ivalid")
					print("Account balance: ", iterator.getData().getBallance())
				else:
					iterator.getData().setBallance(iterator.getData().getBallance() - amount)
					print("Withdraw succesfull.")
					print("Account balance: ", iterator.getData().getBallance())
			else:
				print("Wrong ID. Not Found.")
				break
			iterator = iterator.getNext()






account = LinkedList()

account.add(Bank_accounts(1, "James"))
account.add(Bank_accounts(2, "George"))
account.add(Bank_accounts(3, "Nick", 200000))
account.add(Bank_accounts(4, "Irdi", 90000))

account.delteAccount(4)
account.delteAccount(2)

#account.deposit(5, 100)
account.displayAll()
#account.withdraw(1,50)


