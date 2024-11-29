import emoji

def emojize_text(text):
  return emoji.emojize(text, language='alias')

text = input("Enter your text with emojis: ")
result = emojize_text(text)
print(result)
