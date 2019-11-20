import os

PATH = './Raw_Dataset'



def check_jpgs(path):

    count = 0
    names = []

    for root, folders, files in os.walk(path):
        for f in files:
            if not f.endswith('.jpg'):
                names.append(f)
                count += 1
                   
    if count != 0:
        print(f"Founded {count} non JPG")
        
        for n in names:
            extension = n.split(".")[-1]
            old_name = n
            new_name = old_name.replace(f".{extension}", ".jpg")
            os.rename(os.path.join(path,old_name),os.path.join(path,new_name))

        print("Completed.")

    else:
        print("All files are JPG.")

        

def rename_files(path):
    total_files = len(os.listdir(path))
    num_name = 1

    for root, folders, files in os.walk(path):
        for f in files:
            if f.endswith('.jpg'):
                new_num_name = str(num_name) + ".jpg"
                os.rename(os.path.join(root,f),os.path.join(root,str(new_num_name)))
                num_name += 1
    
    print("Completed.")
    print(f"{total_files} files ofhas been renamed.")


check_jpgs(PATH)
rename_files(PATH)
                



