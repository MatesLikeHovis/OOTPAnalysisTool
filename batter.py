import weighting
from tkinter import ttk
import tkinter as tk
from RangeSlider.RangeSlider import RangeSliderH
import json
from tkinter import filedialog as fd
from tkinter import messagebox
from classes import slider_set, header_, preset_bank

def batter_menu(myFont, batter_list, my_list, canvas):
    print(my_list)
    gapweight = tk.DoubleVar(value=100)
    gapActive = tk.IntVar(value=1)
    powerweight = tk.DoubleVar(value=100)
    powerActive = tk.IntVar(value=1)
    eyeweight = tk.DoubleVar(value=100)
    eyeActive = tk.IntVar(value=1)
    avkweight = tk.DoubleVar(value=100)
    avkActive = tk.IntVar(value=1)
    babipweight = tk.DoubleVar(value=100)
    babipActive = tk.IntVar(value=1)
    offweight = tk.DoubleVar(value=100)
    offActive = tk.IntVar(value=1)
    speedweight = tk.DoubleVar(value=100)
    speedActive = tk.IntVar(value=1)
    stealweight = tk.DoubleVar(value=100)
    stealActive = tk.IntVar(value=1)
    brweight = tk.DoubleVar(value=100)
    brActive = tk.IntVar(value=1)
    runweight = tk.DoubleVar(value=100)
    runActive = tk.IntVar(value=1)
    defweight = tk.DoubleVar(value=100)
    defActive = tk.IntVar(value=1)
    platoonSearch = tk.IntVar(value=0)

    bat_active = {
        'Gap':gapActive,
        'Power':powerActive,
        'Eye':eyeActive,
        'AvKs':avkActive,
        'Babip':babipActive,
        'Speed':speedActive,
        'Steal':stealActive,
        'BR':brActive,
        'Off':offActive,
        'Run':runActive,
        'Def':defActive
    }

    bat_weights = {
        'Gap': gapweight,
        'Power': powerweight,
        'Eye': eyeweight,
        'AvKs': avkweight,
        'Babip': babipweight,
        'Speed': speedweight,
        'Steal': stealweight,
        'BR': brweight,
        'Off': offweight,
        'Run': runweight,
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

    def export_weights(bat_weights, bat_active):
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
        gapAct = bat_active['Gap'].get()
        powerAct = bat_active['Power'].get()
        eyeAct = bat_active['Eye'].get()
        avkAct = bat_active['AvKs'].get()
        babipAct = bat_active['Babip'].get()
        speedAct = bat_active['Speed'].get()
        stealAct = bat_active['Steal'].get()
        brAct = bat_active['BR'].get()
        dfAct = bat_active['Def'].get()
        off = bat_weights['Off'].get()
        offAct = bat_active['Off'].get()
        run = bat_weights['Run'].get()
        runAct = bat_active['Run'].get()
        literal_weights = {
            'Gap': gap,
            'Power': power,
            'Eye': eye,
            'AvKs': avk,
            'Babip': babip,
            'Speed': speed,
            'Steal': steal,
            'BR': br,
            'Off': off,
            'Run': run,
            'Def': df,
            'GapActive': gapAct,
            'PowerActive': powerAct,
            'EyeActive': eyeAct,
            'AvKsActive': avkAct,
            'BabipActive': babipAct,
            'SpeedActive': speedAct,
            'StealActive': stealAct,
            'BRActive': brAct,
            'OffActive': offAct,
            'RunActive': runAct,
            'DefActive': dfAct
        }

        filename=fd.asksaveasfilename(
            title="Please Select a location and name for your weights JSON File",
            initialdir='Data\Presets\Batters',
            filetypes=filetypes
        )
        if filename:
            if filename[-5:] != '.json':
                filename += '.json'
            try:
                with open(filename, 'w') as file:
                    json.dump(literal_weights, file, ensure_ascii=False, indent=4)
            except:
                messagebox(master=None, message="There was an error - please check that your location is valid.")

    def import_weights(bat_weights, bat_active):
        filetypes=[('JSON Files','*.json'),]
        backupweights = bat_weights
        backupActives = bat_active
        weightList = ['Gap','Power','Eye','AvKs','Babip','Speed','Steal','BR','Off','Run','Def']
        try:
            filename = fd.askopenfilename(
                title="Please locate the batter weights json file",
                initialdir='Data\Presets\Batters',
                filetypes=filetypes
            )
            if filename:
                with open(filename, 'r') as file:
                    literal_weights = json.load(file)
                    for weight in weightList:
                        bat_weights[weight].set(literal_weights[weight])
                        bat_active[weight].set(literal_weights[weight+'Active'])

        except:
            messagebox(master=None, message="There was an error in loading the weights file.")
            bat_weights = backupweights
            bat_active = backupActives

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
            request_list = weighting.weight_batter_list(pos_requested, bat_weights, batter_list, isValueChecked.get(), valueMin.get(), valueMax.get(), bat_active, searchType)
            response_list = weighting.return_nnum_from_list(request_list)
            projected_list = weighting.generate_projected_pcts(response_list)
            stats_list = weighting.generate_projected_stats(projected_list)        
            if myCardsChecked.get() == 1 and my_list:
                stats_list = weighting.filter_my_players(stats_list, my_list)
            list_window = tk.Toplevel()
            list_window.title("List Results for " + position + " " + searchType)
            list_window.iconbitmap(r'Data\SmashIcons_Baseball.ico')
            tree_scroll = ttk.Scrollbar(list_window)
            tree_scroll.pack(side='right', fill='y')
            list_tree = ttk.Treeview(list_window, name="player Rating List", yscrollcommand=tree_scroll.set)
            list_tree['columns'] = ('Name','Card ID','Year','Weighted Rating','Card Value','OFF','DEF','RUN','AVG','OBP','SLG','OPS','HR')
            list_tree.column('#0', width=45, minwidth=40)
            list_tree.column("Name", width=110, minwidth=50)
            list_tree.column("Card ID", width=50)
            list_tree.column("Year", width=50, anchor='center')
            list_tree.column("Weighted Rating", width=50)
            list_tree.column("Card Value", width=50)
            list_tree.column("OFF", width=50, anchor='center')
            list_tree.column("DEF", width=50, anchor='center')
            list_tree.column("RUN", width=50, anchor='center')
            list_tree.column("AVG", width=50, anchor='center')
            list_tree.column("OBP", width=50, anchor='center')
            list_tree.column("SLG", width=50, anchor='center')
            list_tree.column("OPS", width=50, anchor='center')
            list_tree.column("HR", width=50, anchor='center')
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
            list_tree.heading("SLG", text="SLG", command=lambda: sort_treeview(list_tree, "SLG"))
            list_tree.heading("OPS", text="OPS", command=lambda: sort_treeview(list_tree, "OPS"))
            list_tree.heading("HR", text="HR", command=lambda: sort_treeview(list_tree, "HR"))
            for batter in stats_list:
                list_tree.insert(parent='', index='end', iid=batter['Id'], values=((batter['FirstName'] + ' ' + batter['LastName']), batter['Id'], batter['Year'], batter['Rating'], batter['Value'], batter['Offense'], batter['Defense'], batter['Running'], batter['AVG'], batter['OBP'],batter['SLG'],batter['OPS'],batter['HR']))
            tree_scroll.config(command=list_tree.yview)
            list_tree.pack()

    instructionHeader = header_(canvas, 'Batter Analysis Tool', myFont, 3, 1 ,0)
    instructionHeader.padY(10)
    welcomeHeader = header_(canvas, 'Set Relative Weights Here', myFont, 3, 1, 1)

    sliders = [('BABIP', 2, babipweight, babipActive, 'powderblue'),('AvKs', 3, avkweight, avkActive, 'powderblue'),('Power', 4, powerweight, powerActive, 'powderblue'), ('Eye', 5, eyeweight, eyeActive, 'powderblue'), ('Gap', 6, gapweight, gapActive, 'powderblue'), ('OFFENSE', 7, offweight, offActive, 'blue'), ('Speed', 8, speedweight, speedActive, 'pink'), ('Steal', 9, stealweight, stealActive, 'pink'), ('Baserunning', 10, brweight, brActive, 'pink'), ('RUNNING', 11, runweight, runActive, 'red'), ('DEFENSE', 12, defweight, defActive, 'green')]

    for slider in sliders:
        thisSlider = slider_set(canvas=canvas, text=slider[0], font=myFont, row=slider[1], variable=slider[2], activeVariable=slider[3], troughColor=slider[4])
        
    filterheader = header_(canvas, 'Card Selection Filters', myFont, 3, 1, 13)
    filterlabel = header_(canvas, 'Card Value Filter', myFont, 1, 0, 14)

    valueMin = tk.DoubleVar(value=40)
    valueMax = tk.DoubleVar(value=100)
    valueSlider = RangeSliderH(canvas, variables=[valueMin, valueMax], min_val=40, max_val=100, padX=20, bar_radius=5, line_width=2, Height=55)
    valueSlider.grid(columnspan=3, row=14, column=1)

    isValueChecked = tk.IntVar()
    valueCheckBox = ttk.Checkbutton(canvas, text="Make Filter Active",variable=isValueChecked)
    valueCheckBox.grid(columnspan=1, column=4, row=14)
    isValueChecked.set(1)
    valueCheckBox.state(('!alternate','selected'))

    positionheader = header_(canvas, 'Position to search:', myFont, 1, 0, 18)
    positionfilterDropDown = ttk.Combobox(canvas, state='readonly', width=10, values=position_list)
    positionfilterDropDown.grid(columnspan=1, pady=5, padx=5, column=1,row=18)
    positionfilterDropDown.set('C')

    generateListButton = tk.Button(canvas,text="Generate List", command=activate, bg='pink')
    generateListButton.grid(column=4,row=18)

    def setSlider(minimum, maximum):
        valueMin.set(minimum)
        valueMax.set(maximum)
        valueSlider.forceValues([minimum,maximum])
    
    presetsheader = header_(canvas, 'Card Value Presets', myFont, 3, 1, 15)
    presetbank = preset_bank(canvas, myFont, 16, valueSlider, valueMax, valueMin)
    
    platoonStandardRadio = tk.Radiobutton(canvas, text="Standard (No Platoon)", value=False, variable=platoonSearch, state='active')
    platoonStandardRadio.grid(column=5,row=6)
    platoonSplitsRadio = tk.Radiobutton(canvas, text="Splits (vR/vL) Active", value=True, variable = platoonSearch)
    platoonSplitsRadio.grid(column=5,row=7)

    myCardsChecked = tk.IntVar()
    myCardsCheckBox = ttk.Checkbutton(canvas, text="Only MY Cards", variable=myCardsChecked)
    myCardsCheckBox.grid(columnspan=1, column=5, row = 10)
    myCardsChecked.set(1)
    myCardsCheckBox.state(('!alternate','selected'))

    importWeightsButton = tk.Button(canvas,text="Import Weights JSON", bg="yellow", command=lambda: import_weights(bat_weights, bat_active))
    importWeightsButton.grid(column=5,row=2)
    exportWeightsButton = tk.Button(canvas,text="Export Weights JSON", bg="yellow", command=lambda: export_weights(bat_weights, bat_active))
    exportWeightsButton.grid(column=5,row=3)
