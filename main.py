from flask import Flask, jsonify, render_template, request
import os
import json
from web3 import Web3
import requests
from wordcloud import WordCloud

wc = WordCloud()

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

# initial wordcloud_storage.txt populated with a single address: 0x5c43B1eD97e52d009611D89b74fA829FE4ac56b1 (aka pileofscraps.eth) so that the initial pong has data
@app.route('/server', methods=['GET', 'POST'])
def server():

	if request.method == 'POST':

		result = request.data
		print(result)
		result = json.loads(result)

		for i in range(len(result["activity"])):
			from_address = (result["activity"][i]["fromAddress"])

			f = open("wordcloud_storage.txt", "a")
			f.write(str(from_address)+" ")
			f.close()

		print("---Printing: DATA WRITE----")
		text = open('wordcloud_storage.txt').read()
		print(text)

		return ("OK")


	if request.method == 'GET':
		id = request.args.get('id')
		print('ID', id)

		print("---Printing: DATA READ----")
		text = open('wordcloud_storage.txt').read()
		print(text)
		wc = WordCloud(background_color="white", max_words=100)

		# generate word cloud
		wc.generate(text)
		svg_text = wc.to_svg()
		print(svg_text)

		pic = {"name":"Address Rainfall 0x00","description":"Off-Chain Word Cloud Generation","image_data":str(svg_text),"attributes":[{"trait_type":"Isaac Lau","value":"One"},{"trait_type":"Adam","value":"One"},{"trait_type":"Austin","value":"One"},{"trait_type":"Xiangan","value":"One"}]}

		return (pic)


	#return render_template('index.html', form=form, bal=balance, block_num=block_num, total_burn=total_burn)


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
