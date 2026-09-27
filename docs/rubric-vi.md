# Rubric — mô tả mức, không có trọng số

Đây là rubric **mô tả**, dùng để bạn tự đối chiếu trước khi nộp. Điểm số, trọng số, và cổng đạt/trượt **không** nằm
trong repo này — thuộc autograder riêng của chương trình.

| Tiêu chí | Chưa vững | Đạt mục tiêu buổi | Vững |
|---|---|---|---|
| **Geometry** (O1) | Box "nắn thẳng" vật cong ở rìa; thiếu vật gần trong `ego_body`/`center` | Box bám đúng phần nhìn thấy trên ảnh gốc; `truncated` đúng theo vòng kính/khung | Nhất quán qua cả 3 frame; tự bắt và sửa lỗi hình học của mình trước khi khoá |
| **Class & attribute** (O1) | Còn nhầm ThreeWheeler/Bus/Truck; sai luật rider; `occluded`/`truncated` lẫn nhau | Đúng bảng 6 class và luật rider; hai attribute tách bạch | Không lệch giữa các đối tượng cùng loại trong slice; ghi rõ ca mơ hồ thay vì đoán |
| **Soát độc lập trước khi thấy reference** (O2) | Đoán trước `why`/reference khi chưa mở; soát qua loa | Soát chéo chỉ bằng luật (`rule_id`), `why` để trống đúng như thiết kế | Bắt được ca thật (không chỉ đồng thuận với người khoá) trước khi có reference |
| **Đọc quality report CVAT** (O3) | Không đối chiếu `cvat_quality.md` với `compare.md` | Nói được vài số của report (valid/missing/extra) | Giải thích được vì sao hai nguồn lệch số (ngữ nghĩa ignore, xem `docs/05`) |
| **Phân loại WHAT × WHY × owner** (O4) | Không dùng `E0`; mọi khác biệt gán `E1` | Có phân loại cho phần lớn dòng, dùng `E0` khi có bằng chứng | Phân biệt rõ `E0`–`E4`; mỗi `E0`/`E4` có frame + lý do cụ thể |
| **Zone bán kính** (O5) | Không có `zone_table.md`, hoặc không tách center/mid/edge | `zone_table.md` có đủ 3 zone với n cụ thể | Nói được zone nào model gãy nhiều nhất và giả thuyết vì sao (méo, thiếu `ego_body`) |
| **Hệ quả** (O6) | Error card/guideline patch/escalation ticket còn sơ sài, không có bằng chứng cụ thể | Đủ 4 hạng mục (`10`, `20`, `30`, decision log), mỗi mục có evidence | Guideline patch giải quyết đúng khoảng trống đã tìm thấy; escalation đúng 5 trường, đúng owner |
| **Sampling/gold plan** (O7) | `45_review_plan.md` bỏ trống hoặc chung chung | Có bảng rút gọn: lát cắt khó nào cần review trước, vì sao | Làm thêm `stretch/` với lý luận mở rộng hợp lý |

## Bằng chứng nằm ở đâu

- Khoá và so sánh: `p1_calib/`, `r1_craft/lock.txt`, `compare.md/html`.
- Soát chéo: `r2_qa/qa_review.md`.
- Chẩn đoán: `r3_diag/cvat_quality.md`, `model_compare.*`, `zone_table.md`, cột `why`/`severity`/`owner` của
  `findings.csv`.
- Rework có đo: `rework/delta.md`.
- Hệ quả: `10_error_card.md`, `20_guideline_patch.md`, `30_escalation_ticket.md`, `40_decision_log.csv`.

## Không làm giảm đánh giá

- Dùng `E0_reference_defect` khi có bằng chứng — teaching reference **có** lỗi đã biết, ghi ra là đúng, không phải
  "cãi lại" reference.
- Không làm phần `stretch/`.
