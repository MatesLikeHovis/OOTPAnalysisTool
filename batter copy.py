import weighting
from tkinter import ttk
import tkinter as tk
from RangeSlider.RangeSlider import RangeSliderH
import json
from tkinter import filedialog as fd
from tkinter import messagebox
import tensorflow as tf
import numpy as np
from classes import slider_set, header_, preset_button

def batter_menu(myFont, batter_list, canvas):

    gapweight = tk.DoubleVar(value=100)
    powerweight = tk.DoubleVar(value=100)
    eyeweight = tk.DoubleVar(value=100)
    avkweight = tk.DoubleVar(value=100)
    babipweight = tk.DoubleVar(value=100)
    speedweight = tk.DoubleVar(value=100)
    stealweight = tk.DoubleVar(value=100)
    brweight = tk.DoubleVar(value=100)
    defweight = tk.DoubleVar(value=100)
    platoonSearch = tk.IntVar(value=0)

    bat_weights = {
        'Gap': gapweight,
        'Power': powerweight,
        'Eye': eyeweight,
        'AvKs': avkweight,
        'Babip': babipweight,
        'Speed': speedweight,
        'Steal': stealweight,
        'BR': brweight,
        'Def': defweight
    }
    position_list = [
        'C',
        '1B',
        '2B',
        '3B',
        'SS',
        'LF',
        'CF',
        'RF',
        'DH'
    ]

    def export_weights(bat_weights):
        filetypes=[('JSON Files','*.json')]
        gap = bat_weights['Gap'].get()
        power = bat_weights['Power'].get()
        eye = bat_weights['Eye'].get()
        avk = bat_weights['AvKs'].get()
        babip = bat_weights['Babip'].get()
        speed = bat_weights['Speed'].get()
        steal = bat_weights['Steal'].get()
        br = bat_weights['BR'].get()
        df = bat_weights['Def'].get()
        literal_weights = {
            'Gap': gap,
            'Power': power,
            'Eye': eye,
            'AvKs': avk,
            'Babip': babip,
            'Speed': speed,
            'Steal': steal,
            'BR': br,
            'Def': df
        }

        filename=fd.asksaveasfilename(
            title="Please Select a location and name for your weights JSON File",
            initialdir='Data\JSON Files\Batters',
            filetypes=filetypes
        )
        if filename:
            if filename[-5] != '.json':
                filename += '.json'
            try:
                with open(filename, 'w') as file:
                    json.dump(literal_weights, file, ensure_ascii=False, indent=4)
            except:
                messagebox(master=None, message="There was an error - please check that your location is valid.")

    def import_weights(bat_weights):
        filetypes=[('JSON Files','*.json'),]
        backupweights = bat_weights
        try:
            filename = fd.askopenfilename(
                title="Please locate the batter weights json file",
                initialdir='Data\Presets\Batters',
                filetypes=filetypes
            )
            if filename:
                with open(filename, 'r') as file:
                    literal_weights = json.load(file)
                    bat_weights['Gap'].set(literal_weights['Gap'])
                    bat_weights['Power'].set(literal_weights['Power'])
                    bat_weights['Eye'].set(literal_weights['Eye'])
                    bat_weights['AvKs'].set(literal_weights['AvKs'])
                    bat_weights['Babip'].set(literal_weights['Babip'])
                    bat_weights['Speed'].set(literal_weights['Speed'])
                    bat_weights['Steal'].set(literal_weights['Steal'])
                    bat_weights['BR'].set(literal_weights['BR'])
                    bat_weights['Def'].set(literal_weights['Def'])
        except:
            messagebox(master=None, message="There was an error in loading the weights file.")
            bat_weights = backupweights

    def load_neural_network(filename):
        model = tf.keras.models.load_model(filename)
        return model

    def generate_projected_pcts(batter_list):
        babip_filename = 'Models\BABIP.keras'
        hrpct_filename = 'Models\Power to HR%.keras'
        avkso_filename = 'Models\SO% to AVKs.keras'
        bbeye_filename = 'Models\Walks to Eye.keras'

        babip_model = load_neural_network(babip_filename)
        hrpct_model = load_neural_network(hrpct_filename)
        avkso_model = load_neural_network(avkso_filename)
        bbeye_model = load_neural_network(bbeye_filename)

        babip_array = []
        power_array = []
        avk_array = []
        eye_array = []

        for batter in batter_list:
            babip_array.append(batter['Babip'])
            power_array.append(batter['Power'])
            avk_array.append(batter['AvKs'])
            eye_array.append(batter['Eye'])
        
        babip_score = np.array(babip_array)
        power_score = np.array(power_array)
        avk_score = np.array(avk_array)
        eye_score = np.array(eye_array)

        babip_pct_array = babip_model.predict(babip_score)
        hr_pct_array = hrpct_model.predict(power_score)
        so_pct_array = avkso_model.predict(avk_score)
        bb_pct_array = bbeye_model.predict(eye_score)

        for i, batter in enumerate(batter_list):  
            batter['babip_pct'] = babip_pct_array[i][0]
            batter['hr_pct'] = hr_pct_array[i][0]
            batter['so_pct'] = so_pct_array[i][0]
            batter['bb_pct'] = bb_pct_array[i][0]

        return batter_list

    def generate_projected_stats(batter_list):
        for batter in batter_list:
            pa = 600
            so = pa * batter['so_pct']
            bb = pa * batter['bb_pct']
            hr = pa * batter['hr_pct']
            bip = (pa - (so + bb + hr))
            h = bip * batter['babip_pct']
            ab = pa - bb
            avg = h / ab
            obp = (bb + h) / pa
            batter['HR'] = int(hr)
            batter['AVG'] = round(avg,3)
            batter['OBP'] = round(obp,3)
        return batter_list

    def sort_treeview(tree, col, reverse=False):
        if col == 'Name':
            data = [(tree.set(child, col), child) for child in tree.get_children('')]
        elif col == 'Card ID':
            data = [(int(tree.set(child, col)), child) for child in tree.get_children('')]
        else:
            data = [(float(tree.set(child, col)), child) for child in tree.get_children('')]
        data.sort(reverse=reverse)
        for index, (val, child) in enumerate(data):
            tree.move(child, '', index)
        tree.heading(col, command=lambda: sort_treeview(tree, col, not reverse))

    def activate():
        position = positionfilterDropDown.get()
        match position:
            case 'C':
                pos_requested = 2
            case '1B':
                pos_requested = 3
            case '2B':
                pos_requested = 4
            case '3B':
                pos_requested = 5
            case 'SS':
                pos_requested = 6
            case 'LF':
                pos_requested = 7
            case 'CF':
                pos_requested = 8
            case 'RF':
                pos_requested = 9
            case 'DH':
                pos_requested = 10
        if platoonSearch.get() == False:
            search_list = ['']
        else:
            search_list = ['vR','vL']

        for searchType in search_list:
            request_list = weighting.weight_batter_list(pos_requested, bat_weights, batter_list, isValueChecked.get(), valueMin.get(), valueMax.get(), searchType)
            response_list = weighting.return_nnum_from_list(request_list)
            projected_list = generate_projected_pcts(response_list)
            stats_list = generate_projected_stats(projected_list)        

            list_window = tk.Toplevel()
            list_window.title("List Results for " + position + " " + searchType)
            list_window.iconbitmap(r'Data\SmashIcons_Baseball.ico')
            tree_scroll = ttk.Scrollbar(list_window)
            tree_scroll.pack(side='right', fill='y')
            list_tree = ttk.Treeview(list_window, name="player Rating List", yscrollcommand=tree_scroll.set)
            list_tree['columns'] = ('Name','Card ID','Year','Weighted Rating','Card Value','OFF','DEF','RUN','AVG','OBP','HR')
            list_tree.column('#0', width=30 , minwidth=25)
            list_tree.column("Name")
            list_tree.column("Card ID", width=50)
            list_tree.column("Year", width=50)
            list_tree.column("Weighted Rating", width=50)
            list_tree.column("Card Value", width=50)
            list_tree.column("OFF", width=50)
            list_tree.column("DEF", width=50)
            list_tree.column("RUN", width=50)
            list_tree.column("AVG", width=50)
            list_tree.column("OBP", width=50)
            list_tree.column("HR", width=50)
            list_tree.heading("#0", text=position+' '+searchType)
            list_tree.heading("Name", text="Name", command=lambda: sort_treeview(list_tree, "Name"))
            list_tree.heading("Card ID", text="ID", command=lambda: sort_treeview(list_tree, "Card ID"))
            list_tree.heading("Year", text='Year', command=lambda:sort_treeview(list_tree,'Year'))
            list_tree.heading("Weighted Rating", text="OVR", command=lambda: sort_treeview(list_tree, "Weighted Rating"))
            list_tree.heading("Card Value", text="VAL", command=lambda: sort_treeview(list_tree, "Card Value"))
            list_tree.heading("OFF", text="OFF", command=lambda: sort_treeview(list_tree, "OFF"))
            list_tree.heading("DEF", text="DEF", command=lambda: sort_treeview(list_tree, "DEF"))
            list_tree.heading("RUN", text="RUN", command=lambda: sort_treeview(list_tree, "RUN"))
            list_tree.heading("AVG", text="AVG", command=lambda: sort_treeview(list_tree, "AVG"))
            list_tree.heading("OBP", text="OBP", command=lambda: sort_treeview(list_tree, "OBP"))
            list_tree.heading("HR", text="HR", command=lambda: sort_treeview(list_tree, "HR"))
            for batter in stats_list:
                list_tree.insert(parent='', index='end', iid=batter['Id'], values=((batter['FirstName'] + ' ' + batter['LastName']), batter['Id'], batter['Year'], batter['Rating'], batter['Value'], batter['Offense'], batter['Defense'], batter['Running'], batter['AVG'], batter['OBP'],batter['HR']))
            tree_scroll.config(command=list_tree.yview)
            list_tree.pack()

    instructionHeader = header_(canvas, 'Welcome to OOTPB25 Analysis Tool', myFont, 3, 1 ,0)
    instructionHeader.padY(10)
    welcomeHeader = header_(canvas, 'Set Relative Weights Here', myFont, 3, 1, 1)

    sliders = [('BABIP', 2, babipweight),('AvKs', 3, avkweight),('Power', 4, powerweight), ('Eye', 5, eyeweight), ('Gap', 6, gapweight), ('Speed', 7, speedweight), ('Steal', 8, stealweight), ('Baserunning', 9, brweight), ('Defense', 10, defweight)]

    for slider in sliders:
        thisSlider = slider_set(canvas=canvas, text=slider[0], font=myFont, row=slider[1], variable=slider[2])
        
    filterheader = header_(canvas, 'Card Selection Filters', myFont, 3, 1, 11)
    filterlabel = header_(canvas, 'Card Value Filter', myFont, 1, 0, 12)

    valueMin = tk.DoubleVar(value=40)
    valueMax = tk.DoubleVar(value=100)
    valueSlider = RangeSliderH(canvas, variables=[valueMin, valueMax], min_val=40, max_val=100, padX=20, bar_radius=5, line_width=2, Height=55)
    valueSlider.grid(columnspan=3, row=12, column=1)

    isValueChecked = tk.BooleanVar()
    valueCheckBox = ttk.Checkbutton(canvas, text="Make Filter Active",variable=isValueChecked,onvalue=True,offvalue=False )
    valueCheckBox.grid(columnspan=1, column=4, row=12)
    valueCheckBox.state(('!alternate','selected'))

    positionheader = header_(canvas, 'Position to search:', myFont, 1, 0, 16)
    positionfilterDropDown = ttk.Combobox(canvas, state='readonly', width=10, values=position_list)
    positionfilterDropDown.grid(columnspan=1, pady=5, padx=5, column=1,row=16)
    positionfilterDropDown.set('C')

    generateListButton = tk.Button(canvas,text="Generate List", command=activate, bg='pink')
    generateListButton.grid(column=4,row=16)

    def setSlider(minimum, maximum):
        valueMin.set(minimum)
        valueMax.set(maximum)
        valueSlider.forceValues([minimum,maximum])
    
    presetsheader = header_(canvas, 'Card Calue Presets', myFont, 3, 1, 13)
    valuePresetIron = preset_button(canvas=canvas, text='<= Iron', font=myFont, bgColor='Gray', valueSlider=valueSlider, valueMinVar = valueMin, valueMaxVar=valueMax, valueMin=40, valueMax=59.9, col=0,row=14)
    valuePresetBronze = preset_button(canvas=canvas, text='<= Bronze', font=myFont, bgColor='brown', valueSlider=valueSlider, valueMinVar = valueMin, valueMaxVar=valueMax, valueMin=40, valueMax=69.9, col=1,row=14)
    valuePresetSilver = preset_button(canvas=canvas, text='<= Silver', font=myFont, bgColor='silver', valueSlider=valueSlider, valueMinVar = valueMin, valueMaxVar=valueMax, valueMin=40, valueMax=79.9, col=2,row=14)
    valuePresetGold = preset_button(canvas=canvas, text='<= Gold', font=myFont, bgColor='gold', valueSlider=valueSlider, valueMinVar = valueMin, valueMaxVar=valueMax, valueMin=40, valueMax=89.9, col=3,row=14)
    valuePresetDiamond = preset_button(canvas=canvas, text='<= Diamond', font=myFont, bgColor='lightblue', valueSlider=valueSlider, valueMinVar = valueMin, valueMaxVar=valueMax, valueMin=40, valueMax=99.9, col=1,row=15)
    valuePresetAll = preset_button(canvas=canvas, text='All Values', font=myFont, bgColor='white', valueSlider=valueSlider, valueMinVar = valueMin, valueMaxVar=valueMax, valueMin=40, valueMax=100, col=2,row=15)

    platoonStandardRadio = tk.Radiobutton(canvas, text="Standard (No Platoon)", value=False, variable=platoonSearch, state='active')
    platoonStandardRadio.grid(column=5,row=6)
    platoonSplitsRadio = tk.Radiobutton(canvas, text="Splits (vR/vL) Active", value=True, variable = platoonSearch)
    platoonSplitsRadio.grid(column=5,row=7)

    importWeightsButton = tk.Button(canvas,text="Import Weights JSON", bg="yellow", command=lambda: import_weights(bat_weights))
    importWeightsButton.grid(column=5,row=2)
    exportWeightsButton = tk.Button(canvas,text="Export Weights JSON", bg="yellow", command=lambda: export_weights(bat_weights))
    exportWeightsButton.grid(column=5,row=3)
