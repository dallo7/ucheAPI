import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers = {"Authorization": "Bearer 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"}


def summerize(usertext):
    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    output = query({
        "inputs": f" summerize the text in quotation using points, separate each point with a comma. '{usertext}'."
    })

    return output[0]["summary_text"]


def format_to_points(text):
    points = [f"* {sentence.strip()}" for sentence in text.split(".")]
    return "\n".join(points)

#
# print(summerize("dallo is a good boy bu he is sick with love"))
                    
                      
                      
                      
  

