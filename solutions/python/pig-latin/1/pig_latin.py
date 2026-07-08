def translate(text):
    text = text.strip()
    text = text.split()
    translated_words = []
    for j in text:
        end_text = ""
        if j[0] in "aeiou" or j[0:2] in ["xr","yt"]:
            translated_words.append(j + "ay")
        elif j[0] == "y":
            translated_words.append(j[1:] +"yay")
        else:
            i = 0 
            while i < len(j) and j[i] not in "aeiou" and j[i] not in "y" and j[i:i+2] != "qu":
                end_text += j[i]
                i += 1 
            if j[i:i+2] == "qu":

                sum = int(len(end_text)) + 2 
                translated_words.append( j[sum :] + end_text +"quay")
            else:
        
               translated_words.append(j[len(end_text):] + end_text + "ay" )
    
    return " ".join(translated_words)

