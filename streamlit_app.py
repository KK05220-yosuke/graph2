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
x_values_real = np.linspace(x_min, x_max, 100)  # 実数のxの値を生成
x_values_complex = np.linspace(complex(x_min), complex(x_max), 100)  # 複素数のxの値を生成

# y = x^n の計算
y_values_real = x_values_real ** n
y_values_complex = x_values_complex ** n

# 3Dプロットの作成
fig = go.Figure()

# 実数のxに対するプロット
fig.add_trace(go.Scatter3d(
    x=x_values_real,
    y=y_values_real,
    z=x_values_real,
    mode='lines',
    line=dict(color='blue', width=3),
    name=f'y = x^{n} (Real)'
))

# 複素数のxに対するプロット
fig.add_trace(go.Scatter3d(
    x=x_values_complex.real,
    y=y_values_complex.real,
    z=x_values_complex.imag,
    mode='lines',
    line=dict(color='red', width=3),
    name=f'y = x^{n} (Complex)'
))

# プロットの設定
fig.update_layout(
    scene=dict(
        xaxis=dict(title='X'),
        yaxis=dict(title='Y'),
        zaxis=dict(title='Imaginary Part of X'),
    ),
    title=f'3D Plot of y = x^{n}'
)

# プロットの表示
st.plotly_chart(fig)
