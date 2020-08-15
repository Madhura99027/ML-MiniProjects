
import streamlit as st
import pickle
import numpy as np
import pandas as pd
import os
from PIL import Image,ImageFilter,ImageEnhance

#-------------------------------------------------------->

html="""

	<h1 style=text-align:center;font-size:50px;>House Price Prediction Model</h1>
	<hr></hr>

	

	"""

html2="""
<h3>DRIVEWAY?</h3>
		<br>

"""

#---------------------------------------------------------->

st.markdown(html, unsafe_allow_html=True)

# algo= st.radio('',('LogisticRegression','knn','DecisionTree'))
# st.write("you selected",algo)

#------------------------------------------------------------->

#loading the pickle files

model=pickle.load(open('OLS.pkl','rb'))


 
	
#------------------------------------------------------

def main():
	
# 'driveway', 'fullbase' , 'gashw' , 'airco', 'prefarea'
#  'garagepl',  'bathrms',
# lotsize'
# 'stories_four', 'stories_one', 'stories_three'

#------------------------------------

	df = pd.DataFrame({
  	'column1': ['Yes','No'],
  
	})

	menu=["House Prediction","Predicted House","About","Visual"]
	choices=st.sidebar.selectbox("",menu)

	if choices=="House Prediction":
		st.subheader("Enter the following fields")
		c=tuple([i for i in range(0,2)])
		st.subheader(" Want DRIVEWAY? ( 1= yes ,0=No) ")
		driveway= st.selectbox('',c)
		st.subheader("Want Airco?(yes=1 , No=0) ")
		airco= st.selectbox ('-', c )
		st.subheader("Want preffered area?(yes=1 , No=0)")
		prefarea= st.selectbox('--', c)
		st.subheader("Want gashw?(yes=1 , No=0)")
		gashw= st.selectbox('_', c)
		st.subheader("Want fullbase?(yes=1 , No=0) ")
		fullbase= st.selectbox('__' ,c)

		#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

		garagepl=st.number_input("Enter number of garagepl",min_value=1,max_value=3,step=1,format='%d')
		bathrms=st.number_input("Enter number of BathRooms",min_value=1,max_value=4,step=1,format='%d')

		#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


		stories_one=0
		stories_two=0
		stories_three=0
		stories_four=0

		stories=st.number_input("Enter number of Stories",min_value=1,max_value=4,step=1,format='%d')
 
		if stories==1:
			
			stories_one+=1
			 

		if stories==2:
			 
			stories_two+=1
			 
		if stories==3:
			 
			stories_three+=1
			 
		if stories==4:
			 
			stories_four+=1

		st.write(stories_one,stories_two,stories_three ,stories_four)

		#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
			 
		

		lotsize= st.slider('LOTSIZE',1000,17000)
		st.write(lotsize)

		#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
		st.subheader("Click below button for prediction") 

		if st.button('predict'):
			# output=predictfunc()

		 
		
			# st.success('Your predicted Price is   {}'.format(output[0]))
			

			st.write("yes!!!!!")







if __name__=='__main__':
	main()