from secrets import OPENAI_API_KEY
import openai

openai.api_key = OPENAI_API_KEY

SAMPLE_PROMPT = 'Give me a recommendation for 10 things to do in Honolulu'

response = openai.Completion.create(
  engine="text-davinci-003",  # or whatever the current top engine is
  prompt=SAMPLE_PROMPT,
  max_tokens=50
)

print(response.choices[0].text.strip())