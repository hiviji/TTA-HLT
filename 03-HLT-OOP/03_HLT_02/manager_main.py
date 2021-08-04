from employee import Employee
from manager import Manager
from developer import Developer

manager1 = Manager("pm1",500)

dev1 = Developer("dev1", 750, "Py")
dev2 = Developer("dev2", 750, "Py")
dev3 = Developer("dev3", 750, "Java")
dev4 = Developer("dev4", 750, "Java")
dev5 = Developer("dev5", 750, "Py")

manager1.add_staff_member(dev1)
manager1.add_staff_member(dev2)
manager1.add_staff_member(dev3)
manager1.add_staff_member(dev4)
manager1.add_staff_member(dev5)

print(manager1)

num_dev = manager1.count_all_devs()
print (f"\n Number of Developers :{num_dev}")

num_java = manager1.count_all_java_devs()
print (f"\n Number of Java Developers :{num_java}")

java_dev_list = manager1.java_devs()

for d in java_dev_list:
    print( f" Java Developers: {d}")

num_py = manager1.count_all_py_devs()
print (f"\n Number of Python Developers :{num_py}")

py_dev_list = manager1.py_devs()

for d in py_dev_list:
    print( f" Python Developers: {d}")