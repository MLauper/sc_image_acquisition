import ffmpy

class VideoStreamer():
    """This class can stream a video from RTSP and save it locally"""

    def streamVideo(self, camera, camera_id, videoPath, imagePath, protocol, ip, user, password, videocodec, resolution, audio, clock, overwriteFiles, fps, render_on_gpu, gpu_id):

        globalOptions = '-rtsp_transport tcp' + (' -y' if overwriteFiles else '')
        inputStream = protocol + '://' + user + ':' + password + '@' + ip + '/axis-media/media.amp?videocodec=' + videocodec + '&camera=' + camera_id + '&resolution=' + resolution + '&audio=' + audio + '&clock=' + clock

        output_parameters = '-vcodec copy'
        # if (render_on_gpu):
        #     output_parameters = '-vcodec h264_nvenc -gpu ' + gpu_id
        # else:
        #     output_parameters = ''

        ff = ffmpy.FFmpeg(
            global_options=globalOptions,
            inputs={inputStream: '-vcodec h264_cuvid'},
            outputs={
                (videoPath + 'out_' + camera + '.mkv'): output_parameters,
                (imagePath + 'out_' + camera + '_%d.jpg'): ('-vf fps=' + fps)
            }
        )
        print(ff.cmd)

        ff.run()
