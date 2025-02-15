import express from "express";
import ollama from "ollama";

const app = express();
const port = 3000;

// Middleware to parse JSON body
app.use(express.json());

// Endpoint to get the chat page
app.post("/chat", async (req, res) => {
  const userMessage = req.body.message;

  if (!userMessage) {
    return res.status(400).json({ error: "Message is required" });
  }

  const message = { role: "user", content: userMessage };

  try {
    const response = await ollama.chat({
      model: "deepseek-r1:1.5b",
      messages: [message],
      stream: true,
    });

    let fullResponse = "";
    for await (const part of response) {
      fullResponse += part.message.content;
    }

    res.json({ response: fullResponse });
  } catch (error) {
    console.error("Error communicating with Ollama:", error);
    res.status(500).json({ error: "Failed to communicate with Ollama" });
  }
});

// Initialize the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
