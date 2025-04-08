from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# Đọc dữ liệu từ file
data = pd.read_csv('Gold_2003_2024_Standardization.csv')  # Thay 'your_data.csv' bằng đường dẫn tới file dữ liệu của bạn
scaled_data = data.copy()

# Chuyển đổi cột 'Date' thành định dạng datetime và đặt làm chỉ số
scaled_data['Date'] = pd.to_datetime(scaled_data['Date'])
scaled_data.set_index('Date', inplace=True)

# Hàm tạo biểu đồ và trả về base64 string
def create_plot(plot_func):
    img = io.BytesIO()
    plot_func()
    plt.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    plot_base64 = base64.b64encode(img.getvalue()).decode('utf8')
    plt.close()
    return plot_base64

# Các hàm tạo biểu đồ
def plot_price_open_high_low():
    plt.figure(figsize=(14, 7))
    plt.plot(scaled_data.index, scaled_data['Price'], label='Price', marker='o')
    plt.plot(scaled_data.index, scaled_data['Open'], label='Open', marker='o')
    plt.plot(scaled_data.index, scaled_data['High'], label='High', marker='o')
    plt.plot(scaled_data.index, scaled_data['Low'], label='Low', marker='o')
    plt.title('Price, Open, High, Low Over Time')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)

def plot_volume():
    plt.figure(figsize=(14, 7))
    plt.bar(scaled_data.index, scaled_data['Vol'], color='skyblue')
    plt.title('Volume Over Time')
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.grid(True)

def plot_change_percent_line():
    plt.figure(figsize=(14, 7))
    plt.plot(scaled_data.index, scaled_data['Change%'], label='Change%', color='green', marker='o')
    plt.title('Change% Over Time')
    plt.xlabel('Date')
    plt.ylabel('Change%')
    plt.legend()
    plt.grid(True)

def plot_change_percent_bar():
    plt.figure(figsize=(14, 7))
    plt.bar(scaled_data.index, scaled_data['Change%'], color='orange', label='Change%')
    plt.xlabel('Date')
    plt.ylabel('Change%')
    plt.title('Price Change Percentage Over Time')
    plt.legend()
    plt.grid(True)

def plot_price_volume_combined():
    fig, ax1 = plt.subplots(figsize=(14, 7))
    ax1.bar(scaled_data.index, scaled_data['Vol'], color='skyblue', label='Volume')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Volume', color='skyblue')
    ax1.tick_params(axis='y', labelcolor='skyblue')
    ax2 = ax1.twinx()
    ax2.plot(scaled_data.index, scaled_data['Price'], color='green', label='Price', marker='o')
    ax2.set_ylabel('Price', color='green')
    ax2.tick_params(axis='y', labelcolor='green')
    plt.title('Price and Trading Volume Over Time')
    fig.tight_layout()
    plt.grid(True)

@app.route('/')
def index():
    # Tạo các biểu đồ và chuyển thành base64
    plot1 = create_plot(plot_price_open_high_low)
    plot2 = create_plot(plot_volume)
    plot3 = create_plot(plot_change_percent_line)
    plot4 = create_plot(plot_change_percent_bar)
    plot5 = create_plot(plot_price_volume_combined)

    return render_template('index.html', 
                          plot1=plot1, 
                          plot2=plot2, 
                          plot3=plot3, 
                          plot4=plot4, 
                          plot5=plot5)

if __name__ == '__main__':
    app.run(debug=True)