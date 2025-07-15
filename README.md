
# 🤖 CodePilot

Your personal GenAI-powered coding assistant built with LangChain and Streamlit.

---

## 🚀 What is CodePilot?

**CodePilot** is an intelligent, multi-language coding assistant designed to help developers debug, refactor, or simply understand code. It uses cutting-edge LLMs (DeepSeek LLaMA 70B) via Groq to provide lightning-fast and context-aware responses to your code-related queries.

Whether you're stuck in Python, exploring Rust, or trying to remember syntax in Go—**CodePilot's got your back**.

---

## ✨ Features

✅ Supports 10+ Programming Languages  
✅ Paste Code + Ask Questions (Context-aware)  
✅ Clean Streamlit UI for instant use  
✅ Chat History to keep track of your questions  
✅ Powered by **LangChain** and **Groq's blazing-fast LLMs**

---

## 🧠 Tech Stack

- `Streamlit` — UI Framework
- `LangChain` — LLM Workflow
- `Groq + DeepSeek LLaMA 70B` — Fast & Intelligent Backend
- `Python` — Base Language

---

## 🖥️ Usage

### 🛠️ 1. Clone the repo
```bash
git clone https://github.com/yourusername/codepilot.git
cd codepilot
````

### 🔐 2. Set up your secret key

Save your **Groq API Key** in `.streamlit/secrets.toml`:

```toml
groq_key = "your_groq_api_key_here"
```

Or, use a Python `constants.py` file with:

```python
groq_key = "your_groq_api_key_here"
```

### ▶️ 3. Run the app

```bash
streamlit run codeAssitant.py
```

---

## 💻 Supported Languages

* Python 🐍
* JavaScript
* Java ☕
* C++
* HTML
* C#
* Go
* Rust 🦀
* TypeScript
* Ruby 💎

---



---

## 🙌 Contributing

Want to add features like code execution, theme toggle, or GitHub Copilot-style autocomplete?

Feel free to fork and PR. Let’s build a dev-first AI suite together. 🧠✨

---

## 🧑‍💻 Built By

**Gaurav Pandit**
 Data Scientist | AI Strategist | Founder of PAIRS
[LinkedIn](https://www.linkedin.com/in/gaurav-pandit) • 

---

## 📄 License

This project is licensed under the MIT License.

```

---

Let me know if you want a logo, `.streamlit/secrets.toml` format, or GIF preview embed as well. Want to convert this into a Streamlit deployable app with private API handling via GitHub secrets? I can guide you through that too.
```
