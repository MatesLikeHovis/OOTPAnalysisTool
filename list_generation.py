import classes
import csv



def make_lists(csv_file):
    batter_list = []
    pitcher_list = []
    with open(csv_file,'r') as data_set:
        csvreader = csv.DictReader(data_set)
        for row in csvreader:
            if int(row['Position']) == 1:
                Cntrl = int(row['Control'])
                DefP = int(row['Pos Rating P'])
                FirstName = row['FirstName']
                LastName = row['LastName']
                Hold = int(row['Hold'])
                Stam = int(row['Stamina'])
                Stuff = int(row['Stuff'])
                Type = int(row['Pitcher Role'])
                Value = int(row['Card Value'])
                Id = int(row['Card ID'])
                Pbabip = int(row['pBABIP'])
                PhR = int(row['pHR'])
                Throws = int(row['Throws'])
                this_pitcher = classes.Pitcher(Id,Value,LastName,FirstName,Type,Stuff,PhR,Pbabip,Cntrl,Stam,Hold,DefP,Throws)
                pitcher_list.append(this_pitcher)
            Id = int(row['Card ID'])
            Value = int(row['Card Value'])
            LastName = row['LastName']
            FirstName = row['FirstName']
            Year = int(row['Year'])
            Pos = int(row['Position'])
            Gap = int(row['Gap'])
            Power = int(row['Power'])
            Eye = int(row['Eye'])
            AvKs = int(row['Avoid Ks'])
            Babip = int(row['BABIP'])
            GapvL = int(row["Gap vL"])
            GapvR = int(row["Gap vR"])
            PowervL = int(row["Power vL"])
            PowervR = int(row['Power vR'])
            EyevL = int(row['Eye vL'])
            EyevR = int(row['Eye vR'])
            avKvL = int(row['Avoid K vL'])
            avKvR = int(row['Avoid K vR'])
            BabipvL = int(row['BABIP vL'])
            BabipvR = int(row['BABIP vR'])
            Spd = int(row['Speed'])
            Stl = int(row['Stealing'])
            Br = int(row['Baserunning'])
            DefC = int(row['Pos Rating C'])
            Def1B = int(row['Pos Rating 1B'])
            Def2B = int(row['Pos Rating 2B'])
            Def3B = int(row['Pos Rating 3B'])
            DefSS = int(row['Pos Rating SS'])
            DefLF = int(row['Pos Rating LF'])
            DefCF = int(row['Pos Rating CF'])
            DefRF = int(row['Pos Rating RF'])
            this_batter = classes.Batter(Id,Value,LastName,FirstName,Year,Pos,Gap,Power,Eye,AvKs,Babip,Spd,Stl,Br,DefC,Def1B,Def2B,DefSS,Def3B,DefLF,DefCF,DefRF,GapvL,PowervL,EyevL,avKvL,BabipvL,GapvR,PowervR,EyevR,avKvR,BabipvR)
            batter_list.append(this_batter)
    print("Data Loaded")
    return batter_list, pitcher_list

def make_my_lists(csv_file):
    my_list = []
    with open(csv_file,'r') as data_set:
        csvreader = csv.DictReader(data_set)
        for row in csvreader:
            this_batter = (row['Name'])
            my_list.append(this_batter)
    print("My List Loaded")
    return my_list