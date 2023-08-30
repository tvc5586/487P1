import PySimpleGUI as sg
from datetime import datetime
from datetime import time
import re

import SQL_Func

# ====================================================================================================================================================

sg.theme("default1") # Set GUI Theme

# ===================================================== Access Window =====================================================

def access():
    
    # =============================== Access Popup Window Elements ===============================
    
    layout_msg = [[sg.VPush()],
                  [sg.Text("Enter Your ID", size = (25, 1)), sg.In(size = (13, 1), key = "ID_Val")],
                  [sg.Button("Confirm", key = "yes"), sg.Button("Cancel", key = "no")],
                  [sg.VPush()]]
    
    # =============================== Access Popup Window Layout ===============================
    
    layout = [[sg.VPush()],
              [sg.Column(layout_msg, element_justification = "center", key = "-MSG-")],
              [sg.VPush()],]
    
    window = sg.Window("Access SUN Lab", layout, element_justification = "c")

    # =============================== Run the Event Loop ===============================
    
    while True:
    
        event, values = window.read(10)
        
        if event == "no" or event == "Exit" or event == sg.WIN_CLOSED:
            # Close Window
            window.close()
            
            # Return nothing
            return None, datetime.now()
            
        if event == "yes":
            # Close Window
            window.close()
            
            # Return ID and date
            if values['ID_val'][0] == '%' and values['ID_val'][1] == 'A': # If swipe card
              return values['ID_val'][2:12], datetime.now()
            
            else:
              return values['ID_Val'], datetime.now()
                
    
# ===================================================== Admin Window =====================================================

def admin():

    # =============================== Admin Popup Window Elements ===============================
    
    layout_msg = [[sg.VPush()],
                  [sg.Text("Enter Your ID", size = (25, 1)), sg.In(size = (13, 1), key = "ID_Val")],
                  [sg.Button("Confirm", key = "yes"), sg.Button("Cancel", key = "no")],
                  [sg.VPush()]]
    
    # =============================== Admin Popup Window Layout ===============================
    
    layout = [[sg.VPush()],
              [sg.Column(layout_msg, element_justification = "center", key = "-MSG-")],
              [sg.VPush()],]
    
    window = sg.Window("Check Admin ID", layout, element_justification = "c")

    # =============================== Run the Event Loop ===============================
    
    while True:
    
        event, values = window.read()
        
        if event == "no" or event == "Exit" or event == sg.WIN_CLOSED:
            # Close Window
            window.close()
            
            # Return nothing
            return None
            
        if event == "yes":
            # Close Window
            window.close()
        
            # Return ID
            if values['ID_val'][0] == '%' and values['ID_val'][1] == 'A': # If swipe card
              return values['ID_val'][2:12]
            
            else:
              return values['ID_Val']

# ===================================================== Filter Windows =====================================================

def date():
  
    # =============================== Date Popup Window Elements ===============================
    
    layout_msg = [[sg.VPush()],
                  [sg.Text("Enter Year", size = (25, 1)), sg.In(size = (13, 1), key = "Year_Val")],
                  [sg.Text("Enter Month", size = (25, 1)), sg.In(size = (13, 1), key = "Month_Val")],
                  [sg.Text("Enter Day", size = (25, 1)), sg.In(size = (13, 1), key = "Day_Val")],
                  [sg.Button("Confirm", key = "yes"), sg.Button("Cancel", key = "no")],
                  [sg.VPush()]]
    
    # =============================== Date Popup Window Layout ===============================
    
    layout = [[sg.VPush()],
              [sg.Column(layout_msg, element_justification = "center", key = "-MSG-")],
              [sg.VPush()],]
    
    window = sg.Window("Student ID", layout, element_justification = "c")

    # =============================== Run the Event Loop ===============================
    
    while True:
    
        event, values = window.read()
        
        if event == "no" or event == "Exit" or event == sg.WIN_CLOSED:
            # Close Window
            window.close()
            
            # Return nothing
            return None, None, None
            
        if event == "yes":
            # Close Window
            window.close()
        
            # Return ID
            return values['Year_Val'], values['Month_Val'], values['Day_Val']

