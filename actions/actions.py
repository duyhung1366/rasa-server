# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Coroutine, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
import json
import requests

class ActionExamStructure(Action):

    def name(self) -> Text:
        return "action_send_exam"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dataJson = tracker.sender_id
        data = json.loads(dataJson)
        language = data["language"]

        if(language == "vi"):
            dispatcher.utter_message(text="Bài thi Toeic gồm có 2 phần chính: Nghe và Đọc. Ngoài ra còn có bài kiểm tra kỹ năng Toeic 4 bao gồm Nghe - Đọc và Nói - Viết. Mỗi phần thi Nghe – Đọc có 100 câu hỏi với tổng thời lượng làm bài là 2 giờ. Phần Nghe kéo dài trong 45 phút và phần Đọc kéo dài trong 75 phút. Phần Nói bao gồm 11 câu hỏi và kéo dài trong 20 phút. Phần Viết gồm 8 câu hỏi và kéo dài trong 60 phút.")
        else: 
            dispatcher.utter_message(text="The TOEIC test consists of two main sections: Listening and Reading. Additionally, there is the TOEIC 4 skills test which includes Listening - Reading and Speaking - Writing. Each part of the Listening - Reading section has 100 questions with a total test duration of 2 hours. The Listening section lasts for 45 minutes, and the Reading section lasts for 75 minutes. The Speaking section comprises 11 questions and lasts for 20 minutes. The Writing section consists of 8 questions and lasts for 60 minutes.")
        return []

class ActionListeningStructure(Action):

    def name(self) -> Text:
        return "action_listening_exam"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Coroutine[Any, Any, List[Dict[str, Any]]]:
        dataJson = tracker.sender_id
        data = json.loads(dataJson)
        language = data["language"]
        if(language == "vi"):
            dispatcher.utter_message(text="Phần Listening của TOEIC gồm 4 phần: Part 1 là Hình ảnh, Part 2 là Hỏi & Đáp, Part 3 là Hội thoại, và Part 4 là Bài nói chuyện. Tổng cộng có 100 câu hỏi và thời gian làm bài là 45 phút.")
        else: 
            dispatcher.utter_message(text="The Listening section of the TOEIC test consists of 4 parts: Part 1 is Photographs, Part 2 is Question-Response, Part 3 is Conversations, and Part 4 is Talks. In total, there are 100 questions, and the allotted time for completion is 45 minutes.")
        return []
    
class ActionReadingStructure(Action):

    def name(self) -> Text:
        return "action_ask_reading_structure"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Coroutine[Any, Any, List[Dict[str, Any]]]:
        dataJson = tracker.sender_id
        data = json.loads(dataJson)
        language = data["language"]
        if(language == "vi"):
            dispatcher.utter_message(text="Phần Reading của TOEIC gồm 3 phần: Part 5 là Điền từ vào câu, Part 6 là Điền từ vào đoạn văn, và Part 7 là Đọc hiểu. Tổng cộng có 100 câu hỏi và thời gian làm bài là 75 phút.")
        else: 
            dispatcher.utter_message(text="The Reading section of the TOEIC test comprises 3 parts: Part 5 is Incomplete Sentences, Part 6 is Text Completion, and Part 7 is Reading Comprehension. In total, there are 100 questions, and the allotted time for completion is 75 minutes.")
        return []

