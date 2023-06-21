import sys

try:
    with open("Valery_test.txt", "r") as f:
        file_content = f.read()
        print("read file " + "Valery_test.txt")
except IOError as e:
   print("I/O error({0}): {1}".format(e.errno, e.strerror))
except: #handle other exceptions such as attribute errors
   print("Unexpected error:", sys.exc_info()[0])
print("done")