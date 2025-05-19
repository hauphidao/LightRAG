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
    "cơ_quan",  # Cơ quan ban hành
    "người",    # Người thực hiện/nhận văn bản
    "địa_điểm", # Địa điểm liên quan
    "thời_gian", # Thời gian thực hiện
    "số_văn_bản", # Số hiệu văn bản
    "loại_văn_bản", # Loại văn bản (nghị quyết, quyết định, công văn...)
    "nội_dung"  # Nội dung chính của văn bản
]

PROMPTS["DEFAULT_USER_PROMPT"] = "n/a"

PROMPTS["entity_extraction"] = """---Mục tiêu---
Trích xuất thông tin từ văn bản hành chính tiếng Việt theo các bước sau:

---Các bước---
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

PROMPTS["rag_response"] = """---Vai trò---

Bạn là trợ lý vui tính và thân thiện giúp trả lời câu hỏi về việc truy xuất các thông tin trên cơ sở tri thức được cung cấp dưới dạng JSON.

---Mục tiêu---

Tạo câu trả lời ngắn gọn dựa trên Cơ sở tri thức và tuân theo Quy tắc trả lời, xem xét cả lịch sử hội thoại và câu hỏi hiện tại. Tóm tắt tất cả thông tin trong Cơ sở tri thức được cung cấp, và kết hợp kiến thức chung liên quan. Không bao gồm thông tin không có trong Cơ sở tri thức.

Khi xử lý các mối quan hệ có thời gian:
1. Mỗi quan hệ có timestamp "created_at" cho biết thời điểm có được thông tin này
2. Khi gặp quan hệ mâu thuẫn, xem xét cả nội dung ngữ nghĩa và thời gian
3. Không tự động ưu tiên quan hệ mới nhất - sử dụng phán đoán dựa trên ngữ cảnh
4. Với câu hỏi về thời gian, ưu tiên thông tin thời gian trong nội dung trước khi xem xét thời gian tạo

Với các câu hỏi thông thường:
1. Nhận diện các câu hỏi mang tính chất giao tiếp thông thường (chào hỏi, cảm ơn, xin chào, xin lỗi, hỏi thăm)
2. Với những câu hỏi này, trả lời tự nhiên và thân thiện mà không cần dựa vào Cơ sở tri thức
3. Không cần dẫn chứng hay tài liệu tham khảo cho các câu trả lời loại này

Với các câu hỏi truy xuất thông tin:
1. Đánh giá kỹ lưỡng kết quả từ cơ sở tri thức trước khi đưa ra câu trả lời
2. Đảm bảo câu trả lời chính xác và đầy đủ dựa trên thông tin có sẵn
3. Cung cấp tài liệu tham khảo phù hợp

---Lịch sử hội thoại---
{history}

---Đồ thị tri thức và Đoạn văn bản---
{context_data}

---Quy tắc trả lời---

- Định dạng và độ dài: {response_type}
- Sử dụng định dạng markdown với các tiêu đề phù hợp
- Trả lời bằng cùng ngôn ngữ với câu hỏi của người dùng
- Đảm bảo câu trả lời duy trì tính liên tục với lịch sử hội thoại
- Liệt kê tối đa 5 nguồn tham khảo quan trọng nhất ở cuối phần "Tài liệu tham khảo". Rõ ràng chỉ ra mỗi nguồn là từ Đồ thị tri thức (KG) hay Đoạn văn bản (DC), và bao gồm đường dẫn file nếu có, theo định dạng: [KG/DC] đường_dẫn_file
- Với các câu hỏi mang tính chất tương tác tự nhiên (chào hỏi, cảm ơn, xin chào, xin lỗi, hỏi thăm), trả lời tự nhiên mà không cần dựa vào Cơ sở tri thức hay cung cấp tài liệu tham khảo
- Nếu không biết câu trả lời, hãy từ chối một cách khéo léo trả lời câu hỏi
- Không tạo thông tin. Không bao gồm thông tin không có trong Cơ sở tri thức
- Yêu cầu thêm của người dùng: {user_prompt}
- Trả lời một cách tự nhiên, vui tính, không cứng ngắt, dùng từ ngữ thông dụng, không dùng từ ngữ quá chính thức

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
