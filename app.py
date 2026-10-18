
from flask import Flask, request
import math
app = Flask(__name__)


@app.route('/IloveItransition/heythemboudjema_gmail_com')
def Calculate():
    x=request.args.get('x',type=int)
    y=request.args.get('y',type=int)
    if x==None or y==None:
        return "NaN"
    if x < 0 or y < 0:
        return "NaN"
    if x==0 or y==0:
        return "0"
    lcd=0
    lcd=(x*y)/math.gcd(x,y)
    return str(lcd)


if __name__ == '__main__':
    app.run()
