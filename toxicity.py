import cohere

COHERE_TOKEN = ''
with open("coheretoken.txt", 'r') as file:
    COHERE_TOKEN = file.read().strip()

co = cohere.Client(COHERE_TOKEN)
print (COHERE_TOKEN)
'''
test = [
    "Hi its nice to meet you!",
    "You should kill yourself NOW!"
]
response = co.classify(
    model = 'cohere-toxicity',
    inputs = test)

print(response.classifications)
'''
# TODO: Implement this
def isToxic(text):
    response = co.classify(model='f6661bd3-106c-470a-ac3f-3a6b1eec4a7b-ft', inputs=[text])
    print(response.classifications[0].labels['Toxic'].confidence)
    if response.classifications[0].labels['Toxic'].confidence > 0.70:
        return True
    return False