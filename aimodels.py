# import requests
# import pdfToTxtConverter
# import listofChannels


# # API_URL = "https://api-inference.huggingface.co/models/microsoft/Phi-3-mini-4k-instruct"
# # headers = {"Authorization": "Bearer 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"}
#
#
# def userClassification(filepath):
#     def combine_resume_text(text):
#         """Remove extra line breaks and leading/trailing whitespaces"""
#         paragraphs = [line.strip() for line in text.splitlines() if line.strip()]
#         return " ".join(paragraphs)
#
#     # print(combine_resume_text(pdfToTxtConverter.readPdf(filepath)))
#
#     # def query(payload):
#     #     response = requests.post(API_URL, headers=headers, json=payload)
#     #     return response.json()
#     #
#     # output = query({
#     #     "inputs": f" classify this resume {combine_resume_text(pdfToTxtConverter.readPdf(filepath))} based on one or more of these classes {listofChannels}",
#     # })
#     #
#     # return output
#
#     # print(userClassification("./test.pdf"))


import requests

API_URL = "https://api-inference.huggingface.co/models/unsloth/llama-3-8b-Instruct-bnb-4bit"
headers = {"Authorization": "Bearer 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"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


output = query({
    "inputs": "Can you please let us know more details about your ",
})

print(output)

