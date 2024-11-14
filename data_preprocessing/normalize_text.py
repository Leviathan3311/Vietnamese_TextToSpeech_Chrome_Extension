import pandas as pd
import os

def convert_csv_to_txt_with_speaker(file_path, speaker, output_path=None):
    # Đọc file CSV và thêm tên cột
    df = pd.read_csv(file_path, header=None, sep='|', names=['audio_filename', 'raw_text'])
    
    # Thêm cột 'speaker' với giá trị do người dùng tự điều chỉnh
    df['speaker'] = speaker
    
    # Đặt tên file output nếu không có output_path
    if output_path is None:
        output_path = file_path.replace('.csv', '.txt')
    
    # Lưu file thành định dạng TXT với '|' làm dấu phân cách và không có header
    df.to_csv(output_path, sep='|', index=False, header=False, encoding='utf-8')
    print(f"File saved to {output_path}")

# Ví dụ sử dụng
file_path = r'code/datasets/TẤT TẦN TẬT về ĐẦU TƯ CƠ BẢN/metadata.csv'  # Đường dẫn đến file CSV
speaker = "Male_01"                     # Giá trị cho cột speaker, tự điều chỉnh theo yêu cầu
convert_csv_to_txt_with_speaker(file_path, speaker)
