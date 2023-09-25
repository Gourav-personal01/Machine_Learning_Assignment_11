# # Q9. You are comparing the performance of two regression models using different evaluation metrics.
# # Model A has an RMSE of 10, while Model B has an MAE of 8. Which model would you choose as the better
# # performer, and why? Are there any limitations to your choice of metric?

# To determine which model is better, you should consider the specific objectives of your analysis and the importance of different aspects of model performance. There is no universal answer, as it depends on the problem context.

# If minimizing large errors and outliers is critical and the data is not heavily influenced by outliers, Model A (RMSE) may be favored.

# If you want a more robust and interpretable measure of overall accuracy that is less affected by outliers, Model B (MAE) may be the better choice.

# Limitations - 

# The choice of metric can be influenced by the nature of the data. If the dataset contains many outliers, RMSE may give too much weight to these outliers

# Both RMSE and MAE provide information about the accuracy of predictions but do not capture other aspects of model performance, such as the ability to capture patterns or interpretability.