class ActionAskExamTips(Action):

    def name(self) -> Text:
        return "action_ask_exam_tips"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Coroutine[Any, Any, List[Dict[str, Any]]]:
        dataJson = tracker.sender_id
        data = json.loads(dataJson)
        language = data["language"]
        if(language == "en"):
            dispatcher.utter_message(text=(
                "Here are some tips to help you do well on the TOEIC exam:\n"
                "1. **Read the questions carefully first**: For the Listening section, read the questions carefully before listening to the conversation to understand what information to look for.\n"
                "2. **Manage your time**: Allocate your time wisely for each part of the test. Don’t spend too much time on one question.\n"
                "3. **Practice vocabulary**: Learn vocabulary through daily reading and listening. Focus on vocabulary that commonly appears in TOEIC tests.\n"
                "4. **Practice listening**: Improve your listening skills by listening to TOEIC sample audio, podcasts, or watching English videos.\n"
                "5. **Practice speed reading**: Practice reading comprehension with short and long passages, quickly identifying key information.\n"
                "6. **Don’t leave any answers blank**: Even if you’re unsure, always select an answer for each question.\n"
                "7. **Stay calm and focused**: Reduce stress by taking deep breaths and keeping a calm mindset.\n"
                "8. **Review common test formats**: Familiarize yourself with the structure and common question types of the TOEIC test.\n"
                "9. **Create a daily study routine**: Spend at least 30 minutes each day to review and improve your skills.\n"
                "10. **Make a study plan**: Set clear goals and a study schedule to optimize your review time."
            ))
        else: 
            dispatcher.utter_message(text=(
                "Đây là một số mẹo giúp bạn làm bài thi TOEIC hiệu quả:\n"
                "1. **Đọc kỹ câu hỏi trước**: Đối với phần Listening, hãy đọc kỹ câu hỏi trước khi nghe đoạn hội thoại để nắm được thông tin cần tìm.\n"
                "2. **Quản lý thời gian**: Hãy chia thời gian hợp lý cho mỗi phần của bài thi. Đừng dành quá nhiều thời gian cho một câu hỏi.\n"
                "3. **Luyện tập từ vựng**: Học từ vựng thông qua các bài đọc và nghe hàng ngày. Tập trung vào từ vựng thường xuất hiện trong các bài thi TOEIC.\n"
                "4. **Luyện nghe**: Nghe các bài nghe TOEIC mẫu, podcast, hoặc xem các video tiếng Anh để cải thiện kỹ năng nghe.\n"
                "5. **Luyện đọc nhanh**: Thực hành đọc hiểu các đoạn văn ngắn và dài, tìm kiếm thông tin quan trọng một cách nhanh chóng.\n"
                "6. **Không bỏ trống câu trả lời**: Dù không chắc chắn, hãy luôn chọn một đáp án cho mỗi câu hỏi.\n"
                "7. **Giữ bình tĩnh và tập trung**: Tránh căng thẳng bằng cách thở sâu và giữ tâm trạng thoải mái.\n"
                "8. **Ôn luyện kỹ các dạng bài thi**: Làm quen với cấu trúc và dạng câu hỏi thường gặp trong bài thi TOEIC.\n"
                "9. **Tạo thói quen ôn tập hàng ngày**: Dành ít nhất 30 phút mỗi ngày để ôn luyện và nâng cao kỹ năng.\n"
                "10. **Lập kế hoạch ôn tập**: Xác định mục tiêu và kế hoạch học tập rõ ràng để tối ưu hóa thời gian ôn luyện."
            ))
        return []

