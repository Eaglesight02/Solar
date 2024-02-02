from flask import Flask, request, jsonify
import urllib.request
import os

app = Flask(__name__)


@app.route('/upload_image', methods=['POST'])
def upload_image():
    data = request.get_json()
    img_url = data.get('imgUrl')
    img_name = data.get('imageName')

    # Download the image
    try:
        urllib.request.urlretrieve(img_url, img_name)
        # You can now use the 'img_name' file for further processing or serve it in your response.

        # For example, if you want to send a response back to the client
        return jsonify({"message": "Image received and downloaded successfully"})

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run(debug=True)
