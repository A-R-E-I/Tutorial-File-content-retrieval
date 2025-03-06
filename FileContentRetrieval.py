import os.path
import sys
from os import path

msg = ["New file name:","Existing file name:"];

def main():
    AskInfo();

def AskInfo():
    checkpoint="askinfo"
    whichoption= str(input("1-Create new file\n"
                           "2-Search for an existing file\n"
                           "3-exit\n"
                           "Select an option by typing 1, 2, or 3: "));
    CheckInfo(whichoption, checkpoint);

def CheckInfo(optionwhich,pointcheck):
    global whichfilename;
    match(pointcheck):
        case "askinfo":
            optwhich = ord(optionwhich);
            if(optwhich < 49 or optwhich > 51):
                print("Incorrect response.")
                AskInfo();
            else:
                match(optionwhich):
                    case "1":
                        whichfilename = str(input(msg[0]));
                    case "2":
                        whichfilename = str(input(msg[1]));
                    case "3":
                        print("Goodbye");
                        sys.exit();

                whichfilename = whichfilename + ".doc";
                FileConnectivity();
        case default:
            print("Houston...we have a problem");
            sys.exit();

def FileConnectivity():
    global adminfile;
    fileDir = os.path.dirname(os.path.realpath("__file__"));
    fileexist = bool(path.exists(whichfilename));

    if(fileexist == True):
        print("File exist");
        adminfile = open(whichfilename,"r+");
        RetrieveFromFile()
    else:
        YesNo = str(input("The file name you entered does not exist. Do you want to create it(Y/N)?"));
        if(YesNo.upper() == "Y"):
            adminfile = open(whichfilename,"x");
            print("text file created")
            CollectInfo();
            ifstart = str(input("Would you like to performanother action, (Y)es or (N)o?")).upper();
            if(ifstart == "Y"):
                Askinfo();
            else:
                print("Thank you");
                sys.exit();
        else:    
            adminfile.close();
            sys.exit();

def CollectInfo():
    print("Let's begin by creating a username and password for your file.");
    username = str(input("Username: "));
    password = str(input("Password: "));
    WriteToFile(username,password,whichfilename);

def WriteToFile(name,passwd,thefile):
    adminfile = open(thefile,"w");
    adminfile.write(name + "," + passwd);
    adminfile.close();

def RetrieveFromFile():
    adminvalue = adminfile.read().split(",")
    adminfile.close();

    usertxt = adminvalue[0].strip();
    userpwd = adminvalue[1].strip();
    print(usertxt + userpwd);

if __name__ == "__main__":
    main();
