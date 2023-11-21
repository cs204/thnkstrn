def convert(text: str) -> str:
        text = text.replace(":)", "🙂")
        text = text.replace(":(", "🙁")
        return text

def main():
    i_text = input("")
    c_text = convert(i_text)
    print(c_text)

main()