from pymongo import MongoClient
from bson import ObjectId
client = MongoClient("mongodb+srv://anandstephan98:1234567890@cluster0.spii61i.mongodb.net/",tlsAllowInvalidCertificates=True)

# print(client)
db = client["ytManager"]
video_collection = db['videos']

def list_video():
   for video in  video_collection.find():
       print(f" ID: {video['_id']}, Name: {video['name']} , time : {video['time']}")



def add_video():
    name=input("Enter video name")
    time = input("Enter video time")
    video_collection.insert_one({"name":name,"time":time})

def update_video(video_id,name,time):
    video_collection.update_one({'_id':ObjectId(video_id)},{
        "$set":{"name":name,"time":time}
    })

def delete_video():
    video_id = input("Enter video id")
    video_collection.delete_one({"_id":ObjectId(video_id)})

def main():
    while True:
         print("\n Youtube Manager App ")
         print("1: List All Videos ")
         print("2: Add Video ")
         print("3: Update Video ")
         print("4: Delete Video ")
         print("5: Exit ")
         choice = input("\nEnter Your Choice -: ")

         if choice == "1":
             list_video()
         elif choice == "2":
             add_video()
         elif choice == "3":
             video_id = input("Enter video Id")
             name = input("Enter video name")
             time = input("Enter video time")
             update_video(video_id,name,time)
         elif choice == "4":
             delete_video()
         elif choice == "5":
             break
         else:
             print("Invalid Input")
        


   
if __name__ == "__main__":
    main()


