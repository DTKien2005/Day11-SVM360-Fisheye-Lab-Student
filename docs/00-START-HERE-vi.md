# 00 — Bắt đầu ở đây

Bài Day 11 dùng repo này cho **thực hành trong phần giảng** và **240 phút lab CVAT** P0–P6 tiếp theo. Cả hai phần đều thuộc
bài lõi: gán nhãn object trên fisheye, vạch ô đỗ/free-space trên ảnh bãi đỗ, review và sửa nhãn, phân tích lỗi model,
rồi lập kế hoạch sampling/gold set cho bốn camera SVM. Ảnh ADASIND là **một camera**, ảnh bãi đỗ là **camera thường**;
tình huống bốn camera là **giả lập trên slide**, không có pixel bốn camera trong repo. Không chắc làm gì tiếp: chạy
`make status` để nhận gợi ý bước tiếp theo.

Mở [rubric tự đối chiếu](rubric-vi.md) trước khi làm và [notebook Colab](../notebooks/README.md) nếu cần bảng tính phụ
cho kế hoạch 200 frame. Notebook không thay CVAT, không cần để nộp.

## Trong phần giảng — vạch ô đỗ và kế hoạch bốn camera

1. Chuẩn bị repo và CVAT theo P0 bên dưới trước hoạt động thực hành; nếu đã làm P0 trong giờ giảng thì không cần làm lại. Làm [micro-practice bãi đỗ](11-parking-lines-vi.md): `make parking` → vẽ
   `parking_line`/`free_space` trên ảnh core → export → `make parking FILE=<zip>`; điền `parking/observations.md`.
2. Ở hoạt động sampling của slide, phác thảo `45_sampling_plan.csv` cho front/rear/left/right, normal/hard, tổng
   **200 frame** từ tình huống **50.000 frame giả lập**. Phác thảo `46_gold_set_plan.md`; sau P4 dùng lỗi đã quan
   sát để sửa lý do và hoàn tất hai file. Không gọi teaching reference ADASIND là gold set.

Hai ảnh bãi đỗ đã đi kèm repo; không cần tìm ảnh đường phố hay tải dataset khác.

Không có `make`: mọi lệnh dưới đây dùng được bằng `python3 lab11.py <tên lệnh, bỏ "make ">`.

## P0 — Khởi động (phút 0–20 của lab; có thể chuẩn bị trong giờ giảng)

| Lệnh | File ra |
|---|---|
| `make doctor` | `submission/00_setup/doctor.txt` |
| `make mode MEMBERS="an,binh,chi"` (một tên nếu solo) | `submission/00_setup/mode.json` (+ `team.json` nếu >1 người) |
| Điền tay `submission/00_setup/sensor_context.md` | — |

CVAT chưa lên: xem `docs/01-guide-cvat-vi.md` mục khởi động lại stack Day 2.

## P1 — Hiệu chuẩn + clinic (phút 20–55)

1. `make cvat SLICE=C0` → vẽ frame hiệu chuẩn `C0` theo `docs/01`, export.
2. `make lock ROUND=calib FILE=<file export>` → `make reference ROUND=calib` → `make compare ROUND=calib`.
3. Xem quality report của pre-label do Lab Coach chiếu (hoặc `assets/worked/prelabel-quality.png`). Ghi 3 dòng đầu
   vào `submission/findings.csv`.
4. Clinic 12' trên 6 card ở `docs/06-misconceptions-vi.md`. Vắng clinic: `make worked`.

## P2 — Vai Annotator (phút 55–110)

1. `make cvat SLICE=<slice của mình>` → tạo task, import sẵn nửa box frame 1 + `lens_border`.
2. Soát `lens_border`, vẽ `ego_body`, vẽ box (đọc `docs/02-rules-vi.md`), gán attribute.
3. Vẽ polygon K12 cho 4 đối tượng công cụ liệt kê (đọc `docs/05-taxonomy-vi.md` mục fill ratio). Chậm thì bỏ bước
   này trước (`docs/08-degrade-vi.md`).
4. **Save rồi export bản nháp CVAT for images 1.1**. `make draft FILE=<file export nháp>` lưu XML vào `exports/r1-draft.xml`
   và báo lỗi nếu thiếu frame bắt buộc của slice.
   Chạy `make fill` (nếu làm K12) và `make selfqc ROUND=r1_craft`; xem lỗi tự động, tick 9 mục thủ công.
5. Sửa trong CVAT theo self-QC → **Save và export bản cuối** → `make lock ROUND=r1_craft FILE=<file export cuối>`.
   Đọc to mã khoá cho người soát mình. Bản nháp chưa khoá không được nộp thay bản cuối.

Nghỉ 15' (phút 110–125).

## P3 — Vai QA reviewer (phút 125–155)

1. Nhận file đã khoá của người kế bên (nhóm, vòng A→B→C→A) hoặc cold review file của mình (solo, hoặc chưa nhận
   được file sau 5').
2. `make qa SLICE=<slice> FILE=<file nhận được> CODE=<mã khoá>` → soát overlay, chỉ dùng luật, `why` để trống.

## P4 — Vai Diagnostician (phút 155–200)

`make reference ROUND=r1_craft` → `make compare ROUND=r1_craft` → `make local-quality` → đối chiếu báo cáo xung đột và chỉ số
(dùng `docs/07-escalation-vi.md` nếu thấy vấn đề không thuộc lỗi của mình) → `make model` → `make iou-sweep
IOU=0.3,0.5,0.7` → điền `cell/why/severity/owner/action` cho mọi dòng, trả lời từng dòng QA, viết `zone_table.md`
(`make triage` kiểm enum).

`make local-quality` chạy offline trên export đã khóa và teaching reference; không cần CVAT Premium hay đăng nhập API.
Đọc `r3_diag/local_quality.md`, ma trận nhầm lớp và CSV xung đột. Đây là tín hiệu chẩn đoán trên vài frame của
một camera, không phải điểm đạt hay chứng nhận gold set. `make cvat-quality` chỉ là thử nghiệm tùy chọn nếu môi
trường có CVAT Quality Control. `why=E5_unresolved` hợp lệ khi chưa đủ bằng chứng; ghi rõ điều cần kiểm thêm.

## P5 — Rework có đo (phút 200–215)

Sửa **chỉ** dòng `action=rework` mức P0/P1 → export → `make lock ROUND=rework FILE=<file>` → `make rework`.

## P6 — Tổng hợp (phút 215–240)

`make card` → hoàn tất `20_guideline_patch.md`, `30_escalation_ticket.md`, `40_decision_log.csv`,
`45_review_plan.md`, **`45_sampling_plan.csv`**, **`46_gold_set_plan.md`**, `50_exit_ticket.md`, `reflection.md` →
`make check` → commit + push repo **private** của bạn. Gửi link repo theo kênh nộp bài mà thầy/Lab Coach công bố.
`make check` chỉ kiểm cấu trúc và số lượng bằng chứng; người soát dùng rubric để xem nhãn và lập luận có đúng không.

Các mốc P0–P6 là **ngân sách dự kiến**, chưa được xác nhận bằng dry-run solo và nhóm. Lab Coach ghi thời gian thực
vào phiếu pilot của giảng viên trước khi phát lớp; đặc biệt kiểm P2 và P6. Hai hiện vật sampling/gold set được phác
thảo trong giờ giảng và hoàn thiện sau P4, không chờ tới phút 215 mới bắt đầu.

Time-box: chậm 5' ở pha nào thì xem thứ tự cắt ở `docs/08-degrade-vi.md`. Không bao giờ bỏ: lock, reference, ≥1
dòng mỗi vai, `delta.md`, `make check`.
