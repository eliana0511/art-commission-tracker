# 🎨 Art Commission Tracker
# Author: Ally
# Description: Manage art commissions using both a queue (waiting) and a stack (completed).
# Demonstrates FIFO + LIFO behavior in a creative way.

from collections import deque

def show_menu():
    print("\n🎨 ART COMMISSION TRACKER")
    print("1. Add new commission")
    print("2. Complete next commission")
    print("3. Undo last completed commission")
    print("4. View commissions")
    print("5. Exit")

def add_commission(queue):
    name = input("Enter client's name: ")
    description = input("Enter commission description: ")
    queue.append({"client": name, "description": description})
    print(f"🖌️ Commission from {name} added to waiting list!")

def complete_commission(queue, stack):
    if not queue:
        print("No commissions waiting! ✨")
        return
    completed = queue.popleft()
    stack.append(completed)
    print(f"✅ Completed commission for {completed['client']}!")

def undo_last(stack, queue):
    if not stack:
        print("No completed commissions to undo!")
        return
    undone = stack.pop()
    queue.appendleft(undone)
    print(f"↩️ Moved {undone['client']}'s commission back to waiting list.")

def view_commissions(queue, stack):
    print("\n📋 Waiting Commissions:")
    if not queue:
        print("None waiting.")
    else:
        for i, c in enumerate(queue, 1):
            print(f"{i}. {c['client']} - {c['description']}")

    print("\n🎨 Completed Commissions:")
    if not stack:
        print("None completed yet.")
    else:
        for i, c in enumerate(reversed(stack), 1):
            print(f"{i}. {c['client']} - {c['description']}")

def main():
    queue = deque()  # FIFO for waiting commissions
    stack = []       # LIFO for completed commissions

    while True:
        show_menu()
        choice = input("Enter choice (1-5): ")

        if choice == "1":
            add_commission(queue)
        elif choice == "2":
            complete_commission(queue, stack)
        elif choice == "3":
            undo_last(stack, queue)
        elif choice == "4":
            view_commissions(queue, stack)
        elif choice == "5":
            print("\n👋 Goodbye! Keep creating beautiful art 💕")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
