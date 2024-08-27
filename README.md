# Linear Regression Practice Project

## Problem Statement

This project aims to practice implementing and evaluating a simple linear regression model using Python. The dataset used for this exercise contains information on TV advertising budgets and the corresponding sales figures. The goal is to build a linear regression model to predict sales based on the TV advertising budget and evaluate the model's performance.

## Approach

1. **Dataset**:
   The dataset consists of two columns:
   - `TV`: The amount spent on TV advertising (independent variable).
   - `Sales`: The resulting sales figures (dependent variable).

   Sample data:
      TV     Sales
0    230.1   22.1
1     44.5   10.4
2     17.2    9.3
3    151.5   18.5
4    180.8   12.9

3. **Model Training**:
- The dataset was split into training and testing sets.
- A simple linear regression model was trained using the `TV` advertising budget to predict `Sales`.
- The model was saved using `joblib` for future use.

3. **Prediction Function**:
A function was created to use the trained model and predict sales based on a given `TV` advertising budget.

4. **Evaluation**:
- **Mean Squared Error (MSE)**: 10.20
- **R² Score**: 0.6767

**MSE**: The mean squared error indicates the average squared difference between actual and predicted sales. A value of 10.20 suggests a moderate level of prediction error.

**R² Score**: The R² score of 0.6767 indicates that approximately 67.67% of the variance in sales is explained by the TV advertising budget. This reflects a moderate to strong linear relationship between `TV` and `Sales`.

5. **Final Thoughts**:
The model demonstrates a reasonable performance for a simple linear regression with only one feature. The R² score suggests that TV advertising has a significant impact on sales, but other factors are also at play. The MSE reflects some level of prediction error, which is expected in real-world scenarios.
