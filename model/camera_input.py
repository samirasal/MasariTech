import cv2
import os

def create_output_directory(output_dir="captured_images"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir

def capture_images(output_dir):
    cap = cv2.VideoCapture(0)  
    if not cap.isOpened():
        print("Error: Could not access the camera.")
        return

    print("Position yourself for the front view. Press 'SPACE' to capture, 'ESC' to exit.")
    views = ["front", "side", "back"]
    for view in views:
        print(f"Capturing {view} view...")
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame.")
                break
            
            cv2.imshow(f"Capture {view} view", frame)

            key = cv2.waitKey(1)
            if key == 27:  
                print("Exiting capture process.")
                break
            elif key == 32: 
                image_path = os.path.join(output_dir, f"{view}.jpg")
                cv2.imwrite(image_path, frame)
                print(f"Saved {view} view to {image_path}")
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    output_dir = create_output_directory()
    capture_images(output_dir)
