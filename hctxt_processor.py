import re


patterns_dict = {
    "clear": r'\B<#no_format>\B{0, }\B</#no_format>\B'
}


def clear_format(text):
    # re.sub(pattern, repl, string, count=0)
    result = re.search(patterns_dict["clear"],
                    text)
    print(result)


def process_text(text):
    pass


if __name__ == "__main__":
    clear_format("gftfd<#no_format>sdsjd</#no_format>")
