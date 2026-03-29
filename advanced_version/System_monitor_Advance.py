import psutil
import sys
import os
import time
import schedule # type: ignore

#--------------------------------------------------------------------
#   Function Name   : CreateLog
#   Description     : Creates log file and stores system & process info
#   Parameters      : Foldername (str)
#   Return          : None
#   Date            : 29/03/26
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
        os.mkdir(Foldername)
        print("Directory for log files gets successfully created")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    
    FileName = os.path.join(Foldername,"Marvellous_%s.log"%timestamp)
    print("Log File gets created with name : ",FileName)

    fobj = open(FileName , "w")

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
    
    Data = ProcessScan()

    for info in Data:
        fobj.write("PID:%s\n" %info.get("pid")) 
        fobj.write("Name:%s\n" %info.get("name")) 
        fobj.write("Username:%s\n" %info.get("username")) 
        fobj.write("Status:%s\n" %info.get("status")) 
        fobj.write("Start time :%s\n" %info.get("create_time")) 
        fobj.write("CPU:%% : %2f\n" %info.get("cpu_percent")) 
        fobj.write("Memory:%% : %2f\n" %info.get("memory_percent")) 
        fobj.write(Border+"\n")

    fobj.write(Border+"\n")
    fobj.write("--------------End of Log File---------------\n")
    fobj.write(Border+"\n")


#--------------------------------------------------------------------
#   Function Name   : ProcessScan
#   Description     : Collects detailed process information
#   Parameters      : None
#   Return          : list (process information dictionaries)
#   Date            : 29/03/26
#   Author          : Tanaya Vikram Gokhale
#--------------------------------------------------------------------
def ProcessScan():
    listprocess = []

    for proc in psutil.process_iter():
        try:
            proc.cpu_percent()
        except:
            pass

    time.sleep(0.2)

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=["pid", "name" ,"username", "status" , "create_time"])

            try:
                info["create_time"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(info["create_time"]))
            except:
                info["create_time"] = "NA"

            info["cpu_percent"] = proc.cpu_percent(None)
            info["memory_percent"] = proc.memory_percent()

            listprocess.append(info)

        except(psutil.NoSuchProcess , psutil.AccessDenied , psutil.ZombieProcess):
            pass

    return listprocess


#--------------------------------------------------------------------
#   Function Name   : main
#   Description     : Handles command-line arguments and scheduling
#   Parameters      : None
#   Return          : None
#   Date            : 29/03/26
#   Author          : Tanaya Vikram Gokhale
#--------------------------------------------------------------------
def main():

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