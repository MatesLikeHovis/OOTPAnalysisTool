import classes
import tensorflow as tf
import numpy as np

def weight_batter_list(position, weights, batter_list, isValueChecked, valueMin, valueMax, active_list, platoon=''):
    weighted_list = []
    for batter in batter_list:
        is_included = True
        defense_score = 0
        defense_raw = 0
        match position:
            case 2:
                defense_raw = batter.DefC
            case 3:
                defense_raw = batter.Def1B
            case 4:
                defense_raw = batter.Def2B
            case 5:
                defense_raw = batter.Def3B
            case 6:
                defense_raw = batter.DefSS
            case 7:
                defense_raw = batter.DefLF
            case 8:
                defense_raw = batter.DefCF
            case 9:
                defense_raw = batter.DefRF
            case 10:
                defense_raw = 0
        defense_score = defense_raw * weights['Def'].get()
        if defense_score == 0 and position != 10:
            is_included = False
        offense_score = 0
        running_score = 0
        if platoon == '':
            gap = batter.Gap
            power = batter.Power
            eye = batter.Eye
            avKs = batter.AvKs
            babip = batter.Babip
        elif platoon == 'vR':
            gap = batter.GapvR
            power = batter.PowervR
            eye = batter.EyevR
            avKs = batter.AvKvR
            babip = batter.BabipvR
        elif platoon == 'vL':
            gap = batter.GapvL
            power = batter.PowervL
            eye = batter.EyevL
            avKs = batter.AvKvL
            babip = batter.BabipvL
        offense_weights = 0
        defense_weights = 0
        running_weights = 0
        if (active_list['Gap'].get() == 1): 
            offense_score += gap * weights['Gap'].get()
            offense_weights += weights['Gap'].get()
        if (active_list['Power'].get() == 1): 
            offense_score += power * weights['Power'].get()
            offense_weights += weights['Power'].get()
        if (active_list['Eye'].get() == 1): 
            offense_score += eye * weights['Eye'].get()
            offense_weights += weights['Eye'].get()
        if (active_list['AvKs'].get() == 1): 
            offense_score += avKs * weights['AvKs'].get()
            offense_weights += weights['AvKs'].get()
        if (active_list['Babip'].get() == 1): 
            offense_score += babip * weights['Babip'].get()
            offense_weights += weights['Babip'].get()
        if (active_list['Speed'].get() == 1): 
            running_score += batter.Spd * weights['Speed'].get()
            running_weights += weights['Speed'].get()
        if (active_list['Steal'].get() == 1):
            running_score += batter.Stl * weights['Steal'].get()
            running_weights += weights['Steal'].get()
        if (active_list['BR'].get() == 1): 
            running_score += batter.Br * weights['BR'].get()
            running_weights += weights['BR'].get()
        if (active_list['Def'].get() == 1): 
            defense_weights = weights['Def'].get()
        if (isValueChecked == 1) and not (valueMin <= batter.Value <= valueMax):
            is_included = False
        if (offense_weights == 0 or active_list['Off'].get() == 0):
            offense_rating = 0
        else:
            offense_rating = offense_score / offense_weights
        round(offense_rating,2)
        if running_weights == 0 or active_list['Run'].get() == 0:
            running_rating = 0
        else:
            running_rating = running_score / running_weights
        round(running_rating, 2)
        if defense_weights == 0 or active_list['Def'].get() == 0:
            defense_rating = 0
        else:
            defense_rating = defense_score / defense_weights
        sum_weights = running_weights + defense_weights + offense_weights
        total_score = offense_rating * offense_weights + defense_rating * defense_weights + running_rating * running_weights
        total_score /= sum_weights
        round(total_score,1)
        if total_score == 0:
            is_included = False
        if is_included:
            weighted_list.append({
                'FirstName':batter.FirstName,
                'LastName':batter.LastName,
                'Id':batter.Id,
                'Year':batter.Year,
                'Rating':float(int(total_score * 10)/10),
                'Value':batter.Value,
                'Offense':int(offense_rating),
                'Defense':int(defense_rating),
                'Running':int(running_rating),
                'Babip':babip,
                'Power':power,
                'Eye':eye,
                'AvKs':avKs,
                'Gap':batter.Gap
                })

    return weighted_list

