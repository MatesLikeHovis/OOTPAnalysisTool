import csv
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def make_stats_list(stats_file):
    player_stats_list = []
    with open(stats_file,'r',errors='ignore') as data_set:
        csvreader = csv.DictReader(data_set)
        for row in csvreader:
            this_player = {}
            this_player['Name'] = row['Name']
            nameList = this_player['Name'].split(' ')
            this_player['FirstName'] = nameList[0]
            this_player['LastName'] = this_player['Name'][(len(this_player['FirstName'])+1):]
            this_player['PA'] = int(row['PA'])
            this_player['HR%'] = float(row['HR%'])
            this_player['SO%'] = float(row['SO%'])
            this_player['BB%'] = float(row['BB%'])
            this_player['XBH%'] = float(row['XBH%'])
            this_player['X/H%'] = float(row['X/H%'])
            this_player['SO'] = int(row['SO'])
            this_player['OBP'] = float(row['OBP'])
            this_player['BA'] = float(row['BA'])
            this_player['BAbip'] = float(row['BAbip'])
            player_stats_list.append(this_player)
    return player_stats_list

def make_pitching_stats_list(stats_file):
    player_stats_list = []
    with open(stats_file,'r',errors='ignore') as data_set:
        csvreader = csv.DictReader(data_set)
        for row in csvreader:
            this_pitcher = {}
            this_pitcher['Name'] = row['Name']
            nameList = this_pitcher['Name'].split(' ')
            this_pitcher['FirstName'] = nameList[0]
            this_pitcher['LastName'] = this_pitcher['Name'][(len(this_pitcher['FirstName'])+1):]
            this_pitcher['IP'] = int(round(float(row['IP']),0))
            this_pitcher['ERA'] = float(row['ERA'])
            this_pitcher['BB9'] = float(row['BB9'])
            this_pitcher['H9'] = float(row['H9'])
            this_pitcher['HR9'] = float(row['HR9'])
            this_pitcher['SO9'] = float(row['SO9'])
            player_stats_list.append(this_pitcher)
    return player_stats_list

def make_fielding_stats_list(stats_file):
    player_stats_list = []
    with open(stats_file,'r',errors='ignore') as data_set:
        csvreader = csv.DictReader(data_set)
        for row in csvreader:
            this_player = {}
            this_player['Name'] = row['Name']
            nameList = this_player['Name'].split(' ')
            this_player['FirstName'] = nameList[0]
            this_player['LastName'] = this_player['Name'][(len(this_player['FirstName'])+1):]
            this_player['Pos'] = (row['Position'])
            this_player['Rtotyr'] = float(row['Rtot/yr'])
            this_player['Rdrsyr'] = float(row['Rdrs/yr'])
            player_stats_list.append(this_player)
    return player_stats_list

def make_batter_list(ratings_csv_location, only2024):
    with open(ratings_csv_location,'r') as data_set:
        csvreader = csv.DictReader(data_set)
        batter_list = []
        for row in csvreader:
            if int(row['Position']) == 1:
                pass
            else:
                this_batter = {}
                this_batter['Id'] = int(row['Card ID'])
                this_batter['Year'] = int(row['Year'])
                this_batter['LastName'] = row['LastName']
                this_batter['FirstName'] = row['FirstName']
                this_batter['Pos'] = int(row['Position'])
                this_batter['Gap'] = int(row['Gap'])
                this_batter['Power'] = int(row['Power'])
                this_batter['Eye'] = int(row['Eye'])
                this_batter['AvKs'] = int(row['Avoid Ks'])
                this_batter['Babip'] = int(row['BABIP'])
                this_batter['Spd'] = int(row['Speed'])
                this_batter['Stl'] = int(row['Stealing'])
                this_batter['Br'] = int(row['Baserunning'])
                this_batter['Pos Rating C'] = row['Pos Rating C']
                this_batter['Pos Rating 1B'] = row['Pos Rating 1B']
                this_batter['Pos Rating 2B'] = row['Pos Rating 2B']
                this_batter['Pos Rating 3B'] = row['Pos Rating 3B']
                this_batter['Pos Rating SS'] = row['Pos Rating SS']
                this_batter['Pos Rating LF'] = row['Pos Rating LF']
                this_batter['Pos Rating CF'] = row['Pos Rating CF']
                this_batter['Pos Rating RF'] = row['Pos Rating RF']
                if this_batter['Year'] == 2024 and only2024:
                    batter_list.append(this_batter)
                elif not only2024:
                    batter_list.append(this_batter)
    return batter_list

