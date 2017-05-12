#!/usr/bin/env python
from flask import Flask, render_template, Response, send_file
# emulated camera
from camera import Camera
# Raspberry Pi camera module (requires picamera package)
# from camera_pi import Camera

app = Flask(__name__)


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

@app.route('/ping')
def ping():
    return "available"


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/changeRotation/<int:value>')
def change_rotation(value):
    if(value > 10):
		print "Rotate Right"
    else:
		print "Rotate left"

@app.route('/video_feed_cam1/')
def video_feed_cam1():
    """Video streaming route. Put this in the src attribute of an img tag."""
    cam = Camera(0)
    return Response(gen(cam), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed_cam2/')
def video_feed_cam2():
    """Video streaming route. Put this in the src attribute of an img tag."""
    cam = Camera(1)
    return Response(gen(cam), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/cam1/')
def cam1():
    return render_template('video_feed_cam1.html')

@app.route('/cam2/')
def cam2():
    return render_template('video_feed_cam2.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True, processes=10)
