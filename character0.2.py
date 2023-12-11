import zhipuai
import requests
from gtts import gTTS
import os
import speech_recognition as sr

zhipuai.api_key = "b4ff2d89de8245d9cad16b9864454b79.6XdHhjC67aWjoeUA"
recognizer = sr.Recognizer()  # 实例化识别器
last_dialog = None  # 请注意，我添加了这一行来初始化 last_dialog

def detect_emotion(text, api_token):
    # 初始化 ChatGLM-Turbo 对象
    chat_glm = ChatGLM(api_token)  # 请确保 ChatGLM 类的定义正确

    # 调用 ChatGLM-Turbo 进行情感识别
    result = chat_glm.text_classification(text, model_name="emotion_recognition")

    # 识别情绪
    emotion = result[0]['label']

    return emotion

def generate_reply(emotion):
    if emotion == "正面":
        return "（正面情绪）非常高兴听到您的话，请继续分享您的感受！"
    elif emotion == "负面":
        return "（负面情绪）非常抱歉听到您的话，请保持微笑，相信自己， Everything will be fine！"
    else:
        return "（中立情绪）非常抱歉，我没有意识到您的情绪。请继续分享您的感受，我会尽力帮助您。"

def main():
    global last_dialog
    recognizer = sr.Recognizer()  # 实例化识别器

    while True:
        # 识别用户的语音输入
        with sr.Microphone() as source:
            print("请说话：")
            try:
                audio = recognizer.listen(source)
                # 将语音转换为文本
                text = recognizer.recognize_google(audio, language="zh-CN")
                print(f"你说了: {text}")

                # 在这里添加你的其他处理逻辑
                # ...

            except sr.WaitTimeoutError:
                # 用户停止说话后的超时，通常不会触发这里
                print("录音结束，等待下一次说话")

            except sr.UnknownValueError:
                # 无法识别的语音
                print("抱歉，无法识别你说的内容")

            except sr.RequestError as e:
                # 无法连接到语音识别服务
                print(f"请求语音识别服务时发生错误: {e}")

            except Exception as e:
                # 处理其他异常
                print(f"发生未知错误: {e}")

        # 调用模型进行交互
        response = zhipuai.model_api.sse_invoke(
            model="ChatGLM_turbo",
            prompt=[
                {"role": "user", "content": "你好"},
                {"role": "assistant", "content": "我是人工智能助手"},
                {"role": "user", "content": "你叫什么名字"},
                {"role": "assistant", "content": "我叫chatGLM"},
                {"role": "user", "content": "你都可以做些什么事"},
            ],
            temperature=0.95,
            top_p=0.7,
            incremental=True
        )

        # 处理响应
        for event in response.events():
            if event.event == "add":
                print(event.data)
            elif event.event == "error" or event.event == "interrupted":
                print(event.data)
            elif event.event == "finish":
                print(event.data)
                print(event.meta)
            else:
                print(event.data)

        # 更新上一次对话内容
        last_dialog = event.data

        # 语音合成
        speech = zhipuai.speech(event.data)
        print(f"语音合成: {speech}")

        # 识别情绪
        emotion = detect_emotion(event.data, "your_api_token")
        print(f"情绪识别: {emotion}")

        # 根据情绪生成回答
        reply = generate_reply(emotion)
        print(f"回答: {reply}")

if __name__ == "__main__":
    main()
