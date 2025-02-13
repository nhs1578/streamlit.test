import streamlit as st
import panas as pd
import matplotlib.pyplot as plt

st.title("st.write() 활용 예시")

# 1. 텍스트 출력 (Markdown 지원)
st.write("## 마크다운 제목")
st.write("* 강조된 텍스트 *")

# 2. 데이터프레임 출력
df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
st.write("### 데이터프레임")
st.write(df)

# 3. 그래프 출력 (Matplotlib)
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 2])
st.write("### Matplotlib 그래프")
st.pyplot(fig)

# 4. 이미지 출력
st.write("### 이미지")
st.image("https://streamlit.io/images/brand/streamlit-logo-horizontal.svg", width=300)




st.write("# test")
st.header("header test")
st.header("header test")

st.image("https://i.namu.wiki/i/sYSJY7DwDYvqCrRvxzAgqpbm7EQzxE6jKPBhRBJGLwRzWvA-uj3YEQjgAVfR1snu3tian_0NYAtv2b06664WkA.webp")

st.markdown("---")



st.title("인터랙티브 위젯 예시")

# 1. 버튼
if st.button("버튼 클릭"):
    st.write("버튼이 클릭되었습니다!")

# 2. 슬라이더
age = st.slider("나이를 선택하세요", 0, 100, 25) # (라벨, 최소값, 최대값, 초기값)
st.write("선택된 나이:", age)
 
# 3. 텍스트 입력
name = st.text_input("이름을 입력하세요", "홍길동") # (라벨, 초기값)
st.write("입력된 이름:", name)

st.markdown("---")




st.title("레이아웃 예시")

# 1. 컬럼 나누기
col1, col2 = st.columns(2)

with col1:
    st.header("첫 번째 컬럼")
    st.image("https://i.namu.wiki/i/_OfUPgi0ovLvUXReAxm_xiZ7vFBs2Y2WWMHKv3ASiPnFl0i6yqpYd9DSnOWdSYhDVpcbc4teVzSrn7fAnC2gtQ.webp", width=350)

with col2:
    st.header("두 번째 컬럼")
    st.image("https://i.namu.wiki/i/sYSJY7DwDYvqCrRvxzAgqpbm7EQzxE6jKPBhRBJGLwRzWvA-uj3YEQjgAVfR1snu3tian_0NYAtv2b06664WkA.webp", width=150)

# 2. 사이드바
with st.sidebar:
    st.header("사이드바 메뉴")
    menu = st.radio("메뉴 선택", ["메뉴 1", "메뉴 2", "메뉴 3"])
    st.write("선택된 메뉴:", menu)

st.markdown("---")


st.write("# # 1개")
st.write("## # 2개")
st.write("### # 3개")
st.write("#### # 4개")
st.write("##### # 5개")
st.write("###### # 6개")
st.write("####### # 7개")

st.markdown("---")

st.write("""
         
         #streamlit 정리
         
         스트림릿에 대해 공부하고 있습니다
         
         write 테스트 중이고, 마크다운
         
         #의 갯수에 따라 수준이 달라진다고 하내요
         
         #울 쓰고 띄어쓰기를 해줘야 헤드가 됨
         
         \ # \ 역슬래시를 붙어됴
         
         \# 헤드 1
         ## 헤드 2 # 헤드 ### 헤드
         ### 헤드 3
         
         
          **아아아**  ㅇㄴㄹㄴㅇㄹㄹㅇ **ㄴㅇㄴㅇㄹㄹㄴ**
         # 안녕하세요
         
         """)
st.markdown("---")

st.title("코드 블록 예제")

code = '''
import streamlit as st

st.write("Hello, Markdown!")
'''
st.code(code, language='python') 

