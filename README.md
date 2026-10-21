# QA Automation Traineeship Test Task (Python)

This project was completed as part of a test task for the QA Automation traineeship.

## Answers to Questions (Task 2)

**Given bracket sequence:** `[(((())()(()]]`

1. **Can this sequence be considered valid?**
   * **Answer:** No, this sequence cannot be considered valid.
   * **Reason:** The validity of the bracket structure is violated. It starts with an opening square bracket `[`, but ends with two closing square brackets `]]` without a second opening bracket. In addition, the balance and pairing of the inner round parentheses are violated.

2. **What needs to be changed in the sequence to make it valid?**
   * **Answer:** To make the sequence valid, you need to balance the opening and closing brackets of the same type.
   * **Fix options:**
     1. If converting the entire sequence to a valid form using round parentheses: `((((())()(()))))`
     2. If keeping the outer square brackets and balancing the inner round parentheses: `[((())()(()))]`

---

## Running the Program

Python 3.x is required to run the script.

Command to run:
```bash
python main.py
