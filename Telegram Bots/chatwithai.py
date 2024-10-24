# By @itzAsuraa 
#Distribute and edit it as your wish but please don't remove credit
#By stealing Credit of Developer you will not become pro so try to give full credit to Developer


from pyrogram import Client, filters
import requests
import urllib.parse


# Function to query the AI API
def ask_query(query, model=None):
    # Available Models 'blackbox','gemini-1.5-flash','llama-3.1-405b','gpt-4o','gemini-pro','claude-sonnet-3.5'
    default_model = 'claude-sonnet-3.5'
    system_prompt = "You are a helpful assistant. Your name is Asuraa, and your owner's name is Captain, known as @itzAsuraa."

    model = model or default_model

    if model == default_model:
        query = f"{system_prompt}\n\nUser: {query}"

    encoded_query = urllib.parse.quote(query)
    url = f"https://chatwithai.codesearch.workers.dev/?chat={encoded_query}&model={model}"

    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json().get("result", "No response found.")
    else:
        return f"Error fetching response from API. Status code: {response.status_code}"

# Handler for the "/ask" command
@app.on_message(filters.command("ask"))
def handle_query(client, message):
    if len(message.command) < 2:
        message.reply_text("<b>Please provide a query to ask.</b>")
        return

    user_query = message.text.split(maxsplit=1)[1]
    
    # Fetch the response from the AI API
    response = ask_query(user_query)

    # Send the response back to the user
    message.reply_text(f"<b>{response}</b>")
    
    
# By @itzAsuraa 
#Distribute and edit it as your wish but please don't remove credit
#By stealing Credit of Developer you will not become pro so try to give full credit to Developer   