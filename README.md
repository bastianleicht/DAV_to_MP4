# DAV_to_MP4
 Most of the CCTV Camera output format as DAV files. Using ffmpeg we can Convert DAV format to Mp4 format. The ffmpeg already a "Multiprocessing" one.


## Installation

### Linux

```bash
sudo apt-get install ffmpeg
```

### Windows

```bash
winget install "FFmpeg (Essentials Build)"
```

## Usage

Run the script in the Directory with all the DAV files, and create a Directory named "Converted".

```bash
python3 DAV2MP4Convert.py
```

The Script then exports the Converted files to the "Converted" Directory.
