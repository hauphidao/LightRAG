from __future__ import annotations
from typing import Any

GRAPH_FIELD_SEP = "<SEP>"

PROMPTS: dict[str, Any] = {}

PROMPTS["DEFAULT_LANGUAGE"] = "Vietnamese"
PROMPTS["DEFAULT_TUPLE_DELIMITER"] = "<|>"
PROMPTS["DEFAULT_RECORD_DELIMITER"] = "##"
PROMPTS["DEFAULT_COMPLETION_DELIMITER"] = "<|COMPLETE|>"

# Các loại thực thể phổ biến trong văn bản hành chính
PROMPTS["DEFAULT_ENTITY_TYPES"] = [
    "tên_cơ_quan",
    "đơn_vị_trực_thuộc",
    "họ_và_tên",
    "chức_vụ",
    "mã_số_cán_bộ",
    "danh_xưng",
    "tên_địa_phương",
    "địa_chỉ",
    "ngày_ban_hành",
    "thời_hạn_hiệu_lực",
    "thời_gian_thực_hiện",
    "loại_văn_bản",
    "số_hiệu_văn_bản",
    "trích_yếu_nội_dung",
    "căn_cứ_pháp_lý",
    "tên_văn_bản_pháp_lý",
    "điều_khoản_viện_dẫn",
    "hành_động_nghiệp_vụ",
    "đối_tượng_thực_hiện",
    "văn_bản_đính_kèm",
    "lĩnh_vực_quản_lý",
    "số_liệu_định_lượng",
    "mức_lương_hỗ_trợ",
    "tên_dự_án_chương_trình",
    "tên_chức_danh_ngạch",
    "cơ_quan_tiếp_nhận",
    "cơ_quan_phối_hợp",
    "cơ_quan_tham_mưu",
    "loại_hồ_sơ",
    "trạng_thái_xử_lý",
    "phương_thức_xử_lý",
    "ngày_tiếp_nhận",
    "ngày_trả_kết_quả",
    "tên_người_ký",
    "chức_vụ_người_ký",
    "cơ_sở_pháp_lý",
    "tên_đơn_vị_sử_dụng",
    "tài_sản_công",
    "hình_thức_thực_hiện",
    "mục_đích_sử_dụng",
    "tên_chức_năng",
    "mã_văn_bản",
    "đơn_vị_chủ_trì",
    "đơn_vị_phối_hợp",
    "tên_nghị_quyết",
    "ngày_ký_kết",
    "tên_hồ_sơ",
    "số_tài_liệu_đính_kèm",
    "điều_kiện_áp_dụng",
    "đối_tượng_áp_dụng",
    "đối_tượng_thực_hiện",
    "tên_hệ_thống",
    "tên_hành_động",
    "tên_bộ_luật",
    "tên_giấy_tờ",
    "thuật_ngữ_liên_quan",
    "tên_điều_khoản",
    "tên_hội_đồng",
    "tên_tổ_chức",
]

PROMPTS["DEFAULT_USER_PROMPT"] = "n/a"

PROMPTS["entity_extraction"] = """---Mục tiêu---
Trích xuất thông tin từ văn bản hành chính tiếng Việt theo các bước sau:

---Các bước---
1. Xác định các thực thể. Với mỗi thực thể, trích xuất:
- tên_thực_thể: Tên của thực thể (Nếu phát hiện có dấu hiệu bất thường như dư dấu khoảng trắng, sai chính tả hãy sửa lại cho chính xác)
- loại_thực_thể: Một trong các loại sau: [{entity_types}]
- mô_tả: Mô tả ngắn gọn về thực thể
Định dạng: ("entity"{tuple_delimiter}<tên_thực_thể>{tuple_delimiter}<loại_thực_thể>{tuple_delimiter}<mô_tả>)

2. Xác định các mối quan hệ giữa các thực thể:
- thực_thể_nguồn: tên thực thể nguồn
- thực_thể_đích: tên thực thể đích  
- mô_tả_quan_hệ: mô tả mối quan hệ
- độ_mạnh: điểm từ 1-10 thể hiện độ mạnh của quan hệ
Định dạng: ("relationship"{tuple_delimiter}<thực_thể_nguồn>{tuple_delimiter}<thực_thể_đích>{tuple_delimiter}<mô_tả_quan_hệ>{tuple_delimiter}<độ_mạnh>)

3. Xác định từ khóa chính của văn bản:
Định dạng: ("content_keywords"{tuple_delimiter}<từ_khóa>)

4. Trả về kết quả bằng tiếng Việt, sử dụng {record_delimiter} để phân cách các mục.

5. Kết thúc bằng {completion_delimiter}

######################
---Ví dụ---
######################
{examples}

#############################
---Dữ liệu thực tế---
######################
Loại thực thể: [{entity_types}]
Văn bản:
{input_text}
######################
Kết quả:"""

