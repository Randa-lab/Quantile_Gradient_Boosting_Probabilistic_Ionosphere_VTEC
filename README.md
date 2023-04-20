# Quantile_Gradient_Boosting_for_Probabilistic_VTEC
The Jupyter notebook demonstrates how to load and evaluate  the probabilistic Quantile Gradient Boosting (QGB) Vertical Total Electron Content (VTEC) models, which provide 95% confidence intervals. QGB VTEC models forecast VTEC 1-day ahead for grid points at 10° of longitude, and 10°, 40°, and 70° of latitude. They were developed within the study "Uncertainty Quantification for Machine Learning-based Ionosphere and Space Weather Forecasting" by Natras R., Soja B. and Schmidt M., submitted to the Space Weather Jornal, AGU. 

Quantiles were estimated by multiplying the quantile values β by the positive and negative residuals in the loss function to obtain the quantile loss (QL) (see Equation 7 in the paper). 
Quantile values of  β ={0.025, 0.975} are chosen for estimating the lower and upper confidence bounds, respectively, to obtain a confidence interval of 95%. The mean quantile  β={0.50} provides the median VTEC. 

It has been shown that the quantile loss can model the data uncertainty. The Gradient Boosted tree is fast, performs well on structured input data, even on relatively small datasets, and has proven to be a powerful method in many data science competitions. For more information on Gradient Boosting for VTEC, see Natras, R.; Soja, B.; Schmidt, M. Ensemble Machine Learning of Random Forest, AdaBoost and XGBoost for Vertical Total Electron Content Forecasting. Remote Sens. 2022, 14, 3547. https://doi.org/10.3390/rs14153547.

The notebook was created and the QGB VTEC models developed by Randa Natras: randa.natras@hotmail.com; randa.natras@tum.de
