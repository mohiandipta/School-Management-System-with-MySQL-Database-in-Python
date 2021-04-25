from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import pymysql


class School:
    def __init__(self, root):
        self.root = root
        self.root.title("School Management System")
        self.root.geometry("1350x800+0+0")
        self.root.configure(background='gainsboro')

        # ----------Frames-----------

        Mainframe = Frame(self.root, bd=10, width=1350,
                          height=700, relief=RIDGE)
        Mainframe.grid()

        Outterframe = Frame(Mainframe, bd=10, width=1340,
                            height=600, relief=RIDGE)
        Outterframe.grid(row=0, column=0)

        InnerMostframe = Frame(Outterframe, bd=5, width=600,
                               height=500, bg='blue', relief=RIDGE)
        InnerMostframe.grid(row=0, column=0)

        Innerframe = Frame(Outterframe, bd=5, width=700,
                           height=500, bg='blue', relief=RIDGE)
        Innerframe.grid(row=0, column=1)

        BottomInnerframe = Frame(Mainframe, bd=7, width=1340,
                                 height=300, bg='gainsboro', relief=RIDGE)
        BottomInnerframe.grid(row=2, column=0)

        # top displayed frames

        Record_Frame = Frame(Innerframe, bd=4, width=900,
                             height=300, relief=RIDGE)
        Record_Frame.grid()

        Display_Frame = Frame(InnerMostframe, bd=4, width=400,
                              height=300, relief=RIDGE)
        Display_Frame.grid()

        # Bottom Subject frames

        Subject_Frame_Left = Frame(BottomInnerframe, bd=5, width=600,
                                   height=300, padx=0, bg='cyan', relief=RIDGE)
        Subject_Frame_Left.grid(row=0, column=0)

        Subject_Frame_Right = Frame(BottomInnerframe, bd=5, width=600,
                                    height=300, padx=0, bg='cyan', relief=RIDGE)
        Subject_Frame_Right.grid(row=0, column=1)

        # inside of subject_Frame_Left

        SubjectFrame1 = Frame(Subject_Frame_Left, bd=5,
                              width=300, height=250, padx=2, bg='gainsboro', relief=RIDGE)
        SubjectFrame1.grid(row=0, column=0)
        SubjectFrame2 = Frame(Subject_Frame_Left, bd=5,
                              width=400, height=250, padx=2, bg='gainsboro', relief=RIDGE)
        SubjectFrame2.grid(row=0, column=1)

        # inside of Subject_Frame_Right

        GuidanceFrame = Frame(Subject_Frame_Right, bd=5,
                              width=400, height=250, padx=2, bg='gainsboro', relief=RIDGE)
        GuidanceFrame.grid(row=0, column=0)
        ButtonsFrame = Frame(Subject_Frame_Right, bd=5,
                             width=200, height=250, padx=2, bg='gainsboro', relief=RIDGE)
        ButtonsFrame.grid(row=0, column=1)
        # ----------Frames are ended here-----------
        #
        #

        # =============Functions=============

        # labels of items and textfield in the displaye_frame

        # =============Student Details=============
        # StudentID
        self.lblStudensID = Label(Display_Frame, font=(
            'arial', 12, 'bold'), text="Student ID", bd=7)
        self.lblStudensID.grid(row=0, column=0, sticky=W, padx=5, pady=5)

        self.txtStudensID = Entry(Display_Frame, font=(
            'arial', 12, 'bold'), bd=5, width=29)
        self.txtStudensID.grid(row=0, column=1)

        # FirstName
        self.lblFirstName = Label(Display_Frame, font=(
            'arial', 12, 'bold'), text="First Name", bd=7)
        self.lblFirstName.grid(row=1, column=0, sticky=W, padx=5, pady=5)

        self.txtFirstName = Entry(Display_Frame, font=(
            'arial', 12, 'bold'), bd=5, width=29)
        self.txtFirstName.grid(row=1, column=1)

        # sureName
        self.lblSureName = Label(Display_Frame, font=(
            'arial', 12, 'bold'), text="Sure Name", bd=7)
        self.lblSureName.grid(row=2, column=0, sticky=W, padx=5, pady=5)

        self.txtSureName = Entry(Display_Frame, font=(
            'arial', 12, 'bold'), bd=5, width=29)
        self.txtSureName.grid(row=2, column=1)

        # sureName
        self.lblNINumber = Label(Display_Frame, font=(
            'arial', 12, 'bold'), text="NI Number", bd=7)
        self.lblNINumber.grid(row=3, column=0, sticky=W, padx=5, pady=5)

        self.txtNINumber = Entry(Display_Frame, font=(
            'arial', 12, 'bold'), bd=5, width=29)
        self.txtNINumber.grid(row=3, column=1)

        # Address
        self.lblAddress = Label(Display_Frame, font=(
            'arial', 12, 'bold'), text="Address", bd=7)
        self.lblAddress.grid(row=4, column=0, sticky=W, padx=5, pady=5)

        self.txtAddress = Entry(Display_Frame, font=(
            'arial', 12, 'bold'), bd=5, width=29)
        self.txtAddress.grid(row=4, column=1)

        # gender
        self.lblGender = Label(Display_Frame, font=(
            'arial', 12, 'bold'), text="Gender", bd=7)
        self.lblGender.grid(row=5, column=0, sticky=W, padx=5, pady=5)
        self.cboGender = ttk.Combobox(
            Display_Frame, width=40, state='readonly')
        self.cboGender['values'] = ('', 'Female', 'Male')
        self.cboGender.current(0)
        self.cboGender.grid(row=5, column=1)

        # DateOfBirth
        self.lblDOB = Label(Display_Frame, font=(
            'arial', 12, 'bold'), text="Date of Birth", bd=7)
        self.lblDOB.grid(row=6, column=0, sticky=W, padx=5, pady=5)

        self.txtDOB = Entry(Display_Frame, font=(
            'arial', 12, 'bold'), bd=5, width=29)
        self.txtDOB.grid(row=6, column=1)

        # Mobile
        self.lblMobile = Label(Display_Frame, font=(
            'arial', 12, 'bold'), text="Mobile", bd=7)
        self.lblMobile.grid(row=7, column=0, sticky=W, padx=5, pady=5)

        self.txtMobile = Entry(Display_Frame, font=(
            'arial', 12, 'bold'), bd=5, width=29)
        self.txtMobile.grid(row=7, column=1)

        # Email
        self.lblEmail = Label(Display_Frame, font=(
            'arial', 12, 'bold'), text="Email", bd=7)
        self.lblEmail.grid(row=8, column=0, sticky=W, padx=5, pady=5)

        self.txtEmail = Entry(Display_Frame, font=(
            'arial', 12, 'bold'), bd=5, width=29)
        self.txtEmail.grid(row=8, column=1)

        # =============Subject-Part-1=============

        self.lblEnglish = Label(SubjectFrame1, font=(
            'arial', 12, 'bold'), text="English", bd=7)
        self.lblEnglish.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.cboGender = ttk.Combobox(
            SubjectFrame1, width=29, state='readonly')
        self.cboGender['values'] = ('Core unit', 'Yes', 'No', 'Completed')
        self.cboGender.current(0)
        self.cboGender.grid(row=0, column=1)

        self.lblMath = Label(SubjectFrame1, font=(
            'arial', 12, 'bold'), text="Math", bd=7)
        self.lblMath.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.cboGender = ttk.Combobox(
            SubjectFrame1, width=29, state='readonly')
        self.cboGender['values'] = ('Core unit', 'Yes', 'No', 'Completed')
        self.cboGender.current(0)
        self.cboGender.grid(row=1, column=1)

        self.lblPhysics = Label(SubjectFrame1, font=(
            'arial', 12, 'bold'), text="Physics", bd=7)
        self.lblPhysics.grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.cboGender = ttk.Combobox(
            SubjectFrame1, width=29, state='readonly')
        self.cboGender['values'] = ('Core unit', 'Yes', 'No', 'Completed')
        self.cboGender.current(0)
        self.cboGender.grid(row=2, column=1)

        self.lblChemistry = Label(SubjectFrame1, font=(
            'arial', 12, 'bold'), text="Chemistry", bd=7)
        self.lblChemistry.grid(row=3, column=0, sticky=W, padx=5, pady=5)
        self.cboGender = ttk.Combobox(
            SubjectFrame1, width=29, state='readonly')
        self.cboGender['values'] = ('Core unit', 'Yes', 'No', 'Completed')
        self.cboGender.current(0)
        self.cboGender.grid(row=3, column=1)

        self.lblBiology = Label(SubjectFrame1, font=(
            'arial', 12, 'bold'), text="Biology", bd=7)
        self.lblBiology.grid(row=4, column=0, sticky=W, padx=5, pady=5)
        self.cboGender = ttk.Combobox(
            SubjectFrame1, width=29, state='readonly')
        self.cboGender['values'] = ('Core unit', 'Yes', 'No', 'Completed')
        self.cboGender.current(0)
        self.cboGender.grid(row=4, column=1)

        # =============Subject-Part-2=============

        # =============Parent of Guidance=============

        # =============Buttons=============


if __name__ == '__main__':
    root = Tk()
    application = School(root)
    root.mainloop()
