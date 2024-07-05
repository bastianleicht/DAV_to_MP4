import os
import subprocess
import time

total_start = time.time()

DAV_INPUT = "."
MP4_OUTPUT = ".\Converted"
FFMPEG = "ffmpeg"


def convert_dav_mp4(dav_path, mp4_path):
    start = time.time()

    command = [FFMPEG, '-y', '-i', dav_path, mp4_path]
    pipe = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    pipe.communicate()

    end = time.time()

    print(f"Time taken in Minutes : {(end - start) / 60}")


if __name__ == "__main__":
    print("------Listing the DAV Files------")
    # List the directories of DAV input path
    listdavfiles = os.listdir(DAV_INPUT)
    # list the directors if .dav extension is present and store in DAVfilesonly list
    DAVfilesonly = [davfiles for davfiles in listdavfiles if davfiles.endswith('.dav')]

    print("------Converting DAV files to MP4 files------")

    for i, DAVinput in enumerate(DAVfilesonly):
        # File name used as same as DAV but the extension is different
        MP4file = os.path.splitext(DAVinput)[0] + '.mp4'

        # Input file and output file path
        DAV_Videoinput = os.path.join(DAV_INPUT, DAVinput)
        MP4_Videooutput = os.path.join(MP4_OUTPUT, MP4file)
        print(f"Processing : {i + 1} file")

        # Function to convert DAV to mp4
        convert_dav_mp4(DAV_Videoinput, MP4_Videooutput)

    total_end = time.time()
    print("------Converted into MP4 files------")
    print(f"Total time taken in Minutes : {(total_end - total_start) / 60}")
