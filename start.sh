#!/bin/bash

# Deep-Live-Cam Startskript für macOS (M1 Pro)
# Dieses Skript aktiviert das Virtual Environment und startet Deep-Live-Cam

cd "$(dirname "$0")"

# Aktiviere das Virtual Environment
source venv/bin/activate

# Starte Deep-Live-Cam mit CoreML (Apple Silicon Beschleunigung)
python3.11 run.py --execution-provider coreml

# Alternativ: CPU-only Modus (langsamer, aber stabiler)
# python3.11 run.py --execution-provider cpu
