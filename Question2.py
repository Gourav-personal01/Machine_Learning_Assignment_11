# Q2. Define adjusted R-squared and explain how it differs from the regular R-squared.

# Answer - 

# Adjusted R-squared, also known as the adjusted coefficient of determination, is a statistical measure used to assess the goodness of fit of a regression model that takes into account the number of predictor variables in the model. It is an extension of 
# the regular R-squared (coefficient of determination) and is particularly useful when comparing models with different numbers of predictors.

# Adjusted R-squared adjusts the regular R-squared by taking into account the number of predictor variables in the model and the sample size.

# It penalizes the inclusion of unnecessary predictors that do not contribute significantly to explaining the variance in the dependent variable.

# Mathematically, the formula for adjusted R-squared is:

# Adjusted R² = 1 - [(1 - R²) * (n - 1) / (n - k - 1)]

# Where:

# R² is the regular R-squared.
# n is the sample size (number of observations).
# k is the number of predictor variables in the model.