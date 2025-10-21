#!/usr/bin/env python3
"""
Kamera-Auflistungstool für macOS

Dieses Skript listet alle verfügbaren Kameras auf und testet sie.
"""

import cv2
import sys

def list_cameras():
    """Liste alle verfügbaren Kameras auf"""
    print("=" * 60)
    print("Suche nach verfügbaren Kameras...")
    print("=" * 60)
    print()

    available_cameras = []

    # Teste Kamera-Indizes 0-5
    for index in range(6):
        print(f"Teste Kamera-Index {index}...", end=" ")

        # Versuche AVFoundation Backend
        cap = cv2.VideoCapture(index, cv2.CAP_AVFOUNDATION)

        if cap.isOpened():
            # Versuche ein Frame zu lesen
            ret, frame = cap.read()

            if ret and frame is not None:
                height, width, _ = frame.shape
                backend = "AVFoundation"
                available_cameras.append((index, width, height, backend))
                print(f"✓ Gefunden! ({width}x{height}, {backend})")
            else:
                print("✗ Geöffnet aber keine Frames")

            cap.release()
        else:
            # Versuche Default Backend
            cap = cv2.VideoCapture(index)

            if cap.isOpened():
                ret, frame = cap.read()

                if ret and frame is not None:
                    height, width, _ = frame.shape
                    backend = "Default"
                    available_cameras.append((index, width, height, backend))
                    print(f"✓ Gefunden! ({width}x{height}, {backend})")
                else:
                    print("✗ Geöffnet aber keine Frames")

                cap.release()
            else:
                print("✗ Nicht verfügbar")

    print()
    print("=" * 60)
    print(f"Zusammenfassung: {len(available_cameras)} Kamera(s) gefunden")
    print("=" * 60)
    print()

    if available_cameras:
        print("Verfügbare Kameras:")
        for index, width, height, backend in available_cameras:
            print(f"  Index {index}: {width}x{height} ({backend})")

            # Versuche herauszufinden welche Kamera es ist
            if index == 0:
                print(f"           → Vermutlich: FaceTime HD Kamera (MacBook)")
            elif index == 1:
                print(f"           → Vermutlich: Externe Kamera oder iPhone")

        print()
        print("Empfehlung:")
        print(f"  Verwende Index {available_cameras[0][0]} für die eingebaute FaceTime Kamera")

        return available_cameras
    else:
        print("⚠️  Keine Kameras gefunden!")
        print()
        print("Mögliche Probleme:")
        print("  1. Keine Kamera-Berechtigung erteilt")
        print("  2. Kamera wird von anderer App verwendet")
        print("  3. Kamera-Hardware-Problem")
        print()
        return []

def test_camera_switch(index1, index2):
    """Teste das Wechseln zwischen zwei Kameras"""
    print()
    print("=" * 60)
    print(f"Teste Kamera-Wechsel zwischen Index {index1} und {index2}")
    print("=" * 60)

    # Öffne erste Kamera
    print(f"\n1. Öffne Kamera {index1}...")
    cap1 = cv2.VideoCapture(index1, cv2.CAP_AVFOUNDATION)
    if cap1.isOpened():
        ret, frame = cap1.read()
        if ret:
            print(f"   ✓ Kamera {index1} funktioniert")
        cap1.release()

    # Öffne zweite Kamera
    print(f"\n2. Öffne Kamera {index2}...")
    cap2 = cv2.VideoCapture(index2, cv2.CAP_AVFOUNDATION)
    if cap2.isOpened():
        ret, frame = cap2.read()
        if ret:
            print(f"   ✓ Kamera {index2} funktioniert")
        cap2.release()

    # Öffne erste wieder
    print(f"\n3. Öffne Kamera {index1} erneut...")
    cap1 = cv2.VideoCapture(index1, cv2.CAP_AVFOUNDATION)
    if cap1.isOpened():
        ret, frame = cap1.read()
        if ret:
            print(f"   ✓ Kamera {index1} funktioniert wieder")
        cap1.release()

    print("\n✓ Kamera-Wechsel-Test abgeschlossen")

if __name__ == "__main__":
    print()
    cameras = list_cameras()

    # Wenn mehrere Kameras gefunden wurden, teste das Wechseln
    if len(cameras) >= 2:
        test_camera_switch(cameras[0][0], cameras[1][0])

    sys.exit(0 if cameras else 1)
