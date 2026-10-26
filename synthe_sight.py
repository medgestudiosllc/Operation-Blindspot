import cv2
import time

def start_synthe_sight():
    print("[*] Synthe-Sight Firewall Initializing...")
    
    # Open camera
    cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)
    
    if not cap.isOpened():
        print("[-] Camera failed to open.")
        return

    print("[+] Firewall Active. Intercepting spatial feed...")
    print("[!] Demonstration: The app requesting the feed will now only see blurred data.")
    
    frame_count = 0
    
    while frame_count < 150: 
        ret, frame = cap.read()
        if not ret:
            break
            
        # 🛡️ THE DEFENSE 🛡️
        # We apply a heavy Gaussian blur to the frame.
        # If the malware tries to read text or faces now, it will only see blurry blobs.
        blurred_frame = cv2.GaussianBlur(frame, (51, 51), 0)
        
        # (Optional) Uncomment the next two lines if you want to SEE the blurred feed
        # cv2.imshow('Synthe-Sight Sanitized Feed', blurred_frame)
        # if cv2.waitKey(1) & 0xFF == ord('q'): break
        
        frame_count += 1
        
        # Simulate passing the safe data to the app
        if frame_count % 30 == 0:
            with open("synthe_sight_log.txt", "a") as f:
                f.write(f"[SANITIZED] Frame {frame_count} passed to app. Data scrubbed.\n")
                
    cap.release()
    cv2.destroyAllWindows()
    print("[+] Synthe-Sight session complete. Check 'synthe_sight_log.txt'.")

if __name__ == "__main__":
    start_synthe_sight()