def weight_pitcher_list(type, weights, pitcher_list, isValueChecked, valueMin, valueMax, active_list):
    weighted_list = []
    is_included = True
    for pitcher in pitcher_list:
        if type == 'SP':
            if pitcher.Type == 11:
                is_included = True
            else:
                is_included = False
        if type == 'RP':
            if pitcher.Type == 12:
                is_included = True
            else:
                is_included = False
        if type == 'CL':
            if pitcher.Type == 13:
                is_included = True
            else:
                is_included = False
        if type == 'RP/CL':
            if pitcher.Type == 11:
                is_included = False
            else:
                is_included = True
        if type == 'SP/RP/CL':
            is_included = True
        total_score = 0
        movement_score = 0
        other_score = 0
        total_score += pitcher.Stuff * weights['Stuff'].get()
        movement_score += pitcher.Phr * weights['PHR'].get()
        movement_score += pitcher.Pbabip * weights['PBABIP'].get()
        total_score += pitcher.Cntrl * weights['Control'].get()
        other_score += pitcher.Stam * weights['Stamina'].get()
        other_score += pitcher.Hold * weights['Hold'].get()
        other_score += pitcher.DefP * weights['Defense'].get()
        total_score += movement_score
        total_score += other_score
        total_score /= (weights['Stuff'].get() + weights['PHR'].get() + weights['PBABIP'].get() + weights['Control'].get() + weights['Stamina'].get() + weights['Hold'].get() + weights['Defense'].get())
        if isValueChecked and not (valueMin <= pitcher.Value <= valueMax):
            is_included = False
        if is_included:
            if (weights['Stamina'].get() + weights['Hold'].get() + weights['Defense'].get() == 0):
                other_rating = 0
            else:
                other_rating = other_score / (weights['Stamina'].get() + weights['Hold'].get() + weights['Defense'].get())
            if (weights['PHR'].get()+weights['PBABIP'].get() == 0):
                movement_rating = 0
            else:
                movement_rating = movement_score / (weights['PHR'].get()+weights['PBABIP'].get())
            other_rating = float(int(other_rating*10)/10)
            movement_rating = float(int(movement_rating*10)/10)
            weighted_list.append({
                'FirstName':pitcher.FirstName,
                'LastName':pitcher.LastName,
                'Id':pitcher.Id,
                'Rating':float(int(total_score * 10)/10),
                'Value':pitcher.Value,
                'Stuff':pitcher.Stuff,
                'Movement':movement_rating,
                'Control':pitcher.Cntrl,
                'Other':other_rating,
                'PBABIP':pitcher.Pbabip,
                'PHR':pitcher.Phr
                })
    return weighted_list

def load_neural_network(filename):
    model = tf.keras.models.load_model(filename)
    return model

def generate_projected_pcts(batter_list):
    gap_to_xbhpct_slope = 0.0021773693
    gap_to_xbhpct_intercept = -0.07695567

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
        batter['XBHPct'] = ((gap_to_xbhpct_slope * (batter['Gap'])) + gap_to_xbhpct_intercept)
        if batter['XBHPct'] > 0.19:
            batter['XBHPct'] = 0.19
        if batter['XBHPct'] < 0:
            batter['XBHPct'] = 0
    
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
            if (so < 0): so = 0
            if (bb < 0): bb = 0
            if (hr < 0): hr = 0
            bip = (pa - (so + bb + hr))
            h = bip * batter['babip_pct']
            if h < 0: h = 0
            singles = h * (1 - batter['XBHPct'])
            xbh = h - singles
            if (xbh < 0): xbh = 0
            tb = (singles + (xbh * 2.3) + (hr * 4))
            ab = pa - bb
            slg = tb / ab
            avg = h / ab
            if avg < 0: avg = 0
            obp = (bb + h) / pa
            if obp < 0: obp = 0
            ops = slg + obp
            if ops < 0: ops = 0

            batter['HR'] = int(hr)
            batter['AVG'] = round(avg,3)
            batter['OBP'] = round(obp,3)
            batter['SLG'] = round(slg,3)
            batter['OPS'] = round(ops,3)
        return batter_list

def return_culled_nnum_from_list(list, number):
    sorted_list = sorted(list, key=lambda x: x['Rating'], reverse=True)
    culled_list = sorted_list[:number]
    return culled_list

def return_nnum_from_list(list):
    sorted_list = sorted(list, key=lambda x: x['Rating'], reverse=True)
    return sorted_list

def filter_my_players(full_list, my_list):
    print('filtering list')
    filtered_list = []
    for player in full_list:
        if (player['FirstName'] + ' ' + player['LastName']) in my_list:
            filtered_list.append(player)
    return filtered_list