import os
import sys
import shutil

#########################################################
if sys.platform == "linux" or sys.platform == "linux2":
   directory = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

elif sys.platform == "win32" or sys.platform == "win64":
    directory = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
else:
    print("mac detected ! You're already elegant")
#########################################################
if not os.path.exists(directory + "/elegantor"):
    os.makedirs(directory + "/elegantor")
    print("Directory [" + directory + "/elegantor] created")
########################################################
print("*"*40)
print("#" * 10+"\t"+"ELEGANTOR 0.1"+"\t"+"#"*10)

print("Pick an option : ")
inst = input(
    "[1] : To elegant content\t[2] : To delete content\t[3] : To list content\n")
#########################################################

insts = ["1", "2", "3"]
if inst not in insts:
    print("Wrong instruction.. exiting")

    sys.exit()
if inst == "1":
    for file in os.listdir(directory+"/elegantor"):

        filename = os.fsdecode(file)

        if filename != "":
            d = filename.split(".")[1]
            if not os.path.exists(directory + "/elegantor/"+d):
                os.makedirs(directory + "/elegantor/"+d)
            shutil.move(directory + "/elegantor/"+filename, directory + "/elegantor/" + d)
        else:    
            print("Folder is empty !")
            break
    print("Content is now elegant !")

elif inst == "2":
    check = input("Delete all content of this folder ? : <y/n>\n")
    if check == "y" or check == "Y":
        if os.listdir(directory + "/elegantor") != []:
            for file in os.listdir(directory + "/elegantor"):
                filename = os.fsdecode(file)
                if os.path.isfile(directory + "/elegantor/" + filename):
                    os.remove(directory + "/elegantor/" + filename)
                    print("File "+"["+filename+"] is deleted")
                else:
                    shutil.rmtree(directory + "/elegantor/" + filename)
                    print("Folder " + "[" + filename + "] is deleted")

        else:
            print("Folder is empty !")
            
    elif check == "n" or check == "N":
        print("Nothing has been deleted")
        sys.exit()

elif inst == "3":
    if os.listdir(directory + "/elegantor") != []:
        f = os.listdir(directory + "/elegantor")
        for _, content in enumerate(f, start=1):
            print({_:content})
    else:
        print("/elegantor is empty !")
            
###




