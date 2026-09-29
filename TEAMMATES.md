# Thành viên và phân vai — Day11 SVM 360 Fisheye

## 1. Thông tin nhóm

- Khóa/lớp: VinUni AI20k - K4
- Tên nhóm: `K4-DAY11-Lab11` (SVM360-AI-Group)
- Repo Public: [https://github.com/DTKien2005/K4-DAY11-Lab11](https://github.com/DTKien2005/K4-DAY11-Lab11)
- Máy giữ hồ sơ chính / người quản lý: Đỗ Trung Kiên (Vai C - Lead & Diagnostician)
- Slice chung lấy từ mode.json: `B4-center`
- Tên định danh vai A dùng cho --self: `tin`
- Kênh trao đổi nội bộ: Discord / Telegram Lab Day 11 VinUni
- Đại diện nộp (vai C): Đỗ Trung Kiên, MSSV: `2A202602283`
- Commit chốt bài: [Commit trên main](https://github.com/DTKien2005/K4-DAY11-Lab11/commits/main)

## 2. Ba vai chính

| Vai | Họ và tên | MSSV | Tên định danh trong mode | Trách nhiệm | Bằng chứng đóng góp |
|---|---|---|---|---|---|
| A · Gán nhãn | Nguyễn Trí Tín | 2A202602275 | `tin` | Parking/C0/slice, self-QC, lock, rework | [parking/annotations.xml](submission/parking/annotations.xml), [p1_calib/lock.txt](submission/p1_calib/lock.txt) (`78D7-86D3`), [r1_craft/lock.txt](submission/r1_craft/lock.txt) (`6997-BF13`), [r1_craft/selfqc.md](submission/r1_craft/selfqc.md), [rework/lock2.txt](submission/rework/lock2.txt) (`9313-188F`), [rework/delta.md](submission/rework/delta.md), commit [`ac57504`](https://github.com/DTKien2005/K4-DAY11-Lab11/commit/ac57504969f37fe41f1f2500c2cb3f3007a0b171) trên branch `p0-parking-export` |
| B · QA độc lập | Võ Trọng Nghĩa | 2A202602072 | `nghia` | Review trước reference, finding QA, kiểm lại ca sửa | [p1_calib/b_review_notes.md](submission/p1_calib/b_review_notes.md), [r2_qa/qa_intake.md](submission/r2_qa/qa_intake.md), [r2_qa/qa_review.md](submission/r2_qa/qa_review.md), [r2_qa/qa_overlay.html](submission/r2_qa/qa_overlay.html), 4 finding `r2_qa` trong [findings.csv](submission/findings.csv), ảnh overlay thật [screenshots/qa_B_295948_overlay.png](submission/screenshots/qa_B_295948_overlay.png), commit [`0503c78`](https://github.com/DTKien2005/K4-DAY11-Lab11/commit/0503c786afa0bd493ca25157b62b31382648a3af) trên branch `nghia-qa-notes` |
| C · Chẩn đoán & điều phối | Đỗ Trung Kiên | 2A202602283 | `kien` | Báo cáo, phân xử, kế hoạch, tích hợp, check và nộp | [00_setup/mode.json](submission/00_setup/mode.json), [r1_craft/compare.md](submission/r1_craft/compare.md), [r3_diag/local_quality.md](submission/r3_diag/local_quality.md), [r3_diag/model_compare.md](submission/r3_diag/model_compare.md), [r3_diag/zone_table.md](submission/r3_diag/zone_table.md), [10_error_card.md](submission/10_error_card.md), [20_guideline_patch.md](submission/20_guideline_patch.md), [30_escalation_ticket.md](submission/30_escalation_ticket.md), [40_decision_log.csv](submission/40_decision_log.csv), [45_sampling_plan.csv](submission/45_sampling_plan.csv), [46_gold_set_plan.md](submission/46_gold_set_plan.md), [50_exit_ticket.md](submission/50_exit_ticket.md), [submission/manifest.json](submission/manifest.json) |

Bảng này xác định vai của nhóm. Vòng QA tự sinh trong team.json thuộc quy trình nhiều hồ sơ của CLI; nhóm dùng một slice chung và quy trình A → B → C đã nêu trong hướng dẫn.

## 3. Bàn giao theo pha

| Mốc | Người giao → nhận | File / commit / mã khóa | Người nhận đã kiểm gì? | Trạng thái / vướng mắc |
|---|---|---|---|---|
| P0 · Chốt môi trường và vai | C → A, B | `00_setup/mode.json`, `team.json`, `sensor_context.md` | A và B xác nhận Docker CVAT local hoạt động tốt; thống nhất vai A (Tín - Annotator), B (Nghĩa - QA), C (Kiên - Diag & Lead); chọn slice `B4-center`. | Hoàn thành đúng hạn, không vướng mắc. |
| P2 · Khóa bản đầu | A → B, C | `r1_craft/annotations.xml`, `lock.txt` (`6997-BF13`), `selfqc.md`, commit `d7862e5` | B và C kiểm tra hash XML khớp lock `6997-BF13`; đủ 3 ảnh 1080×1920, 27 box, 8 polygon; 9 mục self-QC đã soát đạt chuẩn. | Hoàn thành, B tiếp nhận làm QA mù độc lập theo `qa_intake.md`. |
| P3 · Chốt QA mù | B → C, A | `r2_qa/qa_review.md`, 4 dòng finding QA trong `findings.csv`, ảnh `qa_B_295948_overlay.png`, commit `0503c78` | A và C kiểm tra 4 điểm nhận xét frame 295948 (L4 Bike, L5 Pedestrian, L7 Truck che khuất và box #1 Car cao 26.99px dưới H=40); đối chiếu với ảnh overlay thật. | Hoàn thành, chuyển toàn bộ dữ kiện cho C chẩn đoán. |
| P4 · Quyết định sửa | C → A, B | `r3_diag/local_quality.md`, `model_compare.md`, 21 dòng `r3_diag` trong `findings.csv`, `40_decision_log.csv`, `10_error_card.md` | A và B kiểm tra phân tích nguyên nhân lỗi E0–E5 đối chiếu teaching reference và YOLO model; thống nhất 4 quyết định sửa nhãn và 1 ca leo thang. | Hoàn thành, bàn giao yêu cầu sửa chữa cho A. |
| P5 · Kiểm bản sửa | A → B → C | `rework/annotations-v2.xml`, `lock2.txt` (`9313-188F`), `rework/delta.md`, 3 ảnh before/after, commit `f7651fe` | B và C kiểm tra hash lock2 `9313-188F`; đối chiếu bảng delta (26 box, giảm 1 box dưới H=40, cập nhật 3 occluded=true, F1 tăng từ 0.771 lên 0.792); B xác nhận đạt. | Hoàn thành, chuyển C tổng hợp P6. |
| P6 · Chốt nộp | A, B → C | `manifest.json`, `20_guideline_patch.md`, `30_escalation_ticket.md`, `45_sampling_plan.csv`, `46_gold_set_plan.md`, `50_exit_ticket.md` | C chạy `py lab11.py check` xác nhận đạt `✓ Hồ sơ hình thức đầy đủ`, exit code 0, 0 failed gates trong manifest; repo Public sẵn sàng nộp. | Hoàn thành nghiệm thu toàn diện. |

## 4. Bất đồng và phối hợp

- **Một ca đã phân xử:** Frame `adasind_295948.jpg`, đối tượng XML box #1 Car tại tọa độ (451.92, 934.43)–(467.43, 961.42), chiều cao 26.99 px. Ý kiến A: Gán nhãn vì nhìn thấy ô tô thật phía xa. Ý kiến B: Phát hiện box cao < 40 px, vi phạm quy tắc R01 (ngưỡng tối thiểu của bài toán SVM 360). Bằng chứng: [screenshots/qa_B_295948_overlay.png](submission/screenshots/qa_B_295948_overlay.png). Quyết định của C: Đồng thuận với B, yêu cầu A xóa bỏ box này trong bản rework v2 để đảm bảo tính nhất quán của dataset ([40_decision_log.csv](submission/40_decision_log.csv), entry DEC-01).
- **Ca còn mở:** Frame `adasind_295948.jpg`, cụm đối tượng mép trái (x ≤ 145 px) giáp ranh vùng `lens_border` và `ego_body` theo quy tắc R08/R09. Người theo dõi: Đỗ Trung Kiên (Lead) & Data Ops Team. Phép kiểm tiếp theo: Đối chiếu phép chiếu 3D camera và seam lân cận từ camera gương trái (`left_mirror`) để phân định rõ ranh giới thân xe và vật thể ngoài đường. Chi tiết tại [30_escalation_ticket.md](submission/30_escalation_ticket.md).
- **Đóng góp của A/B/C vào kế hoạch và exit ticket:**
  - A (Tín): Đóng góp dữ liệu thực tế về khó khăn phân biệt vạch đỗ xe mờ/lối xe chạy và ảnh hưởng của méo fisheye vào câu 1 và câu 3 của [50_exit_ticket.md](submission/50_exit_ticket.md).
  - B (Nghĩa): Đóng góp kinh nghiệm QA độc lập, đề xuất phân bổ tăng tỷ trọng frame `hard` cho góc `rear` và `left` trong [45_sampling_plan.csv](submission/45_sampling_plan.csv), đóng góp câu 2 về quy trình blind review trong [50_exit_ticket.md](submission/50_exit_ticket.md).
  - C (Kiên): Thiết kế hoàn chỉnh bảng phân bổ 200 frame [45_sampling_plan.csv](submission/45_sampling_plan.csv), chính sách kiểm soát seam 4 camera và chu kỳ làm tươi trong [46_gold_set_plan.md](submission/46_gold_set_plan.md), tổng hợp và chốt toàn bộ nội dung [50_exit_ticket.md](submission/50_exit_ticket.md).
- **Thay đổi phân công nếu có:** Không có thay đổi; ba thành viên hoàn thành đúng và đủ nhiệm vụ theo phân công ban đầu từ P0 đến P6.

## 5. Xác nhận trước khi nộp

- [x] A xác nhận nhãn và export đúng phiên bản: Nguyễn Trí Tín / [r1_craft/lock.txt](submission/r1_craft/lock.txt) (`6997-BF13`), [rework/lock2.txt](submission/rework/lock2.txt) (`9313-188F`), [rework/delta.md](submission/rework/delta.md).
- [x] B xác nhận đã QA độc lập trước reference và kiểm lại ca sửa: Võ Trọng Nghĩa / [r2_qa/qa_review.md](submission/r2_qa/qa_review.md), [r2_qa/qa_intake.md](submission/r2_qa/qa_intake.md), [screenshots/qa_B_295948_overlay.png](submission/screenshots/qa_B_295948_overlay.png).
- [x] C xác nhận báo cáo đúng bản khóa, các file đầy đủ và check exit 0: Đỗ Trung Kiên / [r3_diag/local_quality.md](submission/r3_diag/local_quality.md), [findings.csv](submission/findings.csv), [40_decision_log.csv](submission/40_decision_log.csv), [submission/manifest.json](submission/manifest.json).
- [x] manifest.json tại commit chốt có failed_gates rỗng.
- [x] Repo nhóm Public, ảnh và các bằng chứng mở được: [https://github.com/DTKien2005/K4-DAY11-Lab11](https://github.com/DTKien2005/K4-DAY11-Lab11).
- [x] C đã push và gửi link repo nhóm + commit qua kênh lớp công bố.
