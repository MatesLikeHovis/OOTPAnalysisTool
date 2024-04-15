import tkinter as tk

def batter_weight_sliders(canvas, myFont, weights):
    babipSlider = tk.Scale(canvas, variable=weights['babipweight'], from_=0,to=100, orient='horizontal', length=400)
    avkSlider = tk.Scale(canvas, variable=weights['avkweight'], from_=0,to=100, orient='horizontal', length=400)
    powerSlider = tk.Scale(canvas, variable=weights['powerweight'], from_=0,to=100, orient='horizontal', length=400)
    eyeSlider = tk.Scale(canvas, variable=weights['eyeweight'], from_=0, to=100, orient='horizontal', length=400)
    gapSlider = tk.Scale(canvas, variable=weights['gapweight'], from_=0, to=100, orient='horizontal', length=400)
    speedSlider = tk.Scale(canvas, variable=weights['speedweight'], from_=0, to=100, orient='horizontal', length=400)
    stealSlider = tk.Scale(canvas, variable=weights['stealweight'], from_=0, to=100, orient='horizontal', length=400)
    brSlider = tk.Scale(canvas, variable=weights['brweight'], from_=0, to=100, orient='horizontal', length=400)
    defSlider = tk.Scale(canvas, variable=weights['defweight'], from_=0, to=100, orient='horizontal', length=400)
    babipLabel = tk.Label(canvas,text="BABIP", font=myFont)
    babipLabel.grid(column=0, row=2)
    babipSlider.grid(columnspan=3, column=1, row=2)
    avkLabel = tk.Label(canvas,text="Avoid K's", font=myFont)
    avkLabel.grid(column=0, row=3)
    avkSlider.grid(columnspan=3, column=1, row=3)
    powerLabel = tk.Label(canvas,text="Power", font=myFont)
    powerLabel.grid(column=0, row=4)
    powerSlider.grid(columnspan=3, column=1, row=4)
    eyeLabel = tk.Label(canvas,text="Eye", font=myFont)
    eyeLabel.grid(column=0, row=5)
    eyeSlider.grid(columnspan=3, column=1, row=5)
    gapLabel = tk.Label(canvas,text="Gap Power", font=myFont)
    gapLabel.grid(column=0, row=6)
    gapSlider.grid(columnspan=3, column=1, row=6)
    speedLabel = tk.Label(canvas,text="Speed", font=myFont)
    speedLabel.grid(column=0, row=7)
    speedSlider.grid(columnspan=3, column=1, row=7)
    stealLabel = tk.Label(canvas,text="Steal Ability", font=myFont)
    stealLabel.grid(column=0, row=8)
    stealSlider.grid(columnspan=3, column=1, row=8)
    brLabel = tk.Label(canvas,text="Baserunning", font=myFont)
    brLabel.grid(column=0, row=9)
    brSlider.grid(columnspan=3, column=1, row=9)
    defLabel = tk.Label(canvas,text="Defense", font=myFont)
    defLabel.grid(column=0, row=10)
    defSlider.grid(columnspan=3, column=1, row=10)

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