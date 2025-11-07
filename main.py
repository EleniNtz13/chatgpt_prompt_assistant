# ============================================================
#  ChatGPT Prompt Assistant (Offline Mock Version with Memory)
#  ------------------------------------------------------------
#  Author: [Your Name]
#  Description:
#     This is an offline, simulated version of a ChatGPT-like
#     assistant that mimics conversational AI behavior.
#     It includes short-term memory to make the dialogue feel
#     natural, even without connecting to the OpenAI API.
# ============================================================

import random

# ============================================================
# 🧩 Mock AI Response Generator (Simulated ChatGPT Behavior)
# ============================================================
def mock_ai_response(user_input, conversation_history):
    """
    Generates a mock ChatGPT-like response.
    Uses the last few user messages as context to simulate memory.
    """

    # Extract last 3 user messages from conversation history
    user_messages = [msg["content"] for msg in conversation_history if msg["role"] == "user"]
    context = " | ".join(user_messages[-3:])  # Combine last messages for memory effect

    # --- Rule-based simulated responses ---
    if "hello" in user_input.lower():
        return "Hello there! 👋 How are you feeling today?"
    elif "name" in user_input.lower():
        return "I don’t really have a name yet — maybe you could give me one? 🤖"
    elif "project" in user_input.lower():
        return "Are you referring to your AI project? It sounds exciting!"
    elif "remember" in user_input.lower():
        return f"Of course! You mentioned earlier: '{context}'."
    else:
        # --- Generic memory-based replies ---
        generic_replies = [
            f"Interesting point about '{user_input}'. Based on what we discussed — {context}.",
            f"Hmm, I see your point about '{user_input}'. Earlier you mentioned {context}.",
            f"Let's connect this with what you said before: {context}.",
            f"That’s a nice continuation of our earlier chat about {context}.",
            f"Could you explain a bit more about '{user_input}'?"
        ]
        return random.choice(generic_replies)

# ============================================================
# 💬 Conversation Loop (User ↔ Assistant)
# ============================================================
conversation_history = []  # Stores all previous user and assistant messages

print("🤖 Mock ChatGPT Assistant (with Memory)")
print("Type 'exit' to end the chat.")
print("--------------------------------------------------")

# --- Continuous chat loop ---
while True:
    user_input = input("🧑 You: ")

    # Exit condition
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("👋 Assistant: Goodbye! Talk soon.")
        break

    # Store the user's message
    conversation_history.append({"role": "user", "content": user_input})

    # Generate a simulated response based on the conversation so far
    assistant_reply = mock_ai_response(user_input, conversation_history)

    # Store assistant's reply for memory continuity
    conversation_history.append({"role": "assistant", "content": assistant_reply})

    # Display the AI response
    print(f"🤖 Assistant: {assistant_reply}")
