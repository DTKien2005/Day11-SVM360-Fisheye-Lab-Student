# QA review · B4-center
Reviewer: Võ Trọng Nghĩa (nghia), vai B.
Chủ nhãn bàn giao: Nguyễn Trí Tín (tin), vai A.
Nguồn: commit d7862e5cc9611907fd907d43287bb36c2c8f2111, nhánh p0-parking-export.
Mã khóa đã kiểm: 6997-BF13.
SHA-256: 6997bf13e8daac9ae1cbf02fa422682f9eb3b960cc2812c21d587eaa9293e7f0.
Thời điểm nhận: 2026-09-29T12:40:15.681741+07:00.
Slice: B4-center; Nghĩa đã xác nhận chuyển từ bảng phân công cũ B4-edge sang bản B4-center bàn giao.
Số điểm cần A xử lý theo nhận xét của reviewer: 4 ở ảnh 295948. Các ca chưa rõ ở ảnh 270517 và 271039 được ghi riêng, chưa tính là lỗi xác nhận.
Trạng thái: QA mù vai B đã chốt với 4 finding ở ảnh 295948 và các ca chưa rõ được ghi riêng cho 270517/271039. Ảnh chụp bằng chứng đã lưu. Chưa mở reference/model/compare của slice chính.

## Tiến độ
- [x] adasind_270517.jpg — đã nhận nhận xét trực tiếp của Nghĩa
- [x] adasind_271039.jpg — đã nhận nhận xét, còn occluded từng đối tượng và biên ignore chưa đủ căn cứ để chốt
- [x] adasind_295948.jpg — đã nhận nhận xét trực tiếp của Nghĩa

## adasind_270517.jpg — nhận xét của Nghĩa

- **R06–R09:** `lens_border` phía dưới nhìn chung bám biên tròn; `ego_body` bên trái bám phần thân/cụm camera nhìn thấy, chưa thấy lấn đáng kể vào mặt đường hợp lệ. Nếu mở rộng review hình học, rà lại độ bám chính xác của các vùng ignore.
- **L1 Bike — R02/R05:** class và box phù hợp; xe bị phương tiện phía trước che một phần. `occluded=true`, `truncated=false` trong XML khớp nhận xét của Nghĩa.
- **L2 Pedestrian — R02/R03:** box tương đối đúng phần người đi bộ; chưa thấy người đang điều khiển xe. `occluded=false` trong XML khớp nhận xét.
- **L3 Bike — R02/R05:** class phù hợp; vật bị mép phải cắt mạnh. `truncated=true` trong XML khớp nhận xét.
- **L4 ThreeWheeler — R02:** class và box tương đối sát phương tiện; chưa thấy bị che hoặc cắt biên đáng kể.
- **L5 Car — R02:** class và box bao phần xe nhìn thấy tương đối phù hợp.
- **L6 Car — R02:** class và box xe phía xa phù hợp; chưa thấy bị cắt biên hoặc che đáng kể.
- **L7 ThreeWheeler — R02:** class và box bao phần phương tiện cùng người lái bên trong tương đối phù hợp theo nhận xét của Nghĩa.
- **R01:** chưa thấy đối tượng hợp lệ cao ≥40 px nào chắc chắn bị bỏ sót. Vật tối phía sau L2, giữa L2 và L7, cần A/B xem kỹ xem là phương tiện độc lập và đạt ngưỡng hay không.

Nhãn L1–L7 nhìn chung được Nghĩa chấp nhận trên ảnh này. Vật tối phía sau L2 là **ca chưa rõ**, chưa được ghi là lỗi thiếu box. Không sửa nhãn của A từ nhận xét này.

## adasind_271039.jpg — nhận xét của Nghĩa

