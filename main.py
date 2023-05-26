########################################################
#              THIS IS AN OASIS CREATION               #
# DEVELOPER: ABBILAASH A T                             #
# LANGUAGE OF CREATION: PYTHON, SQL                    #
# FRAMEWORK: CustomTkinter, MySQL                      #
########################################################

#Importing the needed modules
import customtkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector 
import os
from tkinter import ttk
import random



#Entering my MySQL access data (localhost - XAMPP)
# server: Apache
# database: MySQL
USER = "root"
PASSWD = ""
DB = "codegram"
HOSTNAME = "localhost"

global USER_DET
USER_DET = {}

window = customtkinter.CTk()
window.geometry('1250x718')
window.state('zoomed')
window.resizable(0, 0)
window.title(" CodeGram")
window.configure(fg_color="white")

def App():
    # Define the main app frame
    global app
    app = customtkinter.CTkFrame(master=window,fg_color="white")
    app.place(x=0,y=0,relheight=1,relwidth=1)

    def dashboard_func():
        dashFrame = customtkinter.CTkFrame(master=window,fg_color="white")
        dashFrame.place(x=0,y=0,relheight=1,relwidth=1)

        side_options_frame = Frame(dashFrame, bg="white",width=200,height=65)
        side_options_frame.place(x=0,y=0)
        side_options_frame.pack_propagate(False)
        top_line = Canvas(side_options_frame, height=1, bg="MediumPurple2", highlightthickness=0)
        top_line.place(x=0,y=59,relwidth=1)
        top_navbar = Frame(dashFrame, bg="white",height=60)
        top_navbar.place(x=200,y=0,relwidth=1)
        top_line1 = Canvas(top_navbar, height=1, bg="MediumPurple1", highlightthickness=0)
        top_line1.place(x=0,y=59,relwidth=1)

        UserLogo_logo = ImageTk.PhotoImage(Image.open("assets/user-logo.png").resize((50,50)))
        UserLogo_set_lbl1 = customtkinter.CTkLabel(master=top_navbar,image=UserLogo_logo,text="")
        UserLogo_set_lbl1.place(x=860,y=0)
        LoggedUserName_lbl = customtkinter.CTkLabel(master=top_navbar,text=USER_DET['USERNAME'],
                                                    font=("yu gothic ui", 19,"bold"),text_color="black")
        LoggedUserName_lbl.place(x=900,y=5)

        codegram_logo1 = ImageTk.PhotoImage(Image.open("codegram-logo1.png").resize((180,58)))
        logo_set_lbl1 = customtkinter.CTkLabel(master=side_options_frame,image=codegram_logo1,text="")
        logo_set_lbl1.place(x=0,y=0)
    
        SideOptions_frame = customtkinter.CTkFrame(master=dashFrame,width=200,border_width=1,
                                                   border_color="MediumPurple1",
                                                   fg_color="white")
        SideOptions_frame.place(x=5,y=50,relheight=0.9)

        def home_func():
            home_frame = customtkinter.CTkFrame(master=dashFrame,fg_color="white")
            home_frame.place(x=210,y=50,relheight=1,relwidth=1)

            posts_frame = customtkinter.CTkFrame(master=home_frame,fg_color="gray90",width=800)
            posts_frame.place(x=30,y=0,relheight=0.9)

            HomePage_lbl = customtkinter.CTkLabel(master=posts_frame,text="Home Page",
                                                font=("yu gothic ui", 22,"bold"),fg_color="gray90",
                                                height=50,width=200,text_color="black")
            HomePage_lbl.place(x=0,y=10)

            # Defining the post frame
            def AddPost_func():
                #defining the frame structure
                AddPost_frame = customtkinter.CTkFrame(master=dashFrame,width=700,height=600,
                                                       fg_color="MediumPurple2")
                AddPost_frame.place(x=250,y=50)
                def close_func():
                    AddPost_frame.destroy()
                close_btn_img = customtkinter.CTkImage(Image.open(file_path + "/assets/close_icon.png"),size=(22,22))
                close_btn = customtkinter.CTkButton(master=AddPost_frame,command=close_func,anchor="sw",
                                                  hover_color="MediumPurple3",image=close_btn_img,
                                                  fg_color="MediumPurple2",compound="left",height=30,text_color="black",
                                                  font=("yu gothic ui", 19,"bold"),text="")
                close_btn.place(x=640,y=10)
                PostPage_lbl = customtkinter.CTkLabel(master=AddPost_frame,text="Create Post",
                                                font=("yu gothic ui", 22,"bold"),fg_color="MediumPurple2",
                                                height=50,text_color="black")
                PostPage_lbl.place(x=20,y=10)
                PostText_entry = customtkinter.CTkTextbox(master=AddPost_frame,width=660,border_width=1,
                                                          border_color="white",text_color="black",
                                                          fg_color="MediumPurple2",font=("yu gothic ui", 17),
                                                          corner_radius=7,height=400)
                PostText_entry.place(x=20,y=80)

                # Creating the main function to store the post in DB
                def PostDb_func():
                        AllPostID = []
                        AddPost_connection = mysql.connector.connect(host=HOSTNAME,user=USER,password=PASSWD,database=DB)
                        AddPost_cursor = AddPost_connection.cursor()
                        AddPost_cursor.execute("SELECT sno,post_id FROM post")

                        ALPHA2__ = []
                        ALPHA__ = AddPost_cursor.fetchall()
                        for ALPHA1__ in ALPHA__:
                            AllPostID.append(ALPHA1__[1])
                            ALPHA2__.append(ALPHA1__[0])

                        PostNewUniqueVal = 0
                        BETA__ = True
                        while BETA__:
                            RandNumm = random.randint(1000000000000,999999999999999)
                            if RandNumm in AllPostID:
                                continue
                            else:
                                PostNewUniqueVal = RandNumm
                                BETA__ = False

                        AddPost_connection.close()

                        AddPost_conn = mysql.connector.connect(host=HOSTNAME,user=USER,password=PASSWD,database=DB)
                        AddPost_conn_cursor = AddPost_conn.cursor()

                        PostContent = PostText_entry.get("0.0", "end")
                        PostingUserID = USER_DET['USER_ID']
                        PostSno = ALPHA2__[-1]+1

                        post_query = "INSERT INTO post(sno,user_id,post_id,post_content) VALUES (%s,%s,%s,%s)"
                        AddPost_conn_cursor.execute(post_query,(PostSno,PostingUserID,PostNewUniqueVal,PostContent,))

                        AddPost_conn.commit()
                        AddPost_conn.close()
                        AddPost_frame.destroy()

                PostText_btn = customtkinter.CTkButton(master=AddPost_frame,width=100,height=40,
                                                       corner_radius=9,border_color="white",border_width=1,
                                                       fg_color="MediumPurple2",text="POST",hover_color="purple1",
                                                       font=("yu gothic ui", 19,"bold"),command=PostDb_func)
                PostText_btn.place(x=20,y=500)

            AddPost_btn_img = customtkinter.CTkImage(Image.open(file_path + "/assets/post_icon.png"),size=(20,20))
            AddPost_btn = customtkinter.CTkButton(master=posts_frame,command=AddPost_func,anchor="sw",
                                                  hover_color="MediumPurple2",image=AddPost_btn_img,
                                                  fg_color="gray90",compound="left",height=30,text_color="black",
                                                  font=("yu gothic ui", 19,"bold"),text="Post",corner_radius=15,
                                                  width=60,border_color="MediumPurple1",border_width=1)
            AddPost_btn.place(x=630,y=25)

            PostsView_frame = customtkinter.CTkScrollableFrame(master=posts_frame,fg_color="gray90")
            PostsView_frame.place(x=0,y=70,relwidth=1,relheight=1)

            ViewPosts_connection = mysql.connector.connect(host=HOSTNAME,user=USER,password=PASSWD,database=DB)
            ViewPosts_cursor = ViewPosts_connection.cursor()
            
            ViewPosts_cursor.execute("SELECT user_id,post_id,post_content FROM post")
            AllPosts = ViewPosts_cursor.fetchall()
            AllPosts = AllPosts[::-1]
            ViewPosts_connection.close()

            # Scripting the main commenting function
            def comment(POST_id):
                def comment_dialog():
                    comment_frame_main = customtkinter.CTkFrame(master=home_frame,width=600,height=600,
                                                                          fg_color="MediumPurple2",border_width=1,
                                                                          border_color="MediumPurple1")
                    comment_frame_main.pack()

                    def close_func():
                        comment_frame_main.destroy()

                    close_btn_img1 = customtkinter.CTkImage(Image.open(file_path + "/assets/close_icon.png"),size=(22,22))
                    close_btn1 = customtkinter.CTkButton(master=comment_frame_main,command=close_func,anchor="sw",
                                                  hover_color="MediumPurple3",image=close_btn_img1,
                                                  fg_color="MediumPurple2",compound="left",height=30,text_color="black",
                                                  font=("yu gothic ui", 19,"bold"),text="")
                    close_btn1.place(x=550,y=2)

                    comment_entry = customtkinter.CTkEntry(master=comment_frame_main,width=450,height=40,
                                                           corner_radius=6,fg_color="MediumPurple2",border_color="black",
                                                           font=("yu gothic ui", 19),placeholder_text="Comment here...")
                    comment_entry.place(x=5,y=30)

                    def CommentFunc():
                        comment = comment_entry.get()
                        CommentInsertConn = mysql.connector.connect(host=HOSTNAME,user=USER,password=PASSWD,database=DB)
                        CommentInsertConn_cursor = CommentInsertConn.cursor()

                        CommentInsertConn_cursor.execute("INSERT INTO comments(post_id,user_id,comment) VALUES (%s,%s,%s)",(POST_id,USER_DET['USER_ID'],comment))
                        CommentInsertConn.commit()
                        CommentInsertConn.close()
                        comment_frame_main.destroy()


                    
                    comment_btn = customtkinter.CTkButton(master=comment_frame_main,width=100,text="Submit",
                                                          fg_color="Purple",text_color="black",border_color="white",
                                                          hover_color="MediumPurple1",corner_radius=10,height=40,
                                                          command=CommentFunc)
                    comment_btn.place(x=480,y=30)

                    comment_display_frame = customtkinter.CTkScrollableFrame(master=comment_frame_main,
                                                                             fg_color="MediumPurple2")
                    comment_display_frame.place(x=0,y=100,relheight=0.9,relwidth=1)

                    CommentRetrieveConn = mysql.connector.connect(host=HOSTNAME,user=USER,password=PASSWD,database=DB)
                    CommentRetrieveConn_cursor = CommentRetrieveConn.cursor()
                    CommentRetrieveConn_cursor.execute("SELECT * FROM comments WHERE post_id=%s",(POST_id,))
                    RetrievedComments = CommentRetrieveConn_cursor.fetchall()
                    for CommentData__ in RetrievedComments:
                        Comment = str(CommentData__[1])+" : "+CommentData__[2].decode()
                        DisplayComment_lbl = customtkinter.CTkLabel(master=comment_display_frame,
                                                                    text_color="black",text=Comment)
                        DisplayComment_lbl.pack()

                comment_btn_img = customtkinter.CTkImage(Image.open(file_path + "/assets/comment-icon.png"),size=(30,30))
                comment_btn = customtkinter.CTkButton(master=POST_frame,command=comment_dialog,anchor="sw",hover_color="MediumPurple2",image=comment_btn_img,fg_color="white",compound="left",height=30,text_color="black",font=("yu gothic ui", 19,"bold"),text="",corner_radius=8)
                comment_btn.place(x=590,y=240,relwidth=0.07)

            def ReadFull_func(POST_id):
                def  readmore():
                    ReadFull_frame_main = customtkinter.CTkFrame(master=home_frame,width=700,height=700,
                                                                            fg_color="MediumPurple2",border_width=1,
                                                                            border_color="MediumPurple1")
                    ReadFull_frame_main.place(x=200,relheight=0.8)
                    ReadFull_display_frame1 = customtkinter.CTkScrollableFrame(master=ReadFull_frame_main,
                                                                                fg_color="MediumPurple2",
                                                                                border_width=0)
                    ReadFull_display_frame1.place(x=0,y=40,relheight=0.9,relwidth=1)

                    ReadFull_display_frame = customtkinter.CTkFrame(master=ReadFull_display_frame1,
                                                                    fg_color="MediumPurple2")
                    ReadFull_display_frame.pack()

                    ReadFull_conn = mysql.connector.connect(host=HOSTNAME,user=USER,password=PASSWD,database=DB)
                    ReadFull_cursor = ReadFull_conn.cursor()

                    ReadFull_cursor.execute("SELECT user_id,post_content FROM post WHERE post_id=%s",(POST_id,))
                    FullContent = ReadFull_cursor.fetchone()
                    PostedUser = FullContent[0]

                    ReadFull_conn.close()

                    ReadUsername_conn = mysql.connector.connect(host=HOSTNAME,user=USER,password=PASSWD,database=DB)
                    ReadUsername_cursor = ReadUsername_conn.cursor()

                    ReadUsername_cursor.execute("SELECT username FROM users WHERE user_id=%s",(PostedUser,))
                    PostedUsername = "Posted By: "+ReadUsername_cursor.fetchone()[0]

                    ReadUsername_conn.close()

                    PostedUsername_lbl = customtkinter.CTkLabel(master=ReadFull_display_frame,text=PostedUsername,
                                                                text_color="black",
                                                                font=("yu gothic ui", 19,"bold"))
                    PostedUsername_lbl.pack()

                    Content_lbl = customtkinter.CTkLabel(master=ReadFull_display_frame,text=FullContent[1],
                                                             text_color="black",fg_color="MediumPurple2",
                                                             wraplength=670,justify="left")
                    Content_lbl.pack()

                    def close_func():
                        ReadFull_frame_main.destroy()
                    close_btn_img2 = customtkinter.CTkImage(Image.open(file_path + "/assets/close_icon.png"),size=(22,22))
                    customtkinter.CTkButton(master=ReadFull_frame_main,command=close_func,anchor="sw",
                                                  hover_color="MediumPurple3",image=close_btn_img2,
                                                  fg_color="MediumPurple2",compound="left",height=22,text_color="black",
                                                  font=("yu gothic ui", 19),text="",width=22).place(x=650,y=2)


                
                customtkinter.CTkButton(master=POST_frame,text="Read more...",text_color="red",
                                                       font=("yu gothic ui", 15,"bold"),fg_color="white",
                                                       hover_color="MediumPurple1",width=100,height=30,
                                                       command=readmore).place(x=35,y=240)


            for POST in AllPosts:
                global POST_id
                POST_id = POST[1]

                POST_frame = customtkinter.CTkFrame(master=PostsView_frame,fg_color="white", 
                                                    height=300,width=700,border_width=10,
                                                    border_color="gray90")
                POST_frame.pack(anchor="nw")
                ReadUsername_conn = mysql.connector.connect(host=HOSTNAME,user=USER,password=PASSWD,database=DB)
                ReadUsername_cursor = ReadUsername_conn.cursor()
                ReadUsername_cursor.execute("SELECT username FROM users WHERE user_id=%s",(POST[0],))
                PostedUsername = "Posted By: "+ReadUsername_cursor.fetchone()[0]
                ReadUsername_conn.close()
                
                POST_uid = customtkinter.CTkLabel(master=POST_frame,height=50,
                                                        fg_color="white",text_color="black",
                                                        text=PostedUsername,font=("yu gothic ui", 19,"bold"))
                POST_uid.place(x=10,y=15,relwidth=0.8)
                POST_content = customtkinter.CTkLabel(master=POST_frame,
                                                        fg_color="white",
                                                        text_color="black",text=POST[2],
                                                        wraplength=670,justify="left")
                POST_content.place(x=20,y=60,relheight=0.65)

                def comment_func():
                    comment(POST_id)
                comment_func()

                def readfull_func():
                    ReadFull_func(POST_id)
                readfull_func()


        # Creating the DM function
        def DM_func():
            # Getting the friends list
            FriendsList_conn = mysql.connector.connect(host=HOSTNAME,user=USER,password=PASSWD,database=DB)
            FriendsList_cursor = FriendsList_conn.cursor()
            FriendsList_cursor.execute("SELECT user_id FROM followers_details WHERE follower_id=%s",(USER_DET['USER_ID'],))
            # FriendsList = [(username,user_id,)]
            FriendsList = []
            ALPHA__3 = FriendsList_cursor.fetchall()
            for ALPHA__4 in ALPHA__3:
                FriendsList_cursor.execute("SELECT username FROM users WHERE user_id=%s",(int(ALPHA__4[0]),))
                FriendsList.append(FriendsList_cursor.fetchone())
            FriendsList_conn.close()

            # Creating a view for viewing all mails
            chat_frame = customtkinter.CTkFrame(master=dashFrame,fg_color="white")
            chat_frame.place(x=210,y=50,relheight=1,relwidth=1)

            MailDisplayMain_frame = customtkinter.CTkFrame(master=chat_frame,fg_color="gray80",width=400)
            MailDisplayMain_frame.place(x=5,y=0,relheight=0.9)

            MailDisplayMain_frame1 = customtkinter.CTkFrame(master=MailDisplayMain_frame,fg_color="gray68",
                                                            corner_radius=20)
            MailDisplayMain_frame1.place(x=0,y=70,relheight=1,relwidth=1)

            FriendsList_conn2 = mysql.connector.connect(host=HOSTNAME,user=USER,password=PASSWD,database=DB)
            FriendsList_cursor2 = FriendsList_conn2.cursor()

            # Getting all the mails to the main user's inbox
            FriendsList_cursor2.execute("SELECT from_id,message FROM c_mails WHERE to_id=%s",(USER_DET['USER_ID'],))
            AllMails = FriendsList_cursor2.fetchall()[::-1]

            # Creating a detailed mail viewing frame (right side frame)
            MailViewMain_frame = customtkinter.CTkFrame(master=chat_frame,fg_color="gray80")
            MailViewMain_frame.place(x=410,y=0,relheight=0.9,relwidth=0.7)

            ####################### inside the right side frame #####################
            def OnPressAct(ACT):
                customtkinter.CTkLabel(master=MailViewMain_frame,text="From ID: "+str(ACT[0]),font=("Helvetica",18,"bold"),text_color="black",
                                       wraplength=600,justify="left").place(x=10,y=20)
                customtkinter.CTkLabel(master=MailViewMain_frame,text=ACT[1],font=("Helvetica",15),text_color="black",
                                       wraplength=600,justify="left").place(x=10,y=70)
            

            # Creating a composing button
            def ComposeNewMail_func():
                ComposeMainFrame = customtkinter.CTkFrame(master=chat_frame,fg_color="gray60",width=700,height=600)
                ComposeMainFrame.place(x=100,y=0)
                def close_func():
                    ComposeMainFrame.destroy()
                close_btn_img = customtkinter.CTkImage(Image.open(file_path + "/assets/close_icon.png"),size=(22,22))
                close_btn = customtkinter.CTkButton(master=ComposeMainFrame,command=close_func,anchor="sw",
                                                  hover_color="gray50",image=close_btn_img,
                                                  fg_color="gray60",compound="left",height=30,text_color="black",
                                                  font=("yu gothic ui", 19,"bold"),text="",border_color="gray60",
                                                  border_width=1)
                close_btn.place(x=540,y=10)
        
            compose_btn_img = customtkinter.CTkImage(Image.open(file_path + "/assets/compose-icon.png"),size=(35,35))
            compose_btn = customtkinter.CTkButton(master=MailDisplayMain_frame,command=ComposeNewMail_func,width=5,anchor="sw",hover_color="gray70",image=compose_btn_img,fg_color="gray80",compound="left",height=35,text_color="white",font=("yu gothic ui", 19,"bold"),text="",corner_radius=8)
            compose_btn.place(x=330,y=5)


            # Displaying the mails in frames
            for ALPHA__5 in AllMails:
                MailDisplay = customtkinter.CTkFrame(master=MailDisplayMain_frame1,fg_color="white",
                                                     width=390,height=60,border_color="gray68",border_width=6)
                MailDisplay.pack()
                _CONN3_ = mysql.connector.connect(host=HOSTNAME,user=USER,password=PASSWD,database=DB)
                _CONN3_cursor = _CONN3_.cursor()
                _CONN3_cursor.execute("SELECT username FROM users WHERE user_id=%s",(ALPHA__5[0],))
                _CONN3_data = _CONN3_cursor.fetchall()
                for __CONN3__ in _CONN3_data:
                    customtkinter.CTkLabel(master=MailDisplay,
                                           text="FROM: "+__CONN3__[0],text_color="black",
                                           font=("Times New Roman",17)).place(x=15,y=15)
                def OnPress(_EV_):
                    OnPressAct(ALPHA__5)
                MailDisplay.bind("<Double-1>",OnPress)

            FriendsList_conn2.close()












        
        def settings_func():
            print("settings frame man!")

        def explore_func():

            explore_frame = customtkinter.CTkFrame(master=dashFrame,fg_color="gray80",width=400,
                                                   border_color="white",border_width=5)
            explore_frame.place(x=210,y=50,relheight=1)

            ExploreFrnd_entry = customtkinter.CTkEntry(master=explore_frame,width=300,
                                                       height=30,fg_color="gray80",border_color="gray60",
                                                       border_width=1,text_color="black")
            ExploreFrnd_entry.place(x=10,y=10)

            style = ttk.Style()
            style.theme_use('alt')

            Searchtree = ttk.Treeview(explore_frame, column=("c1"), show='headings', height=8)
            Searchtree.column("# 1", anchor="w")
            Searchtree.heading("# 1", text="Users",anchor=CENTER)

            #Searchtree.insert('','end',text=1,values=('abbilaash'))

            Searchtree.place(x=10,y=100,relwidth=0.95,relheight=0.9)

            style.configure("Treeview",
                    fieldbackground="gray80",
                    rowheight=50,
                    background="gray80",
                    font=("Kerning",16))
            style.configure("Treeview.Heading", font=("Kerning",19))

            # Creating a function to search users
            def SearchUser(EV):
                SearchUser_conn = mysql.connector.connect(host=HOSTNAME,user=USER,password=PASSWD,database=DB)
                SearchUser_cursor = SearchUser_conn.cursor()

                SearchQ = ExploreFrnd_entry.get()+'%'
                SearchUser_cursor.execute("SELECT user_id,username,gmail_id,user_bio FROM users WHERE username LIKE %s",(SearchQ,))
                SearchedUsers = SearchUser_cursor.fetchall()
                if len(SearchedUsers) > 0:
                    Searchtree.delete(*Searchtree.get_children())
                    for ALPHA__2 in SearchedUsers:
                        # ALPHA__2 ==> (user_id username gmail_id)
                        Searchtree.insert('','end',text=(ALPHA__2[0],ALPHA__2[1],ALPHA__2[2]),values=(ALPHA__2[1]))
                else:
                    Searchtree.delete(*Searchtree.get_children())
                SearchUser_conn.close()
                
                # Creating the main user detail page when username is double clicked
                def OnDoubleClick(EV1):
                    # Finding the selected username
                    Selection = Searchtree.selection()[0]
                    Selected_Username = Searchtree.item(Selection,"text").split(" ")

                    ViewId_frame = customtkinter.CTkFrame(master=dashFrame,fg_color="white")
                    ViewId_frame.place(x=210,y=50,relheight=1,relwidth=1)

                    UserDetails_frame = customtkinter.CTkFrame(master=ViewId_frame,fg_color="white")
                    UserDetails_frame.place(x=20,y=60,relwidth=1)

                    UserName_lbl = customtkinter.CTkLabel(master=UserDetails_frame,font=("Helvetica",24),
                                                          fg_color="white",text_color="black",
                                                          text=Selected_Username[1])
                    UserName_lbl.place(x=0,y=0)

                    GmailIdlbl_text = "Contact: "+Selected_Username[2]
                    GmailId_lbl = customtkinter.CTkLabel(master=UserDetails_frame,font=("Helvetica",15),
                                                          fg_color="white",text_color="black",
                                                          text=GmailIdlbl_text)
                    GmailId_lbl.place(x=0,y=40)

                    CodegramId_text = "CodeGram ID: "+Selected_Username[0]
                    CodegramId_lbl = customtkinter.CTkLabel(master=UserDetails_frame,font=("Helvetica",15),
                                                          fg_color="white",text_color="black",
                                                          text=CodegramId_text)
                    CodegramId_lbl.place(x=0,y=80)
                    
                    SearchUserFollow_conn = mysql.connector.connect(host=HOSTNAME,user=USER,password=PASSWD,database=DB)
                    SearchUserFollow_cursor = SearchUserFollow_conn.cursor()

                    SearchUserFollow_cursor.execute("SELECT followers,following,posts FROM follows WHERE user_id=%s",(int(Selected_Username[0]),))
                    SearchUserFollow = SearchUserFollow_cursor.fetchone()
                    
                    # Getting the count of posts, followers and followings from DB
                    UserPostCount = str(SearchUserFollow[2])+" posts"
                    UserfollowersCount = str(SearchUserFollow[0])+" followers"
                    UserFollowingCount = str(SearchUserFollow[1])+" following"

                    SearchUserFollow_conn.close()

                    SearchedUserPostsCount_lbl = customtkinter.CTkLabel(master=UserDetails_frame,font=("Helvetica",15),
                                                          fg_color="white",text_color="black",
                                                          text=UserPostCount)
                    SearchedUserPostsCount_lbl.place(x=0,y=150)

                    SearchedUserfollowers_lbl = customtkinter.CTkLabel(master=UserDetails_frame,font=("Helvetica",15),
                                                          fg_color="white",text_color="black",
                                                          text=UserfollowersCount)
                    SearchedUserfollowers_lbl.place(x=150,y=150)

                    SearchedUserfollowing_lbl = customtkinter.CTkLabel(master=UserDetails_frame,font=("Helvetica",15),
                                                          fg_color="white",text_color="black",
                                                          text=UserFollowingCount)
                    SearchedUserfollowing_lbl.place(x=300,y=150)

                    # Defining the follow function
                    def follow_func():
                        def Follow_func():
                            FollowREQ_conn = mysql.connector.connect(host=HOSTNAME,user=USER,password=PASSWD,database=DB)
                            FollowREQ_cursor = FollowREQ_conn.cursor()

                            FollowREQ_cursor.execute("UPDATE follows SET followers=followers+1 WHERE user_id=%s",(int(Selected_Username[0]),))
                            FollowREQ_conn.commit()
                            FollowREQ_cursor.execute("UPDATE follows SET following=following+1 WHERE user_id=%s",(USER_DET['USER_ID'],))
                            FollowREQ_conn.commit()
                            FollowREQ_cursor.execute("INSERT INTO followers_details (user_id,follower_id) VALUES (%s,%s)",(int(Selected_Username[0]),USER_DET['USER_ID'],))
                            FollowREQ_conn.commit()
                            FollowREQ_conn.close()

                            Follow_btn = customtkinter.CTkButton(master=UserDetails_frame,text="Following",command=unfollow_func,
                                                                    text_color="white",fg_color="gray25",
                                                                    hover_color="gray20",width=100,height=40)
                            Follow_btn.place(x=400,y=0)
                            
                            # To refresh the page when following data is processed
                            UserDetails_frame.destroy()
                            OnDoubleClick(EV)

                        def unfollow_func():
                            UnFollowREQ_conn = mysql.connector.connect(host=HOSTNAME,user=USER,password=PASSWD,database=DB)
                            UnFollowREQ_cursor = UnFollowREQ_conn.cursor()

                            UnFollowREQ_cursor.execute("UPDATE follows SET followers=followers-1 WHERE user_id=%s",(int(Selected_Username[0]),))
                            UnFollowREQ_conn.commit()
                            UnFollowREQ_cursor.execute("UPDATE follows SET following=following-1 WHERE user_id=%s",(USER_DET['USER_ID'],))
                            UnFollowREQ_conn.commit()
                            UnFollowREQ_cursor.execute("DELETE FROM followers_details WHERE follower_id=%s AND user_id=%s",(USER_DET['USER_ID'],int(Selected_Username[0]),))
                            UnFollowREQ_conn.commit()
                            UnFollowREQ_conn.close()
                            follow_func()

                            Follow_btn = customtkinter.CTkButton(master=UserDetails_frame,text="Follow",command=Follow_func,
                                                                        text_color="white",fg_color="Purple",
                                                                        hover_color="MediumPurple2",width=100,height=40)
                            Follow_btn.place(x=400,y=0)

                            UserDetails_frame.destroy()
                            OnDoubleClick(EV)

                        FollowREQ_conn1 = mysql.connector.connect(host=HOSTNAME,user=USER,password=PASSWD,database=DB)
                        FollowREQ_cursor1 = FollowREQ_conn1.cursor()

                        FollowREQ_cursor1.execute("SELECT follower_id FROM followers_details WHERE user_id=%s",(int(Selected_Username[0]),))
                        FollowREQ_data = FollowREQ_cursor1.fetchall()
                        
                        if FollowREQ_data:
                            for ALPHA__3 in FollowREQ_data:
                                print(ALPHA__3)
                                if ALPHA__3[0] == USER_DET['USER_ID']:
                                    Follow_btn = customtkinter.CTkButton(master=UserDetails_frame,text="Following",command=unfollow_func,
                                                                    text_color="white",fg_color="gray25",
                                                                    hover_color="gray20",width=100,height=40)
                                    Follow_btn.place(x=400,y=0)
                                else:
                                    Follow_btn = customtkinter.CTkButton(master=UserDetails_frame,text="Follow",command=Follow_func,
                                                                        text_color="white",fg_color="Purple",
                                                                        hover_color="MediumPurple2",width=100,height=40)
                                    Follow_btn.place(x=400,y=0)
                        else:
                            Follow_btn = customtkinter.CTkButton(master=UserDetails_frame,text="Follow",command=Follow_func,
                                                                        text_color="white",fg_color="Purple",
                                                                        hover_color="MediumPurple2",width=100,height=40)
                            Follow_btn.place(x=400,y=0)

                        FollowREQ_conn1.close()

                        def ComposeNewMail_func():
                            ComposeMainFrame = customtkinter.CTkFrame(master=ViewId_frame,fg_color="gray50",width=700,height=600)
                            ComposeMainFrame.place(x=100,y=0)
                            def close_func():
                                ComposeMainFrame.destroy()
                            close_btn_img = customtkinter.CTkImage(Image.open(file_path + "/assets/close_icon.png"),size=(22,22))
                            close_btn = customtkinter.CTkButton(master=ComposeMainFrame,command=close_func,anchor="sw",
                                                            hover_color="gray40",image=close_btn_img,
                                                            fg_color="gray50",compound="left",height=22,text_color="black",
                                                            font=("yu gothic ui", 19,"bold"),text="",width=22)
                            close_btn.place(x=630,y=10)

                            toaddr_text = "To: "+Selected_Username[1]
                            toaddr_lbl = customtkinter.CTkLabel(master=ComposeMainFrame,font=("yu gothic ui", 18,"bold"),
                                                                text=toaddr_text,text_color="white")
                            toaddr_lbl.place(x=15,y=80)

                            body_lbl = customtkinter.CTkLabel(master=ComposeMainFrame,font=("yu gothic ui", 20,"bold"),
                                                              text_color="white",text="Body")
                            body_lbl.place(x=15,y=140)

                            body_entry = customtkinter.CTkTextbox(master=ComposeMainFrame,font=("yu gothic ui", 15),
                                                                text_color="white",border_width=1,border_color="black",
                                                                fg_color="gray50",width=650,height=300)
                            body_entry.place(x=15,y=180)

                            # getting all the inserted hyperlinks in a list form
                            AllHyperlinks = []

                            # Creating a function to add hyperlinks
                            def add_hyperlink():
                                # Frame to add hyperlink and its descriptions
                                AddHyperlink_Frame = customtkinter.CTkFrame(master=ComposeMainFrame,width=500,
                                                                            height=250,fg_color="gray60",
                                                                            border_color="black",border_width=1)
                                AddHyperlink_Frame.place(x=10,y=10)

                                def close_func():
                                    AddHyperlink_Frame.destroy()
                                close_btn_img = customtkinter.CTkImage(Image.open(file_path + "/assets/close_icon.png"),size=(22,22))
                                close_btn = customtkinter.CTkButton(master=AddHyperlink_Frame,command=close_func,anchor="sw",
                                                                hover_color="gray40",image=close_btn_img,
                                                                fg_color="gray50",compound="left",height=22,text_color="black",
                                                                font=("yu gothic ui", 19,"bold"),text="",width=22)
                                close_btn.place(x=470,y=0)

                                AddHyperlink_lbl = customtkinter.CTkLabel(master=AddHyperlink_Frame,
                                                                          text="Add Hyperlink",font=("yu gothic ui",19,"bold"),
                                                                          text_color="black")
                                AddHyperlink_lbl.place(x=15,y=20)
                                PasteHyperlink_lbl = customtkinter.CTkLabel(master=AddHyperlink_Frame,
                                                                            text="Paste Link: ",font=("yu gothic ui",16),text_color="black")
                                PasteHyperlink_lbl.place(x=10,y=50)
                                AddHyperlink_entry = customtkinter.CTkEntry(master=AddHyperlink_Frame,
                                                                            width=300,height=30,fg_color="gray60")
                                AddHyperlink_entry.place(x=120,y=50)

                                HyperlinkDesc_lbl = customtkinter.CTkLabel(master=AddHyperlink_Frame,
                                                                            text="Description: ",font=("yu gothic ui",16),text_color="black")
                                HyperlinkDesc_lbl.place(x=10,y=80)
                                HyperlinkDesc_entry = customtkinter.CTkTextbox(master=AddHyperlink_Frame,
                                                                            width=300,height=80,fg_color="gray60",
                                                                            font=("yu gothic ui",16),text_color="black",
                                                                            border_color="black",border_width=1)
                                HyperlinkDesc_entry.place(x=10,y=110) 

                                def AddHyperlink():
                                    AddHyperlink = AddHyperlink_entry.get()
                                    HyperlinkDesc = HyperlinkDesc_entry.get("0.0","end")
                                    AddHyperlink_dict = {}
                                    AddHyperlink_dict['LINK'] = AddHyperlink
                                    AddHyperlink_dict['DESCRIPTION'] = HyperlinkDesc
                                    AllHyperlinks.append(AddHyperlink_dict)
                                    body_entry.insert(CURRENT,"\n"+AddHyperlink+" ("+HyperlinkDesc+"\b"+")")
                                    AddHyperlink_Frame.destroy()


                                AddHyperlink_btn = customtkinter.CTkButton(master=AddHyperlink_Frame,width=100,height=40,
                                                               text="Add",font=("yu gothic ui", 16),
                                                               fg_color="gray20",hover_color="gray15",
                                                               command=AddHyperlink)
                                AddHyperlink_btn.place(x=30,y=190)

                            
                            hyperlink_btn_img = customtkinter.CTkImage(Image.open(file_path + "/assets/hyperlink-icon.png"),size=(22,22))
                            Hyperlink_btn = customtkinter.CTkButton(master=ComposeMainFrame,command=add_hyperlink,anchor="sw",hover_color="gray40",image=hyperlink_btn_img,fg_color="gray50",compound="left",height=22,text_color="black",font=("yu gothic ui", 19,"bold"),text="",width=22,corner_radius=10)
                            Hyperlink_btn.place(x=30,y=520)

                            def send_message():
                                DraftMessage = body_entry.get("0.0", "end")

                                # Create a database connection which inserts the details in db
                                _db_connect = mysql.connector.connect(host=HOSTNAME,user=USER,password=PASSWD,database=DB)
                                _db_cursor = _db_connect.cursor()
                                _db_cursor.execute("INSERT INTO c_mails(from_id,to_id,message) VALUES (%s,%s,%s)",(USER_DET['USER_ID'],int(Selected_Username[0]),DraftMessage,))
                                _db_connect.commit()
                                _db_connect.close()

                                # Destroy the compose frame
                                ComposeMainFrame.destroy()

                            Send_btn = customtkinter.CTkButton(master=ComposeMainFrame,width=100,height=40,
                                                               text="Send",font=("yu gothic ui", 16),
                                                               fg_color="gray20",hover_color="gray15",
                                                               command=send_message)
                            Send_btn.place(x=300,y=520)



                        Message_btn = customtkinter.CTkButton(master=UserDetails_frame,text="Message",command=ComposeNewMail_func,
                                                                        text_color="white",fg_color="gray60",
                                                                        hover_color="gray68",width=100,height=40)
                        Message_btn.place(x=595,y=0)

                    follow_func()

                # Opening the user's profile page when the ID is clicked
                Searchtree.bind("<Double-1>",OnDoubleClick)

            # The entry to search an user
            ExploreFrnd_entry.bind("<Key>",SearchUser) 
        


        global file_path
        file_path = os.path.dirname(os.path.realpath(__file__))

        dashboard_btn_img = customtkinter.CTkImage(Image.open(file_path + "/assets/dashboard_icon.png"),size=(20,20))
        settings_btn_img = customtkinter.CTkImage(Image.open(file_path + "/assets/settings_icon.png"),size=(22,22))
        explore_btn_img = customtkinter.CTkImage(Image.open(file_path + "/assets/explore-icon.png"),size=(22,22))
        dm_btn_img = customtkinter.CTkImage(Image.open(file_path + "/assets/chat-icon.png"),size=(22,22))

        dashboard_btn = customtkinter.CTkButton(master=SideOptions_frame,command=home_func,anchor="sw",hover_color="MediumPurple2",image=dashboard_btn_img,fg_color="white",compound="left",height=40,text_color="black",font=("yu gothic ui", 19,"bold"),text="  Home",corner_radius=8)
        dashboard_btn.place(x=5,y=70,relwidth=0.95)

        explore_btn = customtkinter.CTkButton(master=SideOptions_frame,command=explore_func,anchor="sw",hover_color="MediumPurple2",image=explore_btn_img,fg_color="white",compound="left",height=40,text_color="black",font=("yu gothic ui", 19,"bold"),text="  Explore",corner_radius=8)
        explore_btn.place(x=5,y=130,relwidth=0.95)

        dm_btn = customtkinter.CTkButton(master=SideOptions_frame,command=DM_func,anchor="sw",hover_color="MediumPurple2",image=dm_btn_img,fg_color="white",text_color="black",compound="left",height=40,font=("yu gothic ui", 19,"bold"),text="  Chat",corner_radius=8)
        dm_btn.place(x=5,y=190,relwidth=0.95)

        settings_btn = customtkinter.CTkButton(master=SideOptions_frame,command=settings_func,anchor="sw",hover_color="MediumPurple2",image=settings_btn_img,fg_color="white",text_color="black",compound="left",height=40,font=("yu gothic ui", 19,"bold"),text="  Settings",corner_radius=8)
        settings_btn.place(x=5,y=250,relwidth=0.95)

        home_func()


    codegram_logo = ImageTk.PhotoImage(Image.open("codegram-logo.png").resize((400,400)))
    logo_set_lbl = customtkinter.CTkLabel(master=app,image=codegram_logo,text="")
    logo_set_lbl.place(x=50,y=200)

    half_frame = customtkinter.CTkFrame(master=app,fg_color="MediumPurple2")
    half_frame.place(x=400,y=0,relheight=1,relwidth=1)

    welcome_lbl = customtkinter.CTkLabel(master=half_frame,text="Welcome To CodeGram Login,",
                                                font=("yu gothic ui", 24,"bold"),fg_color="MediumPurple2",height=50,width=200,
                                                text_color="black")
    welcome_lbl.place(x=120,y=150)

    # Creating the signup frame
    def signup_func():
        allUserId = []
        lastSNO = []
        userid_db_connect = mysql.connector.connect(host=HOSTNAME,user=USER,password=PASSWD,database=DB)
        userid_db_cursor = userid_db_connect.cursor()
        userid_db_cursor.execute("SELECT sno,user_id FROM users")
        userid_account = userid_db_cursor.fetchall()
        for A_ in userid_account:
            allUserId.append(A_[1])
            lastSNO.append(A_[0])
        userid_db_connect.close()

        half_frame1 = customtkinter.CTkFrame(master=app,fg_color="MediumPurple2")
        half_frame1.place(x=400,y=0,relheight=1,relwidth=1)

        signup_welcome_lbl = customtkinter.CTkLabel(master=half_frame1,text="Welcome To CodeGram Sign Up,",
                                                font=("yu gothic ui", 24,"bold"),fg_color="MediumPurple2",height=50,width=200,
                                                text_color="black")
        signup_welcome_lbl.place(x=120,y=150)

        signup_username_lbl = customtkinter.CTkLabel(half_frame1,text="Username",font=("yu gothic ui", 19,"bold"),
                                          text_color="black",fg_color="MediumPurple2")
        signup_username_lbl.place(x=120,y=210)
        signup_username_entry = customtkinter.CTkEntry(half_frame1, placeholder_text="",height=40,width=500,
                                                fg_color="MediumPurple2",border_width=1,border_color="black",
                                                corner_radius=20,text_color="black",font=("yu gothic ui", 17,"bold"))
        signup_username_entry.place(x=120,y=250)
        signup_password_lbl = customtkinter.CTkLabel(half_frame1,text="Password",font=("yu gothic ui", 19,"bold"),
                                            text_color="black",fg_color="MediumPurple2")
        signup_password_lbl.place(x=120,y=320)
        signup_password_entry = customtkinter.CTkEntry(half_frame1, placeholder_text="",height=40,width=500,
                                                fg_color="MediumPurple2",border_width=1,border_color="black",
                                                corner_radius=20,text_color="black",font=("yu gothic ui", 17,"bold"),
                                                show="*")
        signup_password_entry.place(x=120,y=360)
        signup_gmail_lbl = customtkinter.CTkLabel(half_frame1,text="Gmail Id",font=("yu gothic ui", 19,"bold"),
                                            text_color="black",fg_color="MediumPurple2")
        signup_gmail_lbl.place(x=120,y=430)
        signup_gmail_entry = customtkinter.CTkEntry(half_frame1, placeholder_text="",height=40,width=500,
                                                fg_color="MediumPurple2",border_width=1,border_color="black",
                                                corner_radius=20,text_color="black",font=("yu gothic ui", 17,"bold"))
        signup_gmail_entry.place(x=120,y=470)

        #adding the details to database
        def signup_db():
            signUsername = signup_username_entry.get()
            if len(signUsername.split(" ")) > 1:
                messagebox.showwarning("Sign Up Error!","The username should be a single phrase!")
                exit()
            else:
                pass
            signPassword = signup_password_entry.get()
            signGmail = signup_gmail_entry.get()

            sno_ = lastSNO[-1]+1
            UniqueSerial = 0
            while True:
                RandNum = random.randrange(1000000000,9999999999)
                if RandNum in allUserId:
                    continue
                else:
                    UniqueSerial = RandNum
                    break

            signup_db_connect = mysql.connector.connect(host=HOSTNAME,user=USER,password=PASSWD,database=DB)
            signup_db_cursor = signup_db_connect.cursor()
            signup_db_cursor.execute("INSERT INTO `users`(`sno`, `username`, `password`, `user_id`,`gmail_id`) VALUES (%s,%s,%s,%s,%s)",(sno_,signUsername,signPassword,UniqueSerial,signGmail,))
            signup_db_cursor.execute("INSERT INTO follows(user_id,followers,following,posts) VALUES (%s,0,0,0)",(UniqueSerial,))
            signup_db_cursor.execute("UPDATE tot_users SET total_users=total_users+1")
            signup_db_connect.commit()
            signup_db_connect.close()

            half_frame1.destroy()

        sign_btn = customtkinter.CTkButton(master=half_frame1,text="Sign up",width=250,height=40,
                                        fg_color="white",hover_color="MediumPurple4",
                                        text_color="black",font=("yu gothic ui", 18),
                                        border_color="MediumPurple2",
                                        border_width=1,corner_radius=20,command=signup_db)
        sign_btn.place(x=120,y=550)
        login1_btn = customtkinter.CTkButton(master=half_frame1,text="Login",width=180,height=40,
                                            fg_color="MediumPurple2",hover_color="white",
                                            text_color="black",font=("yu gothic ui", 18),
                                            border_color="white",
                                            border_width=1,corner_radius=20,command=App)
        login1_btn.place(x=440,y=550)


    username_lbl = customtkinter.CTkLabel(half_frame,text="Username",font=("yu gothic ui", 19,"bold"),
                                          text_color="black",fg_color="MediumPurple2")
    username_lbl.place(x=120,y=230)
    username_entry = customtkinter.CTkEntry(half_frame, placeholder_text="",height=40,width=500,
                                            fg_color="MediumPurple2",border_width=1,border_color="black",
                                            corner_radius=20,text_color="black",font=("yu gothic ui", 17,"bold"))
    username_entry.place(x=120,y=270)
    password_lbl = customtkinter.CTkLabel(half_frame,text="Password",font=("yu gothic ui", 19,"bold"),
                                          text_color="black",fg_color="MediumPurple2")
    password_lbl.place(x=120,y=340)
    password_entry = customtkinter.CTkEntry(half_frame, placeholder_text="",height=40,width=500,
                                            fg_color="MediumPurple2",border_width=1,border_color="black",
                                            corner_radius=20,text_color="black",font=("yu gothic ui", 17,"bold"),
                                            show="*")
    password_entry.place(x=120,y=380)

    def login_func():
        user_entry = username_entry.get()
        pass_entry = password_entry.get()
        login_db_connect = mysql.connector.connect(host=HOSTNAME,user=USER,password=PASSWD,database=DB)
        login_db_cursor = login_db_connect.cursor()
        login_db_cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s",(user_entry,pass_entry,))
        logged_account = login_db_cursor.fetchone()
        if logged_account:
            USER_DET['SNO'] = logged_account[0]
            USER_DET['USERNAME'] = logged_account[1]
            USER_DET['PASSWORD'] = logged_account[2]
            USER_DET['USER_ID'] = logged_account[3]
            dashboard_func()
        else:
            messagebox.showerror("Error!","Wrong username or password. Please Retry!")

    login_btn = customtkinter.CTkButton(master=half_frame,text="Login",width=250,height=40,
                                        fg_color="white",hover_color="MediumPurple4",
                                        text_color="black",font=("yu gothic ui", 18),
                                        border_color="MediumPurple2",
                                        border_width=1,corner_radius=20,command=login_func)
    login_btn.place(x=120,y=450)
    signup_btn = customtkinter.CTkButton(master=half_frame,text="Sign up",width=180,height=40,
                                        fg_color="MediumPurple2",hover_color="white",
                                        text_color="black",font=("yu gothic ui", 18),
                                        border_color="white",
                                        border_width=1,corner_radius=20,command=signup_func)
    signup_btn.place(x=440,y=450)


App()

window.mainloop()
