import time
import aiml
time.clock = time.time # AIML uses time.clock but is deprecated, not the best patch but works.

def main():
    chatbot = aiml.Kernel()
    chatbot.verbose(True)

    # AIML Files - Uncomment as required.
    # chatbot.learn("data/workbook2.aiml")
    # chatbot.learn("data/hello.aiml")

    print(f"Loaded {chatbot.numCategories()} categories.")
    print("\nType \"exit\" to quit. ")
    while True:
        next_input = input("Enter Message: ")
        if next_input == "exit":
            exit(0)
        else:
            print(chatbot.respond(next_input))
            time.sleep(0.1)


if __name__ == '__main__':
    main()
