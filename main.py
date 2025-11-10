# ChatGPT Prompt Assistant (Offline Mock Version with Memory)

import random  # Import the built-in module for generating random choices

# ============================================================
# Mock AI Response Generator (Simulated ChatGPT Behavior)
# ============================================================

def mock_ai_response(user_input, conversation_history): # Defines a function named mock_ai_response that takes: user_input -> the latest message from the user, conversation_history -> a list of all previous messages exchanged
    """
    Generates a mock ChatGPT-like response.
    Uses the last few user messages as context to simulate memory.
    """

    # Extract the last 3 user messages from the conversation history
    user_messages = [msg["content"] for msg in conversation_history if msg["role"] == "user"] # Filters the conversation history to extract only the messages sent by the user
    context = " | ".join(user_messages[-3:])  # Combine last messages to simulate memory # Joins the last 3 user messages into a single string, separated by " | ", to simulate short-term memory

    # Rule-based simulated responses 
    # If the user says "hello" (case-insensitive), return a friendly greeting
    if "hello" in user_input.lower():
        return "Hello there! 👋 How are you feeling today?"
    
    # If the user mentions "name", respond with a playful answer about not having a name
    elif "name" in user_input.lower():
        return "I don’t really have a name yet — maybe you could give me one? 😊"
    
    # If "project" is mentioned, assume the user is talking about an AI-related project
    elif "project" in user_input.lower():
        return "Are you referring to your AI project? It sounds exciting!"
    
    # If the user says "remember", the assistant recalls the last few messages
    elif "remember" in user_input.lower():
        return f"Of course! You mentioned earlier: '{context}'."
    
    # If no keyword matches, choose a generic response that references the recent context
    else:
        # Generic memory-based replies
        generic_replies = [
            f"Interesting point about '{user_input}'. Based on what we discussed — {context}.",
            f"Hmm, I see your point about '{user_input}'. Earlier you mentioned {context}.",
            f"Let's connect this with what you said before: {context}.",
            f"That’s a nice continuation of our earlier chat about {context}.",
            f"Could you explain a bit more about '{user_input}'?"
        ]
        return random.choice(generic_replies)  # Return a random generic reply # random.choice(): randomly selects one of the five predefined replies

# ============================================================
# 💬 Conversation Loop (User ↔ Assistant)
# ============================================================
conversation_history = []  # Initializes an empty list to store all previous full conversation between user and assistant messages

# Displays a welcome message and instructions to the user
print("🤖 Mock ChatGPT Assistant (with Memory)")
print("Type 'exit' to end the chat.")
print("--------------------------------------------------")

# Continuous chat loop
# Starts an infinite loop to keep the conversation going 
# Prompts the user for input
while True:
    user_input = input("🧑 You: ")  # Get user input

    # Exit condition
    # If the user types "exit", "quit", or "bye", the assistant says goodbye and breaks the loop
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("👋 Assistant: Goodbye! Talk soon.")
        break  # Exit the loop

    # Store the user's message -> adds the user's message to the conversation history
    conversation_history.append({"role": "user", "content": user_input})

    # Calls the response function to generate a reply based on the current input and history
    assistant_reply = mock_ai_response(user_input, conversation_history)

    # Store assistant's reply to the conversation history and for memory continuity 
    conversation_history.append({"role": "assistant", "content": assistant_reply})

    # Display the assistant’s response to the user
    print(f"🤖 Assistant: {assistant_reply}")