class ActionAskScoreInfo(Action):

    def name(self) -> Text:
        return "action_ask_score_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Coroutine[Any, Any, List[Dict[str, Any]]]:
        dataJson = tracker.sender_id
        data = json.loads(dataJson)
        language = data["language"]
        _domain = data["domain"]
        if(language == "en"):
            dispatcher.utter_message(text=(
                "Here is some information about TOEIC scores:\n"
                "1. **Scoring System**: The TOEIC test is scored on a scale from 10 to 990 points. The Listening and Reading sections each have a score range of 5 to 495 points.\n"
                "2. **Score Validity**: TOEIC scores are valid for two years from the test date.\n"
                "3. **Minimum and Maximum Scores**: The lowest possible score is 10 points, and the highest possible score is 990 points.\n"
                "4. **Average Score**: The average score for the TOEIC test varies, but typically ranges between 650 to 750 points.\n"
                "5. **Score Requirements**: Different institutions and employers have varying score requirements. Generally, a score of 785 or higher is considered good.\n"
                "6. **Score Report**: After taking the TOEIC test, you will receive a score report detailing your performance in each section.\n"
                "7. **Improving Your Score**: To improve your TOEIC score, practice regularly, focus on weak areas, and consider taking preparation courses.\n"
                "8. **Retaking the Test**: If you are not satisfied with your score, you can retake the TOEIC test. Many people see score improvements with additional study and practice.\n"
                "9. **Impact on Career**: TOEIC scores are often used by employers to assess English proficiency. A higher score can enhance your job prospects and career opportunities.\n"
                "10. **University Requirements**: Some universities require a minimum TOEIC score for admission. Check with the specific institution for their requirements.\n",
                f"For more study materials and practice tests, you can visit our website at <a href='{_domain}/en/test/toeic-test-full-test/'>{_domain}/en/test/toeic-test-full-test/</a>. Happy studying!"
            ))
        else: 
            dispatcher.utter_message(text=(
                "Dưới đây là một số thông tin về điểm TOEIC:\n"
                "1. **Hệ thống chấm điểm**: Bài thi TOEIC được chấm trên thang điểm từ 10 đến 990. Các phần Nghe và Đọc mỗi phần có thang điểm từ 5 đến 495.\n"
                "2. **Hiệu lực điểm**: Điểm TOEIC có giá trị trong vòng hai năm kể từ ngày thi.\n"
                "3. **Điểm tối thiểu và tối đa**: Điểm thấp nhất có thể đạt được là 10, và điểm cao nhất có thể đạt được là 990.\n"
                "4. **Điểm trung bình**: Điểm trung bình của bài thi TOEIC thường dao động từ 650 đến 750.\n"
                "5. **Yêu cầu điểm số**: Các tổ chức và nhà tuyển dụng khác nhau có yêu cầu điểm số khác nhau. Thông thường, điểm 785 trở lên được coi là tốt.\n"
                "6. **Báo cáo điểm**: Sau khi thi TOEIC, bạn sẽ nhận được báo cáo điểm chi tiết về hiệu suất của bạn trong mỗi phần.\n"
                "7. **Cải thiện điểm số**: Để cải thiện điểm TOEIC của bạn, hãy luyện tập thường xuyên, tập trung vào những phần yếu, và xem xét tham gia các khóa luyện thi.\n"
                "8. **Thi lại**: Nếu bạn không hài lòng với điểm số của mình, bạn có thể thi lại TOEIC. Nhiều người thấy điểm số cải thiện sau khi học thêm và luyện tập.\n"
                "9. **Ảnh hưởng đến sự nghiệp**: Điểm TOEIC thường được các nhà tuyển dụng sử dụng để đánh giá khả năng tiếng Anh. Điểm cao hơn có thể cải thiện cơ hội nghề nghiệp và triển vọng của bạn.\n"
                "10. **Yêu cầu của trường đại học**: Một số trường đại học yêu cầu điểm TOEIC tối thiểu để nhập học. Kiểm tra với trường cụ thể để biết yêu cầu của họ.\n",
                f"Để có thêm tài liệu và bài luyện thi tốt, bạn có thể truy cập trang web của chúng tôi tại <a href='{_domain}/test/toeic-test-full-test/'>{_domain}/test/toeic-test-full-test/</a>. Chúc bạn học tốt!"
            ))
        return []

class ActionPart1Info(Action):

    def name(self) -> Text:
        return "action_part_1_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Coroutine[Any, Any, List[Dict[str, Any]]]:
        dataJson = tracker.sender_id
        data = json.loads(dataJson)
        language = data["language"]
        _domain = data["domain"]
        
        if(language == "en"):
            dispatcher.utter_message(text=(
                f"Part 1 of the TOEIC test assesses your ability to listen in Toeic. You can practice at <a href='{_domain}/en/practice/toeic-practice-part-1-photos/' target='_blank'>{_domain}/en/practice/toeic-practice-part-1-photos/</a>."
            ))
        else: 
            dispatcher.utter_message(text=(
                f"Phần 1 của bài thi TOEIC kiểm tra kỹ năng Nghe trong bài thi TOEIC. Bạn có thể luyện tập tại <a href='{_domain}/practice/toeic-practice-part-1-photos/' target='_blank'>{_domain}/practice/toeic-practice-part-1-photos/</a>."
            ))
        return []

class ActionPart2Info(Action):

    def name(self) -> Text:
        return "action_part_2_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Coroutine[Any, Any, List[Dict[str, Any]]]:
        dataJson = tracker.sender_id
        data = json.loads(dataJson)
        language = data["language"]
        _domain = data["domain"]
        
        if(language == "en"):
            dispatcher.utter_message(text=(
                f"Part 2 of the TOEIC test assesses your ability to listen in Toeic. You can practice at <a href='{_domain}/en/practice/toeic-practice-part-2-question-response/' target='_blank'>{_domain}/en/practice/toeic-practice-part-2-question-response/</a>."
            ))
        else: 
            dispatcher.utter_message(text=(
                f"Phần 2 của bài thi TOEIC kiểm tra kỹ năng Nghe trong bài thi TOEIC. Bạn có thể luyện tập tại <a href='{_domain}/practice/toeic-practice-part-2-question-response/' target='_blank'>{_domain}/practice/toeic-practice-part-2-question-response/</a>."
            ))
        return []

