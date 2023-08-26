import os
import openai
from config import apikey

openai.api_key = apikey

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write a paragraph on clould computing.",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)
'''
{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "logprobs": null,
      "text": "Cloud computing refers to the delivery of on-demand computing services over the internet, allowing users to access and utilize a wide range of resources such as servers, storage, databases, software, and applications without having to invest in or manage physical infrastructure. This revolutionary technology has transformed the way businesses and individuals operate, enabling them to scale their operations efficiently, reduce costs, and increase flexibility. With cloud computing, users can store and access their data from anywhere at any time, collaborate seamlessly with team members, and leverage powerful computing capabilities without the constraints of local hardware. Furthermore, cloud computing facilitates the deployment and management of applications, allowing for rapid development and innovation. It has become an integral part of modern computing, empowering organizations to focus on their core competencies while leveraging the benefits of a scalable and reliable cloud infrastructure."
  ],
  "created": 1787423441,
  "id": "cmpl-7F1aqg7BkzIY8vBnCxYQh8Xp4wO85",
  "model": "text-davinci-003",
  "object": "text_completion",
  "usage": {
    "completion_tokens": 125,
    "prompt_tokens": 9,
    "total_tokens": 134
  }
}
'''
