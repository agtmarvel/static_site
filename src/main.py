from textnode import TextNode, TextType
import os
import shutil

def copy_directory_contents(src, dst):
    srclist = os.listdir(src)    
    
    if os.path.exists(dst) == False:
        os.mkdir(dst)
    
    for item in srclist:
        if os.path.isfile(os.path.join(src,item)) == True:
            src_path = shutil.copy2(os.path.join(src, item), os.path.join(dst, item))
        elif os.path.isdir(os.path.join(src, item)) == True:
            copy_directory_contents(os.path.join(src, item), os.path.join(dst, item))
    pass

def main():
    src = "static"
    dst = "public"
    if os.path.exists(dst) == True:
        shutil.rmtree(dst)
    
    copy_directory_contents(src, dst)
	


if __name__ == "__main__":
	main()