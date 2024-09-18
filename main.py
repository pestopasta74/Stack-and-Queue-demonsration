import tkinter as tk

class Collection:
    def __init__(self, max_size):
        self.items = []
        self.max_size = max_size

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) >= self.max_size

    def list_items(self):
        return self.items

class Stack(Collection):
    def push(self, item):
        if not self.is_full():
            self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

class Queue(Collection):
    def enqueue(self, item):
        if not self.is_full():
            self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def peek(self):
        if not self.is_empty():
            return self.items[0]

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Stack and Queue Interface")
        self.geometry("540x560")
        self.resizable(False, False)


        self.stack = Stack(10)
        self.queue = Queue(10)

        self.create_widgets()

    def create_widgets(self):
        # Main Frame
        main_frame = tk.Frame(self)
        main_frame.pack(pady=10, padx=10, fill="both", expand=True)

        # Stack Section
        stack_frame = tk.LabelFrame(main_frame, text="Stack", padx=10, pady=10)
        stack_frame.grid(row=0, column=0, padx=20, pady=10)

        self.stack_entry = tk.Entry(stack_frame)
        self.stack_entry.pack(pady=5)

        self.stack_push_button = tk.Button(stack_frame, text="Push", command=self.push_stack)
        self.stack_push_button.pack(pady=5)

        self.stack_pop_button = tk.Button(stack_frame, text="Pop", command=self.pop_stack)
        self.stack_pop_button.pack(pady=5)

        self.stack_listbox = tk.Listbox(stack_frame, height=10, width=20)
        self.stack_listbox.pack(pady=10)

        # Queue Section
        queue_frame = tk.LabelFrame(main_frame, text="Queue", padx=10, pady=10)
        queue_frame.grid(row=0, column=1, padx=20, pady=10)

        self.queue_entry = tk.Entry(queue_frame)
        self.queue_entry.pack(pady=5)

        self.queue_enqueue_button = tk.Button(queue_frame, text="Enqueue", command=self.enqueue_queue)
        self.queue_enqueue_button.pack(pady=5)

        self.queue_dequeue_button = tk.Button(queue_frame, text="Dequeue", command=self.dequeue_queue)
        self.queue_dequeue_button.pack(pady=5)

        self.queue_listbox = tk.Listbox(queue_frame, height=10, width=20)
        self.queue_listbox.pack(pady=10)

        # Output Section
        output_frame = tk.Frame(main_frame)
        output_frame.grid(row=1, column=0, columnspan=2, pady=10)

        self.output_label = tk.Label(output_frame, text="Output:")
        self.output_label.pack(anchor="w")

        self.output_box = tk.Text(output_frame, height=5, width=50, state=tk.DISABLED, wrap=tk.WORD)
        self.output_box.pack(pady=5)

    def push_stack(self):
        item = self.stack_entry.get().strip()
        if item and not self.stack.is_full():
            self.stack.push(item)
            self.update_stack_listbox()
            self.show_output(f"Pushed to stack: {item}")
        elif not item:
            self.show_output("Error: Please enter a valid item.")
        else:
            self.show_output("Error: Stack is full.")

    def pop_stack(self):
        if not self.stack.is_empty():
            item = self.stack.pop()
            self.update_stack_listbox()
            self.show_output(f"Popped from stack: {item}")
        else:
            self.show_output("Error: Stack is empty.")

    def enqueue_queue(self):
        item = self.queue_entry.get().strip()
        if item and not self.queue.is_full():
            self.queue.enqueue(item)
            self.update_queue_listbox()
            self.show_output(f"Enqueued to queue: {item}")
        elif not item:
            self.show_output("Error: Please enter a valid item.")
        else:
            self.show_output("Error: Queue is full.")

    def dequeue_queue(self):
        if not self.queue.is_empty():
            item = self.queue.dequeue()
            self.update_queue_listbox()
            self.show_output(f"Dequeued from queue: {item}")
        else:
            self.show_output("Error: Queue is empty.")

    def update_stack_listbox(self):
        self.stack_listbox.delete(0, tk.END)
        for item in self.stack.list_items():
            self.stack_listbox.insert(tk.END, item)

    def update_queue_listbox(self):
        self.queue_listbox.delete(0, tk.END)
        for item in self.queue.list_items():
            self.queue_listbox.insert(tk.END, item)

    def show_output(self, message):
        self.output_box.config(state=tk.NORMAL)
        self.output_box.delete(1.0, tk.END)  # Clear previous messages
        self.output_box.insert(tk.END, message)
        self.output_box.config(state=tk.DISABLED)

if __name__ == "__main__":
    app = App()
    app.mainloop()
