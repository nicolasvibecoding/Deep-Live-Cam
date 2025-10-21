"""
macOS Camera Fix for OpenCV GIL Issues

This module provides a workaround for the "PyEval_RestoreThread: the function
must be called with the GIL held" error that occurs on macOS when OpenCV
requests camera permissions.

The issue occurs because:
1. macOS shows a permission dialog for camera access
2. OpenCV's AVFoundation backend tries to access the camera in a callback
3. The callback runs on a thread without the Python GIL
4. This causes a fatal Python error

Solution: Pre-authorize camera access and use AVFoundation backend explicitly.
"""

import cv2
import platform
import time
import sys


def safe_camera_open(camera_index: int, backend=None):
    """
    Safely open a camera on macOS with proper permission handling.

    Args:
        camera_index: Camera device index (usually 0 for built-in camera)
        backend: OpenCV backend to use (None for auto-select)

    Returns:
        cv2.VideoCapture object or None if failed
    """
    if platform.system() != "Darwin":
        # Not macOS, use standard method
        if backend is not None:
            return cv2.VideoCapture(camera_index, backend)
        return cv2.VideoCapture(camera_index)

    # macOS-specific handling
    print(f"[macOS Camera] Opening camera {camera_index}...")
    print("[macOS Camera] If prompted, please allow camera access.")
    print("[macOS Camera] The application may need to be restarted after granting permission.")

    # Try AVFoundation backend first (recommended for macOS)
    try:
        print("[macOS Camera] Trying AVFoundation backend...")
        cap = cv2.VideoCapture(camera_index, cv2.CAP_AVFOUNDATION)

        if cap.isOpened():
            # Test if we can actually read a frame
            ret, frame = cap.read()
            if ret and frame is not None:
                print("[macOS Camera] Camera opened successfully with AVFoundation!")
                return cap
            else:
                print("[macOS Camera] AVFoundation opened but cannot read frames")
                cap.release()
        else:
            print("[macOS Camera] AVFoundation backend failed to open")
            cap.release()
    except Exception as e:
        print(f"[macOS Camera] AVFoundation error: {e}")

    # Fallback to default backend
    try:
        print("[macOS Camera] Trying default backend...")
        cap = cv2.VideoCapture(camera_index)

        if cap.isOpened():
            ret, frame = cap.read()
            if ret and frame is not None:
                print("[macOS Camera] Camera opened successfully with default backend!")
                return cap
            else:
                print("[macOS Camera] Default backend opened but cannot read frames")
                cap.release()
        else:
            print("[macOS Camera] Default backend failed to open")
    except Exception as e:
        print(f"[macOS Camera] Default backend error: {e}")

    print("[macOS Camera] Failed to open camera")
    print("[macOS Camera] Please check:")
    print("  1. Camera permissions in System Settings > Privacy & Security > Camera")
    print("  2. No other application is using the camera")
    print("  3. The camera is not disabled")

    return None


def test_camera_access(camera_index: int = 0):
    """
    Test camera access and permissions.

    Args:
        camera_index: Camera device index to test

    Returns:
        True if camera is accessible, False otherwise
    """
    cap = safe_camera_open(camera_index)
    if cap is None:
        return False

    # Try to read a few frames to ensure stability
    success_count = 0
    for i in range(5):
        ret, frame = cap.read()
        if ret and frame is not None:
            success_count += 1
        time.sleep(0.1)

    cap.release()

    if success_count >= 3:
        print(f"[macOS Camera] Camera test passed ({success_count}/5 frames)")
        return True
    else:
        print(f"[macOS Camera] Camera test failed ({success_count}/5 frames)")
        return False


if __name__ == "__main__":
    """Test the camera fix"""
    print("Testing macOS camera access...")
    if test_camera_access(0):
        print("✓ Camera is working!")
        sys.exit(0)
    else:
        print("✗ Camera test failed")
        sys.exit(1)
