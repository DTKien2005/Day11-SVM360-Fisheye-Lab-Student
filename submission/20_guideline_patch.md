# Guideline patch

- **Rule mới đề xuất:** R10 — Xử lý đối tượng cắt đôi hoặc xuất hiện đồng thời tại vùng giáp ranh ghép mí 4 camera (SVM Stitching Seam Cross-Camera Object).
  - *Quy định chi tiết:* Khi một phương tiện hoặc người đi bộ nằm tại đường ghép mí giữa hai camera liền kề (Front-Left, Front-Right, Rear-Left, Rear-Right), mỗi camera gán nhãn phần nhìn thấy độc lập trên ảnh fisheye gốc của mình kèm thuộc tính `truncated=true` nếu bị cắt bởi mép khung hình. Không tự ý gộp hai box hoặc xóa bỏ box ở một camera nếu chưa có tầng tracking/fusion 3D đồng bộ timestamp.
- **Áp dụng cho:** Tất cả 6 class động (`Car`, `Truck`, `Bus`, `Motorcycle`, `Bicycle`, `Pedestrian`) và vùng giáp ranh seam giữa 4 camera trong hệ thống SVM 360.
- **Vì sao luật hiện tại (`docs/02-rules-vi.md`) không đủ:** Quy tắc hiện tại `v1.0.0` chỉ thiết kế cho camera fisheye đơn lẻ (single camera domain), hoàn toàn thiếu chỉ dẫn xử lý khi đối tượng bị chia cắt quang học hoặc xuất hiện đồng thời ở hai góc nhìn khác nhau tại seam, gây tranh cãi và bất đồng quan điểm giữa annotator và QA reviewer (dễ bị nhầm lẫn thành lỗi duplicate box).
- **`rules_version` mới:** `v1.1.0`
- **Hiệu lực từ:** Vòng kiểm thử và gán nhãn hệ thống 4 camera Surround View Monitoring tiếp theo (Sau vòng P5 rework).

