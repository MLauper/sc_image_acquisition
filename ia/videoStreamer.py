import ffmpy

class VideoStreamer():
    """This class can stream a video from RTSP and save it locally"""

    def streamVideo(self, camera, videoPath, imagePath, protocol, ip, user, password, videocodec, resolution, audio, clock, overwriteFiles):

        globalOptions = '-rtsp_transport tcp' + (' -y' if overwriteFiles else '')
        inputStream = protocol + '://' + user + ':' + password + '@' + ip + '/axis-media/media.amp?videocodec=' + videocodec + '&resolution=' + resolution + '&audio=' + audio + '&clock=' + clock + '&duration=10'

        ff = ffmpy.FFmpeg(
            global_options=globalOptions,
            inputs={inputStream: '-vcodec h264_cuvid'},
            outputs={
                (videoPath + 'out_' + camera + '.mkv'): '-vcodec h264_nvenc',
                (imagePath + 'out_' + camera + '_%d.jpg'): '-vf fps=1'
            }
        )
        print(ff.cmd)

        ff.run()
