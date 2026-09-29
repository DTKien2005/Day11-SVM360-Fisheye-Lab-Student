# Tiếp nhận P2 cho QA vai B

- Nguồn: [commit d7862e5](https://github.com/DTKien2005/Day11-SVM360-Fisheye-Lab-Student/commit/d7862e5cc9611907fd907d43287bb36c2c8f2111).
- Nhận lúc: 2026-09-29T12:40:15.681741+07:00.
- Slice thực tế: B4-center, đã được Nghĩa xác nhận.
- SHA-256 XML khớp lock, mã 6997-BF13.
- Có đủ 3 ảnh 1080×1920; 27 box và 8 polygon.
- Mã L theo report.scoped của tool QA (box cao từ 40 px), bắt đầu lại trên từng ảnh.

## Dấu hiệu kỹ thuật cần reviewer kiểm trên ảnh

1. adasind_295948.jpg: XML box #1 Car tại (451.92,934.43)–(467.43,961.42) cao 26.99 px, dưới ngưỡng R01. Box này không có L trong overlay chuẩn; overlay bổ sung ký hiệu XML#1 để reviewer nhìn thấy.
2. Giá trị native occluded=1 khác custom occluded=false tại adasind_271039.jpg L7/L8/L9; adasind_295948.jpg L4/L5/L7 và XML box #1. Parser lab đọc custom attribute. Cần xác nhận trạng thái nhìn thấy theo R05, chưa tự sửa nhãn.
3. adasind_271039.jpg nằm trong danh sách ngoại lệ không có ego_body của repo; chỉ có hai lens_border không tự động là lỗi thiếu ego.

Đây là biên bản kiểm kỹ thuật lúc tiếp nhận. Sau đó Nghĩa đã xem cả ba ảnh và xác nhận bốn nhận xét ở frame 295948; xem `qa_review.md` và bốn dòng `r2_qa` trong `findings.csv` để biết trạng thái QA hiện tại. Chưa mở reference/model/compare của slice chính.
