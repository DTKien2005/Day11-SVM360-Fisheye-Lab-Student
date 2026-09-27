# Rubric tự đối chiếu — Day 11 SVM/360

Rubric này cho biết **bằng chứng nào người soát sẽ đọc** và thế nào là một câu trả lời có cơ sở. Đây là bản mô tả
do Lab Coach chuẩn bị để rà soát nội bộ; điểm số, trọng số, ngưỡng đạt và quyết định đánh giá chính thức chưa
được công bố trong repo. `make check` chỉ kiểm cấu trúc, không chấm đúng/sai nhãn.

| Tiêu chí / bằng chứng | Chưa vững | Đạt mục tiêu buổi | Vững |
|---|---|---|---|
| **Object trên fisheye** — `r1_craft/annotations.xml`, self-QC | Bỏ vật thuộc phạm vi, áp hình học camera thường hoặc nhầm class/rider | Box bám phần nhìn thấy, áp H=40 và sáu class của lab, tách `truncated`/`occluded` | Tự phát hiện và sửa sai trước khi khoá; giải thích được ca méo ở rìa |
| **Vùng loại trừ** — XML và self-QC | `lens_border`/`ego_body` sai hoặc vẽ ego khi không thấy | Giữ hai mask đúng theo frame; ignore có reason; không box trong vùng loại trừ | Chỉ ra được một sai mask làm lệch phép so sánh ra sao |
| **Vạch ô đỗ và free-space** — `parking/annotations.xml`, `observations.md` | Gọi vạch làn/lối xe chạy là vạch ô đỗ hoặc polygon xuyên vật cản | Vẽ đoạn chia ô bằng polyline; polygon vùng lối xe trống nhìn thấy; giải thích một vạch đã loại | Nêu ca mơ hồ và rule/evidence cần để xử lý; không suy an toàn từ ảnh tĩnh |
| **QA độc lập và rework** — lock, `qa_review.md`, `delta.md` | Xem reference trước khi tự soát hoặc không ghi thay đổi | Soát bằng rule trước reference, ghi ca cần sửa và số trước/sau | Phân biệt bất đồng hợp lý với lỗi nhãn; chỉ sửa ca có căn cứ và giữ dấu vết |
| **Đọc quality report** — `compare.md`, `local_quality.md`, confusion CSV | Lấy một số accuracy làm phán quyết đúng/sai | Đọc TP/FP/FN, micro và một class yếu; truy lại xung đột trên ảnh | Nêu giới hạn teaching reference, ngưỡng IoU, cỡ mẫu và vì sao hai phép ghép cho kết quả khác |
| **Chẩn đoán nguyên nhân** — `findings.csv`, error card | Gán mọi bất đồng cho người label/model; thiếu frame hoặc rule | Tách WHAT và giả thuyết WHY; có evidence, owner, action; dùng `E5_unresolved` khi chưa đủ dữ liệu | Đề xuất phép kiểm phân biệt lỗi guideline, data, reference và model; không khẳng định nhân quả từ một ca |
| **Sampling bốn camera** — `45_sampling_plan.csv`, `45_review_plan.md` | Chỉ chọn ảnh front hoặc cộng không đủ 200 | Đủ front/rear/left/right × normal/hard, tổng 200 của tình huống giả lập, nêu rủi ro và lý do phân bổ | Ưu tiên hard slice có căn cứ và giải thích cách thay phân bổ khi điều kiện camera đổi |
| **Gold-set plan** — `46_gold_set_plan.md` | Gọi teaching reference ADASIND là gold set cho SVM | Nêu ca cần review riêng từng camera, annotation space/calibration và cách kiểm chứng trước khi gọi gold | Có refresh trigger, xử lý seam/cross-camera và giới hạn peer agreement/report |
| **Tracking và liên camera** — `50_exit_ticket.md`, gold-set plan | Tự ghép identity hoặc gọi hai box vùng seam là lỗi trùng | Giải thích track ID, keyframe/Outside trên một camera và bằng chứng cần trước khi nối liên camera | Nêu cách timestamp, calibration và policy output ảnh hưởng quyết định ở seam |
| **Handoff** — guideline patch, escalation, decision log, exit ticket | Đề xuất chung chung, thiếu owner hoặc bằng chứng | Một rule update, một escalation có frame/ảnh/impact/owner/đề xuất; decision log truy được | Sửa rule đúng khoảng trống tìm thấy và nói được tác động tới review kế tiếp |

## Tự kiểm trước khi nộp

1. Mỗi dòng nhận định quan trọng có frame, rule hoặc bảng số liệu để người khác kiểm lại.
2. `parking_line` được phân biệt với vạch đường bằng vai trò **chia ô đỗ**, không chỉ bằng màu sơn.
3. Tập 200 frame là **bài thiết kế bốn camera giả lập**; ba frame ADASIND không đại diện bốn camera.
4. Teaching reference, nhãn bạn vẽ, model output và gold-set plan có tên gọi và vai trò riêng.
5. Nếu dùng `E0`, `E4` hay `E5`, ghi bằng chứng hoặc điều cần kiểm tiếp; không đoán để điền đủ bảng.

**Nộp:** commit/push repo bài làm ở chế độ private và gửi link qua kênh thầy/Lab Coach công bố. Không nộp notebook
Colab thay cho XML, CSV và các file giải thích trong `submission/`.
