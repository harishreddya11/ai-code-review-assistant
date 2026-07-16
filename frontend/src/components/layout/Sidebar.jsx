import { FaPlus, FaComments, FaCog, FaRobot } from "react-icons/fa";

function Sidebar() {
  const chats = [
    "Python REST API",
    "SQL Optimization",
    "React Login Page",
  ];

  return (
    <div className="w-72 bg-[#171717] text-white flex flex-col border-r border-gray-800">

      <div className="p-5 text-2xl font-bold flex items-center gap-3">
        <FaRobot className="text-green-400" />
        DevPilot AI
      </div>

      <div className="px-4">
        <button className="w-full bg-[#2f2f2f] hover:bg-[#404040] rounded-xl py-3 transition">
          <FaPlus className="inline mr-2" />
          New Chat
        </button>
      </div>

      <div className="flex-1 overflow-y-auto mt-6 px-3">

        <p className="text-xs text-gray-400 mb-3 uppercase">
          Today
        </p>

        {chats.map((chat, index) => (
          <button
            key={index}
            className="w-full flex items-center gap-3 rounded-lg px-3 py-3 hover:bg-[#2a2a2a] transition text-left"
          >
            <FaComments size={14} />
            <span className="truncate">{chat}</span>
          </button>
        ))}

      </div>

      <div className="border-t border-gray-800 p-4">
        <button className="flex items-center gap-3 hover:text-green-400">
          <FaCog />
          Settings
        </button>
      </div>

    </div>
  );
}

export default Sidebar;