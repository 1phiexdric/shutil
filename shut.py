import shutil

def get_ffmpeg_path():
    """
    This function returns the path of the ffmpeg executable if it is installed, otherwise it returns None.
    """
    return shutil.which('ffmpeg')
ffmpeg_ruta = get_ffmpeg_path()

print("Ruta de ffmpeg:", ffmpeg_ruta)