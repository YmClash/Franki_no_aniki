import openai
import os


openai.api_key =
key =  os.environ["FRANKI_NO_ANIKI_API_KEY"]


print(key)


try :
    # Make your OpenAI API request here
    response = openai.Completion.create(model="text-davinci-003",
                                        prompt="Hello world")
except openai.error.Timeout as e :
    # Handle timeout error, e.g. retry or log
    print(f"OpenAI API request timed out: {e}")
    pass
except openai.error.APIError as e :
    # Handle API error, e.g. retry or log
    print(f"OpenAI API returned an API Error: {e}")
    pass
except openai.error.APIConnectionError as e :
    # Handle connection error, e.g. check network or log
    print(f"OpenAI API request failed to connect: {e}")
    pass
except openai.error.InvalidRequestError as e :
    # Handle invalid request error, e.g. validate parameters or log
    print(f"OpenAI API request was invalid: {e}")
    pass
except openai.error.AuthenticationError as e :
    # Handle authentication error, e.g. check credentials or log
    print(f"OpenAI API request was not authorized: {e}")
    pass
except openai.error.PermissionError as e :
    # Handle permission error, e.g. check scope or log
    print(f"OpenAI API request was not permitted: {e}")
    pass
except openai.error.RateLimitError as e :
    # Handle rate limit error, e.g. wait or log
    print(f"OpenAI API request exceeded rate limit: {e}")
    pass
