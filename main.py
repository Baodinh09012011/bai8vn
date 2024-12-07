import streamlit as s

s.title("Gioi thieu ban be")
col1,col2 = s.columns(2)


with col1.expander("Ban A"):
  s.image("https://tinhdoanquangninh.vn/wp-content/uploads/2022/11/hoc-sinh-lop-1-nhat-duoc-12-trieu-dong-tim-tra-nguoi-danh-roi-536x400.jpg")
  s.write("Ten : Nguyen Van A")
  s.write("lop : 3")
  s.write("Tinh cach: thong minh")


with col2.expander("Ban B"):
  s.image("https://tse3.mm.bing.net/th?id=OIP.wZTC41ekGZYKLUhpNyDWIgHaGU&pid=Api&P=0&h=180")
  s.write("Ten : Nguyen Van B")
  s.write("lop : 4")
  s.write("Tinh cach: than thien")


s.video("banbe.mp4")

