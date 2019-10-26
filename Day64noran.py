#Python Try-Except
#The try block will generate an error, because x is not defined:
try:
    print(x)
except:
    print("An exception occured")
#The try block will generate a Nameerror, because y is not defined:
try:
    print(y)
except NameError:
    print("Variable y is not defined")
except:
    print("Somthing else went wrong")
#The try block dosen't raise any errors,so the else block is excuted:
try:
    print("Hello")
except:
    print("Somthing went wrong")
else:
    print("nothing went wrong")
#The finally block gets excuted no matter if the try block raises any errors or not:
try:
    print(z)
except:
    print("something went wrong")
finally:
    print("The 'try except' is finished")