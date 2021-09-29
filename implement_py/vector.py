class vector :
	def __init__(self, name):
		self.data = []
		self.name = name
		self.size = 0
		self.capacity = capacity

	def size(self, size):
		self.size = size

	def capacity(self, capacity):
		self.capacity = capacity

	def is_empty(self):
		return(self.size == 0)

	def at(self, idx):
		if idx < self.size :
			# return() something
			pass
		else :
			### Raise an exception!
			pass 

	def push(self, item):
		if self.capacity <= self.size :
			self.capacity *= 2
		self.append(item)
		self.size += 1

	def insert(self, idx, item):
		if idx > self.size :
			### Raise an exception!
			pass
		else :
			if self.capacity <= self.size :
				self.capacity *=2
			self.size += 1
			pointer = self.size - 1
			while pointer > index :
				self[pointer] = self[pointer -1]
				pointer -= 1
			self[idx] = item

	def prepend(self, item):
		self.insert(0, item)

	def pop(self):
		self[size-1] = deleted
		self.size -= 1

	def delete(self, idx):
		if idx > self.size :
			### Raise an exception!
			pass
		else :
			pointer = self.size - 1
			while idx < pointer :
				self[idx] = self[idx+1]
			self[pointer] deleted

	def remove(self, item):
		- looks for value and removes index holding it (even if in multiple places)

	def find(self, item):
		- looks for value and returns first index with that value, -1 if not found

	def resize(self. new_capacity) : // private function
            - when you reach capacity, resize to double the size
            - when popping an item, if size is 1/4 of capacity, resize to half