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

# 実数または純虚数のxの値を生成
x_type = st.radio("Select x type", ["Real", "Imaginary"])
if x_type == "Real":
    x_min = st.number_input("Enter the minimum value of x (Real)", value=-10)
    x_max = st.number_input("Enter the maximum value of x (Real)", value=10)
    x_values = np.linspace(x_min, x_max, 100)
    y_values = np.linspace(0, 0, 100)  # 純虚数の場合はyはすべて0
else:
    y_min = st.number_input("Enter the minimum value of y (Imaginary)", value=-10)
    y_max = st.number_input("Enter the maximum value of y (Imaginary)", value=10)
    x_values = np.linspace(0, 0, 100)  # 実数の場合はxはすべて0
    y_values = np.linspace(y_min, y_max, 100)

# y = x^n の計算
z_values = (x_values + 1j * y_values) ** n

# 3Dプロットの作成
fig = go.Figure()

# 実数または純虚数のxに対するプロット
if x_type == "Real":
    fig.add_trace(go.Scatter3d(
        x=x_values,
        y=z_values.real,  # y_valuesとz_valuesを入れ替える
        z=y_values,  # y_valuesとz_valuesを入れ替える
        mode='lines',
        line=dict(color='blue', width=3),
        name=f'y = x^{n} (Real)'
    ))
else:
    fig.add_trace(go.Scatter3d(
        x=x_values,
        y=z_values.real,  # y_valuesとz_valuesを入れ替える
        z=y_values,  # y_valuesとz_valuesを入れ替える
        mode='lines',
        line=dict(color='red', width=3),
        name=f'y = x^{n} (Imaginary)'
    ))

# プロットの設定
fig.update_layout(
    scene=dict(
        xaxis=dict(title='X'),
        yaxis=dict(title='Z'),  # Y軸とZ軸のラベルを入れ替える
        zaxis=dict(title='Y'),  # Y軸とZ軸のラベルを入れ替える
    ),
    title=f'3D Plot of y = x^{n}'
)

# プロットの表示
st.plotly_chart(fig)