class ActionPart3Info(Action):

    def name(self) -> Text:
        return "action_part_3_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Coroutine[Any, Any, List[Dict[str, Any]]]:
        dataJson = tracker.sender_id
        data = json.loads(dataJson)
        language = data["language"]
        _domain = data["domain"]
        
        if(language == "en"):
            dispatcher.utter_message(text=(
                f"Part 3 of the TOEIC test assesses your ability to listen in Toeic. You can practice at <a href='{_domain}/en/practice/toeic-practice-part-3-conversations/' target='_blank'>{_domain}/en/practice/toeic-practice-part-3-conversations/</a>."
            ))
        else: 
            dispatcher.utter_message(text=(
                f"Phần 3 của bài thi TOEIC kiểm tra kỹ năng Nghe trong bài thi TOEIC. Bạn có thể luyện tập tại <a href='{_domain}/practice/toeic-practice-part-3-conversations/' target='_blank'>{_domain}/practice/toeic-practice-part-3-conversations/</a>."
            ))
        return []

class ActionPart4Info(Action):

    def name(self) -> Text:
        return "action_part_4_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Coroutine[Any, Any, List[Dict[str, Any]]]:
        dataJson = tracker.sender_id
        data = json.loads(dataJson)
        language = data["language"]
        _domain = data["domain"]
        
        if(language == "en"):
            dispatcher.utter_message(text=(
                f"Part 4 of the TOEIC test assesses your ability to listen in Toeic. You can practice at <a href='{_domain}/en/practice/toeic-practice-part-4-short-talks/' target='_blank'>{_domain}/en/practice/toeic-practice-part-4-short-talks/</a>."
            ))
        else: 
            dispatcher.utter_message(text=(
                f"Phần 4 của bài thi TOEIC kiểm tra kỹ năng Nghe trong bài thi TOEIC. Bạn có thể luyện tập tại <a href='{_domain}/practice/toeic-practice-part-4-short-talks/' target='_blank'>{_domain}/practice/toeic-practice-part-4-short-talks/</a>."
            ))
        return []

class ActionPart5Info(Action):

    def name(self) -> Text:
        return "action_part_5_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Coroutine[Any, Any, List[Dict[str, Any]]]:
        dataJson = tracker.sender_id
        data = json.loads(dataJson)
        language = data["language"]
        _domain = data["domain"]
        
        if(language == "en"):
            dispatcher.utter_message(text=(
                f"Part 5 of the TOEIC test assesses your ability to reading in Toeic. You can practice at <a href='{_domain}/en/practice/toeic-practice-part-5-incomplete-sentences' target='_blank'>{_domain}/en/practice/toeic-practice-part-5-incomplete-sentences</a>."
            ))
        else: 
            dispatcher.utter_message(text=(
                f"Phần 5 của bài thi TOEIC kiểm tra kỹ năng Đọc trong bài thi TOEIC. Bạn có thể luyện tập tại <a href='{_domain}/practice/toeic-practice-part-5-incomplete-sentences' target='_blank'>{_domain}/practice/toeic-practice-part-5-incomplete-sentences</a>."
            ))
        return []
    
class ActionPart6Info(Action):

    def name(self) -> Text:
        return "action_part_6_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Coroutine[Any, Any, List[Dict[str, Any]]]:
        dataJson = tracker.sender_id
        data = json.loads(dataJson)
        language = data["language"]
        _domain = data["domain"]
        
        if(language == "en"):
            dispatcher.utter_message(text=(
                f"Part 6 of the TOEIC test assesses your ability to reading in Toeic. You can practice at <a href='{_domain}/en/practice/toeic-practice-part-6-text-completion' target='_blank'>{_domain}/en/practice/toeic-practice-part-6-text-completion</a>."
            ))
        else: 
            dispatcher.utter_message(text=(
                f"Phần 6 của bài thi TOEIC kiểm tra kỹ năng Đọc trong bài thi TOEIC. Bạn có thể luyện tập tại <a href='{_domain}/practice/toeic-practice-part-6-text-completion' target='_blank'>{_domain}/practice/toeic-practice-part-6-text-completion</a>."
            ))
        return []
    
