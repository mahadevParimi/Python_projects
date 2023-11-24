import  customtkinter as ctk
import serial
from PIL import Image,ImageTk

def lf_display_thrust(e):
    load_values()
    lf_dir.delete("0.0","end")
    lf_disp.delete("0.0","end")
    if mode_sel.get():
        send_values()
    lf_dir.insert("0.0",dir_check(int(lf_slider.get())))
    lf_disp.insert("0.0",int(lf_slider.get()))

def rf_display_thrust(e):
    load_values()
    rf_dir.delete("0.0","end")
    rf_disp.delete("0.0","end")
    if mode_sel.get():
        send_values()
    rf_dir.insert("0.0",dir_check(int(rf_slider.get())))
    rf_disp.insert("0.0",int(rf_slider.get()))

def lb_display_thrust(e):
    load_values()
    lb_dir.delete("0.0","end")
    lb_disp.delete("0.0","end")
    if mode_sel.get():
        send_values()
    lb_dir.insert("0.0",dir_check(int(lb_slider.get())))
    lb_disp.insert("0.0",int(lb_slider.get()))

def rb_display_thrust(e):
    load_values()
    rb_dir.delete("0.0","end")
    rb_disp.delete("0.0","end")
    if mode_sel.get():
        send_values()
    rb_dir.insert("0.0",dir_check(int(rb_slider.get())))
    rb_disp.insert("0.0",int(rb_slider.get()))

def display_thrust():
    lf_display_thrust(" ")
    rf_display_thrust(" ")
    lb_display_thrust(" ")
    rb_display_thrust(" ")
    
def load_values():
    lf_thrust = int(lf_slider.get())
    rf_thrust = int(rf_slider.get())
    lb_thrust = int(lb_slider.get())
    rb_thrust = int(rb_slider.get())
    cmd = f"{lf_thrust},{rf_thrust},{lb_thrust},{rb_thrust}"
    cmd_disp.delete("0.0","end")
    cmd_disp.insert("0.0",cmd)
    return cmd

def send_values():
    cmd = load_values()
    uno = serial.Serial(com_entry.get(),9600)
    uno.write(cmd.encode())
    print(cmd)

def stop_rov():
    value = 90
    lf_slider.set(value)
    rf_slider.set(value)
    lb_slider.set(value)
    rb_slider.set(value)
    yaw_slider.set(value)
    linear_slider.set(value)
    display_thrust()
    send_values()

def linear_slid_cmd(e):
    lb_slider.set(int(e))
    rb_slider.set(int(e))
    yaw_slider.set(90)
    
def yaw_slid_cmd(e):
    lb_slider.set(int(e))
    rb_slider.set(int(abs(180-e)))
    linear_slider.set(90)
    display_thrust()
    
def dir_check(val):
    if val == 90:
        msg = "stop"
    elif val > 90:
        msg = "cw"
    else:
        msg = "ccw"
    return msg

def linear_reset():
    lb_slider.set(90)
    rb_slider.set(90)
    linear_slider.set(90)
    display_thrust()

def yaw_reset():
    lb_slider.set(90)
    rb_slider.set(90)
    yaw_slider.set(90)
    display_thrust()

width,height= 540,760
ll,ul=180,0
refx,refy=70,80
gapx,gapy=300,300   
gapx1,gapy1=1,200
disp_w,disp_h=50,20
slider_w,slider_h = 25,450

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

window = ctk.CTk()
window.title("ROV CONTROLLER")
window.resizable(False,False)
window.geometry(f"{width}x{height}")

img_open =Image.open("pauvm_transparent_logo.png")
img_resize = img_open.resize((gapx,gapy))
img = ImageTk.PhotoImage(img_resize)
img_label = ctk.CTkLabel(window,image=img,text=" ")
img_label.place(x=refx+20,y=420)

com_entry = ctk.CTkEntry(window,placeholder_text="Enter com port ")
com_entry.insert(0,"/dev/tty.HC-05")
com_entry.place(x=refx+105,y=refy -50)

mode_sel = ctk.CTkSwitch(window,text="Auto")
mode_sel.place(x=refx+150,y=refy+210)

