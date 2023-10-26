import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Streamlitのページ設定
st.set_page_config(page_title="Complex 3D Function Visualizer")

# ヘッダー
st.title("Complex 3D Function Visualizer")
st.caption("Created by ChatGPT")

# ユーザーからの入力を受け取る
n = st.slider("Choose the exponent (n)", min_value=1, max_value=10, value=2)
x_min = st.number_input("Enter the minimum value of x", value=-10)
x_max = st.number_input("Enter the maximum value of x", value=10)
y_min = st.number_input("Enter the minimum value of y", value=-10)
y_max = st.number_input("Enter the maximum value of y", value=10)

# 実数のxおよびyの値を生成
x_values = np.linspace(x_min, x_max, 100)
y_values = np.linspace(y_min, y_max, 100)

# y = x^n の計算
z_values = (x_values + 1j * y_values) ** n

# 3Dプロットの作成
fig = go.Figure()

# 実数および虚数のxに対するプロット
fig.add_trace(go.Surface(
    x=x_values,
    y=y_values,
    z=z_values.real,
    colorscale='Viridis',
    cmin=z_values.real.min(),
    cmax=z_values.real.max()
))

# プロットの設定
fig.update_layout(
    scene=dict(
        xaxis=dict(title='X'),
        yaxis=dict(title='Y'),
        zaxis=dict(title='Real Part of y = x^{n}'),
    ),
    title=f'3D Plot of y = x^{n}'
)

# プロットの表示
st.plotly_chart(fig)
