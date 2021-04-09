from app import App, db
from flask import current_app as app, render_template, request, redirect, url_for, jsonify
from app.models import divvyData
from datetime import datetime

@app.route('/averageTripDuration/<string:start, string:end>')
def getAverageDuration(id):
    data = divvyData.query.filter(divvyData.start_time.between('start','end')).all()
    averageTripDuration = sum([data[i].trip_duration for i in range(len(data))])/len(data)
    return averageTripDuration



#data = divvyData.query.filter(divvyData.start_time.between('2013-06-28 12:16:00','2013-07-01 14:26:00')).all()