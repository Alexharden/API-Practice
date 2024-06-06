# 政府 API 測試網站
> 本專案是練習Postman獲取API的實際運用過程以及用Python處理特定條件的資料


## **參考網站**
[中華民國政府資料開放平台 ](https://data.gov.tw/datasets/search?p=1&size=10&s=_score_desc&rft=api)

[中華民國政府資料開放平台 api 文件](https://www.ris.gov.tw/rs-opendata/api/Main/docs/v1)

----
## **測試工具**
 ![image](https://github.com/Alexharden/API-Practice/assets/124652625/e3702f54-fcb7-48cb-821e-2d1679d45324)  ![image](https://github.com/Alexharden/API-Practice/assets/124652625/9b2b5035-6ef1-4a46-a153-b2a67b1ce9b2)



## 測試題目

<table>
    <tr>
        <td>題目 1: 請透過上方 api 文件，找出 "歸化國籍人數按原屬國籍及性別分" 的資料，並把你/妳如何操作的步驟寫出</td>
    </tr>
	<tr>
		<td>題目 2: 請透過上方 api 文件，找出 "110年 嬰兒出生數按性別及生母單一年齡分（按登記）" 的資料 (所有頁數)</td>
    </tr>
	<tr>
		<td>題目 3: 接續上題，將媽媽未滿18歲的資料歸納出來</td>
    </tr>
	<tr>
    </tr>
</table>


## 解題思路
* 題目 1: 獲取“歸化國籍人數按原屬國籍及性別分”的數據
1. 通過 DataGetter 類獲取 API 文檔，保存為 test.json。
2. 通過 QuestionOne 類找到描述為“歸化國籍人數按原屬國籍及性別分”的 API 地址，並下載所有頁面的數據，保存到 question_one/question_one.json 文件。

* Question 1: Fetch data for "Number of Naturalized Citizens by Original Nationality and Gender"
1. Use the DataGetter class to fetch the API documentation and save it as test.json.
1. Use the QuestionOne class to find the API endpoint described as "Naturalized nationalities by original nationality and gender," and download all pages of data, saving it to the file question_one/question_one.json.
---
* 題目 2: 獲取“110年 嬰兒出生數按性別及生母單一年齡分（按登記）”的數據（所有頁數）
1. 使用 Question  2 類找到描述為“嬰兒出生數按性別及生母單一年齡分（按登記）”並包含年份 110 的 API 地址。
2. 下載所有頁面的數據，分別保存到 question_two 文件夾中，每頁一個文件。
* Question 2: Fetch data for "Number of Births by Gender and Mother's Single Year Age for the Year 110 (by Registration)"
1. Use the QuestionTwo class to find the API endpoint described as "Number of births by gender and mother's single year age (by registration)" for the year 110.
2. Download all pages of data and save each page to a separate file in the question_two directory.
---
* 題目 3: 將媽媽未滿18歲的數據歸納出來
1. 使用 QuestionThree 類讀取 question_two 文件夾中的所有數據文件。
2. 篩選出母親年齡小於18的數據，保存到 question_three/question_three.json 文件中。
* Question 3: Summarize Data for Mothers Under 18 Years Old
1. Use the QuestionThree class to read all data files in the question_two directory.
2. Filter out the data where the mother's age is less than 18, and save it to the file question_three/question_three.json.
