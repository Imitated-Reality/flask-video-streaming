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


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed_cam1/')
def video_feed_cam1():
    """Video streaming route. Put this in the src attribute of an img tag."""
    cam = Camera(1)
    return Response(gen(cam), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed_cam2/')
def video_feed_cam2():
    """Video streaming route. Put this in the src attribute of an img tag."""
    cam = Camera(0)
    return Response(gen(cam), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, processes=10)