PROMPTS["entity_extraction_examples"] = [
    """Ví dụ 1:

Loại thực thể: [cơ_quan, người, thời_gian, số_văn_bản, loại_văn_bản]
Văn bản:
```
CÔNG VĂN SỐ 123/UBND-TH
Về việc triển khai kế hoạch phòng chống dịch Covid-19

Kính gửi: Các phòng ban trực thuộc UBND quận

Căn cứ Nghị quyết số 45/NQ-CP ngày 15/3/2023 của Chính phủ về việc tăng cường công tác phòng chống dịch Covid-19;

Căn cứ Công văn số 789/BYT-VP ngày 20/3/2023 của Bộ Y tế về việc hướng dẫn triển khai các biện pháp phòng chống dịch;

UBND quận yêu cầu các phòng ban trực thuộc triển khai các nội dung sau:

1. Tổ chức tuyên truyền, phổ biến các biện pháp phòng chống dịch đến người dân
2. Tăng cường kiểm tra, giám sát việc thực hiện các biện pháp phòng chống dịch
3. Báo cáo kết quả triển khai về UBND quận trước ngày 30/3/2023

Nơi nhận:
- Như trên
- Lưu: VT

TM. UBND QUẬN
CHỦ TỊCH
Nguyễn Văn A
```

Kết quả:
("entity"{tuple_delimiter}"UBND quận"{tuple_delimiter}"cơ_quan"{tuple_delimiter}"Cơ quan ban hành công văn"){record_delimiter}
("entity"{tuple_delimiter}"Nguyễn Văn A"{tuple_delimiter}"người"{tuple_delimiter}"Chủ tịch UBND quận"){record_delimiter}
("entity"{tuple_delimiter}"15/3/2023"{tuple_delimiter}"thời_gian"{tuple_delimiter}"Ngày ban hành Nghị quyết 45/NQ-CP"){record_delimiter}
("entity"{tuple_delimiter}"123/UBND-TH"{tuple_delimiter}"số_văn_bản"{tuple_delimiter}"Số hiệu công văn"){record_delimiter}
("entity"{tuple_delimiter}"Công văn"{tuple_delimiter}"loại_văn_bản"{tuple_delimiter}"Loại văn bản được ban hành"){record_delimiter}
("relationship"{tuple_delimiter}"UBND quận"{tuple_delimiter}"Nguyễn Văn A"{tuple_delimiter}"Nguyễn Văn A là Chủ tịch UBND quận"{tuple_delimiter}10){record_delimiter}
("relationship"{tuple_delimiter}"UBND quận"{tuple_delimiter}"Công văn"{tuple_delimiter}"UBND quận ban hành công văn"{tuple_delimiter}9){record_delimiter}
("content_keywords"{tuple_delimiter}"phòng chống dịch, Covid-19, triển khai kế hoạch"){completion_delimiter}
#############################""",
]

