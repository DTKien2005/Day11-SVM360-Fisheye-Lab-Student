# Kế hoạch review từ lỗi quan sát được

Từ `findings.csv` và `zone_table.md`, chọn **hai lát cắt của bài ADASIND một camera** cần review trước. Bảng này
giải thích dữ liệu thật bạn vừa làm; nó không thay cho kế hoạch bốn camera giả lập ở `45_sampling_plan.csv`.

| Lát cắt / frame | Số ca và loại lỗi | Vì sao review trước | Bằng chứng cần giữ |
|---|---|---|---|
| `B4-center` (`adasind_295948`, `270517`, `271039`) | 19 SPURIOUS, 5 IGNORE_SCOPE, 13 MISSING; lỗi lấn vào vùng `ego_body` và box Car <40px | Mật độ xe cộ dày đặc nhất, phát sinh xung đột gay gắt giữa Annotator, Reference và Model. Cần rà soát ngay để đảm bảo chuẩn nhãn không bị sai lệch hệ thống | XML bản lock `6997-BF13`, bản rework `9313-188F`, `rework/delta.md`, và ảnh overlay `qa_B_295948_overlay.png` |
| `C0 Calibration` (`adasind_019560`) | 3 ca MISSING (xe máy/xe ba bánh đỗ dưới mái che), 1 ca nhầm lẫn tách Rider/Bike | Frame hiệu chuẩn mắt nhìn nền tảng; nếu annotator hiểu sai quy tắc ở frame này sẽ lan truyền sai lệch sang toàn bộ các slice tiếp theo | `p1_calib/compare.html`, `c0_calib_missing_review.png`, và biên bản `b_review_notes.md` |

Giới hạn của kết luận từ ba frame ADASIND: 3 frame chỉ là một lát cắt cực nhỏ trong cùng một hành trình và điều kiện ánh sáng ban ngày. Không thể ngoại suy để khẳng định hiệu năng mô hình trên mọi điều kiện thời tiết (mưa, đêm, sương mù) hoặc trong các môi trường ODD khác nhau.

## Chuyển sang kế hoạch bốn camera giả lập

Cách soát độ phủ của 200 frame ở `45_sampling_plan.csv` (kể cả tránh đếm nhiều frame liền nhau trong cùng cảnh
như nhiều ca độc lập), và vì sao kế hoạch đó chỉ giúp tìm ca cần soi, chưa đo được tỷ lệ lỗi: Phân bổ 200 frame rải đều theo các chuyến xe (trips) khác nhau, thời điểm khác nhau (sáng, trưa, tối), và quy định khoảng cách tối thiểu giữa 2 frame được chọn ($\ge 5$ giây hoặc $\ge 150$ frame) để tránh hiện tượng tương quan chuỗi thời gian (temporal correlation - các frame liên tiếp giống hệt nhau). Kế hoạch này là kỹ thuật kiểm tra đại diện có chủ đích (targeted sampling) để săn lùng các ca lỗi biên (edge cases) chứ không phải lấy mẫu ngẫu nhiên độc lập (IID sampling), do đó chỉ dùng để phát hiện lỗi chứ chưa phản ánh tỷ lệ lỗi tổng thể trên toàn bộ 50.000 frame.

