import shutil
import os

src_jpg = r"C:\Users\Usuario\Desktop\Empresa\Nova logo.jpeg"
src_png = r"C:\Users\Usuario\Desktop\Empresa\Nova_logo-removebg-preview (1).png"
dest_dir = r"c:\Users\Usuario\Desktop\Ecosistema_NovaSolum\portal_central\assets"

if os.path.exists(src_jpg):
    shutil.copy(src_jpg, os.path.join(dest_dir, "logo.jpg"))
    shutil.copy(src_jpg, os.path.join(dest_dir, "favicon.jpg"))
    print("Copied JPG logo successfully")

if os.path.exists(src_png):
    shutil.copy(src_png, os.path.join(dest_dir, "logo.png"))
    shutil.copy(src_png, os.path.join(dest_dir, "favicon.png"))
    print("Copied PNG logo successfully")
