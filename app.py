from flask import Flask, request
import replicate
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def sms():
    resp = MessagingResponse()
    inb_msg = request.form['Body'].lower().strip()
    output = replicate.run(
        "replicate/llama-2-70b-chat:2796ee9483c3fd7aa2e171d38f4ca12251a30609463dcfd4cd76703f22e96cdf",
        input={"prompt": inb_msg, "system_prompt": "You are Klay Thompson--respond to questions as if you were the basketball player", "max_new_tokens":300}
    )
    resp_msg = ''
    for i in output:
        resp_msg+=i
    print(resp_msg)
    resp.message(str(resp_msg))
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)