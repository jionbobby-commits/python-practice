import re
import os
import json
from datetime import datetime
import streamlit as st

os.environ["NO_PROXY"] = "127.0.0.1,localhost"
from openai import OpenAI

st.set_page_config(
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    page_title="AI friend",
    menu_items={
        "About": "# 这是一个AI朋友，可以和您聊天，回答您的问题。"
    }
)
st.logo("./file/logo.png")

# ---------- 会话文件管理 ----------
SESSION_DIR = "sessions"
os.makedirs(SESSION_DIR, exist_ok=True)  # 文件夹不存在就创建


def new_session_name():
    """用当前时间当会话名，如 20251216_144915"""
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def save_session():
    """把当前会话写入 JSON 文件；没有消息就不保存"""
    if not st.session_state.messages:
        return
    data = {
        "nick_name": st.session_state.nick_name,
        "nature": st.session_state.nature,
        "messages": st.session_state.messages,
    }
    path = f"{SESSION_DIR}/{st.session_state.current_session}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def list_sessions():
    """列出所有历史会话名，最新的排在最上面"""
    names = [f[:-5] for f in os.listdir(SESSION_DIR) if f.endswith(".json")]
    return sorted(names, reverse=True)


def reset_session():
    """清空当前对话，开一个新的会话名"""
    st.session_state.messages = []
    st.session_state.current_session = new_session_name()


def new_session():
    save_session()   # 先保存旧会话
    reset_session()


def load_session(name):
    with open(f"{SESSION_DIR}/{name}.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    st.session_state.messages = data["messages"]
    st.session_state.nick_name = data["nick_name"]
    st.session_state.nature = data["nature"]
    st.session_state.current_session = name


def delete_session(name):
    path = f"{SESSION_DIR}/{name}.json"
    if os.path.exists(path):
        os.remove(path)
    if name == st.session_state.current_session:
        reset_session()   # 删的是当前会话，就回到空白新会话（这里不能再保存）


# ---------- 初始化状态 ----------
if "messages" not in st.session_state:
    st.session_state.messages = []
if "current_session" not in st.session_state:
    st.session_state.current_session = new_session_name()
if "nick_name" not in st.session_state:
    st.session_state.nick_name = "小美"
if "nature" not in st.session_state:
    st.session_state.nature = "温柔可爱一口台湾腔的台湾妹子"

# ---------- 侧边栏 ----------
with st.sidebar:
    st.subheader("AI控制面板")

    st.button("新建会话", icon="✏️", use_container_width=True, on_click=new_session)

    st.text("历史会话")
    for name in list_sessions():
        col1, col2 = st.columns([4, 1])
        with col1:
            st.button(
                name,
                icon="📄",
                key=f"load_{name}",
                use_container_width=True,
                type="primary" if name == st.session_state.current_session else "secondary",
                on_click=load_session,
                args=(name,),
            )
        with col2:
            st.button("✖", key=f"del_{name}", on_click=delete_session, args=(name,))

    st.divider()
    st.text_input("名字", key="nick_name")
    st.text_area("性格", key="nature")

# ---------- 主界面 ----------
st.title("AI智友")
st.caption(f"当前会话: {st.session_state.current_session}")

# 名字和性格拼进系统提示词
system_prompt = (
    f"你叫{st.session_state.nick_name}，性格是：{st.session_state.nature}。"
    "你拥有计算机和管理学的专业知识，擅长机器学习、编程和人工智能领域。"
    "请始终保持这个人设，用中文和用户交流，并用专业知识帮助用户回答问题。"
)

for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

client = OpenAI(
    api_key="ollama",
    base_url="http://localhost:11434/v1",
)


def stream_answer(stream):
    """把模型的流式输出转成纯文本流，同时过滤 <think>...</think>"""
    raw = ""
    shown = 0
    for chunk in stream:
        if not chunk.choices:
            continue
        raw += chunk.choices[0].delta.content or ""

        visible = re.sub(r"<think>.*?</think>", "", raw, flags=re.DOTALL)
        idx = visible.find("<think>")
        if idx != -1:
            visible = visible[:idx]
        for k in range(len("<think>") - 1, 0, -1):
            if visible.endswith("<think>"[:k]):
                visible = visible[:-k]
                break
        visible = visible.lstrip()

        if len(visible) > shown:
            yield visible[shown:]
            shown = len(visible)


prompt = st.chat_input("请输入您的消息：")
if prompt:
    st.chat_message("user").write(prompt)
    print("------------------->调用ai大模型：提示词：", prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    stream = client.chat.completions.create(
        model="deepseek-r1:7b",
        messages=[
            {"role": "system", "content": system_prompt},
            *st.session_state.messages
        ],
        stream=True,
    )

    with st.chat_message("assistant"):
        answer = st.write_stream(stream_answer(stream))

    print("<-------------------调用ai大模型：返回结果：", answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})

    save_session()   # 每次回答完自动保存
    st.rerun()       # 刷新页面，让新会话出现在侧边栏历史列表里