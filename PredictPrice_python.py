def PredictPrice(df):
	import pickle
	with open('C:/tmp/tokyohousing.pickle',mode='rb') as fp:
		model = pickle.load(fp)
		
		x = df[['years','minutes','sqrm','distance','renovate','express']]
		predict_price = model.predict(x)
		df_predict_price = pd.DataFrame(predict_price, columns=['predict'])
		id_predict_price = pd.concat([df[['id']],df_predict_price],axis=1)
	return id_predict_price

def get_output_schema():
	return pd.DataFrame({
		'id' : prep_int(),
		'predict' : prep_decimal()
		})
