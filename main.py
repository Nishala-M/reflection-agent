
MAX_RETRIES = 3


def generate_solution(task, attempt):
    if attempt == 1:
        # Deliberately create a weak first answer for demonstration
        return f"Python is useful for {task}."

    # Produce a more complete answer on later attempts
    return (
        f"Python can help with {task}. "
        "It provides simple syntax and useful libraries. "
        "Developers can use it to automate tasks and solve problems."
    )


def critic_evaluate(solution):
    words = solution.split()

    if len(words) < 15:
        return "Revise", "The solution is too short."

    return "Pass", "The solution has enough detail."


def reflection_agent(task):
    for attempt in range(1, MAX_RETRIES + 1):
        print(f"\nAttempt {attempt} of {MAX_RETRIES}")

        solution = generate_solution(task, attempt)
        print("\nInitial solution:")
        print(solution)

        decision, reason = critic_evaluate(solution)

        print("\nCritic evaluation:", decision)
        print("Reason:", reason)

        if decision == "Pass":
            print("\nValidated result:")
            print(solution)
            return

        print("Reflection: Regenerating the solution...")

    print("\nRetry limit reached.")
    print("Could not produce a validated result.")


def main():
    print("=== Reflection Agent ===")

    task = input("Enter a task or topic: ").strip()

    if not task:
        print("Please enter a task.")
        return

    reflection_agent(task)


if __name__ == "__main__":
    main()
