from ia.config import Config
from ia.videoStreamer import VideoStreamer
from subprocess import call, Popen
import asyncio

config = Config()

videoPath = config.get_video_path()
imagePath = config.get_image_path()
cameras = config.get_cameras()
streams = {}
streams_future = {}
loop = asyncio.get_event_loop()

for camera in cameras:
    print(camera)

    protocol = config.get_camera_option(camera, 'protocol')
    ip = config.get_camera_option(camera, 'ip')
    user = config.get_camera_option(camera, 'user')
    password = config.get_camera_option(camera, 'password')
    videocodec = config.get_camera_option(camera, 'videocodec')
    resolution = config.get_camera_option(camera, 'resolution')
    audio = config.get_camera_option(camera, 'audio')
    clock = config.get_camera_option(camera, 'clock')
    overwriteFiles = config.get_global_option('overwriteFiles')
    fps = config.get_camera_option(camera, 'fps')
    camera_id = config.get_camera_option(camera, 'camera_id')
    render_on_gpu = config.get_camera_option(camera, 'render_on_gpu')
    gpu_id = config.get_camera_option(camera, 'gpu_id')

    streams[camera] = Popen(["python.exe", "start_capture.py",
                             "--name", camera,
                             "--camera", camera_id,
                             "--videoPath", videoPath,
                             "--imagePath", imagePath,
                             "--protocol", protocol,
                             "--ip", ip,
                             "--user", user,
                             "--password", password,
                             "--videocodec", videocodec,
                             "--resolution", resolution,
                             "--audio", audio,
                             "--clock", clock,
                             "--overwriteFiles", overwriteFiles,
                             "--fps", fps,
                             "--render_on_gpu", render_on_gpu,
                             "--gpu_id", gpu_id
                             ])

for camera in cameras:
    streams[camera].wait()
