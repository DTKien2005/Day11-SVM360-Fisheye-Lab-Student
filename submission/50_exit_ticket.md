# Exit ticket

Đọc `docs/10-svm360-reading-vi.md` trước khi trả lời câu 1–2. Các câu về zone, `why`, rework, parking và sampling
đã nằm trong file tương ứng nên không hỏi lại ở đây.

1. **Một vật ở vùng seam giữa hai camera thật xuất hiện với hai box khác nhau: đó là lỗi `DUPLICATE` hay cần một quy tắc riêng? Vì sao?**
   - **Trả lời:** Cần một quy tắc riêng, **tuyệt đối không được tính là lỗi `DUPLICATE` thuần túy**.
   - **Lý giải kỹ thuật:** Trong hệ thống Surround View Monitoring (SVM) 4 camera fisheye, mỗi camera có một mặt phẳng quang học và tâm chiếu độc lập. Khi một vật thể nằm ở vùng giáp ranh (seam), ví dụ giữa Front và Left camera, nó thực sự xuất hiện trên cả 2 cảm biến với hai góc méo quang học và phối cảnh khác nhau. Ở tầng gán nhãn 2D trên từng camera thô (camera-specific annotation), việc vẽ box cho phần nhìn thấy trên mỗi camera là hoàn toàn hợp lệ để làm ground-truth huấn luyện các nhánh phát hiện (detection heads) riêng lẻ. Lỗi `DUPLICATE` chỉ áp dụng khi cùng một camera có hai box đè lên cùng một vật thể. Việc hợp nhất (fusion) hoặc khử trùng (cross-camera NMS) là nhiệm vụ của tầng BEV/Tracking 3D phía sau chứ không phải ép người gán nhãn xóa mất một góc nhìn hợp lệ.

2. **Một vật đi qua nhiều frame trên cùng camera: khi nào giữ cùng track ID, khi nào thêm keyframe hoặc trạng thái Outside? Nêu bằng chứng sẽ cần trước khi nối track qua hai camera.**
   - **Trả lời:**
     - *Giữ cùng track ID:* Khi đối tượng di chuyển liên tục trong trường nhìn của camera và vẫn nhận diện được cùng một thực thể vật lý (identity consistency), ngay cả khi bị che khuất tạm thời ngắn hạn (<1–2 giây) mà hướng chuyển động có thể dự đoán được.
     - *Thêm keyframe:* Khi đối tượng có sự thay đổi đột ngột về hình học (đổi hướng di chuyển, quay đầu, phóng to/thu nhỏ nhanh do tiếp cận gần thấu kính) hoặc trạng thái che khuất (occluded) thay đổi.
     - *Trạng thái Outside:* Khi đối tượng đi hoàn toàn ra khỏi trường nhìn thấu kính hoặc đi vào vùng đen ngoài vòng kính `lens_border`. Nếu sau đó đối tượng quay trở lại, cần đánh giá xem có đủ bằng chứng nhận dạng để gán lại ID cũ hay phải cấp ID mới.
     - *Bằng chứng cần để nối track qua hai camera:* Cần (1) Đồng bộ thời gian phần cứng (hardware timestamp match $\Delta t < 5$ms); (2) Ma trận hiệu chuẩn ngoại suy (extrinsics) chính xác giữa hai camera; (3) Quỹ đạo chuyển động liên tục khi chiếu lên mặt phẳng xe (BEV) và độ tương đồng đặc trưng ngoại hình (visual appearance/re-ID feature similarity).

3. **Nhìn lại cả buổi: một chỗ bạn tin nhãn mình đúng nhưng reference hoặc người soát nghĩ khác (dẫn frame/`object_ref`), bạn đã xử lý thế nào, và nếu làm lại slice này bạn sẽ đổi gì trong cách làm?**
   - **Trả lời:**
     - *Ca tranh luận cụ thể:* Tại frame `adasind_295948.jpg`, đối tượng xe máy lớn ở sát mép phải `(570, 605)-(1080, 1720)`. Người gán nhãn ban đầu gán `truncated=true` nhưng không tick `edge_zone=true`, trong khi QA Reviewer (Nghĩa) yêu cầu tick cả hai thuộc tính và nghi ngờ box bị lỏng ở phần bánh xe.
     - *Cách xử lý:* Nhóm đã mở file so sánh trực quan `compare.html` và `qa_overlay.html` để đo chính xác tỷ số khoảng cách tâm $r/R = 0.68 \ge 0.6$, từ đó xác định đây chắc chắn thuộc zone `edge`. Tại vòng P5 Rework, nhóm đã cập nhật chính xác thuộc tính `truncated=true` và `edge_zone=true` cho box này, đồng thời tinh chỉnh lại ranh giới box ôm khít mép vòng kính `lens_border`.
     - *Bài học kinh nghiệm:* Nếu làm lại slice này, tôi sẽ: (1) Rà soát trước danh sách các vật thể ở dải viền ngoại vi bằng thước đo bán kính trước khi gán nhãn hàng loạt; (2) Thiết lập quy ước rõ ràng giữa Annotator và QA về ranh giới `ego_body` ngay từ phút đầu tiên để không phải sửa lại hàng loạt box bị lấn vào nắp capo.

