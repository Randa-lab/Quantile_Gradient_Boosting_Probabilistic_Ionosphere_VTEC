import numpy as np
import scipy.stats
from sklearn import metrics

#Calculation of statistics: RMS, Corr. and Confidence Intervals (CI)

def compute_statistics (y_test, y_pred_median, y_pred_upper, y_pred_lower):
  print('RMS (median):', round(np.sqrt(metrics.mean_squared_error(y_test, y_pred_median)),2))
  print('Corr. (median):',  scipy.stats.pearsonr(y_test, y_pred_median)[0])
  print('CI (upper):', round((y_pred_upper-y_pred_median).mean(axis=0), 2))
  print('CI (lower):', round((y_pred_median-y_pred_lower).mean(axis=0), 2))
  print('CI (average):', round((((y_pred_upper-y_pred_median)+(y_pred_median-y_pred_lower)).mean(axis=0))/2, 2))