PROMPTS["summarize_entity_descriptions"] = """Bạn là trợ lý giúp tóm tắt thông tin từ dữ liệu được cung cấp.
Cho một hoặc hai thực thể và danh sách mô tả liên quan đến thực thể đó.
Hãy kết hợp tất cả thành một mô tả toàn diện. Đảm bảo bao gồm thông tin từ tất cả các mô tả.
Nếu có mâu thuẫn, hãy giải quyết và đưa ra một tóm tắt nhất quán.
Viết ở ngôi thứ ba và bao gồm tên thực thể để có đầy đủ ngữ cảnh.
Sử dụng tiếng Việt.

#######
---Dữ liệu---
Thực thể: {entity_name}
Danh sách mô tả: {description_list}
#######
Kết quả:
"""

PROMPTS["entity_continue_extraction"] = """
Có thể còn thiếu một số thực thể và mối quan hệ trong lần trích xuất trước.

---Nhớ các bước---

1. Xác định các thực thể. Với mỗi thực thể, trích xuất:
- tên_thực_thể: Tên của thực thể
- loại_thực_thể: Một trong các loại sau: [{entity_types}]
- mô_tả: Mô tả ngắn gọn về thực thể
Định dạng: ("entity"{tuple_delimiter}<tên_thực_thể>{tuple_delimiter}<loại_thực_thể>{tuple_delimiter}<mô_tả>)

2. Xác định các mối quan hệ giữa các thực thể:
- thực_thể_nguồn: tên thực thể nguồn
- thực_thể_đích: tên thực thể đích  
- mô_tả_quan_hệ: mô tả mối quan hệ
- độ_mạnh: điểm từ 1-10 thể hiện độ mạnh của quan hệ
Định dạng: ("relationship"{tuple_delimiter}<thực_thể_nguồn>{tuple_delimiter}<thực_thể_đích>{tuple_delimiter}<mô_tả_quan_hệ>{tuple_delimiter}<độ_mạnh>)

3. Xác định từ khóa chính của văn bản:
Định dạng: ("content_keywords"{tuple_delimiter}<từ_khóa>)

4. Trả về kết quả bằng tiếng Việt, sử dụng {record_delimiter} để phân cách các mục.

5. Kết thúc bằng {completion_delimiter}

---Kết quả---

Thêm các thực thể và quan hệ còn thiếu theo định dạng trên:\n
""".strip()

PROMPTS["entity_if_loop_extraction"] = """
---Mục tiêu---

Có thể vẫn còn thiếu một số thực thể.

---Kết quả---

Trả lời CHỈ bằng `CÓ` hoặc `KHÔNG` nếu còn thực thể cần thêm.
""".strip()

PROMPTS["fail_response"] = (
    "Xin lỗi, tôi chưa thể trả lời chính xác câu hỏi này, vui lòng cung cấp thêm thông tin để tôi có thể trả lời chính xác hơn."
)

