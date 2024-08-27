import joblib
model = joblib.load('notebook/linear_regression_model.pkl')

def predict_sales(tv_budget, model):
     tv_budget_array = [[tv_budget]]
     predicted_sales = model.predict(tv_budget_array)
    
     return predicted_sales[0] 

if __name__ == "__main__":
    tv_budget = 180.8 
    predicted_sales = predict_sales(tv_budget, model)
    print(f"Predicted Sales for TV budget of {tv_budget}: {predicted_sales}")
