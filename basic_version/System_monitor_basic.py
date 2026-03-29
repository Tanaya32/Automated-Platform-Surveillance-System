import psutil
import sys
import os
import time
import schedule # type: ignore

#--------------------------------------------------------------------
#   Function Name   : CreateLog
#   Description     : Creates log file and stores system information
#   Parameters      : Foldername (str)
#   Return          : None
#   Date            : 28/03/26
#   Author          : Tanaya Vikram Gokhale
#--------------------------------------------------------------------
def CreateLog(Foldername):
    Border = "-" * 50
    Ret = False

    Ret = os.path.exists(Foldername)

    if(Ret == True):
        Ret =os.path.isdir(Foldername)
        if(Ret == False):
            print("Unable to create Folder")
            return
        
    else:
        os.mkdir(Foldername)  # creates folder/ directory
        print("Directory for log files gets successfully created")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")        #strftime- makes string for time
    
    # Naming filename
    FileName = os.path.join(Foldername,"Marvellous_%s.log"%timestamp)
    print("Log File gets created with name : ",FileName)

    fobj = open(FileName , "w")

    # writing inside the file
    fobj.write(Border+"\n")
    fobj.write("-----Marvellous Platform Surveillance System------\n")
    fobj.write("Log Created at : "+ time.ctime() + "\n")
    fobj.write(Border+"\n\n")

    fobj.write("---------------System Report----------------\n")

    fobj.write("CPU usage : %s %%\n" %psutil.cpu_percent())
    fobj.write(Border+"\n")

    mem = psutil.virtual_memory()
    fobj.write("Ram usage : %s %%\n" %mem.percent)
    fobj.write(Border+"\n")

    fobj.write("\nDisk Usage Report\n")
    fobj.write(Border+"\n")

    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            fobj.write("%s -> %s %% used\n" %(part.mountpoint , usage.percent))
        except:
            pass

    fobj.write(Border+"\n")

    net = psutil.net_io_counters()
    fobj.write("\nNetwork Usage Report\n")
    fobj.write("Sent : %.2f MB\n" % (net.bytes_sent / (1024 * 1024)))
    fobj.write("Recv : %.2f MB\n" % (net.bytes_recv / (1024 * 1024)))
    fobj.write(Border+"\n")
    
    fobj.write(Border+"\n")
    fobj.write("--------------End of Log File---------------\n")
    fobj.write(Border+"\n")


#--------------------------------------------------------------------
#   Function Name   : ProcessScan
#   Description     : Displays running processes with PID, name, status
#   Parameters      : None
#   Return          : None
#   Date            : 28/03/26
#   Author          : Tanaya Vikram Gokhale
#--------------------------------------------------------------------
def ProcessScan():
    print("Process Scan Report ")

    for proc in psutil.process_iter(attrs=["pid", "name" , "status"]):
        info = proc.info
        print(info["pid"] , info["name"] , info["status"])
    

#--------------------------------------------------------------------
#   Function Name   : main
#   Description     : Entry point of the program and handles arguments & scheduling
#   Parameters      : None
#   Return          : None
#   Date            : 28/03/26
#   Author          : Tanaya Vikram Gokhale
#--------------------------------------------------------------------
def main():

    ProcessScan()

    return

    Border = "-" * 50
    print(Border)
    print("-----Marvellous Platform Surveillance System------")
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1]== "--H"):
            print("This script is used to :")
            print("1 : Create automatic logs")
            print("2 : Executes periodically")
            print("3 : Sends mail with the log")
            print("4 : Store information about processess")
            print("5 : Store info about CPU")
            print("6 : Store info about RAM usage")
            print("7 : Store info about secondary storage(HDD)")

        elif(sys.argv[1] == "--u" or sys.argv[1]== "--U"):
            print("Use the Automation script as ")
            print("ScriptName.py  TimeInterval  DirectoryName")
            print("Time interval : Time in minutes for periodic scheduling")
            print("DirectoryName : Name of Directory to create auto logs")

        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")

    elif(len(sys.argv) == 3):
        print("Inside projects logic")
        print("Time interval : ", sys.argv[1])
        print("DirectoryName : ",sys.argv[2])

        schedule.every(int(sys.argv[1])).minutes.do(CreateLog, sys.argv[2])

        print("Platform Surveillance System started successfully")
        print("Directory created with name : ",sys.argv[2])
        print("Time interval in minutes : ",sys.argv[1])
        print("Press Ctrl + C to stop execution")

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid Number of command line arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details")

    print(Border)
    print("-----------Thankyou for using our script----------")
    print(Border)


if __name__ =="__main__":
    main()