import requests, json, os  # 引入requests, json和os模組

class DataGetter:  # 定義DataGetter類，用於獲取API數據
    def __init__(self):  # 初始化方法
        pass
    
    def request_url(self, apiUrl):  # 定義方法來請求URL
        response = requests.get(apiUrl)  # 發送GET請求到指定的apiUrl
        if response.status_code == 200:  # 如果請求成功（狀態碼為200）
            jsonData = json.dumps(response.json(), indent=4, ensure_ascii=False)  # 將響應轉換為格式化的JSON字符串
            with open("test.json", "w+", encoding="utf-8") as js:  # 打開test.json文件，模式為寫入（如果不存在則創建）
                js.write(jsonData)  # 將JSON字符串寫入文件
        else:  # 如果請求失敗
            print(f"請求失敗，狀態碼為{response.status_code}")  # 打印錯誤訊息

class BaseQuestion:  # 定義BaseQuestion基類
    def __init__(self, apiName):  # 初始化方法，接受apiName參數
        self.apiName = apiName  # 將apiName存儲為實例變數
        self.targetApi = None  # 初始化targetApi為None
        self.get_target_api()  # 調用get_target_api方法

    def get_target_api(self):  # 定義方法來獲取目標API
        with open("test.json", "r", encoding="utf-8") as js:  # 打開test.json文件，模式為讀取
            js = json.load(js)  # 將JSON數據載入為字典
            for tag in js["tags"]:  # 遍歷字典中的tags列表
                if tag["description"] == self.apiName:  # 如果描述匹配apiName
                    self.targetApi = f"https://www.ris.gov.tw//rs-opendata/api/v1/datastore/{tag['name']}"  # 設置targetApi

    def save_json_data(self, folder, filename, data):  # 定義方法來保存JSON數據
        if not os.path.isdir(folder):  # 如果指定的文件夾不存在
            os.mkdir(folder)  # 創建文件夾
        with open(f"{folder}/{filename}", "w+", encoding="utf-8") as file:  # 打開指定的文件，模式為寫入（如果不存在則創建）
            json.dump(data, file, ensure_ascii=False, indent=4)  # 將數據轉換為格式化的JSON字符串並寫入文件

class QuestionOne(BaseQuestion):  # 定義QuestionOne類，繼承自BaseQuestion
    def __init__(self, apiName):  # 初始化方法，接受apiName參數
        super().__init__(apiName)  # 調用父類的初始化方法
        self.get_target_data()  # 調用get_target_data方法

    def get_target_data(self):  # 定義方法來獲取目標數據
        if not self.targetApi:  # 如果targetApi為None
            return  # 退出方法
        response = requests.get(self.targetApi)  # 發送GET請求到targetApi
        jsonData = response.json()  # 將響應轉換為JSON格式
        if response.status_code == 200:  # 如果請求成功
            all_data = []  # 初始化一個空列表，用於存儲所有頁面的數據
            for page in range(1, int(jsonData["totalPage"]) + 1):  # 遍歷所有頁面
                response = requests.get(f"{self.targetApi}/?page={page}")  # 請求每一頁數據
                if response.status_code == 200:  # 如果請求成功
                    all_data.append(response.json())  # 將響應轉換為JSON並加入列表
            self.save_json_data("./question_one", "question_one.json", all_data)  # 將所有數據保存到文件中
        else:  # 如果請求失敗
            print(f"出問題了，狀態碼為{response.status_code}")  # 打印錯誤訊息

class QuestionTwo(BaseQuestion):  # 定義QuestionTwo類，繼承自BaseQuestion
    def __init__(self, apiName, year):  # 初始化方法，接受apiName和year參數
        self.year = year  # 將year存儲為實例變數
        super().__init__(apiName)  # 調用父類的初始化方法
        self.targetApi = f"{self.targetApi}/{self.year}"  # 根據year設置targetApi
        self.get_target_data()  # 調用get_target_data方法

    def get_target_data(self):  # 定義方法來獲取目標數據
        if not self.targetApi:  # 如果targetApi為None
            return  # 退出方法
        response = requests.get(self.targetApi)  # 發送GET請求到targetApi
        jsonData = response.json()  # 將響應轉換為JSON格式
        if response.status_code == 200:  # 如果請求成功
            for page in range(1, int(jsonData["totalPage"]) + 1):  # 遍歷所有頁面
                response = requests.get(f"{self.targetApi}/?page={page}")  # 請求每一頁數據
                if response.status_code == 200:  # 如果請求成功
                    self.save_json_data("./question_two", f"question_two-{page}.json", response.json())  # 將數據保存到相應的文件中
        else:  # 如果請求失敗
            print(f"出問題了，狀態碼為{response.status_code}")  # 打印錯誤訊息

class QuestionThree:  # 定義QuestionThree類，用於處理問題三
    def __init__(self, motherAge):  # 初始化方法，接受motherAge參數
        self.MotherAge = motherAge  # 將motherAge存儲為實例變數
        self.get_data()  # 調用get_data方法

    def extract_numbers(self, input_string):  # 定義方法來提取字符串中的數字
        numbers = ''.join(filter(str.isdigit, input_string))  # 使用filter過濾出數字並組合成字符串
        return int(numbers) if numbers else None  # 將數字字符串轉換為整數，如果沒有數字則返回None

    def get_data(self):  # 定義方法來獲取數據
        if not os.path.isdir("./question_three"):  # 如果question_three目錄不存在
            os.mkdir("./question_three")  # 創建question_three目錄
        filtered_data = []  # 初始化一個空列表，用於存儲篩選出的數據
        for i in range(len(os.listdir("./question_two"))):  # 遍歷question_two目錄中的所有文件
            with open(f"./question_two/question_two-{i+1}.json", "r", encoding="utf-8") as data:  # 打開每個文件，模式為讀取
                data = json.load(data)  # 將JSON數據載入為字典
                for item in data["responseData"]:  # 遍歷字典中的responseData列表
                    mother_age_str = item["mother_age"]  # 獲取母親年齡字符串
                    mother_age_num = self.extract_numbers(mother_age_str)  # 提取母親年齡中的數字
                    if mother_age_num is not None and mother_age_num < self.MotherAge:  # 如果提取到的年齡數字小於指定年齡
                        filtered_data.append({key: value for key, value in item.items()})  # 將符合條件的數據加入篩選後的列表
        self.save_filtered_data(filtered_data)  # 調用save_filtered_data方法將篩選後的數據保存到文件中

    def save_filtered_data(self, filtered_data):  # 定義方法來保存篩選後的數據
        with open("./question_three/question_three.json", "w+", encoding="utf-8") as file:  # 打開question_three.json文件，模式為寫入
            json.dump(filtered_data, file, ensure_ascii=False, indent=4)  # 將篩選後的數據寫入文件
        print(f"Filtered data saved to question_three/question_three.json")  # 打印確認訊息


