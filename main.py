from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ Enable CORS (for frontend connection)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Chat endpoint (NO validation error, NO API key needed)
@app.post("/chat")
def chat(message: dict = Body(...)):
    user_msg = message.get("message", "").lower()

    if "hello" in user_msg:
        reply = "Hello! How can I help you?"
    elif "name" in user_msg:
        reply = "I am your AI chatbot 🤖"
    elif "college" in user_msg:
        reply = "This project is made for college demo."
    elif "bye" in user_msg:
        reply = "Goodbye! Have a great day!"
    elif "project" in user_msg:
        reply = "This is an AI chatbot project using FastAPI and React."
    else:
        reply = "Sorry, I am still learning. Please try another question."

    return {"reply": reply}