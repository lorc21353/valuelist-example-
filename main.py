valuelist = ["valone", "valtwo"]

def valcheck():
  global valuelist 

  while True:
    try:
      userval = str(input("Enter the name of the value that you wish to check if it is in the array: ")).lower()
      break
    except:
      print("error")

  if userval in valuelist:
    print(userval, "is in valuelist")
  else:
    print(userval, "is out of valuelist")




def valadd(question, adrem, index, valtype):
  global valuelist
  
  if adrem == "add":
    while True:
      try:
        if index == None:
          if valtype == "str" or valtype == None:
            val = input(question)
            valuelist.append(val)
            
          if valtype == "int":
            val = int(input(question))
            valuelist.append(val)
  
          if valtype == "float":
            val = float(input(question))
            valuelist.append(val)

          if index != None:
            if valtype == "str" or valtype == None:
              val = input(question)
              valuelist.insert(index, val)
              
            if valtype == "int":
              val = int(input(question))
              valuelist.insert(index, val)
    
            if valtype == "float":
              val = float(input(question))
              valuelist.insert(index, val)
        break
      except:
        print("err invalid value")

  if adrem == "rem":
      try:
        del(valuelist[index])
      except:
        print("err invalid value")
        
valadd("please enter a value to put in the array: ", "add", None, None)
valcheck()
print(valuelist)
