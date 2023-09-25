# Q10. You are comparing the performance of two regularized linear models using different types of
# regularization. Model A uses Ridge regularization with a regularization parameter of 0.1, while Model B
# uses Lasso regularization with a regularization parameter of 0.5. Which model would you choose as the
# better performer, and why? Are there any trade-offs or limitations to your choice of regularization
# method?


# If the value model simplicity, interpretability, and feature selection (removing less relevant predictors), Model B (Lasso) may be favored. Lasso can drive some coefficients to zero, effectively simplifying the model.

# If you prefer to retain all predictors and want to control the magnitude of coefficients without necessarily eliminating them, Model A (Ridge) may be preferred. Ridge tends to shrink coefficients towards zero but does not force them to be exactly zero.

# The choice of λ also plays a crucial role. A smaller λ in Model A (Ridge) or a larger λ in Model B (Lasso) would result in stronger regularization, potentially making the choice more clear-cut.

# Trade-Offs and Limitations:

# Ridge regularization may not perform well when feature selection is essential, as it tends to keep all predictors in the model, albeit with smaller coefficients.

# Lasso regularization can be sensitive to the choice of λ. A too-large λ might eliminate important predictors, while a too-small λ might not provide enough regularization.

# If there is multicollinearity (high correlation) among predictors, Ridge regularization is generally preferred because it tends to distribute the coefficient values among correlated variables, whereas Lasso may choose one of them and set the others to zero.