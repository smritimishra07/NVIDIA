from openai import OpenAI

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "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"
)

completion = client.chat.completions.create( 
  model="meta/llama3-70b-instruct",
  messages=[{"role":"user","content":"Provide me an article on machine learning"}],
  temperature=0.5,
  top_p=1,
  max_tokens=1024,
  stream=True
)

for chunk in completion:
  if chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")

