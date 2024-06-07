#Inheritance #Polymorphism #Encapsulation
class University:
  chancellor="Mohammed Shahabuddin"

  def set_info(self,univ_name,univ_location,univ_type,univ_vc_name):
    self.univ_name= univ_name              #Public Attribute
    self._univ_location= univ_location    #Protected Atribute
    self.__univ_type= univ_type           #Private Attribute
    self.univ_vc_name= univ_vc_name

  def get_info(self):
    print(f"University Name:{self.univ_name} \n University Location: {self.univ_location}")


class Department(University):
  def __init__(self, dept_id, dept_name, dept_head):
    self.dept_id=dept_id
    self.dept_name=dept_name
    self.dept_head=dept_head
    print(f"{dept_name} department information is sucessfully inserted")

  def viewCampus(self):
    #print("\nOur Campus is Very Fucking Good..........")
    print("Method is not overridden\n")



  def registration_req(self,student_id,dept,term, delay):
      self.student_id=student_id
      if (delay==True):
        print(f"Hi {student_id}, Your registration is successfull ")

      else:
        print(f"Hi {student_id}, Your registration will be done by dept or advisor")


#University Class
obj1=University()
print(obj1.chancellor)


#Department Class
obj2=Department("15","CSE", "SRHN")
obj2.viewCampus()
obj2.registration_req("221-15-4997", "CSE", "Fall 2024",False)
obj2.registration_req("221-15-4998", "CSE", "Fall 2024",True)

from logging import NullHandler

"""def divide(x,y):
  try: # Always Execute
    result=x/y # x=10, y=2
    print(result)
  except: # Alternate of try
    print("Error in try block")
  finally:
    print("End of division")

divide(10,2)
divide(10,0)"""



