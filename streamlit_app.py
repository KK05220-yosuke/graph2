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

# 複素数のxの値を生成
x_values_real = np.linspace(x_min, x_max, 100)
y_values_real = np.linspace(y_min, y_max, 100)
x_mesh, y_mesh = np.meshgrid(x_values_real, y_values_real)
x_values_complex = x_mesh + 1j * y_mesh

# y = x^n の計算
y_values_complex = x_values_complex ** n

# 3Dプロットの作成
fig = go.Figure()

# 複素数のxに対するプロット
fig.add_trace(go.Surface(
    x=x_values_complex.real,
    y=x_values_complex.imag,
    z=y_values_complex.real,
    colorscale='Viridis',
    cmin=y_min**n,
    cmax=y_max**n
))

# プロットの設定
fig.update_layout(
    scene=dict(
        xaxis=dict(title='Real Part of X'),
        yaxis=dict(title='Imaginary Part of X'),
        zaxis=dict(title=f'Y = X^{n}'),
    ),
    title=f'3D Plot of y = x^{n}'
)

# プロットの表示
st.plotly_chart(fig)
