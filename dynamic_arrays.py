import ctypes
class DynamicArrays:

  def __init__(self):

    self.size = 0;
    self.capacity = 1;
    self._A = self._make_array(self.capacity);
  
  def __len__(self):
    return self.size
    
  def ___str__(self):
    return self.capacity

  def append(self,element):
    if(self.size == self.capacity):
      new_array = self._make_array(2*self.capacity)
      for i in range(self.size):
        new_array[i] = self._A[i]
      self._A = new_array
      self.capacity = 2*self.capacity
    self._A[self.size] = element
    self.size +=1
 

  def _make_array(self,c):
    return (c*ctypes.py_object)( )
  
  def _get(self,i):
    if i<0 or i>=self.size:
      raise IndexError("Invalid index")
    return self._A[i]

  def _set(self,i,element):
    if i<0 or i>=self.size:
      raise IndexError("Invalid index")
    self._A[i] = element