class RingBuffer:
    def __init__(self, capacity):
        self.capacity: int = capacity #initialize 
        self.storage = [] #created storage 
        self.current_location = 0 #created index with value of 0

    def append(self, item):
        if self.current_location >= len(self.storage):
            self.storage.append(item) # stores new item when there is space available in capacity
        else: #else if we are at or over capacity
            self.storage[self.current_location] = item #overwrite existing item begining at index
        
        self.current_location += 1 # move index to next item in list
        if self.current_location == self.capacity: # check if reached max capacity
            self.current_location = 0 #if so reset to 0

    def get(self):
        return self.storage