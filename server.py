#app.logger.info(u'Inserting message: {}'.format(message))#See https://github.com/heroku-examples/python-websockets-chat/blob/master/chat.py

import os
import logging
import gevent
import random
from flask import Flask, render_template, request
from flask_sockets import Sockets
from datetime import datetime

#The following few lines are like copied so idk what they do
app = Flask(__name__)
app.debug = 'DEBUG' in os.environ

sockets = Sockets(app)

chatHistory = ['DigiTea Server started {}'.format(datetime.now())]

@app.route("/chat")
def getPage():
    return render_template('chat-page.html')

@app.route("/get-history", methods=['POST'])
def getHistory():
    global chatHistory
    historyInAString = ''
    for message in chatHistory:
        historyInAString += message
        historyInAString += '\n'
    historyInAString = historyInAString[:-1]
    return (historyInAString, 200)

@app.route("/send-message", methods=['POST'])
def setMessage():
    global chatHistory
    chatHistory.append(request.values.get('message', 'missing_no'))
    if (len(chatHistory) > 250):
        chatHistory = chatHistory[-250:]
    return getHistory()
    #Do stuff

@app.route("/cephaloholic")#Addicted to the head
def getConsole():
    return render_template('console.html')











'''





website = 'custom.html'

args = 'Blank_Screen'
lastRefresh = 'Blank_Screen'
current = 'Blank_Screen'

colors = ['FADA63', 'E68A86', 'DE5284', '9C5292', '74559B', '8C99C9', '83CCD9', '7DCFCE', 'B1D6A0']

#receiving message from slack
@app.route('/slack-message', methods=['POST'])
def receive():##RETURNS TO SLACK NOT THE ACTUAL WEB PAGE
    global website
    global args
    global current
    data = request.values.get('text', 'custom Error Parsing Data')
    #type = data.split(' ', 1)[0]
    #args = data.split(' ', 1)[1]
    app.logger.warning(u'Data: {}'.format(data))
    website = 'custom.html'
    current = data
    args = data
    app.logger.warning(u'Selected Custom Template: {}'.format(data))
    return ('Setting live display screen to custom message...', 200)

@app.route('/page')
def getWebsite():#Returns the actual website(this is where the comp at the front should go)
    #added these two lines
    global website
    global args
    #added above
    app.logger.warning(u'Returning website {} with args {}'.format(website, args))
    return render_template(website, msg2=args, clr=colors[random.randint(0, len(colors) - 1)], animations=animations[random.randint(0, len(animations) - 1)])

@app.route ('/refresh')
def refresh():
    global lastRefresh
    global current
    app.logger.warning(u'Last refresh {}, current {}'.format(lastRefresh, current))
    if lastRefresh != current:
        lastRefresh = current
        app.logger.warning(u'Returning refresh.')
        return ('refresh', 200)
    app.logger.warning(u'Returning keep.')
    return ('keep', 200)#Usually would be keep but idk what happened debugging here


'''
