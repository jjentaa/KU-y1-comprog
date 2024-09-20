def readMenu(fn='CoffeeMenu01.txt'): # นำฟังชันนี้ไปใช้อ่านเมนูกาแฟ โดยไม่ต้องส่งซ้ำ
    with open(fn) as fd:
        return fd.read()
    
class CupOfCoffee:
    def __init__(self, coffee_type, drinking_type, price):
        self.coffee_type = coffee_type
        self.drinking_type = drinking_type
        self.add_on = []
        self.price = price

    def set_add_on(self, one_add_on, one_add_on_price):
        if(self.add_on == []):
            self.add_on = [one_add_on]
        else:
            self.add_on.append(one_add_on)

        self.price += one_add_on_price

    def __repr__(self):
        if(self.add_on==[]):
            return f" This cup is {self.drinking_type.lower()} {self.coffee_type} with no add on, {self.price} baht."
        elif(len(self.add_on)==1):
            return  f" This cup is {self.drinking_type.lower()} {self.coffee_type} with {self.add_on[0]}, {self.price} baht."
        elif(len(self.add_on)==2):
            return  f" This cup is {self.drinking_type.lower()} {self.coffee_type} with {self.add_on[0]} and {self.add_on[1]}, {self.price} baht."
        elif(len(self.add_on)>1):
            txt = ""
            for e in range(len(self.add_on)-1):
                txt+=self.add_on[e]+", "
            return f' This cup is {self.drinking_type.lower()} {self.coffee_type} with {txt[0:-2]} and {self.add_on[-1]}, {self.price} baht.'

class CustomerBill:
    def __init__(self, name):
        self.name = name
        self.ordered_coffee = []

    def add_ordered_coffee(self, aCupOfCoffeeObject):
        self.ordered_coffee.append(aCupOfCoffeeObject)
    
    def receipt(self):
        def insert_commas_recursive(num_str, counter):
            if len(num_str) <= 3:
                return num_str
            else:
                result = insert_commas_recursive(num_str[:-3], counter+3)
                return result + ',' + num_str[-3:]
        p = 0
        txt = "++++++++++++++++++++++++++++++++\n"
        txt += "      CPE38 **StarBUG Cafe    \n"
        text = f"Kun {self.name}'s Receipt"
        space = (32-len(text))//2
        txt += " "*space+text+" "*space+"\n"
        txt += "++++++++++++++++++++++++++++++++\n"
        txt += "Description                Price\n"

        for i in self.ordered_coffee:
            d = f"{i.drinking_type} {i.coffee_type}"
            txt+=f"{d:<29}{i.price:>3}\n"
            p+= i.price
            if(i.add_on!="no"):
                for j in i.add_on:
                    txt+=f" + {j}\n"
            if(len(self.ordered_coffee)>1):
                txt+="\n"

        pp = insert_commas_recursive(str(p), 0)
        if(len(self.ordered_coffee)>1):
            txt +=f"Total{pp:>27}\n"
        else:
            txt +=f"\nTotal{pp:>27}\n"

        txt += "++++++++++++++++++++++++++++++++\n"
        txt += " Thank you, please come back :) \n"
        txt += "++++++++++++++++++++++++++++++++\n"

        return txt
    
def insert_commas_recursive(num_str, counter):
    if len(num_str) <= 3:
        return num_str
    else:
        result = insert_commas_recursive(num_str[:-3], counter+3)
        return result + ',' + num_str[-3:]

def print_menu():
    global coffee_menu_CSV, add_on_menu_CSV

    menu = coffee_menu_CSV.split("\n")
    add_menu = add_on_menu_CSV.split("\n")


    print("Welcome to CPE38 **StarBUG Cafe!")
    print("+++++++++++++ MENU +++++++++++++")
    print("Coffee         Hot  Cold  Frappe")
    
    idx = 1
    for i in range(len(menu)):
        pivot = menu[i]
        if(pivot == "" or pivot==" "):
            continue
        pivot = pivot.strip()
        ls = pivot.split(",")
        txt = f"{idx}.{ls[0]:<13}{int(ls[1]):>3}{int(ls[2]):>6}{int(ls[3]):>6}"
        idx+=1
        print(txt)

    print("++++++++++++ ADD-ON ++++++++++++")

    idx = 1
    for i in range(len(add_menu)):
        pivot = add_menu[i]
        if(pivot == "" or pivot==" "):
            continue

        pivot = pivot.strip()
        ls = pivot.split(",")
        txt = f"{idx}.{ls[0]:<20}{int(ls[1]):>2}      "
        idx+=1
        print(txt)

    print("++++++++++++++++++++++++++++++++")
    print()

