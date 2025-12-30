<h1>🤖 AI Agent (Gemini) – Configurable Tool-Using Agent Framework</h1>

<p>
This project is a <b>configurable AI agent framework</b> built with Google Gemini.
The agent can reason, plan actions, call tools, observe results, and iterate until a task is complete.
By changing the system prompt, the same agent can act as a coding assistant, documentation generator,
analysis tool, or general-purpose automation agent.
</p>

<p>
The repository includes a <b>calculator CLI application</b> used as a realistic example workload
that the agent can inspect, run, modify, and verify.
</p>

<hr/>

<h2>👨‍💻 Project Overview</h2>

<ul>
  <li>Implements a multi-step AI agent loop with iteration limits</li>
  <li>Supports function/tool calling (read files, write files, execute Python)</li>
  <li>Maintains full conversation and tool history across iterations</li>
  <li>Behavior is fully controlled by the system prompt</li>
  <li>Can operate as a coding agent, analysis agent, or documentation agent</li>
  <li>Demonstrated on a real Python calculator application</li>
</ul>

<hr/>

<h2>📂 Project Structure</h2>

<pre>
AI_AGENT_GEMINI/
├── calculator/
│   ├── main.py
│   └── pkg/
│       ├── calculator.py
│       ├── render.py
│       └── tests.py
│
├── functions/
│   ├── get_file_content.py
│   ├── get_files_info.py
│   ├── run_python_file.py
│   └── write_files.py
│
├── call_function.py
├── config.py
├── prompts.py
├── main.py
├── pyproject.toml
├── uv.lock
└── README.md
</pre>

<hr/>

<h2>⚙️ Core Components</h2>

<ul>
  <li><b>main.py</b><br/>
    Entry point for the AI agent. Manages the agent loop, calls the Gemini model,
    executes requested tools, and feeds results back to the model.
  </li>
  <br/>
  <li><b>prompts.py</b><br/>
    Defines the system prompt. Changing this file changes the agent’s role and behavior
    without modifying the core logic.
  </li>
  <br/>
  <li><b>call_function.py</b><br/>
    Dispatches tool calls requested by the model to their corresponding Python implementations.
  </li>
  <br/>
  <li><b>functions/</b><br/>
    Tool implementations available to the agent:
    <ul>
      <li>List files and directories</li>
      <li>Read file contents</li>
      <li>Write or overwrite files</li>
      <li>Execute Python programs with arguments</li>
    </ul>
  </li>
  <br/>
  <li><b>calculator/</b><br/>
    A standalone CLI calculator application used to demonstrate agent capabilities.
  </li>
</ul>

<hr/>

<h2>🧮 Calculator Application</h2>

<p>
The calculator evaluates infix mathematical expressions with correct operator precedence
and outputs results as structured JSON.
</p>

<p><b>Example:</b></p>

<pre>
uv run calculator/main.py "3 + 7 * 2"
</pre>

<pre>
{
  "expression": "3 + 7 * 2",
  "result": 17
}
</pre>

<p>
Structured JSON output allows the agent to reliably verify correctness after modifications.
</p>

<hr/>

<h2>🚀 How to Run</h2>

<h3>Requirements</h3>

<ul>
  <li>Python 3.9+</li>
  <li><a href="https://github.com/astral-sh/uv">uv</a></li>
</ul>

<h3>Install Dependencies</h3>

<pre>
uv sync
</pre>

<h3>Run the Calculator Directly</h3>

<pre>
uv run calculator/main.py "10 / 2 + 3"
</pre>

<h3>Run the AI Agent</h3>

<pre>
uv run main.py "Fix the calculator so that operator precedence is handled correctly."
</pre>

<p>
Depending on the system prompt, the agent may:
</p>

<ul>
  <li>Inspect files</li>
  <li>Analyze code or content</li>
  <li>Modify files</li>
  <li>Execute programs</li>
  <li>Provide explanations or documentation</li>
</ul>

<hr/>

<h2>🧠 Example Agent Capabilities</h2>

<ul>
  <li>Code analysis and refactoring</li>
  <li>Bug detection and correction</li>
  <li>Project documentation generation</li>
  <li>File inspection and reporting</li>
  <li>Automated verification via program execution</li>
</ul>

<hr/>

<h2>🎯 Learning Objectives</h2>

<ul>
  <li>Agent loops and iterative reasoning</li>
  <li>Tool/function calling with LLMs</li>
  <li>Maintaining conversational state</li>
  <li>Safe file access and execution</li>
  <li>Prompt-driven agent behavior</li>
</ul>

<hr/>

<h2>📝 Notes</h2>

<ul>
  <li>The agent is sandboxed to the working directory</li>
  <li>All file paths are relative and validated</li>
  <li>Iteration limits prevent runaway token usage</li>
  <li>Changing the system prompt changes the agent’s role</li>
</ul>

<hr/>

<h2>👤 Author</h2>

<p>
<b>GitHub:</b> <a href="https://github.com/lotsueugene">lotsueugene</a>
</p>
