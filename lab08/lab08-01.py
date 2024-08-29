class Switch:
    def __init__(self, name: str, status: bool=False):
        self.name = name
        self.status = status

    def turn(self):
        self.status = not self.status

    def clone(self):
        return Switch(self.name+".copy", self.status)
    
    def get_name(self) -> str:
        return self.name
    
    def get_status(self) -> bool:
        return self.status
    
    def __str__(self) -> str:
        if(self.status):
            return f"switch({self.name}) is on"
        return f"switch({self.name}) is off"
    

class Light:
    def __init__(self, name: str, switch: Switch):
        self.name = name
        self.switch = switch

    def turn(self):
        self.switch.turn()

    def get_status(self) -> bool:
        return self.switch.get_status()
    
    def set_switch(self, new_switch: Switch):
        self.switch = new_switch

    def clone(self):
        return Light(self.name+".copy", self.switch.clone())
    
    def __str__(self) -> str:
        if(self.switch.status):
            return f"light({self.name}) with switch({self.switch.get_name()}) is on"
        return f"light({self.name}) with switch({self.switch.get_name()}) is off"


