# DeepSeek Chatbot API Integration

## Prerequisites

1. **Create a DeepSeek Account:** 
   - Visit DeepSeek and sign up for an account.
   
2. **Obtain Authorization Token:**
   - Open the DeepSeek chatbot page and inspect the network activity using the developer tools.
   - In the **Network** tab, find the authorization string that starts with `Bearer` in the headers (shown in the image below).

   ![Screenshot of Authorization Token](https://github.com/avijitbhuin21/Tutorials/blob/main/Deepseek_Free_Api/Screenshot%202024-09-15%20063944.png)

3. **Extract the Token:**
   - Copy the token but **exclude** the `Bearer` part.

Now you are ready to use the API!

## Usage

```python
from DEEPSEEK import deepseek_chat

# Initialize the bot with your authorization token (without the "Bearer" part)
bot = deepseek_chat('your_authtoken_here')

# Ask the bot to generate a code in JSON format
response = bot.ask('Generate me a code to check if a number is prime or not in json format {"CODE": "YOUR CODE HERE"}')

print(response)
```

## Sample Output

The bot returns the following :

'Sure! Here is the code to check if a number is prime or not in JSON format:
```json
{
  "CODE": "def is_prime(n):\n    if n <= 1:\n        return False\n    if n == 2:\n        return True\n    if n % 2 == 0:\n        return False\n    for i in range(3, int(n**0.5) + 1, 2):\n        if n % i == 0:\n            return False\n    return True\n\n# Example usage:\n# print(is_prime(29))  # Output: True"
}
```

This JSON object contains a Python function `is_prime` that checks whether a number `n` is prime. It returns `True` if the number is prime and `False` otherwise.

## Happy Coding!
