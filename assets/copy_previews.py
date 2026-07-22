import shutil
import os

brain_dir = r"C:\Users\Usuario\.gemini\antigravity-ide\brain\50073fd1-3ddc-4e80-a9ce-9576e31ba138"
dest_dir = r"c:\Users\Usuario\Desktop\Ecosistema_NovaSolum\portal_central\assets"

files = {
    "crm_preview_1784729705398.png": "crm_preview.png",
    "geoweb_preview_1784729727630.png": "geoweb_preview.png",
    "geoasist_preview_1784729745231.png": "geoasist_preview.png",
    "farmago_preview_1784729763535.png": "farmago_preview.png",
    "simulador_preview_1784729784477.png": "simulador_preview.png"
}

for src_name, dest_name in files.items():
    src = os.path.join(brain_dir, src_name)
    dest = os.path.join(dest_dir, dest_name)
    if os.path.exists(src):
        shutil.copy(src, dest)
        print(f"Copied {dest_name} successfully")
    else:
        print(f"Source {src_name} not found")
