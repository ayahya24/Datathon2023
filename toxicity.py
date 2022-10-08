import cohere

COHERE_TOKEN = ''
with open("coheretoken.txt", 'r') as file:
    COHERE_TOKEN = file.read().strip()

co = cohere.Client(COHERE_TOKEN)

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
    response = co.classify(model='cohere-toxicity', inputs=[text])
    print(response.classifications[0].labels['TOXIC'].confidence)
    if response.classifications[0].labels['TOXIC'].confidence > 0.70:
        return True
    return False