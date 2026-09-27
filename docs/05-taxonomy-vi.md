# 05 — Đọc trục phân loại (taxonomy)

## Zone bán kính — bin chẩn đoán, không phải chuẩn ngành

`r/R` = khoảng cách từ tâm box tới tâm vòng kính, chia cho bán kính vòng kính của frame đó.

- `center`: r/R < 0.35
- `mid`: 0.35 ≤ r/R < 0.6
- `edge`: r/R ≥ 0.6

Hai ngưỡng 0.35 và 0.6 là **bin chẩn đoán** chọn từ phân bố pre-label của lab này, để so sánh trong buổi học. Đây
**không** phải ngưỡng chuẩn ngành cho hệ thống 360°/SVM thật.

## 6 class là tập con

ADASIND gốc và slide Ngày 11 nói tới nhiều class hơn (kể cả vật tĩnh như cone/pole/obstacle). Lab này chỉ dùng
**6 class động** (`docs/02-rules-vi.md`) — không có class tĩnh nào. Khi viết `20_guideline_patch.md` hay
`30_escalation_ticket.md`, nói rõ đây là tập con, không phải toàn bộ taxonomy gốc.

## Cột `cell` trong `findings.csv`

`cell` mô tả ba nguồn nào "thấy" cùng một vật: **L** = nhãn của bạn, **R** = teaching reference, **M** = model
(YOLO26m đóng băng).

| `cell` | Nghĩa |
|---|---|
| `LRM` | Cả ba đều thấy |
| `LR_noM` | Bạn + reference thấy, model bỏ sót |
| `LM_noR` | Bạn + model thấy, reference không có (nghi ngờ reference thiếu — E0) |
| `L_only` | Chỉ bạn thấy |
| `RM_noL` | Reference + model thấy, bạn bỏ sót |
| `R_only` | Chỉ reference có |
| `M_only` | Chỉ model có |
| `na` | Không áp dụng (dòng không so 3 nguồn, ví dụ `STRUCTURE`) |

## Cột `what` — công cụ gán tự động

`MISSING`, `SPURIOUS`, `WRONG_CLASS`, `BOX_GEOMETRY`, `DUPLICATE`, `ATTRIBUTE`, `IGNORE_SCOPE`, `STRUCTURE`. Chi
tiết luật ghép nằm trong `make compare`; bạn không tự gán cột này.

## Cột `why` — bạn tự phán đoán

- `E0_reference_defect` — **teaching reference sai**, không phải bạn sai. Đây là hạng mục **hợp pháp**: reference
  là bản nháp Lab Coach sửa tay, chưa phải "gold set" đã kiểm bởi nhiều người. Ghi rõ frame + lý do khi dùng `E0`.
- `E1_annotator_error` — bạn sai (hoặc người soát trước bạn sai).
- `E2_guideline_gap` — luật hiện tại (`docs/02`) không đủ để phân xử ca này.
- `E3_data_defect` — lỗi ở chính dữ liệu ảnh (mờ, cắt, blur đè lên vật).
- `E4_model_domain` — model sai vì lệch miền dữ liệu (model gốc huấn luyện trên ảnh phẳng, không biết `ego_body`,
  gãy ở vùng méo cạnh rìa).

## Vì sao `make cvat-quality` và `make compare` cho số khác nhau

CVAT quality report **không có ngữ nghĩa `ignore_region`** — box của bạn nằm trong vùng `ego_body` vẫn bị đếm là
`extra` trên CVAT, dù `make compare` (áp luật don't-care K13) đã loại bỏ ca đó. Khi đối chiếu hai nguồn ở P4, đây là
điểm khác biệt cần giải thích, không phải lỗi công cụ.

## Fill ratio (K12) — số đo riêng của lab

`make fill` tính diện tích polygon / diện tích box cho 4 đối tượng bạn vẽ polygon viền thấy được. Không có thuật
ngữ chuẩn "fill ratio" trong tài liệu ngành; đây là số đo tự đặt để minh hoạ box trục thẳng lỏng bao nhiêu ở vùng
rìa cong so với vùng trung tâm.
