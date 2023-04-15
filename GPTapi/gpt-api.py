import openai

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
   print("Hello Painful world")
   return "<p> Hello World </p>"

@app.route("/concatenate", methods=["POST"])
def concatenate():
 
  data = request.get_json()
  result = data.get("result")
  print(result)
  result = call_GPT(result)
  return result

def call_GPT(userInput):

   completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
         {"role": "system", "content": "The answer musy always include these sections, greeting, diagnosis, remedies to alleviate the discomfort, over the counter medication and conclusion. This advice should be coming from Dr. GPT, an AI doctor. Provide a very very lengthy friendly response going into details. Answer should be in html format using div and other html tags and highlight important advices in bold."},
         {"role": "user", "content": userInput}
      ]
   )
   gptMessage = completion.choices[0].message
   print(gptMessage["content"])
   return gptMessage["content"]

 