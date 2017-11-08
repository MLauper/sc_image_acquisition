import argparse
from ia.videoStreamer import VideoStreamer

# Parse Arguments
parser = argparse.ArgumentParser(description='This script starts video capturing from a single source.')
parser.add_argument('--name', action='store', default="camera", help='Name of the camera')
parser.add_argument('--camera_id', action='store', default="camera_id", help='The id of the camera stream')
parser.add_argument('--videoPath', action='store', default="C:\\temp\\video\\", help='Folder to store video files')
parser.add_argument('--imagePath', action='store', default="C:\\temp\\image\\", help='Folder to store image files')
parser.add_argument('--protocol', action='store', default="rtsp", help='Protocol to connect to the source')
parser.add_argument('--ip', action='store', help='The IP address of the video source')
parser.add_argument('--user', action='store', default="root", help='The username to authenticate')
parser.add_argument('--password', action='store', help='The password to authenticate')
parser.add_argument('--videocodec', action='store', default="h264", help='The desired video codec')
parser.add_argument('--resolution', action='store', default="1920x1080", help='The desired resolution')
parser.add_argument('--audio', action='store', default="no", help='Audio enabled flag')
parser.add_argument('--clock', action='store', default="yes", help='Clock enabled flag')
parser.add_argument('--overwriteFiles', action='store', default="yes", help='Overwrite existing files')
parser.add_argument('--fps', action='store', default="1", help='Frames extracted per second')
parser.add_argument('--render_on_gpu', action='store', default="1", help='Specify if stream should be rendered on gpu')
parser.add_argument('--gpu_id', action='store', default="1", help='Specify GPU for GPU based rendering')
args = parser.parse_args()

print(args.name)

streamer = VideoStreamer()
streamer.streamVideo(args.name,
                     args.camera_id,
                     args.videoPath,
                     args.imagePath,
                     args.protocol,
                     args.ip,
                     args.user,
                     args.password,
                     args.videocodec,
                     args.resolution,
                     args.audio,
                     args.clock,
                     args.overwriteFiles,
                     args.fps,
                     args.render_on_gpu,
                     args.gpu_id
                     )

