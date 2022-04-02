# Các bước cài đặt và chạy project 
Bước 1: Cài đặt python, version 3.4 => 3.8
- Link cài đặt: https://www.python.org/
Bước 2: Cấp quyền ExecutionPolicy 
- Chạy power shell bằng Admin
- Chạy: Set-ExecutionPolicy RemoteSigned, chọn A hoặc Y
Bước 3: Tạo môi trường cho project
- Mở terminal trong project, chạy: py -3 -m venv venv
- venv\Scripts\activate
- Trong thư mục venv,file pyenv.cfg, sửa home và version trỏ đến thư mục python trên máy, đảm bảo thư mục 
python đúng với version đã cài 
Bước 4: Cài đặt Flask: https://flask.palletsprojects.com/en/2.0.x/installation/
- pip install flask
Bước 5: Cài đặt Chatterbot: https://chatterbot.readthedocs.io/en/stable/setup.html
- pip install chatterbot 
Hoặc 
- git clone https://github.com/gunthercox/ChatterBot.git
- pip install ./ChatterBot
