#!/bin/bash

# Deep-Live-Cam Kamera-Test für macOS
# Dieses Skript testet ob die Kamera korrekt funktioniert

cd "$(dirname "$0")"

echo "========================================"
echo "Deep-Live-Cam Kamera-Test"
echo "========================================"
echo ""

# Aktiviere das Virtual Environment
source venv/bin/activate

echo "Teste Kamera-Zugriff..."
echo ""

# Führe den Kamera-Test aus
python -m modules.macos_camera_fix

exit_code=$?

echo ""
echo "========================================"
if [ $exit_code -eq 0 ]; then
    echo "✓ Kamera-Test erfolgreich!"
    echo ""
    echo "Du kannst Deep-Live-Cam jetzt starten mit:"
    echo "  ./start.sh"
else
    echo "✗ Kamera-Test fehlgeschlagen!"
    echo ""
    echo "Bitte prüfe:"
    echo "  1. Kamera-Berechtigungen in System Settings"
    echo "  2. Keine andere App nutzt die Kamera"
    echo "  3. Kamera ist nicht deaktiviert"
    echo ""
    echo "Für mehr Hilfe siehe: MACOS_CAMERA_FIX.md"
fi
echo "========================================"

exit $exit_code
