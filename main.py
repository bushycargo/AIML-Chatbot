import time, requests, aiml, json

time.clock = time.time  # AIML uses time.clock, but it is deprecated, not the best patch but works.


def main():

    print(definition_api("door","noun"))
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


def definition_api(word, type):
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    if response.status_code == 200:
        data = response.json()
        for entry in data:
            for meaning in entry['meanings']:
                part_of_speech = meaning['partOfSpeech']
                definition = meaning['definitions'][0]['definition']
                if part_of_speech == type:
                    return definition
                else:
                    continue
        return None
    else:
        return None

if __name__ == '__main__':
    main()
