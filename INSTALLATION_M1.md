# Deep-Live-Cam Installation auf M1 MacBook Pro

## ✅ Installation abgeschlossen!

Deep-Live-Cam wurde erfolgreich auf deinem MacBook M1 Pro eingerichtet.

## 📋 Was wurde installiert:

1. **Python 3.11** - via Homebrew
2. **FFmpeg** - für Video-Verarbeitung
3. **python-tk@3.11** - für die GUI
4. **Virtual Environment** - isolierte Python-Umgebung
5. **Python Dependencies** - alle erforderlichen Bibliotheken
6. **ML-Modelle**:
   - GFPGANv1.4.pth (332 MB) - Gesichtsverbesserung
   - inswapper_128_fp16.onnx (264 MB) - Face-Swapping

## 🚀 Starten von Deep-Live-Cam

### Methode 1: Mit dem Startskript (Empfohlen)
```bash
cd "/Users/nicolasdamerius/Desktop/Coding Projekte/DeepLiveCam/Deep-Live-Cam"
./start.sh
```

### Methode 2: Manuell
```bash
cd "/Users/nicolasdamerius/Desktop/Coding Projekte/DeepLiveCam/Deep-Live-Cam"
source venv/bin/activate
python3.11 run.py --execution-provider coreml
```

### Methode 3: Nur GUI (kein CoreML)
```bash
cd "/Users/nicolasdamerius/Desktop/Coding Projekte/DeepLiveCam/Deep-Live-Cam"
source venv/bin/activate
python3.11 run.py
```

## ⚡ Hardware-Beschleunigung

**CoreML** ist für dein M1 MacBook optimiert und nutzt die Neural Engine:
```bash
python3.11 run.py --execution-provider coreml
```

**CPU-Modus** (Fallback):
```bash
python3.11 run.py --execution-provider cpu
```

## 🎯 Verwendungsmodi

### 1. GUI-Modus (Standard)
Einfach `python3.11 run.py` ausführen und das grafische Interface verwenden.

### 2. Live Webcam-Modus
1. GUI starten
2. Quellbild auswählen (das Gesicht, das du verwenden möchtest)
3. "Live" Button klicken
4. Warten bis Preview erscheint (10-30 Sekunden)
5. Mit OBS oder ähnlicher Software streamen

### 3. Bild/Video-Verarbeitung
1. GUI starten
2. Quellbild auswählen
3. Ziel-Bild oder Video auswählen
4. "Start" klicken
5. Output wird im selben Verzeichnis gespeichert

### 4. CLI-Modus
```bash
python3.11 run.py \
  --source face.jpg \
  --target video.mp4 \
  --output result.mp4 \
  --execution-provider coreml
```

## 🛠️ Wichtige Parameter

- `--many-faces` - Alle Gesichter im Video verarbeiten
- `--mouth-mask` - Original-Mund beibehalten
- `--map-faces` - Spezifisches Face-Mapping verwenden
- `--keep-fps` - Original FPS beibehalten
- `--keep-audio` - Original Audio beibehalten
- `--video-quality [0-51]` - Video-Qualität (0=beste, 51=schlechteste)
- `--max-memory 4` - RAM-Limit in GB (Standard 4GB für macOS)

## 📁 Projektstruktur

```
Deep-Live-Cam/
├── venv/                  # Virtual Environment
├── models/                # ML-Modelle
│   ├── GFPGANv1.4.pth
│   └── inswapper_128_fp16.onnx
├── modules/               # Python Module
├── run.py                 # Hauptprogramm
├── start.sh              # Startskript
└── requirements_macos.txt # macOS Dependencies
```

## ⚠️ Hinweise

1. **Erster Start**: Beim ersten Start werden zusätzliche Modelle (~300MB) heruntergeladen
2. **Kamera-Berechtigungen**: macOS wird nach Kamera-Zugriff fragen - erlauben!
3. **Performance**: CoreML nutzt die Neural Engine deines M1 für beste Performance
4. **Ethik**: Verwende dieses Tool verantwortungsvoll und legal!

## 🐛 Fehlerbehebung

### Kamera-Problem: "PyEval_RestoreThread: GIL error"

**Problem**: Absturz beim Kamera-Zugriff mit GIL-Fehler

**Lösung**:
1. Dieser Fehler wurde bereits gefixt! Die neuesten Änderungen enthalten einen macOS Camera Fix.
2. Stelle sicher, dass Kamera-Berechtigungen erteilt sind:
   - `Systemeinstellungen` > `Datenschutz & Sicherheit` > `Kamera`
   - Aktiviere `Terminal` oder deine IDE
3. Teste die Kamera:
   ```bash
   python -m modules.macos_camera_fix
   ```
4. Ausführliche Informationen: Siehe [MACOS_CAMERA_FIX.md](MACOS_CAMERA_FIX.md)

### "tkinter missing" Fehler
```bash
brew reinstall python-tk@3.11
```

### Virtual Environment Probleme
```bash
rm -rf venv
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements_macos.txt
```

### CoreML Fehler
Fallback auf CPU:
```bash
python3.11 run.py --execution-provider cpu
```

### Kamera-Berechtigungen zurücksetzen
Falls die Kamera nicht erkannt wird:
```bash
tccutil reset Camera
# Dann App neu starten und Berechtigung erneut erteilen
```

## 📚 Weitere Informationen

- **GitHub**: https://github.com/hacksider/Deep-Live-Cam
- **README**: [README.md](README.md)
- **Models**: Die Modelle sind nur für nicht-kommerzielle Forschungszwecke

## 🎉 Viel Spaß!

Deep-Live-Cam ist bereit! Vergiss nicht:
- Hol die Zustimmung der Person, deren Gesicht du verwendest
- Kennzeichne Deepfakes klar als solche
- Verwende das Tool ethisch und legal
