# GPT 기반 작성
import os
import openai
import requests
import io  # 이 줄을 추가하세요
import base64  # base64 모듈도 추가
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
gpt_key_path = os.path.join(BASE_DIR, 'keys', 'gptKey.txt')

with open(gpt_key_path, 'r') as file:
    api_key = file.read().strip()
# openai.api_key = api_key

# OpenAI 클라이언트 초기화 (새로운 API 형식)
client = openai.OpenAI(api_key=api_key)

# OpenAI API 키 설정
# openai.api_key = 
# client = openai.OpenAI()
# image_path = '/home/myeong/ex_room_img/room.jpg'


# OpenAI 클라이언트 초기화
# client = openai(api_key="YOUR_API_KEY")

able_object_list = ['Sectional_Sofas', 'Sleeper_Sofas', 'Reclining_Sofas', 'LoveSeats', 'Futons', 'Settles', 'Convertibles', 
                        'Accent_Chairs', 'Coffee_Tables', 'TV_Stands', 'End_Tables', 'Console_Tables', 'Ottomans', 'Living_Room_Sets', 
                        'Decorative_Pillows', 'Throw_Blankets', 'Area_Rugs', 'Wall_Arts', 'Table_Lamps', 'Floor_Lamps', 
                        'Pendants_and_Chandeliers', 'Sconces', 'Baskets_and_Storage', 'Candles', 'Live_Plants', 'Artificial_Plants', 
                        'Planters', 'Decorative_Accessories', 'Window_Coverings', 'Decorative_Mirrors', 'Dining_Sets', 
                        'Dining_Tables', 'Dining_Chairs', 'Bar_Stools', 'Kitchen_Islands', 'Buffets_and_Sideboards', 'China_Cabinets', 
                        'Bakers_Recks', 'Bedroom_Sets', 'Mattresses', 'Nightstands', 'Dressers', 'Beds', 'Bedframes', 'Bases', 'Vanities', 
                        'Entryway_Furnitures', 'Desks', 'Desk_Chairs', 'Bookcases', 
                        'File_Cabinets', 'Computer_Armoires', 'Drafting_Tables', 'Cabinets', 'Furniture_Sets']

prompt = "As Sherlock Holmes, please analyze the pictures of the following rooms and recommend what furniture you would like for this room. Here's a list of furniture you can recommend, so all you have to do is pick one piece of furniture.'able_object_list': {}. you just need to tell one object. just a one word.".format(able_object_list)
# def analyze_room_and_recommend_furniture(image_path):
#     """
#     방 사진을 분석하고 셜록 홈즈 스타일로 방에 대한 추리와 가구 추천을 제공합니다.

#     :param image_path: 방 사진의 경로 또는 URL
#     :return: 추리 및 가구 추천 결과
#     """
#     # 'gpt-4-vision-preview' 모델에 이미지와 프롬프트 전달
    
#     # 'gpt-4-vision-preview' 모델에 이미지와 프롬프트 전달
#     response = openai.ChatCompletion.create(
#         model="gpt-4-vision-preview",
#         messages=[{
#             "role": "system",
#             "content": prompt
#         }, {
#             "role": "user",
#             "content": image_path
#         }]
#     )

#     return response.choices[0].message.content


# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')
 
 
# Path to your image
# image_path = "/home/myeong/ex_room_img/bae_room.jpg"
 
# Getting the base64 string
def analyze_room_and_recommend_furniture(image_path):
    base64_image = encode_image(image_path)
    
    # headers = {
    # "Content-Type": "application/json",
    # "Authorization": f"Bearer {api_key}"
    # }
    
    # payload = {
    # "model": "gpt-4.1-nano",
    # "messages": [
    #     {
    #     "role": "user",
    #     "content": [
    #         {
    #         "type": "text",
    #         "text": prompt
    #         },
    #         {
    #         "type": "image_url",
    #         "image_url": {
    #             "url": f"data:image/jpeg;base64,{base64_image}"
    #         }
    #         }
    #     ]
    #     }
    # ],
    # "max_tokens": 300
    # }
        # ✅ 새로운 OpenAI API 형식으로 변경
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        max_tokens=300
    )
    
    # OpenAI API에 POST 요청 보내기
    # response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    
    # API 응답에서 필요한 정보 추출
    # furniture_recommendation = response.json()['choices'][0]['message']['content']
    furniture_recommendation = response.choices[0].message.content
    # 추출된 내용 출력
    return furniture_recommendation

# 예시 이미지 경로
# image_path = '/home/myeong/ex_room_img/room.jpg'

# 분석 및 추천 실행
# result = analyze_room_and_recommend_furniture(image_path)
# print(result)











####################################################
# gpt4 설명
# 참고 사항
# low"고해상도" 모델이 비활성화됩니다. 모델은 저해상도 512px x 512px 버전의 이미지를 수신하고 65개의 토큰 예산으로 이미지를 나타냅니다. 
# 이를 통해 API는 높은 세부 정보가 필요하지 않은 사용 사례에 대해 더 빠른 응답을 반환하고 더 적은 입력 토큰을 사용할 수 있습니다.

# high먼저 모델이 저해상도 이미지를 볼 수 있도록 한 다음 입력 이미지 크기를 기반으로 512px 정사각형으로 입력 이미지의 세부 자르기를 생성하는 "고해상도" 모드를 활성화합니다. 
# 각각의 세부 작물은 토큰 예산(65개 토큰)의 두 배를 사용하여 총 129개 토큰을 사용합니다.