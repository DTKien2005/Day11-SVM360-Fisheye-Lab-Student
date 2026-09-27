# 10 — Đọc 10 phút: từ một camera tới hệ 360°/SVM

Bài lab này chỉ thực hành trên **một** camera fisheye (ADASIND). Slide Ngày 11 nói về hệ **Surround View
Monitoring (SVM)** với **4 camera** (trước, sau, trái, phải) ghép lại. Đọc phần này trước khi trả lời câu
360°/cross-camera ở `50_exit_ticket.md`.

## 4 camera và vùng chồng (seam)

Bốn camera fisheye gắn quanh xe có vùng nhìn chồng lên nhau ở góc xe (seam). Một vật ở vùng seam có thể xuất hiện
**đồng thời** trên hai camera, với hai hộp khác nhau, hai zone bán kính khác nhau (có thể là `edge` ở camera này,
`mid` ở camera kia). Hệ thống thật phải quyết định: giữ box nào, hợp nhất ra sao, hay giữ cả hai và để tầng sau xử
lý. Đây là bài toán không có trong lab một-camera của chúng ta.

## Bird's-eye view (BEV)

SVM thường hợp nhất 4 ảnh fisheye thành một ảnh nhìn từ trên xuống (bird's-eye view) để hiển thị cho tài xế hoặc
làm đầu vào cho một mô hình khác. Việc "tight" trên ảnh gốc (bài lab của bạn) và "tight" sau khi ảnh bị biến đổi
phối cảnh sang BEV là hai câu hỏi khác nhau — một box đúng trên ảnh gốc có thể méo lệch trên BEV, và ngược lại.

## Free-space và parking line

Hai lớp `free_space` (vùng xe có thể đi vào) và `parking_line` (vạch kẻ chỗ đỗ) là hai bài thực hành riêng trong
slide gốc, dùng cho tính năng đỗ xe tự động. Lab này **không thực hành** hai lớp đó — không có dataset fisheye mở
giấy phép nào có sẵn polygon free-space/parking-line hợp lệ để phát lại. Nếu Lab Coach chiếu minh hoạ WoodScape, đó
chỉ để bạn hình dung, không có bài tập đi kèm.

## Vì sao ADASIND không thực hành được cả bộ

ADASIND chỉ có **một** camera, không có track theo thời gian qua nhiều camera, không có free-space/parking-line.
Vì vậy trục `camera_id` của slide được thay bằng **zone bán kính × block thời gian** trong lab này — một cách xấp
xỉ, không phải bản thay thế đầy đủ cho bài toán 4 camera thật.

## Câu hỏi để tự kiểm sau khi đọc

Nếu một vật xuất hiện ở vùng seam của hai camera thật với hai box khác nhau, việc gán nhãn "một vật — hai box" đó
nên tính là lỗi `DUPLICATE` hay là một trường hợp hợp lệ cần một quy tắc riêng? Không có đáp án chuẩn ở đây — câu
hỏi này dùng cho câu cross-camera trong `50_exit_ticket.md`.
