from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/', methods = ['GET','POST']) #Here we enable the GET and POST methods
def home():
	if(request.method == 'GET'): #
		data = "hello world"
		return jsonify({'data': data})
	
	if(request.method == 'POST'):
		data = request.get_json()
		return jsonify(data)

@app.route('/home/<int:num>', methods = ['GET'])
def disp(num):
	return jsonify({'data': num**2})

@app.route('/test_json', methods = ['POST'])
def test_json():
	if(request.method == 'POST'):
		#data_id = request.form.get('Id')
		#data_customer = request.form.get('Customer')
		#data_quantity  = request.form.get('Quantity')
		#data_price = request.form.get('Price')
		data_id = request.get_json()['Id']
		data_customer = request.get_json()['Customer']
		data_quantity = request.get_json()['Quantity']
		data_price = request.get_json()['Price']
		print('Id: ', data_id)
		print('Customer: ', data_customer)
		print('Quantity: ', data_quantity)
		print('Price: ', data_price)
		return jsonify({'data': 'success'})
		
@app.route('/test', methods = ['GET','POST'])
def test():
	if(request.method == 'POST'):
		content_type = request.headers.get('Content-Type')
		print(content_type)
		data_id = request.form.get('ID')
		data_customer = request.form.get('Customer')
		data_quantity  = request.form.get('Quantity')
		data_price = request.form.get('Price')
		print('Id: ', data_id)
		print('Customer: ', data_customer)
		print('Quantity: ', data_quantity)
		print('Price: ', data_price)
	return render_template('test.html')

if __name__ == '__main__':
	app.run()