def make_batter_list_simple(ratings_csv_location, only2024):
    with open(ratings_csv_location,'r') as data_set:
        csvreader = csv.DictReader(data_set)
        batter_list = []
        for row in csvreader:
            if int(row['Position']) == 1:
                pass
            else:
                this_batter = {}
                this_batter['Id'] = int(row['Card ID'])
                this_batter['Year'] = int(row['Year'])
                this_batter['LastName'] = row['LastName']
                this_batter['FirstName'] = row['FirstName']
                this_batter['Pos'] = int(row['Position'])
                this_batter['Gap'] = int(row['Gap'])
                this_batter['Power'] = int(row['Power'])
                this_batter['Eye'] = int(row['Eye'])
                this_batter['AvKs'] = int(row['Avoid Ks'])
                this_batter['Babip'] = int(row['BABIP'])
                this_batter['Spd'] = int(row['Speed'])
                this_batter['Stl'] = int(row['Stealing'])
                if row['babip%'] != '': this_batter['BAbip'] = float(row['babip%'])
                if row['HR%'] != '': this_batter['HR%'] = float(row['HR%'])
                if row['SO%'] != '': this_batter['SO%'] = float(row['SO%'])
                if row['BB%'] != '': this_batter['BB%'] = float(row['BB%'])
                if this_batter['Year'] == 2024 and only2024:
                    batter_list.append(this_batter)
                elif not only2024:
                    batter_list.append(this_batter)
    return batter_list

def make_pitcher_list(ratings_csv_location, only2024):
    with open(ratings_csv_location,'r') as data_set:
        csvreader = csv.DictReader(data_set)
        pitcher_list = []
        for row in csvreader:
            if int(row['Position']) == 1:
                this_pitcher = {}
                this_pitcher['Id'] = int(row['Card ID'])
                this_pitcher['Year'] = int(row['Year'])
                this_pitcher['LastName'] = row['LastName']
                this_pitcher['FirstName'] = row['FirstName']
                this_pitcher['Pos'] = int(row['Position'])
                this_pitcher['Control'] = int(row['Control'])
                this_pitcher['Stuff'] = int(row['Stuff'])
                this_pitcher['pBABIP'] = int(row['pBABIP'])
                this_pitcher['pHR'] = int(row['pHR'])
                if this_pitcher['Year'] == 2024 and only2024:
                    pitcher_list.append(this_pitcher)
                elif not only2024:
                    pitcher_list.append(this_pitcher)
    return pitcher_list

def make_pitcher_list_for_era(ratings_csv_location):
    with open(ratings_csv_location,'r') as data_set:
        csvreader = csv.DictReader(data_set)
        pitcher_list = []
        for row in csvreader:
            this_pitcher = {}
            this_pitcher['ERA'] = float(row['ERA'])
            this_pitcher['WHIP'] = float(row['WHIP'])
            this_pitcher['H9'] = float(row['H9'])
            this_pitcher['HR9'] = float(row['HR9'])
            this_pitcher['BB9'] = float(row['BB9'])
            this_pitcher['SO9'] = float(row['SO9'])
            pitcher_list.append(this_pitcher)
    return pitcher_list

def merge_lists(stats_list, batter_list):
    for stat_batter in stats_list:
        for rating_batter in batter_list:
            if (rating_batter['FirstName'][:4] == stat_batter['FirstName'][:4] and rating_batter['LastName'][:6] == stat_batter['LastName'][:6]):
                ratingList = ['Gap','Power','Eye','AvKs','Babip','Spd','Stl','Br']
                for rating in ratingList:
                    stat_batter[rating] = rating_batter[rating]
    return stats_list
    
