import matplotlib.pyplot as plt

def feature_importance_plot (model, features, VTEC_point):

  importance = model.feature_importances_

  plt.barh([x for x in range(len(importance))], importance, color='#8f63f4', align='center')
  plt.title(VTEC_point)
  plt.yticks(range(len(features)), features)
  plt.xticks((np.arange(0.0, 1.1, 0.2)))
  plt.xlabel('Relative Importance')

  plt.rcParams ['figure.figsize'] = [3.6, 5]
  plt.rcParams.update({'font.size': 12})
  plt.show()
  

## features_70 = X_70_test_df.columns[:]
## features_40 = X_40_test_df.columns[:]
## features_10 = X_10_test_df.columns[:]

## feature_importance_plot (qgb_UB_10E70N, features_70, '10E 70N, UB')
