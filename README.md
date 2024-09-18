# Stack and Queue Interface Application

This is a simple GUI application built using Python's `tkinter` library to visually interact with a **Stack** and **Queue**. The app allows users to perform basic operations like pushing and popping elements from a stack, as well as enqueuing and dequeuing elements from a queue. Additionally, it provides an output section to display the results of operations and a text output section for additional feedback or logs.

## Features

- **Stack Operations**:
  - Push elements onto the stack.
  - Pop elements off the stack.
  - View the current state of the stack.

- **Queue Operations**:
  - Enqueue elements to the queue.
  - Dequeue elements from the queue.
  - View the current state of the queue.

- **Output Display**:
  - Displays feedback messages, such as success, errors (e.g., "Stack is empty"), and other operation results.

- **Text Output Section**:
  - Separate section to display additional text-based logs or information.

## Installation

To run this application, you need to have Python installed along with the `tkinter` library (which is usually included with most Python distributions).

1. Clone the repository or download the source code.
   ```bash
   git clone https://github.com/pestopasta74/Stack-and-Queue-demonsration.git
   cd stack-queue-app
   ```

2. Run the application:
   ```bash
   python main.py
   ```

## How to Use

1. **Stack Operations**:
   - Input a value in the "Stack" section and click **Push** to add the value to the stack.
   - Click **Pop** to remove the last added value from the stack.
   - The stack's current state will be displayed in the list box below the buttons.

2. **Queue Operations**:
   - Input a value in the "Queue" section and click **Enqueue** to add the value to the queue.
   - Click **Dequeue** to remove the first value from the queue.
   - The queue's current state will be displayed in the list box below the buttons.

3. **Output Section**:
   - After performing any operation, the output (success/error message) will be displayed in the **Output** text box.

4. **Text Output Section**:
   - The **Text Output** box can be used to show additional information or logs based on operations.

## Example Use Case

- Enter "5" in the Stack section and click **Push**. You will see "5" added to the stack list box and a message like "Pushed to stack: 5" in the Output box.
- Similarly, enter "10" in the Queue section and click **Enqueue** to see it added to the queue.

## Project Structure

```
Stack-and-Queue-demonsration/
│
├── main.py              # Main application file
├── README.md            # Documentation
└── LICENCE              # Licence
```

## Future Improvements

- Add more data structures like deque, priority queue, etc.
- Include validation for data types (e.g., integers only).
- Enhance the UI with themes and better aesthetics.
- Add undo/redo functionality for operations.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Enjoy using the Stack and Queue Interface Application! Feel free to contribute or suggest new features.