def merge_fielding_lists(fielding_stats_list, batter_list):
    for stat_batter in fielding_stats_list:
        for rating_batter in batter_list:
            if (rating_batter['FirstName'][:4] == stat_batter['FirstName'][:4] and rating_batter['LastName'][:6] == stat_batter['LastName'][:6]):
                if (rating_batter['Pos'] == 2 and stat_batter['Pos'] == 'C'):
                    stat_batter['Defense'] = rating_batter['Pos Rating C']
                if (rating_batter['Pos'] == 3 and stat_batter['Pos'] == '1B'):
                    stat_batter['Defense'] = rating_batter['Pos Rating 1B']
                if (rating_batter['Pos'] == 4 and stat_batter['Pos'] == '2B'):
                    stat_batter['Defense'] = rating_batter['Pos Rating 2B']
                if (rating_batter['Pos'] == 5 and stat_batter['Pos'] == '3B'):
                    stat_batter['Defense'] = rating_batter['Pos Rating 3B']
                if (rating_batter['Pos'] == 6 and stat_batter['Pos'] == 'SS'):
                    stat_batter['Defense'] = rating_batter['Pos Rating SS']
                if (rating_batter['Pos'] == 7 and stat_batter['Pos'] == 'LF'):
                    stat_batter['Defense'] = rating_batter['Pos Rating LF']
                if (rating_batter['Pos'] == 8 and stat_batter['Pos'] == 'CF'):
                    stat_batter['Defense'] = rating_batter['Pos Rating CF']
                if (rating_batter['Pos'] == 9 and stat_batter['Pos'] == 'RF'):
                    stat_batter['Defense'] = rating_batter['Pos Rating RF']
    return fielding_stats_list

def merge_pitching_lists(stats_list, pitcher_list):
    for stat_pitcher in stats_list:
        for rating_pitcher in pitcher_list:
            if (rating_pitcher['FirstName'][:4] == stat_pitcher['FirstName'][:4] and rating_pitcher['LastName'][:6] == stat_pitcher['LastName'][:6]):
                ratingList = ['Control','Stuff','pBABIP','pHR']
                for rating in ratingList:
                    stat_pitcher[rating] = rating_pitcher[rating]
    return stats_list

def cull_missing(stats_list):
    culled_list = []
    for batter in stats_list:
        if 'BAbip' in batter:
            culled_list.append(batter)
    return culled_list

def cull_missing_fielding(stats_list):
    culled_list = []
    for fielder in stats_list:
        if 'Defense' in fielder:
            culled_list.append(fielder)
    return culled_list

def cull_missing_pitcher(stats_list):
    culled_list = []
    for pitcher in stats_list:
        if 'Stuff' in pitcher:
            culled_list.append(pitcher)
    return culled_list

ratings_csv_location = 'Data\CSV Files\pt_card_list.csv'
stats_csv_location = 'Data\CSV Files\Statistics PCT - Sheet1.csv'
fielding_csv_location = 'Data\CSV Files\Fielding Statistics - Sheet1.csv'
pitching_csv_location = 'Data\CSV Files\Pitching Statistics - Sheet1.csv'

batter_list = make_batter_list(ratings_csv_location, True)
all_batters_list = make_batter_list(ratings_csv_location, False)
pitcher_list = make_pitcher_list(ratings_csv_location, True)
pitching_stats_list = make_pitching_stats_list(pitching_csv_location)

stats_list = make_stats_list(stats_csv_location)
stats_list = merge_lists(stats_list, batter_list)

#fielding_stats_list = make_fielding_stats_list(fielding_csv_location)
#merged_fielding_stats_list = merge_fielding_lists(fielding_stats_list, batter_list)
#culled_fielding_list = cull_missing_fielding(merged_fielding_stats_list)

#pitching_list = make_pitching_stats_list(pitching_csv_location)
#merged_pitching_list = merge_pitching_lists(pitching_stats_list, pitcher_list)
#culled_pitching_list = cull_missing_pitcher(merged_pitching_list)

#already_mixed_list = make_batter_list_simple('OOTP Master with Stats - Sheet1.csv', False)
#culled_mixed_list = cull_missing(already_mixed_list)

