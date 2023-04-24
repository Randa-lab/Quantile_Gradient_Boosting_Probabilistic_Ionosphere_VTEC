def feature_importance_plot (model, features, VTEC_point):
  
  importance = model.feature_importances_
  
  plt.barh([x for x in range(len(importance))], importance, color='#8f63f4', align='center')
  
  plt.title(VTEC_point)
  plt.yticks(range(len(features)), features)
  plt.xticks((np.arange(0.0, 1.1, 0.2)))
  
  plt.rcParams ['figure.figsize'] = [3.6, 5]
  plt.rcParams.update({'font.size': 12})
  
  plt.xlabel('Relative Importance')
  plt.show()
