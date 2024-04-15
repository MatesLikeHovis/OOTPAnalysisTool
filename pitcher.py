import weighting
from tkinter import ttk
import tkinter as tk
from RangeSlider.RangeSlider import RangeSliderH
from tkinter import filedialog as fd
from tkinter import messagebox
import json
import tensorflow as tf
import numpy as np
from classes import slider_set, header_, preset_bank

def pitcher_menu(myFont, pitcher_list, my_list, canvas):

    stuffweight = tk.DoubleVar(value=100)
    stuffActive = tk.IntVar(value=1)
    phrweight = tk.DoubleVar(value=100)
    phrActive = tk.IntVar(value=1)
    pbabipweight = tk.DoubleVar(value=100)
    pbabipActive = tk.IntVar(value=1)
    controlweight = tk.DoubleVar(value=100)
    controlActive = tk.IntVar(value=1)
    staminaweight = tk.DoubleVar(value=100)
    staminaActive = tk.IntVar(value=1)
    holdweight = tk.DoubleVar(value=100)
    holdActive = tk.IntVar(value=1)
    defweight = tk.DoubleVar(value=100)
    defActive = tk.IntVar(value=1)

    ptch_weights = {
        'Stuff':stuffweight,
        'PHR':phrweight,
        'PBABIP':pbabipweight,
        'Control':controlweight,
        'Stamina':staminaweight,
        'Hold':holdweight,
        'Defense':defweight
    }

    pitch_actives = {
        'Stuff':stuffActive,
        'PHR':phrActive,
        'PBABIP':pbabipActive,
        'Control':controlActive,
        'Stamina':staminaActive,
        'Hold':holdActive,
        'Defense':defActive
    }

    position_list = [
        'SP',
        'RP',
        'CL',
        'RP/CL',
        'SP/RP/CL'
    ]

    def export_weights(ptch_weights, ptch_actives):
        filetypes=[('JSON Files','*.json')]
        stuff = ptch_weights['Stuff'].get()
        stuffAct = ptch_actives['Stuff'].get()
        phr = ptch_weights['PHR'].get()
        phrAct = ptch_actives['Stuff'].get()
        pbabip = ptch_weights['PBABIP'].get()
        pbabipAct = ptch_actives['PBABIP'].get()
        control = ptch_weights['Control'].get()
        controlAct = ptch_actives['Control'].get()
        stamina = ptch_weights['Stamina'].get()
        staminaAct = ptch_actives['Stamina'].get()
        hold = ptch_weights['Hold'].get()
        holdAct = ptch_actives['Hold'].get()
        df = ptch_weights['Defense'].get()
        dfAct = ptch_actives['Hold'].get()
        literal_weights = {
            'Stuff': stuff,
            'PHR': phr,
            'PBABIP': pbabip,
            'Control': control,
            'Stamina': stamina,
            'Hold': hold,
            'Defense': df,
            'StuffActive': stuffAct,
            'PHRActive': phrAct,
            'PBABIPActive': pbabipAct,
            'ControlActive': controlAct,
            'StaminaActive': staminaAct,
            'HoldActive': holdAct,
            'DefenseActive': dfAct
        }

        filename=fd.asksaveasfilename(
            title="Please Select a location and name for your weights JSON File",
            initialdir='Data\Presets\Pitchers',
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

    def import_weights(ptch_weights, ptch_actives):
        filetypes=[('JSON Files','*.json')]
        backupweights = ptch_weights
        backupActives = ptch_actives
        try:
            filename = fd.askopenfilename(
                title="Please locate the pitcher weights json file",
                initialdir='Data\Presets\Pitchers',
                filetypes=filetypes
            )
            if filename:
                with open(filename, 'r') as file:
                    literal_weights = json.load(file)
                    weightList = ['Stuff','PHR','PBABIP','Control','Stamina','Hold','Defense']
                    for weight in weightList:
                        ptch_weights[weight].set(literal_weights[weight])
                        ptch_actives[weight].set(literal_weights[weight+'Active'])
        except:
            messagebox(master=None, message="There was an error in loading the weights file.")
            ptch_weights = backupweights
            ptch_actives = backupActives

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

    def generate_projected_pcts(pitcher_list):
        stuff_to_sopct_slope = 0.0021956584
        stuff_to_sopct_intercept = 0.027717765
        control_to_bbpct_slope = -0.0010105851
        control_to_bbpct_intercept = 0.15812697
        babip_to_babippct_slope = -0.0011705309
        babip_to_babippct_intercept = 0.37854692
        pHR_to_hrpct_slope = -0.0003623672
        pHR_to_hrpct_intercept = 0.048940595

        for pitcher in pitcher_list:
            pitcher['bbpct'] = ((control_to_bbpct_slope * (pitcher['Control'])) + control_to_bbpct_intercept)

            pitcher['babipPct'] = ((babip_to_babippct_slope * (pitcher['PBABIP'])) + babip_to_babippct_intercept)

            pitcher['hrpct'] = ((pHR_to_hrpct_slope * (pitcher['PHR'])) + pHR_to_hrpct_intercept)

            pitcher['sopct'] = ((stuff_to_sopct_slope * (pitcher['Stuff'])) + stuff_to_sopct_intercept)
            if (pitcher['bbpct'] < 0): pitcher['bbpct'] = 0
            if (pitcher['babipPct'] < 0): pitcher['babipPct'] = 0
            if (pitcher['hrpct'] < 0): pitcher['hrpct'] = 0
            if (pitcher['sopct'] < 0): pitcher['sopct'] = 0
            if (pitcher['bbpct'] > 0.23): pitcher['bbpct'] = 0.23
            if (pitcher['babipPct'] > 0.45): pitcher['babipPct'] = 0.45
            if (pitcher['hrpct'] > 0.06): pitcher['hrpct'] = 0.06
            if (pitcher['sopct'] > 0.45): pitcher['sopct'] = 0.45
            babip = pitcher['babipPct']
            sopct = pitcher['sopct']
            bbpct = pitcher['bbpct']
            hrpct = pitcher['hrpct']
            innings = 9
            outs = 27
            outonbipPct = (1-babip)
            chanceofbip = (1-(sopct+bbpct+hrpct))
            batters_faced =  outs / ((chanceofbip * outonbipPct) + sopct)
            so = batters_faced * sopct
            bb = batters_faced * bbpct
            hr = batters_faced * hrpct
            h = batters_faced * chanceofbip * babip
            ab = batters_faced - bb
            avg = (h + hr) / ab
            obp = (h + hr + bb) / (ab + bb)
            multiplier = 600 / batters_faced
            h600 = avg * 600
            xbht600 = (h * 0.08)
            hr600 = hr * multiplier
            xbh600 = xbht600 - hr600
            if xbh600 < 0: xbh600 = 0
            tb600 = (h600 * 0.92) + (xbh600 * 2.3) + (hr600 * 4)
            bb600 = 600 * bbpct
            slg = tb600 / (600 - bb600)
            ops = slg + obp
            bb600 = bb * multiplier
            so600 = so * multiplier
            pitcher['h9'] = h
            pitcher['AVG'] = round(avg, 3)
            pitcher['hr9'] = hr
            pitcher['bb9'] = bb
            pitcher['so9'] = so
            pitcher['OBP'] = round(obp, 3)
            pitcher['SLG'] = round(slg, 3)
            pitcher['OPS'] = round(ops, 3)
            pitcher['HR'] = int(round(hr600))
            pitcher['SO'] = int(round(so600))
            pitcher['BB'] = int(round(bb600))

        return pitcher_list

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
        request_list = weighting.weight_pitcher_list(position, ptch_weights, pitcher_list, isValueChecked.get(), valueMin.get(), valueMax.get(), pitch_actives)
        response_list = weighting.return_nnum_from_list(request_list)
        projected_list = generate_projected_pcts(response_list)
        if myCardsChecked.get() == 1 and my_list:
            projected_list = weighting.filter_my_players(projected_list, my_list)

        list_window = tk.Toplevel()
        list_window.title("Weighting List Results")
        list_window.iconbitmap(r'Data\SmashIcons_Baseball.ico')
        tree_scroll = ttk.Scrollbar(list_window)
        tree_scroll.pack(side='right', fill='y')
        list_tree = ttk.Treeview(list_window, name="player Rating List", yscrollcommand=tree_scroll.set)
        list_tree['columns'] = ('Name','Card ID','Weighted Rating','Card Value','Stuff','Movement','Control','Other','pAVG','pOBP', 'pSLG','pOPS','HR','BB','SO')
        list_tree.column("#0", width=5 , minwidth=5)
        list_tree.column("Name")
        list_tree.column("Card ID", width=50)
        list_tree.column("Weighted Rating", width=50)
        list_tree.column("Card Value", width=50)
        list_tree.column("Stuff", width=50)
        list_tree.column("Movement", width=50)
        list_tree.column("Control", width=50)
        list_tree.column("Other", width=50)
        list_tree.column("pAVG", width=50)
        list_tree.column("pOBP", width=50)
        list_tree.column("pSLG", width=50)
        list_tree.column("pOPS", width=50)
        list_tree.column("HR", width=50)
        list_tree.column("BB", width=50)
        list_tree.column("SO", width=50)
        list_tree.heading("#0", text="")
        list_tree.heading("Name", text="Name", command=lambda: sort_treeview(list_tree,'Name'))
        list_tree.heading("Card ID", text="ID", command=lambda: sort_treeview(list_tree,'Card ID'))
        list_tree.heading("Weighted Rating", text="OVR", command=lambda: sort_treeview(list_tree,'Weighted Rating'))
        list_tree.heading("Card Value", text="VAL", command=lambda: sort_treeview(list_tree,'Card Value'))
        list_tree.heading("Stuff", text="STF", command=lambda: sort_treeview(list_tree,'Stuff'))
        list_tree.heading("Movement", text="MVM", command=lambda: sort_treeview(list_tree,'Movement'))
        list_tree.heading("Control", text="CNT", command=lambda: sort_treeview(list_tree,'Control'))
        list_tree.heading("Other", text="OTH", command=lambda: sort_treeview(list_tree,'Other'))
        list_tree.heading("pAVG", text="pAVG", command=lambda: sort_treeview(list_tree,'pAVG'))
        list_tree.heading("pOBP", text="pOBP", command=lambda: sort_treeview(list_tree,'pOBP'))
        list_tree.heading("pSLG", text="pSLG", command=lambda: sort_treeview(list_tree,'pSLG'))
        list_tree.heading("pOPS", text="pOPS", command=lambda: sort_treeview(list_tree,'pOPS'))
        list_tree.heading("HR", text="HR", command=lambda: sort_treeview(list_tree,'HR'))
        list_tree.heading("BB", text="BB", command=lambda: sort_treeview(list_tree,'BB'))
        list_tree.heading("SO", text="SO", command=lambda: sort_treeview(list_tree,'SO'))      

        for pitcher in projected_list:
            list_tree.insert(parent='', index='end', iid=pitcher['Id'], values=((pitcher['FirstName'] + ' ' + pitcher['LastName']), pitcher['Id'], pitcher['Rating'], pitcher['Value'], pitcher['Stuff'], pitcher['Movement'], pitcher['Control'], pitcher['Other'], pitcher['AVG'], pitcher['OBP'], pitcher['SLG'], pitcher['OPS'], pitcher['HR'],pitcher['BB'], pitcher['SO']))
        tree_scroll.config(command=list_tree.yview)
        list_tree.pack()

    instructionHeader = header_(canvas, 'Pitcher Analysis Tool', myFont, 3, 1 ,0)
    instructionHeader.padY(10)
    welcomeHeader = header_(canvas, 'Set Relative Weights Here', myFont, 3, 1, 1)

    sliders = [('Stuff', 2, stuffweight, stuffActive, 'red'),('PHR', 3, phrweight, phrActive, 'powderblue'),('PBABIP', 4, pbabipweight, pbabipActive, 'powderblue'), ('Control', 5, controlweight, controlActive, 'yellow'), ('Stamina', 6, staminaweight, staminaActive, 'orange'), ('Hold', 7, holdweight, holdActive, 'brown'), ('Defense', 8, defweight, defActive, 'green')]

    for slider in sliders:
        thisSlider = slider_set(canvas=canvas, text=slider[0], font=myFont, row=slider[1], variable=slider[2], activeVariable=slider[3], troughColor=slider[4])

    filterheader = header_(canvas, 'Card Selection Filters', myFont, 3, 1, 11)
    filterlabel = header_(canvas, 'Card Value Filter', myFont, 1, 0, 12)

    valueMin = tk.DoubleVar(value=40)
    valueMax = tk.DoubleVar(value=100)
    valueSlider = RangeSliderH(canvas, variables=[valueMin, valueMax], min_val=40, max_val=100, padX=20, bar_radius=5, line_width=2, Height=55)
    valueSlider.grid(columnspan=3, row=12, column=1)

    isValueChecked = tk.IntVar()
    valueCheckBox = ttk.Checkbutton(canvas, text="Make Filter Active",variable=isValueChecked,onvalue=True,offvalue=False )
    valueCheckBox.grid(columnspan=1, column=4, row=12)
    isValueChecked.set(1)
    valueCheckBox.state(('!alternate','selected'))

    positionfilterLabel = tk.Label(canvas,text="Position to search:", font=myFont, pady=10, anchor='e')
    positionfilterLabel.grid(column=0, row=16)
    positionfilterDropDown = ttk.Combobox(canvas, state='readonly', width=10, values=position_list)
    positionfilterDropDown.grid(columnspan=1, pady=5, padx=5, column=1,row=16)
    positionfilterDropDown.set('SP')

    generateListButton = tk.Button(canvas,text="Generate List", command=activate, bg='pink')
    generateListButton.grid(column=4,row=16)

    def setSlider(minimum, maximum):
        valueMin.set(minimum)
        valueMax.set(maximum)
        valueSlider.forceValues([minimum,maximum])

    presetsheader = header_(canvas, 'Card Value Presets', myFont, 3, 1, 13)
    presetbank = preset_bank(canvas, myFont, 14, valueSlider, valueMax, valueMin)

    myCardsChecked = tk.IntVar()
    myCardsCheckBox = ttk.Checkbutton(canvas, text="Only MY Cards", variable=myCardsChecked)
    myCardsCheckBox.grid(columnspan=1, column=5, row = 10)
    myCardsChecked.set(1)
    myCardsCheckBox.state(('!alternate','selected'))    

    importWeightsButton = tk.Button(canvas,text="Import Weights JSON", bg="yellow", command=lambda: import_weights(ptch_weights, pitch_actives))
    importWeightsButton.grid(column=5,row=2)
    exportWeightsButton = tk.Button(canvas,text="Export Weights JSON", bg="yellow", command=lambda: export_weights(ptch_weights, pitch_actives))
    exportWeightsButton.grid(column=5,row=3)
