import os

saved_content = None

def save_original_file(file_path: str):
    with open(file_path, "r") as f:
        saved = f.read()
    saved_content[file_path] = saved
    # 存到lcmbackup里面
    if not os.path.exists("lcmbackup"):
        os.makedirs("lcmbackup")
    with open(f"lcmbackup/{file_path}", "w") as f:
        f.write(saved)
