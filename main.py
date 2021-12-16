class stack:
  mystack = []
  def __init__(self):
    self

    
  
  def isEmpty(self):
    if len(self.mystack) != 0:
      return True
    else:
      return False

  def push(self, elem):
    
    self.mystack.append(elem)
    

  def pop(self):
    self.mystack.pop()
    if len(self.mystack) != 0:
      return self.mystack[-1]
      
        

  def peek(self):
    return self.mystack[-1]

  def size(self):
    return len(self.mystack)

str_1 = '[([])((([[[]]])))]{()}'
str_2 = '(((([{}]))))'
str_3 = '{{[(])]}}'


def check(str_):  
  list_ = list(str_)  
  for el in list_:
    if el == '(' or el =='[' or el =='{':      
      stack().push(el)      
    else:
      try:      
        stack().pop()
      except LookupError:
        return 'Несбалансированно'

  if stack().isEmpty() == False:
    return 'Сбалансированно'
  else:
    return 'Несбалансированно'     
  
print(check(str_1))
print(check(str_2))
print(check(str_3))
