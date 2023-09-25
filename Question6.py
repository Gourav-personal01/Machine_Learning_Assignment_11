# Q6. Explain the concept of Lasso regularization. How does it differ from Ridge regularization, and when is
# it more appropriate to use?

# Lasso regularization, also known as L1 regularization, is a technique used in linear regression and other regression models 
# to prevent overfitting by adding a penalty term to the loss function. Lasso achieves this by adding the absolute values of the coefficients
# (parameter values) as a penalty term. 
# The goal of Lasso regularization is to encourage sparsity in the model by driving some of the coefficient values to exactly zero.

# Differences Between Lasso and Ridge Regularization:

# Lasso uses L1 regularization, which adds the absolute values of the coefficients as a penalty term.
# Ridge regularization uses L2 regularization, which adds the squared values of the coefficients as a penalty term.

# Lasso can shrink some coefficients to exactly zero, effectively removing the corresponding predictors from the model.
# Ridge can shrink coefficients close to zero but rarely drives them exactly to zero. It reduces the magnitude of all coefficients.

# Lasso is more suitable for feature selection because it can eliminate irrelevant predictors.
# Ridge can shrink coefficients but does not perform explicit feature selection.

