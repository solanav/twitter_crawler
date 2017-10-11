import requests

user = input("USER >>> ")
main = requests.get("https://twitter.com/" + user)
source = main.text
s0_source = source.split('<div class="js-tweet-text-container">')

def linkclean(splitt):
    split0 = splitt.split("\"")
    try:
        split1 = split0.split("/")
        print(split1[0])
        return split0[1]
    except:
        return split0[1]

def clear_link(raw_text):
    try:
        split0 = raw_text.split("<a")
        split1 = split0[1].split("</a>")
        final_text = split0[0] + split1[1]
        link = linkclean(split1[0])
        if link.split("/")[1] == "hashtag":
            link_split = link.split("/")[2].split("?")[0]
            return final_text + " #" + link_split
        else:
            if list(link)[0] == "/":
                return final_text + " @" + link.split("/")[1]
            else:
                return final_text + " " + link
            
    except:
        return raw_text

def clear_img(raw_text):
    try:
        split0 = raw_text.split("<img")
        return split0[0]
    except:
        return raw_text

def clear_quotes(raw_text):
    try:
        split0 = raw_text.split("&quot;")
        return "\"".join(split0)
    except:
        return raw_text

for x in range(1, len(s0_source)):
    s1_source = s0_source[x].split(">")
    s1_source.pop(0)
    s10_source = ">".join(s1_source)
    s2_source = s10_source.split("</p")

    print("_______________________________________________\n")
    print(clear_quotes(clear_img(clear_link(s2_source[0]))))

print("_______________________________________________\n")
print("\n")
    