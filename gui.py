from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os

from binary_search_tree import Tree
from visualizer import visualize_tree

def add():
    tree.addnode(txtvalue.get())
    tree.visualizetree(tree.root)
    img = ImageTk.PhotoImage(Image.open("tree.png"))
    lblimage.configure(image=img)
    lblimage.image = img

def inorder():
    tree.inorder(tree.root)
    messagebox.showinfo("Inorder",tree.nodes)
    tree.nodes = ""

def preorder():
    tree.preorder(tree.root)
    messagebox.showinfo("Preorder",tree.nodes)
    tree.nodes = ""

def postorder():
    tree.postorder(tree.root)
    messagebox.showinfo("Postorder",tree.nodes)
    tree.nodes = ""

def show_image(event):
    os.system("tree.png") if os.path.exists("tree.png") else None

if __name__ == "__main__":
    tree = Tree()
    root = Tk()
    root.title("Binary Search Tree")
    root.geometry("500x300")

    lblvalue = Label(root,text="Enter data: ")
    lblvalue.place(x=50,y=50,width=100)

    txtvalue = Entry(root)
    txtvalue.place(x=150,y=50,width=100)

    btnadd = Button(root,text="Add",command=add)
    btnadd.place(x=50,y=100,width=100)

    btninorder = Button(root,text="Inorder",command=inorder)
    btninorder.place(x=150,y=100,width=100)

    btnpreorder = Button(root,text="Preorder",command=preorder)
    btnpreorder.place(x=50,y=150,width=100)

    btnpostorder = Button(root,text="Postorder",command=postorder)
    btnpostorder.place(x=150,y=150,width=100)

    lblimage = Label(root)
    lblimage.bind("<Button-1>",showimage)
    lblimage.place(x=300,y=50,width=150,height=150)
    root.mainloop()

    if os.path.exists("tree.png"):
       os.remove("tree.png")
       os.remove("tree")