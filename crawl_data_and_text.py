import pandas as pd
from vctube import VCtube
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Ẩn cửa sổ Tkinter
Tk().withdraw()
file_path = askopenfilename(title="Chọn file sheet", filetypes=[("Excel files", "*.xlsx"), ("CSV files", "*.csv"), ("Text files", "*.txt")])

# Đọc file theo định dạng
if file_path.endswith('.xlsx'):
    df = pd.read_excel(file_path)
elif file_path.endswith('.csv'):
    df = pd.read_csv(file_path)
elif file_path.endswith('.txt'):
    df = pd.read_csv(file_path, delimiter="\t", header=None)  # Đọc file .txt với tab làm delimiter và không có header
    df.columns = ['Title', 'Link']  # Gán tên cột giả định

# Xóa khoảng trắng ở đầu và cuối tên cột nếu có
df.columns = df.columns.str.strip()

# Duyệt từng dòng để thực hiện crawl dữ liệu
for index, row in df.iterrows():
    playlist_name = row[0]  # Cột 1 là Title
    playlist_url = row[1]   # Cột 2 là Link

    # Khởi tạo đối tượng VCtube với đường dẫn output là thư mục con
    vc = VCtube(playlist_name, playlist_url, lang="vi")
    vc.output_dir = playlist_name  # Chỉ định thư mục đích cho từng playlist

    # Thực hiện các thao tác download và xử lý audio
    vc.download_audio()      # Download audios từ YouTube
    vc.download_captions()   # Download captions từ YouTube
    vc.audio_split()         # Split audio với captions
