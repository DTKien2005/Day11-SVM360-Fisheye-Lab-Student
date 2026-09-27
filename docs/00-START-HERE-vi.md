# 00 — Bắt đầu ở đây

Bản đồ 240 phút, bảy pha P0–P6. Mỗi bước có **một lệnh** và **một file ra**. Không chắc làm gì tiếp: chạy
`make status` — lệnh luôn in đúng một việc kế tiếp.

Không có `make`: mọi lệnh dưới đây dùng được bằng `python3 lab11.py <tên lệnh, bỏ "make ">`.

## P0 — Khởi động (phút 0–20)

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
4. Tự soát 9 mục (`docs/04-selfqc-checklist-vi.md`) → `make selfqc ROUND=r1_craft` → `make fill`.
5. Export → `make lock ROUND=r1_craft FILE=<file export>`. Đọc to mã khoá cho người soát mình.

Nghỉ 15' (phút 110–125).

## P3 — Vai QA reviewer (phút 125–155)

1. Nhận file đã khoá của người kế bên (nhóm, vòng A→B→C→A) hoặc cold review file của mình (solo, hoặc chưa nhận
   được file sau 5').
2. `make qa SLICE=<slice> FILE=<file nhận được> CODE=<mã khoá>` → soát overlay, chỉ dùng luật, `why` để trống.

## P4 — Vai Diagnostician (phút 155–200)

`make reference ROUND=r1_craft` → `make compare ROUND=r1_craft` → `make cvat-quality` → đối chiếu hai nguồn
(dùng `docs/07-escalation-vi.md` nếu thấy vấn đề không thuộc lỗi của mình) → `make model` → `make iou-sweep
IOU=0.3,0.5,0.7` → điền `cell/why/severity/owner/action` cho mọi dòng, trả lời từng dòng QA, viết `zone_table.md`
(`make triage` kiểm enum).

## P5 — Rework có đo (phút 200–215)

Sửa **chỉ** dòng `action=rework` mức P0/P1 → export → `make lock ROUND=rework FILE=<file>` → `make rework`.

## P6 — Tổng hợp (phút 215–240)

`make card` → viết `20_guideline_patch.md`, `30_escalation_ticket.md`, `40_decision_log.csv`, `45_review_plan.md`,
`50_exit_ticket.md`, `reflection.md` → `make check` → commit + push.

Time-box: chậm 5' ở pha nào thì xem thứ tự cắt ở `docs/08-degrade-vi.md`. Không bao giờ bỏ: lock, reference, ≥1
dòng mỗi vai, `delta.md`, `make check`.
