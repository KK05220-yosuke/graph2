import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Streamlitのページ設定
st.set_page_config(page_title="Classic 3D Function Visualizer")

# ヘッダー
st.title("Classic 3D Function Visualizer")
st.caption("Created by ChatGPT")

# ユーザーからの入力を受け取る
n = st.slider("Choose the exponent (n)", min_value=1, max_value=10, value=2)
x_min = st.number_input("Enter the minimum value of x", value=-10)
x_max = st.number_input("Enter the maximum value of x", value=10)
y_min = st.number_input("Enter the minimum value of y", value=-10)
y_max = st.number_input("Enter the maximum value of y", value=10)
x_values = np.linspace(x_min, x_max, 100)
y_values = np.linspace(y_min, y_max, 100)

# 2Dグラフ（平面上の指数関数のプロット）
x_mesh, y_mesh = np.meshgrid(x_values, y_values)
z_mesh = (x_mesh + 1j * y_mesh) ** n
surface = go.Surface(x=x_mesh, y=y_mesh, z=np.real(z_mesh), colorscale='Viridis')

# 3Dプロットの作成
fig = go.Figure(surface)

# プロットの設定
fig.update_layout(
    scene=dict(
        xaxis=dict(title='X'),
        yaxis=dict(title='Y'),
        zaxis=dict(title='Z'),
    ),
    title=f'Classic 3D Plot of z = (x + iy)^n'
)

# プロットの表示
st.plotly_chart(fig)
