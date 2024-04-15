import weighting
from tkinter import ttk
import tkinter as tk
from RangeSlider.RangeSlider import RangeSliderH
import json
from tkinter import filedialog as fd
from tkinter import messagebox
from classes import slider_set, header_, preset_bank
import batter
drag_position = 'DH'

def teambuilder_menu(myFont, batter_list, my_list, canvas):

    attributes_list = ['Gap','Power','Eye','AvKs','Babip','Speed','Steal','BR','Def', 'Off', 'Run']
    position_list = ['C','1B','2B','3B','SS','LF','CF','RF','DH']
    team_weights = {}
    team_active = {}
    for position in position_list:
        pos_dict = {}
        pos_active = {}
        for attribute in attributes_list:
            pos_dict[attribute] = tk.DoubleVar(value=100)
            pos_active[attribute] = tk.IntVar(value=1)
        team_weights[position] = pos_dict
        team_active[position] = pos_active

        
    
    current_position = tk.StringVar()
    current_babip = tk.DoubleVar(value=100)
    current_babip_active = tk.IntVar(value=1)
    current_gap = tk.DoubleVar(value=100)
    current_gap_active = tk.IntVar(value=1)
    current_power = tk.DoubleVar(value=100)
    current_power_active = tk.IntVar(value=1)
    current_eye = tk.DoubleVar(value=100)
    current_eye_active = tk.IntVar(value=1)
    current_speed = tk.DoubleVar(value=100)
    current_speed_active = tk.IntVar(value=1)
    current_steal = tk.DoubleVar(value=100)
    current_steal_active = tk.IntVar(value=1)
    current_br = tk.DoubleVar(value=100)
    current_br_active = tk.IntVar(value=1)
    current_def = tk.DoubleVar(value=100)
    current_def_active = tk.IntVar(value=1)
    current_avk = tk.DoubleVar(value=100)
    current_avk_active = tk.IntVar(value=1)
    current_off = tk.DoubleVar(value=100)
    current_off_active = tk.IntVar(value=1)
    current_run = tk.DoubleVar(value=100)
    current_run_active = tk.IntVar(value=1)

    bat_active = {
        'Gap':current_gap_active,
        'Power':current_power_active,
        'Eye':current_eye_active,
        'AvKs':current_avk_active,
        'Babip':current_babip_active,
        'Speed':current_speed_active,
        'Steal':current_steal_active,
        'BR':current_br_active,
        'Off':current_off_active,
        'Run':current_run_active,
        'Def':current_def_active
    }
    

    def update_sliders(position):
        print(sliders)
        global drag_position
        old_position = drag_position
        team_weights[old_position]['Babip'].set(sliders[0][2].get())
        team_weights[old_position]['AvKs'].set(sliders[1][2].get())
        team_weights[old_position]['Power'].set(sliders[2][2].get())
        team_weights[old_position]['Eye'].set(sliders[3][2].get())
        team_weights[old_position]['Gap'].set(sliders[4][2].get())
        team_weights[old_position]['Speed'].set(sliders[6][2].get())
        team_weights[old_position]['Steal'].set(sliders[7][2].get())
        team_weights[old_position]['BR'].set(sliders[8][2].get())
        team_weights[old_position]['Def'].set(sliders[10][2].get())
        team_weights[old_position]['Off'].set(sliders[5][2].get())
        team_weights[old_position]['Run'].set(sliders[9][2].get())
        team_active[old_position]['Babip'].set(sliders[0][3].get())
        team_active[old_position]['AvKs'].set(sliders[1][3].get())
        team_active[old_position]['Power'].set(sliders[2][3].get())
        team_active[old_position]['Eye'].set(sliders[3][3].get())
        team_active[old_position]['Gap'].set(sliders[4][3].get())
        team_active[old_position]['Speed'].set(sliders[6][3].get())
        team_active[old_position]['Steal'].set(sliders[7][3].get())
        team_active[old_position]['BR'].set(sliders[8][3].get())
        team_active[old_position]['Def'].set(sliders[10][3].get())
        team_active[old_position]['Off'].set(sliders[5][3].get())
        team_active[old_position]['Run'].set(sliders[9][3].get())


        current_position.set(position)
        current_babip.set(team_weights[position]['Babip'].get())
        current_avk.set(team_weights[position]['AvKs'].get())
        current_power.set(team_weights[position]['Power'].get())
        current_eye.set(team_weights[position]['Eye'].get())
        current_gap.set(team_weights[position]['Gap'].get())
        current_speed.set(team_weights[position]['Speed'].get())
        current_steal.set(team_weights[position]['Steal'].get())
        current_br.set(team_weights[position]['BR'].get())
        current_def.set(team_weights[position]['Def'].get())
        current_off.set(team_weights[position]['Off'].get())
        current_run.set(team_weights[position]['Run'].get())
        current_babip_active.set(team_active[position]['Babip'].get())
        current_avk_active.set(team_active[position]['AvKs'].get())
        current_power_active.set(team_active[position]['Power'].get())
        current_eye_active.set(team_active[position]['Eye'].get())
        current_gap_active.set(team_active[position]['Gap'].get())
        current_speed_active.set(team_active[position]['Speed'].get())
        current_steal_active.set(team_active[position]['Steal'].get())
        current_br_active.set(team_active[position]['BR'].get())
        current_def_active.set(team_active[position]['Def'].get())
        current_off_active.set(team_active[position]['Off'].get())
        current_run_active.set(team_active[position]['Run'].get())

        drag_position = position

    def export_weights():
        filetypes=[('JSON Files','*.json')]
        gap = current_gap.get()
        power = current_power.get()
        eye = current_eye.get()
        avk = current_avk.get()
        babip = current_babip.get()
        speed = current_speed.get()
        steal = current_steal.get()
        br = current_br.get()
        df = current_def.get()
        gapAct = current_gap_active.get()
        powerAct = current_power_active.get()
        eyeAct = current_eye_active.get()
        avkAct = current_avk_active.get()
        babipAct = current_babip_active.get()
        speedAct = current_speed_active.get()
        stealAct = current_steal_active.get()
        brAct = current_br_active.get()
        dfAct = current_def_active.get()
        off = current_off.get()
        offAct = current_off_active.get()
        run = current_run.get()
        runAct = current_run_active.get()
        literal_weights = {
            'Gap': gap,
            'Power': power,
            'Eye': eye,
            'AvKs': avk,
            'Babip': babip,
            'Speed': speed,
            'Steal': steal,
            'BR': br,
            'Def': df,
            'Off': off,
            'Run': run,
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
            if filename[-5] != '.json':
                filename += '.json'
            try:
                with open(filename, 'w') as file:
                    json.dump(literal_weights, file, ensure_ascii=False, indent=4)
            except:
                messagebox(master=None, message="There was an error - please check that your location is valid.")

    def export_team(team_weights, team_active):
        filetypes=[('JSON Files','*.json')]
        literal_team_data = {}
        weight_types = ['Gap','Power','Eye','Babip','Steal','Speed','AvKs','BR','Def','Off','Run']
        for position in team_weights:
            print(position)
            literal_weights = {}
            for weight in weight_types:
                literal_weights[weight] = team_weights[position][weight].get()
            literal_team_data[position] = literal_weights
        for position in team_active:
            literal_actives = {}
            for weight in weight_types:
                literal_actives[weight] = team_active[position][weight].get()
            literal_team_data[position+'Active'] = literal_actives


            
        filename=fd.asksaveasfilename(
            title="Please Select a location and name for your weights JSON File",
            initialdir='Data\Presets\Teams',
            filetypes=filetypes
        )
        if filename:
            if filename[-5] != '.json':
                filename += '.json'
            try:
                with open(filename, 'w') as file:
                    json.dump(literal_team_data, file, ensure_ascii=False, indent=4)
            except:
                messagebox(master=None, message="There was an error - please check that your location is valid.")

    def import_weights(team_weights, team_active):
        filetypes=[('JSON Files','*.json'),]
        backupweights = team_weights
        backupactive = team_active
        try:
            filename = fd.askopenfilename(
                title="Please locate the batter weights json file",
                initialdir='Data\Presets\Batters',
                filetypes=filetypes
            )
            if filename:
                with open(filename, 'r') as file:
                    literal_weights = json.load(file)
                    current_gap.set(literal_weights['Gap'])
                    current_power.set(literal_weights['Power'])
                    current_eye.set(literal_weights['Eye'])
                    current_avk.set(literal_weights['AvKs'])
                    current_babip.set(literal_weights['Babip'])
                    current_speed.set(literal_weights['Speed'])
                    current_steal.set(literal_weights['Steal'])
                    current_br.set(literal_weights['BR'])
                    current_def.set(literal_weights['Def'])
                    current_off.set(literal_weights['Off'])
                    current_run.set(literal_weights['Run'])
                    current_gap_active.set(literal_weights['GapActive'])
                    current_power_active.set(literal_weights['PowerActive'])
                    current_eye_active.set(literal_weights['EyeActive'])
                    current_avk_active.set(literal_weights['AvKsActive'])
                    current_babip_active.set(literal_weights['BabipActive'])
                    current_speed_active.set(literal_weights['SpeedActive'])
                    current_steal_active.set(literal_weights['StealActive'])
                    current_br_active.set(literal_weights['BRActive'])
                    current_off_active.set(literal_weights['OffActive'])
                    current_def_active.set(literal_weights['DefActive'])
                    current_run_active.set(literal_weights['RunActive'])
        except:
            messagebox(master=None, message="There was an error in loading the weights file.")
            team_weights = backupweights
            team_active = backupactive

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

    def build_position_list(position, bat_weights, batter_list, bat_active):
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
        bat_literals = {}
        for key in bat_weights:
            bat_literals[key] = bat_weights[key]
        request_list = weighting.weight_batter_list(pos_requested, bat_literals, batter_list, isValueChecked.get(), valueMin.get(), valueMax.get(), bat_active)
        if myCardsChecked.get() == 1 and my_list:
            request_list = weighting.filter_my_players(request_list, my_list)
        response_list = weighting.return_culled_nnum_from_list(request_list, 5)
        projected_list = weighting.generate_projected_pcts(response_list)
        stats_list = weighting.generate_projected_stats(projected_list)
        for player in stats_list:
            player['Position'] = position
        return stats_list
        
    def build_team_lists(team_weights, batter_list):
        position_list = ['C','1B','2B','SS','3B','LF','CF','RF','DH']
        list_window = tk.Toplevel()
        list_window.title("List Results for Team Builder Analysis")
        list_window.iconbitmap(r'Data\SmashIcons_Baseball.ico')
        list_window.config(height=800)
        list_tree = ttk.Treeview(list_window, name="player Rating List", height=800)
        list_tree['columns'] = ('Position','Name','Card ID','Year','Weighted Rating','Card Value','OFF','DEF','RUN','AVG','OBP','SLG','OPS','HR')
        list_tree.column('#0', width=30 , minwidth=25)
        list_tree.column("Position", width=40)
        list_tree.column("Name")
        list_tree.column("Card ID", width=50)
        list_tree.column('Year', width=50)
        list_tree.column("Weighted Rating", width=50)
        list_tree.column("Card Value", width=50)
        list_tree.column("OFF", width=50)
        list_tree.column("DEF", width=50)
        list_tree.column("RUN", width=50)
        list_tree.column("AVG", width=50, anchor='center')
        list_tree.column("OBP", width=50, anchor='center')
        list_tree.column("SLG", width=50, anchor='center')
        list_tree.column("OPS", width=50, anchor='center')
        list_tree.column("HR", width=50, anchor='center')
        list_tree.heading("#0")
        list_tree.heading("Position", text="POS", command=lambda: sort_treeview(list_tree, 'POS'))
        list_tree.heading("Name", text="Name", command=lambda: sort_treeview(list_tree, 'Name'))
        list_tree.heading("Card ID", text="ID", command=lambda: sort_treeview(list_tree, 'ID'))
        list_tree.heading('Year', text='Year', command=lambda: sort_treeview(list_tree,'Year'))
        list_tree.heading("Weighted Rating", text="OVR", command=lambda: sort_treeview(list_tree, 'Weighted Rating'))
        list_tree.heading("Card Value", text="VAL", command=lambda:sort_treeview(list_tree, 'Card Value'))
        list_tree.heading("OFF", text="OFF", command=lambda:sort_treeview(list_tree,'OFF'))
        list_tree.heading("DEF", text="DEF", command=lambda:sort_treeview(list_tree,'DEF'))
        list_tree.heading("RUN", text="RUN", command=lambda:sort_treeview(list_tree,'RUN'))
        list_tree.heading("AVG", text="AVG", command=lambda:sort_treeview(list_tree,'AVG'))
        list_tree.heading("OBP", text="OBP", command=lambda:sort_treeview(list_tree,'OBP'))
        list_tree.heading("SLG", text="SLG", command=lambda:sort_treeview(list_tree,'OBP'))
        list_tree.heading("OPS", text="OPS", command=lambda:sort_treeview(list_tree,'OBP'))
        list_tree.heading("HR", text="HR", command=lambda:sort_treeview(list_tree,'HR'))
        team_list = []
        for position in position_list:
            team_list.extend(build_position_list(position, team_weights[position], batter_list, team_active[position]))
        
        for batter in team_list:
            list_tree.insert(parent='', index='end', iid=(str(batter['Position'])+str(batter['Id'])), values=(batter['Position'],(batter['FirstName'] + ' ' + batter['LastName']), batter['Id'], batter['Year'], batter['Rating'], batter['Value'], batter['Offense'], batter['Defense'], batter['Running'], batter['AVG'], batter['OBP'], batter['SLG'],batter['OPS'],batter['HR']) )
        list_tree.pack()

    instructionHeader = header_(canvas, 'Teambuilder Analysis Tool', myFont, 3, 1 ,0)
    instructionHeader.padY(10)
    welcomeHeader = header_(canvas, 'Set Relative Weights Here', myFont, 3, 1, 1)

    sliders = [('BABIP', 2, current_babip, current_babip_active, 'powderblue'),('AvKs', 3, current_avk, current_avk_active, 'powderblue'),('Power', 4, current_power, current_power_active, 'powderblue'), ('Eye', 5, current_eye, current_eye_active, 'powderblue'), ('Gap', 6, current_gap, current_gap_active, 'powderblue'), ('OFFENSE', 7, current_off, current_off_active, 'blue'), ('Speed', 8, current_speed, current_speed_active, 'pink'), ('Steal', 9, current_steal, current_steal_active, 'pink'), ('Baserunning', 10, current_br, current_br_active, 'pink'), ('RUNNING', 11, current_run, current_run_active, 'red'), ('DEFENSE', 12, current_def, current_def_active, 'green')]

    for slider in sliders:
        thisSlider = slider_set(canvas=canvas, text=slider[0], font=myFont, row=slider[1], variable=slider[2], activeVariable=slider[3], troughColor=slider[4])

    filterheader = header_(canvas, 'Card Selection Filters', myFont, 3, 1, 13)
    filterlabel = header_(canvas, 'Card Value Filter', myFont, 1, 0, 14)

    valueMin = tk.DoubleVar(value=40)
    valueMax = tk.DoubleVar(value=100)
    valueSlider = RangeSliderH(canvas, variables=[valueMin, valueMax], min_val=40, max_val=100, padX=20, bar_radius=5, line_width=2, Height=55)
    valueSlider.grid(columnspan=3, row=14, column=1)

    isValueChecked = tk.IntVar()
    valueCheckBox = ttk.Checkbutton(canvas, text="Make Filter Active",variable=isValueChecked,onvalue=True,offvalue=False )
    valueCheckBox.grid(columnspan=1, column=4, row=14)
    isValueChecked.set(1)
    valueCheckBox.state(('!alternate','selected'))

    generateListButton = tk.Button(canvas,text="Generate List", command=lambda:build_team_lists(team_weights=team_weights, batter_list=batter_list), bg='pink')
    generateListButton.grid(column=4,row=16)

    def setSlider(minimum, maximum):
        valueMin.set(minimum)
        valueMax.set(maximum)
        valueSlider.forceValues([minimum,maximum])

    presetsLabel = tk.Label(canvas,text="Card Value Presets", font=myFont)
    presetsLabel.grid(columnspan=3,column=1, row=13)

    presetsheader = header_(canvas, 'Card Value Presets', myFont, 3, 1, 15)
    presetbank = preset_bank(canvas, myFont, 16, valueSlider, valueMax, valueMin)

    importWeightsButton = tk.Button(canvas,text="Import Weights JSON", bg="yellow", command=lambda: import_weights(team_weights=team_weights, team_active=team_active))
    importWeightsButton.grid(column=5,row=2)
    exportWeightsButton = tk.Button(canvas,text="Export Weights JSON", bg="yellow", command=lambda: export_weights())
    exportWeightsButton.grid(column=5,row=3)
    exportTeamButton = tk.Button(canvas,text="Export Team Settings JSON", bg="green", command=lambda: export_team(team_weights=team_weights, team_active=team_active))
    exportTeamButton.grid(column=5,row=5)

    myCardsChecked = tk.IntVar()
    myCardsCheckBox = ttk.Checkbutton(canvas, text="Only MY Cards", variable=myCardsChecked)
    myCardsCheckBox.grid(columnspan=1, column=5, row=10)
    myCardsChecked.set(1)
    myCardsCheckBox.state(('!alternate','selected'))

    currentPositionCRadioButton = tk.Radiobutton(canvas, text="C",value="C",state='normal', variable=current_position, command=lambda:update_sliders('C'))
    currentPositionCRadioButton.grid(column=0,row=18)
    currentPosition1BRadioButton = tk.Radiobutton(canvas,text="1B",value="1B",state='normal',variable=current_position, command=lambda:update_sliders('1B'))
    currentPosition1BRadioButton.grid(column=1,row=18)
    currentPosition2BRadioButton = tk.Radiobutton(canvas,text="2B",value="2B",state='normal',variable=current_position,command=lambda:update_sliders('2B'))
    currentPosition2BRadioButton.grid(column=2,row=18)
    currentPositionSSRadioButton = tk.Radiobutton(canvas,text="SS",value="SS",state='normal',variable=current_position,command=lambda:update_sliders('SS'))
    currentPositionSSRadioButton.grid(column=3,row=18)
    currentPosition3BRadioButton = tk.Radiobutton(canvas,text="3B",value="3B",state='normal',variable=current_position,command=lambda:update_sliders('3B'))
    currentPosition3BRadioButton.grid(column=0,row=19)
    currentPositionLFRadioButton = tk.Radiobutton(canvas,text="LF",value="LF",state='normal',variable=current_position,command=lambda:update_sliders('LF'))
    currentPositionLFRadioButton.grid(column=1,row=19)
    currentPositionCFRadioButton = tk.Radiobutton(canvas,text="CF",value="CF",state='normal',variable=current_position,command=lambda:update_sliders('CF'))
    currentPositionCFRadioButton.grid(column=2,row=19)
    currentPositionRFRadioButton = tk.Radiobutton(canvas,text="RF",value="RF",state='normal',variable=current_position,command=lambda:update_sliders('RF'))
    currentPositionRFRadioButton.grid(column=3,row=19)
    currentPositionDHRadioButton = tk.Radiobutton(canvas,text="DH",value="DH",state='active',variable=current_position,command=lambda:update_sliders('DH'))
    currentPositionDHRadioButton.grid(column=4,row=19)

    currentPositionDHRadioButton.select()