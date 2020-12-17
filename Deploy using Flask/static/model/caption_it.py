import numpy as np
import pickle
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
import os

def encode_img(path):
	model=load_model("./static/model/model_00.h5")
	img=image.load_img(path,target_size=(224,224))
	img=image.img_to_array(img)
	img=np.array(img)
	img=np.expand_dims(img,axis=0)
	img=preprocess_input(img)
	features=model.predict(img)
	features=features.reshape(-1,)
	return features

def predict_cap(photo):
	with open("./static/model/index2word.pkl","rb") as f:
		idx_to_word=pickle.load(f)
	with open("./static/model/word2index.pkl","rb") as f:
		word_to_idx=pickle.load(f)
	in_txt="startseq"
	for i in range(35):
		sequence=[word_to_idx[w] for w in in_txt.split() if w in word_to_idx]
		seq=pad_sequences([sequence],maxlen=35,value=0,padding='post')
		loaded_model = load_model('./static/model/model_29.h5')
		y_pred=loaded_model.predict([photo,seq])
		y_pred=y_pred.argmax()
		word=idx_to_word[y_pred]
		in_txt+=' '+word

		if word=='endseq':
			break

	final_cap=in_txt.split()[1:-1]
	final_cap=' '.join(final_cap)

	return final_cap

def get_caption(path):
	encoded_test=encode_img(path)
	photo=encoded_test.reshape(1,2048)
	caption=predict_cap(photo)
	return caption
