
import streamlit as st
import pickle
import numpy as np
import os
from PIL import Image,ImageFilter,ImageEnhance

#-------------------------------------------------------->

html="""

	<h1 style=text-align:center;font-size:50px;>Iris Species Prediction Model</h1>
	<hr></hr>

	<center><h2>Which Algorithm	 You wish to apply?</h2></center>

	"""

html2="""
		<br>

"""

#---------------------------------------------------------->

st.markdown(html, unsafe_allow_html=True)

algo= st.radio('',('LogisticRegression','knn','DecisionTree'))
st.write("you selected",algo)

#------------------------------------------------------------->

#loading the pickle files

if algo=='LogisticRegression':
	 
	model=pickle.load(open('logistic.pkl','rb'))


if algo=='knn':
	 
	model=pickle.load(open('knn.pkl','rb'))

if algo=='Dtree':
	 
	model=pickle.load(open('dtree.pkl','rb'))

#--------------------------------------------------------------->


@st.cache
def load_image(img):
	im =Image.open(os.path.join(img))
	return im

def predictfunc(x,y,z,w):
	input=np.array([[x,y,z,w]]).reshape(1,-1).astype(np.float64)
	final=model.predict(input)
	return final


#---------------------------------------------------------------->

def main():
	
	st.subheader("Enter the following fields")
	 

	#------------------------------------------>

	#Input the required field

	sepal_length = st.text_input("sepal_length","")
	sepal_width = st.text_input("sepal_width ","")
	petal_length= st.text_input("petal_length","")
	petal_width= st.text_input("petal_width","")


	#--------------------------------------------->
	st.markdown(html2, unsafe_allow_html=True)
	st.subheader("Click below button for prediction")
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