#era_pitcher_list = make_pitcher_list_for_era('ERA per9 1980+ - Sheet1.csv')

"""
def linear_regression(list, source, target, destfile):

    player_list = {}
    for player in list:
            try:
                this_player = {}
                this_player[target] = player[target]
                this_player[source] = player[source]
                player_list.append(this_player)
            except:
                pass

    df = pd.DataFrame(player_list)

    # Split the dataset into training and testing sets
    train_df, test_df = train_test_split(df, test_size=0.1, random_state=0)

    # Separate features and target variable
    X_train = train_df.drop(columns=[target])
    y_train = train_df[target]
    X_test = test_df.drop(columns=[target])
    y_test = test_df[target]

    model = tf.keras.Sequential([
        tf.keras.layers.Dense(units=1, input_shape=[1])  # Single unit for linear regression
        ])
    model.compile(optimizer='sgd', loss='mean_squared_error')

    # Train the model
    model.fit(X_train, y_train, epochs=175)

def neural_network_AVG(list, source_variable, target_variable, description):
    print(list)
    avg_list = []

    for batter in list:
        try:
            avg_batter = {}
            avg_batter[target_variable] = batter[target_variable]
            avg_batter[source_variable] = batter[source_variable]
            avg_list.append(avg_batter)
        except:
            pass

    df = pd.DataFrame(avg_list)
    print(df)

    # Split the dataset into training and testing sets
    train_df, test_df = train_test_split(df, test_size=0.1, random_state=0)
    
    train_df.reset_index(drop=True, inplace=True)
    test_df.reset_index(drop=True, inplace=True)

    # Separate features and target variable
    X_train = train_df.drop(columns=[source_variable])
    y_train = train_df[source_variable]
    X_test = test_df.drop(columns=[source_variable])
    y_test = test_df[source_variable]

    print(X_train)
    print(y_train)
    
    # Create a normalization layer
    normalization_layer = tf.keras.layers.Normalization()

    # Adapt the normalization layer to your training data
    normalization_layer.adapt(np.array(X_train))

    # Define the neural network model
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(X_train.shape[1],)),
        normalization_layer,
        tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(1)
    ])

    # Compile the model
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Train the model
    history = model.fit(X_train, y_train, epochs=300, batch_size=32, validation_split=0.2, verbose=1)

    # Evaluate the model
    test_loss = model.evaluate(X_test, y_test)
    print(f"Test Loss: {test_loss}")

    # Make predictions
    predictions = model.predict(X_test) 

    test_df_reset = test_df.reset_index(drop=True)
    # Merge the original data with the denormalized predictions
    merged_data = pd.concat([test_df_reset, pd.DataFrame(predictions, columns=[target_variable])], axis=1)

    print(merged_data)
    merged_data.to_csv(description + ' Prediction', index=False)

    model.save(description + '.keras')

def neural_network_ERA(list, description):

    avg_list = []

    for batter in list:
        avg_batter = {}
        avg_batter['BB9'] = batter['BB9']
        avg_batter['SO9'] = batter['SO9']
        avg_batter['H9'] = batter['H9']
        avg_batter['HR9'] = batter['HR9']
        avg_batter['ERA'] = batter['ERA']
        avg_list.append(avg_batter)

    df = pd.DataFrame(avg_list)
    print(df)

    # Split the dataset into training and testing sets
    train_df, test_df = train_test_split(df, test_size=0.1, random_state=0)
    
    train_df.reset_index(drop=True, inplace=True)
    test_df.reset_index(drop=True, inplace=True)

    # Separate features and target variable
    X_train = train_df.drop(columns=['ERA'])
    y_train = train_df['ERA']
    X_test = test_df.drop(columns=['ERA'])
    y_test = test_df['ERA']

    print(X_train)
    print(y_train)
    
    # Create a normalization layer
    normalization_layer = tf.keras.layers.Normalization()

    # Adapt the normalization layer to your training data
    normalization_layer.adapt(np.array(X_train))

    # Define the neural network model
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(X_train.shape[1],)),
        normalization_layer,
        tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(32, activation='relu'),

        tf.keras.layers.Dense(1)
    ])

    # Compile the model
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Train the model
    history = model.fit(X_train, y_train, epochs=500, batch_size=64, validation_split=0.2, verbose=1)

    # Evaluate the model
    test_loss = model.evaluate(X_test, y_test)
    print(f"Test Loss: {test_loss}")

    # Make predictions
    predictions = model.predict(X_test) 

    test_df_reset = test_df.reset_index(drop=True)
    # Merge the original data with the denormalized predictions
    merged_data = pd.concat([test_df_reset, pd.DataFrame(predictions, columns=['pERA'])], axis=1)

    print(merged_data)
    merged_data.to_csv(description + 'Actual Prediction', index=False)

    model.save(description + 'seq.keras')

def neural_network_ERA_CNN(list, description):

    avg_list = []

    for batter in list:
        avg_batter = {}
        avg_batter['BB9'] = batter['BB9']
        avg_batter['SO9'] = batter['SO9']
        avg_batter['H9'] = batter['H9']
        avg_batter['HR9'] = batter['HR9']
        avg_batter['ERA'] = batter['ERA']
        avg_list.append(avg_batter)

    df = pd.DataFrame(avg_list)
    print(df)

    # Split the dataset into training and testing sets
    train_df, test_df = train_test_split(df, test_size=0.1, random_state=0)
    
    train_df.reset_index(drop=True, inplace=True)
    test_df.reset_index(drop=True, inplace=True)

    # Separate features and target variable
    X_train = train_df.drop(columns=['ERA'])
    y_train = train_df['ERA']
    X_test = test_df.drop(columns=['ERA'])
    y_test = test_df['ERA']

    print(X_train)
    print(y_train)
    
    # Create a normalization layer
    normalization_layer = tf.keras.layers.Normalization()

    # Adapt the normalization layer to your training data
    normalization_layer.adapt(np.array(X_train))

    # Define the neural network model
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(X_train.shape[1],)),
        normalization_layer,
        tf.keras.layers.Reshape((X_train.shape[1], 1)),  # Reshape for compatibility with CNN
        tf.keras.layers.Conv1D(64, 3, activation='relu'),  # Convolutional layer
        tf.keras.layers.MaxPooling1D(2),  # Max pooling layer
        tf.keras.layers.Flatten(),  # Flatten layer
        tf.keras.layers.Dense(32, activation='relu'),  # Fully connected layer
        tf.keras.layers.Dense(1)
    ])

    # Compile the model
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Train the model
    history = model.fit(X_train, y_train, epochs=250, batch_size=32, validation_split=0.2, verbose=1)

    # Evaluate the model
    test_loss = model.evaluate(X_test, y_test)
    print(f"Test Loss: {test_loss}")

    # Make predictions
    predictions = model.predict(X_test) 

    test_df_reset = test_df.reset_index(drop=True)
    # Merge the original data with the denormalized predictions
    merged_data = pd.concat([test_df_reset, pd.DataFrame(predictions, columns=['pERA'])], axis=1)

    print(merged_data)
    merged_data.to_csv(description + 'cnn Prediction', index=False)

    model.save(description + 'cnn.keras')

def neural_network_ERA_Wide(list, description):

    avg_list = []

    for batter in list:
        avg_batter = {}
        avg_batter['BB9'] = batter['BB9']
        avg_batter['SO9'] = batter['SO9']
        avg_batter['H9'] = batter['H9']
        avg_batter['HR9'] = batter['HR9']
        avg_batter['ERA'] = batter['ERA']
        avg_list.append(avg_batter)

    df = pd.DataFrame(avg_list)
    print(df)

    # Split the dataset into training and testing sets
    train_df, test_df = train_test_split(df, test_size=0.1, random_state=0)
    
    train_df.reset_index(drop=True, inplace=True)
    test_df.reset_index(drop=True, inplace=True)

    # Separate features and target variable
    X_train = train_df.drop(columns=['ERA'])
    y_train = train_df['ERA']
    X_test = test_df.drop(columns=['ERA'])
    y_test = test_df['ERA']

    print(X_train)
    print(y_train)
    
  # Create a normalization layer
    normalization_layer = tf.keras.layers.Normalization()

    # Adapt the normalization layer to your training data
    normalization_layer.adapt(np.array(X_train))

    # Define the wide pathway
    wide_input = tf.keras.layers.Input(shape=(X_train.shape[1],))
    wide_normalized = normalization_layer(wide_input)
    wide_output = tf.keras.layers.Dense(1, activation='linear')(wide_normalized)

    # Define the deep pathway
    deep_input = tf.keras.layers.Input(shape=(X_train.shape[1],))
    deep_normalized = normalization_layer(deep_input)
    deep_output = tf.keras.layers.Dense(64, activation='relu')(deep_normalized)
    deep_output = tf.keras.layers.Dense(32, activation='relu')(deep_output)
    deep_output = tf.keras.layers.Dense(1, activation='relu')(deep_output)

    # Concatenate wide and deep pathways
    combined_branches = tf.keras.layers.Concatenate()([wide_output, deep_output])

    # Final output layer
    output_layer = tf.keras.layers.Dense(1)(combined_branches)

    # Create and compile the model
    model = tf.keras.Model(inputs=[wide_input, deep_input], outputs=output_layer)

    # Compile the model
    model.compile(optimizer='adam', loss='mean_squared_error')

    # Train the model
    history = model.fit([X_train, X_train], y_train, epochs=1000, batch_size=32, validation_split=0.2, verbose=1)


    # Evaluate the model
    test_loss = model.evaluate([X_test, X_test], y_test)
    print(f"Test Loss: {test_loss}")

    # Make predictions
    predictions = model.predict([X_test, X_test]) 

    test_df_reset = test_df.reset_index(drop=True)
    # Merge the original data with the denormalized predictions
    merged_data = pd.concat([test_df_reset, pd.DataFrame(predictions, columns=['pERA'])], axis=1)

    print(merged_data)
    merged_data.to_csv(description + 'wide Prediction', index=False)

    model.save(description + 'wide.keras')

#linear_regression(stats_list,'Gap','XBH%','Gap Power to XBH% updated')

def scikit_regression():

    batter_list = make_batter_list(ratings_csv_location, True)
    not_2023_batter_list = make_batter_list(ratings_csv_location, False)
    stats_list = make_stats_list(stats_csv_location)
    stats_list = merge_lists(stats_list, batter_list)
    stats_list = cull_missing(stats_list)
    print(len(stats_list))
    avgX = []
    avgy = []
    train_list = stats_list[:300]
    print(len(train_list))
    test_list = stats_list[300:]
    for batter in train_list:
        avgX.append([batter['Babip'], batter['Power'], batter['AvKs']])
        avgy.append(batter['AVG']) 
    avgmodel = LinearRegression()
    avgmodel.fit(avgX,avgy)
    avgmodel.f
    test_list = []

    for batter in not_2023_batter_list:
        batterX = [[batter['Babip'],batter['Power'],batter['AvKs']]]
        batterY = avgmodel.predict(batterX)
        test_list.append([batter['FirstName'],batter['LastName'],batterX, batterY[0]])
"""      
"""
neural_network_AVG(culled_mixed_list,'BAbip','Babip','BABIP updated')
neural_network_AVG(culled_mixed_list,'HR%','Power','Power to HR% updated')
neural_network_AVG(culled_mixed_list,'BB%','Eye','Walks to Eye updated')
neural_network_AVG(culled_mixed_list,'SO%','AvKs','SO% to AVKs updated')

neural_network_AVG(culled_fielding_list, 'Rtotyr', 'Defense', 'RTOTYR')
neural_network_AVG(culled_fielding_list, 'Rdrsyr', 'Defense', 'RDRSYR')

neural_network_ERA(culled_pitching_list, 'ERA from per9')

neural_network_AVG(culled_pitching_list, 'HR9', 'pHR', 'HR9outof200')
neural_network_AVG(culled_pitching_list, 'H9', 'pBABIP', 'H9outof200')
neural_network_AVG(culled_pitching_list, 'BB9', 'Control', 'BB9outof200')
neural_network_AVG(culled_pitching_list, 'SO9', 'Stuff', 'SO9')
"""