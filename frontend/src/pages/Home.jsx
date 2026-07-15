import Navbar from "../components/layout/Navbar";
import Sidebar from "../components/layout/Sidebar";
import ChatWindow from "../components/chat/ChatWindow";
import InputBox from "../components/chat/InputBox";

function Home() {
  return (
    <div
      style={{
        display: "flex",
        height: "100vh",
        background: "#202123",
        color: "white",
      }}
    >
      <Sidebar />

      <div
        style={{
          flex: 1,
          display: "flex",
          flexDirection: "column",
        }}
      >
        <Navbar />
        <ChatWindow />
        <InputBox />
      </div>
    </div>
  );
}

export default Home;