- **Class và phạm vi:** các box chính thuộc `Car`, `ThreeWheeler`, `Pedestrian` nhìn chung đúng nhóm. Chưa thấy rõ vật hợp lệ cao ≥40 px nào chắc chắn bị bỏ sót. Cần rà các phương tiện nhỏ ở nền trái/trung tâm vì nhiều box chồng nhau.
- **L7, L8, L9 — R05:** XML có `occluded=false` ở thuộc tính dùng cho báo cáo, trong khi cờ `occluded` gốc của shape bằng `1`. L7/L8 là `Pedestrian`; L9 là `ThreeWheeler`. Nghĩa yêu cầu kiểm theo ảnh: chỉ đánh `occluded=true` nếu **chính đối tượng đó** bị vật khác che phần nhìn thấy; người còn nhìn rõ phần lớn cơ thể thì `false`. Phần làm mờ/anonymization không được tính là vật thể che. Nghĩa chưa chốt riêng giá trị cuối cho từng L7–L9.
- **L10 Pedestrian — R05:** người phía phải thấy phần lớn cơ thể; Nghĩa chưa thấy lý do đặt `occluded=true`. Thuộc tính đang lưu là `occluded=false`, phù hợp nhận xét hiện tại.
- **L11 Car — R02/R05:** đây là xe đỏ lớn phía phải theo vị trí box. Nghĩa chưa thấy vật khác che đáng kể; `occluded=false` đang lưu phù hợp nhận xét. Mép dưới box có vẻ hơi rộng xuống mặt đường; cần kiểm sát lại biên theo ảnh gốc, chưa kết luận sai hình học.
- **R08/R09:** vùng `lens_border` ở mép trái chỉ nên phủ phần tối ngoài vòng kính, không lấn đường hoặc đối tượng. Nghĩa chưa xem đủ toàn bộ biên dưới để xác nhận vùng ignore của ảnh. XML ảnh này chỉ có hai polygon `lens_border`, không có `ego_body`; repo liệt kê `271039` là frame ngoại lệ không thấy thân xe. Kiểm ảnh đầy đủ nếu cần chốt độ bám biên.

Kết luận hiện tại của Nghĩa: ưu tiên kiểm thuộc tính `occluded` của L7–L9, mép box L11, các vật nhỏ ở nền và biên ignore. Các nhãn còn lại chưa thấy lỗi class rõ ràng. Đây là nhận xét đang mở, chưa phải QA chốt hay yêu cầu sửa xác định cho từng đối tượng.

## adasind_295948.jpg — nhận xét của Nghĩa

- **L4 Bike — R05:** người/xe bị cụm thân hoặc xe tiền cảnh bên trái che một phần. Nghĩa xác nhận `occluded=true`; XML đang lưu custom `occluded=false` dù cờ shape gốc là `1`. Rà và thống nhất thuộc tính trong bản A sửa. Nghĩa chỉ nói phần khuất không chủ yếu do vòng kính; không chốt lại `truncated` ở đây vì hai thuộc tính độc lập.
- **L5 Pedestrian — R05:** chỉ thấy một phần cơ thể; phần dưới bị vật/phương tiện phía trước che. Nghĩa xác nhận `occluded=true`; custom trong XML đang là `false`.
- **L7 Truck — R05:** ở phía sau vật khác, phần thấy được nhỏ. Nghĩa xác nhận `occluded=true`; custom trong XML đang là `false`.
- **XML box #1 Car — R01:** người soát xác nhận đây là đối tượng thật nhưng box cao khoảng 27 px (`26.99` theo XML), dưới ngưỡng `H=40` của guideline. Đây là box nhỏ không thuộc phạm vi gán bắt buộc; Nghĩa đề nghị A bỏ khỏi bản nhãn nếu đang áp dụng đúng ngưỡng của bài. Box này không có mã L trong overlay chuẩn vì tool chỉ đánh số box đạt ngưỡng. Không thay XML đã khóa khi ghi QA.
- **L1 Truck, L2 Bike, L3 Truck — R02/R03:** class và box nhìn chung phù hợp. L2 là người đang ngồi/điều khiển xe nên gộp `Bike` hợp lý.
- **Phạm vi — R01:** hai `Pedestrian` ở trái giữa đã được box; chưa thấy rõ vật hợp lệ cao ≥40 px nào bị bỏ sót.
- **Vùng ignore — R07/R08:** `lens_border` dưới bám khá sát vòng kính; `ego_body` trái phủ phần thân/cụm xe camera, chưa thấy che nhầm đối tượng đáng kể.

Nghĩa xác nhận ba trường hợp `occluded=true` và đề nghị loại box nhỏ dưới ngưỡng. Các nhãn còn lại chưa thấy lỗi rõ. A cần sửa trên bản làm việc và xuất/khóa bản mới có truy vết; B kiểm lại sau khi A bàn giao.

