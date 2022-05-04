##########################################################################
##
##  Prasad R. Bhosale
##  Wednesday (4/05/2022)
##  day_30__start
##
##########################################################################

#FileNotFound

try:
    file = open("a_file.txt")
    a_dictionary = {"key" : "value"}
    print(a_dictionary["cdafdsa"])
except FileNotFoundError:
    file = open("a_file.txt","w")
    file.write("Something")

except KeyError as error_msg:
    print(f"That key{error_msg} does not exist.")

else:
    content = file.read()
    print(content)
# finally:
#     file.close()
#     print("This is final line.file is close now")

finally:
    raise KeyError

