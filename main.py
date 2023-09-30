from functions_utils import *
from google.colab import files

def process_data(images_frames: str, input_folder: str, colmap_output: str):
    remove_hands(images_frames, input_folder)
    os.system(f'ns-process-data images --data {input_folder} --output-dir {colmap_output}')


def nerf_train(colmap_output: str):
    os.system(
        f'ns-train nerfacto --viewer.websocket-port 7007 nerfstudio-data --data {colmap_output} --downscale-factor 10')

def render_video(video_filename: str):
    base_dir = 'outputs/unnamed/nerfacto/'
    training_run_dir = base_dir + os.listdir(base_dir)[0]
    os.chdir(training_run_dir)
    uploaded = files.upload()
    uploaded_camera_path_filename = list(uploaded.keys())[0]
    config_filename = training_run_dir + "/config.yml"
    camera_path_filename = training_run_dir + "/" + uploaded_camera_path_filename
    camera_path_filename = camera_path_filename.replace(" ", "\\ ").replace("(", "\\(").replace(")", "\\)")
    os.chdir('Project')
    os.system(f'!ns-render camera-path --load-config {config_filename} --camera-path-filename {camera_path_filename} --output-path {video_filename}')


if __name__ == '__main__':
    video_name = 'IMG_1136.MOV'
    images_folder = 'frames'
    extract_frames(video_name, images_folder)
    output_dir = 'no_hand_frames'
    custom_data = 'colmap_output'
    process_data(images_folder, output_dir, custom_data)
    nerf_train(custom_data)
    render_file_name = 'rendered_result.mp4'
    render_video(render_file_name)