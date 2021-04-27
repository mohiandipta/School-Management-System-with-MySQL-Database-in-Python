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
                          height=700, bg='gainsboro', relief=RIDGE)
        Mainframe.grid()

        Outterframe = Frame(Mainframe, bd=10, width=1340,
                            height=300, bg='gainsboro', relief=RIDGE)
        Outterframe.grid(row=0, column=0)

        InnerMostframe = Frame(Outterframe, bd=5, width=600,
                               height=300, bg='blue', relief=RIDGE)
        InnerMostframe.grid(row=0, column=0)

        Innerframe = Frame(Outterframe, bd=5, width=700,
                           height=300, bg='blue', relief=RIDGE)
        Innerframe.grid(row=0, column=1)

        BottomInnerframe = Frame(Mainframe, bd=7, width=1340,
                                 height=300, bg='gainsboro', relief=RIDGE)
        BottomInnerframe.grid(row=2, column=0)

        # top displayed frames

        Records_Frame = Frame(Innerframe, bd=4, width=900,
                              height=300, relief=RIDGE)
        Records_Frame.grid()

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
                              width=300, height=300, padx=2, bg='gainsboro', relief=RIDGE)
        SubjectFrame1.grid(row=0, column=0)
        SubjectFrame2 = Frame(Subject_Frame_Left, bd=5,
                              width=500, height=300, padx=2, bg='gainsboro', relief=RIDGE)
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

        # =============Student Records=============

        scroll_x = Scrollbar(Records_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Records_Frame, orient=VERTICAL)

        self.student_records = ttk.Treeview(
            Records_Frame, height=13, column=("stdid", "firstname", "surname", "ninumber", "address", "gender", "dob", "mobile", "email"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.student_records.heading("stdid", text='Student ID')
        self.student_records.heading("firstname", text='First Name')
        self.student_records.heading("surname", text='Sure Name')
        self.student_records.heading("ninumber", text='NI Number')
        self.student_records.heading("address", text='Address')
        self.student_records.heading("gender", text='Gender')
        self.student_records.heading("dob", text='Date of Birth')
        self.student_records.heading("mobile", text='Mobile')
        self.student_records.heading("email", text='Email')

        self.student_records['show'] = 'headings'

        self.student_records.column("stdid", width=70)
        self.student_records.column("firstname", width=100)
        self.student_records.column("surname", width=100)
        self.student_records.column("ninumber", width=70)
        self.student_records.column("address", width=150)
        self.student_records.column("gender", width=70)
        self.student_records.column("dob", width=70)
        self.student_records.column("mobile", width=100)
        self.student_records.column("email", width=150)

        self.student_records.pack(fill=BOTH, expand=1)

        # =============Subject-Part-1=============

        self.lblEnglish = Label(SubjectFrame1, font=(
            'arial', 12, 'bold'), text="English", bd=7)
        self.lblEnglish.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.cboEnglish = ttk.Combobox(
            SubjectFrame1, width=29, state='readonly')
        self.cboEnglish['values'] = ('Core unit', 'Yes', 'No', 'Completed')
        self.cboEnglish.current(0)
        self.cboEnglish.grid(row=0, column=1)

        self.lblGames = Label(SubjectFrame1, font=(
            'arial', 12, 'bold'), text="Games", bd=7)
        self.lblGames.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.cboGames = ttk.Combobox(
            SubjectFrame1, width=29, state='readonly')
        self.cboGames['values'] = ('Core unit', 'Yes', 'No', 'Completed')
        self.cboGames.current(0)
        self.cboGames.grid(row=1, column=1)

        self.lblAnimation = Label(SubjectFrame1, font=(
            'arial', 12, 'bold'), text="Animaion", bd=7)
        self.lblAnimation.grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.cboAnimation = ttk.Combobox(
            SubjectFrame1, width=29, state='readonly')
        self.cboAnimation['values'] = ('Core unit', 'Yes', 'No', 'Completed')
        self.cboAnimation.current(0)
        self.cboAnimation.grid(row=2, column=1)

        self.lblDatabase = Label(SubjectFrame1, font=(
            'arial', 12, 'bold'), text="Database", bd=7)
        self.lblDatabase.grid(row=3, column=0, sticky=W, padx=5, pady=5)
        self.cboDatabase = ttk.Combobox(
            SubjectFrame1, width=29, state='readonly')
        self.cboDatabase['values'] = ('Core unit', 'Yes', 'No', 'Completed')
        self.cboDatabase.current(0)
        self.cboDatabase.grid(row=3, column=1)

        self.lblAddMaths = Label(SubjectFrame1, font=(
            'arial', 12, 'bold'), text="AddMaths", bd=7)
        self.lblAddMaths.grid(row=4, column=0, sticky=W, padx=5, pady=5)
        self.cboAddMaths = ttk.Combobox(
            SubjectFrame1, width=29, state='readonly')
        self.cboAddMaths['values'] = ('Core unit', 'Yes', 'No', 'Completed')
        self.cboAddMaths.current(0)
        self.cboAddMaths.grid(row=4, column=1)

        self.lblPhysics = Label(SubjectFrame1, font=(
            'arial', 12, 'bold'), text="Physics", bd=7)
        self.lblPhysics.grid(row=5, column=0, sticky=W, padx=5, pady=5)
        self.cboPhysics = ttk.Combobox(
            SubjectFrame1, width=29, state='readonly')
        self.cboPhysics['values'] = ('Core unit', 'Yes', 'No', 'Completed')
        self.cboPhysics.current(0)
        self.cboPhysics.grid(row=5, column=1)

        # =============Subject-Part-2=============

        self.lblDataScience = Label(SubjectFrame2, font=(
            'arial', 12, 'bold'), text="Data Science", bd=7)
        self.lblDataScience.grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.cboDataScience = ttk.Combobox(
            SubjectFrame2, width=29, state='readonly')
        self.cboDataScience['values'] = ('Core unit', 'Yes', 'No', 'Completed')
        self.cboDataScience.current(0)
        self.cboDataScience.grid(row=0, column=1)

        self.lblEventDrivenProg = Label(SubjectFrame2, font=(
            'arial', 12, 'bold'), text="Event Driven Prog   ", bd=7)
        self.lblEventDrivenProg.grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.cboEventDrivenProg = ttk.Combobox(
            SubjectFrame2, width=29, state='readonly')
        self.cboEventDrivenProg['values'] = (
            'Core unit', 'Yes', 'No', 'Completed')
        self.cboEventDrivenProg.current(0)
        self.cboEventDrivenProg.grid(row=1, column=1)

        self.lblObjectOriented = Label(SubjectFrame2, font=(
            'arial', 12, 'bold'), text="Object Oriented", bd=7)
        self.lblObjectOriented.grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.cboObjectOriented = ttk.Combobox(
            SubjectFrame2, width=29, state='readonly')
        self.cboObjectOriented['values'] = (
            'Core unit', 'Yes', 'No', 'Completed')
        self.cboObjectOriented.current(0)
        self.cboObjectOriented.grid(row=2, column=1)

        self.lblSpreadSheet = Label(SubjectFrame2, font=(
            'arial', 12, 'bold'), text="Spread Sheet", bd=7)
        self.lblSpreadSheet.grid(row=3, column=0, sticky=W, padx=5, pady=5)
        self.cboSpreadSheet = ttk.Combobox(
            SubjectFrame2, width=29, state='readonly')
        self.cboSpreadSheet['values'] = ('Core unit', 'Yes', 'No', 'Completed')
        self.cboSpreadSheet.current(0)
        self.cboSpreadSheet.grid(row=3, column=1)

        self.lblSystemAnalysis = Label(SubjectFrame2, font=(
            'arial', 12, 'bold'), text="System Analysis", bd=7)
        self.lblSystemAnalysis.grid(row=4, column=0, sticky=W, padx=5, pady=5)
        self.cboSystemAnalysis = ttk.Combobox(
            SubjectFrame2, width=29, state='readonly')
        self.cboSystemAnalysis['values'] = (
            'Core unit', 'Yes', 'No', 'Completed')
        self.cboSystemAnalysis.current(0)
        self.cboSystemAnalysis.grid(row=4, column=1)

        self.lblDigitalGraphics = Label(SubjectFrame2, font=(
            'arial', 12, 'bold'), text="Digital Graphics", bd=7)
        self.lblDigitalGraphics.grid(row=5, column=0, sticky=W, padx=5, pady=5)
        self.cboDigitalGraphics = ttk.Combobox(
            SubjectFrame2, width=29, state='readonly')
        self.cboDigitalGraphics['values'] = (
            'Core unit', 'Yes', 'No', 'Completed')
        self.cboDigitalGraphics.current(0)
        self.cboDigitalGraphics.grid(row=5, column=1)

        # =============Parent of Guidance=============

        # StudentID
        self.lblStudensID = Label(GuidanceFrame, font=(
            'arial', 12, 'bold'), text="Parent or Guidance", bd=7)
        self.lblStudensID.grid(row=0, column=0, sticky=W, padx=5, pady=5)

        self.cboParentOrGuidance = ttk.Combobox(
            GuidanceFrame, width=40, state='readonly')
        self.cboParentOrGuidance['values'] = (
            '', 'Mother', 'Father', 'Brother', 'Sister')
        self.cboParentOrGuidance.current(0)
        self.cboParentOrGuidance.grid(row=0, column=1)

        # FirstName
        self.lblFirstName = Label(GuidanceFrame, font=(
            'arial', 12, 'bold'), text="First Name", bd=7)
        self.lblFirstName.grid(row=1, column=0, sticky=W, padx=5, pady=5)

        self.txtFirstName = Entry(GuidanceFrame, font=(
            'arial', 12, 'bold'), bd=5, width=29)
        self.txtFirstName.grid(row=1, column=1)

        # sureName
        self.lblSureName = Label(GuidanceFrame, font=(
            'arial', 12, 'bold'), text="Sure Name", bd=7)
        self.lblSureName.grid(row=2, column=0, sticky=W, padx=5, pady=5)

        self.txtSureName = Entry(GuidanceFrame, font=(
            'arial', 12, 'bold'), bd=5, width=29)
        self.txtSureName.grid(row=2, column=1)

        # NI Number
        self.lblNINumber = Label(GuidanceFrame, font=(
            'arial', 12, 'bold'), text="NI Number", bd=7)
        self.lblNINumber.grid(row=3, column=0, sticky=W, padx=5, pady=5)

        self.txtNINumber = Entry(GuidanceFrame, font=(
            'arial', 12, 'bold'), bd=5, width=29)
        self.txtNINumber.grid(row=3, column=1)

        # Address
        self.lblAddress = Label(GuidanceFrame, font=(
            'arial', 12, 'bold'), text="Address", bd=7)
        self.lblAddress.grid(row=4, column=0, sticky=W, padx=5, pady=5)

        self.txtAddress = Entry(GuidanceFrame, font=(
            'arial', 12, 'bold'), bd=5, width=29)
        self.txtAddress.grid(row=4, column=1)

        # gender
        self.lblGender = Label(GuidanceFrame, font=(
            'arial', 12, 'bold'), text="Gender", bd=7)
        self.lblGender.grid(row=5, column=0, sticky=W, padx=5, pady=5)
        self.cboGender = ttk.Combobox(
            GuidanceFrame, width=40, state='readonly')
        self.cboGender['values'] = ('', 'Female', 'Male')
        self.cboGender.current(0)
        self.cboGender.grid(row=5, column=1)

        # =============Buttons=============

        self.btnAddNew = Button(ButtonsFrame, width=9, height=2, text='Add New', pady=1, padx=24, bd=4, font=(
            'arial', 12, 'bold'))
        self.btnAddNew.grid(row=0, column=0)

        self.btnUpdate = Button(ButtonsFrame, width=9, height=2, text='Update', pady=1, padx=24, bd=4, font=(
            'arial', 12, 'bold'))
        self.btnUpdate.grid(row=1, column=0)

        self.btnReset = Button(ButtonsFrame, width=9, height=2, text='Reset', pady=1, padx=24, bd=4, font=(
            'arial', 12, 'bold'))
        self.btnReset.grid(row=2, column=0)

        self.btnDelete = Button(ButtonsFrame, width=9, height=2, text='Delete', pady=1, padx=24, bd=4, font=(
            'arial', 12, 'bold'))
        self.btnDelete.grid(row=3, column=0)

        self.btnExit = Button(ButtonsFrame, width=9, height=2, text='Exit', pady=1, padx=24, bd=4, font=(
            'arial', 12, 'bold'))
        self.btnExit.grid(row=4, column=0)


if __name__ == '__main__':
    root = Tk()
    application = School(root)
    root.mainloop()
