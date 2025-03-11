# ⚽ FootyFacts - Football Trivia App

FootyFacts is an interactive **football trivia application** built with **Streamlit** and powered by **AI-based trivia services**. Challenge yourself with exciting football-related questions, test your knowledge, and learn new facts about the beautiful game! 🏆

---

## 🎯 Features

✅ **Interactive Trivia** - Answer football-related trivia questions in an engaging UI.  
✅ **AI-Powered Hints** - Get hints generated using OpenAI’s ChatGPT.  
✅ **Leaderboard** - Track your progress and compete with friends.  
✅ **User-Friendly Interface** - Built with **Streamlit** for a seamless experience.  

---

## 🛠️ Installation

### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/your-username/footyfacts.git
cd footyfacts
```

### 2️⃣ **Create and Activate a Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3️⃣ **Install Dependencies**
```sh
pip install -r requirements.txt
```

---

## 🚀 Running the App

After installation, launch the Streamlit app using:

```sh
streamlit run app/app.py
```

---

## 🔧 Configuration

The project uses environment variables for sensitive information like API keys.  
Create a `.env` file in the `config/` directory and add:

```
OPENAI_API_KEY=your_openai_api_key
GPT_MODEL=your-llm-model
MAX_TOKENS=500
HUGGINGFACE_TOKEN=your_hugging_face_token
```

---

## 📂 Project Structure

```
footyfacts/
│── app/             # Main entry point (Streamlit app)
│── assets/          # Images and other static assets
│── config/          # Configuration files and environment variables
│── data/            # Trivia questions and datasets
│── services/        # AI services and game logic
│── ui/              # Streamlit UI components
│── utils/           # Helper functions
│── requirements.txt # Python dependencies
│── README.md        # Project documentation
```

---

## 🤝 Contributing

Contributions are welcome! If you’d like to improve the project, feel free to:
- Fork the repository 🍴
- Create a new branch 🔀
- Submit a pull request ✅

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 💬 Contact

For questions or suggestions, reach out at [tayyabrahmani@example.com] or open an issue on GitHub.

Happy coding! 🎉