def runStarBUGcafe_main():
    global coffee_menu_CSV, add_on_menu_CSV

    menu = coffee_menu_CSV.split("\n")
    add_menu = add_on_menu_CSV.split("\n")

    menu_ls = dict()
    add_on_ls = dict()

    report = dict()
    total = 0

    idx=1
    for i in range(len(menu)):
        pivot = menu[i]
        if(pivot == "" or pivot ==" "):
            continue
        pivot = pivot.strip()
        ls = pivot.split(",")
        menu_ls[idx] = {"H":int(ls[1].strip()), "C":int(ls[2].strip()), "F":int(ls[3].strip()), "name":ls[0].strip()}
        report[ls[0]] = 0
        idx+=1

    idx = 1
    for i in range(len(add_menu)):
        pivot = add_menu[i]
        if(pivot=="" or pivot==" "):
            continue

        pivot = pivot.strip()
        ls = pivot.split(",")
        add_on_ls[idx] = {"price": int(ls[1].strip()), "name":ls[0].strip()}
        idx+=1

    # print(menu_ls)
    # print(add_on_ls)
    
    while(True):
        print_menu()
        name_c = input("Enter customer's name: ")
        if(name_c=="Good Day"): 
            break
        customer = CustomerBill(name = name_c)

        while True:
            n = input("How many cups of coffee to order? ")
            try:
                n = int(n)
                if(n>0):
                    break
                else:
                    print(" ERROR: Invalid input!")
            except:
                print(" ERROR: Invalid input!")

        # cup loop
        for c in range(n):
            p = 0
            while True:
                txt = f"Cup #{c+1}, please select type of coffee: "
                t = input(txt)
                try:
                    t = int(t)
                    if(t not in range(1, len(menu_ls.keys())+1)):
                        print(" ERROR: Invalid input!")
                    else:
                        break
                except:
                    print(" ERROR: Invalid input!")
            
            report[menu_ls[t]["name"]] +=1

            ava = ["H", "C", "F"]
            l_ava = ["h", "c", "f"]
            if(menu_ls[t]["H"]==0): 
                ava.remove("H")
                l_ava.remove("h")
            if(menu_ls[t]["C"]==0): 
                ava.remove("C")
                l_ava.remove("c")
            if(menu_ls[t]["F"]==0): 
                ava.remove("F")
                l_ava.remove("f")

            if(len(ava)>1):
                tt = ""
                for ee in ava:
                    tt+=ee+","
                txt = f"Cup #{c+1}, please select drinking type ({tt[0:-1]}): "
                while True:
                    cc = input(txt)
                    if(cc not in ava and cc not in l_ava):
                        print(" ERROR: Invalid input!")
                    else:
                        if(cc in "hcf"):
                            cc = cc.upper()
                        if(cc == "H"):
                            cup = CupOfCoffee(menu_ls[t]["name"],"Hot", menu_ls[t]["H"])
                        if(cc == "C"):
                            cup = CupOfCoffee(menu_ls[t]["name"],"Cold", menu_ls[t]["C"])
                        if(cc == "F"):
                            cup = CupOfCoffee( menu_ls[t]["name"], "Frappe", menu_ls[t]["F"])
                        break
            else:
                if(ava[0]=="H"):
                    cup = CupOfCoffee(menu_ls[t]["name"], "Hot", menu_ls[t]["H"])
                if(ava[0]=="C"):
                    cup = CupOfCoffee(menu_ls[t]["name"], "Cold", menu_ls[t]["C"])
                if(ava[0]=="F"):
                    cup = CupOfCoffee(menu_ls[t]["name"], "Frappe", menu_ls[t]["F"])

            ad_ls = []
            while True:
                txt = f"Cup #{c+1}, please select add on (enter for exit): "
                ad = input(txt)
                if(ad=="" or len(ad_ls)==len(add_on_ls.keys())):
                    break
                try:
                    ad = int(ad)
                    if(ad in ad_ls):
                        print(" ERROR: Invalid input!")
                    else:
                        if(ad in range(1, len(add_on_ls.keys())+1)):
                            ad_ls.append(ad)
                            cup.set_add_on(add_on_ls[ad]["name"], add_on_ls[ad]["price"])
                        else:
                            print(" ERROR: Invalid input!")
                except:
                    print(" ERROR: Invalid input!")

                if(ad=="" or len(ad_ls)==len(add_on_ls.keys())):
                    break
            
            customer.add_ordered_coffee(cup)
            print(str(cup))
            total += cup.price

        print(customer.receipt())

    tt = insert_commas_recursive(str(total), 0)
    
    print("++++++++++++++++++++++++++++++++")
    print("      CPE38 **StarBUG Cafe    ")
    print("  Report for Coffee sold today")
    print("++++++++++++++++++++++++++++++++")
    for k, v in report.items():
        if(v==0): continue
        if(v>1):
            print(f" {k:<24}{v} cups")
        else:
            print(f" {k:<24}{v} cup")
    print()
    print(f"Total sold amount{tt:>10} baht")
    print("++++++++++++++++++++++++++++++++")
    print("       What's a good day!     ")
    print("++++++++++++++++++++++++++++++++")

coffee_menu_filename = input('Enter Coffee Menu available today (filename): ')
coffee_menu_CSV = readMenu(coffee_menu_filename)
addon_menu_filename = input('Enter AddOn Menu available today (filename): ')
add_on_menu_CSV = readMenu(addon_menu_filename)

runStarBUGcafe_main()