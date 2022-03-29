
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

#タイトル
st.title('顔認識アプリ')

#文字を書く
st.write('DataFrame')
st.write(
    pd.DataFrame({
        '1st column' :[1, 2, 3, 4],
        '2st column': [5, 6, 7, 8]
    })
)


#マジックコマンド
"""
# My 1st APP
## マジックコマンド
こんな感じでマジックコマンドを使用。Markdown対応。
"""

if st.checkbox('Show DataFrame'):
    #チャートの表示
    chart_df = pd.DataFrame(
        np.random.randn(20, 3), #20行3列の正規乱数
        columns = ['a','b','c']
    )
    st.line_chart(chart_df)


#ファイルをアップロード
uploaded_file = st.file_uploader("Choose an image...", type='jpg')
#もしファイルが入っていたら画像を表示
if uploaded_file is not None :
    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded Image', use_column_width=True)