PROMPTS["rag_response"] = """🧑‍💼 Vai trò
Bạn là một trợ lý người Việt Nam sống tại TP.HCM, hiểu biết sâu về văn hóa, xã hội và pháp luật Việt Nam. Bạn chỉ sử dụng tiếng Việt thuần túy, văn phong tự nhiên, vui vẻ, thân thiện, như một người Việt bình thường khi trả lời câu hỏi về dữ liệu được cung cấp dưới dạng JSON.

---Mục tiêu---
- Trả lời ngắn gọn, chính xác và dễ hiểu dựa trên dữ liệu trong Cơ sở tri thức, đồng thời không thêm thông tin không có sẵn. Câu trả lời cần:
- Tuân theo lịch sử hội thoại và yêu cầu hiện tại
- Phản ánh đúng nội dung được cung cấp, kết hợp với kiến thức phổ thông phù hợp
- Chỉ tập trung vào bối cảnh Việt Nam và các lĩnh vực hành chính công

---Nguyên tắc xử lý dữ liệu theo thời gian---
- Mỗi quan hệ có created_at để đánh dấu thời điểm tạo.
- Khi có mâu thuẫn, cân nhắc cả thời gian và ngữ nghĩa.
- Không mặc định quan hệ mới là đúng – cần đánh giá theo ngữ cảnh.
- Với câu hỏi liên quan đến thời gian, ưu tiên thông tin bên trong nội dung hơn là created_at.

---Xử lý câu hỏi thường gặp---
- Nhận biết các câu như chào hỏi, cảm ơn, xin lỗi…
- Trả lời tự nhiên, không cần dẫn chứng hoặc truy xuất dữ liệu
- Nếu câu hỏi không dùng tiếng Việt, dịch câu trả lời sang tiếng Việt rồi trả lời
- Tuyệt đối trả lời dưới góc nhìn, văn hoá người Việt

---Truy xuất thông tin---
- Kiểm tra kỹ dữ liệu trước khi trả lời
- Trả lời chính xác, đầy đủ, dễ hiểu
- Cuối câu trả lời, nếu cần, liệt kê tối đa 5 tài liệu tham khảo, định dạng như sau:
  + [Văn bản] đường_dẫn_file
  + [Tri thức] đường_dẫn_file

---Giới hạn nội dung & bảo mật---
- Chỉ hỗ trợ các câu hỏi liên quan đến hành chính công vụ Việt Nam, như:
- Quản lý dự án, đấu thầu, hợp đồng
- Hoạt động cơ quan hành chính, CNTT
- Quy định pháp lý (Nghị định, Thông tư…)
- Từ chối trả lời các câu hỏi liên quan đến:
  + Chính trị, quân sự, giới tính, tôn giáo, sắc tộc, tranh chấp lãnh thổ
  + Nội dung nhạy cảm (bạo lực, mại dâm, hack, chất cấm, vũ khí…)
  + Ví dụ: “Tôi chỉ hỗ trợ thông tin liên quan đến hành chính công vụ tại Việt Nam, không thể cung cấp thông tin về các vấn đề nhạy cảm như vậy nhé!”

---Quy tắc định dạng---
- Định dạng và độ dài: {response_type}
- Luôn dùng tiếng Việt
- Trình bày bằng markdown với tiêu đề rõ ràng
- Văn phong gần gũi, dễ hiểu, không quá kỹ thuật hay hành chính
Ví dụ:
- “Bộ phận kế toán chịu trách nhiệm kiểm tra…”
- “Bộ phận kế toán sẽ xem xét kỹ các điều kiện thanh toán để đảm bảo mọi thứ đúng quy định nha!”

---Đầu vào và yêu cầu---
- Lịch sử hội thoại: {history}
- Dữ liệu JSON (Tri thức + Văn bản): {context_data}
- Yêu cầu thêm từ người dùng: {user_prompt}

---Khi không có dữ liệu---
- Nếu không có thông tin phù hợp: khéo léo từ chối thay vì đoán hoặc suy diễn.

Trả lời:"""

PROMPTS["keywords_extraction"] = """---Vai trò---

Bạn là trợ lý giúp xác định từ khóa cấp cao và cấp thấp trong câu hỏi và lịch sử hội thoại của người dùng.

---Mục tiêu---

Cho câu hỏi và lịch sử hội thoại, liệt kê cả từ khóa cấp cao và cấp thấp. Từ khóa cấp cao tập trung vào khái niệm hoặc chủ đề tổng thể, trong khi từ khóa cấp thấp tập trung vào thực thể, chi tiết hoặc thuật ngữ cụ thể.

---Hướng dẫn---

- Xem xét cả câu hỏi hiện tại và lịch sử hội thoại liên quan khi trích xuất từ khóa
- Đầu ra từ khóa theo định dạng JSON, sẽ được phân tích bởi JSON parser, không thêm nội dung khác
- JSON nên có hai khóa:
  - "high_level_keywords" cho khái niệm hoặc chủ đề tổng thể
  - "low_level_keywords" cho thực thể hoặc chi tiết cụ thể

######################
---Ví dụ---
######################
{examples}

#############################
---Dữ liệu thực tế---
######################
Lịch sử hội thoại:
{history}

Câu hỏi hiện tại: {query}
######################
Đầu ra phải là văn bản thông thường, không phải ký tự unicode. Giữ nguyên ngôn ngữ với Câu hỏi.
Đầu ra:

"""

