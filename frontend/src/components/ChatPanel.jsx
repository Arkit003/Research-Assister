import React, { useState, useRef, useEffect } from "react";
import ChatMessage from "./ChatMessage";


const SendIcon = () => (
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
);

export default function ChatPanel() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([
    { role: "assistant", content: "Hello! I've indexed your document. Ask me anything." }
  ]);
  const [isLoading, setIsLoading] = useState(false);

  const messagesEndRef = useRef(null);
  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };
  useEffect(scrollToBottom, [messages, isLoading]);


  const handleSubmit = async () => {
    if (!input.trim()) return;

    
    const userMessage = { role: "user", content: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setIsLoading(true);

    try {
  const response = await fetch("http://localhost:8000/chat/query", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      query: input,
    }),
  });

  if (!response.ok) {
    throw new Error(`Server error: ${response.status}`);
  }

  const data = await response.json();

  
  const aiResponse = {
    role: "assistant",
    content: data.answer,
  };

  setMessages((prev) => [...prev, aiResponse]);

} catch (error) {
  console.error(error);
  setMessages((prev) => [
    ...prev,
    {
      role: "assistant",
      content: "⚠️ Unable to reach the backend. Please try again.",
    },
  ]);
} finally {
  setIsLoading(false);
}
  };


  const handleKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSubmit();
    }
  };

  return (
    <>
      <div className="chat-messages">
        {messages.map((msg, index) => (
          <ChatMessage key={index} message={msg} />
        ))}

        {/* Typing Indicator Bubble */}
        {isLoading && (
          <div className="message-wrapper assistant">
            <div className="avatar ai">
               <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2"><path d="M12 2a2 2 0 0 1 2 2v2a2 2 0 0 1-2 2 2 2 0 0 1-2-2V4a2 2 0 0 1 2-2Z"/><path d="m8 6 4-4 4 4"/><path d="M12 14a5 5 0 0 0-5 5v2a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1v-2a5 5 0 0 0-5-5Z"/></svg>
            </div>
            <div className="bubble ai">
              <div className="typing-dot"></div>
              <div className="typing-dot"></div>
              <div className="typing-dot"></div>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      <div className="chat-input-container">
        <div className="input-wrapper">
          <textarea
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Ask a question about the document..."
            rows={1}
          />
          <button 
            className="send-button" 
            onClick={handleSubmit} 
            disabled={isLoading || !input.trim()}
          >
            <SendIcon />
          </button>
        </div>
      </div>
    </>
  );
}