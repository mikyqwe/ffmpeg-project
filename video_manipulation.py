import os
import random
import numpy as np
import cv2

def process_video(input_folder, output_folder):
    # Iterate through all the files in the input folder
    for file in os.listdir(input_folder):
        if file.endswith(".mp4"):
            # Get the full path of the input file
            input_path = os.path.join(input_folder, file)
            # Create the output path for the cropped video
            cropped_output_path = os.path.join(output_folder, "cropped_" + file)
            # Crop the video by 10% width and 10% height
            os.system(f'ffmpeg -i {input_path} -vf "crop=iw*0.9:ih*0.9" {cropped_output_path}')
            # Create the frames folder
            frames_folder = os.path.join(output_folder, "frames")
            if not os.path.exists(frames_folder):
                os.makedirs(frames_folder)
            # Extract all the frames from the cropped video
            os.system(f'ffmpeg -i {cropped_output_path} -vf "fps=1" {os.path.join(frames_folder, "frame%d.png")}')
            # Iterate through all the frames
            for i in range(len(os.listdir(frames_folder))):
                # Get the full path of the current frame
                frame_path = os.path.join(frames_folder, f"frame{i}.png")
                # Load the frame
                frame = cv2.imread(frame_path)
                # Replace frame with the one before it at a 14% chance
                if random.random() < 0.14:
                    frame = cv2.imread(os.path.join(frames_folder, f"frame{i-1}.png"))
                # Add 5% random gaussian noise to the frame
                frame = frame + np.random.normal(0, 0.05, frame.shape)
                # Change the red, blue, green, and alpha channels by 5-10% randomly
                for channel in range(frame.shape[2]):
                    frame[:, :, channel] = frame[:, :, channel] * random.uniform(0.95, 1.05)
                # Brighten or darken the frame by 5-10% randomly
                frame = frame * random.uniform(0.95, 1.05)
                # Save the modified frame
                cv2.imwrite(frame_path, frame)
            # Create the output path for the final video
            output_path = os.path.join(output_folder, "pro_" + file)
            # Combine the frames to form a video
            os.system(f'ffmpeg -framerate 1 -i {os.path.join(frames_folder, "frame%d.png")} -c:v libx264 -r 30 -pix_fmt yuv420p {output_path}')

# Example usage:
process_video("/path/to/input", "/path/to/output")