import { useState } from "react";
import { FaPaperPlane, FaPaperclip } from "react-icons/fa";

function InputBox({ setMessages }) {
  const [prompt, setPrompt] = useState("");

  const handleSubmit = async () => {
    if (!prompt.trim()) return;

    const userPrompt = prompt;

    // Show user message immediately
    setMessages((prev) => [
      ...prev,
      {
        role: "user",
        content: userPrompt,
      },
    ]);

    // Clear input
    setPrompt("");

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/api/v1/assistant/",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            prompt: userPrompt,
          }),
        }
      );

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}`);
      }

      const data = await response.json();

      console.log("Backend Response:", data);

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: data.response,
        },
      ]);
    } catch (error) {
      console.error(error);

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: `❌ ${error.message}`,
        },
      ]);
    }
  };

  return (
    <div className="border-t border-gray-700 bg-[#202123] p-5">
      <div className="max-w-5xl mx-auto">

        <div className="flex items-center bg-[#2F2F2F] rounded-2xl px-4 py-3">

          <button className="text-gray-400 mr-3">
            <FaPaperclip />
          </button>

          <input
            type="text"
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                handleSubmit();
              }
            }}
            placeholder="Ask DevPilot AI anything..."
            className="flex-1 bg-transparent outline-none text-white"
          />

          <button
            onClick={handleSubmit}
            className="bg-green-500 hover:bg-green-600 text-white rounded-full p-3 ml-3 transition"
          >
            <FaPaperPlane />
          </button>

        </div>

      </div>
    </div>
  );
}

export default InputBox;