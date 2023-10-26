import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Streamlitアプリケーションのタイトルを設定
st.title('3Dグラフ表示アプリ')

# x, y, zの値を入力するスライダーを作成
x_values = st.slider('X軸の範囲', -10.0, 10.0, 1.0)
y_values = st.slider('Y軸の範囲', -10.0, 10.0, 1.0)
z_values = st.slider('Z軸の範囲', -10.0, 10.0, 1.0)

# グラフを描画する関数
def plot_3d_graph(x_range, y_range, z_range):
    x = np.linspace(-x_range, x_range, 100)
    y = np.linspace(-y_range, y_range, 100)
    X, Y = np.meshgrid(x, y)
    Z = X**2 + Y**2 + z_range
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_xlabel('X軸')
    ax.set_ylabel('Y軸')
    ax.set_zlabel('Z軸')
    ax.set_title('3D グラフ')

    # グラフを表示
    st.pyplot(fig)

# グラフを描画する関数を呼び出し
plot_3d_graph(x_values, y_values, z_values)
