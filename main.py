import contextlib
import sys
from pyke import knowledge_engine
from pyke import krb_traceback
engine = knowledge_engine.engine(__file__)
import PySimpleGUI as sg
sg.theme("BlueMono")
soil = [

    [sg.Text("Select the type of soil \
    \n\n1: Light sandy \
    \n\n2: Heavy loams \
    \n\n3: Sandy loams \
    \n\n4: Alluvial lands \
    \n\n5: Light black\n")],
    [sg.InputText(key="soil")],
    [sg.Text("______________________________________________________________________________________")],
    [sg.Text("\nSelect cultivation time\n\n1: January \
                            2: February\
		\n\n3: March\
		                4: April\
		\n\n5: May\
		                6: June\
		\n\n7: July\
		                8: August\
		\n\n9: September\
		 10: October\
		\n\n11: November\
		 12: December\n")],
    [sg.InputText(key = "month")],
    [sg.Text("______________________________________________________________________________________")],
    [sg.Text("\nSelect harvest season\n\n1: Summer Harvest \
              2: Winter Harvest\
		3: Early Summer Harvest\
		\n\n4: Fall Harvest\
		5: Spring Harvest\n")],
    [sg.InputText(key = "season")],
 [sg.Text("\n")],


    
    [sg.Submit(),sg.Cancel()]
]

window = sg.Window("soil",soil,resizable=True)

event,value = window.read()
file = open("plant.txt","w")
print(value)
for i in value:
    file.write(str(value[i])+'\n')
file.close()


window.close()

def bc_test_questions():

    engine.reset()      
    engine.activate('bc_simple_rules_questions') 
    lst=list()
    try:
        with engine.prove_goal('bc_simple_rules_questions.what_to_plant($plant1,$temp1,$temp2,$seed,$crop)') as gen:
            for vars, plan in gen:
                print("------------------------------------------------------------------------")
                lst.append(("\nYou can plant: %s" % (vars['plant1'])+"\nSuitable tempreture is from %s" % (vars['temp1'])+" to %s" % (vars['temp2'])+" ℃"+"\nSeeds per acre: %s" % (vars['seed'])+ "\nCrop Harvest Quantity: %s" % (vars['crop'])+"\n\n") )
    except Exception:
        
        krb_traceback.print_exc()
        sys.exit(1)
    return lst

sys.stdin=open("plant.txt")
x = bc_test_questions()
s=""
for i in x:
    s += str(i)+'\n'
sg.popup(s)