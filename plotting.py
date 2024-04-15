import matplotlib.pyplot as plt
import numpy as np
import lin_regression
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from pylab import *
from keras import optimizers
import pandas as pd

stuff_to_sopct_slope = 0.0021956584
stuff_to_sopct_intercept = 0.027717765
control_to_bbpct_slope = -0.0010105851
control_to_bbpct_intercept = 0.15812697
babip_to_babippct_slope = -0.0011705309
babip_to_babippct_intercept = 0.37854692
pHR_to_hrpct_slope = -0.0003623672
pHR_to_hrpct_intercept = 0.048940595
h9_hr9_bbpct_sum_to_era_slope = 0.4967373
h9_hr9_bbpct_sum_to_era_intercept = -2.384482
pHR_to_hrper9_slope = -0.016680183
pHR_to_hrper9_intercept = 2.3589768
mod_pHR_to_hrper9_slope = 0
mod_pHR_to_hrper9_intercept = 0
control_to_bbper9_slope = -0.042766504
control_to_bbper9_intercept = 5.9787097
mod_control_to_bbper9_slope = -0.07154865
mod_control_to_bbper9_intercept = 8.817354
stuff_to_soper9_slope = 0.084339656
stuff_to_soper9_intercept = 3.6953728
mod_stuff_to_soper9_slope = 0.103466846
mod_stuff_to_soper9_intercept = 0.74195576
gap_to_xbhpct_slope = 0.0021773693
gap_to_xbhpct_intercept = -0.07695567



ratings_csv_location = 'Data\CSV Files\pt_card_list.csv'

pitching_csv_location = 'Data\OOTP Working Historical - Sheet1.csv'

batter_list = lin_regression.make_batter_list(ratings_csv_location, True)
batter_stats_list = lin_regression.make_stats_list('Data\CSV Files\Statistics PCT - Sheet1.csv')

batter_merged_list = lin_regression.merge_lists(batter_stats_list, batter_list)

batter_safe_list = {}
for batter in batter_merged_list:
    try:
        this_batter = {}
        this_batter['Gap'] = batter['Gap']
        this_batter['XBH%'] = batter['XBH%']
        if this_batter['Gap'] != NaN:
            batter_safe_list.append(this_batter)
    except:
        pass

print(batter_safe_list)
xbh_values = [batter['XBH%'] for batter in batter_safe_list]
gap_values = [batter['Gap'] for batter in batter_safe_list]
xbh_np = np.array(xbh_values)
gap_np = np.array(gap_values)

bat_df = pd.DataFrame(batter_merged_list)
bat_df = bat_df.dropna(subset=['Gap'])

def linear_regression_analyze(input_value, output_value, input_text, output_text, color):
    plt.figure()
    plt.scatter(input_value, output_value, color=color, alpha=0.1)

    # Add labels and title
    plt.title(input_text + ' vs ' + output_text)
    plt.xlabel(input_text)
    plt.ylabel(output_text)

    # Show plot

    def lin_regress():
        lin_regress_model = Sequential()
        lin_regress_model.add(Dense(1, activation='linear', input_dim=1, kernel_initializer=tf.keras.initializers.Constant(value=0.1)))
        lin_regress_model.compile(optimizer=optimizers.Adam(learning_rate=0.00001), loss='mean_absolute_error', metrics = ['accuracy'])
        return lin_regress_model


    regr = lin_regress()
    regr.fit(input_value, output_value, epochs=1000,batch_size=22)

    predictions = regr.predict(input_value)
    # Get the weights and biases of the trained model
    weights, biases = regr.layers[0].get_weights()

    m = weights[0][0]  # Slope
    b = biases[0]      # Intercept

    print("Slope (m):", m)
    print("Intercept (b):", b)
    plt.plot(input_value, predictions, color='red')

def neural_network_analyze(input_value, output_value, input_text, description):

    avg_list = []

    for batter in list:
        avg_batter = {}
        avg_batter[target_variable] = batter[target_variable]
        avg_batter[source_variable] = batter[source_variable]
        avg_list.append(avg_batter)

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


linear_regression_analyze(bat_df['Gap'], bat_df['XBH%'], 'GAP','XBH', 'green')

"""

linear_regression_analyze(hist_h, hist_h_score, 'H/9','pBABIP','blue')
linear_regression_analyze(hist_so, hist_so_score, 'SO/9','Stuff','orange')
linear_regression_analyze(hist_bb, hist_bb_score, 'BB/9', 'Control', 'purple')
linear_regression_analyze((h9_array+bb9_array+hr9_array), era_array, 'H9+BB9+HR9','ERA','teal')
linear_regression_analyze(bb9_array, era_array, 'BB9','ERA', 'green')
linear_regression_analyze(so9_array, era_array, 'SO9','ERA','blue')
linear_regression_analyze(hr9_array, era_array, 'HR9','ERA','orange')
"""
plt.show()

#pitching_list = lin_regression.make_pitching_stats_list(pitching_csv_location)
#merged_pitching_list = lin_regression.merge_pitching_lists(pitching_list, pitcher_list)
#culled_pitching_list = lin_regression.cull_missing_pitcher(merged_pitching_list)

#era_datagrame = pd.read_csv('ERA per9 1980+ - Sheet1.csv')

#historical_dataframe = pd.read_csv(historical_list)
#culled_pitching_list = pd.read_csv('Data\Copy of OOTP Pitching Stats Historical - Sheet1.csv')

#pct_df = pd.DataFrame(culled_pitching_list)

#stuff_values = [pitcher['Stuff'] for pitcher in culled_pitching_list]
#sopct_values = [pitcher['sopct'] for pitcher in culled_pitching_list]
#stuff_mod_array = np.array(stuff_values)
#sopct_mod_array = np.array(sopct_values)


#control_values = [pitcher['Control'] for pitcher in culled_pitching_list]
#bbpct_values = [pitcher['bbpct'] for pitcher in culled_pitching_list]
#control_mod_array = np.array(control_values)
#bbpct_mod_array = np.array(bbpct_values)


#pbabip_values = [pitcher['pBABIP'] for pitcher in culled_pitching_list]
#bab_values = [pitcher['bab'] for pitcher in culled_pitching_list]



#phr_values = [pitcher['pHR'] for pitcher in culled_pitching_list]
#hrpct_values = [pitcher['hrpct'] for pitcher in culled_pitching_list]
#phr_mod_array = np.array(phr_values)
#hrpct_mod_array = np.array(hrpct_values)


#hist_hr = historical_dataframe['hr/9']
#hist_hr_score = historical_dataframe['pHR']
#hist_h = historical_dataframe['h/9']
#hist_h_score = historical_dataframe['pBABIP']
#hist_bb = historical_dataframe['bb/9']
#hist_bb_score = historical_dataframe['Control']
#hist_so = historical_dataframe['so/9']
#hist_so_score = historical_dataframe['Stuff']

#era_array = era_datagrame['ERA']
#h9_array = era_datagrame['H9']
#hr9_array = era_datagrame['HR9']
#so9_array = era_datagrame['SO9']
#bb9_array = era_datagrame['BB9']


#pitcher_list = lin_regression.make_pitcher_list(ratings_csv_location, True)
#pitching_stats_list = lin_regression.make_pitching_stats_list(pitching_csv_location)

#historical_list = 'Data\OOTP Working Historical - per9.csv'