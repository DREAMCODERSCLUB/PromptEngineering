🔍 PromptCraft Lab
PromptCraft Lab is an interactive playground that demonstrates how different prompt engineering techniques affect the responses of Google's Gemini 1.5 Flash model. 
It helps learners and developers explore Zero-shot, One-shot, Few-shot, and Chain-of-Thought (CoT) prompting strategies with real-time comparisons.


<img width="1277" alt="image" src="https://github.com/user-attachments/assets/068c570a-084c-4a37-8bd7-e75850636ada" />



Example interface:
🧠 Choose a task (e.g., Summarize, Sentiment Analysis, or General Question)
✍️ Enter your input text
⚡️ Compare how the Gemini model responds under different prompting techniques

📦 Features
✅ Gemini 1.5 Flash API integration via Google Generative AI SDK
✅ Four prompt techniques:
Zero-shot
One-shot
Few-shot
Chain-of-Thought (CoT)
✅ Simple web UI using Gradio
✅ Easily extendable for more tasks or prompt strategies


🛠️ Tech Stack
Python 3.9+
Gradio
Google Generative AI SDK
dotenv

🧠 Prompt Engineering Types
Prompt Type	        Description
Zero-shot	          Directly asks the model to perform a task without examples.
One-shot	          Includes one example before the task.
Few-shot	          Includes multiple examples to improve performance and alignment.
Chain-of-Thought	  Prompts the model to reason step-by-step (useful for logical questions).


🔐 Setup Instructions
Clone the repository
git clone https://github.com/DREAMCODERSCLUB/promptcraft-lab.git
cd promptcraft-lab

Install dependencies
pip install -r requirements.txt

Add your API key
Create a .env file in the root directory with your Gemini API key:
GOOGLE_API_KEY=your_gemini_api_key_here

Run the app
python app.py

Your app will launch at http://127.0.0.1:7860

Examples - 
- Summarize -
  <img width="1202" alt="image" src="https://github.com/user-attachments/assets/f3ac4d87-236d-42f1-990e-a09ce7aa61b4" />

- Sentiment Analysis
  <img width="1162" alt="image" src="https://github.com/user-attachments/assets/582f03e2-fee0-4d40-8952-5df78cdf066a" />

- General Question -
  <img width="1143" alt="image" src="https://github.com/user-attachments/assets/be65327e-f602-426d-b72e-839fec21a4ed" />

📌 Future Ideas
Add more NLP tasks (e.g., translation, topic classification)
Visualize response quality metrics
Let users add their own examples
Integrate Pinecone for embedding-based similarity

🤝 Contributing
Pull requests are welcome! Please open an issue first to discuss changes or enhancements.

📜 License
MIT License

🌐 Connect with Us
Made with ❤️ by DREAM Coders Club