## Các điểm cần kiểm trên toàn slice
| frame | object_ref | rule_id | quan sát của Nghĩa | cần kiểm lại | bằng chứng |
|---|---|---|---|---|---|
| adasind_270517.jpg | vật tối phía sau L2, giữa L2 và L7 (chưa có mã L) | R01 | Nghĩa thấy một vùng tối giống phương tiện ở nền; chưa rõ là vật độc lập hoặc cao ≥40 px. | Phóng ảnh gốc để xác nhận loại vật, chiều cao nhìn thấy và vùng hợp lệ; chỉ đề nghị thêm box nếu đủ điều kiện R01. | [Ảnh gốc](../../assets/images/adasind_270517.jpg), [overlay QA](qa_overlay.html) |
| adasind_271039.jpg | L7, L8, L9 | R05 | Hai cách lưu `occluded` trong XML khác nhau; Nghĩa nhấn mạnh phải xét che khuất thật trên ảnh, không tính vùng làm mờ. Chưa chốt giá trị riêng từng object. | A/B xác nhận trực tiếp đối tượng nào bị vật khác che; thống nhất hai trường occluded khi sửa nếu cần. | [Ảnh gốc](../../assets/images/adasind_271039.jpg), [overlay QA](qa_overlay.html) |
| adasind_271039.jpg | L11 Car đỏ | R02 | Mép dưới box có vẻ rộng xuống mặt đường; chưa đo phần dư. | Xem ảnh gốc ở độ phóng lớn, kiểm biên box chỉ ôm phần xe nhìn thấy. | [Ảnh gốc](../../assets/images/adasind_271039.jpg), [overlay QA](qa_overlay.html) |
| adasind_271039.jpg | phương tiện nhỏ nền trái/trung tâm (chưa có mã L) | R01 | Các box chồng nhau, chưa thấy rõ vật ≥40 px chắc chắn bị bỏ sót. | Kiểm vật độc lập, chiều cao nhìn thấy và vùng hợp lệ trước khi đề nghị bổ sung box. | [Ảnh gốc](../../assets/images/adasind_271039.jpg), [overlay QA](qa_overlay.html) |
| adasind_271039.jpg | lens_border mép trái và biên dưới | R08, R09 | Nghĩa chưa thấy đủ biên dưới; mép trái chỉ nên phủ vùng tối. | Soát toàn bộ vòng kính trên ảnh gốc để xác nhận không lấn đường hoặc đối tượng. | [Ảnh gốc](../../assets/images/adasind_271039.jpg), [overlay QA](qa_overlay.html) |
| adasind_295948.jpg | L4 Bike | R05 | Nghĩa xác nhận bị vật tiền cảnh che một phần; custom `occluded=false` không khớp ảnh. | A kiểm và sửa custom `occluded=true`, soát sự nhất quán với cờ shape gốc. | [Ảnh chụp QA](../screenshots/qa_B_295948_overlay.png), [overlay QA](qa_overlay.html) |
| adasind_295948.jpg | L5 Pedestrian | R05 | Nghĩa xác nhận phần dưới cơ thể bị vật/phương tiện khác che; custom `occluded=false`. | A kiểm và sửa custom `occluded=true`, soát sự nhất quán với cờ shape gốc. | [Ảnh chụp QA](../screenshots/qa_B_295948_overlay.png), [overlay QA](qa_overlay.html) |
| adasind_295948.jpg | L7 Truck | R05 | Nghĩa xác nhận vật khác che đáng kể; custom `occluded=false`. | A kiểm và sửa custom `occluded=true`, soát sự nhất quán với cờ shape gốc. | [Ảnh chụp QA](../screenshots/qa_B_295948_overlay.png), [overlay QA](qa_overlay.html) |
| adasind_295948.jpg | XML box #1 Car (không có L do H&lt;40) | R01 | Đối tượng thật nhưng box cao 26.99 px, dưới ngưỡng H=40 của bài. | A kiểm và loại box dưới ngưỡng nếu áp dụng đúng R01; ghi lý do trong rework/decision log. | [Ảnh chụp QA](../screenshots/qa_B_295948_overlay.png), [overlay QA](qa_overlay.html) |

Đã nhận và chốt nhận xét mù cho cả ba ảnh. Các ca chưa rõ ở 270517 và 271039 vẫn cần A/B trả lời; không được tính thành lỗi đã xác nhận. Bốn điểm A cần xử lý ở 295948 đã ghi vào `findings.csv` vòng `r2_qa`.

## Ảnh bằng chứng và việc còn mở

- [Ảnh chụp QA thật do Nghĩa cung cấp](../screenshots/qa_B_295948_overlay.png) hiển thị L4, L5, L7 và XML#1 trên frame `adasind_295948.jpg`; đã lưu nguyên byte, không dựng lại từ XML.
- Cần người soát xem lại vật tối phía sau L2 của `270517` và vùng ignore/giá trị `occluded` riêng của L7–L9 trên `271039` nếu muốn chốt các ca chưa rõ. Các ca này được giữ ở trạng thái chưa xác nhận lỗi.
- B bàn giao bản review và bốn dòng finding cho A/C, ghi rõ các ca chưa rõ; A phản hồi/sửa trên bản riêng, B kiểm lại bản A đã khóa lần sau.

Các dấu hiệu kỹ thuật ở qa_intake.md là dữ liệu kiểm tra XML; chưa thay nhận xét nhìn ảnh của Nghĩa.
Cột why, severity, owner và action của findings dành cho C theo phân công nhóm.
