# Q7. How do regularized linear models help to prevent overfitting in machine learning? Provide an
# example to illustrate.


# Regularized linear models, such as Ridge and Lasso regression, help prevent overfitting in machine learning by introducing 
# penalty terms into the model's optimization objective. These penalty terms add a cost for the complexity of the model, effectively
# discouraging the model from fitting 
# the noise in the data and from having excessively large coefficient values. Here's how regularized linear models work to prevent overfitting.


# Suppose you are building a regression model to predict house prices based on various features such as square footage, number of bedrooms, number of bathrooms, 
# and neighborhood crime rate. Here's how regularized linear models help prevent overfitting in this scenario:

# Ridge Regularization: When using Ridge regression with an appropriate value of λ, it will encourage the model to have small but non-zero coefficients for all predictors. This helps prevent overfitting by reducing the impact of individual predictors. For example, it might reduce the effect of a noisy predictor like "neighborhood crime rate."

# Lasso Regularization: Lasso regression, on the other hand, can drive some coefficients to exactly zero. In our example, if "neighborhood crime rate" is not a strong predictor, Lasso may set its coefficient to zero, effectively removing it from the model. This is a form of feature selection and can lead to a simpler and more interpretable model.