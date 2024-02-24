import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS videos(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL

        )

''') 

def add_video(name,time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (?,?)",(name,time))
    conn.commit()

def list_video():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def update_video(id,name,time):
    cursor.execute("UPDATE videos SET name=?,time=? WHERE id=?",(name,time,id))
    conn.commit()

def delete_video(id):
    cursor.execute("DELETE FROM videos WHERE id = ?",(id,))
    conn.commit()



def main():
    while True:
        
        print("\n Youtube Manager App")
        print("1: Add Youtube Video")
        print("2: List All Video")
        print("3: Update Youtube Video")
        print("4: Delete Youtube Video")
        print("5: Exit \n")
        choice = input("Enter Your Choice\n")

        match choice:
            case "1":
                name=input("Enter the video name")
                time = input("Enter the video time")
                add_video(name,time)

            case "2":
                list_video()
            case "3":
                id = input("Enter the video Id")
                name=input("Enter the video name")
                time = input("Enter the video time")
                update_video(id,name,time)
            case "4":
                id = input("Enter the video Id")
                delete_video(id)
            case "5":
                break
            case _:
                print("Invalid Input")

    conn.close()

if __name__ == "__main__":
    main()