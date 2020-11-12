#IMPORTING LIBRARIES

import streamlit as st
import pickle
import pandas as pd
import numpy as np
import os
from PIL import Image,ImageFilter,ImageEnhance
import base64
#-----------------------------------------------------------

# @st.cache(allow_output_mutation=True)
# def get_base64_of_bin_file(bin_file):
#     with open(bin_file, 'rb') as f:
#         data = f.read()
#     return base64.b64encode(data).decode()

# def set_png_as_page_bg(png_file):
#     bin_str = get_base64_of_bin_file(png_file)
#     page_bg_img = '''
#     <style>
#     body {
#     background-image: url("data:im/jpg;base64,%s");
#     background-size: cover;
#     }
#     </style>
#     ''' % bin_str
    
#     st.markdown(page_bg_img, unsafe_allow_html=True)
#     return

# set_png_as_page_bg('im.jpg')

#-------------------------------------------------------->

html="""

	<h1 style=text-align:center;font-size:50px;color:black;>Predicting Chronic Kidney Disease Model</h1>
	 
	<center><h1 style=color:black;>Enter the following details :</h1>
	</center>

	"""

# page_bg_img = """
# <style>
# body {
# background-image: url("image.jpg");
# background-size: cover;
# }
# </style>
# """

# st.markdown(page_bg_img, unsafe_allow_html=True)

html2="""  <hr> </hr>"""

st.markdown(html, unsafe_allow_html=True)

model=pickle.load(open('values.pkl','rb'))


def predictfunc(a,b,c,d,e,f,g,h,i,j,k,l,m,n):
	input=np.array([[a,b,c,d,e,f,g,h,i,j,k,l,m,n]]).reshape(1,-1).astype(np.float64)
	final=model.predict(input)
	return final
@st.cache
def load_image(img):
	im =Image.open(os.path.join(img))
	return im
#---------------------------------------
def main():

	
	df = pd.DataFrame({
  'column1': [0,1],'column2':['abnormal','normal']
})


	# sg=st.slider('specific gravity ', 1.0, 1.01)


	sg= st.text_input("Enter specific gravity choose from values(1.02,1.01,1.015,1.025,1.005)","")

	alb=st.slider('albumin ', 0.0, 4.0)
	st.markdown(html2, unsafe_allow_html=True)

	pc= st.selectbox('pus_cell normal or abnormal ?=> Note: select 1:abnormal and 0:normal',df['column1'])
	pcc= st.selectbox('pus_cell_clumps present or not ? ',df['column1'])
	ba= st.selectbox('bacteria yes or no?',df['column1'])

	st.markdown(html2, unsafe_allow_html=True)

	bgr=st.slider(' blood_glucose_random ', 20.0, 300.0)
	pot=st.slider(' potassium', 1.0, 7.0)
	hm=st.slider('haemoglobin ', 2.0, 20.0)
	pcv=st.slider('packed_cell_volume  ', 50.0, 60.0)
	wc=st.slider(' white_blood_cell_count  ', 1000.0, 12000.0)
	rc=st.slider('red_blood_cell_count ', 2.0, 9.0)

	st.markdown(html2, unsafe_allow_html=True)

	htn= st.selectbox('Hypertension?',df['column1'])
	dm= st.selectbox('diabetes_mellitus',df['column1'])
	cad= st.selectbox('"coronary_artery_disease?',df['column1'])

	





	if st.button('predict'):
		output=predictfunc(sg,alb,pc,pcc,ba,bgr,pot,hm,pcv,wc,rc,htn,dm,cad)
		st.success('Your prediction is {}'.format(output[0]))

		if output==1:
			st.write("Alert You are at high risk for Chronic Kidney Disease")
		if output==0:
			st.write("no worries!You are safe Take care!!!")

		










if __name__=='__main__':
	main()