import json
import time
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("groq_key"),
    base_url="https://api.groq.com/openai/v1"
)


'''response  = client.chat.completions.create(
    model  = "openai/gpt-oss-20b",
    messages =[
        {
            "role" : "user",
            "content" : "what is weather today"

        }
    ]
)'''

#print(response.choices[0])
#print(response.choices[0].message.content)

# defining the weather tool

def get_weather(city : str ):
    '''Get weather for the city'''
    fake_weather = {
        "hyderabad": "25 Degrees, partly cloudy, Humidity: 65%",
        "kakinada": "35 Degrees, partly sunny, Humidity: 80%",
        "delhi": "32 Degrees, partly cloudy, Humidity: 45%",
        "pune": "19 Degrees, partly rainy, Humidity: 63%",
        "amsterdam": "23 Degrees, partly cloudy, Humidity: 40%",
        "rajahmundry": "37 Degrees, Sunny, Humidity: 89%",

    }

    lower_city = city.lower().strip()
    if lower_city in fake_weather:
        return fake_weather[lower_city]
    return f"the city weather data is not avaliable in the current data {lower_city}"

print(get_weather("Hyderabad"))



def Calculator(expression : str)-> str:

    """evaluate a mathematical expression and return the result """

    try:
        allowed = set('0123456789+-*() /')

        if not all (c in allowed for c in expression):
            return "Error:  Only numbers and () + / * are allowed"

        result = eval(expression)

        return str(result)
    except Exception as e:
        return f"Error: {e}"



# registering the json schema for the tool get_weather tool

tools = [
    {
        "type" :"function",
        "function" : {
            "name" : "get_weather",
            "description" : "Get the current weather data of a city",
            "parameters":{
                "type" : "object",
                "properties": {
                    "city" :{
                        "type" : "string",
                        "description" : "Name of the city e.g. Hyderabad"
                    }
                },
                "requried" :["city"]
            }
        }
    },
    {
        "type" :"function",
        "function" : {
            "name" : "Calculator",
            "description" : "Evaluate the math expression",
            "parameters": {
                "type" :"object",
                "properties" : {
                    "expression" : {
                         "type" : "string",
                        "description" : "Evaluates the expression for the given string, example: '25 * 5'"
                        }
                }
            }
        }
        
    }
]

for tool in tools:
    name = tool["function"]["name"]
    desc = tool["function"]["description"]
    param = list(tool["function"]["parameters"]["properties"])
    print(f"{name}({" ".join(param)}) - {desc}")


tool_functions ={
    "get_weather" : get_weather,
    "Calculator" : Calculator
}



messages = [
    {
        "role" : "system",
        "content" : "you are a helpfull assistant and use the tools when needed"
    },

    {
        "role" : "user",
        "content" : "95 +5"
    }
]


response  = client.chat.completions.create(
    model = "openai/gpt-oss-20b",
    tools = tools,
    messages = messages

)


choice = response.choices[0]

print(f"finish reason : {choice.finish_reason}")
print(f"Content : {choice.message.content}")
print(f"Tool calls : {choice.message.tool_calls}")

if choice.message.tool_calls:
    tc = choice.message.tool_calls[0]
    tool_name = tc.function.name
    arguments = json.loads(tc.function.arguments)
    function = tool_functions[tool_name]

    print(f"Tool : , {tc.function.name}")

    print(f"Arguments :,{tc.function.arguments}" )

    print(f"ID: , {tc.id}")
    result = function(**arguments)
    print(result)








