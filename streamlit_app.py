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