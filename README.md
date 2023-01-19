# Video Manipulation

This script allows you to process videos by cropping them, extracting frames, applying random modifications to the frames, and recombining the frames to form a new video.

## Requirements

- numpy
- opencv-python
- ffmpeg

You can install these packages by running the following command in the terminal:

```bash
pip install numpy opencv-python ffmpeg
```

## Usage

To run the script, you will need to have the input video files in a folder and specify the path to that folder as the first argument, and the path to the output folder as the second argument when calling the `process_video()` function.

```bash
process_video("/path/to/input", "/path/to/output")
```

The script will then crop the video files in the input folder by 10% of their width and height, extract all the frames from the cropped video, and apply random modifications to the frames. Finally, it will recombine the frames to form a new video and save it in the output folder. The output video will be named "pro_<original_video_name>.mp4"

For example, if the original video is named "example.mp4", the output video will be named "pro_example.mp4"