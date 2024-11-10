from logging import NullHandler     
def divide(x,y):    
  try: # Always Execute
    result=x/y # x=10, y=2
    print(result)
  except: # Alternate of try
    print("Error in try block")
  finally:
    print("End of division")

divide(10,2). 
divide(10,0)
