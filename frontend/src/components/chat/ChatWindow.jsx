function ChatWindow({ messages = [] }) {
  return (
    <div className="flex-1 overflow-y-auto bg-[#202123] text-white px-6 py-6">

      {messages.length === 0 ? (
        <div className="flex flex-col items-center justify-center h-full">

          <h1 className="text-5xl font-bold mb-4">
            👋 Welcome to DevPilot AI
          </h1>

          <p className="text-gray-400 text-lg text-center max-w-2xl">
            Ask anything about programming, debugging, interview preparation,
            system design, SQL, Python, Java, React, FastAPI, resume writing,
            or any technical topic.
          </p>

        </div>
      ) : (
        <div className="max-w-5xl mx-auto">

          {messages.map((message, index) => (
            <div
              key={index}
              className={`flex mb-6 ${
                message.role === "user"
                  ? "justify-end"
                  : "justify-start"
              }`}
            >

              <div
                className={`rounded-2xl px-5 py-4 max-w-4xl shadow-md ${
                  message.role === "user"
                    ? "bg-green-600"
                    : "bg-[#2F2F2F]"
                }`}
              >

                <div className="font-semibold mb-3">
                  {message.role === "user"
                    ? "👤 You"
                    : "🤖 DevPilot AI"}
                </div>

                <pre className="whitespace-pre-wrap break-words font-sans">
                  {message.content}
                </pre>

              </div>

            </div>
          ))}

        </div>
      )}

    </div>
  );
}

export default ChatWindow;