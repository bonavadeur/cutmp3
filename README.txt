HƯỚNG DẪN CUT FILE .MP3

Prerequisite:
	+ download ffmpeg (có sẵn trong git repo này) và thêm thư mục bin vào Env path của Windows

Bước 1:
	+ xoá file.mp3 trong folder này (nếu có)
	+ copy file nhạc vào folder này.
	+ đổi tên file nhạc thành file.mp3

Bước 2: double-click vào script.exe, nhập số đoạn cần chia, ví dụ: 3

Bước 3:
Ví dụ 1 video dài 14p53s, ta cần chia thành các đoạn:
	0:00 -> 5:00
	5:00 -> 10:00
	10:00 -> hết

Nhập thì nhập vào là:
	minutes-1:5
	seconds-1:0

	minutes-2:10
	seconds-2:0

tức là nhập các mốc thời gian vào, chia 4 đoạn thì nhập tương tự

Bước 4: đợi một lúc sẽ hiện ra 3 file kết quả rồi tắt cửa sổ màu đen đi.
	