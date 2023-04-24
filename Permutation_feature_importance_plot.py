from sklearn.inspection import permutation_importance

def permutation_feature_importance_plot (model, X_data, y_data, features, VTEC_point):
  
  result = permutation_importance(model, X_data, y_data, n_repeats=5, random_state=42, n_jobs=2)
  result_importances = pd.Series(result.importances_mean, index=features)
  
  fig, ax = plt.subplots()
  result_importances.plot.barh(yerr=result.importances_std, ax=ax, align='center')
  plt.xticks((np.arange(0.0, 1.1, 0.2)))
  ax.set_title(VTEC_point)
  ax.set_ylabel("Relative Permutation Feature Importance")

  plt.rcParams ['figure.figsize'] = [3.6, 5]
  plt.rcParams.update({'font.size': 12})
  plt.show()
