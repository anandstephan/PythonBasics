import json
def load_data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    

def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)

def add_video(videos):
    name = input("Enter video name ")
    time = input("Enter video time")
    videos.append({'name':name,'time':time})
    save_data_helper(videos)

def list_video(videos):
    for video in videos:
        print(f"{video}")
def update_video(videos):
    list_video(videos)
    index = int(input("Enter the video number to update"))
    if 1<=index<=len(videos):
        name = input("Enter new video name")
        time = input("Enter new video time")
        videos[index-1] = {'name':name,'time':time}
        save_data_helper(videos)
    else:
        print("Invalid Index")

def delete_video(videos):
    list_video(videos)
    index = int(input("Enter the video number to delete"))
    if 1<=index<=len(videos):
       del videos[index-1]
       save_data_helper(videos)
    else:
        print("Invalid Index")
def main():
    while True:
        videos = load_data()
        print("\n Youtube Manager App")
        print("1: Add Youtube Video")
        print("2: List All Video")
        print("3: Update Youtube Video")
        print("4: Delete Youtube Video")
        print("5: Exit \n")
        choice = input("Enter Your Choice\n")

        match choice:
            case "1":
                add_video(videos)
            case "2":
                list_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid Input")
            
     

if __name__ == "__main__":
    main()