import cv2
import os
def extract_hand(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = remove_background(img)
    img = remove_skin(img)

    return img

def remove_background(img):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i][j][0] > 113 and img[i][j][1] > 97 and img[i][j][2] > 89:
                img[i][j][0] = 230
                img[i][j][1] = 230
                img[i][j][2] = 230
    return img

def remove_skin(img):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i][j][0] > 83 and img[i][j][1] > 32 and img[i][j][2] > 20:
                img[i][j][0] = 230
                img[i][j][1] = 230
                img[i][j][2] = 230

    return img

def remove_hands(image_directory, output_folder):
    image_files = [f for f in os.listdir(image_directory) if f.endswith('.png')]
    count = 0

    for image_file in image_files:
        input_image_path = os.path.join(image_directory, image_file)
        image = cv2.imread(input_image_path)
        #image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        result = extract_hand(image)
        result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
        im_filename = os.path.join(output_folder, 'frame_' + str(count) + '.png')
        cv2.imwrite(im_filename, result)
        count += 1

def extract_frames(video_file: str, output_folder: str):

    cap = cv2.VideoCapture(video_file)

    if not cap.isOpened():
        print("Error: Could not open video file.")
        exit()
    # Initialize variables
    frame_count = 0
    frame_interval = 3  # Save every fifth frame

    os.makedirs(output_folder, exist_ok=True)
    counter = 0
    while True:
        # Read the next frame
        ret, frame = cap.read()

        if not ret:
            break  # Break the loop if we've reached the end of the video

        frame_count += 1

        # Check if it's time to save this frame (every fifth frame)
        if frame_count % frame_interval == 0:
            # Save the frame as an image in the output folder
            frame_filename = os.path.join(output_folder, f'frame_{counter}.png')
            cv2.imwrite(frame_filename, frame)
            print(f'Saved frame {counter}')
            counter += 1
    # Release the video capture object and close the output folder
    cap.release()
    cv2.destroyAllWindows()

    print("Frames saved successfully.")

