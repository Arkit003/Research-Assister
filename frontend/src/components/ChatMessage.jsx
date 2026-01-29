import React from "react";

const UserIcon = () => (
  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
);

const BotIcon = () => (
  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M12 2a2 2 0 0 1 2 2v2a2 2 0 0 1-2 2 2 2 0 0 1-2-2V4a2 2 0 0 1 2-2Z"/><path d="m8 6 4-4 4 4"/><path d="M12 14a5 5 0 0 0-5 5v2a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1v-2a5 5 0 0 0-5-5Z"/></svg>
);

export default function ChatMessage({ message }) {
  const isUser = message.role === "user";

  return (
    <div className={`message-wrapper ${isUser ? "user" : "assistant"}`}>
      {/* Avatar Section */}
      <div className={`avatar ${isUser ? "user" : "ai"}`}>
        {isUser ? <UserIcon /> : <BotIcon />}
      </div>

      {/* Message Bubble Section */}
      <div className={`bubble ${isUser ? "user" : "ai"}`}>
        {message.content}
      </div>
    </div>
  );
}