import cohere
from cohere.classify import Example

COHERE_TOKEN = ''
with open("coheretoken.txt", 'r') as file:
    COHERE_TOKEN = file.read().strip()

co = cohere.Client(COHERE_TOKEN)
print (COHERE_TOKEN)

examples=[Example("kys", "Toxic"),
         Example("gg ez", "Toxic"),
         Example("family guy", "Not Toxic"),
         Example("Family Man", "Not Toxic")]

# TODO: Implement this
def isToxic(text):
    response = co.classify(model='f6661bd3-106c-470a-ac3f-3a6b1eec4a7b-ft', inputs=[text], examples=examples)
    print(response.classifications[0].labels['Toxic'].confidence)
    if response.classifications[0].labels['Toxic'].confidence > 0.70:
        return True
    return False