def SID():

    # =============================== Student ID Popup Window Elements ===============================
    
    layout_msg = [[sg.VPush()],
                  [sg.Text("Enter Student ID", size = (25, 1)), sg.In(size = (13, 1), key = "ID_Val")],
                  [sg.Button("Confirm", key = "yes"), sg.Button("Cancel", key = "no")],
                  [sg.VPush()]]
    
    # =============================== Student Popup Window Layout ===============================
    
    layout = [[sg.VPush()],
              [sg.Column(layout_msg, element_justification = "center", key = "-MSG-")],
              [sg.VPush()],]
    
    window = sg.Window("Student ID", layout, element_justification = "c")

    # =============================== Run the Event Loop ===============================
    
    while True:
    
        event, values = window.read()
        
        if event == "no" or event == "Exit" or event == sg.WIN_CLOSED:
            # Close Window
            window.close()
            
            # Return nothing
            return None
            
        if event == "yes":
            # Close Window
            window.close()
        
            # Return ID
            return values['ID_Val']

def input_time():
    
    # =============================== Time Popup Window Elements ===============================
    
    layout_msg = [[sg.VPush()],
                  [sg.Text("Enter Start Hour", size = (20, 1)), sg.In(size = (13, 1), key = "h1_Val"),
                   sg.Text("Enter Start Min", size = (20, 1)), sg.In(size = (13, 1), key = "min1_Val"),
                   sg.Text("Enter Start Sec", size = (20, 1)), sg.In(size = (13, 1), key = "sec1_Val")],
                  [sg.Text("Enter End Hour", size = (20, 1)), sg.In(size = (13, 1), key = "h2_Val"),
                   sg.Text("Enter End Min", size = (20, 1)), sg.In(size = (13, 1), key = "min2_Val"),
                   sg.Text("Enter End Sec", size = (20, 1)), sg.In(size = (13, 1), key = "sec2_Val")],
                  [sg.Button("Confirm", key = "yes"), sg.Button("Cancel", key = "no")],
                  [sg.VPush()]]
    
    # =============================== Time Popup Window Layout ===============================
    
    layout = [[sg.VPush()],
              [sg.Column(layout_msg, element_justification = "center", key = "-MSG-")],
              [sg.VPush()],]
    
    window = sg.Window("Student ID", layout, element_justification = "c")

    # =============================== Run the Event Loop ===============================
    
    while True:
    
        event, values = window.read()
        
        if event == "no" or event == "Exit" or event == sg.WIN_CLOSED:
            # Close Window
            window.close()
            
            # Return nothing
            return None, None, None, None, None, None
            
        if event == "yes":
            # Close Window
            window.close()
        
            # Return ID
            return values['h1_Val'], values['min1_Val'], values['sec1_Val'], values['h2_Val'], values['min2_Val'], values['sec2_Val']

# ===================================================== User ID Window =====================================================

def uid():

    # =============================== Popup Window Elements ===============================
    
    layout_msg = [[sg.VPush()],
                  [sg.Text("Enter User ID", size = (25, 1)), sg.In(size = (13, 1), key = "ID_Val")],
                  [sg.Button("Confirm", key = "yes"), sg.Button("Cancel", key = "no")],
                  [sg.VPush()]]
    
    # =============================== Popup Window Layout ===============================
    
    layout = [[sg.VPush()],
              [sg.Column(layout_msg, element_justification = "center", key = "-MSG-")],
              [sg.VPush()],]
    
    window = sg.Window("Enter ID", layout, element_justification = "c")

    # =============================== Run the Event Loop ===============================
    
    while True:
    
        event, values = window.read()
        
        if event == "no" or event == "Exit" or event == sg.WIN_CLOSED:
            # Close Window
            window.close()
            
            # Return nothing
            return None
            
        if event == "yes":
            # Close Window
            window.close()
        
            # Return ID
            return values['ID_Val']

# ===================================================== Main Page =====================================================
   
