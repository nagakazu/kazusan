import time
import numpy as np
import streamlit as st
from PIL import Image
st.title('長野県の郷土料理')
st.write('小倉です')

text = st.text_input('あなたの名前を教えてください。')
st.write('あなたの名前は'+text+'です')
condition = st.slider('あなたの今の調子は?',0, 100, 50)
option = st.selectbox(
'郷土料理について知りたい地域を選択してください',
list(['北信','東信','南信','中信'])
)
# st.sidebar.write('プログレスバーの表示')
# 'Start!'

# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#     latest_iteration.text(f'Iteration{i+1}')
#     bar.progress(i +1)
#     time.sleep(0.1)

'Done!!!'
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
 right_column.write('ここは右カラムです')

from PIL import Image
img = Image.open('S__83451917_0.jpg')
st.image(img,caption='紙',use_column_width=True)


import pandas as pd
df = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69,139.70],
    columns = ['lat','lon',]#lat lon 緯度と経度
)
st.map(df)

import numpy as np
df = pd.DataFrame(
    np.random.rand(20,3), #20行3列
    columns = ['a','b','c']
)
st.table(df.style.highlight_max(axis=0))

st.bar_chart(df)


