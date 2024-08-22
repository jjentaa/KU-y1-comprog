class Radio:
    def __init__(self, mode: str="FM", frequency: float=87.5):
        self.mode = mode
        self.frequency = frequency

    def get_mode(self) -> str:
        return self.mode
    
    def get_frequency(self) -> float:
        return self.frequency
    
    def set_mode(self, mode: str):
        self.mode = mode

        if(self.mode == "FM"):
            self.frequency = 87.5
        else:
            self.frequency = 150

    def set_frequency(self, frequency):
        if(self.mode == "FM"):
            if(87.5 <= frequency <= 108):
                self.frequency = frequency
            
        else:
            if(150 <= frequency <= 280):
                self.frequency = frequency
    
    def adjust_frequency(self, frequency) -> bool:
        new_freq = self.frequency+frequency

        if(self.mode == "FM"):
            if(87.5 <= new_freq <= 108):
                self.frequency = new_freq
                return True
            
            else:
                return False
            
        else:
            if(150 <= new_freq <= 280):
                self.frequency = new_freq
                return True
            
            else:
                return False

    def __str__(self) -> str:
        if(self.mode == "FM"):
            return f"{self.mode} Radio: {self.frequency:.1f} MHz"
        else:
            return f"{self.mode} Radio: {self.frequency:.1f} kHz"
    
############## test case for Radio class
def print_des(a):
    print("mode:", a.get_mode())
    print("freq:", a.get_frequency())
    print("str:", a)
    print("")


def do_set_freq(a, fre):
    a.set_frequency(fre)
    print(f"set_frequency({fre})")
    print_des(a)


def do_set_mode(a, mode):
    a.set_mode(mode)
    print(f"set_mode({mode})")
    print_des(a)


def do_adjust(a, adjust):
    b = a.adjust_frequency(adjust)
    print(f"adjust({adjust})")
    print(f"return: {b}")
    print_des(a)
    return b


a = Radio()
b = False
print("Init")
print_des(a)
a.set_mode("AM")
print("a.set_mode(AM)")
print_des(a)
do_set_freq(a, 149.9)
do_set_freq(a, 270)
do_set_freq(a, 280.0001)
do_set_freq(a, 280)
do_set_mode(a, "FM")
do_set_freq(a, 10)
do_set_freq(a, 107.9)
do_set_freq(a, 108.1)
do_set_freq(a, 108)
do_set_freq(a, 87.5)
do_adjust(a, 0.5)
do_adjust(a, -5)
do_adjust(a, 19.9)
do_adjust(a, 0.1)
do_adjust(a, 1)
do_adjust(a, -20.5)
do_adjust(a, 0.0001)
do_set_mode(a, "AM")
do_adjust(a, -0.001)
do_adjust(a, 100.51)
do_adjust(a, -0.51)
do_adjust(a, 30)
do_adjust(a, 20.5)
do_adjust(a, -2000)
do_adjust(a, -130)