def main():
      
    # =============================== SQL function code ===============================  
      
    SQL = SQL_Func.functions("root", "040147", "P1")  
      
    # =============================== History Panel Elements ===============================
    
    history = [[sg.Button("Student", size = (7, 1), key = "student"),
                sg.Button("By date", size = (7, 1), key = "date"),
                sg.Button("By ID", size = (7, 1), key = "ID"),
                sg.Button("By time", size = (7, 1), key = "time"),],
               [sg.Listbox(values=[], enable_events = True, size = (50, 28), key = "-HISTORY LIST-")],]
               
    # =============================== Users Panel Elements ===============================
      
    users = [[sg.Button("Activate", size = (10, 1), key = "activate"),
              sg.Button("Suspend", size = (10, 1), key = "suspend"),],
             [sg.Listbox(values=[], enable_events = True, size = (50, 26), key = "-USERS LIST-")],]
      
    # =============================== Admin Mode Elements ===============================
                         
    admin_button = [[sg.VPush()],
                      [sg.Button("History", size = (15, 1), key = "history_button")],
                      [sg.Button("Users", size = (15, 1), key = "users_button")],
                      [sg.VPush()]]

    # =============================== Main Layouts ===============================
         
    empty_layout = []     
                                 
    admin_mode_layout = [[sg.VPush()],
                          [sg.Text("Admin Menu", font = ("Arial", 14), key = "subtitle")],
                          [sg.HorizontalSeparator(color = "black")],
                          [sg.Column(admin_button, size = (150, 435)),
                           sg.VSeparator(color = "black"),
                           sg.Column(history, size = (470, 435), pad = ((0, 0),(10, 0)), visible = True, key = "history"),
                           sg.Column(users, size = (470, 435), pad = ((0, 0),(10, 0)), visible = False, key = "users"),],
                          [sg.VPush()]]
    
    main_layout = [[sg.Text("Main Menu", font = ("Arial", 15))],
                   [sg.Button("Access", size = (15, 2), key = "Access")],
                   [sg.Button("Admin", size = (15, 2), key = "Admin")],
                   [sg.Exit(size = (15, 2))]]
                   
    layout = [[sg.VPush()],
              [sg.Text("SUN Lab Access and Management", font = ("Arial", 20))],
              [sg.Text(" ", font = ("Arial", 12), key = "admin_menu")],
              [sg.HorizontalSeparator(color = "black")],
              [sg.Column(main_layout, size = (150, 490), element_justification = "center", key = "-ML-"),
               sg.VSeparator(color = "black"),
               sg.Column(empty_layout, size = (620, 490), visible = True, element_justification = "left", key = "-EL-"),
               sg.Column(admin_mode_layout, size = (620, 490), visible = False, element_justification = "left", key = "-DML-"),],
              [sg.HorizontalSeparator(color = "black")],
              [sg.VPush()],]
              
    window = sg.Window("SUN Lab Access", layout, 
                       size = (770, 665), 
                       resizable = False, 
                       enable_close_attempted_event = True, 
                       element_justification = "center").finalize()
        
    # =============================== Run the Event Loop ===============================
    
    while True:
    
        event, values = window.read()
    
        # =============================== Main Menu Functions ===============================
    
        if ((event == "Exit" or event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT) and 
             sg.PopupOKCancel('Are you sure to exit the program?', title = "Exit")) == "OK":
            # Quit program
            break
            
        # =============================== Access Menu Functions ===============================
                    
        elif event == "Access":
            # Change subtitle
            window['admin_menu'].update(" ")
        
            # Switch Layout
            window['-EL-'].update(visible = True)
            window['-DML-'].update(visible = False)
                    
            try:
                ID, Time = access() # Get ID and Timestamp
            
                # If user entered ID
                if ID != None:
                
                    check = SQL.add_to_history(ID, Time) # Insert ID and entry time
                   
                    # If authorized user 
                    if check:
                      sg.popup("Access granted!", title = "Success")
                
                    else:
                      sg.popup("Access denied!", title = "Notice")
                
            except Exception as e: 
                sg.popup("Invalid value!", title = "Error")
                    
        # =============================== Admin Menu Functions ===============================
        
        elif event == "Admin":              
            try:
                ID = admin() # Get Admin ID
                
                # If user entered ID
                if ID != None: 
                
                    # Check ID
                    check = SQL.check_admin(ID) 
                    
                    # If user is an Admin
                    if check:
                        # Switch Layout
                        window['-EL-'].update(visible = False)
                        window['-DML-'].update(visible = True)
                        window['history'].update(visible = True)
                        window['users'].update(visible = False)
                        
                        # Change subtitle
                        window['admin_menu'].update("Admin Menu")
                        window['subtitle'].update("History View")
                        
                        # Show entry history
                        window["-HISTORY LIST-"].update(SQL.show_history())
                        
                    else:
                        sg.popup("Access denied!", title = "Notice")
                
            except Exception as e: 
                sg.popup("Invalid value!", title = "Error")
        
        # =============================== History Sub-Menu Functions ===============================
        
        elif event == "history_button":
            # Change subtitle
            window['subtitle'].update("History View")
            
            # Switch Layout
            window['history'].update(visible = True)
            window['users'].update(visible = False)
            
            # Show entry history
            window["-HISTORY LIST-"].update(SQL.show_history())
            
        elif event == "student":
            # Show student-only history
            window["-HISTORY LIST-"].update(SQL.show_student_only())
        
        elif event == "date":
            try:
                year, month, day = date() # Get date
                
                # Check if date is in correct format   
                Date = re.split('-', re.split('\s+', str(datetime(int(year), int(month), int(day))))[0])
                                
                # Filter by date
                result = SQL.show_history_by_date(Date)
                    
                if result:
                    # Show entry history
                    window["-HISTORY LIST-"].update(result)
                        
                else:
                    sg.popup("No entry!", title = "Notice")
                
            except Exception as e: 
                sg.popup("Invalid value!", title = "Error")
            
        elif event == "ID":
            try:
                ID = SID() # Get Student ID
                
                # If user entered ID
                if ID != None: 
                
                    # Filter out ID not belong to student
                    result = SQL.show_student_match(ID)
                    
                    if result:
                        # Show entry history
                        window["-HISTORY LIST-"].update(result)
                        
                    else:
                        sg.popup("ID does not belong to a student!", title = "Notice")
                
            except Exception as e: 
                sg.popup("Invalid value!", title = "Error")
        
        elif event == "time":
            try:
                h1, min1, sec1, h2, min2, sec2 = input_time() # Get start time and end time
                
                # Check if time is in correct format   
                sTime = time(int(h1), int(min1), int(sec1))
                eTime = time(int(h2), int(min2), int(sec2))
                                
                # Filter by date
                result = SQL.show_history_by_time(sTime, eTime)
                    
                if result:
                    # Show entry history
                    window["-HISTORY LIST-"].update(result)
                        
                else:
                    sg.popup("No entry!", title = "Notice")
                
            except Exception as e: 
                sg.popup("Invalid value!", title = "Error")
            
        # =============================== Users Sub-Menu Functions ===============================
        
        elif event == "users_button":
            # Change subtitle
            window['subtitle'].update("User View")
            
            # Switch Layout
            window['history'].update(visible = False)
            window['users'].update(visible = True)
        
            # Show list of users
            window["-USERS LIST-"].update(SQL.show_user())
            
        elif event == "activate":
            # Activate ID
            
            try:
                ID = uid() # Get Admin ID
                
                # If user entered ID
                if ID != None: 
                
                    # Check ID
                    check = SQL.activate(ID) 
                    
                    # If user is an Admin
                    if check == 1:
                        sg.popup("ID activated!", title = "Success")
                        
                        # Show list of users
                        window["-USERS LIST-"].update(SQL.show_user())
                        
                    elif check == 2:
                        sg.popup("ID does not exist!", title = "Notice")
                    
                    else:
                        sg.popup("ID is already active!", title = "Notice")
                
            except Exception as e: 
                sg.popup("Invalid value!", title = "Error")
        
        elif event == "suspend":
            # Suspend ID
            
            try:
                ID = uid() # Get Admin ID
                
                # If user entered ID
                if ID != None: 
                
                    # Check ID
                    check = SQL.suspend(ID) 
                    
                    # If user is an Admin
                    if check == 1:
                        sg.popup("ID suspended!", title = "Success")
                        
                        # Show list of users
                        window["-USERS LIST-"].update(SQL.show_user())
                    
                    elif check == 2:
                        sg.popup("ID does not exist!", title = "Notice")
                        
                    else:
                        sg.popup("ID is already suspended!", title = "Notice")
                
            except Exception as e: 
                sg.popup("Invalid value!", title = "Error")
        
        # =============================== Mode Functions End ===============================
        
    # Close Window
    window.close()

# ====================================================================================================================================================

if __name__ == "__main__":
    main()

