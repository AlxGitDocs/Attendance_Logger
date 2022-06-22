from time import sleep

# Modules
import Modules.logger as logger
# import Modules.display as display #TODO only be run while connected to the PI

# Coded in Python 3.10
# Install Pip3 to get the requests dependancy
# Example: sudo apt-get -y install python3-pip python3 && pip3 install redis

# Checks for the RFID stags that are set for this project
def checkRFData(data):
  if data == ("02004819B2E1") or data == ("0D004EC21091"): #TODO add card ID
    # display.createSound() #TODO only be run while connected to the PI
    return True
  else:
    return False

# In case of restart or power loss, save current status
def checkStatus():
  # False if timer not running
  # True if timer is running
  # Status written on database
  return

if __name__ == "__main__":

  #display.welcomeUser() #TODO only be run while connected to the PI
  sleep(0.5)

  # Startin the loop when program starts up
  #while True:

  status = checkStatus()
  #print(f"{status}")

  #data = display.read_rfid.read_rfid() #TODO only be run while connected to the PI
  #isRead = checkRFData(data)
  #print(f"{data} + {isRead}")

  isRead = True #TODO dev only

  if isRead:
    
    # Do the rest
    
    logger.logger().start()

    #sleep(5) # Wait until it reads from database again

  else:
    # incorrect read
    print("error reading")
    
    

    




