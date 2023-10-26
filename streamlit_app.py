import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Streamlitのページ設定
st.set_page_config(page_title="3D Function Visualizer")

# ヘッダー
st.title("3D Function Visualizer")
st.caption("Created by ChatGPT")

# ユーザーからの入力を受け取る
n = st.slider("Choose the exponent (n)", min_value=1, max_value=10, value=2)
x_min = st.number_input("Enter the minimum value of x", value=-10)
x_max = st.number_input("Enter the maximum value of x", value=10)
x_values = np.linspace(x_min, x_max, 100)  # xの値を生成

# y = x^n の計算
y_values = x_values ** n

# 3Dプロットの作成
fig = go.Figure()

fig.add_trace(go.Scatter3d(
    x=x_values,
    y=y_values,
    z=x_values,
    mode='lines',
    line=dict(color='blue', width=3),
    name=f'y = x^{n}'
))

# プロットの設定
fig.update_layout(
    scene=dict(
        xaxis=dict(title='X'),
        yaxis=dict(title='Y'),
        zaxis=dict(title='Z'),
    ),
    title=f'3D Plot of y = x^{n}'
)

# プロットの表示
st.plotly_chart(fig)
