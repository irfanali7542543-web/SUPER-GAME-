#!/bin/bash
git add signals.json
git commit -m "Auto-update signals by FX Master"
git push origin main
echo "Siganls updated successfully on Web!"
