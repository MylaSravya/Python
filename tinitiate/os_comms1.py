import os

# String to store the OS command
OScommand = "echo Tinitiate.com"

# Run the OS command using system function
os.system(OScommand)


import subprocess
subprocess.call(['echo','Hello Tinitiate'], shell=True)

(SDOut,SDErr) = subprocess.Popen( ["C:/Python311/python.exe", "e:/Training/Dec2022_precision/print1.py"]
                                 ,stdout=subprocess.PIPE
                                 ,stderr=subprocess.PIPE
                                 ,shell=True).communicate()

# Print the SDOut and SDErr variables
print(SDOut)
print(SDErr)