class vector :
	""" Trying to implement dynamically 
	sized array in python for practise"""
	def __init__(self, capacity = 4):
		self.size = 0
		self.capacity = capacity
		self.array = self.create_array(self.capacity)

	def create_array(self, capacity):
		return [None] * capacity

	def size(self, size):
		return(self.size)

	def capacity(self, capacity):
		self.capacity = capacity

	def is_empty(self):
		return(self.size == 0)

	def at(self, idx):
		if 0 <= idx < self.size :
			return(self.data[idx])
			pass
		else :
			raise IndexError("{0} is out of range! Please specify an index between {1} and {2}".format(idx, 0, self.size))

	def push(self, item):
		if self.capacity <= self.size :
			temp_capacity = 2 * self.capacity
			temp_array = self.create_array(temp_capacity)
			for i in range(self.size) :
				temp_array[i] = self.array[i]
			self.array = temp_array
			self.capacity = temp_capacity
		self.array[self.size] = item
		self.size += 1

	def insert(self, idx, item):
		if not (0 <= idx < self.size) :
			raise IndexError("{0} is out of range! Please specify an index between {1} and {2}".format(idx, 0, self.size))
		elif self.capacity <= self.size :
			temp_capacity = 2 * self.capacity
			temp_array = self.create_array(temp_capacity)
			for i in range(self.size) :
				temp_array[i] = self.array[i]
			self.array = temp_array
			self.capacity = temp_capacity
			
			pointer = self.size
			while pointer > idx :
				self.array[pointer] = self[pointer -1]
				pointer -= 1
			self.array[idx] = item
			self.size += 1

	def prepend(self, item):
		self.insert(0, item)

	def pop(self):
		if self.size > 0 :
			target = self.array[self.size-1]
			self.array[self.size-1] = None
			self.size -= 1
			if self.size/self.capacity < 0.25:
				temp_capacity = 0.5 * self.capacity
				temp_array = self.create_array(temp_capacity)
				for i in range(self.size):
					temp_array[i] = self.array[i]
				self.array = temp_array
				self.capacity = temp_capacity
			return(target)
		else:
			raise IndexError("There is nothing to remove!")


	def delete(self, idx):
		if not (0 <= idx < self.size) :
			raise IndexError("{0} is out of range! Please specify an index between {1} and {2}".format(idx, 0, self.size))
		else :
			self.size -= 1
			while idx < self.size:
				self.array[idx] = self.array[idx+1]
				idx += 1
			self.array[idx] = None
			if self.size/self.capacity < 0.25:
				temp_capacity = 0.5 * self.capacity
				temp_array = self.create_array(temp_capacity)
				for i in range(self.size):
					temp_array[i] = self.array[i]
				self.array = temp_array
				self.capacity = temp_capacity

	def remove(self, item):
        swap = []
        rem_rec = []
		for i in range(self.size()) :
            if self.array[i] != item:
                swap.append(self.array[i])
            
            else :
                rem_rec.append(i)
        
        self.array = swap
        del swap
        if len(rem_rec) > 0:
            print(f"{item} removed at indices {indices}")
        else :
            print(f"{item} was not present in the array")
        

	def find(self, item):
        for idx, val in enumerate(array) :
            if item == val:
                return(idx)
		return(-1)

	def resize(self, new_capacity) : // private function

            - when you reach capacity, resize to double the size
            - when popping an item, if size is 1/4 of capacity, resize to half