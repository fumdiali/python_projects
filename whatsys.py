'''prototype of a program that outputs details of 
   operating systems. It utilizes the (platform module).
   it is hoped that a version for smartphones
   can evolve from this.'''

import platform

print("Some details about the system you run..")
print()
print("\t\tUser Details: \n \t\t",platform.uname())
print()
print()
print("\tOperating System: \n \t\t",platform.system())
print("\tVersion info(detailed with TimeStamp): \n \t\t",platform.version())
print()
print("\tMachine info: \n \t\t",platform.machine())
print("\tYour Processor: \n \t\t",platform.processor())
print()
print("\tSystem Architecture: \n \t\t",platform.architecture())

print("\t\tWritten by Patrick C. Diali 2017")
