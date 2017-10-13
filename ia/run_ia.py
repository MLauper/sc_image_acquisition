from ia.config import Config
from ia.videoStreamer import VideoStreamer
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

    streams[camera] = VideoStreamer()

    protocol = config.get_camera_option(camera, 'protocol')
    ip = config.get_camera_option(camera, 'ip')
    user = config.get_camera_option(camera, 'user')
    password = config.get_camera_option(camera, 'password')
    videocodec = config.get_camera_option(camera, 'videocodec')
    resolution = config.get_camera_option(camera, 'resolution')
    audio = config.get_camera_option(camera, 'audio')
    clock = config.get_camera_option(camera, 'clock')
    overwriteFiles = config.get_global_option('overwriteFiles')

    loop.run_until_complete(streams[camera].streamVideo(camera, videoPath, imagePath, protocol, ip, user, password, videocodec, resolution, audio, clock, overwriteFiles))

loop.close()

#streamer = VideoStreamer()
#streamer.streamVideo(videoPath, imagePath)
