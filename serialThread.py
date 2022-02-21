import threading
import serial

class Serial_thread:
    def __init__(self):
        self.ser = None
        self.baud = 9600
        self.port = None
        self.get_serial()
        
        self.threadRun = True
        self.thread = threading.Thread(target = self.loop)
        self.thread.start()
        
        
        
    def get_serial(self):
        for i in range(3,50):
            try: 
                self.ser = serial.Serial('COM'+str(i), self.baud)
                self.port = 'COM'+str(i)
                print("connect ser "+self.port)
                return
            except: pass
        print("not conneting serial....")
        
        
    def check_connect(self):
        try: self.ser.inWaiting()
        except: 
            if self.ser != None: 
                print("ser "+self.port+" disconnect")
                print("trying... reconnect")
            self.ser = None
            return False
        return True


    def reconnect (self): 
        try: 
            self.ser = serial.Serial(self.port, self.baud)
            print("reconnect ser "+self.port)
        except: pass
        
        
    def loop (self):
        while True:
            if self.threadRun:
                if not self.check_connect():
                    self.reconnect()
            
            else:
                print(self.port+" serial_thread stop...")
                print("waiting restart...")
                while not self.threadRun:
                    pass
        

import time
if __name__ == "__main__":
    test = Serial_thread()
    test.threadRun = True
    time.sleep(5)
    test.threadRun = False
    
    
