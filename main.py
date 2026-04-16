from src.data_preprocessing import load_data
from src.feature_engineering import create_features
from src.model import train_model, predict
from src.inventory import calculate_inventory
from src.visualization import plot_sales, plot_forecast, save_inventory_table

# Step 1: Load Data
df = load_data()

# Step 2: Feature Engineering
df = create_features(df)

# Step 3: Train Model
model = train_model(df)

# Step 4: Generate Forecast
forecast = predict(model, df)

# Step 5: Inventory Optimization
inventory = calculate_inventory(forecast)

# Step 6: Create Images
plot_sales(df)
plot_forecast(df, forecast)
save_inventory_table(inventory)  # ✅ THIS FIXES YOUR EMPTY PNG

# Step 7: Save Outputs
inventory.to_csv("outputs/inventory.csv", index=False)
forecast.to_csv("outputs/forecast.csv", index=False)

# Step 8: Print Output
print("\n✅ Inventory Optimization Output:")
print(inventory.head())