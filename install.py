# this script would serve as the main configuration install for eliteTrader projects
import shutil
import os

def main():
    print "Start copying configuration......"
    source = "config"
    dest = "/local/config"
    exist = os.path.exists(dest)
    
    # if dest exists delete it first
    if exist:
        shutil.rmtree(dest)
        print "Previously existed path has been deleted!"
    shutil.copytree(source, dest)
    print "Copy is succeeded."

if __name__ == "__main__":
    main()