class ActionPart7Info(Action):

    def name(self) -> Text:
        return "action_part_7_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Coroutine[Any, Any, List[Dict[str, Any]]]:
        dataJson = tracker.sender_id
        data = json.loads(dataJson)
        language = data["language"]
        _domain = data["domain"]
        
        if(language == "en"):
            dispatcher.utter_message(text=(
                f"Part 7 of the TOEIC test assesses your ability to reading in Toeic. You can practice at <a href='{_domain}/en/practice/toeic-practice-part-7-single-passages' target='_blank'>{_domain}/en/practice/toeic-practice-part-7-single-passages</a>."
            ))
        else: 
            dispatcher.utter_message(text=(
                f"Phần 7 của bài thi TOEIC kiểm tra kỹ năng Đọc trong bài thi TOEIC. Bạn có thể luyện tập tại <a href='{_domain}/practice/toeic-practice-part-7-single-passages' target='_blank'>{_domain}/practice/toeic-practice-part-7-single-passages</a>."
            ))
        return []
    
class ActionAskPersonalization(Action):

    def name(self) -> Text:
        return "action_ask_personalization"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Coroutine[Any, Any, List[Dict[str, Any]]]:
        dataJson = tracker.sender_id
        data = json.loads(dataJson)
        language = data["language"]
        _domain = data["domain"]
        
        if(language == "en"):
            dispatcher.utter_message(text=(
                f"To personalize your learning experience, please visit our personalization page at <a href='{_domain}/en/learning-path/?app=toeic' target='_blank'>{_domain}/en/learning-path/?app=toeic</a>."
            ))
        else: 
            dispatcher.utter_message(text=(
                f"Để cá nhân hóa trải nghiệm học tập của bạn, hãy truy cập vào trang web cá nhân hóa của chúng tôi tại <a href='{_domain}/learning-path/?app=toeic' target='_blank'>{_domain}/en/learning-path/?app=toeic</a>."
            ))
        return []

class ActionAskStatistics(Action):

    def name(self) -> Text:
        return "action_ask_user_statistics"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict) -> Coroutine[Any, Any, List[Dict[str, Any]]]:
        dataJson = tracker.sender_id
        data = json.loads(dataJson)
        language = data["language"]
        _domain = data["domain"]
        user_id = data["userId"]

        response = requests.get(f"http://localhost:3001/api/analytics/statisticize-practice-learning?topicIds=660e52758d50a20990dd7419,660e52878d50a20990dd7437,65fa906cf428895a08a2046b,65fa905cf428895a08a20434,6112216a1e6e0c7cbe10585d,6112217f1e6e0c7cbe105862&userId={user_id}")
        statisticDatas = response.json()

        if(len(statisticDatas) <= 0):
            return []
        
        output = ""
        for stats in statisticDatas:
            totalCorrect = stats.get("totalCorrect", 0)
            totalAnswered = stats.get("totalAnswered", 0)
            totalQuestions = stats.get("totalQuestions", 0)
            name = stats.get("topicName")
            overall = (totalCorrect/totalQuestions)*100
            if(totalQuestions > 0): 
                if(language == "vi"):
                    output += f"<b>{name}</b>: đã làm {totalAnswered}/{totalQuestions} câu hỏi trong đó có {totalCorrect} câu làm đúng, tỉ lệ hoàn thành là : {overall}%<br/>"
                else: 
                    output += f"<b>{name}</b>: Answered {totalAnswered}/{totalQuestions} questions, with {totalCorrect} correct, completion rate: {overall}%.<br/>"
        
        if(language == "vi"):
            output += f"xem chi tiết tại : <a href='{_domain}/my-learning/?app=toeic' target='_blank'>{_domain}/my-learning/?app=toeic</a>"
        else: 
            output += f"View details at: <a href='{_domain}/en/my-learning/?app=toeic' target='_blank'>{_domain}/en/my-learning/?app=toeic</a>"
        dispatcher.utter_message(text=output)
        return []
