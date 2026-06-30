def clean_text(text):
    return text.strip().lower()
def replace(text2):
    text2= text2.replace("bad", "Good")
    text2= text2.replace("nice", "Nachiket")
    return text2
    

print(replace(" you ARE bad guy,  nice   da "))