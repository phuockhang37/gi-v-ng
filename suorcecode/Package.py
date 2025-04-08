# save_models.py
import pandas as pd
from sklearn.ensemble import AdaBoostRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
import xgboost as xgb
import lightgbm as lgb
import joblib

# Load data and preprocess
DATA_PATH = 'Gold_2003_2024_AfterPreprocessing.csv'
data = pd.read_csv(DATA_PATH)
X = data.drop(columns=['Price', 'Date'])
y = data['Price']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train models
ada_model = AdaBoostRegressor(estimator=DecisionTreeRegressor(max_depth=4), n_estimators=100, random_state=42)
ada_model.fit(X_train, y_train)

xgb_model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, random_state=42)
xgb_model.fit(X_train, y_train)

lgb_model = lgb.LGBMRegressor(
    boosting_type='gbdt',
    max_depth=6,
    num_leaves=31,
    n_estimators=100,
    learning_rate=0.1,
    random_state=42
)
lgb_model.fit(X_train, y_train)

# Save the trained models to .pkl files
joblib.dump(ada_model, 'ada_model.pkl')
joblib.dump(xgb_model, 'xgb_model.pkl')
joblib.dump(lgb_model, 'lgb_model.pkl')

print("Models được lưu thành công!")
