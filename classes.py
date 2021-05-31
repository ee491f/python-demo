class SimpleClass():
  class_variable = "any number"

  def __init__(self, first_argument):
    self.instance_variable = first_argument
  
  def classMethod():
    print("class method called")

  def instanceMethod(self):
    print("from method: " + self.instance_variable)
    print(self.class_variable)
    return "return value"

  def modifyInstanceVariable(self, new_argument):
    self.instance_variable = new_argument

  def modifyClassVariable(self, new_argument):
    class_variable = new_argument

print(SimpleClass("passed in").instanceMethod())

class_instance1 = SimpleClass("one")
class_instance2 = SimpleClass("two")
SimpleClass.classMethod()
# class_instance1.classMethod() # calling a class method from a class instance will not work

class_instance1.instanceMethod()
class_instance2.instanceMethod()

class_instance1.modifyInstanceVariable("new one")
class_instance2.modifyInstanceVariable("new two")

class_instance1.instanceMethod()
class_instance2.instanceMethod()

class_instance1.modifyClassVariable("new any number")
class_instance1.instanceMethod()
class_instance2.instanceMethod()
