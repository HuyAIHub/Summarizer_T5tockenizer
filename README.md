# Summarizer_T5tockenizer
## BƯỚC 1: Clone dự án xuống
   ```sh
   git clone https://github.com/Quanghuy99/Summarizer_T5tockenizer.git
   ```
## BƯỚC 2: Cài thư viện pytorch
### note: tùy vào os với môi trường thì chọn và copy lệnh install tương ứng
link :https://pytorch.org/get-started/locally/
![image](https://github.com/Quanghuy99/Summarizer_T5tockenizer/assets/30777550/0ad0443e-589e-4576-b6f3-2e67daba383d)

### vd: os là ubuntu và sử dụng anaconda 
   ```sh
   conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia
   ```
## BƯỚC 3: cài các dependencies
   ```sh
   pip install -r requirements.txt
   ```
## BƯỚC 4: chạy code
   ```sh
   python3 app.py
   ```
## BƯỚC 5: chạy API bằng cách nhét 1 đoạn văn bản cần tóm tắt vô.
link api: http://localhost:8686/docs
![image](https://github.com/Quanghuy99/Summarizer_T5tockenizer/assets/30777550/e030b90a-d252-4e63-8dad-e78f5f8eb5a0)


# done!
