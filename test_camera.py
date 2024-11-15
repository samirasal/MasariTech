import cv2

def test_camera():
    print("Testing camera...")
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open camera")
        return
        
    print("Reading frame...")
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame")
        return
        
    print("Showing frame...")
    cv2.imshow('Test', frame)
    cv2.waitKey(3000)  # Wait for 3 seconds
    
    cap.release()
    cv2.destroyAllWindows()
    print("Test complete")

if __name__ == "__main__":
    test_camera()