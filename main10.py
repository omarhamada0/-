all_tasks = input("Enter your tasks for today separated by a comma:\n").split(", ")
complete = []
incomplete = []
for task in all_tasks:
    print(f"\n{task}\n")
    finished_tasks = input(f"Did you finish {task} already? ('yes' or 'no'): ").lower()
    if finished_tasks == "yes":
        complete.append(task)
        print("Nice job")
    elif finished_tasks == "no":
        incomplete.append(task)
        print("Try not to put it off")
    else:
        print("Please write ('yes' or 'no')")
    print("-------------")
progress = input("Do you want to see your today's progress? (yes , no)\n")
if progress.lower() == "yes":
    print("\n     ******* Done Tasks *******     ")
    print(complete)
    print("\n     ****** Ongoing Tasks ******     ")
    print(incomplete)