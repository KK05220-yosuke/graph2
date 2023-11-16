import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Streamlitのページ設定
st.set_page_config(page_title="Quadratic 3D Function Visualizer")

# ヘッダー
st.title("Quadratic 3D Function Visualizer")
st.caption("Created by ChatGPT")

# ユーザーからの入力を受け取る
a = st.slider("Choose the coefficient 'a'", min_value=-10, max_value=10, value=1)
b = st.slider("Choose the coefficient 'b'", min_value=-10, max_value=10, value=0)
c = st.slider("Choose the coefficient 'c'", min_value=-10, max_value=10, value=0)

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

# y = ax^2 + bx + c の計算
z_values = a * x_values**2 + b * x_values + c + 1j * y_values

# 3Dプロットの作成
fig = go.Figure()

# 実数または純虚数のxに対するプロット
if x_type == "Real":
    fig.add_trace(go.Scatter3d(
        x=x_values,
        y=y_values,
        z=z_values.real,
        mode='lines',
        line=dict(color='blue', width=3),
        name=f'y = {a}x^2 + {b}x + {c} (Real)'
    ))
else:
    fig.add_trace(go.Scatter3d(
        x=x_values,
        y=y_values,
        z=z_values.real,
        mode='lines',
        line=dict(color='red', width=3),
        name=f'y = {a}x^2 + {b}x + {c} (Imaginary)'
    ))

# プロットの設定
fig.update_layout(
    scene=dict(
        xaxis=dict(title='X'),
        yaxis=dict(title='Y'),
        zaxis=dict(title='Z'),
    ),
    title=f'3D Plot of y = {a}x^2 + {b}x + {c}'
)

# プロットの表示
st.plotly_chart(fig)