lf_slider = ctk.CTkSlider(window,from_=ll,to=ul,orientation=ctk.VERTICAL,command=lf_display_thrust,progress_color="orange",width=slider_w,height=slider_h//1.7)
lf_slider.place(x=refx,y=refy-10)
lf_slider.configure(number_of_steps=90)

lf_dir = ctk.CTkTextbox(window,width=disp_w,height=disp_h,activate_scrollbars=False)
lf_dir.place(x=refx-10,y=refy-50)

rf_slider = ctk.CTkSlider(window,from_=ll,to=ul,orientation=ctk.VERTICAL,command=rf_display_thrust,progress_color="orange",width=slider_w,height=slider_h//1.7)
rf_slider.place(x=refx+gapx,y=refy-10)
rf_slider.configure(number_of_steps=90)

rf_dir = ctk.CTkTextbox(window,width=disp_w,height=disp_h,activate_scrollbars=False)
rf_dir.place(x=refx+gapx-10,y=refy-50)

lb_slider = ctk.CTkSlider(window,from_=ll,to=ul,orientation=ctk.VERTICAL,command=lb_display_thrust,progress_color="orange",width=slider_w,height=slider_h//1.7)
lb_slider.place(x=refx,y=refy+gapy+20)
lb_slider.configure(number_of_steps=90)

lb_dir = ctk.CTkTextbox(window,width=disp_w,height=disp_h,activate_scrollbars=False)
lb_dir.place(x=refx-10,y=refy+270)

rb_slider = ctk.CTkSlider(window,from_=ll,to=ul,orientation=ctk.VERTICAL,command=rb_display_thrust,progress_color="orange",width=slider_w,height=slider_h//1.7)
rb_slider.place(x=refx+gapx,y=refy+gapy+20)
rb_slider.configure(number_of_steps=90)

rb_dir = ctk.CTkTextbox(window,width=disp_w,height=disp_h,activate_scrollbars=False)
rb_dir.place(x=refx+gapx-10,y=refy+270)

lf_disp = ctk.CTkTextbox(window,width=disp_w,height=disp_h,activate_scrollbars=False)
lf_disp.place(x=refx+120-20,y=refy+20)

rf_disp = ctk.CTkTextbox(window,width=disp_w,height=disp_h,activate_scrollbars=False)
rf_disp.place(x=refx+220-20,y=refy+20)

lb_disp = ctk.CTkTextbox(window,width=disp_w,height=disp_h,activate_scrollbars=False)
lb_disp.place(x=refx+120-20,y=refy+70)

rb_disp = ctk.CTkTextbox(window,width=disp_w,height=disp_h,activate_scrollbars=False)
rb_disp.place(x=refx+220-20,y=refy+70)

cmd_disp = ctk.CTkTextbox(window,width=3*disp_w,height=disp_h,activate_scrollbars=False)
cmd_disp.place(x=refx+100,y=refy+130)

send_btn = ctk.CTkButton(window,text="SEND",command=send_values,hover_color="green")
send_btn.place(x=refx+100,y=refy+250)

stop_btn = ctk.CTkButton(window,text="ROV STOP",command=stop_rov,hover_color="red")
stop_btn.place(x=refx+100,y=refy+300)

linear_slider = ctk.CTkSlider(window,from_=ll,to=ul,orientation=ctk.VERTICAL,progress_color="green",width=slider_w,height=slider_h*1.3,command=linear_slid_cmd)
linear_slider.place(x=refx+400,y=refy-40)

yaw_slider = ctk.CTkSlider(window,from_=ll,to=ul,orientation=ctk.HORIZONTAL,progress_color="green",width=slider_h+20,height=slider_w,command=yaw_slid_cmd)
yaw_slider.place(x=refx-50+10,y=refy+610)

left_label = ctk.CTkLabel(window,text="LEFT")
left_label.place(x=refx-50+10,y=refy+630)

right_label = ctk.CTkLabel(window,text="RIGHT")
right_label.place(x=refx+380+10,y=refy+630)

stop_label = ctk.CTkButton(window,text="⬆",fg_color="transparent",width=25,command=yaw_reset)
stop_label.place(x=refx-47-7+10+slider_h/2,y=refy+638)

front_label = ctk.CTkLabel(window,text="FRONT")
front_label.place(x=refy+390-10,y=refy-70)

back_label = ctk.CTkLabel(window,text="BACK",)
back_label.place(x=refy+390-10,y=refy+slider_h*1.3-40)

stop_label = ctk.CTkButton(window,text="⬅",fg_color="transparent",width=25,command=linear_reset)
stop_label.place(x=refy+375-10+53,y=refy+slider_h//2+14)

stop_rov()

window.mainloop()