PROMPTS["keywords_extraction_examples"] = [
    """Ví dụ 1:

Câu hỏi: "Công văn số 123/UBND-TH quy định những nội dung gì về phòng chống dịch Covid-19?"
################
Đầu ra:
{
  "high_level_keywords": ["Công văn", "Phòng chống dịch", "Covid-19"],
  "low_level_keywords": ["123/UBND-TH", "Quy định", "Nội dung"]
}
#############################""",
    """Ví dụ 2:

Câu hỏi: "Ai là người ký công văn số 456/UBND-TH về việc triển khai kế hoạch phát triển kinh tế?"
################
Đầu ra:
{
  "high_level_keywords": ["Công văn", "Ký", "Kế hoạch phát triển"],
  "low_level_keywords": ["456/UBND-TH", "Người ký", "Kinh tế"]
}
#############################""",
]

PROMPTS["naive_rag_response"] = """---Vai trò---

Bạn là trợ lý giúp trả lời câu hỏi về Đoạn văn bản được cung cấp dưới dạng JSON.

---Mục tiêu---

Tạo câu trả lời ngắn gọn dựa trên Đoạn văn bản và tuân theo Quy tắc trả lời, xem xét cả lịch sử hội thoại và câu hỏi hiện tại. Tóm tắt tất cả thông tin trong Đoạn văn bản được cung cấp, và kết hợp kiến thức chung liên quan. Không bao gồm thông tin không có trong Đoạn văn bản.

Khi xử lý nội dung có thời gian:
1. Mỗi phần nội dung có timestamp "created_at" cho biết thời điểm có được thông tin này
2. Khi gặp thông tin mâu thuẫn, xem xét cả nội dung và thời gian
3. Không tự động ưu tiên nội dung mới nhất - sử dụng phán đoán dựa trên ngữ cảnh
4. Với câu hỏi về thời gian, ưu tiên thông tin thời gian trong nội dung trước khi xem xét thời gian tạo

---Lịch sử hội thoại---
{history}

---Đoạn văn bản(DC)---
{content_data}

---Quy tắc trả lời---

- Định dạng và độ dài: {response_type}
- Sử dụng định dạng markdown với các tiêu đề phù hợp
- Trả lời bằng cùng ngôn ngữ với câu hỏi của người dùng
- Đảm bảo câu trả lời duy trì tính liên tục với lịch sử hội thoại
- Liệt kê tối đa 5 nguồn tham khảo quan trọng nhất ở cuối phần "Tài liệu tham khảo". Rõ ràng chỉ ra mỗi nguồn từ Đoạn văn bản(DC), và bao gồm đường dẫn file nếu có, theo định dạng: [DC] đường_dẫn_file
- Nếu không biết câu trả lời, hãy nói như vậy
- Không bao gồm thông tin không có trong Đoạn văn bản
- Yêu cầu thêm của người dùng: {user_prompt}

Trả lời:"""

# TODO: deprecated
PROMPTS["similarity_check"] = """Hãy phân tích độ tương đồng giữa hai câu hỏi:

Câu hỏi 1: {original_prompt}
Câu hỏi 2: {cached_prompt}

Hãy đánh giá xem hai câu hỏi này có tương đồng về ngữ nghĩa không, và liệu câu trả lời cho Câu hỏi 2 có thể dùng để trả lời Câu hỏi 1 không, cung cấp điểm tương đồng từ 0 đến 1.

Tiêu chí điểm tương đồng:
0: Hoàn toàn không liên quan hoặc không thể tái sử dụng câu trả lời, bao gồm nhưng không giới hạn:
   - Câu hỏi có chủ đề khác nhau
   - Địa điểm được đề cập khác nhau
   - Thời gian được đề cập khác nhau
   - Cá nhân cụ thể được đề cập khác nhau
   - Sự kiện cụ thể được đề cập khác nhau
   - Thông tin nền khác nhau
   - Điều kiện chính khác nhau
1: Giống hệt và có thể tái sử dụng câu trả lời trực tiếp
0.5: Có liên quan một phần và cần điều chỉnh câu trả lời
Chỉ trả về một số từ 0-1, không có nội dung bổ sung.
"""
