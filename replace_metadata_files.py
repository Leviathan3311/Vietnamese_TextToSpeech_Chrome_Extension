
import os
import shutil

def replace_metadata_files(folder1, folder2):
    # Duyệt qua từng thư mục con trong dataset2
    for subfolder in os.listdir(folder2):
        folder2_subfolder_path = os.path.join(folder2, subfolder)
        folder1_subfolder_path = os.path.join(folder1, subfolder)

        # Kiểm tra xem thư mục con có tồn tại trong cả hai folder và là thư mục
        if os.path.isdir(folder2_subfolder_path) and os.path.isdir(folder1_subfolder_path):
            # Đường dẫn tới file metadata.csv trong mỗi folder
            file2_path = os.path.join(folder2_subfolder_path, 'metadata.csv')
            file1_path = os.path.join(folder1_subfolder_path, 'metadata.csv')

            # Kiểm tra xem file metadata.csv có tồn tại trong dataset2
            if os.path.exists(file2_path):
                # Sao chép file metadata.csv từ dataset2 sang dataset1 và ghi đè nếu có
                shutil.copy2(file2_path, file1_path)
                print(f"Replaced {file1_path} with {file2_path}")

# Sử dụng ví dụ
folder1 = r'datasets'  # Thư mục gốc chứa các thư mục con của dataset1
folder2 = r'Bản sao datasets'  # Thư mục gốc chứa các thư mục con của dataset2
replace_metadata_files(folder1, folder2)
print("Done")
