import { useState } from "react";
import Navbar from "../components/layout/Navbar";
import Sidebar from "../components/layout/Sidebar";
import ChatWindow from "../components/chat/ChatWindow";
import InputBox from "../components/chat/InputBox";

function Home() {
  const [messages, setMessages] = useState([]);

  return (
    <div className="flex h-screen bg-[#202123] text-white">
      <Sidebar />

      <div className="flex flex-1 flex-col">
        <Navbar />

        <ChatWindow messages={messages} />

        <InputBox
          messages={messages}
          setMessages={setMessages}
        />
      </div>
    </div>
  );
}

export default Home;