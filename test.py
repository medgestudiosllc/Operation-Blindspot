import cv2

# Open the default camera (usually 0)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

print("Camera is open! Press 'q' on your keyboard to quit.")

while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    
    if not ret:
        print("Can't receive frame. Exiting...")
        break

    # Show the frame in a window called "Operation Blindspot"
    cv2.imshow('Operation Blindspot', frame)

    # Wait for 1 millisecond, and check if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the windows
cap.release()
cv2.destroyAllWindows()
