import tkinter as tk
from tkinter import ttk

class Batter:
    def __init__(self, id, value, lastName, firstName, year, pos, gap, power, eye, avKs, babip, spd, stl, br, defc, def1b, def2b, defss, def3b, deflf, defcf, defrf, gapvL, powervL, eyevL, avKvL, babipvL, gapvR, powervR, eyevR, avKvR, babipvR):
        self.Id = id
        self.Value = value
        self.LastName = lastName
        self.FirstName = firstName
        self.Year = year
        self.Pos = pos
        self.Gap = gap
        self.Power = power
        self.Eye = eye
        self.AvKs = avKs
        self.Babip = babip
        self.Spd = spd
        self.Stl = stl
        self.Br = br
        self.DefC = defc
        self.Def1B = def1b
        self.Def2B = def2b
        self.Def3B = def3b
        self.DefSS = defss
        self.DefLF = deflf
        self.DefCF = defcf
        self.DefRF = defrf
        self.GapvL = gapvL
        self.GapvR = gapvR
        self.EyevL = eyevL
        self.EyevR = eyevR
        self.PowervL = powervL
        self.PowervR = powervR
        self.BabipvL = babipvL
        self.BabipvR = babipvR
        self.AvKvL = avKvL
        self.AvKvR = avKvR

class Pitcher:
    def __init__(self, id, value, lastName, firstName, type, stuff, pHR, pBabip, cntrl, stam, hold, defP, throws):
        self.Id = id
        self.Value = value
        self.LastName = lastName
        self.FirstName = firstName
        self.Type = type
        self.Stuff = stuff
        self.Phr = pHR
        self.Pbabip = pBabip
        self.Cntrl = cntrl
        self.Stam = stam
        self.Hold = hold
        self.DefP = defP
        self.Throws = throws

class bat_weights:
    def __init__(self, gap, power, eye, avk, babip, speed, steal, br, defense):
        self.Gap = gap
        self.Power = power
        self.Eye = eye
        self.Avk = avk
        self.Babip = babip
        self.Speed = speed
        self.Steal = steal
        self.Br = br
        self.Def = defense

class slider_set:
    def __init__(self, canvas, text, font, row, variable, activeVariable, troughColor):
        self.canvas = canvas
        self.text = text
        self.font = font
        self.row = row
        self.variable = variable
        self.ActiveVariable = activeVariable

        self.thisLabel = tk.Label(self.canvas, text=self.text, font=self.font)
        self.thisLabel.grid(column=0, row=self.row)
        self.thisSlider = tk.Scale(self.canvas, variable=self.variable, from_=0, to=100, length=400, orient='horizontal', relief='groove', troughcolor=troughColor)
        self.thisSlider.grid(columnspan=3, column=1, row=self.row)
        self.thisActiveCheck = ttk.Checkbutton(self.canvas, text="Active", variable=self.ActiveVariable)
        self.thisActiveCheck.grid(column=4, row=self.row)
        self.thisActiveCheck.state(('!alternate','selected'))

class header_:
    def __init__(self, canvas, text, font, span, col, row):
        self.canvas = canvas
        self.text = text
        self.font = font
        self.span = span
        self.col = col
        self.row = row

        self.thisLabel = tk.Label(self.canvas, text=self.text, font=self.font)
        self.thisLabel.grid(columnspan=self.span, column=self.col, row=self.row)

    def padY(self, padding):
        self.thisLabel.config(pady=padding)

class preset_button:
    def __init__(self, canvas, text, font, bgColor, valueSlider, valueMinVar, valueMaxVar, valueMin, valueMax, col, row):
        self.canvas = canvas
        self.text = text
        self.font = font
        self.bgColor = bgColor
        self.valueMinVar = valueMinVar
        self.valueMaxVar = valueMaxVar
        self.ValueMin = valueMin
        self.ValueMax = valueMax
        self.col = col
        self.row = row

        def setSlider(valueMin, valueMax):
            valueMinVar.set(valueMin)
            valueMaxVar.set(valueMax)
            valueSlider.forceValues([valueMin,valueMax])
        self.thisButton = tk.Button(canvas,text=text, command=lambda: setSlider(valueMin, valueMax), background=bgColor)
        self.thisButton.grid(column=col, row=row)

class preset_bank:
    def __init__(self, canvas, font, rowStart, valueSlider, valueMinVar, valueMaxVar):
        self.Canvas = canvas
        self.Font = font
        self.RowStart = rowStart
        self.ValueSlider = valueSlider
        self.ValueMinVar = valueMinVar
        self.ValueMaxVar = valueMaxVar

        self.ironPreset = preset_button(self.Canvas, '<= Iron', self.Font, 'Gray', self.ValueSlider, self.ValueMinVar, self.ValueMaxVar, 40, 59.9, 0, self.RowStart)
        self.bronzePreset = preset_button(self.Canvas, '<= Bronze', self.Font, 'brown', self.ValueSlider, self.ValueMinVar, self.ValueMaxVar, 40, 69.9, 1, self.RowStart)
        self.silverPreset = preset_button(self.Canvas, '<= Silver', self.Font, 'silver', self.ValueSlider, self.ValueMinVar, self.ValueMaxVar, 40, 79.9, 2, self.RowStart)
        self.goldPreset = preset_button(self.Canvas, '<= Gold', self.Font, 'gold', self.ValueSlider, self.ValueMinVar, self.ValueMaxVar, 40, 89.9, 3, self.RowStart)
        self.diamondPreset = preset_button(self.Canvas, '<= Diamond', self.Font, 'lightblue', self.ValueSlider, self.ValueMinVar, self.ValueMaxVar, 40, 99.9, 1, (self.RowStart + 1))
        self.allPreset = preset_button(self.Canvas, 'All Values', self.Font, 'white', self.ValueSlider, self.ValueMinVar, self.ValueMaxVar, 40, 100, 2, (self.RowStart + 1))