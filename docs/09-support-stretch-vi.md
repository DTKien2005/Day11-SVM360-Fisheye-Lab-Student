# 09 — Hỗ trợ (support) và làm thêm (stretch)

## Cần hỗ trợ ở P2 (frame 2 cũng import sẵn)

Nếu cảm thấy quá tải với việc vẽ trắng cả frame 2 và 3: `make cvat SLICE=<slice> SUPPORT=1` import sẵn thêm nửa
box cho **frame 2** (giống frame 1), chỉ còn frame 3 vẽ trắng hoàn toàn. Đây không phải "làm ít hơn" — mọi mục
tiêu học tập (O1–O6) vẫn áp dụng, chỉ giảm khối lượng vẽ tay.

## Stretch — chỉ làm nếu còn thời gian ở P6

Thư mục `submission/stretch/` để **rỗng** nếu không làm phần này — không bị trừ gì. Nếu làm:

- **`sampling_plan.csv`** — bảng lấy mẫu đầy đủ (đối chiếu slide p.49 deliverable 2): mở rộng bảng rút gọn ở
  `submission/45_review_plan.md` thành kế hoạch lấy mẫu theo mọi zone × block, không chỉ lát cắt khó.
- **`gold_set_matrix.md`** — ma trận đề xuất frame nào nên vào một "gold set" thật (nhiều người kiểm chứng) nếu lớp
  làm tiếp ở quy mô lớn hơn, và vì sao (đối chiếu slide p.49 deliverable 3).
- **Tự chạy YOLO26m** — tuỳ chọn, không bắt buộc. Nếu bạn có sẵn môi trường Ultralytics (ngoài repo lab, vì repo
  Student không import `ultralytics`), có thể tự chạy lại pre-label trên slice của mình để so với
  `model-yolo26m.xml` đã đóng băng. **Không commit** file trọng số `.pt`/`.onnx` nào vào repo — `make check` sẽ
  báo lỗi nếu thấy.

## Không có trong bài lab này

- **WoodScape** không nằm trong lane học viên (giấy phép Valeo không cho phát lại). Nếu Lab Coach chiếu minh hoạ
  free-space/parking-line/curb, đó chỉ là hình ảnh trình chiếu, không có trong repo và không có bài tập nào dùng
  tới. Về CVAT: quality report chạy trên bản self-hosted của lớp, không phải một tính năng chỉ có ở bản trả phí.
