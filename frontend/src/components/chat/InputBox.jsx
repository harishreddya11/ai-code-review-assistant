function InputBox() {
  return (
    <div
      style={{
        padding: 20,
        borderTop: "1px solid #333",
      }}
    >
      <input
        type="text"
        placeholder="Ask anything..."
        style={{
          width: "100%",
          padding: 14,
          borderRadius: 10,
        }}
      />
    </div>
  );
}

export default InputBox;