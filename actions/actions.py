# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import mysql.connector


class DatabaseManager:
    def __init__(self):
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="123456789",
            database="rasa_db"
        )

    def disconnect(self):
        if self.connection:
            self.connection.close()

    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result


class ActionGreet(Action):
    def name(self) -> Text:
        return "action_greet"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(response="utter_greet")
        return []


class ActionSaveCustInfo(Action):
    def name(self) -> Text:
        return "action_save_cust_info"

    async def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        user_id = (tracker.current_state())["sender_id"]
        print(user_id)
        customer_gender = next(tracker.get_latest_entity_values("customer_gender"), None)
        customer_name = next(tracker.get_latest_entity_values("customer_name"), None)
        return [SlotSet("customer_gender", customer_gender), SlotSet("customer_name", customer_name)]


class ActionGetBrandInfo(Action):
    def name(self) -> Text:
        return "action_get_brands_info"

    async def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        db_manager = DatabaseManager()
        db_manager.connect()

        result = db_manager.execute_query("SELECT name FROM brand")

        db_manager.disconnect()

        data_list = [f"- {''.join(str(info) for info in data)}" for index, data in
                     enumerate(result)]

        dispatcher.utter_message(response="utter_brand_results", data="\n".join(data_list))

        return []


class ActionGetLaptopName(Action):
    def name(self) -> Text:
        return "action_get_laptop_name"

    async def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        global name_lap
        laptop_name = next(tracker.get_latest_entity_values("laptop_name"), None)
        db_manager = DatabaseManager()
        db_manager.connect()

        result = db_manager.execute_query("SELECT * FROM laptop "
                                          "WHERE name LIKE '%{}%'".format(laptop_name))

        db_manager.disconnect()

        if result is None or len(result) == 0:
            dispatcher.utter_message(response="utter_not_found")
        else:
            result_0 = result[0]
            template = "- Tên: {}\n Mô tả: {}\n- Cấu hình: {}\n- Cân nặng {}\n- Giá tiền: {}"
            data = template.format(result_0[1], result_0[4], result_0[5], result_0[6], "{:,}".format(result_0[2]))
            dispatcher.utter_message(response="utter_laptop_result", data=data)
        # print(name_lap)
        return []


class ActionGetWarrantyPolice(Action):
    def name(self) -> Text:
        return "action_get_warranty_police"

    async def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        data = 'Hỗ trợ trả bảo hành tận nơi tại Tp.HCM và tại trung tâm các tỉnh/Tp khác./nCam kết bảo hành trong 12 tháng/nĐể biết thêm thông tin chi tiết, bạn vui lòng truy cập vào link dưới đây/n/nhttps://www.google.com/'
        dispatcher.utter_message(response="utter_warranty_police", data=data)
        return []


class ActionGetLaptopPriceUnder(Action):
    def name(self) -> Text:
        return "action_get_laptop_price_under"

    async def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        laptop_under = next(tracker.get_latest_entity_values("laptop_under"), None)
        laptop_name = 'PRICE UNDER'
        return [SlotSet("laptop_name", laptop_name), SlotSet("laptop_under", laptop_under)]


class ActionGetLaptopForStudying(Action):
    def name(self) -> Text:
        return "action_get_laptop_for_studying"

    async def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        data = ['Laptop DELL', 'Laptop MSI', 'Laptop ASUS']
        dispatcher.utter_message(response="utter_laptop_for_studying", data=data)


class ActionGetLaptopForGaming(Action):
    def name(self) -> Text:
        return "action_get_laptop_for_gaming"

    async def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        data = ['Laptop ASUS', 'Laptop MSI']
        dispatcher.utter_message(response="utter_laptop_for_gaming", data=data)


class ActionGetLaptopForWorking(Action):
    def name(self) -> Text:
        return "action_get_laptop_for_working"

    async def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        data = ['Laptop MSI', 'Macbook Pro', 'Macbook Air']
        dispatcher.utter_message(response="utter_laptop_for_working", data=data)


class ActionGetLaptopOfBrand(Action):
    def name(self) -> Text:
        return "action_get_laptop_of_brand"

    async def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        brand_name = next(tracker.get_latest_entity_values("brand_name"), None)
        db_manager = DatabaseManager()
        db_manager.connect()

        query_sql = "SELECT brand.name, laptop.* FROM laptop INNER JOIN brand ON brand.id = laptop.brand_id WHERE brand.name LIKE '%{}%'"

        result = db_manager.execute_query(query_sql.format(brand_name))

        db_manager.disconnect()

        if result is None or len(result) == 0:
            dispatcher.utter_message(response="utter_brand_not_found")
        else:

            # data_list = [f"- {''.join(str(info) for info in data)}" for index, data in
            #              enumerate(result)]
            template = "- Tên: {}\n  Giá tiền: {}\n\n"
            data_list = ''.join([template.format(item[2], "{:,}".format(item[3])) for item in result])

            SlotSet("brand_name", result[1][0])
            dispatcher.utter_message(response="utter_laptops_brand_result", data=data_list)

        return []


class ActionGetPaymentMethod(Action):
    def name(self) -> Text:
        return "action_get_payment_method"

    async def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        data_list = ['- Tiền mặt', '- Ví điện tử', '- Thẻ tín dụng', '- Internet banking']
        dispatcher.utter_message(response="utter_payment_result", data='\n'.join(data_list))
        return []


class ActionInformation(Action):
    def name(self) -> Text:
        return "action_information"

    async def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        data_list = ['- Số điện thoại: 0999.999.999', '- Địa chỉ: 19 Đ. Nguyễn Hữu Thọ, Tân Hưng, Quận 7, Thành phố Hồ Chí Minh']
        dispatcher.utter_message(response="utter_information", data='\n'.join(data_list))
        return []


class ActionFallback(Action):
    def name(self) -> Text:
        return "action_fallback"

    async def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        message_content = tracker.latest_message.get('text')
        print(message_content)
        dispatcher.utter_message(response="utter_please_rephrase")
        return []