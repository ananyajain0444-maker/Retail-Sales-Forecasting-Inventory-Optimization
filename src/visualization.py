import matplotlib.pyplot as plt

def plot_sales(df):
    plt.figure()
    plt.plot(df['date'], df['sales'])
    plt.title("Sales Trend")
    plt.savefig("images/sales_trend.png")
    plt.close()

def plot_forecast(df, forecast):
    plt.figure()
    plt.plot(df['date'], df['sales'], label='Actual')
    plt.plot(df['date'], forecast['forecast'], label='Forecast')
    plt.legend()
    plt.title("Forecast vs Actual")
    plt.savefig("images/forecast_plot.png")
    plt.close()

def save_inventory_table(df):
    plt.figure(figsize=(10, 4))
    plt.axis('off')

    table = plt.table(
        cellText=df.head(10).values,
        colLabels=df.columns,
        loc='center'
    )

    table.auto_set_font_size(False)
    table.set_fontsize(8)

    plt.title("Inventory Optimization Table")
    plt.savefig("images/inventory_table.png")
    plt.close()