import requests
import time

def close_direct_messages(token):
    try:
        channels_response = requests.get("https://discord.com/api/v8/users/@me/channels", headers={"Authorization": token})
        
        if channels_response.status_code == 200:
            channels_data = channels_response.json()
            for channel in channels_data:
                channel_id = channel["id"]
                close_channel(channel_id, token)
        else:
            print("Failed to retrieve channel list.")
    except Exception as e:
        print(f"An error occurred: {e}")

def close_channel(channel_id, token):
    try:
        response = requests.delete(f"https://discord.com/api/v8/channels/{channel_id}", headers={"Authorization": token})
        
        if response.status_code in [200, 201, 204]:
            print(f"[STATUS] Closed >> [ {channel_id} ] DMS")
        elif response.status_code == 429:
            print(f"[STATUS] Failed Close >> [ {channel_id} ] DMS")
            time.sleep(response.json()['retry_after'])
        else:
            print(f"[STATUS] Failed Close >> [ {channel_id} ] DMS")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    token = input("Please enter your Discord token: ")
    close_direct_messages(token)

if __name__ == "__main__":
    main()
