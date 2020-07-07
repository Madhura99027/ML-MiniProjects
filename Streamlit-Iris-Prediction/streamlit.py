
import streamlit as st
import pickle
import numpy as np
import os
from PIL import Image,ImageFilter,ImageEnhance
model=pickle.load(open('logistic.pkl','rb'))



@st.cache
def load_image(img):
	im =Image.open(os.path.join(img))
	return im

def predictfunc(x,y,z,w):
	input=np.array([[x,y,z,w]]).reshape(1,-1).astype(np.float64)
	final=model.predict(input)
	return final

 
def main():
	html="""

	<h1 style=text-align:center;font-size:50px;>Iris Species Prediction Using Logistic regression </h1>
	<hr></hr>

	"""
	st.markdown(html, unsafe_allow_html=True)


	#------------------------------------>

	#selectbox

	# d1=['LogisticRegression','KNN','Decisiontree']
	# html2="""
	# <h2>Which Model you wish to Apply?</h2>"""
	# st.markdown(html2,unsafe_allow_html=True)

	# option=st.selectbox("",d1)


	# option= st.radio('',('LogisticRegression','knn','Dtree'))

	# 'You selected:', option
	#--------------------------------------->

	# 
		


	 


	#------------------------------------------>

	#Input the required field

	sepal_length = st.text_input("sepal_length","")
	sepal_width = st.text_input("sepal_width ","")
	petal_length= st.text_input("petal_length","")
	petal_width= st.text_input("petal_width","")


	#--------------------------------------------->


	#predict button

	if st.button('predict'):
		output=predictfunc(sepal_length,sepal_width,petal_length,petal_width)

		 

		st.success('Your predicted species is   {}'.format(output[0]))




		if output=='virginica':
			st.text("Showing Virginica")
			st.image(load_image('iris_virginica.jpg'))
			
		if output=='versicolor':
			st.text("Showing Versicolor")
			st.image(load_image('iris_versicolor.jpg'))

		if output=='setosa':
			st.text("Showing Setosa")
			st.image(load_image('iris_setosa.jpg'))







if __name__=='__main__':
	main()	 