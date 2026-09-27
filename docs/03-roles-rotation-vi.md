# 03 — Ba vai và vòng quay

Một nhiệm vụ duy nhất — audit một slice 3 frame — qua ba vai. Mọi vai ghi vào **một** bảng `submission/findings.csv`.

## Ba vai

| Vai | Việc | Xong khi |
|---|---|---|
| **Annotator** (P2) | Gán nhãn slice của mình: box, `ego_body`, attribute, polygon K12 | `make lock ROUND=r1_craft` xong |
| **QA reviewer** (P3) | Soát nhãn đã khoá của người khác **chỉ bằng luật**, chưa biết reference | `make qa` ra `qa_review.md` |
| **Diagnostician** (P4) | Mở reference + quality report + model, phân loại mọi khác biệt theo WHAT × WHY × owner | `zone_table.md` + `findings.csv` ≥12 dòng |

## Vòng quay (làm nhóm 2–3 người)

Vòng cố định **A → B → C → A**: nhận slice đã khoá của người **kế bên**, không phải người mình chọn. Vai xoay theo
từng pha — mỗi người tự làm cả ba vai trên slice của chính mình (Annotator), rồi soát slice người khác (QA), rồi
chẩn đoán slice của chính mình (Diagnostician).

## Làm một mình (solo)

Không có ai để đổi bài ở P3. Thay bằng **cold review**: đợi ≥5 phút (để quên chi tiết vừa vẽ), rồi tự soát lại
chính slice của mình bằng `make qa SLICE=<slice> FILE=<file mình vừa khoá> CODE=<mã khoá>`, vẫn chỉ dùng luật.

## Chờ quá 5 phút mà chưa nhận được file (nhóm)

Coi như solo: chuyển sang cold review chính mình, không chờ thêm. `mode.json` ghi lại việc này, không tính là lỗi.
