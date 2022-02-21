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
        
        self.readCurrent = ""
        
        
    def loop (self):
        while True:
            if not self.check_connect(): 
                self.serial_reconnect()
                    
            try:
                
                if self.threadRun:
                    # 코드를 넣어주세요
                    self.serial_read()
                    self.ser.write('hi\n'.encode())
                    
                    print(self.readCurrent)
                    
                
                else:
                    print(self.port+" serial_thread stop...")
                    print("waiting thread restart...")
                    while not self.threadRun: pass
            except: pass
                
                
    def serial_read (self):
        if self.ser.readable():
            time.sleep(0.03)
            data = self.ser.read_all().decode()[:-2]
            if data != "": 
                self.readCurrent = data
            

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


    def serial_disconnect (self):
        self.ser.close()
        self.ser = None
        
        
    def serial_reconnect (self): 
        try: 
            self.ser = serial.Serial(self.port, self.baud)
            print("reconnect ser "+self.port)
        except: pass
        
        
    
        


if __name__ == "__main__":
    import time
    test = Serial_thread()
    test.threadRun = True
    time.sleep(5)
    test.serial_disconnect()
    test.threadRun = False
    
    
    
