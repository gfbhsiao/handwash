from argparse import ArgumentParser
from extract_module import extract

parser = ArgumentParser()
parser.add_argument("--video_path", help="path of video to be extracted")
parser.add_argument("-f", help="path of destiny folder",
                    default=".\dest", dest="folder_path")
parser.add_argument("-n", help="path of destiny folder",
                    default=-1, dest="max_img_number", type=int)
parser.add_argument(
    "-r", help="ratio of frame to be skipped to frame to be extracted",
    default=5, dest="extract_ratio", type=int)

#video_path = parser.parse_args().video_path
#video_path = "/vedio/finger.MOV"
#video_path = "C:/Users/Vicki/Documents/GitHub/handwash/vedio/finger.MOV"
video_path="C:\\Users\\Vicki\\Documents\\GitHub\\handwash\\vedio\\palm.MOV"
print(video_path)
folder_path = parser.parse_args().folder_path
max_img_number = parser.parse_args().max_img_number
extract_ratio = parser.parse_args().extract_ratio

extract(
    video_path=video_path, folder_path=folder_path,
    max_img_number=max_img_number, extract_ratio=extract_ratio)