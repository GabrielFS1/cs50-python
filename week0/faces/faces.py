def main():
    # Gets user input
    txt = input()

    #convert emojis
    converted_txt = convert(txt)

    print(converted_txt)

def convert(msg: str):
    msg = msg.replace(":)", "🙂")
    msg = msg.replace(":(", "🙁")
    return msg

main()