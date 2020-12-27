
import time

x={} # dictionary to store data

#create operation
def create(key,value,timeout=0):
    if key in x:
        print("error: this key already exists") #error message1
    else:
        if(key.isalpha()):
            if len(x)<(1024*1020*1024) and value<=(16*1024*1024):
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: 
                    x[key]=l
            else:
                print("error: Memory limit exceeded!! ")#error message2
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")#error message3

#read operation           
def read(key):
    if key not in x:
        print("error: given key does not exist in database. Please enter a valid key") #error message4
    else:
        b=x[key]
        if b[1]!=0:
            if time.time()<b[1]:
                stri=str(key)+":"+str(b[0]) 
                return stri
            else:
                print("error: time-to-live of",key,"has expired") #error message5
        else:
            stri=str(key)+":"+str(b[0])
            return stri

#delete operation
def delete(key):
    if key not in x:
        print("error: given key does not exist in database. Please enter a valid key") #error message4
    else:
        b=x[key]
        if b[1]!=0:
            if time.time()<b[1]:
                del x[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") #error message5
        else:
            del x[key]
            print("key is successfully deleted")
